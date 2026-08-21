#!/usr/bin/env python3
"""Founder-departure authority-diffusion vs. post-TFDD survival pipeline.

Reimplements Avelino et al. (ESEM 2019) DOA / Truck-Factor / TFDD pipeline on a
GitHub commit-history corpus, adds a NEW pre-departure authority-diffusion
trajectory covariate, and tests whether it predicts 18-month post-TFDD survival
beyond Avelino et al.'s own at-TFDD snapshot covariates (size/popularity), via
(1) matched-pairs comparison, (2) BH-corrected logistic + ordinal regression,
(3) a window-shuffle placebo check.
"""

from __future__ import annotations

import argparse
import gc
import glob
import json
import multiprocessing as mp
import random
import resource
import sys
import time
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional

import numpy as np
import pandas as pd
import psutil
import statsmodels.api as sm
from loguru import logger
from scipy import stats
from sklearn.neighbors import NearestNeighbors
from statsmodels.stats.multitest import multipletests

try:
    from statsmodels.miscmodels.ordinal_model import OrderedModel
except Exception:  # pragma: no cover
    OrderedModel = None

WORKSPACE = Path(__file__).resolve().parent
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
(WORKSPACE / "logs").mkdir(exist_ok=True)
logger.add(WORKSPACE / "logs" / "run.log", rotation="30 MB", level="DEBUG")

# ---------------------------------------------------------------------------
# Resource limits (aii-use-hardware): container cap is 57GB, cap ourselves at
# a conservative 20GB virtual address space budget for this CPU-bound job.
# ---------------------------------------------------------------------------
_avail = psutil.virtual_memory().available
RAM_BUDGET = min(20 * 1024**3, int(_avail * 0.5))
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))

NUM_CPUS = max(1, min(11, len(psutil.Process().cpu_affinity()) if hasattr(psutil.Process(), "cpu_affinity") else 8))

# Fritz et al. DOA weights, as used by Avelino et al. (ESEM 2019)
DOA_FA, DOA_LOG, DOA_AC = 3.293, 1.098, -1.017
SILENCE_MONTHS = 12
SURVIVAL_WINDOW_MONTHS = 18
PRE_WINDOW_FAR_MONTHS = 12
PRE_WINDOW_NEAR_MONTHS = 6
N_PLACEBO_DRAWS = 500
N_BOOTSTRAP = 10_000
RNG_SEED = 20260820

MONTH = timedelta(days=30.4375)


def months(n: float) -> timedelta:
    return n * MONTH


# ---------------------------------------------------------------------------
# STEP 0: data loading + alias resolution
# ---------------------------------------------------------------------------


def _find_dataset_files(data_path: Optional[str]) -> list[Path]:
    """Locate the DATASET dependency's output json(s). Robust to several
    plausible layouts (single file, full_/mini_ split files, per-repo files
    under a datasets/ directory)."""
    candidates: list[Path] = []
    if data_path:
        p = Path(data_path)
        if p.is_file():
            return [p]
        if p.is_dir():
            candidates.extend(sorted(p.glob("**/*.json")))
    if not candidates:
        dep_root = WORKSPACE.parent / "gen_art_dataset_1"
        patterns = [
            "full_data_out*.json",
            "data_out*.json",
            "*data_out*.json",
            "temp/datasets/**/*.json",
        ]
        for pat in patterns:
            candidates.extend(sorted(dep_root.glob(pat)))
    # de-dup, drop mini/preview variants when a full one exists
    seen = set()
    uniq = []
    for c in candidates:
        if c.resolve() not in seen and c.stat().st_size > 0:
            seen.add(c.resolve())
            uniq.append(c)
    return uniq


def _normalize_email(email: str) -> str:
    email = (email or "").strip().lower()
    if "@" in email:
        local, domain = email.rsplit("@", 1)
        local = local.split("+", 1)[0]
        if domain == "users.noreply.github.com":
            # e.g. 12345+login@users.noreply.github.com -> login
            if "+" in local:
                local = local.split("+", 1)[1]
            return f"github:{local}"
        return f"{local}@{domain}"
    return email


def resolve_aliases(commits: pd.DataFrame) -> tuple[pd.Series, float]:
    """Collapse (name, email) pairs onto a canonical author_id.

    Primary key: normalized email (or github login where resolvable via the
    noreply-email convention). Falls back to normalized display name when no
    email is present. Returns (author_id series, collapse_rate)."""
    email_norm = commits.get("author_email", pd.Series([""] * len(commits))).fillna("").map(_normalize_email)
    name_norm = commits.get("author_name", pd.Series([""] * len(commits))).fillna("").str.strip().str.lower()
    login = commits.get("author_login", pd.Series([None] * len(commits)))

    author_id = login.where(login.notna() & (login.astype(str).str.len() > 0), None)
    author_id = author_id.fillna(email_norm.where(email_norm.str.len() > 0, None))
    author_id = author_id.fillna(name_norm)
    author_id = author_id.replace("", "unknown")

    n_raw = commits.get("author_email", email_norm).fillna(commits.get("author_name", name_norm)).nunique()
    n_resolved = author_id.nunique()
    collapse_rate = 0.0 if n_raw == 0 else max(0.0, (n_raw - n_resolved) / n_raw)
    return author_id.astype(str), collapse_rate


