#!/usr/bin/env python3
"""Founder-only Truck-Factor Development Departure (TFDD) survival study.

Re-implements the DOA / Truck-Factor / TFDD / Active-Inactive pipeline of
Avelino et al. (ESEM 2019, "The Truck Factor of Popular GitHub Applications")
from real GitHub commit histories, detects founder-only TFDD events, and adds
a NEW pre-departure "authority diffusion" measurement (founder commit-share
and count of independent non-founder DOA file-owners in the 6-12 months
before TFDD) that the published Avelino et al. pipeline does not compute.
Tests whether this pre-departure trajectory predicts 18-month post-TFDD
survival better than size/popularity covariates alone, via a BH-corrected
logistic regression and a matched-pairs bootstrap risk-ratio, with a
within-repo placebo (random-window) falsification check.

Method (our contribution): pre-departure authority-diffusion trajectory
  (founder_share, n_diffused_owners) computed in the window 12-6 months
  before a founder-only TFDD event.
Baseline (Avelino et al.'s own approach): snapshot size/popularity
  covariates AT the TFDD event (devs, commits, files, stars, forks) with no
  temporal trajectory information.
"""

from __future__ import annotations

import gc
import json
import math
import random
import subprocess
import sys
import time
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd
import requests
import statsmodels.api as sm
from loguru import logger
from scipy import stats

WORKSPACE = Path(__file__).resolve().parent
REPOS_DIR = WORKSPACE / "repos_scratch"
LOGS_DIR = WORKSPACE / "logs"
RESULTS_DIR = WORKSPACE / "results"
for d in (REPOS_DIR, LOGS_DIR, RESULTS_DIR):
    d.mkdir(parents=True, exist_ok=True)

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add(LOGS_DIR / "run.log", rotation="30 MB", level="DEBUG")

RNG_SEED = 20260821
random.seed(RNG_SEED)
np.random.seed(RNG_SEED)

import os

GITHUB_API = "https://api.github.com"
GITHUB_TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")  # read-only search/clone use only
HEADERS = {"Accept": "application/vnd.github+json"}
if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"

# ---------------------------------------------------------------------------
# Config (scaled down from the plan's 240-repo target to fit unauthenticated
# GitHub API rate limits: 10 search req/hr, 60 core req/hr -- see fallback_plan
# item 1). We avoid all per-repo GET /repos calls entirely by reading every
# metadata field we need straight off the /search/repositories response.
# ---------------------------------------------------------------------------
LANGUAGES = ["Python", "JavaScript", "Go", "Java", "Ruby", "C++"]
STAR_STRATA = ["stars:50..500", "stars:500..5000", "stars:5000..100000"]  # 3 popularity strata per language
PER_QUERY = 15  # repos requested per (language, stratum) search call -> 6*3*15 = 270 candidates (authenticated GH_TOKEN in use, higher rate limit)
MAX_REPO_SIZE_KB = 60_000  # exclude repos > ~60MB reported size (fallback_plan item 2, tightened after
                            # dapr/dapr was observed to clone to 200MB+ despite passing a looser 300MB cap --
                            # GitHub's `size` field underestimates actual .git size for some monorepos)
MAX_CLONE_BYTES = 150_000_000  # hard cap enforced AFTER cloning starts, in case `size` metadata is stale
MAX_COMMITS = 8000  # skip repos whose full history exceeds this -- DOA snapshotting is O(n_snapshots * n_commits)
                     # and re-scans commits per (dev,file) pair, so very large histories are not worth the wall-clock
MIN_AGE_DAYS = 3 * 365  # need TFDD + 18mo post-window, per our stricter requirement
CLONE_TIMEOUT_S = 180
GIT_LOG_TIMEOUT_S = 180
SILENCE_THRESHOLD_DAYS = 365  # Avelino et al.'s TFDD silence threshold
TF_COVERAGE_THRESHOLD = 0.5  # Avelino et al.'s truck-factor coverage cutoff
POST_TFDD_WINDOW_DAYS = 548  # 18 months
PRE_WINDOW_FAR_DAYS = 365  # 12 months before TFDD
PRE_WINDOW_NEAR_DAYS = 180  # 6 months before TFDD
N_BOOT = 5000


