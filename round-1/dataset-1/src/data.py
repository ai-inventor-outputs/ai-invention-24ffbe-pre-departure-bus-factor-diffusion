#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Standardize the GitHub Founder-Departure commit-history corpus into
exp_sel_data_out.json schema: one example per (commit, file) row, grouped
under a single dataset entry. Reads the raw row-level JSONL built by
temp/build_corpus.py from temp/datasets/github_founder_corpus_rows.jsonl.
"""
import json
import os

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
ROWS_FILE = os.path.join(WORKSPACE, "temp", "datasets", "github_founder_corpus_rows.jsonl")
OUT_FILE = os.path.join(WORKSPACE, "full_data_out.json")


def to_example(row):
    # `input`: the observable commit/file-change features a downstream DOA /
    # truck-factor / survival model would condition on. Author identity itself
    # is withheld from `input` since `output` is the founder/non-founder label
    # derived from it -- author identity is still preserved as metadata for
    # provenance and alias-resolution auditing.
    input_obj = {
        "commit_index": row["commit_index"],
        "n_commits_total": row["n_commits_total"],
        "days_since_repo_created": row["days_since_repo_created"],
        "file_path": row["file_path"],
        "file_ext": row["file_ext"],
        "lines_added": row["lines_added"],
        "lines_removed": row["lines_removed"],
        "is_creation": row["is_creation"],
        "repo_stars": row["stars"],
        "repo_forks": row["forks"],
        "repo_primary_language": row["primary_language"],
    }
    output = "founder" if row["is_founder_commit"] == 1 else "other"
    example = {
        "input": json.dumps(input_obj, ensure_ascii=False),
        "output": output,
        "metadata_repo_id": row["repo_id"],
        "metadata_full_name": row["full_name"],
        "metadata_license": row["license"],
        "metadata_repo_created_at": row["repo_created_at"],
        "metadata_commit_sha": row["commit_sha"],
        "metadata_commit_timestamp": row["commit_timestamp"],
        "metadata_author_alias_key": row["author_alias_key"],
        "metadata_author_email": row["author_email"],
        "metadata_author_name": row["author_name"],
        "metadata_dominant_founder_share_first_window": row["dominant_founder_share_first_window"],
        "metadata_alias_ambiguous_repo": row["alias_ambiguous_repo"],
        "metadata_task_type": "classification",
        "metadata_n_classes": 2,
    }
    return example


PER_REPO_CAP = 4000  # stratified cap so a handful of huge-history repos
                      # (e.g. jenkinsci/jenkins at 150k rows) can't dominate
                      # the corpus or blow the 100MB full_data_out.json cap.


def main():
    # First pass: count rows per repo so the systematic-stride sampling below
    # can pick every Nth row per repo (preserving chronological spread and
    # founder/non-founder mix) rather than truncating to the earliest rows.
    counts = {}
    with open(ROWS_FILE) as f:
        for line in f:
            if not line.strip():
                continue
            full_name = json.loads(line)["full_name"]
            counts[full_name] = counts.get(full_name, 0) + 1

    strides = {name: max(1, n // PER_REPO_CAP + 1) for name, n in counts.items()}

    examples = []
    seen = {}
    with open(ROWS_FILE) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            name = row["full_name"]
            i = seen.get(name, 0)
            seen[name] = i + 1
            if i % strides[name] != 0:
                continue
            examples.append(to_example(row))

    out = {
        "metadata": {
            "source": "Local git clone (git log --numstat) over GitHub repos sampled via "
                       "the GitHub REST search/repositories API across JavaScript/Python/Java/Go "
                       "and 3 popularity strata (100-1k, 1k-10k, 10k+ stars); repo-level metadata "
                       "(stars, forks, license, language, created_at) from the same API.",
            "description": "Per-(commit,file) rows for GitHub repos passing founder-only-start "
                            "filters (>=100 commits, no history-loss/squash artifact, a single "
                            "author holding >=70% share of commits in the first ~50-commit / "
                            "6-month window). `output` is founder-vs-other authorship of that "
                            "commit; `input` withholds author identity so it can serve as a "
                            "downstream classification/DOA feature set without leaking the label. "
                            f"Repos with more than {PER_REPO_CAP} (commit,file) rows are systematically "
                            "strided down to that cap (keep every Nth row, chronological order preserved) "
                            "to keep the corpus size bounded and prevent a few huge-history repos "
                            "(e.g. jenkinsci/jenkins) from dominating the example count.",
            "n_examples": len(examples),
            "n_repos": len({e["metadata_full_name"] for e in examples}),
        },
        "datasets": [
            {
                "dataset": "github_founder_departure_corpus",
                "examples": examples,
            }
        ],
    }
    with open(OUT_FILE, "w") as f:
        json.dump(out, f, ensure_ascii=False)
    print(f"wrote {len(examples)} examples across "
          f"{out['metadata']['n_repos']} repos to {OUT_FILE}")


if __name__ == "__main__":
    main()