def _detect_import_artifact_files(commits: pd.DataFrame) -> pd.DataFrame:
    """Flag and drop bulk-import first commits (Kalliamvakou et al. 2014):
    a commit within the first 7 days touching >80% of the eventual repo's
    file set is almost certainly a migrated-history import, not real
    founder authorship."""
    if commits.empty:
        return commits
    t0 = commits["ts"].min()
    early = commits[commits["ts"] <= t0 + timedelta(days=7)]
    total_files = commits["file"].nunique()
    if total_files == 0:
        return commits
    bad_shas = set()
    for sha, grp in early.groupby("sha"):
        if grp["file"].nunique() / total_files > 0.80 and len(early["sha"].unique()) > 1:
            bad_shas.add(sha)
    if bad_shas:
        commits = commits[~commits["sha"].isin(bad_shas)]
    return commits


def load_repo_commits(raw_repo: dict) -> Optional[dict]:
    """Adapt one dataset-dependency repo record into a normalized dict with
    a commits DataFrame (sha, author_id, ts, file) and repo metadata."""
    meta = raw_repo.get("repo_metadata", raw_repo.get("metadata", raw_repo))
    commit_records = raw_repo.get("commits", raw_repo.get("commit_log", []))
    if not commit_records:
        return None

    rows = []
    for c in commit_records:
        ts_raw = c.get("timestamp") or c.get("committer_date") or c.get("date") or c.get("ts")
        try:
            ts = pd.to_datetime(ts_raw, utc=True)
        except Exception:
            continue
        sha = c.get("sha") or c.get("commit_sha") or c.get("hash")
        author_email = c.get("author_email") or c.get("email")
        author_name = c.get("author_name") or c.get("name")
        author_login = c.get("author_login") or c.get("login")
        files = c.get("files_touched") or c.get("files") or c.get("files_changed") or []
        if isinstance(files, dict):
            files = list(files.keys())
        if not files:
            continue
        for f in files:
            fpath = f.get("path") if isinstance(f, dict) else f
            if not fpath:
                continue
            rows.append(
                dict(
                    sha=sha,
                    ts=ts,
                    author_email=author_email,
                    author_name=author_name,
                    author_login=author_login,
                    file=fpath,
                )
            )
    if not rows:
        return None
    commits = pd.DataFrame(rows)
    commits["author_id"], collapse_rate = resolve_aliases(commits)
    commits = commits.sort_values("ts").reset_index(drop=True)
    commits = _detect_import_artifact_files(commits)
    if commits.empty:
        return None

    repo_id = meta.get("full_name") or meta.get("name") or raw_repo.get("repo") or raw_repo.get("id") or "unknown/unknown"
    stars = float(meta.get("stars", meta.get("stargazers_count", 0)) or 0)
    forks = float(meta.get("forks", meta.get("forks_count", 0)) or 0)
    language = meta.get("language") or "unknown"
    license_ = meta.get("license") or "unknown"
    if isinstance(license_, dict):
        license_ = license_.get("key", license_.get("name", "unknown"))

    return dict(
        repo_id=str(repo_id),
        commits=commits,
        stars=stars,
        forks=forks,
        language=str(language),
        license=str(license_),
        alias_collapse_rate=collapse_rate,
    )


# ---------------------------------------------------------------------------
# STEP 1: yearly DOA table
# ---------------------------------------------------------------------------


def compute_doa_owner_per_file(commits: pd.DataFrame, as_of: pd.Timestamp) -> dict[str, str]:
    """Primary DOA owner per file, using all commits up to `as_of` (cumulative
    window, matching Avelino et al.'s yearly-snapshot design)."""
    window = commits[commits["ts"] <= as_of]
    if window.empty:
        return {}
    owners: dict[str, str] = {}
    for fpath, grp in window.groupby("file"):
        grp_sorted = grp.sort_values("ts")
        first_author = grp_sorted.iloc[0]["author_id"]
        counts = grp["author_id"].value_counts()
        total = counts.sum()
        best_author, best_doa = None, -np.inf
        for author, n in counts.items():
            others = total - n
            doa = DOA_FA * (author == first_author) + DOA_LOG * np.log1p(n) + DOA_AC * np.log1p(others)
            if doa > best_doa:
                best_doa, best_author = doa, author
        if best_author is not None and best_doa > 0:
            owners[fpath] = best_author
    return owners


# ---------------------------------------------------------------------------
# STEP 2: Truck Factor set (greedy, half-of-files criterion)
# ---------------------------------------------------------------------------


