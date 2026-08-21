#!/usr/bin/env python3
"""Search GitHub for candidate repos, stratified by language and star-count bucket."""
import json
import sys
import time
from pathlib import Path

import requests
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/search.log", rotation="10 MB", level="DEBUG")

OUT = Path("temp/candidates.json")
LANGUAGES = ["Python", "JavaScript", "Go", "Rust", "Java", "Ruby"]
# stratified star buckets to avoid confounding popularity with survival
STAR_BUCKETS = ["100..2000", "2000..10000", ">10000"]

EXCLUDE_KEYWORDS = ["awesome", "book", "tutorial", "course", "cheatsheet", "interview",
                    "roadmap", "list-of", "resources", "guide"]

HEADERS = {"Accept": "application/vnd.github+json", "User-Agent": "aii-research-mining"}


def gh_get(url, params, max_retries=5):
    for attempt in range(max_retries):
        r = requests.get(url, headers=HEADERS, params=params, timeout=30)
        if r.status_code == 200:
            return r.json()
        if r.status_code in (403, 429):
            reset = r.headers.get("X-RateLimit-Reset")
            wait = 60
            if reset:
                wait = max(5, int(reset) - int(time.time()) + 2)
            logger.warning(f"Rate limited ({r.status_code}), sleeping {wait}s (attempt {attempt+1})")
            time.sleep(min(wait, 300))
            continue
        logger.error(f"GitHub API error {r.status_code}: {r.text[:300]}")
        time.sleep(5)
    return None


def is_junk(repo):
    name_desc = f"{repo.get('name','')} {repo.get('description') or ''}".lower()
    topics = " ".join(repo.get("topics") or []).lower()
    text = f"{name_desc} {topics}"
    return any(k in text for k in EXCLUDE_KEYWORDS)


def main():
    candidates = {}
    queries_run = 0
    for lang in LANGUAGES:
        for bucket in STAR_BUCKETS:
            q = f"language:{lang} stars:{bucket} fork:false archived:false"
            params = {"q": q, "sort": "stars", "order": "desc", "per_page": 100}
            logger.info(f"Query: {q}")
            data = gh_get("https://api.github.com/search/repositories", params)
            queries_run += 1
            if not data or "items" not in data:
                logger.error(f"No data for query: {q}")
                continue
            n_added = 0
            for repo in data["items"]:
                if is_junk(repo):
                    continue
                full_name = repo["full_name"]
                if full_name in candidates:
                    continue
                candidates[full_name] = {
                    "full_name": full_name,
                    "clone_url": repo["clone_url"],
                    "html_url": repo["html_url"],
                    "stars": repo["stargazers_count"],
                    "forks": repo["forks_count"],
                    "language": repo.get("language"),
                    "license": (repo.get("license") or {}).get("spdx_id"),
                    "created_at": repo["created_at"],
                    "pushed_at": repo["pushed_at"],
                    "description": repo.get("description"),
                    "topics": repo.get("topics") or [],
                    "default_branch": repo.get("default_branch", "main"),
                    "size_kb": repo.get("size"),
                    "search_bucket": f"{lang}:{bucket}",
                }
                n_added += 1
            logger.info(f"  -> {len(data['items'])} results, {n_added} new candidates (total {len(candidates)})")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(list(candidates.values()), indent=2))
    logger.info(f"Saved {len(candidates)} unique candidates from {queries_run} queries to {OUT}")


if __name__ == "__main__":
    main()
