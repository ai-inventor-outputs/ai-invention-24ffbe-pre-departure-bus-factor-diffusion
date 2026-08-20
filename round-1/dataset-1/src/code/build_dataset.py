"""
Build the GitHub Founder-Departure Commit History Corpus.

Data sources (real, verifiable):
  1. GitHub REST API (unauthenticated, 60 req/hour) for repo-level metadata
     (stars, forks, language, license, created_at, pushed_at, contributor
     approximation, README presence).
  2. `git clone` (git smart-HTTP protocol, NOT subject to the REST API rate
     limit) for full commit history with per-file change stats, via
     `git log --numstat`.

No claims about "single founder dominance" are asserted a priori — they are
computed empirically per repo from the cloned commit log (year-1 author
commit share) and used to decide inclusion in the final corpus.

Because this environment has no GITHUB_TOKEN (unauthenticated 60 req/hour),
the original plan's 150-250 repo target is infeasible within the time
budget while also pulling multi-thousand-commit histories; this script
documents that tradeoff explicitly (see README/manifest `rate_limit_note`)
and produces the largest corpus feasible with checkpointing, following the
plan's own failure-handling guidance (reduce target repo count, checkpoint
incrementally).
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

sys.path.insert(0, os.path.dirname(__file__))
from candidates import CANDIDATES  # noqa: E402

ROOT = "/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_1/gen_art/gen_art_dataset_1"
CLONE_DIR = f"{ROOT}/temp/clones"
CKPT_PATH = f"{ROOT}/temp/checkpoint.json"
LOG_PATH = f"{ROOT}/logs/build.log"
MAX_COMMITS_PER_REPO = 5000
MIN_STARS = 100
MIN_HISTORY_YEARS = 4.0

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
    """GET against the GitHub REST API, honoring the unauthenticated rate limit."""
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


def fetch_repo_meta(full_name):
    r = api_get(f"/repos/{full_name}")
    if r.status_code != 200:
        return None, f"http_{r.status_code}"
    d = r.json()
    if d.get("archived"):
        return None, "archived"
    if d.get("fork"):
        return None, "is_fork"
    if (d.get("stargazers_count") or 0) < MIN_STARS:
        return None, "too_few_stars"
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
        "readme_excerpt": readme_excerpt,
    }
    return meta, None


def clone_repo(full_name):
    dest = os.path.join(CLONE_DIR, full_name.replace("/", "__"))
    if os.path.isdir(dest):
        shutil.rmtree(dest, ignore_errors=True)
    url = f"https://github.com/{full_name}.git"
    try:
        # NOTE: no --filter=blob:none here — --numstat needs blob content, and a
        # blob:none partial clone forces a slow per-commit lazy fetch over the
        # network during `git log --numstat` (observed: minutes per repo stall).
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
    """Full commit history via `git log --numstat`, newest first."""
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
    """Fraction of commits in the repo's first 365 days by its top author."""
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


def process_repo(full_name, ckpt):
    if full_name in ckpt["done"] or full_name in ckpt["skipped"]:
        return
    log(f"processing {full_name}")
    meta, skip_reason = fetch_repo_meta(full_name)
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
    share, top_email = year1_author_share(commits)
    truncated = len(commits) > MAX_COMMITS_PER_REPO
    kept_commits = commits[:MAX_COMMITS_PER_REPO]  # newest-first: keep most recent
    record = {
        "repo_metadata": {**meta, "total_commit_count": len(commits), "history_years": round(hist_years, 2)},
        "founder_signal": {
            "year1_top_author_email": top_email,
            "year1_top_author_share": round(share, 4) if share is not None else None,
        },
        "truncated": truncated,
        "commit_cap": MAX_COMMITS_PER_REPO,
        "commits": kept_commits,
    }
    out_path = f"{CLONE_DIR}/../repo_records/{full_name.replace('/', '__')}.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(record, f)
    ckpt["done"][full_name] = {
        "path": out_path,
        "stars": meta["stars"],
        "language": meta["language"],
        "history_years": round(hist_years, 2),
        "year1_top_author_share": round(share, 4) if share is not None else None,
        "n_commits": len(commits),
        "truncated": truncated,
    }
    save_ckpt(ckpt)
    log(f"done {full_name}: {len(commits)} commits, {hist_years:.1f}y history, year1 top-author share={share}")


def main():
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    os.makedirs(CLONE_DIR, exist_ok=True)
    ckpt = load_ckpt()
    for full_name in CANDIDATES:
        try:
            process_repo(full_name, ckpt)
        except Exception as e:
            log(f"ERROR on {full_name}: {e}")
            ckpt["skipped"][full_name] = f"error:{e}"
            save_ckpt(ckpt)
    log(f"FINISHED: {len(ckpt['done'])} done, {len(ckpt['skipped'])} skipped")


if __name__ == "__main__":
    main()
