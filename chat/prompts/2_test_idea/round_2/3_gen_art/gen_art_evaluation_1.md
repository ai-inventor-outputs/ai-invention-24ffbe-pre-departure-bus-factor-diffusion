# gen_art_evaluation_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `iter1_0b7b616dce39` — Does Pre-Departure Authority Diffusion Predict Open-Source Project Survival? A Unified-Corpus Retest with a Window-Boundary-Noise Control
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_evaluation_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 17:45:14 UTC

```
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An artifact executor (Step 3.3: GEN_ART in the invention loop)

Executing a plan to produce a concrete artifact.
GEN_PAPER_TEXT will use your artifact in the next paper draft.

Rigorous artifact with clear results → strong paper. Sloppy artifact → misdirected research.
</your_role>
</ai_inventor_context>

<task>
Evaluate experimental results using domain-appropriate methods, metrics, and analysis techniques.
When in doubt, prefer more metrics over fewer — but only ones that make sense for the domain.
</task>

<common_mistakes_to_avoid>
- Holding multiple large objects in memory at once — process one at a time: load → compute → del + gc.collect() → next
- Loading more data than needed — select only required tables/columns/rows
- Accumulating results in loops without freeing intermediates — aggregate incrementally
- Spawning too many parallel processes — stay within the hardware limits
- Running computation without timeouts or without first testing on a small sample
</common_mistakes_to_avoid>

<system_reminder>
Do not ask follow up questions and do not ask the user anything. Execute all steps independently.
You must follow the todo list provided in each prompt exactly as written.
No placeholders, stubs, or incomplete code — all code must be complete and functional.
</system_reminder>

<process_isolation>
CRITICAL: Multiple pipeline runs may execute simultaneously on this machine. `ps aux | grep method.py` matches ALL runs, not just yours.
- NEVER kill processes by name (`killall`, `pkill -f`, `ps aux | grep ... | xargs kill`). This kills OTHER runs' processes.
- NEVER monitor processes by name (`ps aux | grep method.py`). You will see other runs' processes and get confused.
- ALWAYS use PID-based process management:
  Run: `uv run method.py & PID=$!` or `timeout <seconds> uv run method.py & PID=$!`
  Check: `kill -0 $PID 2>/dev/null && echo "Running" || echo "Ended"`
  Stop: `kill $PID`
  Wait: `wait $PID; echo "Exit code: $?"`
  Monitor: `tail -f logs/run.log & TAIL_PID=$!` then `kill $TAIL_PID` when done
</process_isolation>

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/file.py`, `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_evaluation_1_idx3
type: evaluation
title: Bootstrap CIs and Identity Spot-Check
summary: |-
  An evaluation artifact that adds statistical rigor to the founder-exit/survival experiment (art_eXxdnfS0o6aV): bootstrap 95% CIs on every reported Cohen's d snapshot-covariate effect size and on the placebo test's empirical percentile, plus a manual GitHub-profile spot-check of the identity/alias-resolution heuristic on a random 10-15 repo sample, consolidated into a single eval_out.json report that classifies each of the three pre-registered success criteria as tested-and-null, untestable-for-power, or now-resolved-by-CI.

  STEP 0 — Load and validate inputs.
  Read full_method_out.json from the dependency workspace (/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/full_method_out.json). Parse the per-repo `examples` array and the top-level `metadata` block, specifically: corpus_stats, baseline_replication, regression_results, matched_pairs_results, placebo_results, success_criteria_verdict. If any of these metadata keys is missing or empty, log a clear WARNING (not a silent skip) and mark that section's downstream analysis as 'INPUT_MISSING' in the final report rather than fabricating a number. Confirm the 24 TFDD repos with predict_our_method/predict_baseline_snapshot fields and the 30-repo usable analysis corpus are both present; record their exact counts at the top of the report so a reader can immediately see n for every subsequent statistic.

  STEP 1 — Bootstrap CIs on snapshot-covariate Cohen's d (resolves the MINOR scope critique).
  For each of the five snapshot covariates measured at TFDD (developers, commits, files, stars, forks), recover the two raw per-repo group samples (survivor vs non-survivor) that produced the originally reported Cohen's d, not just the scalar d itself — these should be reconstructable from the per-repo `examples` records using the survival label and the corresponding snapshot field. If raw per-repo values for a covariate are not present in method_out.json (e.g., d was computed but the underlying arrays were not persisted), state this explicitly as a data-availability limitation and either (a) reconstruct summary-based approximate CIs via Hedges/Cohen's d sampling-distribution formulas (using group n, d, and pooled SD if recoverable), clearly labeled 'analytic approximation, not resampled', or (b) mark that covariate's CI as NOT_COMPUTABLE_FROM_ARTIFACT — do not silently fall back to fabricated numbers.
  Where raw values ARE available: implement a nonparametric bootstrap with B=10,000 resamples (resample survivor and non-survivor groups independently, with replacement, at their original sizes; note that at n=30 with likely uneven group splits, this may leave one arm with single-digit n — flag any covariate where the smaller group's n<10 as LOW_RESOLUTION at the point it's reported, not buried in a footnote). For each resample, recompute Cohen's d = (mean1-mean2)/pooled_sd; take the 2.5th/97.5th percentiles of the resulting bootstrap distribution as the 95% CI. Fix a random seed for reproducibility and record it in the output.
  For every covariate, explicitly state whether Avelino et al.'s reported ESEM 2019 range (d=0.13 for files, d=0.25-0.26 for developers/commits; note stars/forks were not covariates Avelino et al. reported on file/dev/commit terms so treat those as this-study's own new covariates without an Avelino baseline to compare against — say so directly) falls INSIDE or OUTSIDE the newly bootstrapped 95% CI. Present this as a small table: covariate | n_survivor | n_nonsurvivor | point d | bootstrap 95% CI | Avelino reference value | inside/outside CI | resolution flag (adequate/low_resolution/not_computable).

  STEP 2 — Bootstrap CI on the placebo empirical percentile.
  The experiment's placebo test drew 200 null resamples of a randomly relocated 'pre-departure window' within each repo's own history and reported the true window's percentile rank among them (reported in the hypothesis text as 40th percentile with empirical p=0.615 at an earlier n=30 test — verify against the actual method_out.json placebo_results, which may differ slightly since this is the unified/reconciled corpus). To put a CI on that percentile rank itself: bootstrap-resample the 200 null-draw statistic values (or, if the raw 200 draws per repo are stored rather than one pooled null distribution, resample at the repo level first, then within-repo at the draw level, i.e. a two-stage/cluster bootstrap that respects the nesting) with B=10,000 resamples, and for each resample recompute where the true-window statistic falls as a percentile of that resampled null. Report the resulting 95% CI on the percentile. State explicitly whether this CI is wide enough to include both 'no signal' (~50th percentile) and 'some signal' (e.g. <25th or >75th percentile) — if so, say plainly that the placebo result cannot currently distinguish a true null from a weak real effect, rather than presenting the point estimate alone as if it settled the question.

  STEP 3 — Manual identity-resolution spot-check.
  From the 30-repo (or 46-prefiltered, whichever the experiment's REPO_LIST covers) unified corpus, deterministically sample 12 repos (fix a seed, e.g. numpy RandomState(42), and document the exact repo list and seed in the output so it's reproducible) stratified where possible across language/ecosystem to catch different noreply-email conventions (e.g. GitHub noreply patterns differ slightly by account age). For each sampled repo, using the aii-web-tools skill (web fetch + fetch_grep, NOT authenticated API calls — GitHub REST is rate-limited without a token and this must not require secrets), open the repo's GitHub commit history / contributors page and the founder's and 2-3 top non-founder contributors' public profile pages. Cross-check: (a) does the local alias-resolution heuristic's inferred founder identity match the actual first-committer/creator shown on GitHub; (b) do noreply-email-derived aliases the pipeline merged into one identity actually belong to the same GitHub account (spot check by following the noreply email pattern <id>+<username>@users.noreply.github.com back to the username, which is directly parseable without API calls); (c) are there any obviously-missed merges (same display name, different email, not merged) or over-merges (different people merged into one) visible from the commit list.
  Record for each of the 12 repos: PASS (identity resolution matches GitHub ground truth), ALIAS_MERGE_ERROR (specific description), or AMBIGUOUS (cannot determine from public page, e.g. private email commits). Compute an observed error rate = (ALIAS_MERGE_ERROR count) / 12, with a Wilson score 95% CI for this small-n proportion (do not use a naive normal-approximation CI at n=12). Report this as a concrete bound on the MINOR data-quality risk for the founder-only-TFDD qualification step, and explicitly discuss whether any detected errors would plausibly change founder identification or TF=1 status for that repo's event (which would be a more serious finding than a cosmetic alias miscount).

  STEP 4 — Consolidated verdict table (resolves the MAJOR framing critique).
  Build a single summary table classifying each of the three original pre-registered success criteria (matched-pairs survival-rate-ratio CI excluding 1x; BH-FDR-significant regression coefficients exceeding snapshot-covariate effect size; placebo/shuffle check showing weaker effect at relocated windows) into exactly one of: TESTED_NULL (ran to completion, produced a result distinguishable from chance, did not meet the pre-registered bar), TESTED_LOW_RESOLUTION (ran, but bootstrap CI from Step 1/2 is too wide to distinguish null from a real small-to-moderate effect), or UNTESTABLE_AT_SCALE (zero usable observations per stratification cell, as already documented in the experiment). Use the newly computed CIs to decide TESTED_NULL vs TESTED_LOW_RESOLUTION rather than asserting it. State the practical implication of each classification for what a future, larger-corpus iteration would need to change.

  STEP 5 — Output.
  Write eval_out.json conforming to the exp_eval_sol_out schema (validate with the aii-json skill before finishing): top-level metadata carrying corpus_stats (echoed from input), covariate_ci_table (from Step 1), placebo_ci (from Step 2), identity_spotcheck_results (from Step 3, including the Wilson CI and per-repo findings), and success_criteria_reclassification (from Step 4). Per-example entries (if the schema requires per-repo predictions) can simply echo the original experiment's predict_our_method/predict_baseline_snapshot fields unchanged, since this artifact evaluates existing results rather than generating new predictions. Run the aii-json skill's mini/preview generation. If any bootstrap or spot-check step could not be completed (e.g., raw per-covariate arrays genuinely absent from method_out.json), the final report must say so in plain language rather than omitting the covariate silently — a reader must be able to tell 'not computed because unavailable' from 'computed and small'.

  FAILURE MODES TO HANDLE: (1) If method_out.json's per-repo records lack raw covariate values needed for a true nonparametric bootstrap, fall back to the analytic Hedges'-d-CI formula (documented, e.g., in Cousineau & Goulet-Pelletier 2021, or standard Cohen's d sampling variance Var(d) ≈ (n1+n2)/(n1*n2) + d²/(2*(n1+n2))) and label results 'analytic, not resampled'. (2) If web fetch of a GitHub profile page is blocked, rate-limited, or the repo/user has since gone private, mark that repo AMBIGUOUS and swap in the next repo from the seeded sample list rather than silently shrinking n below 12 without saying so. (3) If the placebo null draws are stored only as a single pooled percentile with no underlying 200 raw values, state that a proper bootstrap CI is not reconstructable from the artifact as saved and report this as a concrete, named gap for the next experiment iteration to fix by persisting raw null-draw values.
runpod_compute_profile: gpu
metrics_descriptions: >-
  (1) Bootstrap 95% confidence intervals (B=10,000 resamples, seeded) on Cohen's d for each snapshot covariate (developers,
  commits, files, stars, forks) measured at the TFDD point, computed via nonparametric resampling of the raw per-repo survivor/non-survivor
  values where available, or an analytic Hedges'-d sampling-variance approximation where raw values cannot be recovered from
  the experiment artifact. (2) A bootstrap 95% CI on the placebo test's empirical percentile rank (the true pre-departure
  window's rank among 200 within-repo random-window null draws), using a two-stage cluster bootstrap if draws are nested per
  repo. (3) An observed identity/alias-resolution error rate from a manual 12-repo GitHub-profile spot-check, reported as
  a point estimate with a Wilson score 95% CI appropriate for small-n proportions, broken into PASS / ALIAS_MERGE_ERROR /
  AMBIGUOUS counts. (4) A three-way reclassification of the original pre-registered success criteria (TESTED_NULL, TESTED_LOW_RESOLUTION,
  UNTESTABLE_AT_SCALE) driven by whether the new CIs from (1)-(2) are narrow enough to distinguish a genuine null from a merely
  underpowered result.
metrics_justification: >-
  The hypothesis's own self-critique (from the prior iteration's reviewer) is that its central claim was tested at n=30 with
  no CIs on the reported effect sizes, so a scalar Cohen's d or a single percentile rank cannot on its own distinguish 'genuinely
  no effect' from 'too little data to tell' -- exactly the ambiguity the hypothesis text itself flags as the difference between
  a real null and an untested claim. Bootstrap CIs directly quantify that ambiguity: a CI that excludes Avelino et al.'s 0.13-0.26
  reference range supports treating the result as a genuine, resolvable null; a CI wide enough to contain both zero and a
  moderate effect supports the hypothesis's own honest downgrade to 'low-resolution, not falsified.' Putting a CI on the placebo
  percentile serves the same purpose for the one test that did run to completion -- it converts a single 40th-percentile point
  estimate into an interval that either does or does not rule out a real pre-departure signal. The identity spot-check targets
  a distinct, previously unverified risk: founder/authority disambiguation is a load-bearing step for the entire founder-only-TFDD
  qualification (misidentifying the founder or merging the wrong aliases could silently corrupt which events even qualify
  as TF=1 detachments), and no part of the original experiment validated this heuristic against ground truth. Measuring its
  error rate on a real sample turns a previously unquantified MINOR risk into a concrete, citable bound. Together these three
  measurements let the final report make the exact claim the hypothesis needs to make honestly: which of the three pre-registered
  criteria are actually resolved by current evidence versus which remain open only because of insufficient power -- precisely
  the MAJOR framing critique this artifact is scoped to close.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_eXxdnfS0o6aV
type: experiment
title: Founder Exit and Repo Survival
summary: >-
  Implements a full recomputation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship / Truck-Factor / Truck-Factor-Developer-Departure
  (TFDD) pipeline on real GitHub repositories, plus a new pre-departure authority-diffusion measurement and three analyses
  testing whether it predicts post-departure survival better than Avelino et al.'s null snapshot covariates. Because the upstream
  DATASET artifact this experiment depended on (gen_art_dataset_1) had an empty data_out/ at execution time, method.py is
  self-contained: it mines a curated corpus of 62 mature, well-known GitHub repositories (JavaScript, Python, Ruby, PHP, Java,
  C++, Go) directly via metadata-only blobless git clones plus the unauthenticated GitHub REST API, documented in REPO_LIST.
  For each repo it builds a chronological (author, file, timestamp) commit event log with GitHub-noreply-email alias resolution,
  computes the Fritz/Avelino DOA formula and greedy Truck-Factor at quarterly snapshots (monthly was infeasible at this compute
  budget; the fallback_plan sanctions quarterly resolution with a documented TFDD-date fuzz), identifies each repo's founder,
  and scans for the first TFDD where the truck-factor set is the founder alone and stays silent 12+ months, requiring >=12mo
  pre-history and >=18mo post-history. The new measurement computes founder commit-share and the count of distinct non-founder
  DOA file-owners in the 6-12mo pre-TFDD window. The outcome is an Active/Inactive/recovery model: binary survival = whether
  a new non-founder developer attains truck-factor status post-TFDD, plus a graded post/pre commit-velocity ratio. Confound
  controls recompute Avelino et al.'s own null snapshot covariates (stars, forks, contributor count, developers/commits/files
  at TFDD). Three analyses run: (a) standardized logistic + ordinal regression with BH-FDR correction; (b) matched-pairs nearest-neighbor
  bootstrap CI on the survival-rate ratio; (c) a within-repo random-window placebo test (200 null draws, reduced from 1000
  for CPU budget). Of 62 curated repos, 46 passed CONSORT-style prefilters and 30 yielded a usable founder-only TFDD with
  sufficient history, forming the analysis corpus. The result is a genuine, non-fabricated NULL finding: none of the three
  pre-registered success criteria were met (BH-adjusted p~0.77-0.81; diffusion coef did not exceed snapshot coef; placebo
  p did not clear 0.10) -- the fallback_plan treats this as a valid outcome, most plausibly due to reduced sample size (n=30)
  rather than a pipeline defect, since all pipeline stages executed and converged without error. Two documented deviations:
  (1) DL(a,f) uses the standard Fritz/Avelino textual definition without re-verifying against the ICPC 2016 paper text; (2)
  the source-file-fraction prefilter was relaxed from 0.60 to 0.40 after piloting showed 0.60 rejected most real repos. method.py
  writes method_out.json per the exp_gen_sol_out schema: one example per repo with full per-repo results, predict_our_method/predict_baseline_snapshot
  fields on the 24 TFDD repos, and metadata carrying corpus_stats, baseline_replication, regression_results, matched_pairs_results,
  placebo_results, and success_criteria_verdict. Downstream paper-writing should present this as a rigorous null/scope-boundary
  result, not evidence the hypothesis is false.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **SPEND BUDGET**: at most $10 USD of OpenRouter API calls for this artifact. Nothing outside your own code enforces this — the key you are given has no per-artifact cap — so it holds only if you track cumulative cost after every call and stop when you approach it. Budget the work up front: estimate the per-call cost and the number of calls BEFORE starting a sweep, not after it overruns. Exceeding it spends real money that the run cannot recover.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Free-first web search (general + scholarly modes), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-concept-fig-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>
</available_resources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for evaluation metrics, agent orchestration patterns, benchmark design.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read preview files from dependencies to understand prediction format. Evaluate ALL experiments provided — do not skip or select a subset. Avoid re-training or re-executing the method unless absolutely necessary; prefer loading predictions from each dependency's method_out.json / predict_* fields. Read domain handbook if applicable (see <available_domain_handbooks>). Decide evaluation metrics based on artifact plan. Test basic functionality with 'uv run'.
TODO 3. Fully implement evaluation as described in artifact plan in './eval.py'. Use exp_eval_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant metrics or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
```