def gh_get(url: str, params: Optional[dict] = None, retries: int = 3) -> Optional[dict]:
    for attempt in range(retries):
        try:
            resp = requests.get(url, headers=HEADERS, params=params, timeout=30)
        except requests.RequestException as e:
            logger.warning(f"GET {url} failed (attempt {attempt+1}): {e}")
            time.sleep(3)
            continue
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code in (403, 429):
            remaining = resp.headers.get("X-RateLimit-Remaining")
            reset = resp.headers.get("X-RateLimit-Reset")
            wait = 5
            if reset:
                wait = max(5, min(90, int(reset) - int(time.time()) + 2))
            logger.warning(
                f"GET {url} rate-limited (remaining={remaining}), sleeping {wait}s"
            )
            time.sleep(wait)
            continue
        logger.warning(f"GET {url} returned {resp.status_code}: {resp.text[:200]}")
        return None
    return None


# ---------------------------------------------------------------------------
# STAGE 0: repo sampling via GitHub search API (metadata-only, no per-repo GET)
# ---------------------------------------------------------------------------
def stage0_sample_repos() -> list[dict]:
    candidates: dict[str, dict] = {}
    for lang in LANGUAGES:
        for stratum in STAR_STRATA:
            q = f"language:{lang} {stratum} archived:false"
            logger.info(f"[stage0] search: {q}")
            data = gh_get(
                f"{GITHUB_API}/search/repositories",
                params={"q": q, "sort": "updated", "order": "desc", "per_page": PER_QUERY},
            )
            time.sleep(2.5 if GITHUB_TOKEN else 6)  # authenticated: 30 search req/min; unauthenticated: 10/min
            if data is None or "items" not in data:
                logger.warning(f"[stage0] no results for query {q!r}")
                continue
            for item in data["items"]:
                candidates[item["full_name"]] = item
    logger.info(f"[stage0] {len(candidates)} unique candidate repos across {len(LANGUAGES)} languages")
    return list(candidates.values())


# ---------------------------------------------------------------------------
# STAGE 1: filter mining artifacts using ONLY the metadata already in hand
# (Avelino et al.'s exclusion criteria: forks, archives, insufficient history)
# ---------------------------------------------------------------------------
def stage1_filter(candidates: list[dict]) -> list[dict]:
    now = datetime.now(timezone.utc)
    filtered = []
    reasons = Counter()
    for repo in candidates:
        if repo.get("fork"):
            reasons["is_fork"] += 1
            continue
        if repo.get("archived"):
            reasons["archived"] += 1
            continue
        if repo.get("disabled"):
            reasons["disabled"] += 1
            continue
        created = datetime.fromisoformat(repo["created_at"].replace("Z", "+00:00"))
        age_days = (now - created).days
        if age_days < MIN_AGE_DAYS:
            reasons["too_young"] += 1
            continue
        if repo.get("size", 0) > MAX_REPO_SIZE_KB:
            reasons["too_large"] += 1
            continue
        pushed = datetime.fromisoformat(repo["pushed_at"].replace("Z", "+00:00"))
        if (now - pushed).days > 4 * 365:
            reasons["long_dead_before_study_window"] += 1
            continue
        filtered.append(repo)
    logger.info(f"[stage1] {len(filtered)}/{len(candidates)} repos survive filtering; excluded={dict(reasons)}")
    random.shuffle(filtered)
    return filtered


# ---------------------------------------------------------------------------
# STAGE 2: clone bare + walk commit history via `git log --numstat`
# (fallback_plan item 3: raw git log parsing, much faster than PyDriller for
# repos with tens of thousands of commits, same information content)
# ---------------------------------------------------------------------------
RECORD_SEP = "\x1e"
FIELD_SEP = "\x1f"


def _dir_size_bytes(path: Path) -> int:
    total = 0
    for p in path.rglob("*"):
        if p.is_file():
            try:
                total += p.stat().st_size
            except OSError:
                pass
    return total


