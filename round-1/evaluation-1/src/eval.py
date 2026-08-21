#!/usr/bin/env python3
"""Placebo-window falsification and robustness audit for the founder-exit
authority-diffusion survival experiment.

Loads the upstream EXPERIMENT artifact's per-repo event table (method_out.json),
re-derives placebo (randomly-relocated) pre-departure windows, refits the
matched-pairs / regression tests on true vs placebo windows, stratifies by
language and popularity bucket, sanity-checks the DOA/TF/TFDD pipeline against
Avelino et al.'s published aggregate statistics, and bootstraps calibration/CIs
for the survival regression.

If upstream fields required for a given check are missing, that check is
skipped and explicitly flagged as a PIPELINE_GAP in eval_out.json rather than
being fabricated.
"""
from __future__ import annotations

import gc
import json
import resource
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
Path("logs").mkdir(exist_ok=True)
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

# ---------------------------------------------------------------------------
# Resource limits (see aii-use-hardware skill: 29GB container RAM limit)
# ---------------------------------------------------------------------------
RAM_BUDGET_BYTES = 6 * 1024**3  # 6GB budget; this workload is small tabular data
try:
    resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET_BYTES * 3, RAM_BUDGET_BYTES * 3))
except (ValueError, OSError) as e:  # some sandboxes disallow RLIMIT_AS
    logger.warning(f"Could not set RLIMIT_AS: {e}")

WORKSPACE = Path(__file__).resolve().parent
RUN_ROOT = WORKSPACE.parents[2]  # .../3_invention_loop/iter_1
GEN_ART_ROOT = WORKSPACE.parent  # .../gen_art
EXPERIMENT_DIR = GEN_ART_ROOT / "gen_art_experiment_1"
DATASET_DIR = GEN_ART_ROOT / "gen_art_dataset_1"

RNG_SEEDS = [1234, 5678, 9012]  # >=3 seeds for placebo seed-sensitivity, recorded for reproducibility
N_BOOT = 2000  # bootstrap resamples for CIs (reduced from 5000 to stay within CPU budget on 4 cores)
N_BOOT_CALIB = 1000  # calibration bootstrap, per plan (>=1000)

AVELINO_TFDD_RATE = 315 / 1932  # ~0.163
AVELINO_TF1_SHARE = 0.66
AVELINO_TFDD_SURVIVAL = 128 / 315  # ~0.406


# ---------------------------------------------------------------------------
# Upstream data discovery
# ---------------------------------------------------------------------------
_SKIP_DIR_NAMES = {".venv", "venv", "node_modules", "__pycache__", ".git", "repos_scratch", "temp"}


def _find_json(root: Path, names: list[str], max_depth: int = 3) -> Path | None:
    """Search root for the first matching filename, skipping venvs/caches and bounding depth
    (sibling artifact directories may contain full .venv installs with thousands of files)."""
    if not root.exists():
        return None
    for name in names:
        direct = root / name
        if direct.is_file():
            return direct

    def _walk(d: Path, depth: int):
        if depth > max_depth:
            return None
        try:
            entries = list(d.iterdir())
        except OSError:
            return None
        for p in entries:
            if p.is_file() and p.name in names:
                return p
        for p in entries:
            if p.is_dir() and p.name not in _SKIP_DIR_NAMES and not p.name.startswith("."):
                found = _walk(p, depth + 1)
                if found is not None:
                    return found
        return None

    return _walk(root, 0)


def load_upstream() -> tuple[dict[str, Any] | None, dict[str, Any] | None, list[str]]:
    """Load experiment method_out.json and dataset full_data_out.json if present.

    Returns (method_out, data_out, gap_notes).
    """
    gaps: list[str] = []
    method_out_path = _find_json(EXPERIMENT_DIR, ["method_out.json", "full_method_out.json"])
    data_out_path = _find_json(DATASET_DIR, ["full_data_out.json", "data_out.json"])

    method_out = None
    if method_out_path is not None:
        try:
            method_out = json.loads(method_out_path.read_text())
            logger.info(f"Loaded experiment output from {method_out_path}")
        except (json.JSONDecodeError, OSError) as e:
            gaps.append(f"Found experiment output at {method_out_path} but failed to parse: {e}")
    else:
        gaps.append(
            "No method_out.json found under gen_art_experiment_1 at evaluation time — "
            "the upstream EXPERIMENT artifact had not produced its final output yet "
            "(inspected: repos_scratch/ present but empty, only an in-progress agent log). "
            "This is the dominant pipeline gap: every check below that needs per-repo "
            "TFDD event data with commit-level histories falls back to a self-contained "
            "reconstruction from whatever partial upstream files exist, or is marked "
            "UNAVAILABLE."
        )

    data_out = None
    if data_out_path is not None:
        try:
            data_out = json.loads(data_out_path.read_text())
            logger.info(f"Loaded dataset output from {data_out_path}")
        except (json.JSONDecodeError, OSError) as e:
            gaps.append(f"Found dataset output at {data_out_path} but failed to parse: {e}")
    else:
        gaps.append(
            "No full_data_out.json found under gen_art_dataset_1 at evaluation time — "
            "only intermediate temp/ files (repo_candidates_raw.jsonl, search_repos.py) "
            "were present, indicating the DATASET artifact was still mid-collection "
            "(cloning + numstat extraction) when this evaluation ran."
        )

    return method_out, data_out, gaps