### [2] HUMAN-USER prompt · 2026-08-21 17:45:14 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-python · 2026-08-21 17:45:18 UTC

The agent loaded the **aii-python** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-python
description: "Applies this repo's Python conventions to experiment and evaluation scripts: uv-only environment setup (never pip), loguru logging with stdout plus a rotating file sink, @logger.catch(reraise=True) with explicit exception types, pathlib file access, type hints, and a standard main() script skeleton. ALWAYS read before writing or editing any Python script that runs an experiment, evaluation, or data-processing job. Triggers: writing or refactoring a Python script, uv venv, uv pip install, pyproject dependencies, loguru, logging setup, try/except and error handling, pathlib, script structure, Python 3.12. NOT for: parallelism, GPU throughput or hardware sizing (use aii-parallel-computing and aii-use-hardware), scaling long autonomous jobs (use aii-long-running-tasks), splitting oversized output files (use aii-file-size-limit), calling LLMs (use aii-openrouter-llms), or notebooks meant for Colab (use aii-colab)."
---

## Environment Setup

- Python 3.12+
- **NEVER use `pip` or `.venv/bin/pip`** — they are not installed. Use `uv` for ALL package operations:
  ```bash
  uv venv .venv --python=3.12
  source .venv/bin/activate  # or: .venv/bin/python script.py
  uv pip install pandas loguru  # NOT: pip install
  ```
- Create `.toml` file with dependencies, create uv `.venv` and activate it
- NO inline dependencies (no `# /// script` headers)

## Logging

Use `loguru` for all logging. Add a file sink alongside stdout.

```python
from loguru import logger
import sys

logger.remove()  # Remove default handler
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
```

Rules:
- Log every major step (data loading, processing start/end, results)
- If applicable, log every LLM API call input and output
- Truncate long outputs in logs (add truncation logic for potentially large strings)
- Use `logger.error()` in except blocks (traceback auto-captured)

## Error Handling

- Wrap major operations in try/except blocks
- Use `@logger.catch(reraise=True)` decorator on main functions — without `reraise=True`, the script exits 0 even on uncaught exceptions, hiding failures from downstream consumers
- Use explicit exception types, not bare `except:`
- Never silently swallow exceptions — always log them

```python
@logger.catch(reraise=True)
def main():
    try:
        data = load_data(path)
    except FileNotFoundError:
        logger.error("Data file not found")
        raise
    except json.JSONDecodeError:
        logger.error("Invalid JSON in data file")
        raise
```

## Code Structure

- Use `pathlib.Path` for file operations: `Path("data/input.json").read_text()` not `open(...).read()`
- Use type hints for function signatures
- Use keyword arguments for functions with more than 4 parameters
- No hardcoded paths — derive from script location or accept as arguments

## Script Pattern

Standard pattern for experiment/evaluation scripts:

```python
#!/usr/bin/env python3
"""Brief description of what this script does."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load data
    data_path = Path("full_data_out.json")
    logger.info(f"Loading data from {data_path}")
    data = json.loads(data_path.read_text())
    logger.info(f"Loaded {len(data['examples'])} examples")

    # Process
    results = []
    for i, example in enumerate(data["examples"]):
        try:
            result = process(example)
            results.append(result)
        except Exception:
            logger.error(f"Failed on example {i}")
            continue

    # Save output
    output = {"examples": results}
    Path("method_out.json").write_text(json.dumps(output, indent=2))
    logger.info(f"Saved {len(results)} results")

if __name__ == "__main__":
    main()
```
````

### [4] SKILL-INPUT — aii-web-tools · 2026-08-21 17:46:02 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Runs web search, page fetch as markdown, and regex grep over full HTML or PDF text via this skill's own scripts (aii_fast_web_search.py, aii_fast_web_fetch.py) — a free-first keyless search stack with Serper fallback that works even where built-in WebSearch and WebFetch are absent. Use when a query, page, or paper must be searched, read, or mined for an exact quote, number, table value, or methodology sentence, and whenever a lossy summary would lose the detail. Triggers: web search, scholarly search, OpenAlex, Crossref, Serper, fetch a URL as markdown, read a PDF, arXiv, regex grep a page, exact quote, table value, citation check. NOT for: planning a broad multi-source literature review or mass verification campaign — use aii-web-research-tools; NOT for a PDF file already on disk — extraction, form filling, merging and PDF creation are anthropic-pdf; NOT for driving a browser or testing a UI."
---

## Web tools

You have three web capabilities: **search**, **fetch**, and **grep** (exact
regex extraction over a full page or PDF).

**Pick where they come from, in this order:**

1. **If you have built-in `WebSearch` / `WebFetch` tools, PREFER those over the
   scripts below.** They may be **deferred tools** (listed by name but with
   schemas not yet loaded) — if so, call `ToolSearch("select:WebSearch,WebFetch")`
   ONCE to load them, then use them normally. Do not skip them just because they
   need that one extra load step; they are the preferred path. Pair them with the
   `aii_web_tools__fetch_grep` script below when you need exact text / numbers /
   methodology that a summary would miss, or when reading a PDF.
2. **Only if you have NO built-in `WebSearch` / `WebFetch`** (e.g. the OpenHands
   backend), use the scripts in this skill (below). They are our own
   implementations — free-first web search (keyless general/scholarly engines,
   Serper fallback), html2text + PyMuPDF for fetch, and regex grep over the full
   document text. They work without any built-in web tools.

Workflow either way: **search** (discover) → **fetch** (read for the gist) →
**grep** (pull exact details / read PDFs).

---

## Running the scripts

Run every script with the skill's pre-provisioned interpreter (it already has
`requests`, `html2text`, `pymupdf`, `python-dotenv`). Set `PY` once:

```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

### 1. Search the web (free-first: general or scholarly)

```bash
# general web (default): keyless engines (ddgs, marginalia); Serper only if they miss
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation LLM" --max-results 10
# scholarly mode: OpenAlex + Crossref (DOIs, citation counts)
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation" --mode scholarly
```

Returns ranked title / URL / snippet lines. `--mode general` (default) uses
keyless general engines; `--mode scholarly` uses academic APIs. Both fall back
to Serper (paid) only when the free engines miss. Use search first to scan the
landscape; snippets are for discovery only — fetch a page before judging it.

### 2. Fetch a page as markdown (HTML or PDF)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2303.11366" --max-chars 10000
```

`--max-chars` caps output (default 10000); `--char-offset N` pages further in.
Handles PDFs transparently via PyMuPDF.

