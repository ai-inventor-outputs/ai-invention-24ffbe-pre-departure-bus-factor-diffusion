#!/usr/bin/env python3
"""Clone one repo and extract everything needed for a single dataset row:
per-commit (author, date, files) table, yearly DOA/TF, founder/TFDD detection,
pre/post-TFDD windows, survival label. Designed to be called by a worker process
per repo (see run_mining.py) so failures/timeouts are isolated per-repo.
"""
from __future__ import annotations

import math
import shutil
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

CLONE_TIMEOUT_S = 180
LOG_TIMEOUT_S = 120
MAX_COMMITS = 60000  # skip pathologically large histories to respect time budget
SILENCE_YEARS = 1.0  # Avelino et al. abandonment threshold
COVERAGE_THRESHOLD = 0.5  # TF greedy-removal stopping coverage


def run(cmd, cwd=None, timeout=None):
    return subprocess.run(cmd, cwd=cwd, timeout=timeout, capture_output=True, text=True,
                           errors="replace")


def clone_repo(clone_url: str, dest: Path) -> tuple[bool, str]:
    """Partial clone (blob:none) -> full commit graph + tree diffs, no blob content."""
    if dest.exists():
        shutil.rmtree(dest, ignore_errors=True)
    dest.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["git", "clone", "--filter=blob:none", "--no-checkout", "--quiet", clone_url, str(dest)]
    try:
        r = run(cmd, timeout=CLONE_TIMEOUT_S)
    except subprocess.TimeoutExpired:
        return False, "clone_timeout"
    if r.returncode != 0:
        return False, f"clone_failed: {r.stderr[:300]}"
    return True, "ok"


def get_commit_log(repo_dir: Path) -> tuple[list[dict], str]:
    """Full commit history: hash, author email, author date (ISO), files changed."""
    fmt = "%x02%H%x03%ae%x03%an%x03%aI"
    cmd = ["git", "log", "--all", "--no-renames", "--name-only", f"--pretty=format:{fmt}"]
    try:
        r = run(cmd, cwd=repo_dir, timeout=LOG_TIMEOUT_S)
    except subprocess.TimeoutExpired:
        return [], "log_timeout"
    if r.returncode != 0:
        return [], f"log_failed: {r.stderr[:300]}"
    commits = []
    blocks = r.stdout.split("\x02")
    for block in blocks:
        block = block.strip("\n")
        if not block:
            continue
        parts = block.split("\x03", 3)
        if len(parts) < 4:
            continue
        chash, aemail, aname, adate = parts
        rest = parts[3]
        lines = rest.split("\n")
        date_str = lines[0]
        files = [f for f in lines[1:] if f.strip()]
        try:
            dt = datetime.fromisoformat(date_str)
        except ValueError:
            continue
        commits.append({
            "hash": chash,
            "author_email": aemail.lower().strip(),
            "author_name": aname.strip(),
            "date": dt.astimezone(timezone.utc).isoformat(),
            "files": files,
        })
    commits.sort(key=lambda c: c["date"])
    if len(commits) > MAX_COMMITS:
        return commits, "too_large"
    return commits, "ok"


def resolve_developer_id(commits: list[dict]) -> dict:
    """Map author_email -> a stable developer id (email is already the identity key;
    fall back to normalized name when email is a noreply/placeholder)."""
    dev_of = {}
    for c in commits:
        email = c["author_email"]
        if not email or "noreply" in email or email in ("none", "unknown"):
            key = f"name:{c['author_name'].lower().strip()}"
        else:
            key = f"mail:{email}"
        dev_of[c["hash"]] = key
    return dev_of