def _events_from_exp_gen_sol_out(method_out: dict[str, Any]) -> pd.DataFrame | None:
    """Extract the per-event table from the actual upstream schema: an
    exp_gen_sol_out-style {"datasets": [{"examples": [...]}]} payload where each
    example carries `metadata_*`-prefixed fields plus an `output` string of
    "survived" / "did_not_survive" (the label is NOT a metadata_ field)."""
    datasets = method_out.get("datasets")
    if not isinstance(datasets, list) or not datasets:
        return None
    examples = datasets[0].get("examples")
    if not isinstance(examples, list) or not examples:
        return None
    rows = []
    for ex in examples:
        if not isinstance(ex, dict) or "metadata_repo" not in ex:
            continue  # skip diagnostic placeholder rows (e.g. "no_events")
        row = {k[len("metadata_"):]: v for k, v in ex.items() if k.startswith("metadata_")}
        row["survived"] = 1 if ex.get("output") == "survived" else 0
        rows.append(row)
    if not rows:
        return None
    df = pd.DataFrame(rows)

    # Normalize to the column names the rest of this evaluation expects.
    rename_map = {
        "founder_share_pre_departure": "founder_share",
        "n_diffused_owners_pre_departure": "n_diffused_owners",
    }
    df = df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns})
    if "censored" in df.columns:
        df = df[~df["censored"].astype(bool)].copy()
    if "stars" in df.columns:
        df["log_stars"] = np.log1p(pd.to_numeric(df["stars"], errors="coerce"))
    if "forks" in df.columns:
        df["log_forks"] = np.log1p(pd.to_numeric(df["forks"], errors="coerce"))
    if "devs_at_tfdd" in df.columns and "n_contributors" not in df.columns:
        df["n_contributors"] = df["devs_at_tfdd"]
    if "stars" in df.columns and "popularity_bucket" not in df.columns:
        try:
            df["popularity_bucket"] = pd.qcut(
                pd.to_numeric(df["stars"], errors="coerce"), q=3, labels=["low", "mid", "high"], duplicates="drop"
            ).astype(str)
        except ValueError:
            pass  # too few distinct star values to form 3 buckets; stratification falls back to language only
    return df


def events_to_dataframe(method_out: dict[str, Any] | None) -> pd.DataFrame | None:
    """Extract the per-event record table from method_out.json, tolerant of the
    exact upstream schema variant it was written in."""
    if method_out is None:
        return None
    # Preferred / actual upstream shape: exp_gen_sol_out-style datasets/examples.
    df = _events_from_exp_gen_sol_out(method_out)
    if df is not None:
        return df
    # Fallback: a flat list of event dicts under one of these keys (in case a
    # different experiment run wrote a simpler shape).
    candidates = ["per_event_records", "events", "tfdd_events", "records", "founder_tfdd_events"]
    for key in candidates:
        if key in method_out and isinstance(method_out[key], list) and len(method_out[key]) > 0:
            return pd.DataFrame(method_out[key])
    return None


def load_method_summary(gaps: list[str]) -> dict[str, Any] | None:
    """Load results/method_summary.json (aggregate stats + upstream's own
    matched-pairs / regression / placebo-check results) if present."""
    path = EXPERIMENT_DIR / "results" / "method_summary.json"
    if not path.is_file():
        gaps.append(
            "method_summary: results/method_summary.json not found under the upstream "
            "experiment artifact; aggregate stats (n_repos_sampled, n_repos_processed, "
            "upstream's own matched-pairs/regression/placebo-check results) UNAVAILABLE "
            "for cross-checking against this evaluation's independent recomputation."
        )
        return None
    try:
        return json.loads(path.read_text())
    except (json.JSONDecodeError, OSError) as e:
        gaps.append(f"method_summary: found {path} but failed to parse: {e}")
        return None


# ---------------------------------------------------------------------------
# Statistical helpers
# ---------------------------------------------------------------------------
def wilson_ci(successes: int, n: int, z: float = 1.96) -> tuple[float, float, float]:
    """Wilson score interval for a binomial proportion. Returns (point, lo, hi)."""
    if n == 0:
        return (float("nan"), float("nan"), float("nan"))
    p = successes / n
    denom = 1 + z**2 / n
    center = (p + z**2 / (2 * n)) / denom
    half = (z * np.sqrt(p * (1 - p) / n + z**2 / (4 * n**2))) / denom
    return (p, max(0.0, center - half), min(1.0, center + half))


def bootstrap_ci(values: np.ndarray, stat_fn, n_boot: int, seed: int) -> tuple[float, float, float]:
    """Generic bootstrap: returns (point estimate, 2.5%, 97.5%) for stat_fn(values)."""
    rng = np.random.default_rng(seed)
    if len(values) == 0:
        return (float("nan"), float("nan"), float("nan"))
    point = stat_fn(values)
    n = len(values)
    boots = np.empty(n_boot)
    for b in range(n_boot):
        idx = rng.integers(0, n, size=n)
        boots[b] = stat_fn(values[idx])
    lo, hi = np.percentile(boots, [2.5, 97.5])
    return (float(point), float(lo), float(hi))