def truck_factor_set(file_owner: dict[str, str]) -> list[str]:
    if not file_owner:
        return []
    owned_files: dict[str, set] = defaultdict(set)
    for f, a in file_owner.items():
        owned_files[a].add(f)
    total = len(file_owner)
    remaining = set(file_owner.keys())
    tf_set: list[str] = []
    covered = 0
    while covered < 0.5 * total and owned_files:
        top_author = max(owned_files, key=lambda a: len(owned_files[a] & remaining))
        top_files = owned_files.pop(top_author) & remaining
        if not top_files:
            break
        tf_set.append(top_author)
        remaining -= top_files
        covered = total - len(remaining)
    return tf_set


# ---------------------------------------------------------------------------
# STEP 3: TFDD detection (per-repo, worker function for multiprocessing)
# ---------------------------------------------------------------------------


@dataclass
class RepoResult:
    repo_id: str
    language: str
    license: str
    stars: float
    forks: float
    alias_collapse_rate: float
    has_founder_tfdd: bool = False
    tfdd_date: Optional[str] = None
    founder: Optional[str] = None
    founder_share_pre: Optional[float] = None
    n_diffuse_owners_pre: Optional[float] = None
    diffusion_score: Optional[float] = None
    developers_at_tfdd: Optional[int] = None
    commits_at_tfdd: Optional[int] = None
    files_at_tfdd: Optional[int] = None
    contributor_count: Optional[int] = None
    survival_label: Optional[str] = None
    survived_binary: Optional[int] = None
    placebo_founder_shares: list = field(default_factory=list)
    placebo_n_diffuse_owners: list = field(default_factory=list)
    error: Optional[str] = None


def _year_ends(commits: pd.DataFrame) -> list[pd.Timestamp]:
    y0, y1 = commits["ts"].min().year, commits["ts"].max().year
    return [pd.Timestamp(year=y, month=12, day=31, tz="UTC") for y in range(y0, y1 + 1)]


def _first_commit_author(commits: pd.DataFrame) -> str:
    first_ts = commits["ts"].min()
    early = commits[commits["ts"] <= first_ts + timedelta(days=1)]
    return early["author_id"].value_counts().idxmax()


def classify_survival(commits: pd.DataFrame, tfdd_date: pd.Timestamp, departing_set: set) -> tuple[str, int]:
    window_end = tfdd_date + months(SURVIVAL_WINDOW_MONTHS)
    post = commits[(commits["ts"] > tfdd_date) & (commits["ts"] <= window_end)]
    pre = commits[commits["ts"] <= tfdd_date]
    if post.empty:
        return "dead", 0
    new_dev_commits = post[~post["author_id"].isin(departing_set)]
    n_new_devs = new_dev_commits["author_id"].nunique()
    if n_new_devs == 0:
        return "dormant", 0
    # regained TF set (post-window, using files touched only in the window)
    owners_post = compute_doa_owner_per_file(post, window_end)
    non_dep_owners = {a for a in owners_post.values() if a not in departing_set}
    pre_year = pre[pre["ts"] > tfdd_date - months(12)]
    pre_monthly = pre_year.groupby(pre_year["ts"].dt.to_period("M")).size()
    pre_median = float(pre_monthly.median()) if len(pre_monthly) else 0.0
    post_monthly = post.groupby(post["ts"].dt.to_period("M")).size()
    post_rate = float(post_monthly.mean()) if len(post_monthly) else 0.0
    if len(non_dep_owners) >= 2 and post_rate >= pre_median and pre_median > 0:
        return "thriving", 1
    if len(non_dep_owners) >= 1:
        return "maintained", 1
    return "dormant", 0