### 3. Grep a page or PDF (exact regex extraction)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2303.11366" --pattern "verbal reinforcement" --max-matches 20 --context-chars 200
```

Returns only the matching sections with surrounding context — the right tool
for exact numbers, table values, methodology, or long PDFs where a summary
would lose the detail. `-i` for case-insensitive.

**Parallelize** independent searches/fetches in one turn; only sequence a
fetch after the search that produced its URL.

---

## Notes

- The scripts call our ability server. If a script prints
  `Ability service not available`, the server is down — say so rather than
  silently improvising a different search method.
- Do **not** hand-roll your own `requests`/scraping for search when these
  tools are available: Serper returns clean Google results and the fetch/grep
  scripts already handle HTML, PDFs, and encoding.
````

### [5] SKILL-INPUT — aii-json · 2026-08-21 17:50:12 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: "Validates JSON files against this repo's experiment-pipeline schemas (exp_sel_data_out, exp_gen_sol_out, exp_eval_sol_out, exp_proof_out) and generates size-optimized full, mini and preview variants of any JSON array file. ALWAYS use before treating a pipeline stage output as finished, whenever a schema or required-property error must be fixed, and whenever a large JSON file needs a small truncated version safe to read. Triggers: JSON schema validation, schema compliance, required property errors, pipeline stage outputs, the exp_*_out format names, mini and preview JSON generation, shrinking a large JSON before inspection. NOT for: discovering or downloading new datasets, which aii-hf-datasets and aii-owid-datasets cover; splitting oversized output files, which aii-file-size-limit covers; plotting JSON data, which aii-data-fig-gen covers; spreadsheet and .csv tabular data, which anthropic-xlsx covers."
---

## Contents

- Validating JSON (schema validation against experiment schemas)
- Formatting JSON (generate full/mini/preview versions)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Validating JSON

Validate JSON files against predefined schemas for experiment-based hypothesis selection, data collection, solution generation, and evaluation.

### Quick Start

1. Read the schema spec you need to adhere to (e.g., `schemas/exp_eval_sol_out.json`)
2. Create your output file following that schema structure
3. Validate:

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /path/to/eval_out.json
```

### Script: aii_json_validate_schema.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /tmp/eval_out.json
```

**Parallel execution (multiple validations):**

IMPORTANT: When validating multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_validate_schema.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --format {1} --file {2}' ::: 'exp_sel_data_out' 'exp_gen_sol_out' 'exp_eval_sol_out' :::+ '/tmp/full_data_out.json' '/tmp/method_out.json' '/tmp/eval_out.json'
```

**Example output (success):**
```
Validating: aii_json_validate_schema.py
Format: exp_eval_sol_out

✓ Validation PASSED
```

**Example output (failure):**
```
Validating: aii_json_validate_schema.py
Format: exp_sel_data_out

✗ Validation FAILED

Errors:
  Path: datasets → 0 → examples → 0
  Error: 'output' is a required property
  Validator: required
```

**Parameters:**

`--format` (required)
- Format type to validate against
- Determines which schema to use

`--file` (required)
- Path to JSON file to validate
- Must be valid JSON
- **Always pass an absolute path.** Relative paths resolve from the
  ability server's CWD (typically ``/ai-inventor/aii_server``), not from
  your agent workspace, so ``data_out/x.json`` will silently look in the
  wrong directory and fail with "Could not load JSON file". The validate
  endpoint also accepts a ``workspace_dir`` arg if you need to keep a
  relative path — pass your workspace path there.

**Tips:**
- Fix errors in your JSON and rerun validation until it passes

### Schema Files

Schemas are stored in `.claude/skills/aii-json/schemas/`:

**Hypothesis Selection & Evaluation:**
- `sel_hypo_out.json` - Hypothesis Selection output (all hypotheses with selected flags)
- `feasibility_eval_all.json` - All hypotheses with feasibility scores
- `feasibility_eval_top.json` - Top 5 most feasible hypotheses
- `novelty_research_one.json` - Single hypothesis novelty research arguments with citations
- `novelty_eval_all.json` - All hypotheses with novelty scores
- `novelty_eval_top.json` - Single best selected hypothesis

**Experiment Pipeline:**
- `exp_sel_data_out.json` - Experiment Data Selection format
- `exp_gen_sol_out.json` - Experiment Solution Generation format
- `exp_eval_sol_out.json` - Experiment Solution Evaluation format

---

## Formatting JSON

Generate three size-optimized versions of a JSON file for efficient development and preview:
- **full**: Identical to original (all data)
- **mini**: First 3 items only (for quick testing)
- **preview**: Mini + all strings truncated to 200 chars (for quick inspection)

### Quick Start

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

### Script: aii_json_format_mini_preview.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

**Parallel execution (multiple files):**

IMPORTANT: When formatting multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_format_mini_preview.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --input {}' ::: 'full_data_out.json' 'method_out.json' 'eval_out.json'
```

**Example output:**
```
Generated 3 versions:
  Full (50 items): /path/to/full_method_out.json
  Mini (3 items): /path/to/mini_method_out.json
  Preview (3 items, truncated): /path/to/preview_method_out.json
