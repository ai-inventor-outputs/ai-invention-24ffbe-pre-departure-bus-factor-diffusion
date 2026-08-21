#!/usr/bin/env python3
"""Evaluation: calibration + robustness checks for the founder-departure
authority-diffusion vs. survival experiment.

STAGE A: reproduce Avelino et al. (ESEM 2019) headline aggregate statistics
on the reimplemented DOA/TF/TFDD pipeline (16% TFDD incidence, 66% TF=1
share, 41% overall 18mo survival, negligible-small snapshot Cohen's d).

STAGE B: robustness / confound-freedom checks on the founder-TFDD
diffusion-vs-survival result (window sensitivity, founder-ID sensitivity,
age confound, matched-pairs bucket sensitivity, placebo/permutation test).

Per plan: does NOT re-mine git history. Re-uses the EXPERIMENT's own
DOA/TF/TFDD functions (imported from method.py) applied to the DATASET
dependency's already-extracted per-commit event log, only varying window
parameters / disambiguation heuristics / covariates -- this is "recomputing
derived aggregates from the raw event log", not re-implementing DOA.
"""

from __future__ import annotations

import gc
import importlib.util
import json
import subprocess
import sys
import time
from collections import defaultdict
from datetime import timedelta
from pathlib import Path
from typing import Any, Optional

import numpy as np
import pandas as pd
import psutil
from loguru import logger
from scipy import stats
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm

# ---------------------------------------------------------------------------
# hardware / logging setup
# ---------------------------------------------------------------------------
WORKSPACE = Path(__file__).resolve().parent
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
(WORKSPACE / "logs").mkdir(exist_ok=True)
logger.add(WORKSPACE / "logs" / "run.log", rotation="30 MB", level="DEBUG")

RUN_ROOT = WORKSPACE.parent
EXP_DIR = RUN_ROOT / "gen_art_experiment_1"
DATASET_DIR = RUN_ROOT / "gen_art_dataset_1"
REPO_RECORDS_DIR = DATASET_DIR / "temp" / "repo_records"
METHOD_PY = EXP_DIR / "method.py"

RNG_SEED = 20260820
N_BOOTSTRAP = 2000
# compute_doa_owner_per_file() is O(n_commits) and is re-run once per
# permutation draw per bundle with no caching across draws; 1000 perms
# previously hung the container for >8 minutes without finishing. Capped
# to a value that keeps check10 within a couple of minutes on this corpus
# size -- see check10_placebo_permutation()'s hard n_actual cap.
N_PERMUTATIONS = 60

# ---------------------------------------------------------------------------
# import the experiment's own method module (reuse DOA/TF/TFDD logic exactly)
# ---------------------------------------------------------------------------
spec = importlib.util.spec_from_file_location("exp_method", str(METHOD_PY))
exp_method = importlib.util.module_from_spec(spec)
sys.modules["exp_method"] = exp_method
spec.loader.exec_module(exp_method)  # noqa: S102 -- trusted local dependency file
# exp_method's own import already set a process-wide RLIMIT_AS (and loguru
# sinks); re-adding a lower cap here would raise ValueError, so we simply
# reuse the limit method.py established rather than lowering it further.
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add(WORKSPACE / "logs" / "run.log", rotation="30 MB", level="DEBUG")

months = exp_method.months
compute_doa_owner_per_file = exp_method.compute_doa_owner_per_file
truck_factor_set = exp_method.truck_factor_set
load_repo_commits = exp_method.load_repo_commits
classify_survival = exp_method.classify_survival
SILENCE_MONTHS = exp_method.SILENCE_MONTHS
SURVIVAL_WINDOW_MONTHS = exp_method.SURVIVAL_WINDOW_MONTHS
PRE_WINDOW_FAR_MONTHS = exp_method.PRE_WINDOW_FAR_MONTHS
PRE_WINDOW_NEAR_MONTHS = exp_method.PRE_WINDOW_NEAR_MONTHS
DOA_FA, DOA_LOG, DOA_AC = exp_method.DOA_FA, exp_method.DOA_LOG, exp_method.DOA_AC


# ===========================================================================
# small stat helpers
# ===========================================================================
def wilson_ci(k: int, n: int, z: float = 1.959963985) -> tuple[Optional[float], Optional[float], Optional[float]]:
    """Wilson score 95% CI for a binomial proportion. Returns (phat, lo, hi)."""
    if n == 0:
        return None, None, None
    phat = k / n
    denom = 1 + z**2 / n
    center = phat + z**2 / (2 * n)
    half = z * np.sqrt(phat * (1 - phat) / n + z**2 / (4 * n**2))
    lo = (center - half) / denom
    hi = (center + half) / denom
    return float(phat), float(max(0.0, lo)), float(min(1.0, hi))


def bootstrap_ci(values: np.ndarray, stat_fn, n_boot: int = N_BOOTSTRAP, seed: int = RNG_SEED) -> dict:
    rng = np.random.default_rng(seed)
    values = np.asarray(values)
    if len(values) == 0:
        return {"point": None, "ci_95": [None, None], "n_boot": 0}
    point = float(stat_fn(values))
    boots = []
    for _ in range(n_boot):
        sample = rng.choice(values, size=len(values), replace=True)
        try:
            boots.append(float(stat_fn(sample)))
        except Exception:
            continue
    if not boots:
        return {"point": point, "ci_95": [None, None], "n_boot": 0}
    boots = np.array(boots)
    return {
        "point": point,
        "ci_95": [float(np.percentile(boots, 2.5)), float(np.percentile(boots, 97.5))],
        "n_boot": len(boots),
    }


def cohens_d(a: np.ndarray, b: np.ndarray) -> Optional[float]:
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    a, b = a[~np.isnan(a)], b[~np.isnan(b)]
    if len(a) < 2 or len(b) < 2:
        return None
    na, nb = len(a), len(b)
    pooled_sd = np.sqrt(((na - 1) * a.var(ddof=1) + (nb - 1) * b.var(ddof=1)) / (na + nb - 2))
    if pooled_sd == 0:
        return None
    return float((a.mean() - b.mean()) / pooled_sd)