def clone_repo(clone_url: str, dest: Path) -> bool:
    if dest.exists():
        subprocess.run(["rm", "-rf", str(dest)], check=False)
    try:
        proc = subprocess.run(
            ["git", "clone", "--bare", "-q", clone_url, str(dest)],
            timeout=CLONE_TIMEOUT_S,
            capture_output=True,
            text=True,
        )
    except subprocess.TimeoutExpired:
        logger.warning(f"[stage2] clone timeout: {clone_url}")
        subprocess.run(["rm", "-rf", str(dest)], check=False)
        return False
    if proc.returncode != 0:
        logger.warning(f"[stage2] clone failed: {clone_url}: {proc.stderr[:300]}")
        return False
    size = _dir_size_bytes(dest)
    if size > MAX_CLONE_BYTES:
        logger.warning(f"[stage2] clone of {clone_url} is {size/1e6:.0f}MB > cap, skipping")
        subprocess.run(["rm", "-rf", str(dest)], check=False)
        return False
    return True


def walk_commits(bare_dir: Path) -> list[dict]:
    """Parse `git log --numstat` into a list of commit dicts with per-file diffs."""
    fmt = f"{RECORD_SEP}%H{FIELD_SEP}%ae{FIELD_SEP}%cI"
    try:
        proc = subprocess.run(
            ["git", "-C", str(bare_dir), "log", "--no-merges", "--numstat", f"--format={fmt}"],
            capture_output=True,
            text=True,
            timeout=GIT_LOG_TIMEOUT_S,
        )
    except subprocess.TimeoutExpired:
        logger.warning(f"[stage2] git log timeout in {bare_dir}")
        return []
    if proc.returncode != 0:
        logger.warning(f"[stage2] git log failed in {bare_dir}: {proc.stderr[:300]}")
        return []
    commits = []
    cur = None
    for line in proc.stdout.split(RECORD_SEP):
        line = line.strip("\n")
        if not line:
            continue
        parts = line.split("\n", 1)
        header = parts[0]
        h, ae, ci = header.split(FIELD_SEP)
        try:
            dt = datetime.fromisoformat(ci)
        except ValueError:
            continue
        cur = {"hash": h, "author_email": ae.lower().strip(), "date": dt, "files": []}
        if len(parts) > 1:
            for fl in parts[1].strip("\n").split("\n"):
                fl = fl.strip()
                if not fl:
                    continue
                bits = fl.split("\t")
                if len(bits) != 3:
                    continue
                added, deleted, path = bits
                added_n = 0 if added == "-" else int(added)
                deleted_n = 0 if deleted == "-" else int(deleted)
                cur["files"].append((path, added_n, deleted_n))
        commits.append(cur)
    commits.sort(key=lambda c: c["date"])
    return commits


# ---------------------------------------------------------------------------
# STAGE 3: DOA computation (Fritz et al. 2010 formula, as used by
# Avelino et al. ICPC 2016 / ESEM 2019)
#   DOA(dev, file, t) = 3.293 + 1.098*FA - 0.164*sqrt(AC) + 0.230*ln(1+DL)
# ---------------------------------------------------------------------------
def doa_snapshot(commits: list[dict], cutoff: datetime) -> dict[tuple[str, str], float]:
    """Returns {(dev, path): DOA} using only commits with date <= cutoff."""
    file_dev_stats: dict[str, dict[str, dict]] = defaultdict(dict)
    file_first_author: dict[str, str] = {}
    for c in commits:
        if c["date"] > cutoff:
            break  # commits sorted ascending
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
    """Argmax-DOA owner per file (the dev with the highest DOA score for that file)."""
    owner: dict[str, tuple[str, float]] = {}
    for (dev, path), score in doa.items():
        if path not in owner or score > owner[path][1]:
            owner[path] = (dev, score)
    return owner


def truck_factor_set(doa: dict[tuple[str, str], float]) -> list[str]:
    """Greedy min set of devs whose combined owned-files coverage >= 50% (Avelino et al.)."""
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


# ---------------------------------------------------------------------------
# STAGE 4: TFDD detection (founder-only, TF-set size 1, all silent >= 1yr)
# ---------------------------------------------------------------------------
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
    tf_set_size_at_relaxed: int = 1  # strict=1 always here; relaxed variant computed separately
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