def process_repo(raw_repo: dict, seed: int) -> RepoResult:
    rng = random.Random(seed)
    parsed = load_repo_commits(raw_repo)
    if parsed is None:
        return RepoResult(repo_id="unknown", language="unknown", license="unknown", stars=0, forks=0, alias_collapse_rate=0, error="no_commits")
    repo_id, commits = parsed["repo_id"], parsed["commits"]
    base = RepoResult(
        repo_id=repo_id,
        language=parsed["language"],
        license=parsed["license"],
        stars=parsed["stars"],
        forks=parsed["forks"],
        alias_collapse_rate=parsed["alias_collapse_rate"],
    )
    try:
        year_ends = _year_ends(commits)
        if len(year_ends) < 2:
            base.error = "insufficient_history"
            return base
        founder = _first_commit_author(commits)

        yearly_tf: dict[pd.Timestamp, list[str]] = {}
        for ye in year_ends:
            owners = compute_doa_owner_per_file(commits, ye)
            yearly_tf[ye] = truck_factor_set(owners)

        last_commit_by_author = commits.groupby("author_id")["ts"].max()

        tfdd_year_end = None
        departing_set: list[str] = []
        sorted_years = sorted(year_ends)
        for i, ye in enumerate(sorted_years):
            tf_set = yearly_tf[ye]
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
            base.error = "no_tfdd"
            return base
        if len(departing_set) != 1 or departing_set[0] != founder:
            base.error = "not_founder_only_tfdd"
            return base

        tfdd_date = last_commit_by_author[founder] + months(SILENCE_MONTHS)
        min_post_needed = tfdd_date + months(SURVIVAL_WINDOW_MONTHS)
        if commits["ts"].max() < min_post_needed - months(3):
            base.error = "right_censored"
            return base

        base.has_founder_tfdd = True
        base.tfdd_date = tfdd_date.isoformat()
        base.founder = founder

        # STEP 4: pre-departure diffusion trajectory
        def diffusion_in_window(w_start: pd.Timestamp, w_end: pd.Timestamp) -> tuple[float, int]:
            wc = commits[(commits["ts"] >= w_start) & (commits["ts"] < w_end)]
            founder_share = float((wc["author_id"] == founder).sum() / max(len(wc), 1))
            doa_pre = compute_doa_owner_per_file(commits[commits["ts"] < w_end], w_end)
            owners_pre = set(doa_pre.values())
            n_diffuse = len(owners_pre - {founder})
            return founder_share, n_diffuse

        w_start = tfdd_date - months(PRE_WINDOW_FAR_MONTHS)
        w_end = tfdd_date - months(PRE_WINDOW_NEAR_MONTHS)
        founder_share, n_diffuse = diffusion_in_window(w_start, w_end)
        base.founder_share_pre = founder_share
        base.n_diffuse_owners_pre = float(n_diffuse)
        base.diffusion_score = float((1 - founder_share) * np.log1p(n_diffuse))

        # STEP 5: at-TFDD snapshot covariates
        at_tfdd = commits[commits["ts"] <= tfdd_date]
        base.developers_at_tfdd = int(at_tfdd["author_id"].nunique())
        base.commits_at_tfdd = int(at_tfdd["sha"].nunique())
        base.files_at_tfdd = int(at_tfdd["file"].nunique())
        base.contributor_count = int(commits["author_id"].nunique())

        # STEP 6: survival outcome
        label, surv_bin = classify_survival(commits, tfdd_date, set(departing_set))
        base.survival_label = label
        base.survived_binary = surv_bin

        # STEP 9: placebo draws (window-shuffle)
        earliest = commits["ts"].min()
        latest_allowed_start = tfdd_date - months(18) - months(PRE_WINDOW_NEAR_MONTHS)
        if latest_allowed_start > earliest:
            span_days = (latest_allowed_start - earliest).days
            n_draws = min(N_PLACEBO_DRAWS, 20)  # per-repo cap; aggregated across repos downstream
            for _ in range(n_draws):
                offset = rng.uniform(0, max(span_days, 1))
                p_start = earliest + timedelta(days=offset)
                p_end = p_start + months(PRE_WINDOW_FAR_MONTHS - PRE_WINDOW_NEAR_MONTHS)
                if p_end >= w_start:
                    continue
                fs, nd = diffusion_in_window(p_start, p_end)
                base.placebo_founder_shares.append(fs)
                base.placebo_n_diffuse_owners.append(nd)

        return base
    except Exception as e:  # noqa: BLE001
        base.error = f"exception: {e}"
        logger.exception(f"repo {repo_id} failed")
        return base


def _process_repo_star(args):
    return process_repo(*args)


# ---------------------------------------------------------------------------
# Synthetic self-test data (smoke test per testing_plan step 1)
# ---------------------------------------------------------------------------


def make_synthetic_repos(n: int, seed: int = RNG_SEED) -> list[dict]:
    rng = random.Random(seed)
    repos = []
    t0 = datetime(2016, 1, 1, tzinfo=timezone.utc)
    for i in range(n):
        founder = f"founder{i}@example.com"
        files = [f"src/file_{j}.py" for j in range(30)]
        commits = []
        # founder-dominant year 1-2
        for d in range(0, 730, 3):
            ts = t0 + timedelta(days=d)
            commits.append({"sha": f"r{i}c{d}", "timestamp": ts.isoformat(), "author_email": founder, "author_name": f"Founder{i}", "files": [rng.choice(files)]})
        diffuse = i % 2 == 0  # half the repos get a co-maintainer handoff before departure
        if diffuse:
            for k in range(3):
                dev = f"dev{i}_{k}@example.com"
                for d in range(600, 900, 5):
                    ts = t0 + timedelta(days=d)
                    commits.append({"sha": f"r{i}d{k}c{d}", "timestamp": ts.isoformat(), "author_email": dev, "author_name": f"Dev{i}_{k}", "files": [rng.choice(files)]})
        # founder goes silent after day 900; survives if diffuse (new devs keep committing)
        if diffuse:
            for k in range(2):
                dev = f"dev{i}_{k}@example.com"
                for d in range(900, 1700, 4):
                    ts = t0 + timedelta(days=d)
                    commits.append({"sha": f"r{i}s{k}c{d}", "timestamp": ts.isoformat(), "author_email": dev, "author_name": f"Dev{i}_{k}", "files": [rng.choice(files)]})
        else:
            # single-founder repos die after founder goes silent (no new devs)
            for d in range(900, 950, 5):
                ts = t0 + timedelta(days=d)
                commits.append({"sha": f"r{i}tail{d}", "timestamp": ts.isoformat(), "author_email": founder, "author_name": f"Founder{i}", "files": [rng.choice(files)]})
        repos.append(
            {
                "repo": f"synthetic/repo{i}",
                "repo_metadata": {
                    "full_name": f"synthetic/repo{i}",
                    "stars": 100 * (i + 1),
                    "forks": 10 * (i + 1),
                    "language": ["Python", "JavaScript", "Go"][i % 3],
                    "license": "mit",
                },
                "commits": commits,
            }
        )
    return repos