def compute_doa(commits: list[dict], dev_of: dict, up_to_date: datetime) -> dict:
    """Avelino et al. (ICPC 2016) DOA:
    DOA(d,f) = 3.293 + 1.098*FA(d,f) + 0.164*DL(d,f) - 0.321*ln(1+AC(d,f))
    Computed using all commits with date <= up_to_date."""
    first_author = {}  # file -> dev
    delivered = defaultdict(lambda: defaultdict(int))  # file -> dev -> count
    total_changes = defaultdict(int)  # file -> total change count (any dev)
    for c in commits:
        if c["date"] > up_to_date.isoformat():
            continue
        dev = dev_of[c["hash"]]
        for f in c["files"]:
            if f not in first_author:
                first_author[f] = dev
            delivered[f][dev] += 1
            total_changes[f] += 1

    doa = defaultdict(dict)  # file -> dev -> raw doa
    for f, dev_counts in delivered.items():
        for dev, dl in dev_counts.items():
            fa = 1 if first_author.get(f) == dev else 0
            ac = total_changes[f] - dl
            val = 3.293 + 1.098 * fa + 0.164 * dl - 0.321 * math.log(1 + ac)
            doa[f][dev] = val
    return doa


def truck_factor(doa: dict) -> tuple[int, list[str], dict]:
    """Greedy TF algorithm (Avelino et al. Algorithm 1): main author of a file =
    highest-DOA dev for that file; remove top author (most files authored) while
    coverage of remaining authors' files >= 0.5; TF = number removed."""
    total_files = len(doa)
    if total_files == 0:
        return 0, [], {}
    main_author_of = {f: max(devs, key=devs.get) for f, devs in doa.items() if devs}
    files_by_author = defaultdict(set)
    for f, dev in main_author_of.items():
        files_by_author[dev].add(f)

    remaining_files = set(main_author_of.keys())
    remaining_authors = dict(files_by_author)
    tf = 0
    removed = []
    while remaining_authors:
        coverage = len(remaining_files) / total_files
        if coverage < COVERAGE_THRESHOLD:
            break
        top_author = max(remaining_authors, key=lambda a: len(remaining_authors[a]))
        removed.append(top_author)
        tf += 1
        remaining_files -= remaining_authors[top_author]
        del remaining_authors[top_author]
    return tf, removed, files_by_author


def last_commit_date_of(commits: list[dict], dev_of: dict, dev: str) -> str | None:
    for c in reversed(commits):
        if dev_of[c["hash"]] == dev:
            return c["date"]
    return None


def yearly_snapshots(commits: list[dict]) -> list[datetime]:
    if not commits:
        return []
    start = datetime.fromisoformat(commits[0]["date"])
    end = datetime.fromisoformat(commits[-1]["date"])
    snaps = []
    y = start.year
    while True:
        d = datetime(y, 12, 31, tzinfo=timezone.utc)
        if d > end:
            break
        snaps.append(d)
        y += 1
    return snaps


def monthly_activity(commits: list[dict], from_dt: datetime, months: int) -> list[int]:
    counts = [0] * months
    for c in commits:
        dt = datetime.fromisoformat(c["date"])
        if dt < from_dt:
            continue
        delta_months = (dt.year - from_dt.year) * 12 + (dt.month - from_dt.month)
        if 0 <= delta_months < months:
            counts[delta_months] += 1
    return counts