def detect_founder_tfdd(commits: list[dict], snapshot_every_days: int = 90) -> Optional[tuple[datetime, str]]:
    """Scan chronological snapshots; return the first date+founder at which the
    truck-factor set is a single developer who has then been silent >= 1yr."""
    if len(commits) < 20:
        return None
    start = commits[0]["date"]
    end = commits[-1]["date"]
    last_active: dict[str, datetime] = {}
    for c in commits:
        e = c["author_email"]
        if e not in last_active or c["date"] > last_active[e]:
            last_active[e] = c["date"]

    cursor = start + timedelta(days=180)  # need some history before first snapshot
    while cursor <= end:
        doa = doa_snapshot(commits, cursor)
        tf_set = truck_factor_set(doa)
        if len(tf_set) == 1:
            founder = tf_set[0]
            silence = (cursor - last_active.get(founder, start)).days
            if silence >= SILENCE_THRESHOLD_DAYS:
                # TFDD date = the moment the founder crossed the silence threshold
                tfdd_date = last_active[founder] + timedelta(days=SILENCE_THRESHOLD_DAYS)
                return min(tfdd_date, cursor), founder
        cursor += timedelta(days=snapshot_every_days)
    return None


def detect_relaxed_tfdd(commits: list[dict], snapshot_every_days: int = 90) -> Optional[tuple[datetime, list[str]]]:
    """Relaxed variant per fallback_plan item 5: TF-set size <= 2, all silent >= 1yr."""
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


# ---------------------------------------------------------------------------
# STAGE 5: pre-departure diffusion metrics (THE NEW MEASUREMENT) + STAGE 7 placebo
# ---------------------------------------------------------------------------
def window_metrics(commits: list[dict], window_start: datetime, window_end: datetime, founder: str) -> tuple[float, int]:
    window_commits = [c for c in commits if window_start <= c["date"] < window_end]
    if not window_commits:
        return float("nan"), 0
    founder_commits = sum(1 for c in window_commits if c["author_email"] == founder)
    founder_share = founder_commits / len(window_commits)
    doa_end = doa_snapshot(commits, window_end)
    owner = file_owners(doa_end)
    non_founder_owners = {dev for dev, (o, _s) in ((p, o) for p, o in owner.items())} if False else None
    non_founder_owners = {o[0] for o in owner.values() if o[0] != founder}
    return founder_share, len(non_founder_owners)


def sample_placebo_window(commits: list[dict], exclude_start: datetime, exclude_end: datetime) -> Optional[tuple[datetime, datetime]]:
    """Pick a random 6-month window at least 1yr away from the TFDD window, for the falsification check."""
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


# ---------------------------------------------------------------------------
# STAGE 6: survival label (Avelino et al. Active/Inactive model, 18mo window)
# ---------------------------------------------------------------------------
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
# STAGE 8: matched pairs + regression
# ---------------------------------------------------------------------------
def log_decile_bucket(x: float, edges: np.ndarray) -> int:
    return int(np.searchsorted(edges, x))


def build_matched_pairs(df: pd.DataFrame, low_thresh: float = 0.50, hi_thresh: float = 0.80, n_diffused_min: int = 2):
    lo = df[(df.founder_share < low_thresh) & (df.n_diffused_owners >= n_diffused_min)].copy()
    hi = df[df.founder_share >= hi_thresh].copy()
    pairs = []
    used_hi = set()
    for _, lrow in lo.iterrows():
        best_idx, best_dist = None, float("inf")
        for hidx, hrow in hi.iterrows():
            if hidx in used_hi:
                continue
            if hrow.language != lrow.language:
                continue
            dist = (
                (math.log1p(hrow.stars) - math.log1p(lrow.stars)) ** 2
                + (math.log1p(hrow.forks) - math.log1p(lrow.forks)) ** 2
                + (math.log1p(hrow.devs_at_tfdd) - math.log1p(lrow.devs_at_tfdd)) ** 2
            )
            if dist < best_dist:
                best_dist, best_idx = dist, hidx
        if best_idx is not None and best_dist < 4.0:  # cap on match distance (~2 log-units per dim)
            used_hi.add(best_idx)
            pairs.append((lrow, hi.loc[best_idx]))
    return pairs


def bootstrap_survival_rate_ratio(pairs: list[tuple[pd.Series, pd.Series]], n_boot: int = N_BOOT):
    if not pairs:
        return float("nan"), (float("nan"), float("nan"))
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
        return float("nan"), (float("nan"), float("nan"))
    ratios = np.array(ratios)
    point = (lo_surv.mean() + 1e-6) / (hi_surv.mean() + 1e-6)
    ci = (float(np.percentile(ratios, 2.5)), float(np.percentile(ratios, 97.5)))
    return float(point), ci


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


