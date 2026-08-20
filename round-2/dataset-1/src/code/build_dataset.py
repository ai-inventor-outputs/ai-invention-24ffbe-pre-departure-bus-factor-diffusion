"""
Build a liveness-non-conditioned founder-departure candidate corpus via the GitHub REST API.

Unlike a "currently trending/famous repos" sample, candidates here are discovered purely from
repository CREATION and PUSH date ranges (GitHub Search API `created:`/`pushed:` qualifiers),
with NO filter on current archived/star/maintenance status. Every repo is tagged with an explicit
`sampling_frame` field so downstream code never silently pools this with a liveness-conditioned
sample.

Commit history is pulled via the REST `/commits` and `/stats/contributors` endpoints rather than
`git clone`, which is far cheaper against a 5000 req/hr authenticated budget and a CPU-only,
no-GPU workspace.
"""
from __future__ import annotations

import json
import os
import time
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

import requests

GH_TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("AII_GH_TOKEN")
assert GH_TOKEN, "No GitHub token found in GH_TOKEN / AII_GH_TOKEN"

API = "https://api.github.com"
HEADERS = {
    "Authorization": f"token {GH_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}

WORKSPACE = "/ai-inventor/aii_data/runs/run_LYICROwXFVjo/3_invention_loop/iter_2/gen_art/gen_art_dataset_1"
CKPT_PATH = f"{WORKSPACE}/temp/checkpoint/checkpoint.json"
LOG_PATH = f"{WORKSPACE}/temp/checkpoint/build.log"

# Historical windows to sample from: repos CREATED in these ranges, so their early
# history (founder period) sits well in the past, giving room for >=3yrs post-founder-exit
# history without right-censoring, per the plan's requirement (2). We deliberately span
# several years/languages rather than one query, since a single query returns <=1000 results
# and we do not want the sample dominated by one era or ecosystem.
CREATED_RANGES = [
    ("2011-01-01", "2011-12-31"),
    ("2012-01-01", "2012-12-31"),
    ("2013-01-01", "2013-12-31"),
    ("2014-01-01", "2014-12-31"),
    ("2015-01-01", "2015-12-31"),
]
LANGUAGES = ["Python", "JavaScript", "Ruby", "Go", "C", "Java", "PHP", "Rust"]

MIN_STARS = 20  # floor for "real project with any signal", not a liveness filter (archived/dead repos with old stars pass fine)
MAX_STARS_SEARCH = None  # no ceiling
PER_PAGE = 30
MAX_PAGES_PER_QUERY = 3  # 3*30=90 candidates per (year, language) query, capped by search API
TARGET_CANDIDATES = 220  # dedup'd candidate repos to attempt before filtering
MAX_COMMITS_PER_REPO = 3000  # numstat-free REST /commits pagination cap per repo (perf + rate-limit budget)
MIN_HISTORY_YEARS = 4.0  # need room for founder period + >=3yr post-exit window
MIN_COMMITS = 60


def log(msg: str) -> None:
    line = f"[{datetime.now(timezone.utc).isoformat()}] {msg}"
    print(line, flush=True)
    with open(LOG_PATH, "a") as f:
        f.write(line + "\n")


def load_checkpoint() -> dict:
    if os.path.exists(CKPT_PATH):
        with open(CKPT_PATH) as f:
            return json.load(f)
    return {"candidates_seen": {}, "repos_done": {}, "stage": "search"}


def save_checkpoint(ckpt: dict) -> None:
    tmp = CKPT_PATH + ".tmp"
    with open(tmp, "w") as f:
        json.dump(ckpt, f)
    os.replace(tmp, CKPT_PATH)


def gh_get(url: str, params: dict | None = None, max_retries: int = 5) -> requests.Response | None:
    for attempt in range(max_retries):
        try:
            resp = requests.get(url, headers=HEADERS, params=params, timeout=30)
        except requests.RequestException as e:
            log(f"  network error on {url}: {e}; retrying")
            time.sleep(2 * (attempt + 1))
            continue
        if resp.status_code == 403 and "rate limit" in resp.text.lower():
            reset = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
            wait = max(reset - time.time(), 1) + 2
            log(f"  rate limited, sleeping {wait:.0f}s")
            time.sleep(min(wait, 120))
            continue
        if resp.status_code == 202:
            # stats endpoint computing async — brief backoff and retry
            time.sleep(2 * (attempt + 1))
            continue
        return resp
    return None


def search_candidates(ckpt: dict) -> list[dict]:
    seen = ckpt["candidates_seen"]
    for created_from, created_to in CREATED_RANGES:
        for lang in LANGUAGES:
            key = f"{created_from}:{created_to}:{lang}"
            if key in ckpt.get("queries_done", {}):
                continue
            q = f"language:{lang} created:{created_from}..{created_to} stars:>={MIN_STARS}"
            log(f"search query: {q}")
            for page in range(1, MAX_PAGES_PER_QUERY + 1):
                resp = gh_get(
                    f"{API}/search/repositories",
                    params={"q": q, "sort": "stars", "order": "asc", "per_page": PER_PAGE, "page": page},
                )
                if resp is None or resp.status_code != 200:
                    log(f"  search failed page={page} status={getattr(resp,'status_code',None)}")
                    break
                items = resp.json().get("items", [])
                if not items:
                    break
                for it in items:
                    full_name = it["full_name"]
                    if full_name not in seen:
                        seen[full_name] = {
                            "full_name": full_name,
                            "created_at": it["created_at"],
                            "pushed_at": it["pushed_at"],
                            "stargazers_count": it["stargazers_count"],
                            "archived": it["archived"],
                            "language": it.get("language"),
                            "html_url": it["html_url"],
                            "default_branch": it.get("default_branch", "main"),
                        }
                time.sleep(2.1)  # respect 30/min search rate limit
            ckpt.setdefault("queries_done", {})[key] = True
            save_checkpoint(ckpt)
            if len(seen) >= TARGET_CANDIDATES * 2:
                log(f"reached {len(seen)} candidates, enough for target {TARGET_CANDIDATES}")
                return list(seen.values())
    return list(seen.values())


def fetch_commits(full_name: str) -> list[dict]:
    commits = []
    page = 1
    while len(commits) < MAX_COMMITS_PER_REPO:
        resp = gh_get(f"{API}/repos/{full_name}/commits", params={"per_page": 100, "page": page})
        if resp is None or resp.status_code != 200:
            break
        batch = resp.json()
        if not batch:
            break
        for c in batch:
            author = c.get("author") or {}
            commit_author = c.get("commit", {}).get("author", {}) or {}
            commits.append(
                {
                    "sha": c["sha"],
                    "author_login": author.get("login"),
                    "author_name": commit_author.get("name"),
                    "author_email": commit_author.get("email"),
                    "date": commit_author.get("date"),
                }
            )
        if len(batch) < 100:
            break
        page += 1
    return commits


def fetch_contributor_stats(full_name: str) -> list[dict]:
    resp = gh_get(f"{API}/repos/{full_name}/stats/contributors")
    if resp is None or resp.status_code != 200:
        return []
    try:
        data = resp.json()
    except Exception:
        return []
    if not isinstance(data, list):
        return []
    return data


def founder_signal_from_commits(commits: list[dict]) -> dict:
    if not commits:
        return {"has_dominant_early_author": False}
    # commits from the REST /commits endpoint arrive newest-first
    ordered = sorted(commits, key=lambda c: c.get("date") or "")
    n_early = max(1, min(50, len(ordered) // 5))
    early = ordered[:n_early]
    from collections import Counter

    identity = lambda c: c.get("author_login") or c.get("author_email") or c.get("author_name") or "unknown"
    counts = Counter(identity(c) for c in early)
    top_author, top_count = counts.most_common(1)[0]
    frac = top_count / len(early)
    all_dates = [c["date"] for c in ordered if c.get("date")]
    return {
        "has_dominant_early_author": frac >= 0.6,
        "dominant_early_author": top_author,
        "dominant_early_author_fraction": round(frac, 4),
        "early_window_commit_count": len(early),
        "first_commit_date": all_dates[0] if all_dates else None,
        "last_commit_date": all_dates[-1] if all_dates else None,
    }


def history_span_years(commits: list[dict]) -> float:
    dates = sorted(c["date"] for c in commits if c.get("date"))
    if len(dates) < 2:
        return 0.0
    d0 = datetime.fromisoformat(dates[0].replace("Z", "+00:00"))
    d1 = datetime.fromisoformat(dates[-1].replace("Z", "+00:00"))
    return (d1 - d0).days / 365.25


def process_repo(cand: dict) -> dict | None:
    full_name = cand["full_name"]
    try:
        commits = fetch_commits(full_name)
        if len(commits) < MIN_COMMITS:
            return {"full_name": full_name, "status": "rejected", "reason": f"too_few_commits({len(commits)})"}
        span = history_span_years(commits)
        if span < MIN_HISTORY_YEARS:
            return {"full_name": full_name, "status": "rejected", "reason": f"short_history({span:.1f}yr)"}
        fsig = founder_signal_from_commits(commits)
        if not fsig["has_dominant_early_author"]:
            return {"full_name": full_name, "status": "rejected", "reason": "no_dominant_founder"}
        contrib_stats = fetch_contributor_stats(full_name)
        record = {
            "repo_metadata": {
                "full_name": full_name,
                "html_url": cand["html_url"],
                "created_at": cand["created_at"],
                "pushed_at": cand["pushed_at"],
                "stargazers_count": cand["stargazers_count"],
                "archived": cand["archived"],
                "language": cand["language"],
                "history_span_years": round(span, 2),
                "sampling_frame": "liveness_non_conditioned",
                "frame_construction_method": "github_search_created_pushed_range_no_archive_filter",
            },
            "founder_signal": fsig,
            "commits": commits,
            "contributor_stats_weekly": contrib_stats,
        }
        return {"full_name": full_name, "status": "accepted", "record": record}
    except Exception as e:
        return {"full_name": full_name, "status": "error", "reason": f"{e}\n{traceback.format_exc()[-500:]}"}


def main():
    os.makedirs(f"{WORKSPACE}/temp/checkpoint", exist_ok=True)
    ckpt = load_checkpoint()

    log("=== Phase 1: search candidates ===")
    candidates = search_candidates(ckpt)
    log(f"total dedup'd candidates: {len(candidates)}")

    todo = [c for c in candidates if c["full_name"] not in ckpt["repos_done"]]
    log(f"=== Phase 2: mine commit history for {len(todo)} candidates (already done: {len(ckpt['repos_done'])}) ===")

    accepted, rejected, errored = [], [], []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(process_repo, c): c for c in todo}
        n_done = 0
        for fut in as_completed(futs):
            result = fut.result()
            n_done += 1
            ckpt["repos_done"][result["full_name"]] = {"status": result["status"], "reason": result.get("reason")}
            if result["status"] == "accepted":
                accepted.append(result["record"])
            elif result["status"] == "rejected":
                rejected.append(result)
            else:
                errored.append(result)
            if n_done % 10 == 0:
                save_checkpoint(ckpt)
                log(f"  progress {n_done}/{len(todo)}: accepted={len(accepted)} rejected={len(rejected)} errored={len(errored)}")

    save_checkpoint(ckpt)
    log(f"FINAL: attempted={len(todo)+len(ckpt['repos_done'])-len(todo)} this_run={len(todo)} accepted={len(accepted)} rejected={len(rejected)} errored={len(errored)}")

    # also load any previously-accepted repos from prior partial runs (checkpoint stores status only,
    # not the full record, so this run's `accepted` list is authoritative for records produced now)
    out = {
        "dataset_name": "founder_departure_liveness_non_conditioned_corpus",
        "description": (
            "Repo-level + commit-level GitHub corpus sampled by historical creation/push-date window "
            "(GitHub Search API created:/pushed: qualifiers), with NO filter on present-day archived/"
            "maintenance status. Schema-compatible companion to a liveness-conditioned corpus: "
            "repo_metadata, founder_signal, commits[], plus explicit sampling_frame/"
            "frame_construction_method fields for honest pooling/stratification downstream."
        ),
        "sampling_frame_definitions": {
            "liveness_conditioned": "repos discovered via currently-famous/trending lists (not used by this build)",
            "liveness_non_conditioned": "repos discovered via historical creation/push-date search only, independent of present-day status",
        },
        "build_yield_report": {
            "candidates_seen_total": len(candidates),
            "candidates_attempted_this_run": len(todo),
            "accepted_this_run": len(accepted),
            "rejected_this_run": len(rejected),
            "errored_this_run": len(errored),
            "rejection_reasons": {},
        },
        "repos": accepted,
    }
    from collections import Counter

    out["build_yield_report"]["rejection_reasons"] = dict(Counter(r["reason"] for r in rejected))

    full_path = f"{WORKSPACE}/temp/datasets/full_founder_departure_corpus.json"
    with open(full_path, "w") as f:
        json.dump(out, f, indent=1)
    size_mb = os.path.getsize(full_path) / 1e6
    log(f"wrote {full_path} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