def mine(full_name: str, clone_url: str, repo_dir: Path, meta: dict) -> dict:
    result = {"full_name": full_name, "status": "discarded", "discard_reason": None}

    ok, msg = clone_repo(clone_url, repo_dir)
    if not ok:
        result["discard_reason"] = f"clone_failure:{msg}"
        return result

    commits, msg = get_commit_log(repo_dir)
    shutil.rmtree(repo_dir, ignore_errors=True)  # free disk immediately
    if msg == "log_timeout" or msg.startswith("log_failed"):
        result["discard_reason"] = f"log_failure:{msg}"
        return result
    if msg == "too_large":
        result["discard_reason"] = "too_large_history"
        return result
    if len(commits) < 100:
        result["discard_reason"] = "too_few_commits"
        return result

    dev_of = resolve_developer_id(commits)
    n_devs = len(set(dev_of.values()))
    if n_devs < 2:
        result["discard_reason"] = "single_developer_only"
        return result

    # ---- mining-artifact filter: migration/squash signal (>50% files added in <20 commits) ----
    first_touch_commit_idx = {}
    for i, c in enumerate(commits):
        for f in c["files"]:
            if f not in first_touch_commit_idx:
                first_touch_commit_idx[f] = i
    n_files_total = len(first_touch_commit_idx)
    if n_files_total == 0:
        result["discard_reason"] = "no_files"
        return result
    added_early = sum(1 for idx in first_touch_commit_idx.values() if idx < 20)
    if n_files_total > 0 and added_early / n_files_total > 0.5 and len(commits) >= 20:
        result["discard_reason"] = "mining_artifact_migration_squash"
        return result

    # ---- code-file fraction (drop docs/awesome-list-only repos) ----
    code_ext = {".py", ".js", ".ts", ".jsx", ".tsx", ".go", ".rs", ".java", ".rb", ".c", ".cpp",
                ".h", ".hpp", ".cs", ".php", ".scala", ".kt", ".swift", ".m", ".mm", ".sh", ".ex",
                ".exs", ".erl", ".clj", ".hs", ".lua", ".r", ".jl", ".dart", ".vue"}
    code_files = sum(1 for f in first_touch_commit_idx if Path(f).suffix.lower() in code_ext)
    if code_files / n_files_total < 0.2:
        result["discard_reason"] = "non_software_repo_low_code_fraction"
        return result

    repo_start = datetime.fromisoformat(commits[0]["date"])
    repo_end = datetime.fromisoformat(commits[-1]["date"])
    span_years = (repo_end - repo_start).days / 365.25

    # ---- founder identity: earliest committer w/ dominant early authorship share ----
    early_window = commits[:max(50, len(commits) // 20)]
    early_counts = defaultdict(int)
    for c in early_window:
        early_counts[dev_of[c["hash"]]] += 1
    founder = max(early_counts, key=early_counts.get)
    founder_early_share = early_counts[founder] / len(early_window)

    # ---- yearly DOA / TF tables ----
    snaps = yearly_snapshots(commits)
    yearly_tables = []
    for snap in snaps:
        doa = compute_doa(commits, dev_of, snap)
        tf, tf_devs, files_by_author = truck_factor(doa)
        yearly_tables.append({
            "year": snap.year,
            "truck_factor": tf,
            "tf_developers": tf_devs,
            "n_files": len(doa),
            "n_active_authors_in_doa": len(files_by_author),
        })

    # ---- TFDD detection: walk yearly TF sets forward, require TF==1 (founder-only) at TFDD ----
    tfdd = None
    for entry in yearly_tables:
        tf_devs = entry["tf_developers"]
        if len(tf_devs) != 1:
            continue
        dev = tf_devs[0]
        last_commit = last_commit_date_of(commits, dev_of, dev)
        if last_commit is None:
            continue
        snap_dt = datetime(entry["year"], 12, 31, tzinfo=timezone.utc)
        last_dt = datetime.fromisoformat(last_commit)
        silence_years = (snap_dt - last_dt).days / 365.25
        if silence_years >= SILENCE_YEARS and dev == founder:
            tfdd = {"year": entry["year"], "date": snap_dt.isoformat(), "developer": dev,
                    "last_commit_date": last_commit, "silence_years": round(silence_years, 2)}
            break

    if tfdd is None:
        result["discard_reason"] = "no_qualifying_founder_only_tfdd"
        result["yearly_tables_preview_years"] = [e["year"] for e in yearly_tables]
        return result

    tfdd_dt = datetime.fromisoformat(tfdd["date"])
    years_after = (repo_end - tfdd_dt).days / 365.25
    if years_after < 3.0:
        result["discard_reason"] = "right_censored_insufficient_post_tfdd_history"
        result["years_after_tfdd"] = round(years_after, 2)
        return result

    # ---- fork independent-history check ----
    # (real fork-detection needs the API 'fork' flag; caller filters fork:false already,
    #  but guard on implausible truncation too: first commit far later than repo creation
    #  relative to claimed age is handled via meta['created_at'] check by the caller)

    # ---- pre-TFDD window (6-12mo before) ----
    pre_end = tfdd_dt
    pre_start = tfdd_dt.replace(year=tfdd_dt.year - 1)
    pre_commits = [c for c in commits if pre_start.isoformat() <= c["date"] < pre_end.isoformat()]
    founder_commits_pre = sum(1 for c in pre_commits if dev_of[c["hash"]] == founder)
    founder_share_pre = founder_commits_pre / len(pre_commits) if pre_commits else None

    doa_pre = compute_doa(commits, dev_of, pre_end)
    primary_owner_of = defaultdict(set)  # dev -> files where it's the top DOA-owner
    for f, devs in doa_pre.items():
        top = max(devs, key=devs.get)
        primary_owner_of[top].add(f)
    non_founder_new_owners = sum(1 for dev, files in primary_owner_of.items()
                                  if dev != founder and len(files) >= 1)

    # ---- post-TFDD monthly series + survival label ----
    post_months = monthly_activity(commits, tfdd_dt, 18)
    later_tf_entries = [e for e in yearly_tables if e["year"] > tfdd["year"]]
    survived = False
    for e in later_tf_entries:
        tf_devs = e["tf_developers"]
        if any(d != founder for d in tf_devs):
            snap_dt = datetime(e["year"], 12, 31, tzinfo=timezone.utc)
            months_since = (snap_dt.year - tfdd_dt.year) * 12 + (snap_dt.month - tfdd_dt.month)
            if months_since >= 6:
                new_dev_last = max(
                    (last_commit_date_of(commits, dev_of, d) or "" for d in tf_devs if d != founder),
                    default="",
                )
                if new_dev_last:
                    survived = True
                    break
    total_post = sum(post_months)
    avg_monthly_post = total_post / 18
    if not survived:
        bucket = "dead" if total_post == 0 else "dormant"
    else:
        bucket = "thriving" if avg_monthly_post >= 5 else "maintained"

    result.update({
        "status": "qualified",
        "discard_reason": None,
        "meta": {
            "stars": meta.get("stars"), "forks": meta.get("forks"),
            "language": meta.get("language"), "license": meta.get("license"),
            "created_at": meta.get("created_at"), "html_url": meta.get("html_url"),
        },
        "n_commits": len(commits), "n_developers": n_devs, "n_files": n_files_total,
        "repo_first_commit": commits[0]["date"], "repo_last_commit": commits[-1]["date"],
        "history_span_years": round(span_years, 2),
        "founder": founder, "founder_early_authorship_share": round(founder_early_share, 3),
        "yearly_tables": yearly_tables,
        "tfdd": tfdd,
        "pre_tfdd_window": {
            "window_start": pre_start.isoformat(), "window_end": pre_end.isoformat(),
            "founder_commit_share": round(founder_share_pre, 3) if founder_share_pre is not None else None,
            "n_pre_window_commits": len(pre_commits),
            "n_distinct_new_primary_owners": non_founder_new_owners,
        },
        "tfdd_snapshot_covariates": {
            "stars": meta.get("stars"), "forks": meta.get("forks"),
            "total_contributors": n_devs, "language": meta.get("language"),
            "license": meta.get("license"),
            "project_age_days": (tfdd_dt - datetime.fromisoformat(
                meta["created_at"].replace("Z", "+00:00"))).days if meta.get("created_at") else None,
        },
        "post_tfdd_monthly_commits": post_months,
        "post_tfdd_months_available": 18,
        "years_after_tfdd": round(years_after, 2),
        "survival_label": "Active_survived" if survived else "Inactive_did_not_survive",
        "activity_bucket": bucket,
    })
    return result


def main():
    import json
    full_name, clone_url, meta_json, out_path, workdir = sys.argv[1:6]
    meta = json.loads(meta_json)
    repo_dir = Path(workdir) / full_name.replace("/", "__")
    try:
        result = mine(full_name, clone_url, repo_dir, meta)
    except Exception as e:  # noqa: BLE001 - isolate per-repo failures
        result = {"full_name": full_name, "status": "discarded", "discard_reason": f"exception:{e}"}
    finally:
        shutil.rmtree(repo_dir, ignore_errors=True)
    Path(out_path).write_text(json.dumps(result))


if __name__ == "__main__":
    main()