# ---------------------------------------------------------------------------
# STEP 7-9: cross-repo analysis
# ---------------------------------------------------------------------------


def matched_pairs_analysis(df: pd.DataFrame, rng: np.random.Generator) -> dict:
    df = df.copy()
    df["log_stars"] = np.log1p(df["stars"])
    df["log_forks"] = np.log1p(df["forks"])
    df["log_contrib"] = np.log1p(df["contributor_count"])
    high = df[(df["founder_share_pre"] < 0.5) & (df["n_diffuse_owners_pre"] >= 2)]
    low = df[df["founder_share_pre"] >= 0.8]
    pairs = []
    for lang, hgrp in high.groupby("language"):
        lgrp = low[low["language"] == lang]
        if lgrp.empty:
            continue
        feats_low = lgrp[["log_stars", "log_forks", "log_contrib"]].values
        nn = NearestNeighbors(n_neighbors=1).fit(feats_low)
        feats_high = hgrp[["log_stars", "log_forks", "log_contrib"]].values
        dist, idx = nn.kneighbors(feats_high)
        for hi, (d, j) in zip(hgrp.index, zip(dist.ravel(), idx.ravel())):
            pairs.append((hi, lgrp.index[j], float(d)))
    if not pairs:
        return {"n_pairs": 0, "survival_lift": None, "ci_95": None, "p_value": None, "note": "no eligible matched pairs (relaxed matching not triggered: sample too small)"}
    lifts = []
    for hi, li, _ in pairs:
        lifts.append(df.loc[hi, "survived_binary"] - df.loc[li, "survived_binary"])
    lifts = np.array(lifts, dtype=float)
    obs_lift = float(lifts.mean())
    boot = rng.choice(lifts, size=(N_BOOTSTRAP, len(lifts)), replace=True).mean(axis=1)
    ci = (float(np.percentile(boot, 2.5)), float(np.percentile(boot, 97.5)))
    # two-sided p-value from bootstrap null-shift (test lift != 0)
    p = float(2 * min((boot <= 0).mean(), (boot >= 0).mean()))
    p = min(p, 1.0)
    return {"n_pairs": len(pairs), "survival_lift": obs_lift, "ci_95": ci, "p_value": p}


def run_regressions(df: pd.DataFrame) -> dict:
    d = df.dropna(subset=["founder_share_pre", "n_diffuse_owners_pre", "survived_binary"]).copy()
    if len(d) < 10:
        return {"logistic": {"error": "insufficient_n", "n": len(d)}, "ordinal": {"error": "insufficient_n", "n": len(d)}}
    d["log_stars"] = np.log1p(d["stars"])
    d["log_forks"] = np.log1p(d["forks"])
    d["contributor_count_z"] = (d["contributor_count"] - d["contributor_count"].mean()) / (d["contributor_count"].std() or 1)
    lang_dummies = pd.get_dummies(d["language"], prefix="lang", drop_first=True)
    lic_dummies = pd.get_dummies(d["license"], prefix="lic", drop_first=True)
    predictors = ["founder_share_pre", "n_diffuse_owners_pre", "log_stars", "log_forks", "contributor_count_z"]
    X = pd.concat([d[predictors], lang_dummies, lic_dummies], axis=1).astype(float)
    Xz = X.copy()
    for c in predictors:
        s = Xz[c].std()
        Xz[c] = (Xz[c] - Xz[c].mean()) / s if s else 0.0
    Xc = sm.add_constant(Xz, has_constant="add")
    y = d["survived_binary"].astype(float)

    logit_out: dict = {}
    try:
        model = sm.Logit(y, Xc.astype(float))
        res = model.fit(disp=0, maxiter=200)
        pvals = res.pvalues.drop("const", errors="ignore")
        rej, p_bh, _, _ = multipletests(pvals.values, method="fdr_bh")
        logit_out = {
            "coeffs": {k: float(v) for k, v in res.params.items()},
            "se": {k: float(v) for k, v in res.bse.items()},
            "p_raw": {k: float(v) for k, v in res.pvalues.items()},
            "p_bh": dict(zip(pvals.index, [float(p) for p in p_bh])),
            "std_effect_founder_share_pre": float(res.params.get("founder_share_pre", np.nan)),
            "std_effect_n_diffuse_owners_pre": float(res.params.get("n_diffuse_owners_pre", np.nan)),
            "n": int(len(d)),
            "converged": bool(res.mle_retvals.get("converged", False)),
        }
    except Exception as e:  # noqa: BLE001
        logit_out = {"error": str(e), "n": int(len(d))}

    ordinal_out: dict = {}
    if OrderedModel is not None and d["survival_label"].nunique() >= 3:
        try:
            order = ["dead", "dormant", "maintained", "thriving"]
            cats = pd.Categorical(d["survival_label"], categories=[c for c in order if c in d["survival_label"].unique()], ordered=True)
            om = OrderedModel(cats.codes, Xz.astype(float), distr="logit")
            ores = om.fit(method="bfgs", disp=0, maxiter=200)
            ordinal_out = {
                "coeffs": {k: float(v) for k, v in ores.params.items() if k in Xz.columns},
                "p_raw": {k: float(v) for k, v in ores.pvalues.items() if k in Xz.columns},
                "n": int(len(d)),
            }
        except Exception as e:  # noqa: BLE001
            ordinal_out = {"error": str(e), "n": int(len(d))}
    else:
        ordinal_out = {"error": "insufficient_label_levels_or_no_ordered_model", "n": int(len(d))}

    # snapshot-vs-diffusion standardized effect sizes (Cohen's d equivalents via logistic beta -> d approx)
    def beta_to_d(beta):
        return float(beta * (np.sqrt(3) / np.pi)) if beta == beta else None

    snap_vs_diff = {}
    if "coeffs" in logit_out:
        for k in predictors:
            b = logit_out["coeffs"].get(k)
            snap_vs_diff[k] = {"beta": b, "cohens_d_equiv": beta_to_d(b) if b is not None else None}

    return {"logistic": logit_out, "ordinal": ordinal_out, "snapshot_vs_diffusion_effect_sizes": snap_vs_diff}