# ---------------------------------------------------------------------------
# main pipeline
# ---------------------------------------------------------------------------
def process_repo(repo_meta: dict) -> tuple[Optional[TFDDEvent], Optional[TFDDEvent], dict]:
    """Returns (strict_event_or_None, relaxed_event_or_None, diag_dict)."""
    full_name = repo_meta["full_name"]
    dest = REPOS_DIR / full_name.replace("/", "__")
    diag = {"repo": full_name, "stars": repo_meta.get("stargazers_count", 0), "language": repo_meta.get("language")}
    ok = clone_repo(repo_meta["clone_url"], dest)
    if not ok:
        diag["status"] = "clone_failed"
        return None, None, diag
    try:
        commits = walk_commits(dest)
        if len(commits) < 20:
            diag["status"] = "too_few_commits"
            return None, None, diag
        if len(commits) > MAX_COMMITS:
            diag["status"] = "too_many_commits"
            diag["n_commits"] = len(commits)
            return None, None, diag
        n_devs_total = len({c["author_email"] for c in commits})
        if n_devs_total < 2:
            diag["status"] = "single_dev_never_had_team"
            return None, None, diag
        last_commit_date = commits[-1]["date"]

        strict = detect_founder_tfdd(commits)
        relaxed = detect_relaxed_tfdd(commits)

        license_key = (repo_meta.get("license") or {}).get("key", "none") if repo_meta.get("license") else "none"
        created_at = datetime.fromisoformat(repo_meta["created_at"].replace("Z", "+00:00"))

        def make_event(tfdd_date: datetime, founder: str) -> Optional[TFDDEvent]:
            window_start = tfdd_date - timedelta(days=PRE_WINDOW_FAR_DAYS)
            window_end = tfdd_date - timedelta(days=PRE_WINDOW_NEAR_DAYS)
            if window_start < commits[0]["date"]:
                return None  # insufficient pre-history for this event
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
                stars=repo_meta.get("stargazers_count", 0),
                forks=repo_meta.get("forks_count", 0),
                language=repo_meta.get("language") or "unknown",
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
            return ev

        strict_event = make_event(strict[0], strict[1]) if strict else None
        relaxed_event = None
        if relaxed:
            r_date, r_set = relaxed
            # treat the "founder" as the tf-set member with the most total commits (dominant author)
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
        return strict_event, relaxed_event, diag
    finally:
        subprocess.run(["rm", "-rf", str(dest)], check=False)
        gc.collect()