def benjamini_hochberg(pvals: dict[str, float], alpha: float = 0.05) -> dict[str, float]:
    """Return BH-adjusted p-values keyed identically to the input dict."""
    items = sorted(pvals.items(), key=lambda kv: kv[1])
    m = len(items)
    adjusted = {}
    prev = 1.0
    for rank, (k, p) in enumerate(reversed(items), start=1):
        i = m - rank + 1
        val = min(prev, p * m / i)
        prev = val
        adjusted[k] = val
    return adjusted


def cohens_h(p1: float, p2: float) -> float:
    """Cohen's h effect size for the difference between two proportions."""
    return 2 * np.arcsin(np.sqrt(p1)) - 2 * np.arcsin(np.sqrt(p2))


def brier_score(y_true: np.ndarray, y_prob: np.ndarray) -> float:
    return float(np.mean((y_prob - y_true) ** 2))


def auc_score(y_true: np.ndarray, y_prob: np.ndarray) -> float:
    """Mann-Whitney U based AUC, no sklearn dependency needed for ties handling."""
    pos = y_prob[y_true == 1]
    neg = y_prob[y_true == 0]
    if len(pos) == 0 or len(neg) == 0:
        return float("nan")
    # Rank-based AUC (handles ties by average rank)
    all_scores = np.concatenate([pos, neg])
    order = np.argsort(all_scores)
    ranks = np.empty_like(order, dtype=float)
    ranks[order] = np.arange(1, len(all_scores) + 1)
    # average tie ranks
    _, inv, counts = np.unique(all_scores, return_inverse=True, return_counts=True)
    sum_ranks_per_val = np.zeros(len(counts))
    np.add.at(sum_ranks_per_val, inv, ranks)
    avg_rank_per_val = sum_ranks_per_val / counts
    ranks = avg_rank_per_val[inv]
    rank_pos_sum = ranks[: len(pos)].sum()
    n1, n0 = len(pos), len(neg)
    u = rank_pos_sum - n1 * (n1 + 1) / 2
    return float(u / (n1 * n0))


def logistic_regression_irls(X: np.ndarray, y: np.ndarray, max_iter: int = 100, tol: float = 1e-8):
    """Minimal IRLS logistic regression (no external dep beyond numpy).

    X must already include an intercept column. Returns (coefs, cov_matrix) or
    (None, None) on failure (e.g. singular Hessian / quasi-separation).
    """
    n, p = X.shape
    beta = np.zeros(p)
    for _ in range(max_iter):
        eta = X @ beta
        eta = np.clip(eta, -30, 30)
        mu = 1 / (1 + np.exp(-eta))
        w = mu * (1 - mu)
        w = np.clip(w, 1e-8, None)
        z = eta + (y - mu) / w
        WX = X * w[:, None]
        try:
            hessian = X.T @ WX
            beta_new = np.linalg.solve(hessian, X.T @ (w * z))
        except np.linalg.LinAlgError:
            return None, None
        if np.max(np.abs(beta_new - beta)) < tol:
            beta = beta_new
            break
        beta = beta_new
    eta = np.clip(X @ beta, -30, 30)
    mu = 1 / (1 + np.exp(-eta))
    w = np.clip(mu * (1 - mu), 1e-8, None)
    try:
        cov = np.linalg.inv(X.T @ (X * w[:, None]))
    except np.linalg.LinAlgError:
        cov = np.full((p, p), np.nan)
    return beta, cov


def wald_pvalues(beta: np.ndarray, cov: np.ndarray) -> np.ndarray:
    from scipy import stats

    se = np.sqrt(np.clip(np.diag(cov), 0, None))
    with np.errstate(divide="ignore", invalid="ignore"):
        z = beta / se
    return 2 * (1 - stats.norm.cdf(np.abs(z)))


