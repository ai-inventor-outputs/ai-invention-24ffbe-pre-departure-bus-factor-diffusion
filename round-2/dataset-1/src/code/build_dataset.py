"""
Build the LIVENESS_NON_CONDITIONED companion corpus to iter_1's
github_founder_departure_commits dataset.

Schema-compatible superset: identical repo_metadata / founder_signal /
commits[] structure as iter_1, PLUS two new per-repo fields required by the
gen_plan for this artifact:
  - sampling_frame: 'liveness_non_conditioned' (this corpus) or
    'liveness_conditioned' (iter_1's corpus, carried forward unmodified for
    direct comparison -- see merge_with_iter1() below)
  - frame_construction_method: how the candidate was discovered, e.g.
    'github_search_archived_or_stale_created_range' (see find_candidates.py)
    or 'currently_prominent_handcurated' (iter_1's method, backfilled)

CRITICAL DIFFERENCE from iter_1's build_dataset.py: fetch_repo_meta() here
does NOT reject archived repos and does NOT apply a MIN_STARS floor -- both
of those filters are exactly the "is this still famous/alive today"
conditioning this corpus exists to avoid. The only quality filters kept are
non-liveness ones: not a fork, and enough historical commit span to run the
DOA/Truck-Factor algorithm (MIN_HISTORY_YEARS).
"""
import json
import os
import subprocess
import sys
import time
import shutil
from collections import defaultdict
from datetime import datetime, timezone

import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CANDIDATES_PATH = f"{ROOT}/temp/non_conditioned_candidates.json"
CLONE_DIR = f"{ROOT}/temp/clones"
CKPT_PATH = f"{ROOT}/temp/checkpoint.json"
LOG_PATH = f"{ROOT}/logs/build.log"
MAX_COMMITS_PER_REPO = 5000
MIN_HISTORY_YEARS = 3.0  # per gen_plan: >=3y post-founder-TFDD history needed for the 18mo survival window

API = "https://api.github.com"
SESSION = requests.Session()
SESSION.headers.update({"Accept": "application/vnd.github+json", "User-Agent": "aii-research-corpus/1.0"})


def log(msg):
    line = f"[{datetime.now(timezone.utc).isoformat()}] {msg}"
    print(line, flush=True)
    with open(LOG_PATH, "a") as f:
        f.write(line + "\n")


def load_ckpt():
    if os.path.exists(CKPT_PATH):
        with open(CKPT_PATH) as f:
            return json.load(f)
    return {"done": {}, "skipped": {}}


def save_ckpt(ckpt):
    tmp = CKPT_PATH + ".tmp"
    with open(tmp, "w") as f:
        json.dump(ckpt, f)
    os.replace(tmp, CKPT_PATH)


def api_get(path, params=None):
    while True:
        r = SESSION.get(f"{API}{path}", params=params, timeout=30)
        if r.status_code == 403 and "rate limit" in r.text.lower():
            reset = int(r.headers.get("X-RateLimit-Reset", time.time() + 60))
            wait = max(reset - time.time(), 5) + 2
            log(f"rate limited on {path}; sleeping {wait:.0f}s")
            time.sleep(wait)
            continue
        remaining = r.headers.get("X-RateLimit-Remaining")
        if remaining is not None and int(remaining) <= 1:
            reset = int(r.headers.get("X-RateLimit-Reset", time.time() + 60))
            wait = max(reset - time.time(), 5) + 2
            log(f"remaining<=1 after {path}; sleeping {wait:.0f}s")
            time.sleep(wait)
        return r


def fetch_repo_meta(full_name, discovery):
    r = api_get(f"/repos/{full_name}")
    if r.status_code != 200:
        return None, f"http_{r.status_code}"
    d = r.json()
    if d.get("fork"):
        return None, "is_fork"
    # NOTE: deliberately NO archived-rejection and NO star floor here -- see module docstring.
    readme_excerpt = None
    r2 = api_get(f"/repos/{full_name}/readme")
    if r2.status_code == 200:
        import base64
        try:
            content = base64.b64decode(r2.json().get("content", "")).decode("utf-8", errors="ignore")
            readme_excerpt = content[:1500]
        except Exception:
            pass
    meta = {
        "full_name": d["full_name"],
        "stars": d.get("stargazers_count"),
        "forks": d.get("forks_count"),
        "language": d.get("language"),
        "license": (d.get("license") or {}).get("spdx_id"),
        "created_at": d.get("created_at"),
        "pushed_at": d.get("pushed_at"),
        "default_branch": d.get("default_branch"),
        "open_issues": d.get("open_issues_count"),
        "archived": d.get("archived"),
        "readme_excerpt": readme_excerpt,
    }
    return meta, None


def clone_repo(full_name):
    dest = os.path.join(CLONE_DIR, full_name.replace("/", "__"))
    if os.path.isdir(dest):
        shutil.rmtree(dest, ignore_errors=True)
    url = f"https://github.com/{full_name}.git"
    try:
        subprocess.run(
            ["git", "clone", "--bare", "--quiet", url, dest],
            check=True, timeout=900, capture_output=True,
        )
    except subprocess.CalledProcessError as e:
        log(f"clone failed {full_name}: {e.stderr.decode(errors='ignore')[:300]}")
        return None
    except subprocess.TimeoutExpired:
        log(f"clone timeout {full_name}")
        return None
    return dest


SEP = "\x1f"
REC_SEP = "\x1e"


