#!/usr/bin/env python3
"""
Standardize the founder-departure commit corpus to exp_sel_data_out schema.

One dataset group, `github_founder_departure_commits_non_conditioned`, one
example per repo (matching iter_1's per-repo example granularity, since a
"row" in this domain is a repo's full commit history, not a single commit).

Pools BOTH sampling frames into the SAME dataset group so the corpus is a
true drop-in companion/superset of iter_1's exp_sel_data_out output:
  - sampling_frame='liveness_non_conditioned': repos discovered this iteration
    via GitHub Search API on (archived OR long-stale) x (historical creation
    window) x language, with NO filter on current stars/fame/liveness
    (code/find_candidates.py, code/build_dataset.py).
  - sampling_frame='liveness_conditioned': the 12 successfully-extracted repos
    from iter_1's hand-curated "currently prominent" candidate list, carried
    forward UNMODIFIED (same repo_metadata/founder_signal/commits, just
    retro-tagged) so downstream code can filter or stratify by frame per the
    gen_plan's explicit requirement, rather than silently mixing them.
Every example also carries `metadata_task_type` matching iter_1's convention
so the two corpora are interchangeable inputs to the same downstream method.
"""
import json
import glob
import os
from pathlib import Path

from loguru import logger
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

ROOT = Path(__file__).parent
ITER1_ROOT = Path(
    "/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_1/gen_art/gen_art_dataset_1"
)
FOUNDER_SHARE_THRESHOLD = 0.7


def label_for(share):
    if share is None:
        return "unknown"
    return "founder_dominant" if share >= FOUNDER_SHARE_THRESHOLD else "not_founder_dominant"


def record_to_example(record):
    input_obj = {
        "repo_metadata": record["repo_metadata"],
        "commits": record["commits"],
        "truncated": record["truncated"],
        "commit_cap": record["commit_cap"],
    }
    share = record["founder_signal"]["year1_top_author_share"]
    return {
        "input": json.dumps(input_obj),
        "output": label_for(share),
        "metadata_full_name": record["repo_metadata"]["full_name"],
        "metadata_stars": record["repo_metadata"]["stars"],
        "metadata_language": record["repo_metadata"]["language"],
        "metadata_history_years": record["repo_metadata"]["history_years"],
        "metadata_n_commits": record["repo_metadata"]["total_commit_count"],
        "metadata_truncated": record["truncated"],
        "metadata_year1_top_author_share": share,
        "metadata_task_type": "founder_dominance_classification",
        "metadata_sampling_frame": record["sampling_frame"],
        "metadata_frame_construction_method": record["frame_construction_method"],
        "metadata_archived": record["repo_metadata"].get("archived"),
    }