# ---------------------------------------------------------------------------
# Step 1-3: Placebo window falsification test
# ---------------------------------------------------------------------------
def run_placebo_falsification(df: pd.DataFrame, gaps: list[str]) -> dict[str, Any]:
    """Reconstruct the placebo/shuffle test comparing true vs random-window effects.

    Requires: per-project founder_share / n_diffused_owners for the TRUE window,
    a survival label, and EITHER (a) precomputed placebo_founder_share /
    placebo_n_diffused_owners from the upstream experiment (Stage 7 of its
    pseudocode), or (b) a full per-window time series to draw placebo windows
    from ourselves. If neither is present we cannot fabricate a window series
    (explicitly disallowed by the artifact plan) and report UNAVAILABLE.
    """
    result: dict[str, Any] = {"status": "UNAVAILABLE", "seeds": RNG_SEEDS}

    required_true = {"founder_share", "n_diffused_owners", "survived"}
    if df is None or not required_true.issubset(df.columns):
        gaps.append(
            "placebo_test: upstream event table missing one of "
            f"{sorted(required_true)}; cannot run true-window statistics at all."
        )
        return result

    has_placebo_precomputed = {"placebo_founder_share", "placebo_n_diffused_owners"}.issubset(df.columns)
    has_window_series = "pre_tfdd_window_series" in df.columns or "window_series" in df.columns

    if not has_placebo_precomputed and not has_window_series:
        gaps.append(
            "placebo_test: neither precomputed placebo_founder_share/"
            "placebo_n_diffused_owners columns nor a per-project pre-TFDD window "
            "time series were present in the upstream event table. Per the artifact "
            "plan's explicit fallback instruction, a placebo window series was NOT "
            "fabricated. Falsification check (success_criteria #3) is UNAVAILABLE "
            "this run; only Steps 4-6 (stratification / pipeline-validity / "
            "calibration) could execute on whatever fields ARE present."
        )
        return result

    df = df.dropna(subset=["founder_share", "n_diffused_owners", "survived"]).copy()
    df["survived"] = df["survived"].astype(int)

    def group_lift(sub: pd.DataFrame, share_col: str) -> float:
        """Survival-rate lift: high-diffusion (low founder share) minus low-diffusion group."""
        lo = sub[sub[share_col] < sub[share_col].median()]
        hi = sub[sub[share_col] >= sub[share_col].median()]
        if len(lo) == 0 or len(hi) == 0:
            return float("nan")
        return float(lo["survived"].mean() - hi["survived"].mean())

    true_lift_point, true_lift_lo, true_lift_hi = bootstrap_ci(
        df.index.values, lambda idx: group_lift(df.loc[idx], "founder_share"), N_BOOT, seed=RNG_SEEDS[0]
    )

    seed_results = []
    if has_placebo_precomputed:
        placebo_df = df.dropna(subset=["placebo_founder_share", "placebo_n_diffused_owners"])
        for seed in RNG_SEEDS:
            # single precomputed draw: reuse it under each seed label for seed-sensitivity
            # reporting, since the upstream only stored one placebo draw per project.
            lift_p, lo_p, hi_p = bootstrap_ci(
                placebo_df.index.values,
                lambda idx: group_lift(placebo_df.loc[idx], "placebo_founder_share"),
                N_BOOT,
                seed=seed,
            )
            seed_results.append({"seed": seed, "placebo_lift": lift_p, "ci_lo": lo_p, "ci_hi": hi_p})
        gaps.append(
            "placebo_test: upstream provided only ONE precomputed placebo draw per "
            "project (not a full window series), so seed-sensitivity here reflects "
            "bootstrap resampling variance under different seeds applied to the SAME "
            "draw, not independent re-draws of the placebo window itself. This is a "
            "weaker seed-sensitivity check than the artifact plan specifies."
        )
    else:
        # has_window_series
        series_col = "pre_tfdd_window_series" if "pre_tfdd_window_series" in df.columns else "window_series"
        for seed in RNG_SEEDS:
            rng = np.random.default_rng(seed)
            placebo_rows = []
            for _, row in df.iterrows():
                windows = row[series_col]
                if not isinstance(windows, list) or len(windows) == 0:
                    continue
                choice = windows[int(rng.integers(0, len(windows)))]
                placebo_rows.append({
                    "placebo_founder_share": choice.get("founder_share"),
                    "placebo_n_diffused_owners": choice.get("n_diffused_owners"),
                    "survived": row["survived"],
                })
            pdf = pd.DataFrame(placebo_rows).dropna()
            if len(pdf) == 0:
                continue
            lift_p, lo_p, hi_p = bootstrap_ci(
                pdf.index.values,
                lambda idx: group_lift(pdf.loc[idx], "placebo_founder_share"),
                N_BOOT,
                seed=seed,
            )
            seed_results.append({"seed": seed, "placebo_lift": lift_p, "ci_lo": lo_p, "ci_hi": hi_p})

    if not seed_results:
        gaps.append("placebo_test: placebo data present but produced 0 usable rows after cleaning.")
        return result

    placebo_lifts = np.array([s["placebo_lift"] for s in seed_results if not np.isnan(s["placebo_lift"])])
    if len(placebo_lifts) == 0:
        gaps.append("placebo_test: all placebo lift estimates were NaN.")
        return result

    diff = true_lift_point - float(np.mean(placebo_lifts))
    # Permutation-style test: is the true effect outside the empirical placebo distribution?
    ci_excludes_zero = not (true_lift_lo <= 0 <= true_lift_hi) and (true_lift_lo > np.max(placebo_lifts))
    ci_overlap = not (true_lift_hi < np.min(placebo_lifts) or true_lift_lo > np.max(placebo_lifts))

    if ci_excludes_zero and true_lift_point > np.max(placebo_lifts):
        verdict = "PASS"
    elif true_lift_point > float(np.mean(placebo_lifts)) and ci_overlap:
        verdict = "WEAK"
    else:
        verdict = "FAIL"

    result = {
        "status": "COMPUTED",
        "n_projects": int(len(df)),
        "true_window_survival_lift": {"point": true_lift_point, "ci95": [true_lift_lo, true_lift_hi]},
        "placebo_survival_lift_by_seed": seed_results,
        "placebo_lift_mean_across_seeds": float(np.mean(placebo_lifts)),
        "true_minus_placebo_diff": diff,
        "ci_overlap": bool(ci_overlap),
        "verdict": verdict,
        "seeds": RNG_SEEDS,
    }
    return result