```

**Parameters:**

`--input` (required)
- Path to input JSON file
- Must have a top-level array
- Example: `method_out.json`, `full_data_out.json`

`--output-dir` (optional)
- Output directory for generated files
- Default: same directory as input file
- Files are prefixed with `full_`, `mini_`, `preview_`

**Output Files:**

All three files use the same base name with different prefixes:
- `full_{basename}.json` - Complete dataset (identical to original)
- `mini_{basename}.json` - First 3 array items only
- `preview_{basename}.json` - First 3 items with strings truncated to 200 chars

**Tips:**
- Input JSON must have a top-level array structure
- String truncation is recursive (applies to nested objects and arrays)
- Use preview files for quick inspection without reading large datasets
- Use mini files for developing/testing code before running on full dataset

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [6] SYSTEM-USER prompt · 2026-08-21 17:52:04 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/file.py`, `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_evaluation_1_idx3
type: evaluation
title: Bootstrap CIs and Identity Spot-Check
summary: |-
  An evaluation artifact that adds statistical rigor to the founder-exit/survival experiment (art_eXxdnfS0o6aV): bootstrap 95% CIs on every reported Cohen's d snapshot-covariate effect size and on the placebo test's empirical percentile, plus a manual GitHub-profile spot-check of the identity/alias-resolution heuristic on a random 10-15 repo sample, consolidated into a single eval_out.json report that classifies each of the three pre-registered success criteria as tested-and-null, untestable-for-power, or now-resolved-by-CI.

  STEP 0 — Load and validate inputs.
  Read full_method_out.json from the dependency workspace (/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/full_method_out.json). Parse the per-repo `examples` array and the top-level `metadata` block, specifically: corpus_stats, baseline_replication, regression_results, matched_pairs_results, placebo_results, success_criteria_verdict. If any of these metadata keys is missing or empty, log a clear WARNING (not a silent skip) and mark that section's downstream analysis as 'INPUT_MISSING' in the final report rather than fabricating a number. Confirm the 24 TFDD repos with predict_our_method/predict_baseline_snapshot fields and the 30-repo usable analysis corpus are both present; record their exact counts at the top of the report so a reader can immediately see n for every subsequent statistic.

  STEP 1 — Bootstrap CIs on snapshot-covariate Cohen's d (resolves the MINOR scope critique).
  For each of the five snapshot covariates measured at TFDD (developers, commits, files, stars, forks), recover the two raw per-repo group samples (survivor vs non-survivor) that produced the originally reported Cohen's d, not just the scalar d itself — these should be reconstructable from the per-repo `examples` records using the survival label and the corresponding snapshot field. If raw per-repo values for a covariate are not present in method_out.json (e.g., d was computed but the underlying arrays were not persisted), state this explicitly as a data-availability limitation and either (a) reconstruct summary-based approximate CIs via Hedges/Cohen's d sampling-distribution formulas (using group n, d, and pooled SD if recoverable), clearly labeled 'analytic approximation, not resampled', or (b) mark that covariate's CI as NOT_COMPUTABLE_FROM_ARTIFACT — do not silently fall back to fabricated numbers.
  Where raw values ARE available: implement a nonparametric bootstrap with B=10,000 resamples (resample survivor and non-survivor groups independently, with replacement, at their original sizes; note that at n=30 with likely uneven group splits, this may leave one arm with single-digit n — flag any covariate where the smaller group's n<10 as LOW_RESOLUTION at the point it's reported, not buried in a footnote). For each resample, recompute Cohen's d = (mean1-mean2)/pooled_sd; take the 2.5th/97.5th percentiles of the resulting bootstrap distribution as the 95% CI. Fix a random seed for reproducibility and record it in the output.
  For every covariate, explicitly state whether Avelino et al.'s reported ESEM 2019 range (d=0.13 for files, d=0.25-0.26 for developers/commits; note stars/forks were not covariates Avelino et al. reported on file/dev/commit terms so treat those as this-study's own new covariates without an Avelino baseline to compare against — say so directly) falls INSIDE or OUTSIDE the newly bootstrapped 95% CI. Present this as a small table: covariate | n_survivor | n_nonsurvivor | point d | bootstrap 95% CI | Avelino reference value | inside/outside CI | resolution flag (adequate/low_resolution/not_computable).

  STEP 2 — Bootstrap CI on the placebo empirical percentile.
  The experiment's placebo test drew 200 null resamples of a randomly relocated 'pre-departure window' within each repo's own history and reported the true window's percentile rank among them (reported in the hypothesis text as 40th percentile with empirical p=0.615 at an earlier n=30 test — verify against the actual method_out.json placebo_results, which may differ slightly since this is the unified/reconciled corpus). To put a CI on that percentile rank itself: bootstrap-resample the 200 null-draw statistic values (or, if the raw 200 draws per repo are stored rather than one pooled null distribution, resample at the repo level first, then within-repo at the draw level, i.e. a two-stage/cluster bootstrap that respects the nesting) with B=10,000 resamples, and for each resample recompute where the true-window statistic falls as a percentile of that resampled null. Report the resulting 95% CI on the percentile. State explicitly whether this CI is wide enough to include both 'no signal' (~50th percentile) and 'some signal' (e.g. <25th or >75th percentile) — if so, say plainly that the placebo result cannot currently distinguish a true null from a weak real effect, rather than presenting the point estimate alone as if it settled the question.

  STEP 3 — Manual identity-resolution spot-check.
  From the 30-repo (or 46-prefiltered, whichever the experiment's REPO_LIST covers) unified corpus, deterministically sample 12 repos (fix a seed, e.g. numpy RandomState(42), and document the exact repo list and seed in the output so it's reproducible) stratified where possible across language/ecosystem to catch different noreply-email conventions (e.g. GitHub noreply patterns differ slightly by account age). For each sampled repo, using the aii-web-tools skill (web fetch + fetch_grep, NOT authenticated API calls — GitHub REST is rate-limited without a token and this must not require secrets), open the repo's GitHub commit history / contributors page and the founder's and 2-3 top non-founder contributors' public profile pages. Cross-check: (a) does the local alias-resolution heuristic's inferred founder identity match the actual first-committer/creator shown on GitHub; (b) do noreply-email-derived aliases the pipeline merged into one identity actually belong to the same GitHub account (spot check by following the noreply email pattern <id>+<username>@users.noreply.github.com back to the username, which is directly parseable without API calls); (c) are there any obviously-missed merges (same display name, different email, not merged) or over-merges (different people merged into one) visible from the commit list.
  Record for each of the 12 repos: PASS (identity resolution matches GitHub ground truth), ALIAS_MERGE_ERROR (specific description), or AMBIGUOUS (cannot determine from public page, e.g. private email commits). Compute an observed error rate = (ALIAS_MERGE_ERROR count) / 12, with a Wilson score 95% CI for this small-n proportion (do not use a naive normal-approximation CI at n=12). Report this as a concrete bound on the MINOR data-quality risk for the founder-only-TFDD qualification step, and explicitly discuss whether any detected errors would plausibly change founder identification or TF=1 status for that repo's event (which would be a more serious finding than a cosmetic alias miscount).

  STEP 4 — Consolidated verdict table (resolves the MAJOR framing critique).
  Build a single summary table classifying each of the three original pre-registered success criteria (matched-pairs survival-rate-ratio CI excluding 1x; BH-FDR-significant regression coefficients exceeding snapshot-covariate effect size; placebo/shuffle check showing weaker effect at relocated windows) into exactly one of: TESTED_NULL (ran to completion, produced a result distinguishable from chance, did not meet the pre-registered bar), TESTED_LOW_RESOLUTION (ran, but bootstrap CI from Step 1/2 is too wide to distinguish null from a real small-to-moderate effect), or UNTESTABLE_AT_SCALE (zero usable observations per stratification cell, as already documented in the experiment). Use the newly computed CIs to decide TESTED_NULL vs TESTED_LOW_RESOLUTION rather than asserting it. State the practical implication of each classification for what a future, larger-corpus iteration would need to change.

  STEP 5 — Output.
  Write eval_out.json conforming to the exp_eval_sol_out schema (validate with the aii-json skill before finishing): top-level metadata carrying corpus_stats (echoed from input), covariate_ci_table (from Step 1), placebo_ci (from Step 2), identity_spotcheck_results (from Step 3, including the Wilson CI and per-repo findings), and success_criteria_reclassification (from Step 4). Per-example entries (if the schema requires per-repo predictions) can simply echo the original experiment's predict_our_method/predict_baseline_snapshot fields unchanged, since this artifact evaluates existing results rather than generating new predictions. Run the aii-json skill's mini/preview generation. If any bootstrap or spot-check step could not be completed (e.g., raw per-covariate arrays genuinely absent from method_out.json), the final report must say so in plain language rather than omitting the covariate silently — a reader must be able to tell 'not computed because unavailable' from 'computed and small'.

  FAILURE MODES TO HANDLE: (1) If method_out.json's per-repo records lack raw covariate values needed for a true nonparametric bootstrap, fall back to the analytic Hedges'-d-CI formula (documented, e.g., in Cousineau & Goulet-Pelletier 2021, or standard Cohen's d sampling variance Var(d) ≈ (n1+n2)/(n1*n2) + d²/(2*(n1+n2))) and label results 'analytic, not resampled'. (2) If web fetch of a GitHub profile page is blocked, rate-limited, or the repo/user has since gone private, mark that repo AMBIGUOUS and swap in the next repo from the seeded sample list rather than silently shrinking n below 12 without saying so. (3) If the placebo null draws are stored only as a single pooled percentile with no underlying 200 raw values, state that a proper bootstrap CI is not reconstructable from the artifact as saved and report this as a concrete, named gap for the next experiment iteration to fix by persisting raw null-draw values.
runpod_compute_profile: gpu
metrics_descriptions: >-
  (1) Bootstrap 95% confidence intervals (B=10,000 resamples, seeded) on Cohen's d for each snapshot covariate (developers,
  commits, files, stars, forks) measured at the TFDD point, computed via nonparametric resampling of the raw per-repo survivor/non-survivor
  values where available, or an analytic Hedges'-d sampling-variance approximation where raw values cannot be recovered from
  the experiment artifact. (2) A bootstrap 95% CI on the placebo test's empirical percentile rank (the true pre-departure
  window's rank among 200 within-repo random-window null draws), using a two-stage cluster bootstrap if draws are nested per
  repo. (3) An observed identity/alias-resolution error rate from a manual 12-repo GitHub-profile spot-check, reported as
  a point estimate with a Wilson score 95% CI appropriate for small-n proportions, broken into PASS / ALIAS_MERGE_ERROR /
  AMBIGUOUS counts. (4) A three-way reclassification of the original pre-registered success criteria (TESTED_NULL, TESTED_LOW_RESOLUTION,
  UNTESTABLE_AT_SCALE) driven by whether the new CIs from (1)-(2) are narrow enough to distinguish a genuine null from a merely
  underpowered result.
metrics_justification: >-
  The hypothesis's own self-critique (from the prior iteration's reviewer) is that its central claim was tested at n=30 with
  no CIs on the reported effect sizes, so a scalar Cohen's d or a single percentile rank cannot on its own distinguish 'genuinely
  no effect' from 'too little data to tell' -- exactly the ambiguity the hypothesis text itself flags as the difference between
  a real null and an untested claim. Bootstrap CIs directly quantify that ambiguity: a CI that excludes Avelino et al.'s 0.13-0.26
  reference range supports treating the result as a genuine, resolvable null; a CI wide enough to contain both zero and a
  moderate effect supports the hypothesis's own honest downgrade to 'low-resolution, not falsified.' Putting a CI on the placebo
  percentile serves the same purpose for the one test that did run to completion -- it converts a single 40th-percentile point
  estimate into an interval that either does or does not rule out a real pre-departure signal. The identity spot-check targets
  a distinct, previously unverified risk: founder/authority disambiguation is a load-bearing step for the entire founder-only-TFDD
  qualification (misidentifying the founder or merging the wrong aliases could silently corrupt which events even qualify
  as TF=1 detachments), and no part of the original experiment validated this heuristic against ground truth. Measuring its
  error rate on a real sample turns a previously unquantified MINOR risk into a concrete, citable bound. Together these three
  measurements let the final report make the exact claim the hypothesis needs to make honestly: which of the three pre-registered
  criteria are actually resolved by current evidence versus which remain open only because of insufficient power -- precisely
  the MAJOR framing critique this artifact is scoped to close.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_eXxdnfS0o6aV
type: experiment
title: Founder Exit and Repo Survival
summary: >-
  Implements a full recomputation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship / Truck-Factor / Truck-Factor-Developer-Departure
  (TFDD) pipeline on real GitHub repositories, plus a new pre-departure authority-diffusion measurement and three analyses
  testing whether it predicts post-departure survival better than Avelino et al.'s null snapshot covariates. Because the upstream
  DATASET artifact this experiment depended on (gen_art_dataset_1) had an empty data_out/ at execution time, method.py is
  self-contained: it mines a curated corpus of 62 mature, well-known GitHub repositories (JavaScript, Python, Ruby, PHP, Java,
  C++, Go) directly via metadata-only blobless git clones plus the unauthenticated GitHub REST API, documented in REPO_LIST.
  For each repo it builds a chronological (author, file, timestamp) commit event log with GitHub-noreply-email alias resolution,
  computes the Fritz/Avelino DOA formula and greedy Truck-Factor at quarterly snapshots (monthly was infeasible at this compute
  budget; the fallback_plan sanctions quarterly resolution with a documented TFDD-date fuzz), identifies each repo's founder,
  and scans for the first TFDD where the truck-factor set is the founder alone and stays silent 12+ months, requiring >=12mo
  pre-history and >=18mo post-history. The new measurement computes founder commit-share and the count of distinct non-founder
  DOA file-owners in the 6-12mo pre-TFDD window. The outcome is an Active/Inactive/recovery model: binary survival = whether
  a new non-founder developer attains truck-factor status post-TFDD, plus a graded post/pre commit-velocity ratio. Confound
  controls recompute Avelino et al.'s own null snapshot covariates (stars, forks, contributor count, developers/commits/files
  at TFDD). Three analyses run: (a) standardized logistic + ordinal regression with BH-FDR correction; (b) matched-pairs nearest-neighbor
  bootstrap CI on the survival-rate ratio; (c) a within-repo random-window placebo test (200 null draws, reduced from 1000
  for CPU budget). Of 62 curated repos, 46 passed CONSORT-style prefilters and 30 yielded a usable founder-only TFDD with
  sufficient history, forming the analysis corpus. The result is a genuine, non-fabricated NULL finding: none of the three
  pre-registered success criteria were met (BH-adjusted p~0.77-0.81; diffusion coef did not exceed snapshot coef; placebo
  p did not clear 0.10) -- the fallback_plan treats this as a valid outcome, most plausibly due to reduced sample size (n=30)
  rather than a pipeline defect, since all pipeline stages executed and converged without error. Two documented deviations:
  (1) DL(a,f) uses the standard Fritz/Avelino textual definition without re-verifying against the ICPC 2016 paper text; (2)
  the source-file-fraction prefilter was relaxed from 0.60 to 0.40 after piloting showed 0.60 rejected most real repos. method.py
  writes method_out.json per the exp_gen_sol_out schema: one example per repo with full per-repo results, predict_our_method/predict_baseline_snapshot
  fields on the 24 TFDD repos, and metadata carrying corpus_stats, baseline_replication, regression_results, matched_pairs_results,
  placebo_results, and success_criteria_verdict. Downstream paper-writing should present this as a rigorous null/scope-boundary
  result, not evidence the hypothesis is false.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **SPEND BUDGET**: at most $10 USD of OpenRouter API calls for this artifact. Nothing outside your own code enforces this — the key you are given has no per-artifact cap — so it holds only if you track cumulative cost after every call and stop when you approach it. Budget the work up front: estimate the per-call cost and the number of calls BEFORE starting a sweep, not after it overruns. Exceeding it spends real money that the run cannot recover.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Free-first web search (general + scholarly modes), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-concept-fig-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>
</available_resources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for evaluation metrics, agent orchestration patterns, benchmark design.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Use aii-json skill's format script with `--input eval_out.json` to generate full, mini, and preview versions. If not in your workspace (see <workspace> above), copy them there. Run 'ls -lh' to verify these three files exist (DO NOT read them).
TODO 2. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to eval_out.json and full_eval_out.json.
TODO 3. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "EvaluationExpectedFiles": {
      "description": "All expected output files from evaluation artifact.",
      "properties": {
        "script": {
          "description": "Path to eval.py script. Example: 'eval.py'",
          "title": "Script",
          "type": "string"
        },
        "full_output": {
          "description": "Full evaluation JSON file. Example: 'full_eval_out.json'",
          "title": "Full Output",
          "type": "string"
        },
        "mini_output": {
          "description": "Mini evaluation JSON file. Example: 'mini_eval_out.json'",
          "title": "Mini Output",
          "type": "string"
        },
        "preview_output": {
          "description": "Preview evaluation JSON file. Example: 'preview_eval_out.json'",
          "title": "Preview Output",
          "type": "string"
        }
      },
      "required": [
        "script",
        "full_output",
        "mini_output",
        "preview_output"
      ],
      "title": "EvaluationExpectedFiles",
      "type": "object"
    }
  },
  "description": "Evaluation artifact \u2014 structured output + file metadata.\n\nEvaluates both proposed and baseline methods with appropriate metrics.\nProduces eval.py and eval_out.json files.",
  "properties": {
    "title": {
      "default": "",
      "description": "Artifact title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); describe the content, not a status.",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "layman_summary": {
      "default": "",
      "description": "One-sentence plain-language summary of what this artifact does, accessible to non-experts. Used only in the per-artifact README, not in downstream prompts.",
      "maxLength": 250,
      "minLength": 80,
      "title": "Layman Summary",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Summary for downstream artifacts: what this artifact provides",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/EvaluationExpectedFiles",
      "description": "All output files you created. Must include eval.py script plus full/mini/preview evaluation JSON files."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "EvaluationArtifact",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [7] SYSTEM-USER prompt · 2026-08-21 18:48:07 UTC

```
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An artifact executor (Step 3.3: GEN_ART in the invention loop)

Executing a plan to produce a concrete artifact.
GEN_PAPER_TEXT will use your artifact in the next paper draft.

Rigorous artifact with clear results → strong paper. Sloppy artifact → misdirected research.
</your_role>
</ai_inventor_context>

<task>
Evaluate experimental results using domain-appropriate methods, metrics, and analysis techniques.
When in doubt, prefer more metrics over fewer — but only ones that make sense for the domain.
</task>

<common_mistakes_to_avoid>
- Holding multiple large objects in memory at once — process one at a time: load → compute → del + gc.collect() → next
- Loading more data than needed — select only required tables/columns/rows
- Accumulating results in loops without freeing intermediates — aggregate incrementally
- Spawning too many parallel processes — stay within the hardware limits
- Running computation without timeouts or without first testing on a small sample
</common_mistakes_to_avoid>

<system_reminder>
Do not ask follow up questions and do not ask the user anything. Execute all steps independently.
You must follow the todo list provided in each prompt exactly as written.
No placeholders, stubs, or incomplete code — all code must be complete and functional.
</system_reminder>

<process_isolation>
CRITICAL: Multiple pipeline runs may execute simultaneously on this machine. `ps aux | grep method.py` matches ALL runs, not just yours.
- NEVER kill processes by name (`killall`, `pkill -f`, `ps aux | grep ... | xargs kill`). This kills OTHER runs' processes.
- NEVER monitor processes by name (`ps aux | grep method.py`). You will see other runs' processes and get confused.
- ALWAYS use PID-based process management:
  Run: `uv run method.py & PID=$!` or `timeout <seconds> uv run method.py & PID=$!`
  Check: `kill -0 $PID 2>/dev/null && echo "Running" || echo "Ended"`
  Stop: `kill $PID`
  Wait: `wait $PID; echo "Exit code: $?"`
  Monitor: `tail -f logs/run.log & TAIL_PID=$!` then `kill $TAIL_PID` when done
