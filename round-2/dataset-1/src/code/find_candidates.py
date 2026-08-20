"""
Discover candidate repos for the LIVENESS_NON_CONDITIONED sampling frame.

Method (frame_construction_method = 'github_search_archived_or_stale_created_range'):
GitHub Search API, `q=` combining:
  - a repository-creation-date window (`created:YYYY-01-01..YYYY-12-31`), spanning
    2009-2016 so repos have >=10y of possible post-creation history today
  - EITHER `archived:true` (owner explicitly stopped maintaining it) OR a `pushed:`
    upper bound (no push since a fixed cutoff -- quietly dead, never archived)
  - a language filter, swept across 8 ecosystems for diversity
  - a low star floor (>=15) only to exclude zero-signal toy repos, NOT to select
    for current popularity/fame
No filter is ever applied on whether the repo is still starred, trending, or
alive today -- that is the entire point of this frame, in contrast to the
iter_1 corpus (candidates.py), whose list was hand-curated from "well-known,
currently prominent" projects and is tagged `liveness_conditioned`.

Uses the unauthenticated GitHub Search API (10 req/min, no GITHUB_TOKEN
present in this environment -- verified via `curl` before writing this
script). Results are deduplicated and checkpointed to disk so re-runs are
cheap.
"""
import json
import os
import sys
import time
from datetime import datetime, timezone

import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PATH = f"{ROOT}/temp/non_conditioned_candidates.json"
LOG_PATH = f"{ROOT}/logs/find_candidates.log"

API = "https://api.github.com/search/repositories"
SESSION = requests.Session()
SESSION.headers.update({"Accept": "application/vnd.github+json", "User-Agent": "aii-research-corpus/1.0"})

LANGUAGES = ["Python", "JavaScript", "Ruby", "Go", "Java", "C", "Rust", "PHP", "TypeScript", "C%2B%2B"]
# repo-creation windows: old enough that today (2026) they have >=10y of possible history
CREATED_WINDOWS = ["2009-01-01..2011-12-31", "2012-01-01..2014-12-31", "2015-01-01..2016-12-31"]
STALE_PUSHED_CUTOFF = "2020-01-01"  # no push since this date = quietly dead, never officially archived
MIN_STARS = 15


def log(msg):
    line = f"[{datetime.now(timezone.utc).isoformat()}] {msg}"
    print(line, flush=True)
    with open(LOG_PATH, "a") as f:
        f.write(line + "\n")


def search(query, max_pages=2):
    items = []
    for page in range(1, max_pages + 1):
        while True:
            r = SESSION.get(API, params={"q": query, "sort": "updated", "order": "asc", "per_page": 100, "page": page}, timeout=30)
            if r.status_code == 403:
                reset = int(r.headers.get("X-RateLimit-Reset", time.time() + 65))
                wait = max(reset - time.time(), 5) + 2
                log(f"rate limited; sleeping {wait:.0f}s")
                time.sleep(wait)
                continue
            if r.status_code != 200:
                log(f"search failed ({r.status_code}) for q={query!r}: {r.text[:200]}")
                return items
            break
        d = r.json()
        page_items = d.get("items", [])
        items.extend(page_items)
        log(f"q={query!r} page={page} -> {len(page_items)} items (total_count={d.get('total_count')})")
        time.sleep(6.5)  # unauth search: 10 req/min
        if len(page_items) < 100:
            break
    return items


def main():
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    seen = {}
    if os.path.exists(OUT_PATH):
        seen = {r["full_name"]: r for r in json.load(open(OUT_PATH))}
        log(f"resumed with {len(seen)} candidates already found")

    for lang in LANGUAGES:
        for window in CREATED_WINDOWS:
            for tag, extra in [
                ("archived", f"archived:true created:{window} language:{lang} stars:>={MIN_STARS}"),
                ("stale_unarchived", f"archived:false pushed:<{STALE_PUSHED_CUTOFF} created:{window} language:{lang} stars:>={MIN_STARS}"),
            ]:
                items = search(extra, max_pages=1)
                for it in items:
                    fn = it["full_name"]
                    if fn in seen:
                        continue
                    seen[fn] = {
                        "full_name": fn,
                        "stars": it.get("stargazers_count"),
                        "language": it.get("language"),
                        "created_at": it.get("created_at"),
                        "pushed_at": it.get("pushed_at"),
                        "archived": it.get("archived"),
                        "fork": it.get("fork"),
                        "discovery_tag": tag,
                        "discovery_query": extra,
                    }
                with open(OUT_PATH, "w") as f:
                    json.dump(list(seen.values()), f, indent=2)
                log(f"running total unique candidates: {len(seen)}")

    log(f"FINISHED: {len(seen)} unique liveness_non_conditioned candidates -> {OUT_PATH}")


if __name__ == "__main__":
    main()