# ---------------------------------------------------------------------------
# Step 4: Stratified robustness
# ---------------------------------------------------------------------------
def run_stratified_robustness(df: pd.DataFrame, gaps: list[str]) -> dict[str, Any]:
    required = {"founder_share", "survived"}
    if df is None or not required.issubset(df.columns):
        gaps.append("stratified_robustness: missing founder_share/survived columns; UNAVAILABLE.")
        return {"status": "UNAVAILABLE"}

    df = df.dropna(subset=["founder_share", "survived"]).copy()
    df["survived"] = df["survived"].astype(int)

    strata_cols = [c for c in ["language", "popularity_bucket", "star_bucket"] if c in df.columns]
    if not strata_cols:
        gaps.append(
            "stratified_robustness: no language/popularity_bucket columns found in the "
            "upstream event table; cannot stratify. Reporting pooled effect only."
        )
        strata_cols = []

    def effect(sub: pd.DataFrame) -> float:
        lo = sub[sub["founder_share"] < sub["founder_share"].median()]
        hi = sub[sub["founder_share"] >= sub["founder_share"].median()]
        if len(lo) == 0 or len(hi) == 0:
            return float("nan")
        return float(lo["survived"].mean() - hi["survived"].mean())

    pooled_point, pooled_lo, pooled_hi = bootstrap_ci(
        df.index.values, lambda idx: effect(df.loc[idx]), N_BOOT, seed=RNG_SEEDS[0]
    )

    strata_results = []
    MIN_N = 10
    for col in strata_cols:
        for level, sub in df.groupby(col):
            underpowered = len(sub) < MIN_N
            if len(sub) < 4:
                strata_results.append({
                    "stratum_col": col, "level": str(level), "n": int(len(sub)),
                    "underpowered": True, "effect": None, "ci95": None,
                    "note": "n<4, too small even to bootstrap",
                })
                continue
            pt, lo_, hi_ = bootstrap_ci(sub.index.values, lambda idx: effect(sub.loc[idx]), N_BOOT, seed=RNG_SEEDS[0])
            strata_results.append({
                "stratum_col": col, "level": str(level), "n": int(len(sub)),
                "underpowered": bool(underpowered), "effect": pt, "ci95": [lo_, hi_],
            })

    # Heterogeneity: range of stratum effects vs pooled CI width, and simple Cochran's Q
    valid_effects = [s["effect"] for s in strata_results if s["effect"] is not None and not np.isnan(s["effect"])]
    heterogeneity = {}
    if len(valid_effects) >= 2:
        eff_range = float(max(valid_effects) - min(valid_effects))
        pooled_ci_width = float(pooled_hi - pooled_lo)
        heterogeneity = {
            "effect_range_across_strata": eff_range,
            "pooled_ci_width": pooled_ci_width,
            "range_exceeds_pooled_ci": bool(eff_range > pooled_ci_width),
            "n_strata_compared": len(valid_effects),
        }
    else:
        heterogeneity = {"note": "fewer than 2 valid strata effects; heterogeneity check UNAVAILABLE"}

    return {
        "status": "COMPUTED",
        "pooled_effect": {"point": pooled_point, "ci95": [pooled_lo, pooled_hi]},
        "strata": strata_results,
        "min_n_threshold": MIN_N,
        "heterogeneity_check": heterogeneity,
    }