</process_isolation>

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/file.py`, `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_evaluation_1_idx3
type: evaluation
title: Bootstrap CIs and Identity Spot-Check
summary: |-
  An evaluation artifact that adds statistical rigor to the founder-exit/survival experiment (art_eXxdnfS0o6aV): bootstrap 95% CIs on every reported Cohen's d snapshot-covariate effect size and on the placebo test's empirical percentile, plus a manual GitHub-profile spot-check of the identity/alias-resolution heuristic on a random 10-15 repo sample, consolidated into a single eval_out.json report that classifies each of the three pre-registered success criteria as tested-and-null, untestable-for-power, or now-resolved-by-CI.

  STEP 0 — Load and validate inputs.
  Read full_method_out.json from the dependency workspace (/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/full_method_out.json). Parse the per-repo `examples` array and the top-level `metadata` block, specifically: corpus_stats, baseline_replication, regression_results, matched_pairs_results, placebo_results, success_criteria_verdict. If any of these metadata keys is missing or empty, log a clear WARNING (not a silent skip) and mark that section's downstream analysis as 'INPUT_MISSING' in the final report rather than fabricating a number. Confirm the 24 TFDD repos with predict_our_method/predict_baseline_snapshot fields and the 30-repo usable analysis corpus are both present; record their exact counts at the top of the report so a reader can immediately see n for every subsequent statistic.

  STEP 1 — Bootstrap CIs on snapshot-covariate Cohen's d (resolves the MINOR scope critique).
  For each of the five snapshot covariates measured at TFDD (developers, commits, files, stars, forks), recover the two raw per-repo group samples (survivor vs non-survivor) that produced the originally reported Cohen's d, not just the scalar d itself — these should be reconstructable from the per-repo `examples` records using the survival label and the corresponding snapshot field. If raw per-repo values for a covariate are not present in method_out.json (e.g., d was computed but the underlying arrays were not persisted), state this explicitly as a data-availability limitation and either (a) reconstruct summary-based approximate CIs via Hedges/Cohen's d sampling-distribution formulas (using group n, d, and pooled SD if recoverable), clearly labeled 'analytic approximation, not resampled', or (b) mark that covariate's CI as NOT_COMPUTABLE_FROM_ARTIFACT — do not silently fall back to fabricated numbers.
  Where raw values ARE available: implement a nonparametric bootstrap with B=10,000 resamples (resample survivor and non-survivor groups independently, with replacement, at their original sizes; note that at n=30 with likely uneven group splits, this may leave one arm with single-digit n — flag any covariate where the smaller group's n<10 as LOW_RESOLUTION at the point it's reported, not buried in a footnote). For each resample, recompute Cohen's d = (mean1-mean2)/pooled_sd; take the 2.5th/97.5th percentiles of the resulting bootstrap distribution as the 95% CI. Fix a random seed for reproducibility and record it in the output.
  For every covariate, explicitly state whether Avelino et al.'s reported ESEM 2019 range (d=0.13 for files, d=0.25-0.26 for developers/commits; note stars/forks were not covariates Avelino et al. reported on file/dev/commit terms so treat those as this-study's own new covariates without an Avelino baseline to compare against — say so directly) falls INSIDE or OUTSIDE the newly bootstrapped 95% CI. Present this as a small table: covariate | n_survivor | n_nonsurvivor | point d | bootstrap 95% CI | Avelino reference value | inside/outside CI | resolution flag (adequate/low_resolution/not_computable).

  STEP 2 — Bootstrap CI on the placebo empirical percentile.
  The experiment's placebo test drew 200 null resamples of a randomly relocated 'pre-departure window' within each repo's own history and reported the true window's percentile rank among them (reported in the hypothesis text as 40th percentile with empirical p=0.615 at an earlier n=30 test — verify against the actual method_out.json placebo_results, which may differ slightly since this is the unified/reconciled corpus). To put a CI on that percentile rank itself: bootstrap-resample the 200 null-draw statistic values (or, if the raw 200 draws per repo are stored rather than one pooled null distribution, resample at the repo level first, then within-repo at the draw level, i.e. a two-stage/cluster bootstrap that respects the nesting) with B=10,000 resamples, and for each resample recompute where the true-window statistic falls as a percentile of that resampled null. Report the resulting 95% CI on the percentile. State explicitly whether this CI is wide enough to include both 'no signal' (~50th percentile) and 'some signal' (e.g. <25th or >75th percentile) — if so, say plainly that the placebo result cannot currently distinguish a true null from a weak real effect, rather than presenting the point estimate alone as if it settled the question.

  STEP 3 — Manual identity-resolution spot-check.
  From the 30-repo (or 46-prefiltered, whichever the experiment's REPO_LIST covers) unified corpus, deterministically sample 12 repos (fix a seed, e.g. numpy RandomState(42), and document the exact repo list and seed in the output so it's reproducible) stratified where possible across language/ecosystem to catch different noreply-email conventions (e.g. GitHub noreply patterns differ slightly by account age). For each sampled repo, using the aii-web-tools skill (web fetch + fetch_grep, NOT authenticated API calls — GitHub REST is rate-limited without a token and this must not require secrets), open the repo's GitHub commit history / contributors page and the founder's and 2-3 top non-founder contributors' public profile pages. Cross-check: (a) does the local alias-resolution heuristic's inferred founder identity match the actual first-committer/creator shown on GitHub; (b) do noreply-email-derived aliases the pipeline merged into one identity actually belong to the same GitHub account (spot check by following the noreply email pattern <id>+<username>@users.noreply.github.com back to the username, which is directly parseable without API calls); (c) are there any obviously-missed merges (same display name, different email, not merged) or over-merges (different people merged into one) visible from the commit list.
  Record for each of the 12 repos: PASS (identity resolution matches GitHub ground truth), ALIAS_MERGE_ERROR (specific description), or AMBIGUOUS (cannot determine from public page, e.g. private email commits). Compute an observed error rate = (ALIAS_MERGE_ERROR count) / 12, with a Wilson score 95% CI for this small-n proportion (do not use a naive normal-approximation CI at n=12). Report this as a concrete bound on the MINOR data-quality risk for the founder-only-TFDD qualification step, and explicitly discuss whether any detected errors would plausibly change founder identification or TF=1 status for that repo's event (which would be a more serious finding than a cosmetic alias miscount).

  STEP 4 — Consolidated verdict table (resolves the MAJOR framing critique).
  Build a single summary table classifying each of the three original pre-registered success criteria (matched-pairs survival-rate-ratio CI excluding 1x; BH-FDR-significant regression coefficients exceeding snapshot-covariate effect size; placebo/shuffle check showing weaker effect at relocated windows) into exactly one of: TESTED_NULL (ran to completion, produced a result distinguishable from chance, did not meet the pre-registered bar), TESTED_LOW_RESOLUTION (ran, but bootstrap CI from Step 1/2 is too wide to distinguish null from a real small-to-moderate effect), or UNTESTABLE_AT_SCALE (zero usable observations per stratification cell, as already documented in the experiment). Use the newly computed CIs to decide TESTED_NULL vs TESTED_LOW_RESOLUTION rather than asserting it. State the practical implication of each classification for what a future, larger-corpus iteration would need to change.

  STEP 5 — Output.
  Write eval_out.json conforming to the exp_eval_sol_out schema (validate with the aii-json skill before finishing): top-level metadata carrying corpus_stats (echoed from input), covariate_ci_table (from Step 1), placebo_ci (from Step 2), identity_spotcheck_results (from Step 3, including the Wilson CI and per-repo findings), and success_criteria_reclassification (from Step 4). Per-example entries (if the schema requires per-repo predictions) can simply echo the original experiment's predict_our_method/predict_baseline_snapshot fields unchanged, since this artifact evaluates existing results rather than generating new predictions. Run the aii-json skill's mini/preview generation. If any bootstrap or spot-check step could not be completed (e.g., raw per-covariate arrays genuinely absent from method_out.json), the final report must say so in plain language rather than omitting the covariate silently — a reader must be able to tell 'not computed because unavailable' from 'computed and small'.

  FAILURE MODES TO HANDLE: (1) If method_out.json's per-repo records lack raw covariate values needed for a true nonparametric bootstrap, fall back to the analytic Hedges'-d-CI formula (documented, e.g., in Cousineau & Goulet-Pelletier 2021, or standard Cohen's d sampling variance Var(d) ≈ (n1+n2)/(n1*n2) + d²/(2*(n1+n2))) and label results 'analytic, not resampled'. (2) If web fetch of a GitHub profile page is blocked, rate-limited, or the repo/user has since gone private, mark that repo AMBIGUOUS and swap in the next repo from the seeded sample list rather than silently shrinking n below 12 without saying so. (3) If the placebo null draws are stored only as a single pooled percentile with no underlying 200 raw values, state that a proper bootstrap CI is not reconstructable from the artifact as saved and report this as a concrete, named gap for the next experiment iteration to fix by persisting raw null-draw values.
runpod_compute_profile: gpu
metrics_descriptions: >-
  (1) Bootstrap 95% confidence intervals (B=10,000 resamples, seeded) on Cohen's d for each snapshot covariate (developers,
  commits, files, stars, forks) measured at the TFDD point, computed via nonparametric resampling of the raw per-repo survivor/non-survivor
  values where available, or an analytic Hedges'-d sampling-variance approximation where raw values cannot be recovered from
  the experiment artifact. (2) A bootstrap 95% CI on the placebo test's empirical percentile rank (the true pre-departure
  window's rank among 200 within-repo random-window null draws), using a two-stage cluster bootstrap if draws are nested per
  repo. (3) An observed identity/alias-resolution error rate from a manual 12-repo GitHub-profile spot-check, reported as
  a point estimate with a Wilson score 95% CI appropriate for small-n proportions, broken into PASS / ALIAS_MERGE_ERROR /
  AMBIGUOUS counts. (4) A three-way reclassification of the original pre-registered success criteria (TESTED_NULL, TESTED_LOW_RESOLUTION,
  UNTESTABLE_AT_SCALE) driven by whether the new CIs from (1)-(2) are narrow enough to distinguish a genuine null from a merely
  underpowered result.
metrics_justification: >-
  The hypothesis's own self-critique (from the prior iteration's reviewer) is that its central claim was tested at n=30 with
  no CIs on the reported effect sizes, so a scalar Cohen's d or a single percentile rank cannot on its own distinguish 'genuinely
  no effect' from 'too little data to tell' -- exactly the ambiguity the hypothesis text itself flags as the difference between
  a real null and an untested claim. Bootstrap CIs directly quantify that ambiguity: a CI that excludes Avelino et al.'s 0.13-0.26
  reference range supports treating the result as a genuine, resolvable null; a CI wide enough to contain both zero and a
  moderate effect supports the hypothesis's own honest downgrade to 'low-resolution, not falsified.' Putting a CI on the placebo
  percentile serves the same purpose for the one test that did run to completion -- it converts a single 40th-percentile point
  estimate into an interval that either does or does not rule out a real pre-departure signal. The identity spot-check targets
  a distinct, previously unverified risk: founder/authority disambiguation is a load-bearing step for the entire founder-only-TFDD
  qualification (misidentifying the founder or merging the wrong aliases could silently corrupt which events even qualify
  as TF=1 detachments), and no part of the original experiment validated this heuristic against ground truth. Measuring its
  error rate on a real sample turns a previously unquantified MINOR risk into a concrete, citable bound. Together these three
  measurements let the final report make the exact claim the hypothesis needs to make honestly: which of the three pre-registered
  criteria are actually resolved by current evidence versus which remain open only because of insufficient power -- precisely
  the MAJOR framing critique this artifact is scoped to close.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_eXxdnfS0o6aV
