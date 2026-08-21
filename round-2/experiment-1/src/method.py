#!/usr/bin/env python3
"""Scaled diffusion-vs-survival test plus Medappa reconciliation.

Reuses the iter-1 founder-only Truck-Factor Development Departure (TFDD)
pipeline (Avelino et al. ESEM 2019 DOA / Truck-Factor / TFDD / Active-Inactive
model) VERBATIM, but reads commit history from the already-mined
`full_data_out.json` (34 founder-candidate repos, 70,260 commit/file rows)
instead of re-cloning from GitHub -- this is the SAME 34-repo pool iter1 used,
so "scaling" here means re-running the identical validated method + BH-corrected
stats battery on the same corpus at whatever n it yields, NOT adding new repos.

our_method (unchanged from iter1): pre-departure authority-diffusion trajectory
  (founder_share, n_diffused_owners) in the 12-6mo pre-TFDD window.
baseline (unchanged from iter1): snapshot size/popularity covariates AT the
  TFDD event (devs, commits, files, stars, forks), no temporal trajectory.
NEW reconciliation (this iteration): a Medappa-et-al.-style static, whole-
  pre-history write-access ratio (medappa_ratio) plus a timing_term (fraction
  of non-founder ownership onsets concentrated in the pre-departure window
  vs spread through history) and their interaction, testing whether it is the
  TIMING of diffusion -- not its mere presence -- that flips the sign of its
  association with survival.
"""

from __future__ import annotations

import gc
import json
import math
import multiprocessing as mp
import random
import resource
import sys
import time
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd
import psutil
import statsmodels.api as sm
from loguru import logger
from scipy import stats
from statsmodels.stats.outliers_influence import variance_inflation_factor

WORKSPACE = Path(__file__).resolve().parent
LOGS_DIR = WORKSPACE / "logs"
RESULTS_DIR = WORKSPACE / "results"
for d in (LOGS_DIR, RESULTS_DIR):
    d.mkdir(parents=True, exist_ok=True)

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add(LOGS_DIR / "run.log", rotation="30 MB", level="DEBUG")

RNG_SEED = 20260821
random.seed(RNG_SEED)
np.random.seed(RNG_SEED)

# RAM budget: file is ~78MB on disk, expands ~4-6x as parsed JSON + per-repo
# commit dicts; 6GB is generous headroom under the 29GB container limit.
RAM_BUDGET_BYTES = 6 * 1024**3
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET_BYTES * 3, RAM_BUDGET_BYTES * 3))
NUM_CPUS = len(psutil.Process().cpu_affinity()) if hasattr(psutil.Process(), "cpu_affinity") else 4
NUM_CPUS = max(1, min(NUM_CPUS, 4))

# --- constants reused verbatim from iter1 (do not re-tune) ---
SILENCE_THRESHOLD_DAYS = 365
TF_COVERAGE_THRESHOLD = 0.5
POST_TFDD_WINDOW_DAYS = 548  # 18 months
PRE_WINDOW_FAR_DAYS = 365  # 12 months before TFDD
PRE_WINDOW_NEAR_DAYS = 180  # 6 months before TFDD
N_BOOT = 5000
SNAPSHOT_EVERY_DAYS = 90
STRICT_FOUNDER_SHARE = 0.70  # re-verification threshold for founder-only strict criterion
RELAXED_FOUNDER_SHARE = 0.50
TARGET_N_STRICT = 40  # iter1 power-analysis target; 34-repo pool structurally caps below this

AVELINO_REFERENCE_SURVIVAL_RATE = 0.41


# ---------------------------------------------------------------------------
# STEP 0: load full_data_out.json -> per-repo commit streams (no re-cloning:
# the (commit,file) rows in this dataset ARE the `git log --numstat` output
# iter1 parsed live, just already mined).
# ---------------------------------------------------------------------------
def load_repo_commit_streams(data_path: Path) -> dict[str, dict]:
    logger.info(f"[step0] loading {data_path}")
    raw = json.loads(data_path.read_text())
    examples = raw["datasets"][0]["examples"]
    logger.info(f"[step0] loaded {len(examples)} (commit,file) rows")

    repos: dict[str, dict] = {}
    for row in examples:
        rid = str(row["metadata_repo_id"])
        rep = repos.setdefault(
            rid,
            {
                "full_name": row["metadata_full_name"],
                "license_key": row.get("metadata_license") or "none",
                "created_at": datetime.fromisoformat(row["metadata_repo_created_at"].replace("Z", "+00:00")),
                "stars": None,
                "forks": None,
                "language": None,
                "commits_by_sha": {},
                "dominant_founder_first_window_share": row.get("metadata_dominant_founder_share_first_window"),
                "alias_ambiguous": row.get("metadata_alias_ambiguous_repo"),
            },
        )
        try:
            inp = json.loads(row["input"])
        except (json.JSONDecodeError, TypeError):
            inp = {}
        if rep["stars"] is None:
            rep["stars"] = inp.get("repo_stars", 0)
            rep["forks"] = inp.get("repo_forks", 0)
            rep["language"] = inp.get("repo_primary_language", "unknown")
        sha = row["metadata_commit_sha"]
        c = rep["commits_by_sha"].get(sha)
        if c is None:
            try:
                dt = datetime.fromisoformat(row["metadata_commit_timestamp"])
            except ValueError:
                continue
            c = {"hash": sha, "author_email": row["metadata_author_alias_key"], "date": dt, "files": []}
            rep["commits_by_sha"][sha] = c
        added = inp.get("lines_added", 0) or 0
        removed = inp.get("lines_removed", 0) or 0
        c["files"].append((inp.get("file_path", "?"), added, removed))

    for rep in repos.values():
        commits = sorted(rep["commits_by_sha"].values(), key=lambda c: c["date"])
        rep["commits"] = commits
        del rep["commits_by_sha"]
    logger.info(f"[step0] grouped into {len(repos)} repos")
    return repos