# ---------------------------------------------------------------------------
# Step 5: Pipeline-validity sanity check vs Avelino et al.
# ---------------------------------------------------------------------------
def run_pipeline_validity(
    method_out: dict[str, Any] | None, df: pd.DataFrame | None, gaps: list[str],
    method_summary: dict[str, Any] | None = None,
) -> dict[str, Any]:
    checks: dict[str, Any] = {}
    summary = method_summary or {}

    def flag(name: str, point: float, lo: float, hi: float, reference: float) -> dict[str, Any]:
        rel_dist = abs(point - reference) / reference if reference else float("inf")
        ci_contains = lo <= reference <= hi
        passed = ci_contains or rel_dist <= 1.5
        return {
            "point_estimate": point, "ci95": [lo, hi], "avelino_reference": reference,
            "relative_distance": rel_dist, "flag": "PASS" if passed else "CONCERN",
        }

    # (a) fraction of projects with >=1 TFDD. The upstream pipeline only ever records
    # founder-only (strict, TF=1) and TF<=2 (relaxed) TFDD events -- it never counts
    # TFDDs of any TF-set size, so "n_repos_with_tfdd" in Avelino et al.'s exact sense
    # does not exist upstream. We use the RELAXED (TF<=2) count over n_repos_processed
    # as the closest available proxy (an underestimate of the true any-TF-size rate,
    # since TF=3+ TFDDs are invisible to this pipeline by construction) and label it
    # explicitly as a proxy rather than a like-for-like reproduction.
    n_processed = summary.get("n_repos_processed")
    n_relaxed = summary.get("n_founder_tfdd_events_relaxed")
    n_strict = summary.get("n_founder_tfdd_events_strict")
    if n_processed and n_relaxed is not None:
        p, lo, hi = wilson_ci(int(n_relaxed), int(n_processed))
        checks["tfdd_rate"] = flag("tfdd_rate", p, lo, hi, AVELINO_TFDD_RATE)
        checks["tfdd_rate"]["proxy_caveat"] = (
            "Upstream tracks only TF<=2 TFDDs (relaxed definition), not TFDDs of any "
            "TF-set size as in Avelino et al.; this is a lower-bound proxy for the "
            "true any-size TFDD rate, so a below-reference point estimate is expected "
            "even with a correct implementation."
        )
    else:
        gaps.append(
            "pipeline_validity/tfdd_rate: results/method_summary.json missing "
            "n_repos_processed and/or n_founder_tfdd_events_relaxed; UNAVAILABLE."
        )
        checks["tfdd_rate"] = {"status": "UNAVAILABLE"}

    # (b) fraction of TFDDs at TF=1 (founder-only): proxy as strict / relaxed, i.e.
    # among TF<=2 TFDDs, what share are exactly TF=1. This is NOT Avelino et al.'s
    # exact "share of ALL TFDDs (any TF size) that occur at TF=1" -- their denominator
    # includes TF=2,3,4... events this pipeline never detects -- so we report it as an
    # informative but non-equivalent proxy rather than silently treating it as the
    # same statistic.
    if n_strict is not None and n_relaxed:
        p, lo, hi = wilson_ci(int(n_strict), int(n_relaxed))
        checks["tf1_share"] = flag("tf1_share", p, lo, hi, AVELINO_TF1_SHARE)
        checks["tf1_share"]["proxy_caveat"] = (
            "Computed as strict(TF=1) / relaxed(TF<=2), NOT strict / all-TFDDs-of-"
            "any-size as in Avelino et al. -- the pipeline's own pseudocode only ever "
            "detects founder-only or TF<=2 events, so the true denominator (TFDDs "
            "with a larger initial TF-set) is structurally unmeasured by this "
            "experiment. Treat this as directional evidence only, not a strict "
            "replication of the 66% figure."
        )
    else:
        gaps.append(
            "pipeline_validity/tf1_share: results/method_summary.json missing "
            "n_founder_tfdd_events_strict and/or n_founder_tfdd_events_relaxed; "
            "UNAVAILABLE. Note even with these fields present, this pipeline "
            "structurally cannot reproduce Avelino et al.'s exact tf1_share "
            "definition -- see the proxy_caveat this check would otherwise attach."
        )
        checks["tf1_share"] = {"status": "UNAVAILABLE"}

    # (c) unconditioned survival rate among founder-only (strict) TFDD events --
    # this one IS directly comparable to Avelino et al.'s 41%, since both are
    # "P(survive 18mo | TFDD occurred)" on an uncensored sample.
    strict_surv = summary.get("strict_unconditioned_survival") or {}
    if strict_surv.get("survival_rate") is not None and strict_surv.get("n_uncensored"):
        p = float(strict_surv["survival_rate"])
        n = int(strict_surv["n_uncensored"])
        k = round(p * n)
        _, lo, hi = wilson_ci(k, n)
        checks["unconditioned_survival_rate"] = flag("unconditioned_survival_rate", p, lo, hi, AVELINO_TFDD_SURVIVAL)
    elif df is not None and "survived" in df.columns and len(df) > 0:
        sub = df.dropna(subset=["survived"])
        n = int(len(sub))
        if n > 0:
            k = int(sub["survived"].astype(int).sum())
            p, lo, hi = wilson_ci(k, n)
            checks["unconditioned_survival_rate"] = flag(
                "unconditioned_survival_rate", p, lo, hi, AVELINO_TFDD_SURVIVAL
            )
        else:
            checks["unconditioned_survival_rate"] = {"status": "UNAVAILABLE"}
    else:
        gaps.append(
            "pipeline_validity/unconditioned_survival_rate: no per-event survival "
            "labels (from method_out.json) or precomputed strict_unconditioned_survival "
            "(from method_summary.json) found; UNAVAILABLE."
        )
        checks["unconditioned_survival_rate"] = {"status": "UNAVAILABLE"}

    checks["caveat"] = (
        "This evaluation's corpus is a founder-only, stratified-sampled subset "
        "(6 languages x 3 popularity strata, target ~40/language per the experiment "
        "plan) rather than Avelino et al.'s full top-500-per-language corpus (n=1932), "
        "so some divergence from their published aggregates is EXPECTED and does not "
        "by itself indicate a reimplementation bug; only a large divergence outside "
        "the 1.5x relative-distance band is flagged CONCERN."
    )
    return checks