def placebo_check(df: pd.DataFrame, true_regression: dict) -> dict:
    d = df.dropna(subset=["placebo_founder_shares", "placebo_n_diffuse_owners"])
    d = d[d["placebo_founder_shares"].map(len) > 0]
    if d.empty:
        return {"error": "no_placebo_draws_available"}
    true_beta = true_regression.get("logistic", {}).get("std_effect_founder_share_pre")
    if true_beta is None or true_beta != true_beta:
        return {"error": "true_effect_unavailable"}
    n_draws = min(d["placebo_founder_shares"].map(len).min(), N_PLACEBO_DRAWS)
    placebo_effects = []
    rng = np.random.default_rng(RNG_SEED)
    for draw_i in range(int(n_draws)):
        pdf = d.copy()
        pdf["founder_share_pre"] = pdf["placebo_founder_shares"].map(lambda lst, i=draw_i: lst[i] if i < len(lst) else np.nan)
        pdf["n_diffuse_owners_pre"] = pdf["placebo_n_diffuse_owners"].map(lambda lst, i=draw_i: lst[i] if i < len(lst) else np.nan)
        preg = run_regressions(pdf)
        b = preg.get("logistic", {}).get("std_effect_founder_share_pre")
        if b is not None and b == b:
            placebo_effects.append(float(b))
    if not placebo_effects:
        return {"error": "placebo_regressions_all_failed"}
    placebo_effects = np.array(placebo_effects)
    frac_ge = float((np.abs(placebo_effects) >= abs(true_beta)).mean())
    return {
        "true_effect": float(true_beta),
        "placebo_null_distribution_summary": {
            "mean": float(placebo_effects.mean()),
            "std": float(placebo_effects.std()),
            "p5": float(np.percentile(placebo_effects, 5)),
            "p95": float(np.percentile(placebo_effects, 95)),
            "n_draws": int(len(placebo_effects)),
        },
        "fraction_placebo_ge_true": frac_ge,
    }


# ---------------------------------------------------------------------------
# Baseline method: Avelino et al.'s original snapshot-only predictors (no
# diffusion trajectory) -- used as predict_baseline vs. predict_ourmethod
# ---------------------------------------------------------------------------


def baseline_snapshot_predict(d: pd.DataFrame) -> pd.Series:
    """Baseline = logistic regression on snapshot covariates only (developers,
    commits, files at TFDD + size), no pre-departure diffusion trajectory."""
    dd = d.dropna(subset=["survived_binary"]).copy()
    if len(dd) < 10:
        return pd.Series(index=d.index, dtype=float)
    dd["log_stars"] = np.log1p(dd["stars"])
    dd["log_forks"] = np.log1p(dd["forks"])
    X = dd[["developers_at_tfdd", "commits_at_tfdd", "files_at_tfdd", "log_stars", "log_forks"]].astype(float)
    Xc = sm.add_constant(X, has_constant="add")
    y = dd["survived_binary"].astype(float)
    try:
        res = sm.Logit(y, Xc).fit(disp=0, maxiter=200)
        pred = res.predict(Xc)
        return pred.reindex(d.index)
    except Exception:  # noqa: BLE001
        return pd.Series(index=d.index, dtype=float)