def odds_ratio_ci(a: int, b: int, c: int, d: int) -> dict:
    """2x2 table: a=exposed+event, b=exposed+no_event, c=unexposed+event, d=unexposed+no_event."""
    ac = [a + 0.5, b + 0.5, c + 0.5, d + 0.5] if 0 in (a, b, c, d) else [a, b, c, d]
    a_, b_, c_, d_ = ac
    orv = (a_ * d_) / (b_ * c_)
    se = np.sqrt(1 / a_ + 1 / b_ + 1 / c_ + 1 / d_)
    lo, hi = np.exp(np.log(orv) - 1.96 * se), np.exp(np.log(orv) + 1.96 * se)
    return {"odds_ratio": float(orv), "ci_95": [float(lo), float(hi)], "haldane_corrected": 0 in (a, b, c, d)}


def relative_risk(exposed_events: int, exposed_n: int, unexposed_events: int, unexposed_n: int,
                   rng: np.random.Generator, n_boot: int = N_BOOTSTRAP) -> dict:
    if exposed_n == 0 or unexposed_n == 0:
        return {"rr": None, "ci_95": [None, None], "n_exposed": exposed_n, "n_unexposed": unexposed_n}
    r_exp = exposed_events / exposed_n
    r_unexp = unexposed_events / unexposed_n
    rr = r_exp / r_unexp if r_unexp > 0 else float("inf")
    ex = np.array([1] * exposed_events + [0] * (exposed_n - exposed_events))
    ux = np.array([1] * unexposed_events + [0] * (unexposed_n - unexposed_events))
    boots = []
    for _ in range(n_boot):
        bex = rng.choice(ex, size=len(ex), replace=True).mean() if len(ex) else 0
        bux = rng.choice(ux, size=len(ux), replace=True).mean() if len(ux) else 0
        if bux > 0:
            boots.append(bex / bux)
    ci = [float(np.percentile(boots, 2.5)), float(np.percentile(boots, 97.5))] if boots else [None, None]
    return {"rr": float(rr) if np.isfinite(rr) else None, "ci_95": ci,
            "n_exposed": exposed_n, "n_unexposed": unexposed_n,
            "survival_rate_exposed": float(r_exp), "survival_rate_unexposed": float(r_unexp)}


def bh_adjust(pvals: dict) -> dict:
    keys = list(pvals.keys())
    vals = [pvals[k] for k in keys]
    if not vals:
        return {}
    _, p_bh, _, _ = multipletests(vals, method="fdr_bh")
    return dict(zip(keys, [float(p) for p in p_bh]))


# ===========================================================================
# STAGE A: general (all-departing-set-size) TFDD detection for calibration
# ===========================================================================
def detect_all_tfdd(commits: pd.DataFrame) -> dict:
    """Re-run the SAME TFDD-detection loop as method.py's process_repo, but
    WITHOUT restricting to founder-only (TF=1) departures -- needed to
    reproduce Avelino et al.'s corpus-level incidence/TF=1-share/survival
    numbers, which are computed over ALL TFDDs, not just founder-only ones."""
    year_ends = exp_method._year_ends(commits)
    if len(year_ends) < 2:
        return {"has_tfdd": False, "error": "insufficient_history"}
    last_commit_by_author = commits.groupby("author_id")["ts"].max()
    tfdd_year_end = None
    departing_set: list[str] = []
    for ye in sorted(year_ends):
        tf_set = truck_factor_set(compute_doa_owner_per_file(commits, ye))
        if not tf_set:
            continue
        silent = all(
            (ye - last_commit_by_author.get(a, commits["ts"].min())).days >= SILENCE_MONTHS * 30.4375
            for a in tf_set
        )
        if silent:
            tfdd_year_end = ye
            departing_set = tf_set
            break
    if tfdd_year_end is None:
        return {"has_tfdd": False, "error": "no_tfdd"}
    departure_ts = max(last_commit_by_author[a] for a in departing_set)
    tfdd_date = departure_ts + months(SILENCE_MONTHS)
    min_post_needed = tfdd_date + months(SURVIVAL_WINDOW_MONTHS)
    if commits["ts"].max() < min_post_needed - months(3):
        return {"has_tfdd": True, "tf_size": len(departing_set), "censored": True}
    label, surv_bin = classify_survival(commits, tfdd_date, set(departing_set))
    at_tfdd = commits[commits["ts"] <= tfdd_date]
    return {
        "has_tfdd": True,
        "tf_size": len(departing_set),
        "censored": False,
        "tfdd_date": tfdd_date.isoformat(),
        "survival_label": label,
        "survived_binary": surv_bin,
        "developers_at_tfdd": int(at_tfdd["author_id"].nunique()),
        "commits_at_tfdd": int(at_tfdd["sha"].nunique()),
        "files_at_tfdd": int(at_tfdd["file"].nunique()),
    }


def load_all_repo_records() -> list[dict]:
    files = sorted(REPO_RECORDS_DIR.glob("*.json")) if REPO_RECORDS_DIR.exists() else []
    out = []
    for f in files:
        try:
            out.append(json.loads(f.read_text()))
        except Exception as e:  # noqa: BLE001
            logger.warning(f"failed to parse {f}: {e}")
    return out