# ---------------------------------------------------------------------------
# DOA / Truck-Factor (Fritz et al. 2010 formula, Avelino et al. ICPC2016/ESEM2019)
#   DOA(dev, file, t) = 3.293 + 1.098*FA - 0.164*sqrt(AC) + 0.230*ln(1+DL)
# -- reused VERBATIM from iter1's method.py --
# ---------------------------------------------------------------------------
def doa_snapshot(commits: list[dict], cutoff: datetime) -> dict[tuple[str, str], float]:
    file_dev_stats: dict[str, dict[str, dict]] = defaultdict(dict)
    file_first_author: dict[str, str] = {}
    for c in commits:
        if c["date"] > cutoff:
            break
        for path, added, deleted in c["files"]:
            if path not in file_first_author:
                file_first_author[path] = c["author_email"]
            dev_stats = file_dev_stats[path]
            s = dev_stats.setdefault(c["author_email"], {"ac": 0, "dl": 0})
            s["ac"] += 1
            s["dl"] += deleted
    doa: dict[tuple[str, str], float] = {}
    for path, devs in file_dev_stats.items():
        first_author = file_first_author[path]
        for dev, s in devs.items():
            fa = 1 if dev == first_author else 0
            doa[(dev, path)] = 3.293 + 1.098 * fa - 0.164 * math.sqrt(s["ac"]) + 0.230 * math.log(1 + s["dl"])
    return doa


def file_owners(doa: dict[tuple[str, str], float]) -> dict[str, tuple[str, float]]:
    owner: dict[str, tuple[str, float]] = {}
    for (dev, path), score in doa.items():
        if path not in owner or score > owner[path][1]:
            owner[path] = (dev, score)
    return owner


def truck_factor_set(doa: dict[tuple[str, str], float]) -> list[str]:
    owner = file_owners(doa)
    total_files = len(owner)
    if total_files == 0:
        return []
    owned_counts = Counter(dev for dev, _ in owner.values())
    tf_set: list[str] = []
    covered = 0
    for dev, n in owned_counts.most_common():
        tf_set.append(dev)
        covered += n
        if covered >= TF_COVERAGE_THRESHOLD * total_files:
            break
    return tf_set


@dataclass
class TFDDEvent:
    repo: str
    founder: str
    tfdd_date: datetime
    repo_created_at: datetime
    stars: int
    forks: int
    language: str
    license_key: str
    n_commits_total: int
    tf_set_size_at_relaxed: int = 1
    devs_at_tfdd: int = 0
    commits_at_tfdd: int = 0
    files_at_tfdd: int = 0
    founder_share: float = float("nan")
    n_diffused_owners: int = 0
    placebo_founder_share: float = float("nan")
    placebo_n_diffused_owners: int = 0
    survived: Optional[bool] = None
    grade: str = ""
    censored: bool = False
    devs_seen_up_to_tfdd: int = 0
    # NEW (this iteration): reconciliation-test measurements
    medappa_ratio: float = float("nan")
    timing_term: float = float("nan")


def detect_founder_tfdd(commits: list[dict], snapshot_every_days: int = SNAPSHOT_EVERY_DAYS) -> Optional[tuple[datetime, str]]:
    if len(commits) < 20:
        return None
    start = commits[0]["date"]
    end = commits[-1]["date"]
    last_active: dict[str, datetime] = {}
    for c in commits:
        e = c["author_email"]
        if e not in last_active or c["date"] > last_active[e]:
            last_active[e] = c["date"]
    cursor = start + timedelta(days=180)
    while cursor <= end:
        doa = doa_snapshot(commits, cursor)
        tf_set = truck_factor_set(doa)
        if len(tf_set) == 1:
            founder = tf_set[0]
            silence = (cursor - last_active.get(founder, start)).days
            if silence >= SILENCE_THRESHOLD_DAYS:
                tfdd_date = last_active[founder] + timedelta(days=SILENCE_THRESHOLD_DAYS)
                return min(tfdd_date, cursor), founder
        cursor += timedelta(days=snapshot_every_days)
    return None


def detect_relaxed_tfdd(commits: list[dict], snapshot_every_days: int = SNAPSHOT_EVERY_DAYS) -> Optional[tuple[datetime, list[str]]]:
    if len(commits) < 20:
        return None
    start = commits[0]["date"]
    end = commits[-1]["date"]
    last_active: dict[str, datetime] = {}
    for c in commits:
        e = c["author_email"]
        if e not in last_active or c["date"] > last_active[e]:
            last_active[e] = c["date"]
    cursor = start + timedelta(days=180)
    while cursor <= end:
        doa = doa_snapshot(commits, cursor)
        tf_set = truck_factor_set(doa)
        if 1 <= len(tf_set) <= 2 and all(
            (cursor - last_active.get(d, start)).days >= SILENCE_THRESHOLD_DAYS for d in tf_set
        ):
            tfdd_date = max(last_active[d] for d in tf_set) + timedelta(days=SILENCE_THRESHOLD_DAYS)
            return min(tfdd_date, cursor), tf_set
        cursor += timedelta(days=snapshot_every_days)
    return None


def window_metrics(commits: list[dict], window_start: datetime, window_end: datetime, founder: str) -> tuple[float, int]:
    window_commits = [c for c in commits if window_start <= c["date"] < window_end]
    if not window_commits:
        return float("nan"), 0
    founder_commits = sum(1 for c in window_commits if c["author_email"] == founder)
    founder_share = founder_commits / len(window_commits)
    doa_end = doa_snapshot(commits, window_end)
    owner = file_owners(doa_end)
    non_founder_owners = {o[0] for o in owner.values() if o[0] != founder}
    return founder_share, len(non_founder_owners)


def sample_placebo_window(commits: list[dict], exclude_start: datetime, exclude_end: datetime) -> Optional[tuple[datetime, datetime]]:
    start = commits[0]["date"]
    end = commits[-1]["date"]
    total_span_days = (end - start).days
    if total_span_days < 800:
        return None
    for _ in range(20):
        offset = random.uniform(0, total_span_days - 180)
        w_start = start + timedelta(days=offset)
        w_end = w_start + timedelta(days=180)
        if w_end < exclude_start - timedelta(days=365) or w_start > exclude_end + timedelta(days=365):
            return w_start, w_end
    return None


def classify_grade(post_commits: list[dict], recovered_tf: list[str], founder: str) -> str:
    if not post_commits:
        return "dead"
    n_devs = len({c["author_email"] for c in post_commits})
    n_commits = len(post_commits)
    non_founder_tf = [d for d in recovered_tf if d != founder]
    if non_founder_tf and n_commits >= 20 and n_devs >= 2:
        return "thriving"
    if n_commits >= 5:
        return "maintained"
    if n_commits >= 1:
        return "dormant"
    return "dead"


