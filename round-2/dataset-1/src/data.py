#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Standardize the liveness-non-conditioned founder-departure GitHub corpus
(temp/datasets/full_founder_departure_corpus.json) into exp_sel_data_out.json schema.

Produces the chosen repo_level_founder_departure_survival dataset: one example PER
REPO. input = JSON-encoded repo/founder features observable strictly BEFORE the
founder's last commit (no post-departure leakage); output = the survival label this
artifact exists to make available without liveness conditioning ("survived" /
"non_surviving" / "unknown_insufficient_post_departure_window"). This directly
operationalizes the hypothesis (does the project survive founder departure) at the
correct unit of analysis.
"""
from __future__ import annotations

import json
import logging
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("data")

WORKSPACE = Path(__file__).resolve().parent
SRC_PATH = WORKSPACE / "temp" / "datasets" / "full_founder_departure_corpus.json"
OUT_PATH = WORKSPACE / "full_data_out.json"

NON_SURVIVAL_STALE_DAYS = 730  # no commit in >=2yr as of build time -> "non_surviving" proxy label
POST_DEPARTURE_MIN_DAYS_FOR_LABEL = 30  # need at least some post-departure window to call a label at all


def parse_dt(s: str | None) -> datetime | None:
    if not s:
        return None
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def commit_identity(c: dict) -> str:
    return c.get("author_login") or c.get("author_email") or c.get("author_name") or "unknown"


def build_repo_level_examples(repos: list[dict]) -> list[dict]:
    examples = []
    label_counts = Counter()
    for r in repos:
        meta = r["repo_metadata"]
        fs = r["founder_signal"]
        commits = sorted(r["commits"], key=lambda c: c.get("date") or "")
        founder = fs["dominant_early_author"]

        founder_dates = [c["date"] for c in commits if commit_identity(c) == founder and c.get("date")]
        if not founder_dates:
            continue
        founder_last_dt = parse_dt(founder_dates[-1])
        repo_last_dt = parse_dt(fs["last_commit_date"])
        if founder_last_dt is None or repo_last_dt is None:
            continue

        # pre-departure feature window only: commits up to and including the founder's own last commit.
        # This avoids leaking the post-departure outcome into the input, which would make the label trivial.
        pre_departure_commits = [c for c in commits if (parse_dt(c.get("date")) or founder_last_dt) <= founder_last_dt]
        n_contributors_pre = len({commit_identity(c) for c in pre_departure_commits})

        post_departure_days = (repo_last_dt - founder_last_dt).days
        if post_departure_days < POST_DEPARTURE_MIN_DAYS_FOR_LABEL:
            label = "unknown_insufficient_post_departure_window"
        else:
            now = datetime.now(timezone.utc)
            is_stale = (now - repo_last_dt).days > NON_SURVIVAL_STALE_DAYS
            label = "non_surviving" if is_stale else "survived"
        label_counts[label] += 1

        input_obj = {
            "repo_full_name": meta["full_name"],
            "language": meta["language"],
            "repo_created_at": meta["created_at"],
            "founder_last_commit_date": fs["dominant_early_author"] and founder_dates[-1],
            "n_commits_pre_departure": len(pre_departure_commits),
            "n_contributors_pre_departure": n_contributors_pre,
            "dominant_early_author_fraction": fs["dominant_early_author_fraction"],
            "early_window_commit_count": fs["early_window_commit_count"],
            "stargazers_count_at_scrape_time": meta["stargazers_count"],
            "sampling_frame": meta["sampling_frame"],
        }
        examples.append(
            {
                "input": json.dumps(input_obj, sort_keys=True),
                "output": label,
                "metadata_task_type": "classification",
                "metadata_n_classes": 3,
                "metadata_repo_full_name": meta["full_name"],
                "metadata_sampling_frame": meta["sampling_frame"],
                "metadata_frame_construction_method": meta["frame_construction_method"],
                "metadata_post_departure_days": post_departure_days,
                "metadata_history_span_years": meta["history_span_years"],
                "metadata_archived": meta["archived"],
            }
        )
    log.info(f"repo_level: {len(examples)} examples, label distribution: {dict(label_counts)}")
    return examples


def main() -> None:
    if not SRC_PATH.exists():
        log.error(f"source dataset not found: {SRC_PATH}")
        sys.exit(1)

    with open(SRC_PATH) as f:
        corpus = json.load(f)
    repos = corpus["repos"]
    log.info(f"loaded corpus: {len(repos)} repos")

    repo_examples = build_repo_level_examples(repos)

    if not repo_examples:
        log.error("repo_level produced zero examples")
        sys.exit(1)

    out = {
        "metadata": {
            "source": "GitHub REST API, authenticated (GH_TOKEN), liveness-non-conditioned historical search",
            "description": (
                "Repo-level founder-departure survival-prediction view of the liveness_non_conditioned "
                "GitHub corpus built for this artifact: one example per repo, leakage-safe pre-departure "
                "features only, label = survived / non_surviving / unknown_insufficient_post_departure_window."
            ),
            "n_source_repos": len(repos),
        },
        "datasets": [
            {"dataset": "repo_level_founder_departure_survival", "examples": repo_examples},
        ],
    }

    with open(OUT_PATH, "w") as f:
        json.dump(out, f, indent=1)
    size_mb = OUT_PATH.stat().st_size / 1e6
    log.info(f"wrote {OUT_PATH} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