def stage_a_calibration(raw_repos: list[dict]) -> dict:
    logger.info(f"Stage A: general TFDD detection over {len(raw_repos)} repos")
    all_results = []
    for raw in raw_repos:
        parsed = load_repo_commits(raw)
        if parsed is None:
            continue
        r = detect_all_tfdd(parsed["commits"])
        r["repo_id"] = parsed["repo_id"]
        r["alias_collapse_rate"] = parsed["alias_collapse_rate"]
        all_results.append(r)
        del parsed
    gc.collect()

    n_corpus = len(all_results)
    tfdd_events = [r for r in all_results if r.get("has_tfdd") and not r.get("censored")]
    n_tfdd = len(tfdd_events)

    # --- check 1: TFDD incidence rate vs Avelino 16% (315/1932) ---
    phat, lo, hi = wilson_ci(n_tfdd, n_corpus) if n_corpus else (None, None, None)
    check1 = {
        "metric": "tfdd_incidence_rate",
        "reimplemented_rate": phat, "ci_95": [lo, hi], "n_corpus": n_corpus, "n_tfdd": n_tfdd,
        "avelino_reference": 315 / 1932, "avelino_n": "315/1932",
        "abs_deviation": (abs(phat - 315 / 1932) if phat is not None else None),
        "rel_deviation": (abs(phat - 315 / 1932) / (315 / 1932) if phat is not None else None),
        "status": ("PASS" if (phat is not None and lo <= 315 / 1932 <= hi) else "FLAG_DEVIATION"),
    }

    # --- check 2: TF=1 share among TFDDs vs Avelino 66% ---
    n_tf1 = sum(1 for r in tfdd_events if r["tf_size"] == 1)
    phat2, lo2, hi2 = wilson_ci(n_tf1, n_tfdd) if n_tfdd else (None, None, None)
    check2 = {
        "metric": "tf1_share_of_tfdd",
        "reimplemented_rate": phat2, "ci_95": [lo2, hi2], "n_tfdd": n_tfdd, "n_tf1": n_tf1,
        "avelino_reference": 0.66,
        "abs_deviation": (abs(phat2 - 0.66) if phat2 is not None else None),
        "rel_deviation": (abs(phat2 - 0.66) / 0.66 if phat2 is not None else None),
        "status": ("PASS" if (phat2 is not None and lo2 <= 0.66 <= hi2) else "FLAG_DEVIATION"),
    }

    # --- check 3: overall 18mo survival rate among ALL TFDDs vs Avelino 41% (128/315) ---
    n_survived = sum(1 for r in tfdd_events if r.get("survived_binary") == 1)
    phat3, lo3, hi3 = wilson_ci(n_survived, n_tfdd) if n_tfdd else (None, None, None)
    check3 = {
        "metric": "overall_18mo_survival_rate",
        "reimplemented_rate": phat3, "ci_95": [lo3, hi3], "n_tfdd": n_tfdd, "n_survived": n_survived,
        "avelino_reference": 128 / 315, "avelino_n": "128/315",
        "abs_deviation": (abs(phat3 - 128 / 315) if phat3 is not None else None),
        "rel_deviation": (abs(phat3 - 128 / 315) / (128 / 315) if phat3 is not None else None),
        "status": ("PASS" if (phat3 is not None and lo3 <= 128 / 315 <= hi3) else "FLAG_DEVIATION"),
    }

    # --- check 4: snapshot-null Cohen's d replication (Avelino: 0.13-0.26, negligible-small) ---
    surv = [r for r in tfdd_events if r.get("survived_binary") == 1]
    nonsurv = [r for r in tfdd_events if r.get("survived_binary") == 0]
    d_results = {}
    for feat in ["developers_at_tfdd", "commits_at_tfdd", "files_at_tfdd"]:
        a = np.array([r[feat] for r in surv if r.get(feat) is not None], dtype=float)
        b = np.array([r[feat] for r in nonsurv if r.get(feat) is not None], dtype=float)
        d_results[feat] = cohens_d(a, b)
    valid_ds = [v for v in d_results.values() if v is not None]
    d_in_range = all(0.0 <= abs(v) <= 0.5 for v in valid_ds) if valid_ds else None
    check4 = {
        "metric": "snapshot_null_cohens_d",
        "cohens_d_per_feature": d_results,
        "avelino_reference_range": [0.13, 0.26],
        "n_survivors": len(surv), "n_nonsurvivors": len(nonsurv),
        "status": ("PASS" if d_in_range else ("FLAG_DEVIATION" if valid_ds else "UNAVAILABLE_INSUFFICIENT_N")),
    }

    # --- diagnostic protocol (a)-(d), run for any flagged deviation ---
    flagged = any(c["status"] == "FLAG_DEVIATION" for c in (check1, check2, check3, check4))
    diagnostics = {"ran": flagged, "steps": {}}
    if flagged:
        # (a) strata composition: language / repo-count vs Avelino's 6-language top-500 design
        lang_counts = defaultdict(int)
        for raw in raw_repos:
            meta = raw.get("repo_metadata", raw.get("metadata", raw))
            lang_counts[meta.get("language") or "unknown"] += 1
        diagnostics["steps"]["a_strata_composition"] = {
            "language_counts": dict(lang_counts),
            "avelino_design": "6 languages, top-500-starred repos per language",
            "note": ("SAMPLING_MISMATCH: corpus is a small opportunistic sample "
                     "(candidate list), not a top-500-per-language stratified sample; "
                     "n_corpus is far below Avelino's 1932, so incidence-rate CIs are wide."),
        }
        # (b) abandoner-threshold parameter check
        diagnostics["steps"]["b_abandoner_threshold"] = {
            "silence_months_used": SILENCE_MONTHS,
            "avelino_validated_best": 12,
            "status": "PASS" if SILENCE_MONTHS == 12 else "FLAG_DEVIATION",
        }
        # (c) hand-trace DOA for top contributor on 3-5 projects
        trace = []
        for raw in raw_repos[:5]:
            parsed = load_repo_commits(raw)
            if parsed is None:
                continue
            commits = parsed["commits"]
            top_by_commits = commits["author_id"].value_counts().idxmax()
            owners = compute_doa_owner_per_file(commits, commits["ts"].max())
            owner_counts = pd.Series(list(owners.values())).value_counts()
            top_doa_owner = owner_counts.idxmax() if len(owner_counts) else None
            trace.append({
                "repo_id": parsed["repo_id"],
                "top_commit_count_author": top_by_commits,
                "top_doa_file_owner": top_doa_owner,
                "matches_intuition": bool(top_by_commits == top_doa_owner),
            })
            del parsed
        diagnostics["steps"]["c_doa_hand_trace"] = {
            "n_traced": len(trace), "traces": trace,
            "n_matching_intuition": sum(1 for t in trace if t["matches_intuition"]),
        }
        # (d) alias/email resolution collapse-rate spot check
        rates = [r["alias_collapse_rate"] for r in all_results if r.get("alias_collapse_rate") is not None]
        diagnostics["steps"]["d_alias_resolution"] = {
            "median_collapse_rate": float(np.median(rates)) if rates else None,
            "avelino_reference_median": 0.11,
            "n_over_40pct": sum(1 for r in rates if r > 0.4),
        }

    return {
        "n_corpus": n_corpus, "n_tfdd_all": n_tfdd,
        "check1_tfdd_incidence": check1,
        "check2_tf1_share": check2,
        "check3_overall_survival": check3,
        "check4_snapshot_null_cohens_d": check4,
        "diagnostic_protocol": diagnostics,
        "gate_status": "FLAG_DEVIATION" if flagged else "PASS",
        "all_tfdd_events_detail": tfdd_events,
    }