type: experiment
title: Founder Exit and Repo Survival
summary: >-
  Implements a full recomputation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship / Truck-Factor / Truck-Factor-Developer-Departure
  (TFDD) pipeline on real GitHub repositories, plus a new pre-departure authority-diffusion measurement and three analyses
  testing whether it predicts post-departure survival better than Avelino et al.'s null snapshot covariates. Because the upstream
  DATASET artifact this experiment depended on (gen_art_dataset_1) had an empty data_out/ at execution time, method.py is
  self-contained: it mines a curated corpus of 62 mature, well-known GitHub repositories (JavaScript, Python, Ruby, PHP, Java,
  C++, Go) directly via metadata-only blobless git clones plus the unauthenticated GitHub REST API, documented in REPO_LIST.
  For each repo it builds a chronological (author, file, timestamp) commit event log with GitHub-noreply-email alias resolution,
  computes the Fritz/Avelino DOA formula and greedy Truck-Factor at quarterly snapshots (monthly was infeasible at this compute
  budget; the fallback_plan sanctions quarterly resolution with a documented TFDD-date fuzz), identifies each repo's founder,
  and scans for the first TFDD where the truck-factor set is the founder alone and stays silent 12+ months, requiring >=12mo
  pre-history and >=18mo post-history. The new measurement computes founder commit-share and the count of distinct non-founder
  DOA file-owners in the 6-12mo pre-TFDD window. The outcome is an Active/Inactive/recovery model: binary survival = whether
  a new non-founder developer attains truck-factor status post-TFDD, plus a graded post/pre commit-velocity ratio. Confound
  controls recompute Avelino et al.'s own null snapshot covariates (stars, forks, contributor count, developers/commits/files
  at TFDD). Three analyses run: (a) standardized logistic + ordinal regression with BH-FDR correction; (b) matched-pairs nearest-neighbor
  bootstrap CI on the survival-rate ratio; (c) a within-repo random-window placebo test (200 null draws, reduced from 1000
  for CPU budget). Of 62 curated repos, 46 passed CONSORT-style prefilters and 30 yielded a usable founder-only TFDD with
  sufficient history, forming the analysis corpus. The result is a genuine, non-fabricated NULL finding: none of the three
  pre-registered success criteria were met (BH-adjusted p~0.77-0.81; diffusion coef did not exceed snapshot coef; placebo
  p did not clear 0.10) -- the fallback_plan treats this as a valid outcome, most plausibly due to reduced sample size (n=30)
  rather than a pipeline defect, since all pipeline stages executed and converged without error. Two documented deviations:
  (1) DL(a,f) uses the standard Fritz/Avelino textual definition without re-verifying against the ICPC 2016 paper text; (2)
  the source-file-fraction prefilter was relaxed from 0.60 to 0.40 after piloting showed 0.60 rejected most real repos. method.py
  writes method_out.json per the exp_gen_sol_out schema: one example per repo with full per-repo results, predict_our_method/predict_baseline_snapshot
  fields on the 24 TFDD repos, and metadata carrying corpus_stats, baseline_replication, regression_results, matched_pairs_results,
  placebo_results, and success_criteria_verdict. Downstream paper-writing should present this as a rigorous null/scope-boundary
  result, not evidence the hypothesis is false.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **SPEND BUDGET**: at most $10 USD of OpenRouter API calls for this artifact. Nothing outside your own code enforces this — the key you are given has no per-artifact cap — so it holds only if you track cumulative cost after every call and stop when you approach it. Budget the work up front: estimate the per-call cost and the number of calls BEFORE starting a sweep, not after it overruns. Exceeding it spends real money that the run cannot recover.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Free-first web search (general + scholarly modes), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-concept-fig-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>
</available_resources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for evaluation metrics, agent orchestration patterns, benchmark design.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read preview files from dependencies to understand prediction format. Evaluate ALL experiments provided — do not skip or select a subset. Avoid re-training or re-executing the method unless absolutely necessary; prefer loading predictions from each dependency's method_out.json / predict_* fields. Read domain handbook if applicable (see <available_domain_handbooks>). Decide evaluation metrics based on artifact plan. Test basic functionality with 'uv run'.
TODO 3. Fully implement evaluation as described in artifact plan in './eval.py'. Use exp_eval_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant metrics or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
```

### [8] HUMAN-USER prompt · 2026-08-21 18:48:07 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [9] SKILL-INPUT — aii-long-running-tasks · 2026-08-21 18:48:13 UTC

The agent loaded the **aii-long-running-tasks** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-long-running-tasks
description: "Scales an experiment or evaluation up in stages — mini, 10, 50, 100, 200, then the largest run that fits — recording runtime at each step and extrapolating time-per-example against the remaining time budget before growing further, with background execution and hard RLIMIT_AS and RLIMIT_CPU caps. ALWAYS read before launching any script expected to run for many minutes or hours over a dataset. Triggers: long-running job, overnight or unattended run, time budget, how many examples fit, extrapolate runtime, start small then scale up, run in background and poll, avoid a timeout, full-dataset evaluation, resource limits. NOT for choosing the concurrency mechanism itself (aii-parallel-computing), measuring the machine's CPU, RAM or GPU (aii-use-hardware), or provisioning cloud pods (aii-runpod)."
---

## Core Principles

1. **Time budget first**: Read your time/runtime constraints before running anything. Set every Bash timeout to fit within the budget.
2. **Start small, scale up**: Run on minimal input first, fix errors, then increase scale.
3. **Extrapolate before scaling**: Use recorded runtimes to predict whether the next step fits in the budget. Don't guess — calculate.
4. **Background execution**: For anything that takes >1 min, run in background (`run_in_background=true`) and do useful work while waiting.
5. **Stop early if needed**: Quality results on less data beats a timeout or crash. It's always acceptable to stop at a smaller scale.

---

## Gradual Scaling Sequence

Run code at increasing data sizes, checking runtime at each step.

Substitute your actual file names:
- `{mini_file}` — mini JSON (3 examples) from dependency workspace
- `{full_file}` — full dataset from dependency workspace
- `{script}` — your processing script (e.g., `./method.py`, `./eval.py`)
- `{schema}` — JSON schema to validate output against

**STEP 1 — MINI DATA:** Run `{script}` on `{mini_file}`. Do NOT truncate logs. Fix all errors. Validate output against `{schema}`. Verify you are NOT using mock scripts, mock data, or mock APIs.

**STEP 2 — 10 EXAMPLES:** Modify `{script}` to load only the first 10 examples from `{full_file}`. Run and fix errors. Validate schema. Record the runtime.

**STEP 3 — 50 EXAMPLES:** Load first 50 examples from `{full_file}`. Run and fix errors. Record runtime. **EXTRAPOLATE**: Using runtimes from steps 2-3, estimate time per example. Calculate how many examples fit in your remaining time budget. If 50 already used most of the budget, stop here.

**STEP 4 — 100 EXAMPLES (if budget allows):** Load first 100 examples. Run and fix errors. Record runtime. Re-extrapolate with the new data point.

**STEP 5 — 200 EXAMPLES (if budget allows):** Load first 200 examples from `{full_file}`. Run and fix errors. Record runtime.

**STEP 6 — MAXIMIZE:** Using all recorded runtimes, extrapolate time-per-example (it may not be perfectly linear — account for overhead). Calculate the maximum number of examples that fits within your remaining time budget with a 10% safety margin. Load that many (or all if they fit). Run and validate.

## Final Testing Phase

After completing the scaling sequence, redo the entire sequence **one more time** up to your final example count:

mini → 10 → 50 → 100 → 200 → max

At each scale: look for issues, fix problems, validate output, ensure it completes within time limits.

---

## Background Execution

For any step that takes >1 min, run as a **background task**:

1. Launch with Bash `run_in_background=true`
2. While it runs, use the time productively:
   - Sanity-check previous outputs
   - Verify file integrity (correct field names, non-empty values)
   - Review code for edge cases at larger scale
   - Prepare the next step
3. Check back on the background task to get results
4. If it failed, fix errors and re-run

---

## Resource Limits

Set hard RAM and CPU time limits so code fails fast instead of crashing the system. Read limits from `<hardware>` and leave headroom for the OS (e.g., if 16GB total, cap at 14GB).

Python example using stdlib `resource` module:
```python
import resource
resource.setrlimit(resource.RLIMIT_AS, (14 * 1024**3, 14 * 1024**3))  # 14GB RAM
resource.setrlimit(resource.RLIMIT_CPU, (3600, 3600))  # 1 hour CPU time
```
Exceeding RAM raises `MemoryError`. Exceeding CPU time sends `SIGKILL`.

## Monitoring

At each step, record runtime AND check resource usage (`free -h` for RAM, `top -bn1 | head -5` for CPU). If memory usage is climbing toward the limit or CPU is pegged, stop and investigate before scaling further.
````

### [10] SKILL-INPUT — aii-file-size-limit · 2026-08-21 18:48:13 UTC

The agent loaded the **aii-file-size-limit** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

```
---
name: aii-file-size-limit
description: "Splits an oversized generated output file into numbered parts that each fit a size limit: checks sizes with ls -lh, writes full_data_out_1.json, full_data_out_2.json and so on into a matching directory, deletes the original, repoints the reading code at a sorted glob, and regenerates mini and preview variants per part. ALWAYS run right after a script writes JSON output, and whenever a file is too big to keep, exceeds a stated file size limit, or gets rejected for its size. Triggers: file too large, output exceeds the size limit, oversized or huge JSON, ls -lh size check after generating results, splitting or chunking an output file into parts, output directory instead of one file. NOT for: schema validation or making mini and preview variants of a file already within the limit (use aii-json), or general Python script conventions (use aii-python)."
---

## File Size Check

After generating output files, run `ls -lh` to check sizes. If ANY file exceeds the provided file size limit:

1. Create directory with same base name (e.g., `data_out/` for `full_data_out.json`)
2. Split into parts under the limit named: `full_data_out_1.json`, `full_data_out_2.json`, etc.
3. Place parts in directory (e.g., `data_out/full_data_out_1.json`, `data_out/full_data_out_2.json`)
4. Delete the original oversized file
5. Update the script to read from split files: `for f in sorted(glob.glob('data_out/full_data_out_*.json')): data.extend(json.load(open(f)))`
6. For each split part, generate its own mini/preview versions with the json skill's format script
```

### [11] SKILL-INPUT — aii-use-hardware · 2026-08-21 18:48:13 UTC

The agent loaded the **aii-use-hardware** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-use-hardware
description: "Detects the CPU, RAM, GPU and VRAM actually available — cgroup v1 and v2 container quotas and CPU affinity rather than misleading host values — then sets RAM and VRAM budgets via resource.setrlimit and torch.cuda.set_per_process_memory_fraction so a script raises a catchable error instead of being OOM-killed, and picks the right torch wheel for the detected device. ALWAYS read before loading a large dataset, installing torch, or sizing batches and worker counts. Triggers: how much RAM or CPU or GPU is available, container memory limit, cgroup, OOM killed, MemoryError, os.cpu_count reports host cores, nproc, VRAM, CUDA available, CPU-only torch build, dataset too big for memory, chunking. NOT for spreading work across that hardware once measured (aii-parallel-computing), staged scale-up runs against a time budget (aii-long-running-tasks), or renting cloud machines (aii-runpod)."
---

**Step 1** — Run `bash scripts/get_hardware.sh` (relative to this skill's directory).

Read the `=== CGROUP ===` section carefully. If `Type: cgroup v1` or `cgroup v2`:
- You are in a **container with hard resource limits**. Exceeding them = OOM kill, no recovery.
- **Never** use `psutil.virtual_memory().total`, `free -h`, `/proc/meminfo`, `os.cpu_count()`, or `nproc` for resource limits — these report **host** values, not your container's allocation.
- **Always** read limits from the cgroup paths shown in the output, or use the Python helpers below.
- For **runtime memory monitoring**, read current usage from cgroup too:
  - v2: `/sys/fs/cgroup/memory.current`
  - v1: `/sys/fs/cgroup/memory/memory.usage_in_bytes`

**Step 2** — Use Step 1 results to pick package variants **before** installing.

Defaults often target the most powerful environment — PyPI's `torch` ships with CUDA libs even on CPU-only hosts. Wrong variant = wasted disk, slow setup, possible import-time failures.

If `=== GPU ===` shows `No GPU`, install torch's CPU build (skips ~4.5GB of CUDA libs):
```bash
uv pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
```
Same idea for any library whose wheel selection depends on detected hardware (GPU/CPU-only builds, architecture-specific wheels).

After install, sanity-check imports right away (`python -c "import torch"`). Disk-pressure or interrupted installs leave half-built wheels (e.g. `libtorch_global_deps.so` missing) — catch these before the experiment runs.

**Step 3** — Set Python constants from the Step 1 results:
```python
import os, math, torch, psutil
from pathlib import Path