def parse_commit_log(clone_path):
    fmt = f"{REC_SEP}%H{SEP}%ae{SEP}%an{SEP}%aI"
    cmd = ["git", "-C", clone_path, "log", f"--pretty=format:{fmt}", "--numstat", "--no-renames"]
    try:
        out = subprocess.run(cmd, check=True, timeout=300, capture_output=True, text=True).stdout
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        log(f"git log failed for {clone_path}: {e}")
        return []
    commits = []
    for block in out.split(REC_SEP):
        block = block.strip("\n")
        if not block:
            continue
        lines = block.split("\n")
        header = lines[0].split(SEP)
        if len(header) != 4:
            continue
        sha, email, name, date = header
        files = []
        for line in lines[1:]:
            if not line.strip():
                continue
            parts = line.split("\t")
            if len(parts) != 3:
                continue
            ins, dele, path = parts
            ins = 0 if ins == "-" else int(ins)
            dele = 0 if dele == "-" else int(dele)
            files.append({"path": path, "insertions": ins, "deletions": dele})
        commits.append({"sha": sha, "author_email": email, "author_name": name, "date": date, "files": files})
    return commits


def year1_author_share(commits):
    if not commits:
        return None, None
    dated = sorted(commits, key=lambda c: c["date"])
    t0 = datetime.fromisoformat(dated[0]["date"])
    cutoff = t0.replace(year=t0.year + 1) if t0.month != 2 or t0.day != 29 else t0.replace(year=t0.year + 1, day=28)
    year1 = [c for c in dated if datetime.fromisoformat(c["date"]) <= cutoff]
    if not year1:
        return None, None
    counts = defaultdict(int)
    for c in year1:
        counts[c["author_email"]] += 1
    top_email, top_n = max(counts.items(), key=lambda kv: kv[1])
    return top_n / len(year1), top_email


def history_years(commits):
    if not commits:
        return 0.0
    dates = sorted(datetime.fromisoformat(c["date"]) for c in commits)
    return (dates[-1] - dates[0]).days / 365.25


def process_repo(full_name, discovery, ckpt):
    if full_name in ckpt["done"] or full_name in ckpt["skipped"]:
        return
    log(f"processing {full_name}")
    meta, skip_reason = fetch_repo_meta(full_name, discovery)
    if meta is None:
        ckpt["skipped"][full_name] = skip_reason
        save_ckpt(ckpt)
        return
    clone_path = clone_repo(full_name)
    if clone_path is None:
        ckpt["skipped"][full_name] = "clone_failed"
        save_ckpt(ckpt)
        return
    commits = parse_commit_log(clone_path)
    shutil.rmtree(clone_path, ignore_errors=True)
    if not commits:
        ckpt["skipped"][full_name] = "no_commits"
        save_ckpt(ckpt)
        return
    hist_years = history_years(commits)
    if hist_years < MIN_HISTORY_YEARS:
        ckpt["skipped"][full_name] = f"insufficient_history_{hist_years:.2f}y"
        save_ckpt(ckpt)
        return
    share, top_email = year1_author_share(commits)
    truncated = len(commits) > MAX_COMMITS_PER_REPO
    kept_commits = commits[:MAX_COMMITS_PER_REPO]
    record = {
        "repo_metadata": {**meta, "total_commit_count": len(commits), "history_years": round(hist_years, 2)},
        "founder_signal": {
            "year1_top_author_email": top_email,
            "year1_top_author_share": round(share, 4) if share is not None else None,
        },
        "sampling_frame": "liveness_non_conditioned",
        "frame_construction_method": f"github_search_{discovery['discovery_tag']}",
        "discovery_query": discovery["discovery_query"],
        "truncated": truncated,
        "commit_cap": MAX_COMMITS_PER_REPO,
        "commits": kept_commits,
    }
    out_path = f"{ROOT}/temp/repo_records/{full_name.replace('/', '__')}.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(record, f)
    ckpt["done"][full_name] = {
        "path": out_path,
        "stars": meta["stars"],
        "archived": meta["archived"],
        "language": meta["language"],
        "history_years": round(hist_years, 2),
        "year1_top_author_share": round(share, 4) if share is not None else None,
        "n_commits": len(commits),
        "truncated": truncated,
        "sampling_frame": "liveness_non_conditioned",
    }
    save_ckpt(ckpt)
    log(f"done {full_name}: {len(commits)} commits, {hist_years:.1f}y history, archived={meta['archived']}, year1 top-author share={share}")


def main():
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    os.makedirs(CLONE_DIR, exist_ok=True)
    candidates = json.load(open(CANDIDATES_PATH))
    # prioritize candidates whose repo genuinely looks single-founder-plausible-worthy: sort by
    # star count desc within each discovery bucket only as a tiebreak for signal quality, never
    # to exclude low-star repos (that would reintroduce liveness/fame conditioning).
    candidates.sort(key=lambda c: (c["discovery_tag"], -(c.get("stars") or 0)))
    log(f"loaded {len(candidates)} liveness_non_conditioned candidates")
    ckpt = load_ckpt()
    budget_deadline = time.time() + float(sys.argv[1]) if len(sys.argv) > 1 else None
    for c in candidates:
        if budget_deadline and time.time() > budget_deadline:
            log("time budget exhausted, stopping")
            break
        try:
            process_repo(c["full_name"], c, ckpt)
        except Exception as e:
            log(f"ERROR on {c['full_name']}: {e}")
            ckpt["skipped"][c["full_name"]] = f"error:{e}"
            save_ckpt(ckpt)
    log(f"FINISHED: {len(ckpt['done'])} done, {len(ckpt['skipped'])} skipped")


if __name__ == "__main__":
    main()