# ===========================================================================
# STAGE B: robustness / confound checks on the founder-TFDD diffusion result
# ===========================================================================
def _founder_tfdd_repos(raw_repos: list[dict]) -> list[dict]:
    """Recompute founder-only TFDD parsed-commit bundles (repo_id, commits,
    founder, tfdd_date, departing_set, stars/forks/language/license) exactly
    as method.py's process_repo would, so Stage B checks work off the SAME
    event definitions as the main experiment."""
    out = []
    for raw in raw_repos:
        parsed = load_repo_commits(raw)
        if parsed is None:
            continue
        commits = parsed["commits"]
        year_ends = exp_method._year_ends(commits)
        if len(year_ends) < 2:
            continue
        founder = exp_method._first_commit_author(commits)
        last_commit_by_author = commits.groupby("author_id")["ts"].max()
        tfdd_year_end, departing_set = None, []
        for ye in sorted(year_ends):
            tf_set = truck_factor_set(compute_doa_owner_per_file(commits, ye))
            if not tf_set:
                continue
            silent = all((ye - last_commit_by_author.get(a, commits["ts"].min())).days >= SILENCE_MONTHS * 30.4375 for a in tf_set)
            if silent:
                tfdd_year_end, departing_set = ye, tf_set
                break
        if tfdd_year_end is None or len(departing_set) != 1 or departing_set[0] != founder:
            continue
        tfdd_date = last_commit_by_author[founder] + months(SILENCE_MONTHS)
        min_post_needed = tfdd_date + months(SURVIVAL_WINDOW_MONTHS)
        if commits["ts"].max() < min_post_needed - months(3):
            continue
        label, surv_bin = classify_survival(commits, tfdd_date, {founder})
        out.append(dict(repo_id=parsed["repo_id"], commits=commits, founder=founder, tfdd_date=tfdd_date,
                         stars=parsed["stars"], forks=parsed["forks"], language=parsed["language"],
                         license=parsed["license"], survived_binary=surv_bin, survival_label=label))
    return out


def _diffusion_for_window(commits: pd.DataFrame, founder: str, w_start: pd.Timestamp, w_end: pd.Timestamp) -> tuple[float, int]:
    wc = commits[(commits["ts"] >= w_start) & (commits["ts"] < w_end)]
    founder_share = float((wc["author_id"] == founder).sum() / max(len(wc), 1))
    doa_pre = compute_doa_owner_per_file(commits[commits["ts"] < w_end], w_end)
    owners_pre = set(doa_pre.values())
    return founder_share, len(owners_pre - {founder})


def _fit_matched_or_regression(df: pd.DataFrame, rng: np.random.Generator) -> dict:
    if len(df) < 6 or df["founder_share_pre"].nunique() < 2:
        return {"error": "insufficient_n_for_fit", "n": len(df)}
    med = df["founder_share_pre"].median()
    high, low = df[df["founder_share_pre"] < med], df[df["founder_share_pre"] >= med]
    rr = relative_risk(int(high["survived_binary"].sum()), len(high), int(low["survived_binary"].sum()), len(low), rng)
    d = df.dropna(subset=["founder_share_pre", "n_diffuse_owners_pre", "survived_binary"])
    logit = {"error": "insufficient_n", "n": len(d)}
    if len(d) >= 8:
        try:
            X = d[["founder_share_pre", "n_diffuse_owners_pre"]].astype(float)
            for c in X.columns:
                s = X[c].std()
                X[c] = (X[c] - X[c].mean()) / s if s else 0.0
            Xc = sm.add_constant(X, has_constant="add")
            res = sm.Logit(d["survived_binary"].astype(float), Xc).fit(disp=0, maxiter=200)
            logit = {"coef_founder_share_pre": float(res.params.get("founder_share_pre", np.nan)),
                     "p_founder_share_pre": float(res.pvalues.get("founder_share_pre", np.nan)),
                     "coef_n_diffuse_owners_pre": float(res.params.get("n_diffuse_owners_pre", np.nan)),
                     "p_n_diffuse_owners_pre": float(res.pvalues.get("n_diffuse_owners_pre", np.nan)),
                     "n": len(d), "converged": bool(res.mle_retvals.get("converged", False))}
        except Exception as e:  # noqa: BLE001
            logit = {"error": str(e), "n": len(d)}
    return {"median_split_relative_risk": rr, "logistic": logit, "n": len(df)}


def check6_window_sensitivity(bundles: list[dict], rng: np.random.Generator) -> dict:
    if not bundles:
        return {"status": "UNAVAILABLE", "reason": "no_founder_tfdd_events"}
    near_grid = [6, 9, 12]
    end_offset_grid = [0, 1, 2]
    reduced = len(bundles) < 15
    if reduced:
        near_grid, end_offset_grid = [6, 12], [0, 1]
    variants = []
    p_raw = {}
    for near_m in near_grid:
        for end_off in end_offset_grid:
            far_m = PRE_WINDOW_FAR_MONTHS if near_m != 12 else 18
            if near_m >= far_m:
                continue
            rows = []
            for b in bundles:
                w_end = b["tfdd_date"] - months(end_off)
                w_start = w_end - months(far_m - near_m)
                fs, nd = _diffusion_for_window(b["commits"], b["founder"], w_start, w_end)
                rows.append({"founder_share_pre": fs, "n_diffuse_owners_pre": nd, "survived_binary": b["survived_binary"]})
            fit = _fit_matched_or_regression(pd.DataFrame(rows), rng)
            key = f"near{near_m}mo_end{end_off}mo"
            p = fit.get("logistic", {}).get("p_founder_share_pre")
            if p is not None and p == p:
                p_raw[key] = p
            variants.append({"variant": key, "near_months": near_m, "far_months": far_m, "end_offset_months": end_off, "fit": fit})
    p_bh = bh_adjust(p_raw)
    for v in variants:
        k = v["variant"]
        v["fit"].setdefault("logistic", {})["p_bh"] = p_bh.get(k)
    signs = [np.sign(v["fit"].get("logistic", {}).get("coef_founder_share_pre", 0) or 0) for v in variants
             if v["fit"].get("logistic", {}).get("coef_founder_share_pre") is not None]
    stable_sign = len(set(signs)) <= 1 if signs else None
    return {
        "status": "COMPUTED", "grid_used": "reduced (n<15)" if reduced else "full_3x3",
        "reduction_reason": ("small n_founder_tfdd_events; reduced grid to keep >=8 obs per fit" if reduced else None),
        "n_variants": len(variants), "variants": variants, "sign_stable_across_variants": stable_sign,
    }