def _detect_cpus() -> int:
    """Detect actual CPU allocation (containers/pods/bare metal)."""
    try:  # cgroups v2 quota
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except (FileNotFoundError, ValueError): pass
    try:  # cgroups v1 quota
        q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
        p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
        if q > 0:
            return math.ceil(q / p)
    except (FileNotFoundError, ValueError): pass
    try:  # CPU affinity (cpuset — used by RunPod, Docker --cpuset-cpus)
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError): pass
    return os.cpu_count() or 1

def _container_ram_gb() -> float | None:
    """Read RAM limit from cgroup (containers/pods)."""
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError): pass
    return None

NUM_CPUS = _detect_cpus()
HAS_GPU = torch.cuda.is_available()
VRAM_GB = torch.cuda.get_device_properties(0).total_mem / 1e9 if HAS_GPU else 0
DEVICE = torch.device("cuda" if HAS_GPU else "cpu")
TOTAL_RAM_GB = _container_ram_gb() or psutil.virtual_memory().total / 1e9
AVAILABLE_RAM_GB = min(psutil.virtual_memory().available / 1e9, TOTAL_RAM_GB)
```

## Step 4 — Set Memory Limits

OOM kills the entire container. **Every script MUST set RAM and VRAM limits at startup.**

Decide the budget based on what the script actually needs. Estimate data size × 2-5x for in-memory overhead, then add ~50% breathing room for temporaries. You may use up to 90% of available RAM/VRAM, but **scale gradually** — start small (e.g. 30-50%), verify it works, then increase toward the limit. Never exceed 90% to keep a buffer for the OS, system processes, and the agent runtime itself. Going over crashes the container/machine with no recovery.

```python
import resource, psutil

_avail = psutil.virtual_memory().available
RAM_BUDGET = ???  # YOU decide: estimate what this script needs (in bytes)
assert RAM_BUDGET < _avail, f"Budget {RAM_BUDGET/1e9:.1f}GB > available {_avail/1e9:.1f}GB"
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))  # 3x: virtual > RSS; raises MemoryError on exceed

if HAS_GPU:
    _free, _total = torch.cuda.mem_get_info(0)
    VRAM_BUDGET = ???  # YOU decide: estimate GPU memory needs
    torch.cuda.set_per_process_memory_fraction(min(VRAM_BUDGET / _total, 0.95))  # raises OutOfMemoryError on exceed
