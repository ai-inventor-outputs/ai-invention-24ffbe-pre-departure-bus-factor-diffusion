#!/usr/bin/env python3
"""Assemble mined repo results into the exp_sel_data_out.json schema:
one dataset group ('founder_departure_tfdd_corpus'), one example per
qualifying repo. `input` = JSON of pre-TFDD/TFDD-snapshot covariates
(the predictors); `output` = survival_label (the target). All raw
per-year DOA/TF tables, TFDD metadata, and post-TFDD monthly series are
carried as metadata_* fields so downstream experiment code can recompute
or verify authority-diffusion trajectories without re-cloning repos.
"""
import glob
import json
import sys
from pathlib import Path

from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/data.log", rotation="10 MB", level="DEBUG")

RESULTS_GLOB = "temp/repo_results/*.json"
OUT_PATH = Path("full_data_out.json")


def build_example(r: dict) -> dict:
    pre = r["pre_tfdd_window"]
    cov = r["tfdd_snapshot_covariates"]
    input_features = {
        "founder_commit_share_pre_tfdd": pre["founder_commit_share"],
        "n_distinct_new_primary_owners_pre_tfdd": pre["n_distinct_new_primary_owners"],
        "founder_early_authorship_share": r["founder_early_authorship_share"],
        "stars": cov["stars"],
        "forks": cov["forks"],
        "total_contributors": cov["total_contributors"],
        "language": cov["language"],
        "license": cov["license"],
        "project_age_days": cov["project_age_days"],
        "n_commits_total": r["n_commits"],
        "n_files_total": r["n_files"],
        "history_span_years": r["history_span_years"],
    }
    example = {
        "input": json.dumps(input_features, sort_keys=True),
        "output": r["survival_label"],
        "metadata_full_name": r["full_name"],
        "metadata_activity_bucket": r["activity_bucket"],
        "metadata_founder": r["founder"],
        "metadata_tfdd": r["tfdd"],
        "metadata_pre_tfdd_window": pre,
        "metadata_tfdd_snapshot_covariates": cov,
        "metadata_yearly_doa_tf_tables": r["yearly_tables"],
        "metadata_post_tfdd_monthly_commits": r["post_tfdd_monthly_commits"],
        "metadata_post_tfdd_months_available": r["post_tfdd_months_available"],
        "metadata_years_after_tfdd": r["years_after_tfdd"],
        "metadata_repo_meta": r["meta"],
        "metadata_repo_first_commit": r["repo_first_commit"],
        "metadata_repo_last_commit": r["repo_last_commit"],
        "metadata_task_type": "binary_classification",
        "metadata_n_classes": 2,
    }
    return example


def main():
    files = sorted(glob.glob(RESULTS_GLOB))
    logger.info(f"Found {len(files)} mined repo result files")
    qualified = []
    discard_reasons = {}
    for f in files:
        r = json.loads(Path(f).read_text())
        if r.get("status") == "qualified":
            qualified.append(r)
        else:
            reason = r.get("discard_reason", "unknown")
            discard_reasons[reason] = discard_reasons.get(reason, 0) + 1
    logger.info(f"Qualified repos: {len(qualified)}")
    logger.info(f"Discard reasons: {json.dumps(discard_reasons, indent=2)}")

    examples = [build_example(r) for r in qualified]
    output = {
        "metadata": {
            "source": "GitHub REST search API (candidate discovery) + git log (--filter=blob:none) "
                       "for full commit history mining",
            "description": "Single-founder GitHub repos with founder-only Truck-Factor-Developer-"
                            "Detachment (TFDD) events, per Avelino et al. ICPC'16 (DOA/TF algorithm) "
                            "and Avelino et al. ESEM'19 (TFDD/survival definitions). Each example is "
                            "one qualifying repo; input=pre-TFDD/snapshot covariates, output=survival "
                            "label (Active_survived / Inactive_did_not_survive).",
            "n_qualified": len(qualified),
            "discard_reason_counts": discard_reasons,
            "doa_formula": "DOA(d,f) = 3.293 + 1.098*FirstAuthor(d,f) + 0.164*Deliveries(d,f) "
                           "- 0.321*ln(1+Acceptances(d,f))",
            "tf_algorithm": "greedy removal of highest-file-count DOA-primary-author while "
                            "remaining-authors' file coverage >= 0.5",
        },
        "datasets": [
            {"dataset": "founder_departure_tfdd_corpus", "examples": examples}
        ],
    }
    OUT_PATH.write_text(json.dumps(output, indent=2))
    logger.info(f"Wrote {len(examples)} examples to {OUT_PATH}")


if __name__ == "__main__":
    main()