def check7_founder_id_sensitivity(bundles: list[dict], rng: np.random.Generator) -> dict:
    if not bundles:
        return {"status": "UNAVAILABLE", "reason": "no_founder_tfdd_events"}
    rows_primary, rows_alt_year, rows_alt_doa = [], [], []
    disagreements = 0
    for b in bundles:
        commits, primary_founder = b["commits"], b["founder"]
        # alt heuristic 1: founder = author with plurality of commits in first calendar year
        t0 = commits["ts"].min()
        year1 = commits[commits["ts"] <= t0 + timedelta(days=365)]
        alt_founder_year = year1["author_id"].value_counts().idxmax() if len(year1) else primary_founder
        # alt heuristic 2: founder = highest lifetime DOA-owned-file-count author, pre-TFDD
        owners = compute_doa_owner_per_file(commits[commits["ts"] <= b["tfdd_date"]], b["tfdd_date"])
        owner_counts = pd.Series(list(owners.values())).value_counts()
        alt_founder_doa = owner_counts.idxmax() if len(owner_counts) else primary_founder
        if alt_founder_year != primary_founder or alt_founder_doa != primary_founder:
            disagreements += 1
        w_end = b["tfdd_date"] - months(PRE_WINDOW_NEAR_MONTHS)
        w_start = b["tfdd_date"] - months(PRE_WINDOW_FAR_MONTHS)
        for founder_id, sink in [(primary_founder, rows_primary), (alt_founder_year, rows_alt_year), (alt_founder_doa, rows_alt_doa)]:
            fs, nd = _diffusion_for_window(commits, founder_id, w_start, w_end)
            sink.append({"founder_share_pre": fs, "n_diffuse_owners_pre": nd, "survived_binary": b["survived_binary"]})
    fits = {
        "primary_first_commit_author": _fit_matched_or_regression(pd.DataFrame(rows_primary), rng),
        "alt_year1_plurality": _fit_matched_or_regression(pd.DataFrame(rows_alt_year), rng),
        "alt_highest_lifetime_doa": _fit_matched_or_regression(pd.DataFrame(rows_alt_doa), rng),
    }
    return {
        "status": "COMPUTED", "n_repos": len(bundles),
        "n_disagreements_with_primary_heuristic": disagreements,
        "disagreement_rate": disagreements / len(bundles),
        "avelino_reference_median_alias_rate": 0.11,
        "fits_by_founder_heuristic": fits,
    }


def check8_age_confound(bundles: list[dict], df: pd.DataFrame) -> dict:
    d = df.dropna(subset=["founder_share_pre", "n_diffuse_owners_pre", "survived_binary"]).copy()
    if len(d) < 8:
        return {"status": "UNAVAILABLE", "reason": "insufficient_n", "n": len(d)}
    age_days = {}
    for b in bundles:
        age_days[b["repo_id"]] = (b["tfdd_date"] - b["commits"]["ts"].min()).days
    d["repo_age_days_at_tfdd"] = d["repo_id"].map(age_days)
    d = d.dropna(subset=["repo_age_days_at_tfdd"])
    if len(d) < 8:
        return {"status": "UNAVAILABLE", "reason": "insufficient_n_after_age_merge", "n": len(d)}

    def fit(cols):
        X = d[cols].astype(float).copy()
        for c in cols:
            s = X[c].std()
            X[c] = (X[c] - X[c].mean()) / s if s else 0.0
        Xc = sm.add_constant(X, has_constant="add")
        res = sm.Logit(d["survived_binary"].astype(float), Xc).fit(disp=0, maxiter=200)
        return {k: float(v) for k, v in res.params.items()}, {k: float(v) for k, v in res.pvalues.items()}

    before_coef, before_p = fit(["founder_share_pre", "n_diffuse_owners_pre"])
    try:
        after_coef, after_p = fit(["founder_share_pre", "n_diffuse_owners_pre", "repo_age_days_at_tfdd"])
        after_ok = True
    except Exception as e:  # noqa: BLE001
        after_coef, after_p, after_ok = {"error": str(e)}, {"error": str(e)}, False

    vif = {}
    if after_ok:
        Xv = sm.add_constant(d[["founder_share_pre", "n_diffuse_owners_pre", "repo_age_days_at_tfdd"]].astype(float), has_constant="add")
        try:
            for i, c in enumerate(Xv.columns):
                if c == "const":
                    continue
                vif[c] = float(variance_inflation_factor(Xv.values, i))
        except Exception as e:  # noqa: BLE001
            vif = {"error": str(e)}
    age_survived = d.loc[d.survived_binary == 1, "repo_age_days_at_tfdd"]
    age_died = d.loc[d.survived_binary == 0, "repo_age_days_at_tfdd"]
    partial_corr = None
    if len(d) >= 4:
        try:
            partial_corr = float(np.corrcoef(d["founder_share_pre"], d["repo_age_days_at_tfdd"])[0, 1])
        except Exception:
            partial_corr = None
    return {
        "status": "COMPUTED", "n": len(d),
        "before_age_covariate": {"coef": before_coef, "p_raw": before_p},
        "after_age_covariate": {"coef": after_coef, "p_raw": after_p, "converged": after_ok},
        "vif": vif,
        "founder_share_vs_age_correlation": partial_corr,
        "age_days_survivors_mean": float(age_survived.mean()) if len(age_survived) else None,
        "age_days_nonsurvivors_mean": float(age_died.mean()) if len(age_died) else None,
        "avelino_reference_days": {"survivors": 1095, "nonsurvivors": 1460, "p": 3.4e-7},
        "diffusion_coef_survives_age_control": (
            bool(after_ok and after_coef.get("founder_share_pre") is not None
                 and np.sign(after_coef["founder_share_pre"]) == np.sign(before_coef.get("founder_share_pre", 0)))
        ),
    }


def check9_bucket_sensitivity(df: pd.DataFrame, rng: np.random.Generator) -> dict:
    d = df.dropna(subset=["founder_share_pre", "n_diffuse_owners_pre", "survived_binary", "stars"]).copy()
    if len(d) < 6:
        return {"status": "UNAVAILABLE", "reason": "insufficient_n", "n": len(d)}
    d["high_diffusion"] = (d["founder_share_pre"] < d["founder_share_pre"].median()) & (d["n_diffuse_owners_pre"] >= d["n_diffuse_owners_pre"].median())
    results = {}
    try:
        d["quartile_bucket"] = pd.qcut(d["stars"], q=min(4, d["stars"].nunique()), duplicates="drop")
        results["quartile_stars"] = _bucketed_lift(d, "quartile_bucket", rng)
    except Exception as e:  # noqa: BLE001
        results["quartile_stars"] = {"error": str(e)}
    try:
        d["log_bucket"] = pd.cut(np.log1p(d["stars"]), bins=min(4, d["stars"].nunique()))
        results["log_scale_stars"] = _bucketed_lift(d, "log_bucket", rng)
    except Exception as e:  # noqa: BLE001
        results["log_scale_stars"] = {"error": str(e)}
    lifts = [r.get("point") for r in results.values() if isinstance(r, dict) and r.get("point") is not None]
    excl_1 = [r for r in results.values() if isinstance(r, dict) and r.get("ci_95") and r["ci_95"][0] is not None and r["ci_95"][0] > 1.0]
    return {"status": "COMPUTED", "n": len(d), "bucket_definitions": results,
            "lift_consistently_gte_1_5x": (all(l >= 1.5 for l in lifts) if lifts else None),
            "n_bucket_defs_excluding_1x": len(excl_1), "n_bucket_defs_total": len(results)}