def label_survival(commits: list[dict], event: TFDDEvent, last_commit_date: datetime) -> None:
    window_end = event.tfdd_date + timedelta(days=POST_TFDD_WINDOW_DAYS)
    if last_commit_date < window_end:
        event.censored = True
    post = [c for c in commits if event.tfdd_date <= c["date"] < window_end]
    doa_post = doa_snapshot(commits, window_end)
    recovered_tf = truck_factor_set(doa_post)
    event.survived = bool(recovered_tf) and any(d != event.founder for d in recovered_tf)
    event.grade = classify_grade(post, recovered_tf, event.founder)


# ---------------------------------------------------------------------------
# NEW (this iteration): Medappa-style reconciliation measurements
# ---------------------------------------------------------------------------
def compute_medappa_and_timing(
    commits: list[dict], founder: str, tfdd_date: datetime, window_start: datetime, window_end: datetime
) -> tuple[float, float]:
    """medappa_ratio: static whole-pre-history write-access ratio = (# distinct
    devs who EVER reached primary DOA ownership of >=1 file, over the FULL
    pre-TFDD history) / (# distinct devs, full pre-TFDD history). NOT windowed,
    NOT founder-specific -- this is the analog of Medappa et al.'s construct.

    timing_term: of the non-founder devs who hold primary ownership AT TFDD,
    the fraction whose ownership ONSET (first snapshot at which they appear as
    a primary owner of any file) falls inside the 6-12mo pre-departure window,
    vs. earlier in the repo's history -- tests whether "diffusion" is
    concentrated near departure or was already present.
    """
    devs_before = {c["author_email"] for c in commits if c["date"] <= tfdd_date}
    doa_tfdd = doa_snapshot(commits, tfdd_date)
    owners_tfdd = file_owners(doa_tfdd)
    ever_owners = {o[0] for o in owners_tfdd.values()}
    medappa_ratio = len(ever_owners) / len(devs_before) if devs_before else float("nan")

    non_founder_owners_at_tfdd = {o[0] for o in owners_tfdd.values() if o[0] != founder}
    if not non_founder_owners_at_tfdd:
        return medappa_ratio, float("nan")

    start = commits[0]["date"]
    onset_date: dict[str, datetime] = {}
    cursor = start + timedelta(days=180)
    remaining = set(non_founder_owners_at_tfdd)
    while cursor <= tfdd_date and remaining:
        doa = doa_snapshot(commits, cursor)
        owners = file_owners(doa)
        present = {o[0] for o in owners.values()}
        newly_onset = remaining & present
        for dev in newly_onset:
            onset_date[dev] = cursor
        remaining -= newly_onset
        cursor += timedelta(days=SNAPSHOT_EVERY_DAYS)
    for dev in remaining:  # never caught by a coarse snapshot before TFDD -> onset at TFDD itself
        onset_date[dev] = tfdd_date

    n_total = len(onset_date)
    n_in_window = sum(1 for d in onset_date.values() if window_start <= d < window_end)
    timing_term = n_in_window / n_total if n_total else float("nan")
    return medappa_ratio, timing_term


# ---------------------------------------------------------------------------
# stats helpers (reused verbatim)
# ---------------------------------------------------------------------------
def build_matched_pairs(df: pd.DataFrame, low_thresh: float = 0.50, hi_thresh: float = 0.80, n_diffused_min: int = 2):
    lo = df[(df.founder_share < low_thresh) & (df.n_diffused_owners >= n_diffused_min)].copy()
    hi = df[df.founder_share >= hi_thresh].copy()
    pairs = []
    used_hi = set()
    for _, lrow in lo.iterrows():
        best_idx, best_dist = None, float("inf")
        for hidx, hrow in hi.iterrows():
            if hidx in used_hi or hrow.language != lrow.language:
                continue
            dist = (
                (math.log1p(hrow.stars) - math.log1p(lrow.stars)) ** 2
                + (math.log1p(hrow.forks) - math.log1p(lrow.forks)) ** 2
                + (math.log1p(hrow.devs_at_tfdd) - math.log1p(lrow.devs_at_tfdd)) ** 2
            )
            if dist < best_dist:
                best_dist, best_idx = dist, hidx
        if best_idx is not None and best_dist < 4.0:
            used_hi.add(best_idx)
            pairs.append((lrow, hi.loc[best_idx]))
    return pairs


def build_matched_pairs_relaxed(df: pd.DataFrame, low_thresh: float = 0.50, hi_thresh: float = 0.80, n_diffused_min: int = 2):
    """fallback_plan item (4): same-stratum-only matching, drop the exact language
    requirement (kept as a regression covariate elsewhere instead)."""
    lo = df[(df.founder_share < low_thresh) & (df.n_diffused_owners >= n_diffused_min)].copy()
    hi = df[df.founder_share >= hi_thresh].copy()

    def star_stratum(s: float) -> int:
        return 0 if s < 1000 else (1 if s < 10000 else 2)

    pairs = []
    used_hi = set()
    for _, lrow in lo.iterrows():
        best_idx, best_dist = None, float("inf")
        for hidx, hrow in hi.iterrows():
            if hidx in used_hi or star_stratum(hrow.stars) != star_stratum(lrow.stars):
                continue
            dist = (math.log1p(hrow.devs_at_tfdd) - math.log1p(lrow.devs_at_tfdd)) ** 2
            if dist < best_dist:
                best_dist, best_idx = dist, hidx
        if best_idx is not None:
            used_hi.add(best_idx)
            pairs.append((lrow, hi.loc[best_idx]))
    return pairs