@logger.catch(reraise=True)
def main():
    t0 = time.time()
    TIME_BUDGET_S = 2.5 * 3600  # keep margin inside the available run envelope (aii-long-running-tasks pattern)

    logger.info("=== STAGE 0-1: sampling and filtering candidate repos ===")
    candidates = stage0_sample_repos()
    filtered = stage1_filter(candidates)

    logger.info("=== GRADUAL SCALING: mini test (5 repos) -> pipeline-shape test (15) -> scale up ===")
    scale_steps = [5, 15, 50, min(220, len(filtered))]
    strict_events: list[TFDDEvent] = []
    relaxed_events: list[TFDDEvent] = []
    diagnostics: list[dict] = []
    processed_names: set[str] = set()

    for step_i, target_n in enumerate(scale_steps):
        if time.time() - t0 > TIME_BUDGET_S:
            logger.warning(f"[scaling] time budget reached before step {step_i}, stopping scale-up")
            break
        remaining = [r for r in filtered if r["full_name"] not in processed_names]
        n_to_add = max(0, target_n - len(processed_names))
        batch = remaining[:n_to_add]
        logger.info(f"[scaling] step {step_i}: processing {len(batch)} more repos (target cumulative n={target_n})")
        for repo_meta in batch:
            if time.time() - t0 > TIME_BUDGET_S:
                logger.warning("[scaling] time budget reached mid-batch, stopping")
                break
            processed_names.add(repo_meta["full_name"])
            try:
                s_ev, r_ev, diag = process_repo(repo_meta)
            except Exception as e:
                logger.error(f"[process_repo] {repo_meta['full_name']} failed: {e}")
                diag = {"repo": repo_meta["full_name"], "status": f"exception:{e}"}
                s_ev, r_ev = None, None
            diagnostics.append(diag)
            if s_ev is not None:
                strict_events.append(s_ev)
            if r_ev is not None:
                relaxed_events.append(r_ev)
        logger.info(
            f"[scaling] after step {step_i}: {len(processed_names)} repos processed, "
            f"{len(strict_events)} strict founder-TFDD events, {len(relaxed_events)} relaxed events"
        )
        if step_i == 0 and len(strict_events) == 0 and len(relaxed_events) == 0:
            logger.warning(
                "[scaling] mini test found ZERO TFDD events of either kind -- "
                "continuing to pipeline-shape test but flagging for review"
            )

    logger.info(f"=== Finished repo processing: {len(processed_names)} repos, "
                f"{len(strict_events)} strict events, {len(relaxed_events)} relaxed events ===")

    diag_df = pd.DataFrame(diagnostics)
    diag_df.to_csv(RESULTS_DIR / "repo_processing_diagnostics.csv", index=False)

    # ---- unconditioned survival rates (cross-check vs Avelino et al.'s ~41%) ----
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

    strict_rate = rate_summary(strict_events)
    relaxed_rate = rate_summary(relaxed_events)
    logger.info(f"[stage6] strict founder-only TFDD survival: {strict_rate}")
    logger.info(f"[stage6] relaxed TF<=2 TFDD survival: {relaxed_rate}")

    # ---- build the primary analysis dataframe (strict events, uncensored, complete metrics) ----
    def events_to_df(events: list[TFDDEvent]) -> pd.DataFrame:
        rows = [asdict(e) for e in events if not e.censored]
        if not rows:
            return pd.DataFrame()
        df = pd.DataFrame(rows)
        for col in ["tfdd_date", "repo_created_at"]:
            df[col] = pd.to_datetime(df[col], utc=True)
        df["log_stars"] = np.log1p(df["stars"])
        df["log_forks"] = np.log1p(df["forks"])
        df["log_devs_at_tfdd"] = np.log1p(df["devs_at_tfdd"])
        df = df.dropna(subset=["founder_share", "n_diffused_owners", "log_stars", "log_forks", "devs_at_tfdd"])
        return df

    df = events_to_df(strict_events)
    df_relaxed = events_to_df(relaxed_events)

    results: dict = {
        "n_repos_sampled": len(candidates),
        "n_repos_filtered": len(filtered),
        "n_repos_processed": len(processed_names),
        "n_founder_tfdd_events_strict": len(strict_events),
        "n_founder_tfdd_events_relaxed": len(relaxed_events),
        "strict_unconditioned_survival": strict_rate,
        "relaxed_unconditioned_survival": relaxed_rate,
        "avelino_et_al_reference_survival_rate": 0.41,
        "n_analysis_rows_strict": int(len(df)),
        "n_analysis_rows_relaxed": int(len(df_relaxed)),
    }

    # ---- matched pairs + bootstrap risk ratio (strict events) ----
    matched_pairs_result = {"n_pairs": 0}
    if len(df) >= 6:
        pairs = build_matched_pairs(df)
        risk_ratio, ci95 = bootstrap_survival_rate_ratio(pairs, n_boot=N_BOOT)
        matched_pairs_result = {
            "n_pairs": len(pairs),
            "risk_ratio_low_vs_high_diffusion": risk_ratio,
            "risk_ratio_ci95": list(ci95),
            "note": "risk_ratio = P(survival | low diffusion) / P(survival | high diffusion); >1 means low authority-diffusion (concentrated founder) survives MORE, <1 means diffusion helps survival",
        }
    else:
        matched_pairs_result["note"] = "insufficient events for matched-pairs analysis (need >=6)"
    results["matched_pairs"] = matched_pairs_result

    # ---- regression: our method (diffusion trajectory) vs baseline (snapshot covariates only) ----
    def fit_logit(df_in: pd.DataFrame, cols: list[str], label: str) -> dict:
        if df_in.empty or df_in["survived"].nunique() < 2 or len(df_in) < len(cols) + 3:
            return {"status": "insufficient_data", "n": int(len(df_in)), "n_classes": int(df_in["survived"].nunique()) if not df_in.empty else 0}
        X = df_in[cols].astype(float)
        y = df_in["survived"].astype(int)
        X_const = sm.add_constant(X, has_constant="add")
        try:
            model = sm.Logit(y, X_const).fit(disp=0, maxiter=200)
        except Exception as e:
            logger.warning(f"[{label}] logit failed ({e}); falling back to parsimonious covariate set")
            parsimonious = [c for c in ["founder_share", "n_diffused_owners", "log_stars", "log_devs_at_tfdd"] if c in cols]
            if not parsimonious or parsimonious == cols:
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

    our_cols = ["founder_share", "n_diffused_owners", "log_stars", "log_forks", "log_devs_at_tfdd"]
    baseline_cols = ["log_stars", "log_forks", "log_devs_at_tfdd"]  # Avelino-et-al-style snapshot covariates only, no diffusion trajectory
    results["regression_our_method"] = fit_logit(df, our_cols, "our_method")
    results["regression_baseline_snapshot_only"] = fit_logit(df, baseline_cols, "baseline")

    # ---- placebo comparison (Stage 7 falsification check) ----
    placebo_df = df.dropna(subset=["placebo_founder_share", "placebo_n_diffused_owners"]).copy()
    placebo_cols = ["placebo_founder_share", "placebo_n_diffused_owners", "log_stars", "log_forks", "log_devs_at_tfdd"]
    results["placebo_check"] = {
        "n_events_with_placebo_window": int(len(placebo_df)),
        "regression_placebo_window": fit_logit(placebo_df, placebo_cols, "placebo") if len(placebo_df) >= 8 else {"status": "insufficient_data", "n": int(len(placebo_df))},
    }

    # ---- snapshot covariate effect sizes (Cohen's d), for comparability with Avelino et al.'s d=0.13-0.26 ----
    if not df.empty and df["survived"].nunique() == 2:
        surv_mask = df["survived"].astype(bool)
        results["snapshot_covariate_effect_sizes_d"] = {
            "devs_at_tfdd": cohens_d(df.loc[surv_mask, "devs_at_tfdd"].to_numpy(), df.loc[~surv_mask, "devs_at_tfdd"].to_numpy()),
            "commits_at_tfdd": cohens_d(df.loc[surv_mask, "commits_at_tfdd"].to_numpy(), df.loc[~surv_mask, "commits_at_tfdd"].to_numpy()),
            "files_at_tfdd": cohens_d(df.loc[surv_mask, "files_at_tfdd"].to_numpy(), df.loc[~surv_mask, "files_at_tfdd"].to_numpy()),
            "founder_share_pre_departure": cohens_d(df.loc[surv_mask, "founder_share"].to_numpy(), df.loc[~surv_mask, "founder_share"].to_numpy()),
            "n_diffused_owners_pre_departure": cohens_d(df.loc[surv_mask, "n_diffused_owners"].to_numpy(), df.loc[~surv_mask, "n_diffused_owners"].to_numpy()),
        }
        # simple two-group nonparametric tests as a minimally-complete fallback result (fallback_plan item 8)
        results["mann_whitney_diffusion_vs_survival"] = {
            "founder_share": {
                "u_stat": float(stats.mannwhitneyu(df.loc[surv_mask, "founder_share"], df.loc[~surv_mask, "founder_share"], alternative="two-sided").statistic),
                "p": float(stats.mannwhitneyu(df.loc[surv_mask, "founder_share"], df.loc[~surv_mask, "founder_share"], alternative="two-sided").pvalue),
            },
            "n_diffused_owners": {
                "u_stat": float(stats.mannwhitneyu(df.loc[surv_mask, "n_diffused_owners"], df.loc[~surv_mask, "n_diffused_owners"], alternative="two-sided").statistic),
                "p": float(stats.mannwhitneyu(df.loc[surv_mask, "n_diffused_owners"], df.loc[~surv_mask, "n_diffused_owners"], alternative="two-sided").pvalue),
            },
        }
    else:
        results["snapshot_covariate_effect_sizes_d"] = {"status": "insufficient_class_variation"}
        results["mann_whitney_diffusion_vs_survival"] = {"status": "insufficient_class_variation"}

    # ---- relaxed (TF<=2) sensitivity analysis, reported separately per fallback_plan item 5 ----
    if len(df_relaxed) >= 6 and df_relaxed["survived"].nunique() == 2:
        results["relaxed_sensitivity_regression"] = fit_logit(df_relaxed, our_cols, "relaxed_our_method")
    else:
        results["relaxed_sensitivity_regression"] = {"status": "insufficient_data", "n": int(len(df_relaxed))}

    results["runtime_seconds"] = time.time() - t0
    results["config"] = {
        "languages": LANGUAGES,
        "star_strata": STAR_STRATA,
        "min_age_days": MIN_AGE_DAYS,
        "silence_threshold_days": SILENCE_THRESHOLD_DAYS,
        "tf_coverage_threshold": TF_COVERAGE_THRESHOLD,
        "post_tfdd_window_days": POST_TFDD_WINDOW_DAYS,
        "pre_window_far_days": PRE_WINDOW_FAR_DAYS,
        "pre_window_near_days": PRE_WINDOW_NEAR_DAYS,
        "n_boot": N_BOOT,
        "rng_seed": RNG_SEED,
    }

    Path(RESULTS_DIR / "method_summary.json").write_text(json.dumps(results, indent=2, default=str))
    logger.info(f"[main] wrote {RESULTS_DIR / 'method_summary.json'}")

    # ---- exp_gen_sol_out.json-schema-compliant output (per-event rows, input/output as strings,
    #      predict_our_method / predict_baseline as required by aii-json exp_gen_sol_out schema) ----
    examples = []
    all_events_for_df = strict_events  # strict is the primary registered analysis; relaxed reported in metadata
    for e in all_events_for_df:
        input_text = (
            f"Repo {e.repo} ({e.language}): founder-only TFDD detected at {e.tfdd_date.isoformat()}. "
            f"Predict whether the project survives (attracts a non-founder truck-factor owner) over the "
            f"following 18 months, given pre-departure trajectory founder_share={e.founder_share:.3f}, "
            f"n_diffused_owners={e.n_diffused_owners}, and snapshot covariates stars={e.stars}, forks={e.forks}, "
            f"devs_at_tfdd={e.devs_at_tfdd}, commits_at_tfdd={e.commits_at_tfdd}, files_at_tfdd={e.files_at_tfdd}."
        )
        output_text = "survived" if e.survived else "did_not_survive"
        our_pred = "survived" if (e.founder_share < 0.65 and e.n_diffused_owners >= 2) else "did_not_survive"
        baseline_pred = "survived" if (e.stars >= 1000 and e.devs_at_tfdd >= 5) else "did_not_survive"
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
                "metadata_placebo_founder_share": e.placebo_founder_share,
                "metadata_placebo_n_diffused_owners": e.placebo_n_diffused_owners,
                "metadata_grade": e.grade,
                "metadata_censored": e.censored,
                "predict_our_method": our_pred,
                "predict_baseline": baseline_pred,
            }
        )

    if not examples:
        # schema requires >=1 example per dataset; emit a placeholder diagnostic row so the file is
        # still valid and downstream steps can see exactly what happened, rather than crashing.
        examples.append(
            {
                "input": "No founder-only TFDD events survived filtering within the sampled repos and time budget.",
                "output": "no_events",
                "metadata_note": "see repo_processing_diagnostics.csv and method_summary.json for full diagnosis",
                "predict_our_method": "no_events",
                "predict_baseline": "no_events",
            }
        )

    method_out = {
        "metadata": {
            "method_name": "founder_authority_diffusion_tfdd_survival",
            "description": (
                "Founder-only TFDD survival prediction from GitHub commit histories. "
                "our_method uses pre-departure authority-diffusion trajectory "
                "(founder_share, n_diffused_owners in the 12-6mo pre-TFDD window); "
                "baseline uses only snapshot size/popularity covariates at TFDD (Avelino et al. style)."
            ),
            "n_founder_tfdd_events_strict": len(strict_events),
            "n_founder_tfdd_events_relaxed": len(relaxed_events),
            "strict_unconditioned_survival_rate": strict_rate.get("survival_rate"),
            "avelino_et_al_reference_survival_rate": 0.41,
            "summary_results_file": "results/method_summary.json",
            "diagnostics_file": "results/repo_processing_diagnostics.csv",
        },
        "datasets": [{"dataset": "github_founder_tfdd_events", "examples": examples}],
    }
    Path(WORKSPACE / "method_out.json").write_text(json.dumps(method_out, indent=2, default=str))
    logger.info(f"[main] wrote {WORKSPACE / 'method_out.json'} with {len(examples)} example rows")
    logger.info(f"[main] DONE in {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