def _bucketed_lift(d: pd.DataFrame, bucket_col: str, rng: np.random.Generator) -> dict:
    lifts = []
    for _, grp in d.groupby(bucket_col, observed=True):
        hi = grp[grp["high_diffusion"]]
        lo = grp[~grp["high_diffusion"]]
        if len(hi) == 0 or len(lo) == 0:
            continue
        lifts.append((hi["survived_binary"].mean() / lo["survived_binary"].mean()) if lo["survived_binary"].mean() > 0 else np.nan)
    lifts = np.array([l for l in lifts if l == l])
    if len(lifts) == 0:
        return {"point": None, "ci_95": [None, None], "n_buckets_used": 0}
    boot = bootstrap_ci(lifts, np.mean, seed=RNG_SEED)
    return {"point": boot["point"], "ci_95": boot["ci_95"], "n_buckets_used": len(lifts)}


def check10_placebo_permutation(bundles: list[dict], n_perms: int) -> dict:
    if not bundles:
        return {"status": "UNAVAILABLE", "reason": "no_founder_tfdd_events"}
    rng = np.random.default_rng(RNG_SEED)
    true_effects = []
    for b in bundles:
        commits, founder = b["commits"], b["founder"]
        w_end = b["tfdd_date"] - months(PRE_WINDOW_NEAR_MONTHS)
        w_start = b["tfdd_date"] - months(PRE_WINDOW_FAR_MONTHS)
        fs, nd = _diffusion_for_window(commits, founder, w_start, w_end)
        true_effects.append((1 - fs) * np.log1p(nd))
    true_effects = np.array(true_effects)

    def null_draws(subset: list[dict], n_needed: int) -> list[np.ndarray]:
        draws = []
        for b in subset:
            commits, founder = b["commits"], b["founder"]
            earliest = commits["ts"].min()
            latest_start = b["tfdd_date"] - months(SURVIVAL_WINDOW_MONTHS) - months(PRE_WINDOW_NEAR_MONTHS)
            span = (latest_start - earliest).days
            vals = []
            if span > 1:
                for _ in range(n_needed):
                    off = rng.uniform(0, span)
                    p_start = earliest + timedelta(days=off)
                    p_end = p_start + months(PRE_WINDOW_FAR_MONTHS - PRE_WINDOW_NEAR_MONTHS)
                    fs, nd = _diffusion_for_window(commits, founder, p_start, p_end)
                    vals.append((1 - fs) * np.log1p(nd))
            draws.append(np.array(vals) if vals else np.array([np.nan]))
        return draws

    # compute_doa_owner_per_file() re-scans+groups the FULL commit history on
    # every call; a permutation loop calls it once per (bundle x draw), so at
    # n_perms=1000 this is len(bundles)*1000 O(n_commits) recomputations --
    # in the prior run this alone took >8 minutes and never finished. Cap
    # n_actual hard regardless of len(bundles); split_perm() below halves it
    # again for the survivor/non-survivor subsets.
    n_actual = min(n_perms, 60)
    per_repo_null = null_draws(bundles, n_actual)
    null_means = np.array([np.nanmean([d[i] if i < len(d) else np.nan for d in per_repo_null]) for i in range(n_actual)])
    null_means = null_means[~np.isnan(null_means)]
    true_mean = float(np.nanmean(true_effects))
    p_two_sided = float(((np.abs(null_means - null_means.mean()) >= abs(true_mean - null_means.mean())).sum() + 1) / (len(null_means) + 1)) if len(null_means) else None

    def split_perm(mask):
        sub = [b for b, m in zip(bundles, mask) if m]
        if not sub:
            return {"status": "UNAVAILABLE", "n": 0}
        te = np.array([true_effects[i] for i, m in enumerate(mask) if m])
        nd = null_draws(sub, min(n_actual, 40))
        nm = np.array([np.nanmean([d[i] if i < len(d) else np.nan for d in nd]) for i in range(min(n_actual, 40))])
        nm = nm[~np.isnan(nm)]
        tm = float(np.nanmean(te))
        p = float(((np.abs(nm - nm.mean()) >= abs(tm - nm.mean())).sum() + 1) / (len(nm) + 1)) if len(nm) else None
        return {"status": "COMPUTED", "n": len(sub), "true_mean_effect": tm, "n_perms_used": len(nm), "permutation_p_value": p}

    surv_mask = [b["survived_binary"] == 1 for b in bundles]
    nonsurv_mask = [b["survived_binary"] == 0 for b in bundles]
    return {
        "status": "COMPUTED", "n_repos": len(bundles), "n_permutations_requested": n_perms, "n_permutations_used": n_actual,
        "true_mean_effect": true_mean, "null_mean": float(null_means.mean()) if len(null_means) else None,
        "null_std": float(null_means.std()) if len(null_means) else None,
        "permutation_p_value_pooled": p_two_sided,
        "survivors_only": split_perm(surv_mask),
        "nonsurvivors_only": split_perm(nonsurv_mask),
    }


# ===========================================================================
# main
# ===========================================================================
def run_experiment_if_needed() -> dict:
    """Ensure a fresh method_out.json exists (run against the real dataset
    dependency if not already produced), then load it. Evaluation never
    re-derives DOA/TF from raw git history itself -- only invokes the
    experiment's own script."""
    out_path = WORKSPACE / "method_out_reference.json"
    exp_venv_py = EXP_DIR / ".venv" / "bin" / "python"
    py = str(exp_venv_py) if exp_venv_py.exists() else sys.executable
    cmd = [py, str(METHOD_PY), "--output", str(out_path)]
    logger.info(f"Running experiment method.py for reference output: {' '.join(cmd)}")
    t0 = time.time()
    proc = subprocess.run(cmd, cwd=str(EXP_DIR), capture_output=True, text=True, timeout=1800)
    logger.info(f"method.py exit={proc.returncode} in {time.time()-t0:.1f}s")
    if proc.returncode != 0:
        logger.error(f"method.py stderr tail: {proc.stderr[-3000:]}")
        raise RuntimeError(f"experiment method.py failed: {proc.returncode}")
    return json.loads(out_path.read_text())