@logger.catch(reraise=True)
def main():
    examples = []

    # 1. This iteration's liveness_non_conditioned repos
    nc_paths = sorted(glob.glob(str(ROOT / "temp/repo_records/*.json")))
    logger.info(f"found {len(nc_paths)} liveness_non_conditioned repo records")
    n_nc = 0
    for p in nc_paths:
        record = json.loads(Path(p).read_text())
        examples.append(record_to_example(record))
        n_nc += 1

    # 2. iter_1's liveness_conditioned repos, carried forward unmodified + retro-tagged
    ckpt_path = ITER1_ROOT / "temp/checkpoint.json"
    n_c = 0
    if ckpt_path.exists():
        ckpt = json.loads(ckpt_path.read_text())
        for full_name, info in ckpt["done"].items():
            rp = Path(info["path"])
            if not rp.exists():
                logger.warning(f"iter_1 record missing on disk: {rp}")
                continue
            record = json.loads(rp.read_text())
            record["sampling_frame"] = "liveness_conditioned"
            record["frame_construction_method"] = "currently_prominent_handcurated"
            examples.append(record_to_example(record))
            n_c += 1
    else:
        logger.warning(f"iter_1 checkpoint not found at {ckpt_path}")

    logger.info(f"liveness_non_conditioned examples: {n_nc}, liveness_conditioned examples: {n_c}")

    # yield report, from this iteration's own checkpoint
    ckpt2_path = ROOT / "temp/checkpoint.json"
    ckpt2 = json.loads(ckpt2_path.read_text()) if ckpt2_path.exists() else {"done": {}, "skipped": {}}
    n_candidates = 0
    cand_path = ROOT / "temp/non_conditioned_candidates.json"
    if cand_path.exists():
        n_candidates = len(json.loads(cand_path.read_text()))

    from collections import Counter

    skip_reasons = Counter()
    for v in ckpt2["skipped"].values():
        key = v.split("_")[0] if not v.startswith("insufficient_history") else "insufficient_history"
        skip_reasons[key] += 1

    founder_only_nc = sum(
        1
        for p in nc_paths
        if json.loads(Path(p).read_text())["founder_signal"]["year1_top_author_share"] is not None
        and json.loads(Path(p).read_text())["founder_signal"]["year1_top_author_share"] >= FOUNDER_SHARE_THRESHOLD
    )

    metadata = {
        "source": "GitHub Search API (unauthenticated, 10 req/min search endpoint) for candidate discovery via "
        "archived-or-stale x historical-creation-window x language queries (code/find_candidates.py) + "
        "GitHub REST API (unauthenticated, 60 req/hour) for repo metadata + `git clone --bare` / "
        "`git log --numstat` for full local commit history (code/build_dataset.py). iter_1's "
        "liveness_conditioned repos (currently-prominent hand-curated list) are pooled in unmodified "
        "for direct comparison.",
        "description": "Companion/superset corpus to iter_1's github_founder_departure_commits: per-repo full "
        "commit history + founder-dominance signal, POOLING two explicit sampling frames "
        "(liveness_conditioned vs liveness_non_conditioned) tagged per-example via "
        "metadata_sampling_frame so downstream code can filter or stratify honestly instead of "
        "silently mixing a survivorship-biased sample with an unbiased one.",
        "primary_dataset": "github_founder_departure_commits_non_conditioned",
        "founder_share_threshold": FOUNDER_SHARE_THRESHOLD,
        "n_examples_total": len(examples),
        "n_liveness_non_conditioned": n_nc,
        "n_liveness_conditioned": n_c,
        "yield_report": {
            "candidates_discovered_non_conditioned": n_candidates,
            "candidates_attempted_non_conditioned": len(ckpt2["done"]) + len(ckpt2["skipped"]),
            "candidates_succeeded_non_conditioned": len(ckpt2["done"]),
            "candidates_skipped_non_conditioned": len(ckpt2["skipped"]),
            "skip_reason_breakdown_non_conditioned": dict(skip_reasons),
            "founder_dominant_repos_in_non_conditioned_subset": founder_only_nc,
            "note": (
                "Yield is low and reported honestly per the gen_plan: the majority of "
                "archived/long-stale GitHub repos discovered by creation-date + archived/stale "
                "search queries turn out to have been abandoned WITHIN 1-2 years of creation "
                "(insufficient_history skip, <3.0y total commit span), i.e. they never had enough "
                "history to run a year-by-year DOA/Truck-Factor pipeline on in the first place. "
                "This is itself informative: repos that are prominent enough to survive multiple "
                "years AND still end up archived/abandoned are a genuinely rare intersection "
                "relative to the much larger population of small repos that simply die early. "
                "No liveness_non_conditioned repo in this batch was found to have a NON-surviving "
                "founder-only TFDD event with enough post-departure history to score the 18-month "
                "survival window -- that specific gap this artifact targets remains OPEN, and the "
                "downstream eval/experiment artifacts should treat power for that specific claim "
                "as unproven rather than assume it from this corpus alone."
            ),
        },
        "rate_limit_note": "Unauthenticated GitHub Search API is capped at 10 requests/minute; unauthenticated "
        "REST API (repo/readme fetch) at 60 requests/hour. No GITHUB_TOKEN was present in this "
        "environment (verified via `curl -s https://api.github.com/rate_limit` before writing "
        "find_candidates.py). This makes the gen_plan's full historical-window sweep infeasible "
        "within a single artifact's wall-clock budget; find_candidates.py and build_dataset.py "
        "both checkpoint to disk and are resumable to extend this corpus in a follow-up run.",
    }

    out = {"metadata": metadata, "datasets": [{"dataset": metadata["primary_dataset"], "examples": examples}]}
    out_path = ROOT / "full_data_out.json"
    out_path.write_text(json.dumps(out))
    logger.info(f"wrote {len(examples)} examples to {out_path}")


if __name__ == "__main__":
    main()
