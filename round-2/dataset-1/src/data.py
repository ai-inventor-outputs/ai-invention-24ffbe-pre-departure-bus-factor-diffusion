#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Package the founder-departure GitHub corpus (254 repos, funnel-filtered)
into exp_sel_data_out schema: one example per (commit, file) row, output
withholds is_founder_commit as the downstream classification/DOA-feature label."""
import json
from collections import defaultdict
from pathlib import Path

WORK = Path(__file__).parent
RAW_JSONL = WORK / "temp" / "datasets" / "github_founder_corpus_rows.jsonl"
FUNNEL_FILE = WORK / "temp" / "funnel_report.json"
OUT_FILE = WORK / "full_data_out.json"

MAX_ROWS_PER_REPO = 200
LABEL_FIELD = "is_founder_commit"
INPUT_FIELDS_EXCLUDE = {LABEL_FIELD, "author_alias_key", "author_email", "author_name"}


def load_rows_by_repo():
    by_repo = defaultdict(list)
    with open(RAW_JSONL) as f:
        for line in f:
            row = json.loads(line)
            by_repo[row["full_name"]].append(row)
    return by_repo


def stride_cap(rows, cap):
    n = len(rows)
    if n <= cap:
        return rows
    step = n / cap
    return [rows[int(i * step)] for i in range(cap)]


def to_example(row):
    input_obj = {k: v for k, v in row.items() if k not in INPUT_FIELDS_EXCLUDE}
    example = {
        "input": json.dumps(input_obj, sort_keys=True),
        "output": str(row[LABEL_FIELD]),
        "metadata_fold": row["search_lang_query"] + "|" + row["search_stars_bucket"],
        "metadata_task_type": "classification",
        "metadata_n_classes": 2,
        "metadata_full_name": row["full_name"],
        "metadata_primary_language": row["primary_language"],
        "metadata_search_stars_bucket": row["search_stars_bucket"],
        "metadata_commit_sha": row["commit_sha"],
        "metadata_commit_timestamp": row["commit_timestamp"],
        "metadata_commit_index": row["commit_index"],
        "metadata_n_commits_total": row["n_commits_total"],
        "metadata_contributor_tenure_days": row["contributor_tenure_days"],
        "metadata_founder_tfdd_approx": row["founder_tfdd_approx"],
        "metadata_diffusion_window_tag": row["diffusion_window_tag"],
        "metadata_alias_ambiguous_repo": row["alias_ambiguous_repo"],
    }
    return example


def main():
    by_repo = load_rows_by_repo()
    funnel = json.load(open(FUNNEL_FILE))

    examples = []
    for full_name, rows in by_repo.items():
        rows_sorted = sorted(rows, key=lambda r: r["commit_index"])
        kept = stride_cap(rows_sorted, MAX_ROWS_PER_REPO)
        for row in kept:
            examples.append(to_example(row))

    description = (
        "Per-(commit,file) rows for 254 GitHub repos passing a fame-independent "
        "stratified sample (6 languages x 3 star strata, 1170 candidates -> 254 "
        "final, full funnel in metadata) and founder-only-start filters (>=1095 "
        "days history, <=80% of files touched in first 7 days, single author "
        ">=70% of commits in first 6mo/50 commits). `output` is founder-vs-other "
        "authorship of that (commit,file) row; `input` withholds author identity "
        "to prevent label leakage for downstream DOA/classification use. Adds "
        "per-contributor tenure (write-access-duration proxy), an approximate "
        "founder TFDD point (365-day silence rule), and a diffusion_window_tag "
        "marking each non-founder's first-commit timing relative to the pre-TFDD "
        "6-12mo window, so the downstream experiment can compute both Medappa "
        "et al.'s static write-access-ratio construct and this hypothesis's "
        "dynamic pre-departure diffusion-concentration construct from one corpus. "
        "Repos with >4000 (commit,file) rows are strided down to that cap "
        "(chronological order preserved) to bound corpus size. "
        f"Filtering funnel (18 language x star-stratum cells): {json.dumps(funnel['totals'])}."
    )

    out = {
        "datasets": [
            {
                "dataset": "github_founder_departure_corpus",
                "examples": examples,
            }
        ],
        "metadata": {
            "source": (
                "GitHub REST search/repositories API (candidate discovery, "
                "GH_TOKEN-authenticated) + local `git clone --bare` / "
                "`git log --numstat` (full commit history extraction, avoids "
                "API rate limits)."
            ),
            "description": description,
            "n_examples": len(examples),
            "n_repos": len(by_repo),
            "funnel": funnel,
        },
    }

    OUT_FILE.write_text(json.dumps(out))
    print(f"wrote {len(examples)} examples across {len(by_repo)} repos to {OUT_FILE}")
    print(f"file size: {OUT_FILE.stat().st_size / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