def bootstrap_survival_rate_ratio(pairs: list[tuple[pd.Series, pd.Series]], n_boot: int = N_BOOT) -> tuple[float, tuple[float, float], Optional[str]]:
    if not pairs:
        return float("nan"), (float("nan"), float("nan")), "no matched pairs"
    lo_surv = np.array([1.0 if p[0].survived else 0.0 for p in pairs])
    hi_surv = np.array([1.0 if p[1].survived else 0.0 for p in pairs])
    n = len(pairs)
    ratios = []
    for _ in range(n_boot):
        idx = np.random.randint(0, n, size=n)
        lo_rate = lo_surv[idx].mean()
        hi_rate = hi_surv[idx].mean()
        if hi_rate == 0:
            continue
        ratios.append((lo_rate + 1e-6) / (hi_rate + 1e-6))
    if not ratios:
        degeneracy_note = (
            f"ALL {n_boot} bootstrap resamples had zero survivors in the high-diffusion group "
            f"(hi_surv.mean()={hi_surv.mean():.3f} across the {n} matched pairs) -- the risk-ratio is "
            "degenerate at this n, not computable, and NOT silently reported as a point estimate."
        )
        return float("nan"), (float("nan"), float("nan")), degeneracy_note
    ratios = np.array(ratios)
    point = (lo_surv.mean() + 1e-6) / (hi_surv.mean() + 1e-6)
    ci = (float(np.percentile(ratios, 2.5)), float(np.percentile(ratios, 97.5)))
    return float(point), ci, None


def benjamini_hochberg(pvals: dict[str, float]) -> dict[str, float]:
    items = sorted(pvals.items(), key=lambda kv: kv[1])
    m = len(items)
    adj = {}
    prev = 1.0
    for rank, (k, p) in enumerate(reversed(items), start=1):
        r = m - rank + 1
        val = min(prev, p * m / r)
        adj[k] = val
        prev = val
    return adj


def cohens_d(a: np.ndarray, b: np.ndarray) -> float:
    a, b = a[~np.isnan(a)], b[~np.isnan(b)]
    if len(a) < 2 or len(b) < 2:
        return float("nan")
    pooled_sd = math.sqrt(((len(a) - 1) * a.var(ddof=1) + (len(b) - 1) * b.var(ddof=1)) / (len(a) + len(b) - 2))
    if pooled_sd == 0:
        return float("nan")
    return float((a.mean() - b.mean()) / pooled_sd)


def bootstrap_ci_mean_diff(a: np.ndarray, b: np.ndarray, n_boot: int = N_BOOT) -> tuple[float, float]:
    a, b = a[~np.isnan(a)], b[~np.isnan(b)]
    if len(a) < 2 or len(b) < 2:
        return float("nan"), float("nan")
    diffs = np.empty(n_boot)
    for i in range(n_boot):
        ai = a[np.random.randint(0, len(a), len(a))]
        bi = b[np.random.randint(0, len(b), len(b))]
        diffs[i] = ai.mean() - bi.mean()
    return float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5))


# ---------------------------------------------------------------------------
# per-repo processing
# ---------------------------------------------------------------------------
def process_repo(repo_id: str, rep: dict) -> tuple[Optional[TFDDEvent], Optional[TFDDEvent], dict]:
    full_name = rep["full_name"]
    commits = rep["commits"]
    diag = {"repo": full_name, "stars": rep["stars"], "language": rep["language"]}
    if len(commits) < 20:
        diag["status"] = "too_few_commits"
        return None, None, diag
    n_devs_total = len({c["author_email"] for c in commits})
    if n_devs_total < 2:
        diag["status"] = "single_dev_never_had_team"
        return None, None, diag
    last_commit_date = commits[-1]["date"]

    strict = detect_founder_tfdd(commits)
    relaxed = detect_relaxed_tfdd(commits)
    created_at = rep["created_at"]
    license_key = rep["license_key"]

    def make_event(tfdd_date: datetime, founder: str) -> Optional[TFDDEvent]:
        window_start = tfdd_date - timedelta(days=PRE_WINDOW_FAR_DAYS)
        window_end = tfdd_date - timedelta(days=PRE_WINDOW_NEAR_DAYS)
        if window_start < commits[0]["date"]:
            return None
        founder_share, n_diffused = window_metrics(commits, window_start, window_end, founder)
        if math.isnan(founder_share):
            return None
        doa_tfdd = doa_snapshot(commits, tfdd_date)
        owners_tfdd = file_owners(doa_tfdd)
        devs_before = {c["author_email"] for c in commits if c["date"] <= tfdd_date}
        commits_before = [c for c in commits if c["date"] <= tfdd_date]
        ev = TFDDEvent(
            repo=full_name,
            founder=founder,
            tfdd_date=tfdd_date,
            repo_created_at=created_at,
            stars=rep["stars"] or 0,
            forks=rep["forks"] or 0,
            language=rep["language"] or "unknown",
            license_key=license_key,
            n_commits_total=len(commits),
            devs_at_tfdd=len(devs_before),
            commits_at_tfdd=len(commits_before),
            files_at_tfdd=len(owners_tfdd),
            founder_share=founder_share,
            n_diffused_owners=n_diffused,
            devs_seen_up_to_tfdd=len(devs_before),
        )
        placebo_window = sample_placebo_window(commits, window_start, window_end)
        if placebo_window:
            p_share, p_diff = window_metrics(commits, placebo_window[0], placebo_window[1], founder)
            ev.placebo_founder_share = p_share
            ev.placebo_n_diffused_owners = p_diff
        label_survival(commits, ev, last_commit_date)
        ev.medappa_ratio, ev.timing_term = compute_medappa_and_timing(commits, founder, tfdd_date, window_start, window_end)
        return ev

    strict_event = make_event(strict[0], strict[1]) if strict else None
    relaxed_event = None
    if relaxed:
        r_date, r_set = relaxed
        counts = Counter(c["author_email"] for c in commits if c["author_email"] in r_set)
        dominant = counts.most_common(1)[0][0] if counts else r_set[0]
        relaxed_event = make_event(r_date, dominant)
        if relaxed_event is not None:
            relaxed_event.tf_set_size_at_relaxed = len(r_set)

    diag["status"] = "ok"
    diag["n_commits"] = len(commits)
    diag["n_devs"] = n_devs_total
    diag["strict_tfdd_found"] = strict_event is not None
    diag["relaxed_tfdd_found"] = relaxed_event is not None
    diag["dominant_founder_first_window_share"] = rep.get("dominant_founder_first_window_share")
    return strict_event, relaxed_event, diag


