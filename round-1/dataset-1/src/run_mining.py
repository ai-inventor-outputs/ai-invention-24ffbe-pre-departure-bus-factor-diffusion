#!/usr/bin/env python3
"""Orchestrate mining across all candidates: launch mine_repo.py as an isolated
subprocess per repo (own clone dir, hard wall-clock timeout via `timeout`), run
several in parallel bounded by CPU count, collect results, log discard reasons."""
import json
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/mining.log", rotation="30 MB", level="DEBUG")

CANDIDATES = Path("temp/candidates_filtered.json")
WORKDIR = Path("temp/repos")
RESULTS_DIR = Path("temp/repo_results")
PER_REPO_TIMEOUT_S = 180  # hard wall clock incl. clone+log+compute
NUM_WORKERS = 16  # network I/O bound (clone), not CPU bound -> oversubscribe the 4 CPUs


def process_one(cand: dict) -> dict:
    full_name = cand["full_name"]
    out_path = RESULTS_DIR / f"{full_name.replace('/', '__')}.json"
    if out_path.exists():
        return json.loads(out_path.read_text())
    cmd = ["timeout", str(PER_REPO_TIMEOUT_S), sys.executable, "mine_repo.py",
           full_name, cand["clone_url"], json.dumps(cand), str(out_path), str(WORKDIR)]
    try:
        subprocess.run(cmd, capture_output=True, text=True, timeout=PER_REPO_TIMEOUT_S + 30)
    except subprocess.TimeoutExpired:
        return {"full_name": full_name, "status": "discarded", "discard_reason": "orchestrator_timeout"}
    if out_path.exists():
        return json.loads(out_path.read_text())
    return {"full_name": full_name, "status": "discarded", "discard_reason": "worker_crashed_no_output"}


def main():
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    WORKDIR.mkdir(parents=True, exist_ok=True)
    candidates = json.loads(CANDIDATES.read_text())
    logger.info(f"Loaded {len(candidates)} candidates")

    # process oldest/most-history-plausible first isn't necessary; just cap pool size
    MAX_PROCESS = int(sys.argv[1]) if len(sys.argv) > 1 else len(candidates)
    candidates = candidates[:MAX_PROCESS]
    logger.info(f"Processing {len(candidates)} candidates with {NUM_WORKERS} workers, "
                f"{PER_REPO_TIMEOUT_S}s/repo timeout")

    results = []
    qualified = 0
    discard_counts = {}
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=NUM_WORKERS) as pool:
        futs = {pool.submit(process_one, c): c["full_name"] for c in candidates}
        for i, fut in enumerate(as_completed(futs), 1):
            name = futs[fut]
            try:
                res = fut.result()
            except Exception as e:  # noqa: BLE001
                res = {"full_name": name, "status": "discarded", "discard_reason": f"orchestrator_exception:{e}"}
            results.append(res)
            if res["status"] == "qualified":
                qualified += 1
                logger.info(f"[{i}/{len(candidates)}] QUALIFIED: {name} "
                            f"(total qualified={qualified}, elapsed={time.time()-t0:.0f}s)")
            else:
                reason = res.get("discard_reason", "unknown")
                discard_counts[reason] = discard_counts.get(reason, 0) + 1
                logger.info(f"[{i}/{len(candidates)}] discarded: {name} ({reason})")

    Path("temp/mining_results.json").write_text(json.dumps(results, indent=2))
    logger.info(f"DONE. {qualified}/{len(candidates)} qualified in {time.time()-t0:.0f}s")
    logger.info(f"Discard reasons: {json.dumps(discard_counts, indent=2)}")


if __name__ == "__main__":
    main()