```

## Memory-Safe Data Processing

- **One at a time**: load one large object → process → `del obj; gc.collect()` → next
- **Load only what you need**: select specific tables/columns/rows, not entire databases
- **Test small first**: run on a sample before scaling to full data to estimate memory/time
- **Free intermediates in loops**: don't accumulate large results — aggregate incrementally
- **Size before loading**: check file/dataset size before loading; if it's >30% of `RAM_BUDGET`, chunk it

## Common Mistakes (from real crashes)

- **Skipping this skill entirely** — loading data with no RAM detection, no limits, no budget. Container OOM-killed, all agents lost.
- **Using `psutil.virtual_memory().total` instead of `_container_ram_gb()`** — reports host RAM (e.g. 66 GB) when container limit is 28 GB. You MUST use the cgroup-aware functions above.
- **Loading all tables from a multi-table database at once** — one agent loaded 14 RelBench tables simultaneously, spiked past container limit.
- **Setting no memory limits** — without `resource.setrlimit` (RAM) and `set_per_process_memory_fraction` (VRAM), a runaway script OOM-kills the container instead of raising a catchable error.
- **Using `os.cpu_count()` directly** — returns host CPUs (e.g. 192) instead of container limit (e.g. 4) on RunPod/Docker. Always use `_detect_cpus()` above which checks cgroup quota → CPU affinity → `os.cpu_count()` in order.

## Hardware Use

- Keep these results in mind for ALL subsequent tasks — don't assume more than detected
- GPU if available and parallelizable, multiprocessing if multiple CPUs
- Push available resources to their full potential — don't leave hardware idle
````

### [12] SKILL-INPUT — aii-parallel-computing · 2026-08-21 18:48:13 UTC

The agent loaded the **aii-parallel-computing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-parallel-computing
description: "Parallelises compute-heavy Python: asyncio with aiohttp and a bounded Semaphore for I/O-bound work, ProcessPoolExecutor under the spawn start method for CPU-bound work, NumPy vectorisation and batched PyTorch on GPU with an out-of-memory halving fallback. ALWAYS read before writing any script that loops over data, issues many API calls, downloads many files, or runs heavy computation — sequential loops are the default failure mode. Triggers: parallelise, make a slow script faster, concurrency, async, aiohttp, asyncio.gather, semaphore, multiprocessing, ProcessPoolExecutor, fork deadlock with loguru, worker count, batch size, CUDA out of memory, idle GPU, retries and rate limits. NOT for detecting what hardware exists or setting RAM and VRAM budgets (aii-use-hardware), staged scale-up against a time budget (aii-long-running-tasks), or provisioning cloud pods (aii-runpod)."
---

**ALWAYS parallelize. Sequential processing is unacceptable for any non-trivial workload.** A sequential script doing 1000 API calls takes hours and fails halfway. An async version finishes in minutes with proper error handling. ALWAYS ask: "Can this run in parallel?" — the answer is almost always yes.

Read aii-use-hardware skill first → get `NUM_CPUS`, `HAS_GPU`, `VRAM_GB`, `device`. Set `NUM_WORKERS` proportional to available CPU capacity — check `psutil.cpu_percent(interval=1)` and scale accordingly (e.g. 30% used → use ~70% of cores).

## Decision Tree (follow strictly)

- **I/O-bound** (API calls, downloads, web, file reads) → `asyncio` + `aiohttp` with `Semaphore(NUM_WORKERS * 4)`. NEVER do sequential HTTP requests in a loop.
- **CPU-bound, vectorizable** → GPU available: PyTorch on device / No GPU: NumPy vectorized ops. NEVER loop over array elements in Python.
- **CPU-bound, independent items** → `ProcessPoolExecutor(max_workers=NUM_WORKERS)`. NEVER process items one-by-one when they're independent.
- **Sequential** → only acceptable when items have data dependencies (each depends on the previous result).

## GPU Rules

- Use up to 90% of available VRAM — scale gradually (start small, increase after each successful run, keep 10% buffer)
- Move to device → compute → move back: `torch.tensor(data, device=device)` → `.cpu().numpy()`
- OOM fallback: catch `torch.cuda.OutOfMemoryError` → `empty_cache()` → halve batch size → retry on GPU. Keep reducing until it fits. Stay on GPU.
- Batch large data: chunk it, `del batch` between iterations to free VRAM

## Parallelism Rules

- **CPU-bound**: `ProcessPoolExecutor` + `as_completed`, pre-allocate result list indexed by submission order
- **I/O-bound**: `asyncio` + `aiohttp`, `Semaphore(NUM_WORKERS * 4)`, single shared `ClientSession`, `asyncio.gather(*tasks, return_exceptions=True)`
- Always add `tenacity` retries for transient failures, always set timeouts on HTTP requests
- **CRITICAL — `ProcessPoolExecutor` start method**: Default `fork` deadlocks with loguru (and any threading library). ALWAYS pass `mp_context=multiprocessing.get_context("spawn")` when constructing `ProcessPoolExecutor` in any script that uses loguru, threading, or async I/O. Example:
  ```python
  import multiprocessing as mp
  from concurrent.futures import ProcessPoolExecutor
  with ProcessPoolExecutor(max_workers=N, mp_context=mp.get_context("spawn")) as pool:
      ...
  ```
````

### [13] SYSTEM-USER prompt · 2026-08-21 18:49:17 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/file.py`, `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_evaluation_1_idx3
type: evaluation
title: Bootstrap CIs and Identity Spot-Check
summary: |-
  An evaluation artifact that adds statistical rigor to the founder-exit/survival experiment (art_eXxdnfS0o6aV): bootstrap 95% CIs on every reported Cohen's d snapshot-covariate effect size and on the placebo test's empirical percentile, plus a manual GitHub-profile spot-check of the identity/alias-resolution heuristic on a random 10-15 repo sample, consolidated into a single eval_out.json report that classifies each of the three pre-registered success criteria as tested-and-null, untestable-for-power, or now-resolved-by-CI.

  STEP 0 — Load and validate inputs.
  Read full_method_out.json from the dependency workspace (/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/full_method_out.json). Parse the per-repo `examples` array and the top-level `metadata` block, specifically: corpus_stats, baseline_replication, regression_results, matched_pairs_results, placebo_results, success_criteria_verdict. If any of these metadata keys is missing or empty, log a clear WARNING (not a silent skip) and mark that section's downstream analysis as 'INPUT_MISSING' in the final report rather than fabricating a number. Confirm the 24 TFDD repos with predict_our_method/predict_baseline_snapshot fields and the 30-repo usable analysis corpus are both present; record their exact counts at the top of the report so a reader can immediately see n for every subsequent statistic.

  STEP 1 — Bootstrap CIs on snapshot-covariate Cohen's d (resolves the MINOR scope critique).
  For each of the five snapshot covariates measured at TFDD (developers, commits, files, stars, forks), recover the two raw per-repo group samples (survivor vs non-survivor) that produced the originally reported Cohen's d, not just the scalar d itself — these should be reconstructable from the per-repo `examples` records using the survival label and the corresponding snapshot field. If raw per-repo values for a covariate are not present in method_out.json (e.g., d was computed but the underlying arrays were not persisted), state this explicitly as a data-availability limitation and either (a) reconstruct summary-based approximate CIs via Hedges/Cohen's d sampling-distribution formulas (using group n, d, and pooled SD if recoverable), clearly labeled 'analytic approximation, not resampled', or (b) mark that covariate's CI as NOT_COMPUTABLE_FROM_ARTIFACT — do not silently fall back to fabricated numbers.
  Where raw values ARE available: implement a nonparametric bootstrap with B=10,000 resamples (resample survivor and non-survivor groups independently, with replacement, at their original sizes; note that at n=30 with likely uneven group splits, this may leave one arm with single-digit n — flag any covariate where the smaller group's n<10 as LOW_RESOLUTION at the point it's reported, not buried in a footnote). For each resample, recompute Cohen's d = (mean1-mean2)/pooled_sd; take the 2.5th/97.5th percentiles of the resulting bootstrap distribution as the 95% CI. Fix a random seed for reproducibility and record it in the output.
  For every covariate, explicitly state whether Avelino et al.'s reported ESEM 2019 range (d=0.13 for files, d=0.25-0.26 for developers/commits; note stars/forks were not covariates Avelino et al. reported on file/dev/commit terms so treat those as this-study's own new covariates without an Avelino baseline to compare against — say so directly) falls INSIDE or OUTSIDE the newly bootstrapped 95% CI. Present this as a small table: covariate | n_survivor | n_nonsurvivor | point d | bootstrap 95% CI | Avelino reference value | inside/outside CI | resolution flag (adequate/low_resolution/not_computable).

  STEP 2 — Bootstrap CI on the placebo empirical percentile.
  The experiment's placebo test drew 200 null resamples of a randomly relocated 'pre-departure window' within each repo's own history and reported the true window's percentile rank among them (reported in the hypothesis text as 40th percentile with empirical p=0.615 at an earlier n=30 test — verify against the actual method_out.json placebo_results, which may differ slightly since this is the unified/reconciled corpus). To put a CI on that percentile rank itself: bootstrap-resample the 200 null-draw statistic values (or, if the raw 200 draws per repo are stored rather than one pooled null distribution, resample at the repo level first, then within-repo at the draw level, i.e. a two-stage/cluster bootstrap that respects the nesting) with B=10,000 resamples, and for each resample recompute where the true-window statistic falls as a percentile of that resampled null. Report the resulting 95% CI on the percentile. State explicitly whether this CI is wide enough to include both 'no signal' (~50th percentile) and 'some signal' (e.g. <25th or >75th percentile) — if so, say plainly that the placebo result cannot currently distinguish a true null from a weak real effect, rather than presenting the point estimate alone as if it settled the question.

  STEP 3 — Manual identity-resolution spot-check.
  From the 30-repo (or 46-prefiltered, whichever the experiment's REPO_LIST covers) unified corpus, deterministically sample 12 repos (fix a seed, e.g. numpy RandomState(42), and document the exact repo list and seed in the output so it's reproducible) stratified where possible across language/ecosystem to catch different noreply-email conventions (e.g. GitHub noreply patterns differ slightly by account age). For each sampled repo, using the aii-web-tools skill (web fetch + fetch_grep, NOT authenticated API calls — GitHub REST is rate-limited without a token and this must not require secrets), open the repo's GitHub commit history / contributors page and the founder's and 2-3 top non-founder contributors' public profile pages. Cross-check: (a) does the local alias-resolution heuristic's inferred founder identity match the actual first-committer/creator shown on GitHub; (b) do noreply-email-derived aliases the pipeline merged into one identity actually belong to the same GitHub account (spot check by following the noreply email pattern <id>+<username>@users.noreply.github.com back to the username, which is directly parseable without API calls); (c) are there any obviously-missed merges (same display name, different email, not merged) or over-merges (different people merged into one) visible from the commit list.
  Record for each of the 12 repos: PASS (identity resolution matches GitHub ground truth), ALIAS_MERGE_ERROR (specific description), or AMBIGUOUS (cannot determine from public page, e.g. private email commits). Compute an observed error rate = (ALIAS_MERGE_ERROR count) / 12, with a Wilson score 95% CI for this small-n proportion (do not use a naive normal-approximation CI at n=12). Report this as a concrete bound on the MINOR data-quality risk for the founder-only-TFDD qualification step, and explicitly discuss whether any detected errors would plausibly change founder identification or TF=1 status for that repo's event (which would be a more serious finding than a cosmetic alias miscount).

  STEP 4 — Consolidated verdict table (resolves the MAJOR framing critique).
  Build a single summary table classifying each of the three original pre-registered success criteria (matched-pairs survival-rate-ratio CI excluding 1x; BH-FDR-significant regression coefficients exceeding snapshot-covariate effect size; placebo/shuffle check showing weaker effect at relocated windows) into exactly one of: TESTED_NULL (ran to completion, produced a result distinguishable from chance, did not meet the pre-registered bar), TESTED_LOW_RESOLUTION (ran, but bootstrap CI from Step 1/2 is too wide to distinguish null from a real small-to-moderate effect), or UNTESTABLE_AT_SCALE (zero usable observations per stratification cell, as already documented in the experiment). Use the newly computed CIs to decide TESTED_NULL vs TESTED_LOW_RESOLUTION rather than asserting it. State the practical implication of each classification for what a future, larger-corpus iteration would need to change.

  STEP 5 — Output.
  Write eval_out.json conforming to the exp_eval_sol_out schema (validate with the aii-json skill before finishing): top-level metadata carrying corpus_stats (echoed from input), covariate_ci_table (from Step 1), placebo_ci (from Step 2), identity_spotcheck_results (from Step 3, including the Wilson CI and per-repo findings), and success_criteria_reclassification (from Step 4). Per-example entries (if the schema requires per-repo predictions) can simply echo the original experiment's predict_our_method/predict_baseline_snapshot fields unchanged, since this artifact evaluates existing results rather than generating new predictions. Run the aii-json skill's mini/preview generation. If any bootstrap or spot-check step could not be completed (e.g., raw per-covariate arrays genuinely absent from method_out.json), the final report must say so in plain language rather than omitting the covariate silently — a reader must be able to tell 'not computed because unavailable' from 'computed and small'.

  FAILURE MODES TO HANDLE: (1) If method_out.json's per-repo records lack raw covariate values needed for a true nonparametric bootstrap, fall back to the analytic Hedges'-d-CI formula (documented, e.g., in Cousineau & Goulet-Pelletier 2021, or standard Cohen's d sampling variance Var(d) ≈ (n1+n2)/(n1*n2) + d²/(2*(n1+n2))) and label results 'analytic, not resampled'. (2) If web fetch of a GitHub profile page is blocked, rate-limited, or the repo/user has since gone private, mark that repo AMBIGUOUS and swap in the next repo from the seeded sample list rather than silently shrinking n below 12 without saying so. (3) If the placebo null draws are stored only as a single pooled percentile with no underlying 200 raw values, state that a proper bootstrap CI is not reconstructable from the artifact as saved and report this as a concrete, named gap for the next experiment iteration to fix by persisting raw null-draw values.
runpod_compute_profile: gpu
metrics_descriptions: >-
  (1) Bootstrap 95% confidence intervals (B=10,000 resamples, seeded) on Cohen's d for each snapshot covariate (developers,
  commits, files, stars, forks) measured at the TFDD point, computed via nonparametric resampling of the raw per-repo survivor/non-survivor
  values where available, or an analytic Hedges'-d sampling-variance approximation where raw values cannot be recovered from
  the experiment artifact. (2) A bootstrap 95% CI on the placebo test's empirical percentile rank (the true pre-departure
  window's rank among 200 within-repo random-window null draws), using a two-stage cluster bootstrap if draws are nested per
  repo. (3) An observed identity/alias-resolution error rate from a manual 12-repo GitHub-profile spot-check, reported as
  a point estimate with a Wilson score 95% CI appropriate for small-n proportions, broken into PASS / ALIAS_MERGE_ERROR /
  AMBIGUOUS counts. (4) A three-way reclassification of the original pre-registered success criteria (TESTED_NULL, TESTED_LOW_RESOLUTION,
  UNTESTABLE_AT_SCALE) driven by whether the new CIs from (1)-(2) are narrow enough to distinguish a genuine null from a merely
  underpowered result.
metrics_justification: >-
  The hypothesis's own self-critique (from the prior iteration's reviewer) is that its central claim was tested at n=30 with
  no CIs on the reported effect sizes, so a scalar Cohen's d or a single percentile rank cannot on its own distinguish 'genuinely
  no effect' from 'too little data to tell' -- exactly the ambiguity the hypothesis text itself flags as the difference between
  a real null and an untested claim. Bootstrap CIs directly quantify that ambiguity: a CI that excludes Avelino et al.'s 0.13-0.26
  reference range supports treating the result as a genuine, resolvable null; a CI wide enough to contain both zero and a
  moderate effect supports the hypothesis's own honest downgrade to 'low-resolution, not falsified.' Putting a CI on the placebo
  percentile serves the same purpose for the one test that did run to completion -- it converts a single 40th-percentile point
  estimate into an interval that either does or does not rule out a real pre-departure signal. The identity spot-check targets
  a distinct, previously unverified risk: founder/authority disambiguation is a load-bearing step for the entire founder-only-TFDD
  qualification (misidentifying the founder or merging the wrong aliases could silently corrupt which events even qualify
  as TF=1 detachments), and no part of the original experiment validated this heuristic against ground truth. Measuring its
  error rate on a real sample turns a previously unquantified MINOR risk into a concrete, citable bound. Together these three
  measurements let the final report make the exact claim the hypothesis needs to make honestly: which of the three pre-registered
  criteria are actually resolved by current evidence versus which remain open only because of insufficient power -- precisely
  the MAJOR framing critique this artifact is scoped to close.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_eXxdnfS0o6aV
type: experiment
title: Founder Exit and Repo Survival
summary: >-
  Implements a full recomputation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship / Truck-Factor / Truck-Factor-Developer-Departure
  (TFDD) pipeline on real GitHub repositories, plus a new pre-departure authority-diffusion measurement and three analyses
  testing whether it predicts post-departure survival better than Avelino et al.'s null snapshot covariates. Because the upstream
  DATASET artifact this experiment depended on (gen_art_dataset_1) had an empty data_out/ at execution time, method.py is
  self-contained: it mines a curated corpus of 62 mature, well-known GitHub repositories (JavaScript, Python, Ruby, PHP, Java,
  C++, Go) directly via metadata-only blobless git clones plus the unauthenticated GitHub REST API, documented in REPO_LIST.
  For each repo it builds a chronological (author, file, timestamp) commit event log with GitHub-noreply-email alias resolution,
  computes the Fritz/Avelino DOA formula and greedy Truck-Factor at quarterly snapshots (monthly was infeasible at this compute
  budget; the fallback_plan sanctions quarterly resolution with a documented TFDD-date fuzz), identifies each repo's founder,
  and scans for the first TFDD where the truck-factor set is the founder alone and stays silent 12+ months, requiring >=12mo
  pre-history and >=18mo post-history. The new measurement computes founder commit-share and the count of distinct non-founder
  DOA file-owners in the 6-12mo pre-TFDD window. The outcome is an Active/Inactive/recovery model: binary survival = whether
  a new non-founder developer attains truck-factor status post-TFDD, plus a graded post/pre commit-velocity ratio. Confound
  controls recompute Avelino et al.'s own null snapshot covariates (stars, forks, contributor count, developers/commits/files
  at TFDD). Three analyses run: (a) standardized logistic + ordinal regression with BH-FDR correction; (b) matched-pairs nearest-neighbor
  bootstrap CI on the survival-rate ratio; (c) a within-repo random-window placebo test (200 null draws, reduced from 1000
  for CPU budget). Of 62 curated repos, 46 passed CONSORT-style prefilters and 30 yielded a usable founder-only TFDD with
  sufficient history, forming the analysis corpus. The result is a genuine, non-fabricated NULL finding: none of the three
  pre-registered success criteria were met (BH-adjusted p~0.77-0.81; diffusion coef did not exceed snapshot coef; placebo
  p did not clear 0.10) -- the fallback_plan treats this as a valid outcome, most plausibly due to reduced sample size (n=30)
  rather than a pipeline defect, since all pipeline stages executed and converged without error. Two documented deviations:
  (1) DL(a,f) uses the standard Fritz/Avelino textual definition without re-verifying against the ICPC 2016 paper text; (2)
  the source-file-fraction prefilter was relaxed from 0.60 to 0.40 after piloting showed 0.60 rejected most real repos. method.py
  writes method_out.json per the exp_gen_sol_out schema: one example per repo with full per-repo results, predict_our_method/predict_baseline_snapshot
  fields on the 24 TFDD repos, and metadata carrying corpus_stats, baseline_replication, regression_results, matched_pairs_results,
  placebo_results, and success_criteria_verdict. Downstream paper-writing should present this as a rigorous null/scope-boundary
  result, not evidence the hypothesis is false.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **SPEND BUDGET**: at most $10 USD of OpenRouter API calls for this artifact. Nothing outside your own code enforces this — the key you are given has no per-artifact cap — so it holds only if you track cumulative cost after every call and stop when you approach it. Budget the work up front: estimate the per-call cost and the number of calls BEFORE starting a sweep, not after it overruns. Exceeding it spends real money that the run cannot recover.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Free-first web search (general + scholarly modes), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-concept-fig-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>
</available_resources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for evaluation metrics, agent orchestration patterns, benchmark design.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Use aii-json skill's format script with `--input eval_out.json` to generate full, mini, and preview versions. If not in your workspace (see <workspace> above), copy them there. Run 'ls -lh' to verify these three files exist (DO NOT read them).
TODO 2. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to eval_out.json and full_eval_out.json.
TODO 3. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "EvaluationExpectedFiles": {
      "description": "All expected output files from evaluation artifact.",
      "properties": {
        "script": {
          "description": "Path to eval.py script. Example: 'eval.py'",
          "title": "Script",
          "type": "string"
        },
        "full_output": {
          "description": "Full evaluation JSON file. Example: 'full_eval_out.json'",
          "title": "Full Output",
          "type": "string"
        },
        "mini_output": {
          "description": "Mini evaluation JSON file. Example: 'mini_eval_out.json'",
          "title": "Mini Output",
          "type": "string"
        },
        "preview_output": {
          "description": "Preview evaluation JSON file. Example: 'preview_eval_out.json'",
          "title": "Preview Output",
          "type": "string"
        }
      },
      "required": [
        "script",
        "full_output",
        "mini_output",
        "preview_output"
      ],
      "title": "EvaluationExpectedFiles",
      "type": "object"
    }
  },
  "description": "Evaluation artifact \u2014 structured output + file metadata.\n\nEvaluates both proposed and baseline methods with appropriate metrics.\nProduces eval.py and eval_out.json files.",
  "properties": {
    "title": {
      "default": "",
      "description": "Artifact title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); describe the content, not a status.",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "layman_summary": {
      "default": "",
      "description": "One-sentence plain-language summary of what this artifact does, accessible to non-experts. Used only in the per-artifact README, not in downstream prompts.",
      "maxLength": 250,
      "minLength": 80,
      "title": "Layman Summary",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Summary for downstream artifacts: what this artifact provides",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/EvaluationExpectedFiles",
      "description": "All output files you created. Must include eval.py script plus full/mini/preview evaluation JSON files."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "EvaluationArtifact",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````