def ourmethod_predict(d: pd.DataFrame) -> pd.Series:
    dd = d.dropna(subset=["survived_binary", "founder_share_pre", "n_diffuse_owners_pre"]).copy()
    if len(dd) < 10:
        return pd.Series(index=d.index, dtype=float)
    dd["log_stars"] = np.log1p(dd["stars"])
    dd["log_forks"] = np.log1p(dd["forks"])
    X = dd[["founder_share_pre", "n_diffuse_owners_pre", "developers_at_tfdd", "commits_at_tfdd", "files_at_tfdd", "log_stars", "log_forks"]].astype(float)
    Xc = sm.add_constant(X, has_constant="add")
    y = dd["survived_binary"].astype(float)
    try:
        res = sm.Logit(y, Xc).fit(disp=0, maxiter=200)
        pred = res.predict(Xc)
        return pred.reindex(d.index)
    except Exception:  # noqa: BLE001
        return pd.Series(index=d.index, dtype=float)


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------


def load_raw_repos(files: list[Path], max_repos: Optional[int]) -> list[dict]:
    repos: list[dict] = []
    for f in files:
        try:
            obj = json.loads(f.read_text())
        except Exception as e:  # noqa: BLE001
            logger.warning(f"failed to parse {f}: {e}")
            continue
        if isinstance(obj, dict):
            if "datasets" in obj:
                for ds in obj["datasets"]:
                    for ex in ds.get("examples", ds.get("repos", [])):
                        if isinstance(ex, dict) and "input" in ex and isinstance(ex["input"], str):
                            try:
                                repos.append(json.loads(ex["input"]))
                                continue
                            except (json.JSONDecodeError, TypeError):
                                pass
                        repos.append(ex)
            elif "repos" in obj:
                repos.extend(obj["repos"])
            elif "examples" in obj:
                repos.extend(obj["examples"])
            else:
                repos.append(obj)
        elif isinstance(obj, list):
            repos.extend(obj)
        del obj
        gc.collect()
        if max_repos and len(repos) >= max_repos:
            repos = repos[:max_repos]
            break
    return repos


def _repo_to_example(r: RepoResult) -> dict:
    inp = (
        f"Repository {r.repo_id} ({r.language}, {r.stars:.0f} stars) reached its first "
        f"founder-only Truck-Factor-Detachment-Departure (TFDD) on {r.tfdd_date}. "
        f"Pre-departure (6-12mo before TFDD): founder commit-share={r.founder_share_pre}, "
        f"distinct non-founder DOA file-owners={r.n_diffuse_owners_pre}. "
        f"At-TFDD snapshot: developers={r.developers_at_tfdd}, commits={r.commits_at_tfdd}, files={r.files_at_tfdd}."
    )
    out = f"survival_label={r.survival_label}; survived_binary={r.survived_binary}"
    return {
        "input": inp,
        "output": out,
        "metadata_repo_id": r.repo_id,
        "metadata_language": r.language,
        "metadata_license": r.license,
        "metadata_stars": r.stars,
        "metadata_forks": r.forks,
        "metadata_alias_collapse_rate": r.alias_collapse_rate,
        "metadata_founder_share_pre": r.founder_share_pre,
        "metadata_n_diffuse_owners_pre": r.n_diffuse_owners_pre,
        "metadata_diffusion_score": r.diffusion_score,
        "metadata_developers_at_tfdd": r.developers_at_tfdd,
        "metadata_commits_at_tfdd": r.commits_at_tfdd,
        "metadata_files_at_tfdd": r.files_at_tfdd,
        "metadata_contributor_count": r.contributor_count,
        "metadata_survival_label": r.survival_label,
        "metadata_survived_binary": r.survived_binary,
    }