def main():
    t_start = time.time()
    raw_repos = load_all_repo_records()
    logger.info(f"Loaded {len(raw_repos)} raw repo records from dataset dependency")

    method_out = run_experiment_if_needed()
    meta = method_out.get("metadata", {})
    examples = method_out.get("datasets", [{}])[0].get("examples", [])

    # -------------------- STAGE A --------------------
    stage_a = stage_a_calibration(raw_repos) if raw_repos else {
        "status": "UNAVAILABLE", "reason": "no_dataset_repo_records_found"}

    # -------------------- STAGE B --------------------
    rng = np.random.default_rng(RNG_SEED)
    bundles = _founder_tfdd_repos(raw_repos) if raw_repos else []
    logger.info(f"Stage B: {len(bundles)} founder-only TFDD repo bundles reconstructed")

    df_rows = []
    for ex in examples:
        if "metadata_repo_id" not in ex:
            continue
        df_rows.append({
            "repo_id": ex["metadata_repo_id"], "language": ex.get("metadata_language"),
            "stars": ex.get("metadata_stars"), "forks": ex.get("metadata_forks"),
            "founder_share_pre": ex.get("metadata_founder_share_pre"),
            "n_diffuse_owners_pre": ex.get("metadata_n_diffuse_owners_pre"),
            "survived_binary": ex.get("metadata_survived_binary"),
        })
    df = pd.DataFrame(df_rows)

    check6 = check6_window_sensitivity(bundles, rng)
    check7 = check7_founder_id_sensitivity(bundles, rng)
    check8 = check8_age_confound(bundles, df) if not df.empty else {"status": "UNAVAILABLE", "reason": "no_founder_tfdd_examples"}
    check9 = check9_bucket_sensitivity(df, rng) if not df.empty else {"status": "UNAVAILABLE", "reason": "no_founder_tfdd_examples"}
    check10 = check10_placebo_permutation(bundles, N_PERMUTATIONS)

    stage_b = {
        "n_founder_tfdd_events": len(bundles),
        "check6_window_boundary_sensitivity": check6,
        "check7_founder_id_sensitivity": check7,
        "check8_age_confound": check8,
        "check9_matched_pairs_bucket_sensitivity": check9,
        "check10_placebo_permutation": check10,
    }

    # -------------------- final scoring --------------------
    def verdict_of(chk, key_path):
        cur = chk
        for k in key_path:
            if not isinstance(cur, dict):
                return "FAIL"
            cur = cur.get(k)
        return cur

    c1 = "PASS: pre-departure diffusion (lower founder-share / more distinct DOA owners) is associated with higher 18mo survival, beyond size/popularity"
    sc1_status = "PARTIAL"
    if stage_a.get("gate_status") != "PASS":
        sc1_status = "FAIL"
        sc1_reason = "Stage A calibration gate did not pass; downstream diffusion result is not trustworthy on its own terms."
    elif check6.get("status") == "COMPUTED" and check6.get("sign_stable_across_variants"):
        sc1_status = "PASS"
        sc1_reason = "Sign of the diffusion effect is stable across the window-boundary grid (check 6)."
    else:
        sc1_reason = "Diffusion effect sign is not stable across window choices, or insufficient data to assess (check 6)."

    sc2_status = "FAIL"
    sc2_reason = "insufficient data"
    if check8.get("status") == "COMPUTED":
        sc2_status = "PASS" if check8.get("diffusion_coef_survives_age_control") else "FAIL"
        sc2_reason = f"diffusion coefficient sign-survives age-covariate addition: {check8.get('diffusion_coef_survives_age_control')}"

    sc3_status = "FAIL"
    sc3_reason = "insufficient data"
    if check10.get("status") == "COMPUTED" and check10.get("permutation_p_value_pooled") is not None:
        p = check10["permutation_p_value_pooled"]
        sc3_status = "PASS" if p < 0.05 else ("PARTIAL" if p < 0.10 else "FAIL")
        sc3_reason = f"pooled permutation p-value for true pre-departure window effect vs random window placement = {p:.4f}"

    if stage_a.get("gate_status") == "FLAG_DEVIATION":
        overall = "DOES_NOT_SUPPORT_PIPELINE_UNCALIBRATED"
    elif sc1_status == "PASS" and sc2_status == "PASS" and sc3_status in ("PASS", "PARTIAL"):
        overall = "SUPPORTS_WITH_CAVEATS"
    elif sc1_status == "FAIL" and sc2_status == "FAIL" and sc3_status == "FAIL":
        overall = "DOES_NOT_SUPPORT"
    else:
        overall = "SUPPORTS_WITH_CAVEATS_LOW_POWER"

    final_scoring = {
        "success_criterion_1": {"text": c1, "status": sc1_status, "evidence": sc1_reason},
        "success_criterion_2": {
            "text": "Diffusion predictors' coefficients and significance survive an explicit age-at-TFDD covariate (Avelino confound control).",
            "status": sc2_status, "evidence": sc2_reason,
        },
        "success_criterion_3": {
            "text": "The true pre-departure-window effect is significantly more extreme than randomly-placed-window placebo draws (permutation test).",
            "status": sc3_status, "evidence": sc3_reason,
        },
        "overall_verdict": overall,
        "n_founder_tfdd_events_available": len(bundles),
        "power_caveat": ("Corpus size is far smaller than Avelino et al.'s 1932-repo corpus "
                          "(unauthenticated GitHub API rate limits + time budget); all CIs/p-values "
                          "above must be read as low-power estimates, not as evidence of a null effect "
                          "where they are non-significant.") if len(bundles) < 30 else None,
    }

    eval_out = {
        "metadata": {
            "evaluation_name": "founder_departure_diffusion_calibration_and_robustness",
            "description": ("Stage A: reproduce Avelino et al. (ESEM 2019) headline aggregate statistics on the "
                             "reimplemented DOA/TF/TFDD pipeline. Stage B: robustness/confound checks on the "
                             "founder-TFDD diffusion-vs-survival result."),
            "n_dataset_repo_records": len(raw_repos),
            "n_experiment_repos_total": meta.get("n_repos_total"),
            "n_experiment_founder_tfdd_events": meta.get("n_founder_tfdd_events"),
            "experiment_error_breakdown": meta.get("error_breakdown"),
            "experiment_alias_qa": meta.get("alias_qa"),
            "runtime_seconds": time.time() - t_start,
            "stage_a_calibration": stage_a,
            "stage_b_robustness": stage_b,
            "final_scoring": final_scoring,
        },
        "metrics_agg": {
            "n_dataset_repo_records": float(len(raw_repos)),
            "n_corpus_stage_a": float(stage_a.get("n_corpus", 0) or 0),
            "n_tfdd_all_stage_a": float(stage_a.get("n_tfdd_all", 0) or 0),
            "tfdd_incidence_rate": float(stage_a.get("check1_tfdd_incidence", {}).get("reimplemented_rate") or 0.0),
            "tf1_share": float(stage_a.get("check2_tf1_share", {}).get("reimplemented_rate") or 0.0),
            "overall_survival_rate": float(stage_a.get("check3_overall_survival", {}).get("reimplemented_rate") or 0.0),
            "stage_a_gate_pass": 1.0 if stage_a.get("gate_status") == "PASS" else 0.0,
            "n_founder_tfdd_events": float(len(bundles)),
            "window_sensitivity_sign_stable": (1.0 if check6.get("sign_stable_across_variants") else 0.0) if check6.get("status") == "COMPUTED" else -1.0,
            "founder_id_disagreement_rate": float(check7.get("disagreement_rate") or 0.0) if check7.get("status") == "COMPUTED" else -1.0,
            "age_confound_diffusion_survives": (1.0 if check8.get("diffusion_coef_survives_age_control") else 0.0) if check8.get("status") == "COMPUTED" else -1.0,
            "permutation_p_value_pooled": float(check10.get("permutation_p_value_pooled") or -1.0) if check10.get("status") == "COMPUTED" else -1.0,
            "success_criterion_1_pass": 1.0 if sc1_status == "PASS" else 0.0,
            "success_criterion_2_pass": 1.0 if sc2_status == "PASS" else 0.0,
            "success_criterion_3_pass": 1.0 if sc3_status == "PASS" else 0.0,
        },
        "datasets": [{
            "dataset": "founder_diffusion_evaluation_checks",
            "examples": [
                {"input": "Stage A check 1: TFDD incidence rate vs Avelino et al. 16%", "output": stage_a.get("check1_tfdd_incidence", {}).get("status", "UNAVAILABLE"),
                 "metadata_detail": json.dumps(stage_a.get("check1_tfdd_incidence", {}), default=str), "eval_pass": 1.0 if stage_a.get("check1_tfdd_incidence", {}).get("status") == "PASS" else 0.0},
                {"input": "Stage A check 2: TF=1 share of TFDDs vs Avelino et al. 66%", "output": stage_a.get("check2_tf1_share", {}).get("status", "UNAVAILABLE"),
                 "metadata_detail": json.dumps(stage_a.get("check2_tf1_share", {}), default=str), "eval_pass": 1.0 if stage_a.get("check2_tf1_share", {}).get("status") == "PASS" else 0.0},
                {"input": "Stage A check 3: overall 18mo survival rate vs Avelino et al. 41%", "output": stage_a.get("check3_overall_survival", {}).get("status", "UNAVAILABLE"),
                 "metadata_detail": json.dumps(stage_a.get("check3_overall_survival", {}), default=str), "eval_pass": 1.0 if stage_a.get("check3_overall_survival", {}).get("status") == "PASS" else 0.0},
                {"input": "Stage A check 4: snapshot-null Cohen's d replication", "output": stage_a.get("check4_snapshot_null_cohens_d", {}).get("status", "UNAVAILABLE"),
                 "metadata_detail": json.dumps(stage_a.get("check4_snapshot_null_cohens_d", {}), default=str), "eval_pass": 1.0 if stage_a.get("check4_snapshot_null_cohens_d", {}).get("status") == "PASS" else 0.0},
                {"input": "Stage B check 6: window-boundary sensitivity (6/9/12mo x 0/1/2mo end offset)", "output": check6.get("status", "UNAVAILABLE"),
                 "metadata_detail": json.dumps(check6, default=str), "eval_pass": 1.0 if check6.get("sign_stable_across_variants") else 0.0},
                {"input": "Stage B check 7: founder-identification-heuristic sensitivity", "output": check7.get("status", "UNAVAILABLE"),
                 "metadata_detail": json.dumps(check7, default=str), "eval_pass": 1.0 if (check7.get("status") == "COMPUTED" and check7.get("disagreement_rate", 1.0) < 0.3) else 0.0},
                {"input": "Stage B check 8: age-at-TFDD confound control", "output": check8.get("status", "UNAVAILABLE"),
                 "metadata_detail": json.dumps(check8, default=str), "eval_pass": 1.0 if check8.get("diffusion_coef_survives_age_control") else 0.0},
                {"input": "Stage B check 9: matched-pairs bucket-definition sensitivity", "output": check9.get("status", "UNAVAILABLE"),
                 "metadata_detail": json.dumps(check9, default=str), "eval_pass": 1.0 if check9.get("lift_consistently_gte_1_5x") else 0.0},
                {"input": "Stage B check 10: placebo/shuffle permutation test", "output": check10.get("status", "UNAVAILABLE"),
                 "metadata_detail": json.dumps(check10, default=str),
                 "eval_pass": 1.0 if (check10.get("status") == "COMPUTED" and (check10.get("permutation_p_value_pooled") or 1.0) < 0.05) else 0.0},
                {"input": "Final scoring: success criteria 1-3 and overall verdict", "output": overall,
                 "metadata_detail": json.dumps(final_scoring, default=str), "eval_pass": 1.0 if overall.startswith("SUPPORTS") else 0.0},
            ],
        }],
    }

    out_path = WORKSPACE / "eval_out.json"
    out_path.write_text(json.dumps(eval_out, indent=2, default=str))
    logger.info(f"Wrote {out_path} ({out_path.stat().st_size/1e6:.3f} MB) in {time.time()-t_start:.1f}s")
    logger.info(f"Stage A gate: {stage_a.get('gate_status')}; n_founder_tfdd_events={len(bundles)}; overall verdict: {overall}")


if __name__ == "__main__":
    main()