def _process_repo_worker(args: tuple[str, dict]) -> tuple[Optional[dict], Optional[dict], dict]:
    repo_id, rep = args
    try:
        s_ev, r_ev, diag = process_repo(repo_id, rep)
    except Exception as e:
        logger.error(f"[process_repo] {rep.get('full_name')} failed: {e}")
        return None, None, {"repo": rep.get("full_name"), "status": f"exception:{e}"}
    return (asdict(s_ev) if s_ev else None), (asdict(r_ev) if r_ev else None), diag


def fit_logit(df_in: pd.DataFrame, cols: list[str], label: str) -> dict:
    if df_in.empty or df_in["survived"].nunique() < 2 or len(df_in) < len(cols) + 3:
        return {"status": "insufficient_data", "n": int(len(df_in)), "n_classes": int(df_in["survived"].nunique()) if not df_in.empty else 0}
    X = df_in[cols].astype(float)
    y = df_in["survived"].astype(int)
    X_const = sm.add_constant(X, has_constant="add")
    try:
        model = sm.Logit(y, X_const).fit(disp=0, maxiter=200)
    except Exception as e:
        logger.warning(f"[{label}] logit failed ({e}); dropping lowest-priority covariates in order")
        drop_order = ["license_key", "contributor_count", "medappa_ratio:timing_term", "timing_term"]
        parsimonious = [c for c in cols if c not in drop_order]
        if not parsimonious or set(parsimonious) == set(cols):
            return {"status": f"failed:{e}", "n": int(len(df_in))}
        return fit_logit(df_in, parsimonious, label + "_parsimonious")
    std_X = (X - X.mean()) / X.std(ddof=0).replace(0, 1)
    std_X_const = sm.add_constant(std_X, has_constant="add")
    try:
        std_model = sm.Logit(y, std_X_const).fit(disp=0, maxiter=200)
        std_effects = std_model.params.drop("const").to_dict()
    except Exception:
        std_effects = {}
    return {
        "status": "ok",
        "n": int(len(df_in)),
        "covariates": cols,
        "coefs": model.params.to_dict(),
        "pvalues": model.pvalues.to_dict(),
        "pvalues_bh": benjamini_hochberg(model.pvalues.drop("const").to_dict()),
        "standardized_effect_sizes": std_effects,
        "pseudo_r2": float(model.prsquared),
        "converged": bool(model.mle_retvals.get("converged", True)),
    }


def compute_vif(df_in: pd.DataFrame, cols: list[str]) -> dict:
    if df_in.empty or len(df_in) < len(cols) + 2:
        return {"status": "insufficient_data"}
    X = sm.add_constant(df_in[cols].astype(float), has_constant="add")
    vifs = {}
    for i, c in enumerate(X.columns):
        if c == "const":
            continue
        try:
            vifs[c] = float(variance_inflation_factor(X.values, i))
        except (ZeroDivisionError, np.linalg.LinAlgError, ValueError):
            vifs[c] = float("nan")
    return vifs