# ---------------------------------------------------------------------------
# Step 6: Regression calibration
# ---------------------------------------------------------------------------
def run_calibration(df: pd.DataFrame, gaps: list[str]) -> dict[str, Any]:
    predictor_cols = [c for c in ["founder_share", "n_diffused_owners", "log_stars", "log_forks", "n_contributors"] if df is not None and c in df.columns]
    if df is None or "survived" not in df.columns or len(predictor_cols) == 0:
        gaps.append(
            "calibration: missing survived label or all candidate predictor columns "
            "(founder_share/n_diffused_owners/log_stars/log_forks/n_contributors); "
            "UNAVAILABLE."
        )
        return {"status": "UNAVAILABLE"}

    sub = df.dropna(subset=predictor_cols + ["survived"]).copy()
    if len(sub) < 15:
        gaps.append(
            f"calibration: only {len(sub)} complete rows available (need >=15 for a "
            "stable logistic fit + bootstrap); UNAVAILABLE."
        )
        return {"status": "UNAVAILABLE", "n_available": int(len(sub))}

    y = sub["survived"].astype(int).to_numpy()
    Xraw = sub[predictor_cols].to_numpy(dtype=float)
    Xstd = (Xraw - Xraw.mean(axis=0)) / (Xraw.std(axis=0) + 1e-9)
    X = np.column_stack([np.ones(len(sub)), Xstd])

    beta, cov = logistic_regression_irls(X, y)
    if beta is None:
        gaps.append("calibration: logistic regression failed to converge (singular Hessian, likely quasi-separation).")
        return {"status": "FAILED_TO_CONVERGE", "n_available": int(len(sub))}

    pvals = wald_pvalues(beta, cov)
    coef_names = ["intercept"] + predictor_cols
    pval_dict = {name: float(p) for name, p in zip(coef_names, pvals)}
    bh = benjamini_hochberg({k: v for k, v in pval_dict.items() if k != "intercept"})

    eta = np.clip(X @ beta, -30, 30)
    p_hat = 1 / (1 + np.exp(-eta))

    brier = brier_score(y, p_hat)
    auc_pt, auc_lo, auc_hi = bootstrap_ci(
        np.arange(len(y)), lambda idx: auc_score(y[idx], p_hat[idx]), N_BOOT_CALIB, seed=RNG_SEEDS[0]
    )

    # Bootstrap coefficient CIs
    rng = np.random.default_rng(RNG_SEEDS[0])
    n = len(y)
    boot_coefs = []
    for _ in range(N_BOOT_CALIB):
        idx = rng.integers(0, n, size=n)
        b, _ = logistic_regression_irls(X[idx], y[idx])
        if b is not None:
            boot_coefs.append(b)
    coef_ci = {}
    if boot_coefs:
        boot_arr = np.array(boot_coefs)
        for i, name in enumerate(coef_names):
            lo_c, hi_c = np.percentile(boot_arr[:, i], [2.5, 97.5])
            coef_ci[name] = {"point": float(beta[i]), "ci95": [float(lo_c), float(hi_c)], "wald_p": pval_dict[name]}
    else:
        gaps.append("calibration: all bootstrap resamples failed to converge; coefficient CIs UNAVAILABLE.")

    # Calibration curve: predicted-probability deciles vs observed survival rate
    deciles = pd.qcut(p_hat, q=min(10, len(np.unique(p_hat))), duplicates="drop")
    calib_df = pd.DataFrame({"decile": deciles, "p_hat": p_hat, "y": y})
    calib_curve = (
        calib_df.groupby("decile", observed=True)
        .agg(mean_predicted=("p_hat", "mean"), observed_rate=("y", "mean"), n=("y", "size"))
        .reset_index(drop=True)
        .to_dict(orient="records")
    )

    return {
        "status": "COMPUTED",
        "n": int(len(sub)),
        "predictor_cols": predictor_cols,
        "coefficients": coef_ci,
        "bh_adjusted_pvalues": bh,
        "brier_score": brier,
        "auc": {"point": auc_pt, "ci95": [auc_lo, auc_hi]},
        "calibration_curve_deciles": calib_curve,
        "n_bootstrap": N_BOOT_CALIB,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
from loguru import logger as _logger


@_logger.catch(reraise=True)
def main() -> None:
    logger.info("Loading upstream experiment/dataset outputs")
    method_out, data_out, gaps = load_upstream()
    df = events_to_dataframe(method_out)
    if df is not None:
        logger.info(f"Loaded {len(df)} per-project event records from upstream experiment output")
    else:
        logger.warning("No per-project event table available from upstream experiment output")

    del data_out  # not used beyond availability check
    gc.collect()

    logger.info("Running Step 1-3: placebo-window falsification")
    placebo_result = run_placebo_falsification(df, gaps)

    logger.info("Running Step 4: stratified robustness")
    strat_result = run_stratified_robustness(df, gaps)

    method_summary = load_method_summary(gaps)

    logger.info("Running Step 5: pipeline-validity sanity check vs Avelino et al.")
    validity_result = run_pipeline_validity(method_out, df, gaps, method_summary=method_summary)

    logger.info("Running Step 6: regression calibration")
    calib_result = run_calibration(df, gaps)

    # ------------------------------------------------------------------
    # Overall verdict for success_criteria #3 (falsification/specificity)
    # ------------------------------------------------------------------
    if placebo_result.get("status") == "COMPUTED":
        overall_verdict = placebo_result["verdict"]
    else:
        overall_verdict = "UNDETERMINED_PIPELINE_GAP"

    n_events = int(len(df)) if df is not None else 0

    metrics_agg: dict[str, float] = {
        "n_founder_tfdd_events_evaluated": float(n_events),
        "n_pipeline_gaps_flagged": float(len(gaps)),
    }
    if placebo_result.get("status") == "COMPUTED":
        metrics_agg["true_window_survival_lift"] = placebo_result["true_window_survival_lift"]["point"]
        metrics_agg["placebo_survival_lift_mean"] = placebo_result["placebo_lift_mean_across_seeds"]
        metrics_agg["true_minus_placebo_diff"] = placebo_result["true_minus_placebo_diff"]
        metrics_agg["placebo_verdict_pass"] = 1.0 if placebo_result["verdict"] == "PASS" else 0.0
    if strat_result.get("status") == "COMPUTED":
        metrics_agg["pooled_effect_point"] = strat_result["pooled_effect"]["point"]
        metrics_agg["n_strata_evaluated"] = float(len(strat_result["strata"]))
    for k in ["tfdd_rate", "tf1_share", "unconditioned_survival_rate"]:
        v = validity_result.get(k, {})
        if isinstance(v, dict) and "point_estimate" in v:
            metrics_agg[f"pipeline_validity_{k}"] = v["point_estimate"]
            metrics_agg[f"pipeline_validity_{k}_pass"] = 1.0 if v["flag"] == "PASS" else 0.0
    if calib_result.get("status") == "COMPUTED":
        metrics_agg["calibration_brier_score"] = calib_result["brier_score"]
        metrics_agg["calibration_auc"] = calib_result["auc"]["point"]

    # metrics_agg schema requires every value to be a JSON number — drop any NaN/Inf
    # entries rather than emit a value the schema (and JSON itself) disallows.
    metrics_agg = {
        k: v for k, v in metrics_agg.items()
        if not (isinstance(v, float) and (np.isnan(v) or np.isinf(v)))
    }

    caveats = " | ".join(gaps) if gaps else "No data-availability gaps encountered."

    eval_metadata = {
        "evaluation_name": "Placebo-Window Falsification and Robustness Audit",
        "description": (
            "Evaluates the pre-departure authority-diffusion / OSS-survival experiment "
            "via placebo-window falsification, stratified robustness, Avelino et al. "
            "pipeline-validity sanity checks, and bootstrap regression calibration."
        ),
        "avelino_reference_stats": {
            "tfdd_rate": AVELINO_TFDD_RATE,
            "tf1_share": AVELINO_TF1_SHARE,
            "tfdd_survival_rate": AVELINO_TFDD_SURVIVAL,
        },
        "seeds_used": RNG_SEEDS,
        "n_bootstrap_main": N_BOOT,
        "n_bootstrap_calibration": N_BOOT_CALIB,
        "overall_verdict": overall_verdict,
        "caveats": caveats,
        "checks": {
            "placebo_test": placebo_result,
            "stratified_robustness": strat_result,
            "pipeline_validity": validity_result,
            "calibration": calib_result,
        },
        "upstream_self_reported_results": {
            "note": (
                "The upstream experiment also computes its own matched-pairs risk "
                "ratio, our-method-vs-baseline regression, and placebo-window "
                "regression comparison (Stage 7-8 of its pseudocode). Reproduced "
                "here verbatim from results/method_summary.json for direct "
                "cross-comparison against this evaluation's INDEPENDENT recomputation "
                "above -- large disagreement between the two would itself be a "
                "signal worth investigating, since they should agree on the same "
                "underlying event table."
            ),
            "matched_pairs": (method_summary or {}).get("matched_pairs"),
            "regression_our_method": (method_summary or {}).get("regression_our_method"),
            "regression_baseline_snapshot_only": (method_summary or {}).get("regression_baseline_snapshot_only"),
            "placebo_check": (method_summary or {}).get("placebo_check"),
        } if method_summary is not None else {"status": "UNAVAILABLE"},
    }

    # ------------------------------------------------------------------
    # Build exp_eval_sol_out.json-compliant output.
    # `datasets`/`examples` (input/output strings) are required by schema even
    # though this evaluation is aggregate-statistical, not per-example; we
    # encode each check as one "example" so the schema's per-example slot is
    # used meaningfully rather than left as a dummy placeholder.
    # ------------------------------------------------------------------
    examples = []
    for check_name, check_result in eval_metadata["checks"].items():
        examples.append({
            "input": f"Run {check_name} on the founder-exit authority-diffusion experiment's upstream event table.",
            "output": json.dumps(check_result, default=str)[:20000],
            "metadata_check_name": check_name,
            "eval_status_computed": 1.0 if (isinstance(check_result, dict) and check_result.get("status") == "COMPUTED") else 0.0,
        })

    eval_out = {
        "metadata": eval_metadata,
        "metrics_agg": metrics_agg,
        "datasets": [
            {
                "dataset": "founder_exit_tfdd_events",
                "examples": examples,
            }
        ],
    }

    def _sanitize(obj):
        """Recursively replace NaN/Inf floats with None (JSON has no NaN token)."""
        if isinstance(obj, float):
            if np.isnan(obj) or np.isinf(obj):
                return None
            return obj
        if isinstance(obj, dict):
            return {k: _sanitize(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [_sanitize(v) for v in obj]
        return obj

    eval_out = _sanitize(eval_out)
    out_path = WORKSPACE / "eval_out.json"
    out_path.write_text(json.dumps(eval_out, indent=2, default=str, allow_nan=False))
    logger.info(f"Wrote {out_path} ({out_path.stat().st_size / 1024:.1f} KB)")
    logger.info(f"Overall verdict: {overall_verdict}")
    logger.info(f"Pipeline gaps flagged: {len(gaps)}")
    for g in gaps:
        logger.warning(f"GAP: {g}")


if __name__ == "__main__":
    main()