@logger.catch(reraise=True)
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-path", default=None, help="Override path to dataset dependency output")
    ap.add_argument("--max-repos", type=int, default=None)
    ap.add_argument("--synthetic", action="store_true", help="Force synthetic smoke-test data")
    ap.add_argument("--synthetic-n", type=int, default=40)
    ap.add_argument("--output", default=str(WORKSPACE / "method_out.json"))
    args = ap.parse_args()

    t_start = time.time()
    doa_approximation_used = False

    if args.synthetic:
        logger.info(f"Using synthetic self-test data: {args.synthetic_n} repos")
        raw_repos = make_synthetic_repos(args.synthetic_n)
        dataset_name = "synthetic_smoke_test"
    else:
        files = _find_dataset_files(args.data_path)
        logger.info(f"Found {len(files)} dataset file(s): {[str(f) for f in files]}")
        if not files:
            logger.warning("No real dataset found; falling back to synthetic smoke-test data.")
            raw_repos = make_synthetic_repos(args.synthetic_n)
            dataset_name = "synthetic_smoke_test_fallback"
        else:
            raw_repos = load_raw_repos(files, args.max_repos)
            dataset_name = "github_founder_departure_corpus"
            if raw_repos and not any((r.get("commits") or r.get("commit_log", [{}]))[0:1] and isinstance((r.get("commits") or r.get("commit_log"))[0], dict) and "files" in (r.get("commits") or r.get("commit_log"))[0] or "files_touched" in (r.get("commits") or r.get("commit_log"))[0] for r in raw_repos[:1] if (r.get("commits") or r.get("commit_log"))):
                doa_approximation_used = True

    if args.max_repos:
        raw_repos = raw_repos[: args.max_repos]
    logger.info(f"Loaded {len(raw_repos)} raw repo records")

    # NOTE: this environment has very high per-process import latency (cold
    # disk cache: pandas/sklearn/statsmodels imports alone take ~90s wall
    # time), which makes ProcessPoolExecutor with spawn repay that cost on
    # EVERY worker and lose badly to sequential execution for corpora of the
    # size this pipeline targets (150-250 repos, cheap per-repo compute).
    # Process sequentially in this one warm interpreter instead.
    results: list[RepoResult] = []
    n_workers = 1
    for i, rr in enumerate(raw_repos):
        results.append(process_repo(rr, RNG_SEED + i))
        if (i + 1) % 25 == 0:
            logger.info(f"processed {i + 1}/{len(raw_repos)} repos")

    n_repos_total = len(results)
    founder_events = [r for r in results if r.has_founder_tfdd]
    logger.info(f"n_repos_total={n_repos_total}, n_founder_tfdd_events={len(founder_events)}")

    error_counts = defaultdict(int)
    for r in results:
        if r.error:
            error_counts[r.error] += 1
    logger.info(f"error breakdown: {dict(error_counts)}")

    alias_rates = [r.alias_collapse_rate for r in results if r.alias_collapse_rate is not None]
    alias_qa = {
        "median_collapse_rate": float(np.median(alias_rates)) if alias_rates else None,
        "n_repos_over_40pct_collapse": int(sum(1 for a in alias_rates if a > 0.4)),
    }

    extended_sample_used = False
    if len(founder_events) < 40 and not args.synthetic:
        logger.warning(f"Only {len(founder_events)} founder-only TFDD events (<40); headline restricted to strict TF=1, "
                        f"per fallback_plan this is reported as-is (extended TF<=2 sample not separately mined in this pass).")
        extended_sample_used = False  # extension would require re-mining TF<=2 events; documented as limitation instead

    df = pd.DataFrame([r.__dict__ for r in founder_events]) if founder_events else pd.DataFrame(
        columns=["repo_id", "language", "license", "stars", "forks", "founder_share_pre", "n_diffuse_owners_pre",
                 "developers_at_tfdd", "commits_at_tfdd", "files_at_tfdd", "contributor_count", "survived_binary", "survival_label"])

    rng = np.random.default_rng(RNG_SEED)
    matched_pairs = matched_pairs_analysis(df, rng) if not df.empty else {"n_pairs": 0, "error": "no_founder_tfdd_events"}
    regression = run_regressions(df) if not df.empty else {"logistic": {"error": "no_founder_tfdd_events"}, "ordinal": {"error": "no_founder_tfdd_events"}}
    placebo = placebo_check(df, regression) if not df.empty else {"error": "no_founder_tfdd_events"}

    if not df.empty:
        df["predict_baseline_prob"] = baseline_snapshot_predict(df)
        df["predict_ourmethod_prob"] = ourmethod_predict(df)

    examples = [_repo_to_example(r) for r in founder_events]
    if not examples:
        examples = [
            {
                "input": "No founder-only TFDD events were detected in this run.",
                "output": "n_founder_tfdd_events=0",
                "metadata_note": "pipeline ran end-to-end but found zero qualifying events; see error_breakdown in metadata",
            }
        ]
    for ex, r in zip(examples, founder_events):
        idx = df.index[df["repo_id"] == r.repo_id]
        if len(idx):
            i0 = idx[0]
            ex["predict_baseline"] = json.dumps({"survived_prob": None if pd.isna(df.loc[i0, "predict_baseline_prob"]) else float(df.loc[i0, "predict_baseline_prob"])})
            ex["predict_ourmethod"] = json.dumps({"survived_prob": None if pd.isna(df.loc[i0, "predict_ourmethod_prob"]) else float(df.loc[i0, "predict_ourmethod_prob"])})

    output = {
        "metadata": {
            "method_name": "founder_departure_authority_diffusion_vs_survival",
            "description": "Reimplements Avelino et al. (ESEM 2019) DOA/TF/TFDD pipeline; tests whether pre-departure authority diffusion predicts 18mo post-TFDD survival beyond snapshot covariates.",
            "n_repos_total": n_repos_total,
            "n_founder_tfdd_events": len(founder_events),
            "error_breakdown": dict(error_counts),
            "alias_qa": alias_qa,
            "doa_approximation_used": doa_approximation_used,
            "extended_sample_used_TFle2": extended_sample_used,
            "matched_pairs": matched_pairs,
            "regression": regression,
            "placebo_check": placebo,
            "runtime_seconds": time.time() - t_start,
            "dataset_source": dataset_name,
            "num_cpus_used": n_workers,
        },
        "datasets": [{"dataset": dataset_name, "examples": examples}],
    }

    out_path = Path(args.output)
    out_path.write_text(json.dumps(output, indent=2, default=str))
    logger.info(f"Wrote {out_path} ({out_path.stat().st_size/1e6:.2f} MB) in {time.time()-t_start:.1f}s")


if __name__ == "__main__":
    main()