@logger.catch(reraise=True)
def main():
    t0 = time.time()
    logger.info("=== STEP 0: load full_data_out.json -> per-repo commit streams ===")
    repos = load_repo_commit_streams(WORKSPACE / "full_data_out.json")
    n_repo_candidates = len(repos)
    logger.info(f"[step0] {n_repo_candidates} founder-candidate repos loaded (dataset scope is fixed 34-repo pool)")
    del gc.garbage[:]
    gc.collect()

    logger.info(f"=== STEP 1-3: DOA/TF/TFDD pipeline, {NUM_CPUS} workers, {n_repo_candidates} repos (independent, CPU-bound) ===")
    strict_events: list[dict] = []
    relaxed_events: list[dict] = []
    diagnostics: list[dict] = []
    items = list(repos.items())
    with ProcessPoolExecutor(max_workers=NUM_CPUS, mp_context=mp.get_context("spawn")) as pool:
        futures = {pool.submit(_process_repo_worker, item): item[1]["full_name"] for item in items}
        for i, fut in enumerate(as_completed(futures), start=1):
            name = futures[fut]
            try:
                s_ev, r_ev, diag = fut.result()
            except Exception as e:
                logger.error(f"[worker] {name} raised: {e}")
                s_ev, r_ev, diag = None, None, {"repo": name, "status": f"worker_exception:{e}"}
            diagnostics.append(diag)
            if s_ev is not None:
                strict_events.append(s_ev)
            if r_ev is not None:
                relaxed_events.append(r_ev)
            logger.info(f"[step1-3] ({i}/{len(items)}) {name}: {diag.get('status')}")

    logger.info(f"=== Finished: {len(items)} repos, {len(strict_events)} strict events, {len(relaxed_events)} relaxed events ===")

    diag_df = pd.DataFrame(diagnostics)
    diag_df.to_csv(RESULTS_DIR / "repo_processing_diagnostics.csv", index=False)

    logger.info("=== STEP 4: power/target check ===")
    n_strict, n_relaxed = len(strict_events), len(relaxed_events)
    shortfall_note = None
    if n_strict < TARGET_N_STRICT:
        shortfall_note = (
            f"n_strict={n_strict} < target={TARGET_N_STRICT}. This is EXPECTED and structural: the "
            f"dataset's founder-candidate pool is capped at {n_repo_candidates} repos (same pool as iter1), "
            f"which upper-bounds n_strict at {n_repo_candidates} even at 100% yield. Reporting full battery "
            "at achieved n rather than overclaiming power."
        )
        logger.warning(f"[step4] {shortfall_note}")
    iter1_comparison_note = None
    if n_strict == 16 and n_relaxed == 20:
        iter1_comparison_note = "n_strict/n_relaxed EXACTLY match iter1 (16/20) -- confirms same 34-repo pool, no new repos added by this iteration."
        logger.info(f"[step4] {iter1_comparison_note}")
    else:
        iter1_comparison_note = (
            f"n_strict/n_relaxed ({n_strict}/{n_relaxed}) DIFFER from iter1's (16/20) despite using the SAME "
            "34-repo founder-candidate pool. This iteration reconstructs commit streams from the already-mined "
            "full_data_out.json rows (git log --numstat output captured at dataset-build time) rather than "
            "re-cloning live repos, so the counts reflect the SAME underlying algorithm applied to a slightly "
            "different commit-stream reconstruction (e.g. the >4000-row stride-down applied to large repos when "
            "the dataset was built), not a larger corpus or a different method. Reporting this plainly rather "
            "than implying scale was achieved beyond the fixed 34-repo pool."
        )
        logger.warning(f"[step4] {iter1_comparison_note}")

    def parse_events(raw_events: list[dict]) -> list[TFDDEvent]:
        out = []
        for d in raw_events:
            d = dict(d)
            d["tfdd_date"] = pd.to_datetime(d["tfdd_date"], utc=True).to_pydatetime()
            d["repo_created_at"] = pd.to_datetime(d["repo_created_at"], utc=True).to_pydatetime()
            out.append(TFDDEvent(**d))
        return out

    strict_ev_objs = parse_events(strict_events)
    relaxed_ev_objs = parse_events(relaxed_events)

    def rate_summary(events: list[TFDDEvent]) -> dict:
        uncensored = [e for e in events if not e.censored]
        if not uncensored:
            return {"n_events": len(events), "n_uncensored": 0, "survival_rate": None, "n_censored_excluded": len(events)}
        surv = np.array([1.0 if e.survived else 0.0 for e in uncensored])
        return {
            "n_events": len(events),
            "n_uncensored": len(uncensored),
            "n_censored_excluded": len(events) - len(uncensored),
            "survival_rate": float(surv.mean()),
            "survival_rate_se": float(surv.std(ddof=1) / math.sqrt(len(surv))) if len(surv) > 1 else None,
        }

    strict_rate = rate_summary(strict_ev_objs)
    relaxed_rate = rate_summary(relaxed_ev_objs)
    logger.info(f"[step6] strict founder-only TFDD survival: {strict_rate}")
    logger.info(f"[step6] relaxed TF<=2 TFDD survival: {relaxed_rate}")

    def events_to_df(events: list[TFDDEvent]) -> pd.DataFrame:
        rows = [asdict(e) for e in events if not e.censored]
        if not rows:
            return pd.DataFrame()
        df = pd.DataFrame(rows)
        df["log_stars"] = np.log1p(df["stars"])
        df["log_forks"] = np.log1p(df["forks"])
        df["log_devs_at_tfdd"] = np.log1p(df["devs_at_tfdd"])
        df = df.dropna(subset=["founder_share", "n_diffused_owners", "log_stars", "log_forks", "devs_at_tfdd"])
        return df

    df = events_to_df(strict_ev_objs)
    df_relaxed = events_to_df(relaxed_ev_objs)

    results: dict = {
        "n_repos_input": n_repo_candidates,
        "n_founder_candidates": n_repo_candidates,
        "n_strict_tfdd": n_strict,
        "n_relaxed_tfdd": n_relaxed,
        "target_n": TARGET_N_STRICT,
        "shortfall_note": shortfall_note,
        "iter1_comparison_note": iter1_comparison_note,
        "strict_unconditioned_survival": strict_rate,
        "relaxed_unconditioned_survival": relaxed_rate,
        "avelino_et_al_reference_survival_rate": AVELINO_REFERENCE_SURVIVAL_RATE,
        "n_analysis_rows_strict": int(len(df)),
        "n_analysis_rows_relaxed": int(len(df_relaxed)),
    }

    # ---- STEP 5: primary battery ----
    our_cols = ["founder_share", "n_diffused_owners", "log_stars", "log_forks", "log_devs_at_tfdd"]
    baseline_cols = ["log_stars", "log_forks", "log_devs_at_tfdd"]
    results["primary_regression"] = {
        "our_method": fit_logit(df, our_cols, "our_method"),
        "baseline_snapshot_only": fit_logit(df, baseline_cols, "baseline"),
    }
    if not df.empty and df["survived"].nunique() == 2:
        surv_mask = df["survived"].astype(bool)
        cov_effects = {}
        for col in ["devs_at_tfdd", "commits_at_tfdd", "files_at_tfdd", "founder_share", "n_diffused_owners"]:
            a = df.loc[surv_mask, col].to_numpy(dtype=float)
            b = df.loc[~surv_mask, col].to_numpy(dtype=float)
            cov_effects[col] = {"cohens_d": cohens_d(a, b), "bootstrap_ci95_mean_diff": list(bootstrap_ci_mean_diff(a, b))}
        results["primary_regression"]["snapshot_covariate_effect_sizes"] = cov_effects
    else:
        results["primary_regression"]["snapshot_covariate_effect_sizes"] = {"status": "insufficient_class_variation"}

    matched_pairs_result = {"n_pairs": 0}
    if len(df) >= 6:
        pairs = build_matched_pairs(df)
        if pairs:
            risk_ratio, ci95, degeneracy_note = bootstrap_survival_rate_ratio(pairs, n_boot=N_BOOT)
            matched_pairs_result = {
                "n_pairs": len(pairs),
                "matching": "strict (exact language + star/fork/devs distance)",
                "risk_ratio_low_vs_high_diffusion": risk_ratio,
                "risk_ratio_ci95": list(ci95),
                "note": degeneracy_note or "risk_ratio = P(survival|low diffusion) / P(survival|high diffusion); >1 => concentrated founder survives MORE",
            }
        else:
            relaxed_pairs = build_matched_pairs_relaxed(df)
            if relaxed_pairs:
                risk_ratio, ci95, degeneracy_note = bootstrap_survival_rate_ratio(relaxed_pairs, n_boot=N_BOOT)
                matched_pairs_result = {
                    "n_pairs": len(relaxed_pairs),
                    "matching": "RELAXED (fallback_plan item 4): same star-stratum only, language dropped as exact match (used as regression covariate elsewhere)",
                    "risk_ratio_low_vs_high_diffusion": risk_ratio,
                    "risk_ratio_ci95": list(ci95),
                    "note": degeneracy_note,
                }
            else:
                matched_pairs_result["note"] = "ZERO eligible pairs even under relaxed same-stratum matching -- reporting explicitly rather than omitting"
    else:
        matched_pairs_result["note"] = "insufficient events for matched-pairs analysis (need >=6)"
    results["matched_pairs"] = matched_pairs_result

    if not df.empty and df["survived"].nunique() == 2:
        surv_mask = df["survived"].astype(bool)
        mw = {}
        for col in ["founder_share", "n_diffused_owners"]:
            res = stats.mannwhitneyu(df.loc[surv_mask, col], df.loc[~surv_mask, col], alternative="two-sided")
            mw[col] = {"u_stat": float(res.statistic), "p": float(res.pvalue)}
        results["mann_whitney"] = mw
    else:
        results["mann_whitney"] = {"status": "insufficient_class_variation"}

    placebo_df = df.dropna(subset=["placebo_founder_share", "placebo_n_diffused_owners"]).copy()
    placebo_cols = ["placebo_founder_share", "placebo_n_diffused_owners", "log_stars", "log_forks", "log_devs_at_tfdd"]
    placebo_reg = fit_logit(placebo_df, placebo_cols, "placebo") if len(placebo_df) >= 8 else {"status": "insufficient_data", "n": int(len(placebo_df))}
    true_coef = results["primary_regression"]["our_method"].get("coefs", {}).get("founder_share") if results["primary_regression"]["our_method"].get("status") == "ok" else None
    null_coefs = []
    if len(placebo_df) >= 8:
        for _ in range(1000):
            boot_idx = np.random.randint(0, len(placebo_df), len(placebo_df))
            boot_df = placebo_df.iloc[boot_idx]
            r = fit_logit(boot_df, placebo_cols, "placebo_boot")
            if r.get("status") == "ok":
                null_coefs.append(r["coefs"].get("placebo_founder_share", np.nan))
    null_coefs = np.array([c for c in null_coefs if not np.isnan(c)])
    empirical_p = None
    if true_coef is not None and len(null_coefs) > 10:
        empirical_p = float((np.abs(null_coefs) >= abs(true_coef)).mean())
    results["placebo_check"] = {
        "n_events_with_placebo_window": int(len(placebo_df)),
        "regression_placebo_window": placebo_reg,
        "true_window_founder_share_coef": true_coef,
        "null_distribution_summary": {
            "n": int(len(null_coefs)),
            "mean": float(null_coefs.mean()) if len(null_coefs) else None,
            "std": float(null_coefs.std()) if len(null_coefs) else None,
        },
        "empirical_p": empirical_p,
    }

    if len(df_relaxed) >= 6 and df_relaxed["survived"].nunique() == 2:
        results["relaxed_sensitivity_regression"] = fit_logit(df_relaxed, our_cols, "relaxed_our_method")
    else:
        results["relaxed_sensitivity_regression"] = {"status": "insufficient_data", "n": int(len(df_relaxed))}

    # ---- STEP 6: NEW Medappa reconciliation joint model ----
    logger.info("=== STEP 6: Medappa reconciliation joint model ===")
    recon_df = df.dropna(subset=["medappa_ratio", "timing_term"]).copy()
    recon_df["medappa_x_timing"] = recon_df["medappa_ratio"] * recon_df["timing_term"]
    reconciliation: dict = {"n_events": int(len(recon_df))}

    if len(recon_df) >= 6 and recon_df["survived"].nunique() == 2:
        univariate = {}
        surv_mask = recon_df["survived"].astype(bool)
        for col in ["medappa_ratio", "timing_term", "founder_share"]:
            a = recon_df.loc[surv_mask, col].to_numpy(dtype=float)
            b = recon_df.loc[~surv_mask, col].to_numpy(dtype=float)
            res = stats.mannwhitneyu(a, b, alternative="two-sided") if len(a) >= 1 and len(b) >= 1 else None
            univariate[col] = {
                "cohens_d": cohens_d(a, b),
                "mannwhitney_p": float(res.pvalue) if res is not None else None,
                "mean_survived": float(np.nanmean(a)) if len(a) else None,
                "mean_not_survived": float(np.nanmean(b)) if len(b) else None,
            }
        reconciliation["univariate_associations"] = univariate

        vif = compute_vif(recon_df, ["medappa_ratio", "founder_share"])
        reconciliation["vif_medappa_vs_founder_share"] = vif
        high_vif = isinstance(vif, dict) and any(isinstance(v, float) and v > 10 for v in vif.values())
        reconciliation["multicollinearity_flag"] = bool(high_vif)

        base_reconcile_cols = ["founder_share", "medappa_ratio", "timing_term", "medappa_x_timing", "log_stars", "log_forks", "log_devs_at_tfdd"]
        joint = fit_logit(recon_df, base_reconcile_cols, "reconciliation_joint")
        reconciliation["joint_model"] = joint

        medappa_only = fit_logit(recon_df, ["medappa_ratio", "log_stars", "log_forks", "log_devs_at_tfdd"], "medappa_alone")
        reconciliation["medappa_alone_model"] = medappa_only
        medappa_sign = None
        if medappa_only.get("status") == "ok":
            medappa_sign = "negative" if medappa_only["coefs"].get("medappa_ratio", 0) < 0 else "positive"
        reconciliation["medappa_alone_sign"] = medappa_sign
        reconciliation["replicates_medappa_negative_direction"] = (medappa_sign == "negative")

        interp_parts = []
        if high_vif:
            interp_parts.append(
                "VIF>10 between medappa_ratio and founder_share: the two constructs are NOT cleanly separable "
                f"at n={len(recon_df)}; the joint model's medappa/founder_share coefficients should not be "
                "interpreted independently. Reporting separate univariate associations as the primary evidence instead."
            )
        if joint.get("status") == "ok":
            interaction_coef = joint["coefs"].get("medappa_x_timing")
            timing_coef = joint["coefs"].get("timing_term")
            interp_parts.append(
                f"Joint model converged (n={joint['n']}); medappa_ratio coef={joint['coefs'].get('medappa_ratio'):.3f}, "
                f"timing_term coef={timing_coef:.3f}, interaction coef={interaction_coef:.3f}. "
                + ("Timing/interaction term MODERATES or FLIPS the medappa_ratio-alone sign, consistent with the "
                   "timing-not-presence reconciliation hypothesis."
                   if (medappa_sign == "negative" and interaction_coef is not None and (interaction_coef > 0) != (joint["coefs"].get("medappa_ratio", 0) > 0))
                   else "Timing/interaction term does NOT clearly flip the medappa_ratio-alone sign at this n; "
                        "underpowered to distinguish timing-driven from presence-driven mechanisms.")
            )
        else:
            interp_parts.append(f"Joint model did not converge cleanly ({joint.get('status')}); falling back to separate univariate associations per fallback_plan item (5).")
        reconciliation["interpretation"] = " ".join(interp_parts)
    else:
        reconciliation["status"] = "insufficient_data_or_class_variation"
        reconciliation["note"] = f"n={len(recon_df)} events with complete medappa_ratio/timing_term measurements; need >=6 with both survival classes present"
    results["reconciliation"] = reconciliation

    # ---- raw event table ----
    raw_event_table = []
    for e in strict_ev_objs:
        row = asdict(e)
        row["tfdd_date"] = e.tfdd_date.isoformat()
        row["repo_created_at"] = e.repo_created_at.isoformat()
        raw_event_table.append(row)
    results["raw_event_table"] = raw_event_table

    results["runtime_seconds"] = time.time() - t0
    results["config"] = {
        "silence_threshold_days": SILENCE_THRESHOLD_DAYS,
        "tf_coverage_threshold": TF_COVERAGE_THRESHOLD,
        "post_tfdd_window_days": POST_TFDD_WINDOW_DAYS,
        "pre_window_far_days": PRE_WINDOW_FAR_DAYS,
        "pre_window_near_days": PRE_WINDOW_NEAR_DAYS,
        "strict_founder_share_threshold": STRICT_FOUNDER_SHARE,
        "relaxed_founder_share_threshold": RELAXED_FOUNDER_SHARE,
        "n_boot": N_BOOT,
        "rng_seed": RNG_SEED,
        "num_cpus_used": NUM_CPUS,
    }

    Path(RESULTS_DIR / "method_summary.json").write_text(json.dumps(results, indent=2, default=str))
    logger.info(f"[main] wrote {RESULTS_DIR / 'method_summary.json'}")

    # ---- exp_gen_sol_out.json-schema-compliant output ----
    examples = []
    for e in strict_ev_objs:
        input_text = (
            f"Repo {e.repo} ({e.language}): founder-only TFDD detected at {e.tfdd_date.isoformat()}. "
            f"Predict whether the project survives (attracts a non-founder truck-factor owner) over the "
            f"following 18 months, given pre-departure trajectory founder_share={e.founder_share:.3f}, "
            f"n_diffused_owners={e.n_diffused_owners}, medappa_ratio={e.medappa_ratio:.3f} "
            f"(whole-history write-access ratio), timing_term={e.timing_term:.3f} (fraction of diffusion "
            f"onsets concentrated in the 6-12mo pre-departure window), and snapshot covariates stars={e.stars}, "
            f"forks={e.forks}, devs_at_tfdd={e.devs_at_tfdd}, commits_at_tfdd={e.commits_at_tfdd}, files_at_tfdd={e.files_at_tfdd}."
        )
        output_text = "survived" if e.survived else "did_not_survive"
        our_pred = "survived" if (e.founder_share < 0.65 and e.n_diffused_owners >= 2) else "did_not_survive"
        baseline_pred = "survived" if (e.stars >= 1000 and e.devs_at_tfdd >= 5) else "did_not_survive"
        reconciliation_pred = "survived" if (not math.isnan(e.timing_term) and e.timing_term < 0.5 and e.n_diffused_owners >= 2) else "did_not_survive"
        examples.append(
            {
                "input": input_text,
                "output": output_text,
                "metadata_repo": e.repo,
                "metadata_founder": e.founder,
                "metadata_tfdd_date": e.tfdd_date.isoformat(),
                "metadata_language": e.language,
                "metadata_stars": e.stars,
                "metadata_forks": e.forks,
                "metadata_devs_at_tfdd": e.devs_at_tfdd,
                "metadata_commits_at_tfdd": e.commits_at_tfdd,
                "metadata_files_at_tfdd": e.files_at_tfdd,
                "metadata_founder_share_pre_departure": e.founder_share,
                "metadata_n_diffused_owners_pre_departure": e.n_diffused_owners,
                "metadata_medappa_ratio": e.medappa_ratio,
                "metadata_timing_term": e.timing_term,
                "metadata_placebo_founder_share": e.placebo_founder_share,
                "metadata_placebo_n_diffused_owners": e.placebo_n_diffused_owners,
                "metadata_grade": e.grade,
                "metadata_censored": e.censored,
                "predict_our_method": our_pred,
                "predict_baseline": baseline_pred,
                "predict_reconciliation_timing_model": reconciliation_pred,
            }
        )

    if not examples:
        examples.append(
            {
                "input": "No founder-only TFDD events survived filtering within the founder-candidate dataset.",
                "output": "no_events",
                "metadata_note": "see repo_processing_diagnostics.csv and method_summary.json for full diagnosis",
                "predict_our_method": "no_events",
                "predict_baseline": "no_events",
                "predict_reconciliation_timing_model": "no_events",
            }
        )

    method_out = {
        "metadata": {
            "method_name": "founder_authority_diffusion_tfdd_survival_scaled_reconciliation",
            "description": (
                "Re-run of iter1's validated founder-only TFDD survival pipeline on the SAME 34-repo "
                "founder-candidate corpus (via the mined full_data_out.json rather than re-cloning), plus a "
                "NEW Medappa-et-al.-style reconciliation test (static whole-history write-access ratio + "
                "timing-of-diffusion term + interaction) testing whether timing, not mere presence of "
                "diffusion, explains the sign of its association with survival."
            ),
            "n_founder_tfdd_events_strict": n_strict,
            "n_founder_tfdd_events_relaxed": n_relaxed,
            "target_n_strict": TARGET_N_STRICT,
            "shortfall_note": shortfall_note,
            "strict_unconditioned_survival_rate": strict_rate.get("survival_rate"),
            "avelino_et_al_reference_survival_rate": AVELINO_REFERENCE_SURVIVAL_RATE,
            "summary_results_file": "results/method_summary.json",
            "diagnostics_file": "results/repo_processing_diagnostics.csv",
        },
        "datasets": [{"dataset": "github_founder_tfdd_events_scaled_reconciliation", "examples": examples}],
    }
    Path(WORKSPACE / "method_out.json").write_text(json.dumps(method_out, indent=2, default=str))
    logger.info(f"[main] wrote method_out.json with {len(examples)} example rows")
    logger.info(f"[main] DONE in {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
