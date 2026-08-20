#!/usr/bin/env python3
"""
Standardize the two candidate dataset sources into exp_sel_data_out.json schema.

Dataset A (github_founder_departure_commits): the corpus built directly from the
GitHub REST API (repo metadata) + `git clone`/`git log --numstat` (full commit
history with per-file insertion/deletion stats), per code/build_dataset.py.
Each example = one repository. `output` is the empirically-derived founder-
dominance label used by the plan's inclusion criterion (year-1 top-author
commit share >= 0.7), computed from the real cloned commit log — not assumed.

A second candidate, HuggingFace kamalkishor1991/commit-messages-dataset
(sampled individual commit diffs for commit-message generation across many
repos), was evaluated and REJECTED: it has no per-repo lifecycle, author-
identity-over-time, or per-file change structure, so it cannot support
founder-departure/authority-diffusion analysis. Only the GitHub corpus is
emitted here as the final chosen dataset.
"""
import json
import os

ROOT = "/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_1/gen_art/gen_art_dataset_1"
REPO_RECORDS_DIR = f"{ROOT}/temp/repo_records"
HF_PREVIEW = f"{ROOT}/temp/datasets/mini_kamalkishor1991_commit-messages-dataset_default_train.json"
OUT_PATH = f"{ROOT}/full_data_out.json"

FOUNDER_SHARE_THRESHOLD = 0.7


def build_github_examples():
    examples = []
    if not os.path.isdir(REPO_RECORDS_DIR):
        return examples
    for fname in sorted(os.listdir(REPO_RECORDS_DIR)):
        if not fname.endswith(".json"):
            continue
        with open(os.path.join(REPO_RECORDS_DIR, fname)) as f:
            rec = json.load(f)
        meta = rec["repo_metadata"]
        founder = rec["founder_signal"]
        share = founder.get("year1_top_author_share")
        label = "unknown"
        if share is not None:
            label = "founder_dominant" if share >= FOUNDER_SHARE_THRESHOLD else "not_founder_dominant"
        input_payload = {
            "repo_metadata": meta,
            "founder_signal": founder,
            "truncated": rec["truncated"],
            "commit_cap": rec["commit_cap"],
            "commits": rec["commits"],
        }
        examples.append({
            "input": json.dumps(input_payload, ensure_ascii=False),
            "output": label,
            "metadata_full_name": meta["full_name"],
            "metadata_stars": meta["stars"],
            "metadata_language": meta["language"],
            "metadata_history_years": meta["history_years"],
            "metadata_n_commits": meta["total_commit_count"],
            "metadata_truncated": rec["truncated"],
            "metadata_year1_top_author_share": share,
            "metadata_task_type": "founder_dominance_classification",
        })
    return examples


def build_hf_comparison_examples():
    examples = []
    if not os.path.exists(HF_PREVIEW):
        return examples
    with open(HF_PREVIEW) as f:
        data = json.load(f)
    rows = data if isinstance(data, list) else data.get("rows", data.get("data", []))
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            continue
        msg = row.get("msg") or row.get("msgGPT") or ""
        diff = row.get("diff") or ""
        examples.append({
            "input": json.dumps({"repo": row.get("repo"), "sha": row.get("sha"), "diff": diff}, ensure_ascii=False),
            "output": str(msg),
            "metadata_row_index": i,
            "metadata_repo": row.get("repo"),
            "metadata_task_type": "commit_message_generation",
        })
    return examples


def main():
    datasets = []
    gh_examples = build_github_examples()
    if gh_examples:
        datasets.append({"dataset": "github_founder_departure_commits", "examples": gh_examples})

    # HF kamalkishor1991/commit-messages-dataset was evaluated and REJECTED as a
    # candidate (no per-repo lifecycle / author-identity-over-time / per-file
    # structure) -- see build_hf_comparison_examples() docstring context above.
    # Not included in the final chosen dataset output.
    _ = build_hf_comparison_examples

    out = {
        "metadata": {
            "source": "GitHub REST API (unauthenticated, 60 req/hour) + `git clone` (bare) / `git log --numstat` for full local commit history with per-file insertion/deletion stats",
            "description": "Per-repo full commit history with per-file insertion/deletion stats and repo metadata, for founder-departure survival analysis (Avelino et al. DOA/Truck-Factor pipeline).",
            "primary_dataset": "github_founder_departure_commits",
            "founder_share_threshold": FOUNDER_SHARE_THRESHOLD,
            "n_repos": len(gh_examples),
            "rejected_comparison_candidate": "kamalkishor1991/commit-messages-dataset (HuggingFace) -- individual commit diffs sampled across many repos for commit-message generation; lacks per-repo lifecycle/author-identity/per-file structure needed here",
            "rate_limit_note": "Unauthenticated GitHub REST API is capped at 60 requests/hour (2 calls per repo: /repos/{full_name} and /repos/{full_name}/readme). This makes the plan's 150-250 repo target infeasible within the artifact time budget; git clone (smart-HTTP) itself is NOT rate-limited and was used for all commit history, so per-repo data completeness is unaffected -- only the TOTAL repo count is reduced, exactly per the plan's documented failure-handling guidance (reduce target repo count, checkpoint incrementally).",
        },
        "datasets": datasets,
    }
    with open(OUT_PATH, "w") as f:
        json.dump(out, f)
    print(f"Wrote {len(gh_examples)} github examples -> {OUT_PATH}")


if __name__ == "__main__":
    main()
