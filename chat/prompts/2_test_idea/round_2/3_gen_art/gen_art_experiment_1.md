# gen_art_experiment_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `iter1_0b7b616dce39` — Does Pre-Departure Authority Diffusion Predict Open-Source Project Survival? A Unified-Corpus Retest with a Window-Boundary-Noise Control
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_1` (terminal_claude_agent)

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

<research_methodology>
Design experiments like a researcher, not a programmer running a script.

- Every method needs a meaningful baseline — the current standard approach, not a strawman.
- Control your variables. When comparing methods, hold everything else constant.
- Results need variance, not just point estimates. A single run proves nothing.
- Implement the proposed method and baseline side-by-side in the same pipeline to eliminate implementation-level confounds.
</research_methodology>

<task>
Implement the research methodology as a production-ready experimental system.
Adapt your implementation approach based on the hypothesis and domain requirements.
</task>

<critical_requirements>
- Fully implement the methodology described in hypothesis
- Use appropriate frameworks based on research domain
- Load and process data from the specified data_filepath
- Complete working systems
- Handle all edge cases, errors, and exceptions properly
- Always implement baseline comparison method
</critical_requirements>

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
Your workspace: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx2
type: experiment
title: Unified-Corpus Re-Test of Pre-Departure Authority Diffusion
summary: >-
  Re-run the three pre-registered tests (BH-FDR regression, matched-pairs bootstrap, within-repo placebo at >=200 draws) on
  the single unified 32-repo dataset artifact instead of independently re-mined data, and add a new window-boundary-noise
  control using non-TFDD repos to separate measurement noise from genuine signal.
runpod_compute_profile: gpu
implementation_pseudocode: |-
  # method.py

  ## 0. Setup
  - load full_data_out.json from dataset dependency (art_24Q1bYB_ULpu), group 'founder_departure_tfdd_corpus'
  - parse each row's `input` JSON string -> covariates dict; `output` -> survival label (Active_survived / Inactive_did_not_survive)
  - parse metadata_* fields -> per-year DOA/TF developer-set tables, TFDD date/developer, pre-TFDD window details, post-TFDD monthly commit series, repo identity/stars/language/license
  - log n=32 total rows, breakdown by language (Go7/Ruby11/JS6/Java5/Rust3) and outcome (20 survived/12 not)
  - if n < 32 or schema mismatch vs dataset summary -> hard fail loudly (do NOT silently drop rows) since corpus-provenance unification is the whole point of this iteration

  ## 1. Baseline replication checks (compare against Avelino et al. and dataset artifact summary)
  - founder-only-TFDD rate in corpus (sanity: should match the 32/216 mining yield already reported)
  - survival rate = 20/32 = 62.5% -> report alongside Avelino et al.'s unconditioned 41% baseline (note directionally different denominator: this is founder-only-TF=1 TFDDs, not all TFDDs)
  - snapshot Cohen's d for developers/commits/files between survivors and non-survivors AT the TFDD year (using existing per-year DOA/TF tables in metadata) -> replicate Avelino et al.'s d=0.13-0.26 negligible-small finding on this corpus as a validity check

  ## 2. Core covariates (reuse from method.py in prior iteration's experiment artifact if available in workspace context; otherwise recompute from metadata fields already present in dataset -- do NOT re-clone/re-mine)
  - founder_pre_departure_commit_share (6-12mo window before TFDD)
  - n_new_nonfounder_doa_owners (distinct accounts reaching DOA-primary file ownership in that window)
  - controls: stars, forks, contributor_count, language (categorical), license (categorical), project_age_days, total_commits, total_files, history_span_days

  ## 3. Test A: BH-FDR logistic + ordinal regression
  - outcome: survival (binary Active_survived/Inactive_did_not_survive); if graded labels exist in metadata (thriving/maintained/dormant/dead activity bucket), ALSO fit ordinal logit as secondary model
  - predictors: founder_pre_departure_commit_share, n_new_nonfounder_doa_owners + controls above
  - with n=32 (20/12 split) and up to 8 predictors, explicitly check separation/rank-deficiency BEFORE fitting: use statsmodels Logit with regularization (L2, small C) as primary if unregularized MLE fails to converge or produces |coef|>10 (classic complete-separation symptom); report convergence diagnostics explicitly
  - apply Benjamini-Hochberg correction across the family of predictor p-values (both diffusion predictors + controls), alpha=0.05, per Avelino et al.'s own procedure
  - report standardized effect sizes (Cohen's d equivalents from standardized logistic coefficients) for diffusion predictors vs size/popularity controls -- success criterion #2 needs the head-to-head comparison
  - IMPORTANT: given last iteration's zero-usable-cell failure, explicitly log cell counts for every stratification (language x outcome, popularity-bucket x outcome) BEFORE attempting stratified analysis; if any planned stratified cell has <3 observations, fall back to a single pooled model with strata as covariates rather than per-stratum fits, and document this deviation

  ## 4. Test B: Matched-pairs nearest-neighbor bootstrap
  - define popularity/size bucket via stars+forks+contributor_count (e.g., k-NN on standardized [log(stars), log(forks), log(contributors)] or simple tercile bucketing given n=32)
  - for each survivor, find nearest non-survivor(s) within bucket (or vice versa) differing in founder_pre_departure_commit_share/n_new_nonfounder_doa_owners
  - if exact matched pairs are too sparse at n=32 (this is what killed the test last iteration): use CALIPER-based matching (accept nearest neighbor within a distance threshold rather than requiring exact bucket equality) and report the caliper value and how many usable pairs it yields; sweep 2-3 caliper widths and report sensitivity
  - bootstrap (>=2000 resamples) the paired difference in survival rate between high-diffusion (founder-share<50% AND >=2 non-founder owners) vs low-diffusion (founder-share>=80%) matched groups; report 95% CI
  - if usable pairs remain 0 even under relaxed caliper: explicitly report as UNTESTABLE (not as a negative result), state the achieved match count, and report the unmatched raw group difference with a big caveat instead of fabricating a bootstrap CI

  ## 5. Test C: Within-repo random-window placebo (raise draws 25 -> 300)
  - for each of the 32 repos, draw 300 random 6-12mo windows from that repo's OWN pre-TFDD history (excluding the true window)
  - recompute founder-share/n_new_nonfounder_doa_owners for each placebo window using the same DOA logic as the true window
  - compute correlation (founder-share vs survival) for each placebo draw -> build empirical null distribution (300 draws x however many repos have sufficient history length for windowing)
  - report true window's r against this refined percentile (finer resolution than prior 25-draw 40th percentile / p=0.615)
  - fixed random seed, log it, for reproducibility

  ## 6. NEW: window-boundary validation control (this iteration's main addition)
  - select 10-15 NON-TFDD repos from the corpus's original candidate pool if available in dataset metadata (repos processed but excluded for 'no qualifying TFDD') -- check mine_repo.py / data.py outputs in dataset artifact workspace for a log of the 120 'no qualifying TFDD' discards; if raw candidate logs aren't retrievable, instead use STABLE (non-departure) periods from repos already in the TFDD corpus itself (e.g., a 6-12mo window >=2 years before the TFDD, far from any detachment event)
  - for each, recompute DOA-based founder-share at 3-5 different 6-12mo windows within that stable period
  - compute within-repo variance of founder-share across these stable-period windows -> this is the 'boundary-noise floor'
  - compare: is the true pre-departure window's effect size (r=0.180 from prior iteration, or newly computed r) distinguishable from this noise floor? Report noise-floor variance alongside the true-window vs placebo-window comparison from Test C
  - this directly tests the reviewer's concern: is window computation itself (not the mechanism) responsible for weak signal

  ## 7. Output
  - write method_out.json: all three test results (A/B/C) + window-boundary-noise control results + baseline replication numbers, each tagged EXECUTED/UNTESTABLE with reasons, confidence intervals, and explicit comparison to prior iteration's numbers (r=0.180, p=0.615, n=30)
  - include a clearly-labeled section: 'What changed vs iter1: unified corpus (32 vs 62/30-usable), placebo draws 25->300, new boundary-noise control'
fallback_plan: >-
  If BH-FDR regression still returns a rank-deficient/non-converging fit even after L2 regularization at n=32 (very plausible
  with ~8 predictors and 12 minority-class events): drop to a minimal 2-3 predictor model (just founder_pre_departure_commit_share
  + n_new_nonfounder_doa_owners + one size control like log(stars)) and report that as the primary regression, with the full
  model reported separately as exploratory/unstable. If matched-pairs bootstrap still yields zero usable pairs even with a
  wide caliper: report it as UNTESTABLE at this corpus size (as required by the artifact direction's honesty framing), and
  substitute a simple unmatched two-group comparison (Mann-Whitney U on survival rate or founder-share) with an explicit caveat
  that popularity is not controlled. If the dataset artifact's metadata does not contain enough granularity to recompute placebo/stable-period
  windows without re-cloning (e.g., missing per-commit timestamps needed for arbitrary window slicing): fall back to using
  only the windows/years already present in metadata_* (the yearly DOA/TF tables) rather than attempting fine-grained re-slicing,
  and clearly note this as a resolution limitation rather than silently interpolating. If the non-TFDD stable-period repos
  are unavailable from dataset metadata: use TFDD repos' own multi-year-before-departure windows as the stable-period proxy,
  clearly labeled as a substitution.
testing_plan: >-
  1. First load and validate the dataset artifact's full_data_out.json: assert exactly 32 rows in the founder_departure_tfdd_corpus
  group, spot-check 2-3 rows' parsed `input`/`output`/metadata against the dataset artifact's own textual summary (20 survived/12
  not, language breakdown Go7/Ruby11/JS6/Java5/Rust3) before writing any analysis code -- this catches parsing bugs immediately
  rather than after hours of downstream computation. 2. Run the baseline-replication step (Test 0) first, alone, and check
  the reproduced snapshot Cohen's d is in a similar negligible-small range to Avelino et al.'s d=0.13-0.26 -- if wildly different,
  the covariate parsing or DOA replication has a bug, fix before proceeding. 3. Run Test C (placebo) at only 10 draws per
  repo first as a smoke test to confirm the windowing/DOA recomputation code runs without error and produces a sane correlation
  distribution, THEN scale to the full 300 draws (per aii-long-running-tasks staged-scaling pattern) -- watch wall-clock time
  at 10 draws x 32 repos to extrapolate whether 300 draws is feasible in the time budget; if DOA recomputation per window
  is expensive, consider caching per-commit author/file data once per repo and only re-aggregating per window. 4. Run Test
  A (regression) and immediately print convergence diagnostics (coefficient magnitudes, standard errors) before trusting any
  p-value; log cell counts for every planned stratification before attempting it. 5. Run Test B (matched-pairs) and log the
  achieved match count at each caliper width tried -- if the tightest caliper gives 0 pairs, do not silently widen without
  logging the widening as a documented methodological choice. 6. Run the new window-boundary-noise control last (Test 6) since
  it depends on having working window-recomputation code from Test C. 7. Before finalizing, cross-check that the reported
  r/p-values for the true pre-departure window are computed identically to prior iteration's method (same DOA formula, same
  commit-share definition) so the comparison to r=0.180/p=0.615 is apples-to-apples -- if the unified corpus changes these
  numbers, explicitly report both old and new values side by side.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_0qwvnbyIv0EL
type: research
title: Founder-Departure Mining Recipe Verified
summary: >-
  This research artifact verifies, against the two primary Avelino et al. papers (ICPC 2016, arXiv:1604.06766; ESEM 2019,
  arXiv:1906.08058), the exact reproducible methodology needed to mine founder Truck Factor Developer Detachment (TFDD) events
  and study pre-departure authority-diffusion trajectories from public git histories. Key deliverables: (1) the verified Degree-of-Authorship
  (DOA) formula DOA=3.293+1.098*FA+0.164*DL-0.321*ln(1+AC) with FA/DL/AC precisely defined -- critically, DL is confirmed
  to be a raw commit-count term (number of the developer's own commits to the file), NOT a recency/days-since-last-change
  term as an earlier working hypothesis assumed, and this correction is load-bearing for any downstream implementation; (2)
  the exact 0.75-normalized / 3.293-absolute authorship threshold and its empirical tuning method; (3) the greedy Truck Factor
  algorithm pseudocode with exact coverage-check-before-removal semantics; (4) the verified 1-year abandoner threshold with
  the FULL five-way harmonic-mean sensitivity table (3mo/6mo/1yr/1.5yr/2yr); (5) confirmation that Active/Inactive/survival
  is a strictly BINARY state machine keyed to the LAST observed TFDD (not a graded thriving/dormant/dead framing, which has
  no basis in the primary sources) and that there is no fixed post-TFDD survival window (e.g. no 18-month cutoff exists in
  the paper -- survival is measured via yearly TF recomputation through the dataset collection date); (6) confirmation that
  DOA/TF was only ever validated at YEARLY full-history snapshots, never on arbitrary sub-year windows, meaning any 'pre-departure
  6-12 month window' DOA recomputation is a genuine unvalidated methodological extension that must be built and justified
  independently, with an explicit note on the FA window-boundary ambiguity this creates; (7) a concrete PyDriller-based local
  extraction code sketch for computing per-file per-author FA/DL/AC from a full local clone with no GitHub API dependency;
  (8) a local identity-resolution heuristic (normalize name/email, special-case GitHub noreply numeric IDs, union-find merge,
  bot exclusion, VCS-migration-artifact screening) offered as an explicitly UNVALIDATED substitute for Avelino et al.'s own
  GitHub-API-based alias resolution (median 11% alias rate); (9) pointer to the original authors' public Java reference implementation
  (aserg-ufmg/Truck-Factor, ~240 stars) as the correctness check of record; (10) a vetted 10-entry candidate seed list of
  real founder-handoff open-source repositories with explicit EXCLUDE/CAUTION flags (e.g. node-sass is project death not succession;
  youtube-dl->yt-dlp is a fork not a same-repo handoff; Homebrew and scikit-learn are likely already TF>1 and poor fits for
  a strict single-founder TF=1 construct), offered as a DATASET-artifact starting point rather than a claim of confirmed TFDD
  status. All corpus-selection parameters (top-500-starred x 6 languages, 1,932-project final corpus, exclusion criteria)
  are reproduced exactly. Eight explicit gaps/flags are documented where the primary sources under-specify a needed detail
  (tie-breaking rule, exact history-corruption detection threshold, etc.), so downstream DATASET/EXPERIMENT artifacts know
  precisely where they must make and document their own methodological choices rather than assuming full parity with the published
  pipeline.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_dependency_files:
  file_list:
  - research_out.json

--- Dependency 2 ---
id: art_24Q1bYB_ULpu
type: dataset
title: Founder-Departure OSS Truck-Factor Corpus
summary: >-
  This dataset mines real GitHub repositories to test whether pre-departure authority diffusion predicts whether an open-source
  project survives its founder stepping away. Candidates (1,615 repos) were discovered via the GitHub Search API stratified
  across 6 languages (Python, JavaScript, Go, Rust, Java, Ruby) and 3 star-count buckets (100-2000, 2000-10000, >10000) to
  avoid confounding popularity with survival. Full commit history for each candidate was pulled via `git clone --filter=blob:none`
  (partial clone, no blob content, unlimited by GitHub API rate limits) plus `git log --name-only`, giving per-commit (author
  email, date, files changed) tuples with no cloning-scale API cost. From this raw history the pipeline computes, per year,
  the exact Degree-of-Authorship metric from Avelino et al. (ICPC 2016): DOA(d,f) = 3.293 + 1.098*FirstAuthor(d,f) + 0.164*Deliveries(d,f)
  - 0.321*ln(1+Acceptances(d,f)), and the Truck Factor via the paper's greedy algorithm (repeatedly remove the highest-file-count
  DOA-primary author while remaining authors still cover >=50% of files). A Truck-Factor-Developer-Detachment (TFDD) is flagged
  the first year the sole (TF=1) truck-factor developer has been silent >=1 year and is confirmed to be the project's founder
  (earliest committer with dominant early-commit share). Algorithm correctness was validated against the paper's own worked
  example (composer/satis): the reproduced TF sequence (1,1,1,2,2,2,...) and TFDD detection matches the paper's Figure 1 exactly.
  Of 216 candidates processed, 32 qualified with a founder-only TFDD plus >=3 years of subsequent history (avoiding right-censoring);
  184 were discarded and logged with reasons (no qualifying TFDD 120, non-software/low-code-fraction 24, too few commits 15,
  right-censored 11, migration/squash mining artifact 11, history too large 3). Each of the 32 output rows (dataset group
  'founder_departure_tfdd_corpus' in full_data_out.json, schema exp_sel_data_out.json) has `input` = a JSON string of pre-TFDD/TFDD-snapshot
  covariates (founder's pre-departure commit share, count of new non-founder DOA-primary file owners in the 6-12mo pre-TFDD
  window, founder's early authorship share, stars, forks, contributor count, language, license, project age, total commits/files,
  history span) and `output` = the survival label (Active_survived / Inactive_did_not_survive per Avelino et al.'s Active/Inactive
  model: did a new truck-factor developer arrive and commit activity persist for >=6 months post-TFDD). Rich metadata_* fields
  on every example carry the full per-year DOA/TF developer-set tables, TFDD date/developer/silence-duration, the pre-TFDD
  window details, TFDD-snapshot covariates, the 18-month post-TFDD monthly commit-count time series, activity bucket (thriving/maintained/dormant/dead),
  repo identity/URL/stars/language/license, and first/last commit dates -- enough for downstream experiment code to recompute
  or verify the authority-diffusion trajectory without re-cloning any repository. The corpus spans 5 languages (Go 7, Ruby
  11, JavaScript 6, Java 5, Rust 3) and both survival outcomes (20 Active_survived, 12 Inactive_did_not_survive), is 175KB
  (well under the 300MB budget), and passed exp_sel_data_out.json schema validation. Mining code (search_candidates.py, mine_repo.py,
  run_mining.py, data.py) is included for full reproducibility and to extend the corpus further if a downstream experiment
  wants a larger sample.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json

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
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

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
TODO 2. Read preview files from dependencies to understand data structure. Use ALL datasets provided — do not skip or select a subset. Read domain handbook if applicable (see <available_domain_handbooks>). Test basic functionality with 'uv run'.
TODO 3. Fully implement our method AND baseline (comparison) as described in artifact plan in './method.py'. Use exp_gen_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant methods or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
```

### [2] HUMAN-USER prompt · 2026-08-21 17:45:14 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-python · 2026-08-21 17:45:20 UTC

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

### [4] SKILL-INPUT — aii-long-running-tasks · 2026-08-21 17:45:20 UTC

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

### [5] SKILL-INPUT — aii-json · 2026-08-21 17:45:20 UTC

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

### [6] SKILL-INPUT — aii-use-hardware · 2026-08-21 17:45:20 UTC

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

### [7] SKILL-INPUT — aii-parallel-computing · 2026-08-21 17:45:20 UTC

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

### [8] SKILL-INPUT — aii-file-size-limit · 2026-08-21 17:45:20 UTC

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

### [9] SYSTEM-USER prompt · 2026-08-21 18:02:20 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx2
type: experiment
title: Unified-Corpus Re-Test of Pre-Departure Authority Diffusion
summary: >-
  Re-run the three pre-registered tests (BH-FDR regression, matched-pairs bootstrap, within-repo placebo at >=200 draws) on
  the single unified 32-repo dataset artifact instead of independently re-mined data, and add a new window-boundary-noise
  control using non-TFDD repos to separate measurement noise from genuine signal.
runpod_compute_profile: gpu
implementation_pseudocode: |-
  # method.py

  ## 0. Setup
  - load full_data_out.json from dataset dependency (art_24Q1bYB_ULpu), group 'founder_departure_tfdd_corpus'
  - parse each row's `input` JSON string -> covariates dict; `output` -> survival label (Active_survived / Inactive_did_not_survive)
  - parse metadata_* fields -> per-year DOA/TF developer-set tables, TFDD date/developer, pre-TFDD window details, post-TFDD monthly commit series, repo identity/stars/language/license
  - log n=32 total rows, breakdown by language (Go7/Ruby11/JS6/Java5/Rust3) and outcome (20 survived/12 not)
  - if n < 32 or schema mismatch vs dataset summary -> hard fail loudly (do NOT silently drop rows) since corpus-provenance unification is the whole point of this iteration

  ## 1. Baseline replication checks (compare against Avelino et al. and dataset artifact summary)
  - founder-only-TFDD rate in corpus (sanity: should match the 32/216 mining yield already reported)
  - survival rate = 20/32 = 62.5% -> report alongside Avelino et al.'s unconditioned 41% baseline (note directionally different denominator: this is founder-only-TF=1 TFDDs, not all TFDDs)
  - snapshot Cohen's d for developers/commits/files between survivors and non-survivors AT the TFDD year (using existing per-year DOA/TF tables in metadata) -> replicate Avelino et al.'s d=0.13-0.26 negligible-small finding on this corpus as a validity check

  ## 2. Core covariates (reuse from method.py in prior iteration's experiment artifact if available in workspace context; otherwise recompute from metadata fields already present in dataset -- do NOT re-clone/re-mine)
  - founder_pre_departure_commit_share (6-12mo window before TFDD)
  - n_new_nonfounder_doa_owners (distinct accounts reaching DOA-primary file ownership in that window)
  - controls: stars, forks, contributor_count, language (categorical), license (categorical), project_age_days, total_commits, total_files, history_span_days

  ## 3. Test A: BH-FDR logistic + ordinal regression
  - outcome: survival (binary Active_survived/Inactive_did_not_survive); if graded labels exist in metadata (thriving/maintained/dormant/dead activity bucket), ALSO fit ordinal logit as secondary model
  - predictors: founder_pre_departure_commit_share, n_new_nonfounder_doa_owners + controls above
  - with n=32 (20/12 split) and up to 8 predictors, explicitly check separation/rank-deficiency BEFORE fitting: use statsmodels Logit with regularization (L2, small C) as primary if unregularized MLE fails to converge or produces |coef|>10 (classic complete-separation symptom); report convergence diagnostics explicitly
  - apply Benjamini-Hochberg correction across the family of predictor p-values (both diffusion predictors + controls), alpha=0.05, per Avelino et al.'s own procedure
  - report standardized effect sizes (Cohen's d equivalents from standardized logistic coefficients) for diffusion predictors vs size/popularity controls -- success criterion #2 needs the head-to-head comparison
  - IMPORTANT: given last iteration's zero-usable-cell failure, explicitly log cell counts for every stratification (language x outcome, popularity-bucket x outcome) BEFORE attempting stratified analysis; if any planned stratified cell has <3 observations, fall back to a single pooled model with strata as covariates rather than per-stratum fits, and document this deviation

  ## 4. Test B: Matched-pairs nearest-neighbor bootstrap
  - define popularity/size bucket via stars+forks+contributor_count (e.g., k-NN on standardized [log(stars), log(forks), log(contributors)] or simple tercile bucketing given n=32)
  - for each survivor, find nearest non-survivor(s) within bucket (or vice versa) differing in founder_pre_departure_commit_share/n_new_nonfounder_doa_owners
  - if exact matched pairs are too sparse at n=32 (this is what killed the test last iteration): use CALIPER-based matching (accept nearest neighbor within a distance threshold rather than requiring exact bucket equality) and report the caliper value and how many usable pairs it yields; sweep 2-3 caliper widths and report sensitivity
  - bootstrap (>=2000 resamples) the paired difference in survival rate between high-diffusion (founder-share<50% AND >=2 non-founder owners) vs low-diffusion (founder-share>=80%) matched groups; report 95% CI
  - if usable pairs remain 0 even under relaxed caliper: explicitly report as UNTESTABLE (not as a negative result), state the achieved match count, and report the unmatched raw group difference with a big caveat instead of fabricating a bootstrap CI

  ## 5. Test C: Within-repo random-window placebo (raise draws 25 -> 300)
  - for each of the 32 repos, draw 300 random 6-12mo windows from that repo's OWN pre-TFDD history (excluding the true window)
  - recompute founder-share/n_new_nonfounder_doa_owners for each placebo window using the same DOA logic as the true window
  - compute correlation (founder-share vs survival) for each placebo draw -> build empirical null distribution (300 draws x however many repos have sufficient history length for windowing)
  - report true window's r against this refined percentile (finer resolution than prior 25-draw 40th percentile / p=0.615)
  - fixed random seed, log it, for reproducibility

  ## 6. NEW: window-boundary validation control (this iteration's main addition)
  - select 10-15 NON-TFDD repos from the corpus's original candidate pool if available in dataset metadata (repos processed but excluded for 'no qualifying TFDD') -- check mine_repo.py / data.py outputs in dataset artifact workspace for a log of the 120 'no qualifying TFDD' discards; if raw candidate logs aren't retrievable, instead use STABLE (non-departure) periods from repos already in the TFDD corpus itself (e.g., a 6-12mo window >=2 years before the TFDD, far from any detachment event)
  - for each, recompute DOA-based founder-share at 3-5 different 6-12mo windows within that stable period
  - compute within-repo variance of founder-share across these stable-period windows -> this is the 'boundary-noise floor'
  - compare: is the true pre-departure window's effect size (r=0.180 from prior iteration, or newly computed r) distinguishable from this noise floor? Report noise-floor variance alongside the true-window vs placebo-window comparison from Test C
  - this directly tests the reviewer's concern: is window computation itself (not the mechanism) responsible for weak signal

  ## 7. Output
  - write method_out.json: all three test results (A/B/C) + window-boundary-noise control results + baseline replication numbers, each tagged EXECUTED/UNTESTABLE with reasons, confidence intervals, and explicit comparison to prior iteration's numbers (r=0.180, p=0.615, n=30)
  - include a clearly-labeled section: 'What changed vs iter1: unified corpus (32 vs 62/30-usable), placebo draws 25->300, new boundary-noise control'
fallback_plan: >-
  If BH-FDR regression still returns a rank-deficient/non-converging fit even after L2 regularization at n=32 (very plausible
  with ~8 predictors and 12 minority-class events): drop to a minimal 2-3 predictor model (just founder_pre_departure_commit_share
  + n_new_nonfounder_doa_owners + one size control like log(stars)) and report that as the primary regression, with the full
  model reported separately as exploratory/unstable. If matched-pairs bootstrap still yields zero usable pairs even with a
  wide caliper: report it as UNTESTABLE at this corpus size (as required by the artifact direction's honesty framing), and
  substitute a simple unmatched two-group comparison (Mann-Whitney U on survival rate or founder-share) with an explicit caveat
  that popularity is not controlled. If the dataset artifact's metadata does not contain enough granularity to recompute placebo/stable-period
  windows without re-cloning (e.g., missing per-commit timestamps needed for arbitrary window slicing): fall back to using
  only the windows/years already present in metadata_* (the yearly DOA/TF tables) rather than attempting fine-grained re-slicing,
  and clearly note this as a resolution limitation rather than silently interpolating. If the non-TFDD stable-period repos
  are unavailable from dataset metadata: use TFDD repos' own multi-year-before-departure windows as the stable-period proxy,
  clearly labeled as a substitution.
testing_plan: >-
  1. First load and validate the dataset artifact's full_data_out.json: assert exactly 32 rows in the founder_departure_tfdd_corpus
  group, spot-check 2-3 rows' parsed `input`/`output`/metadata against the dataset artifact's own textual summary (20 survived/12
  not, language breakdown Go7/Ruby11/JS6/Java5/Rust3) before writing any analysis code -- this catches parsing bugs immediately
  rather than after hours of downstream computation. 2. Run the baseline-replication step (Test 0) first, alone, and check
  the reproduced snapshot Cohen's d is in a similar negligible-small range to Avelino et al.'s d=0.13-0.26 -- if wildly different,
  the covariate parsing or DOA replication has a bug, fix before proceeding. 3. Run Test C (placebo) at only 10 draws per
  repo first as a smoke test to confirm the windowing/DOA recomputation code runs without error and produces a sane correlation
  distribution, THEN scale to the full 300 draws (per aii-long-running-tasks staged-scaling pattern) -- watch wall-clock time
  at 10 draws x 32 repos to extrapolate whether 300 draws is feasible in the time budget; if DOA recomputation per window
  is expensive, consider caching per-commit author/file data once per repo and only re-aggregating per window. 4. Run Test
  A (regression) and immediately print convergence diagnostics (coefficient magnitudes, standard errors) before trusting any
  p-value; log cell counts for every planned stratification before attempting it. 5. Run Test B (matched-pairs) and log the
  achieved match count at each caliper width tried -- if the tightest caliper gives 0 pairs, do not silently widen without
  logging the widening as a documented methodological choice. 6. Run the new window-boundary-noise control last (Test 6) since
  it depends on having working window-recomputation code from Test C. 7. Before finalizing, cross-check that the reported
  r/p-values for the true pre-departure window are computed identically to prior iteration's method (same DOA formula, same
  commit-share definition) so the comparison to r=0.180/p=0.615 is apples-to-apples -- if the unified corpus changes these
  numbers, explicitly report both old and new values side by side.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_0qwvnbyIv0EL
type: research
title: Founder-Departure Mining Recipe Verified
summary: >-
  This research artifact verifies, against the two primary Avelino et al. papers (ICPC 2016, arXiv:1604.06766; ESEM 2019,
  arXiv:1906.08058), the exact reproducible methodology needed to mine founder Truck Factor Developer Detachment (TFDD) events
  and study pre-departure authority-diffusion trajectories from public git histories. Key deliverables: (1) the verified Degree-of-Authorship
  (DOA) formula DOA=3.293+1.098*FA+0.164*DL-0.321*ln(1+AC) with FA/DL/AC precisely defined -- critically, DL is confirmed
  to be a raw commit-count term (number of the developer's own commits to the file), NOT a recency/days-since-last-change
  term as an earlier working hypothesis assumed, and this correction is load-bearing for any downstream implementation; (2)
  the exact 0.75-normalized / 3.293-absolute authorship threshold and its empirical tuning method; (3) the greedy Truck Factor
  algorithm pseudocode with exact coverage-check-before-removal semantics; (4) the verified 1-year abandoner threshold with
  the FULL five-way harmonic-mean sensitivity table (3mo/6mo/1yr/1.5yr/2yr); (5) confirmation that Active/Inactive/survival
  is a strictly BINARY state machine keyed to the LAST observed TFDD (not a graded thriving/dormant/dead framing, which has
  no basis in the primary sources) and that there is no fixed post-TFDD survival window (e.g. no 18-month cutoff exists in
  the paper -- survival is measured via yearly TF recomputation through the dataset collection date); (6) confirmation that
  DOA/TF was only ever validated at YEARLY full-history snapshots, never on arbitrary sub-year windows, meaning any 'pre-departure
  6-12 month window' DOA recomputation is a genuine unvalidated methodological extension that must be built and justified
  independently, with an explicit note on the FA window-boundary ambiguity this creates; (7) a concrete PyDriller-based local
  extraction code sketch for computing per-file per-author FA/DL/AC from a full local clone with no GitHub API dependency;
  (8) a local identity-resolution heuristic (normalize name/email, special-case GitHub noreply numeric IDs, union-find merge,
  bot exclusion, VCS-migration-artifact screening) offered as an explicitly UNVALIDATED substitute for Avelino et al.'s own
  GitHub-API-based alias resolution (median 11% alias rate); (9) pointer to the original authors' public Java reference implementation
  (aserg-ufmg/Truck-Factor, ~240 stars) as the correctness check of record; (10) a vetted 10-entry candidate seed list of
  real founder-handoff open-source repositories with explicit EXCLUDE/CAUTION flags (e.g. node-sass is project death not succession;
  youtube-dl->yt-dlp is a fork not a same-repo handoff; Homebrew and scikit-learn are likely already TF>1 and poor fits for
  a strict single-founder TF=1 construct), offered as a DATASET-artifact starting point rather than a claim of confirmed TFDD
  status. All corpus-selection parameters (top-500-starred x 6 languages, 1,932-project final corpus, exclusion criteria)
  are reproduced exactly. Eight explicit gaps/flags are documented where the primary sources under-specify a needed detail
  (tie-breaking rule, exact history-corruption detection threshold, etc.), so downstream DATASET/EXPERIMENT artifacts know
  precisely where they must make and document their own methodological choices rather than assuming full parity with the published
  pipeline.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_dependency_files:
  file_list:
  - research_out.json

--- Dependency 2 ---
id: art_24Q1bYB_ULpu
type: dataset
title: Founder-Departure OSS Truck-Factor Corpus
summary: >-
  This dataset mines real GitHub repositories to test whether pre-departure authority diffusion predicts whether an open-source
  project survives its founder stepping away. Candidates (1,615 repos) were discovered via the GitHub Search API stratified
  across 6 languages (Python, JavaScript, Go, Rust, Java, Ruby) and 3 star-count buckets (100-2000, 2000-10000, >10000) to
  avoid confounding popularity with survival. Full commit history for each candidate was pulled via `git clone --filter=blob:none`
  (partial clone, no blob content, unlimited by GitHub API rate limits) plus `git log --name-only`, giving per-commit (author
  email, date, files changed) tuples with no cloning-scale API cost. From this raw history the pipeline computes, per year,
  the exact Degree-of-Authorship metric from Avelino et al. (ICPC 2016): DOA(d,f) = 3.293 + 1.098*FirstAuthor(d,f) + 0.164*Deliveries(d,f)
  - 0.321*ln(1+Acceptances(d,f)), and the Truck Factor via the paper's greedy algorithm (repeatedly remove the highest-file-count
  DOA-primary author while remaining authors still cover >=50% of files). A Truck-Factor-Developer-Detachment (TFDD) is flagged
  the first year the sole (TF=1) truck-factor developer has been silent >=1 year and is confirmed to be the project's founder
  (earliest committer with dominant early-commit share). Algorithm correctness was validated against the paper's own worked
  example (composer/satis): the reproduced TF sequence (1,1,1,2,2,2,...) and TFDD detection matches the paper's Figure 1 exactly.
  Of 216 candidates processed, 32 qualified with a founder-only TFDD plus >=3 years of subsequent history (avoiding right-censoring);
  184 were discarded and logged with reasons (no qualifying TFDD 120, non-software/low-code-fraction 24, too few commits 15,
  right-censored 11, migration/squash mining artifact 11, history too large 3). Each of the 32 output rows (dataset group
  'founder_departure_tfdd_corpus' in full_data_out.json, schema exp_sel_data_out.json) has `input` = a JSON string of pre-TFDD/TFDD-snapshot
  covariates (founder's pre-departure commit share, count of new non-founder DOA-primary file owners in the 6-12mo pre-TFDD
  window, founder's early authorship share, stars, forks, contributor count, language, license, project age, total commits/files,
  history span) and `output` = the survival label (Active_survived / Inactive_did_not_survive per Avelino et al.'s Active/Inactive
  model: did a new truck-factor developer arrive and commit activity persist for >=6 months post-TFDD). Rich metadata_* fields
  on every example carry the full per-year DOA/TF developer-set tables, TFDD date/developer/silence-duration, the pre-TFDD
  window details, TFDD-snapshot covariates, the 18-month post-TFDD monthly commit-count time series, activity bucket (thriving/maintained/dormant/dead),
  repo identity/URL/stars/language/license, and first/last commit dates -- enough for downstream experiment code to recompute
  or verify the authority-diffusion trajectory without re-cloning any repository. The corpus spans 5 languages (Go 7, Ruby
  11, JavaScript 6, Java 5, Rust 3) and both survival outcomes (20 Active_survived, 12 Inactive_did_not_survive), is 175KB
  (well under the 300MB budget), and passed exp_sel_data_out.json schema validation. Mining code (search_candidates.py, mine_repo.py,
  run_mining.py, data.py) is included for full reproducibility and to extend the corpus further if a downstream experiment
  wants a larger sample.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json

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
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

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
TODO 1. Use aii-json skill's format script with `--input method_out.json` to generate full, mini, and preview versions. If not in your workspace (see <workspace> above), copy them there. Run 'ls -lh' to verify these three files exist (DO NOT read them).
TODO 2. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to method_out.json and full_method_out.json.
TODO 3. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ExperimentExpectedFiles": {
      "description": "All expected output files from experiment artifact.",
      "properties": {
        "script": {
          "description": "Path to method.py script. Example: 'method.py'",
          "title": "Script",
          "type": "string"
        },
        "full_output": {
          "description": "Full method output JSON file. Example: 'full_method_out.json'",
          "title": "Full Output",
          "type": "string"
        },
        "mini_output": {
          "description": "Mini method output JSON file. Example: 'mini_method_out.json'",
          "title": "Mini Output",
          "type": "string"
        },
        "preview_output": {
          "description": "Preview method output JSON file. Example: 'preview_method_out.json'",
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
      "title": "ExperimentExpectedFiles",
      "type": "object"
    }
  },
  "description": "Experiment artifact \u2014 structured output + file metadata.\n\nImplements research methodology with baseline comparison.\nProduces method.py and method_out.json files.",
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
      "$ref": "#/$defs/ExperimentExpectedFiles",
      "description": "All output files you created. Must include method.py script plus full/mini/preview method output JSON files."
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
  "title": "ExperimentArtifact",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [10] SYSTEM-USER prompt · 2026-08-21 18:02:36 UTC

```
<validation-feedback>
Attempt 1 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [11] SYSTEM-USER prompt · 2026-08-21 18:02:56 UTC

```
<validation-feedback>
Attempt 2 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [12] SYSTEM-USER prompt · 2026-08-21 18:03:12 UTC

```
<validation-feedback>
Attempt 3 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [13] SYSTEM-USER prompt · 2026-08-21 18:05:02 UTC

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

<research_methodology>
Design experiments like a researcher, not a programmer running a script.

- Every method needs a meaningful baseline — the current standard approach, not a strawman.
- Control your variables. When comparing methods, hold everything else constant.
- Results need variance, not just point estimates. A single run proves nothing.
- Implement the proposed method and baseline side-by-side in the same pipeline to eliminate implementation-level confounds.
</research_methodology>

<task>
Implement the research methodology as a production-ready experimental system.
Adapt your implementation approach based on the hypothesis and domain requirements.
</task>

<critical_requirements>
- Fully implement the methodology described in hypothesis
- Use appropriate frameworks based on research domain
- Load and process data from the specified data_filepath
- Complete working systems
- Handle all edge cases, errors, and exceptions properly
- Always implement baseline comparison method
</critical_requirements>

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

<CRITICAL_WARNING__PREVIOUS_ATTEMPT_CRASHED>
YOUR PREVIOUS EXECUTION ATTEMPT CATASTROPHICALLY FAILED.
The entire worker container crashed after 1199s.
Error: output_format validation failed after 3 retries: The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Last messages before the crash:
  - [agent_tool_result: Bash] Tool: Bash
Result:
{"stdout": "    PID ELAPSED     TIME\n    812      51 00:00:07\n/bin/bash: line 3: py-spy: command not found", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
  - [agent_response] Only 51s elapsed, 7s CPU used — it's making progress normally (statsmodels Logit fitting is slow per-call but not stuck). I'll continue waiting.
  - [agent_tool_call: Monitor] Tool: Monitor
{'command': 'cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1\nuntil [ -f method_out.json ] || ! kill -0 812 2>/dev/null; do sleep 3; done\nif [ -f method_out.json ]; then echo DONE_SUCCESS; else echo DONE_FAILED; tail -60 logs/run.log; fi', 'description': 'wait for method.py completion (attempt 2)', 'timeout_ms': 600000}
  - [agent_tool_result: Monitor] Tool: Monitor
Result:
{"taskId": "b5xjh92xv", "timeoutMs": 600000, "persistent": false}
  - [agent_response] Still waiting on method.py (PID 812) to finish producing method_out.json.
  - [agent_tool_call: Bash] Tool: Bash
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
ls -la method_out.json 2>&1
ps -o pid,etimes,time -p 812 2>&1
tail -20 logs/run.log
  - [agent_tool_result: Bash] Tool: Bash
Result:
{"stdout": "ls: cannot access 'method_out.json': No such file or directory\n    PID ELAPSED     TIME\n2026-08-21 17:51:47.925 | INFO     | __main__:test0_baseline_replication:134 -   Cohen's d (stars, survived vs not): 0.403\n2026-08-21 17:51:47.929 | INFO     | __main__:test0_baseline_replication:134 -   Cohen's d (forks, survived vs not): 0.441\n2026-08-21 17:51:47.936 | INFO     | __main__:test0_baseline_replication:156 - Test 0 result: survival_rate=0.625, assessment=consistent_negligible_to_small\n2026-08-21 17:51:47.941 | INFO     | __main__:test_a_bhfdr_regression:186 - === Test A: BH-FDR logistic regression ===\n2026-08-21 17:51:48.337 | INFO     | __main__:check_stratification_cells:169 - Stratification cell counts -- language x outcome:\nsurvival    0  1\nlanguage        \nGo          5  2\nJava        0  5\nJavaScript  3  3\nRuby        4  7\nRust        0  3\n2026-08-21 17:51:48.347 | INFO     | __main__:check_stratification_cells:170 - Stratification cell counts -- popularity-tercile x outcome:\nsurvival  0  1\nstars         \nlow       5  6\nmid       5  5\nhigh      2  9\n2026-08-21 18:03:14.866 | INFO     | __main__:main:565 - Available RAM at start: 236.6 GB\n2026-08-21 18:03:14.876 | INFO     | __main__:load_corpus:69 - Loading unified corpus from /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/full_data_out.json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
  - [agent_tool_call: Edit] Tool: Edit
File: /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/method.py
OLD: # Memory: dataset is 175KB, trivially small relative to the 57GB container limit.
# Cap generously to fail fast/catchable rather than OOM-kill on any runaway growth.
resource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))
NEW: # Memory: dataset is 175KB, trivially small relative to the 57GB container limit.
# Cap generously to fail fast/catchable rather than OOM-kill on any runaway growth.
# NOTE: numpy/OpenBLAS/statsmodels reserve large virtual address ranges (mmap'd
# thread-pool arenas etc.) that count against RLIMIT_AS but are never resident,
# so a tight AS cap raises spurious MemoryErrors well before physical RAM is
# actually threatened. Cap at 16GB (still a hard, catchable ceiling; far below
# the 57GB container limit) rather than 4GB.
resource.setrlimit(resource.RLIMIT_AS, (16 * 1024**3, 16 * 1024**3))
  - [agent_tool_result: Edit] Tool: Edit
Result:
{"filePath": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/method.py", "oldString": "# Memory: dataset is 175KB, trivially small relative to the 57GB container limit.\n# Cap generously to fail fast/catchable rather than OOM-kill on any runaway growth.\nresource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))", "newString": "# Memory: dataset is 175KB, trivially small relative to the 57GB container limit.\n# Cap generously to fail fast/catchable rather than OOM-kill on any runaway growth.\n# NOTE: numpy/OpenBLAS/statsmodels reserve large virtual address ranges (mmap'd\n# thread-pool arenas etc.) that count against RLIMIT_AS but are never resident,\n# so a tight AS cap raises spurious MemoryErrors well before physical RAM is\n# actually threatened. Cap at 16GB (still a hard, catchable ceiling; far below\n# the 57GB container limit) rather than 4GB.\nresource.setrlimit(resource.RLIMIT_AS, (16 * 1024**3, 16 * 1024**3))", "originalFile": null, "structuredPatch": [{"oldStart": 59, "oldLines": 7, "newStart": 59, "newLines": 12, "lines": [" ", " # Memory: dataset is 175KB, trivially small relative to the 57GB container limit.", " # Cap generously to fail fast/catchable rather than OOM-kill on any runaway growth.", "-resource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))", "+# NOTE: numpy/OpenBLAS/statsmodels reserve large virtual address ranges (mmap'd", "+# thread-pool arenas etc.) that count against RLIMIT_AS but are never resident,", "+# so a tight AS cap raises spurious MemoryErrors well before physical RAM is", "+# actually threatened. Cap at 16GB (still a hard, catchable ceiling; far below", "+# the 57GB container limit) rather than 4GB.", "+resource.setrlimit(resource.RLIMIT_AS, (16 * 1024**3, 16 * 1024**3))", " ", " ", " # ---------------------------------------------------------------------------"]}], "userModified": false, "replaceAll": false}
  - [agent_response] Fixed the memory-limit bug (RLIMIT_AS was too tight for numpy/statsmodels virtual memory). Rerunning now.
  - [agent_tool_call: Bash] Tool: Bash
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
rm -f method_out.json
nohup .venv/bin/python method.py > run_stdout2.log 2>&1 &
echo "PID=$!"
disown
  - [agent_tool_result: Bash] Tool: Bash
Result:
{"stdout": "PID=1047", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
  - [agent_tool_call: Monitor] Tool: Monitor
{'command': 'cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1\nuntil [ -f method_out.json ] || ! kill -0 1047 2>/dev/null; do sleep 3; done\nif [ -f method_out.json ]; then echo DONE_SUCCESS; else echo DONE_FAILED; tail -60 run_stdout2.log; fi', 'description': 'wait for method.py completion after memory-limit fix', 'timeout_ms': 600000}
  - [agent_tool_result: Monitor] Tool: Monitor
Result:
{"taskId": "bkfu03tsv", "timeoutMs": 600000, "persistent": false}
  - [agent_response] Waiting for the run to finish (PID 1047).

This was NOT a normal code error — the entire container died. Study the error
and last messages above carefully. Identify what caused the crash and be
EXTREMELY careful to avoid repeating it. Do NOT use the same approach.
</CRITICAL_WARNING__PREVIOUS_ATTEMPT_CRASHED>

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx2
type: experiment
title: Unified-Corpus Re-Test of Pre-Departure Authority Diffusion
summary: >-
  Re-run the three pre-registered tests (BH-FDR regression, matched-pairs bootstrap, within-repo placebo at >=200 draws) on
  the single unified 32-repo dataset artifact instead of independently re-mined data, and add a new window-boundary-noise
  control using non-TFDD repos to separate measurement noise from genuine signal.
runpod_compute_profile: gpu
implementation_pseudocode: |-
  # method.py

  ## 0. Setup
  - load full_data_out.json from dataset dependency (art_24Q1bYB_ULpu), group 'founder_departure_tfdd_corpus'
  - parse each row's `input` JSON string -> covariates dict; `output` -> survival label (Active_survived / Inactive_did_not_survive)
  - parse metadata_* fields -> per-year DOA/TF developer-set tables, TFDD date/developer, pre-TFDD window details, post-TFDD monthly commit series, repo identity/stars/language/license
  - log n=32 total rows, breakdown by language (Go7/Ruby11/JS6/Java5/Rust3) and outcome (20 survived/12 not)
  - if n < 32 or schema mismatch vs dataset summary -> hard fail loudly (do NOT silently drop rows) since corpus-provenance unification is the whole point of this iteration

  ## 1. Baseline replication checks (compare against Avelino et al. and dataset artifact summary)
  - founder-only-TFDD rate in corpus (sanity: should match the 32/216 mining yield already reported)
  - survival rate = 20/32 = 62.5% -> report alongside Avelino et al.'s unconditioned 41% baseline (note directionally different denominator: this is founder-only-TF=1 TFDDs, not all TFDDs)
  - snapshot Cohen's d for developers/commits/files between survivors and non-survivors AT the TFDD year (using existing per-year DOA/TF tables in metadata) -> replicate Avelino et al.'s d=0.13-0.26 negligible-small finding on this corpus as a validity check

  ## 2. Core covariates (reuse from method.py in prior iteration's experiment artifact if available in workspace context; otherwise recompute from metadata fields already present in dataset -- do NOT re-clone/re-mine)
  - founder_pre_departure_commit_share (6-12mo window before TFDD)
  - n_new_nonfounder_doa_owners (distinct accounts reaching DOA-primary file ownership in that window)
  - controls: stars, forks, contributor_count, language (categorical), license (categorical), project_age_days, total_commits, total_files, history_span_days

  ## 3. Test A: BH-FDR logistic + ordinal regression
  - outcome: survival (binary Active_survived/Inactive_did_not_survive); if graded labels exist in metadata (thriving/maintained/dormant/dead activity bucket), ALSO fit ordinal logit as secondary model
  - predictors: founder_pre_departure_commit_share, n_new_nonfounder_doa_owners + controls above
  - with n=32 (20/12 split) and up to 8 predictors, explicitly check separation/rank-deficiency BEFORE fitting: use statsmodels Logit with regularization (L2, small C) as primary if unregularized MLE fails to converge or produces |coef|>10 (classic complete-separation symptom); report convergence diagnostics explicitly
  - apply Benjamini-Hochberg correction across the family of predictor p-values (both diffusion predictors + controls), alpha=0.05, per Avelino et al.'s own procedure
  - report standardized effect sizes (Cohen's d equivalents from standardized logistic coefficients) for diffusion predictors vs size/popularity controls -- success criterion #2 needs the head-to-head comparison
  - IMPORTANT: given last iteration's zero-usable-cell failure, explicitly log cell counts for every stratification (language x outcome, popularity-bucket x outcome) BEFORE attempting stratified analysis; if any planned stratified cell has <3 observations, fall back to a single pooled model with strata as covariates rather than per-stratum fits, and document this deviation

  ## 4. Test B: Matched-pairs nearest-neighbor bootstrap
  - define popularity/size bucket via stars+forks+contributor_count (e.g., k-NN on standardized [log(stars), log(forks), log(contributors)] or simple tercile bucketing given n=32)
  - for each survivor, find nearest non-survivor(s) within bucket (or vice versa) differing in founder_pre_departure_commit_share/n_new_nonfounder_doa_owners
  - if exact matched pairs are too sparse at n=32 (this is what killed the test last iteration): use CALIPER-based matching (accept nearest neighbor within a distance threshold rather than requiring exact bucket equality) and report the caliper value and how many usable pairs it yields; sweep 2-3 caliper widths and report sensitivity
  - bootstrap (>=2000 resamples) the paired difference in survival rate between high-diffusion (founder-share<50% AND >=2 non-founder owners) vs low-diffusion (founder-share>=80%) matched groups; report 95% CI
  - if usable pairs remain 0 even under relaxed caliper: explicitly report as UNTESTABLE (not as a negative result), state the achieved match count, and report the unmatched raw group difference with a big caveat instead of fabricating a bootstrap CI

  ## 5. Test C: Within-repo random-window placebo (raise draws 25 -> 300)
  - for each of the 32 repos, draw 300 random 6-12mo windows from that repo's OWN pre-TFDD history (excluding the true window)
  - recompute founder-share/n_new_nonfounder_doa_owners for each placebo window using the same DOA logic as the true window
  - compute correlation (founder-share vs survival) for each placebo draw -> build empirical null distribution (300 draws x however many repos have sufficient history length for windowing)
  - report true window's r against this refined percentile (finer resolution than prior 25-draw 40th percentile / p=0.615)
  - fixed random seed, log it, for reproducibility

  ## 6. NEW: window-boundary validation control (this iteration's main addition)
  - select 10-15 NON-TFDD repos from the corpus's original candidate pool if available in dataset metadata (repos processed but excluded for 'no qualifying TFDD') -- check mine_repo.py / data.py outputs in dataset artifact workspace for a log of the 120 'no qualifying TFDD' discards; if raw candidate logs aren't retrievable, instead use STABLE (non-departure) periods from repos already in the TFDD corpus itself (e.g., a 6-12mo window >=2 years before the TFDD, far from any detachment event)
  - for each, recompute DOA-based founder-share at 3-5 different 6-12mo windows within that stable period
  - compute within-repo variance of founder-share across these stable-period windows -> this is the 'boundary-noise floor'
  - compare: is the true pre-departure window's effect size (r=0.180 from prior iteration, or newly computed r) distinguishable from this noise floor? Report noise-floor variance alongside the true-window vs placebo-window comparison from Test C
  - this directly tests the reviewer's concern: is window computation itself (not the mechanism) responsible for weak signal

  ## 7. Output
  - write method_out.json: all three test results (A/B/C) + window-boundary-noise control results + baseline replication numbers, each tagged EXECUTED/UNTESTABLE with reasons, confidence intervals, and explicit comparison to prior iteration's numbers (r=0.180, p=0.615, n=30)
  - include a clearly-labeled section: 'What changed vs iter1: unified corpus (32 vs 62/30-usable), placebo draws 25->300, new boundary-noise control'
fallback_plan: >-
  If BH-FDR regression still returns a rank-deficient/non-converging fit even after L2 regularization at n=32 (very plausible
  with ~8 predictors and 12 minority-class events): drop to a minimal 2-3 predictor model (just founder_pre_departure_commit_share
  + n_new_nonfounder_doa_owners + one size control like log(stars)) and report that as the primary regression, with the full
  model reported separately as exploratory/unstable. If matched-pairs bootstrap still yields zero usable pairs even with a
  wide caliper: report it as UNTESTABLE at this corpus size (as required by the artifact direction's honesty framing), and
  substitute a simple unmatched two-group comparison (Mann-Whitney U on survival rate or founder-share) with an explicit caveat
  that popularity is not controlled. If the dataset artifact's metadata does not contain enough granularity to recompute placebo/stable-period
  windows without re-cloning (e.g., missing per-commit timestamps needed for arbitrary window slicing): fall back to using
  only the windows/years already present in metadata_* (the yearly DOA/TF tables) rather than attempting fine-grained re-slicing,
  and clearly note this as a resolution limitation rather than silently interpolating. If the non-TFDD stable-period repos
  are unavailable from dataset metadata: use TFDD repos' own multi-year-before-departure windows as the stable-period proxy,
  clearly labeled as a substitution.
testing_plan: >-
  1. First load and validate the dataset artifact's full_data_out.json: assert exactly 32 rows in the founder_departure_tfdd_corpus
  group, spot-check 2-3 rows' parsed `input`/`output`/metadata against the dataset artifact's own textual summary (20 survived/12
  not, language breakdown Go7/Ruby11/JS6/Java5/Rust3) before writing any analysis code -- this catches parsing bugs immediately
  rather than after hours of downstream computation. 2. Run the baseline-replication step (Test 0) first, alone, and check
  the reproduced snapshot Cohen's d is in a similar negligible-small range to Avelino et al.'s d=0.13-0.26 -- if wildly different,
  the covariate parsing or DOA replication has a bug, fix before proceeding. 3. Run Test C (placebo) at only 10 draws per
  repo first as a smoke test to confirm the windowing/DOA recomputation code runs without error and produces a sane correlation
  distribution, THEN scale to the full 300 draws (per aii-long-running-tasks staged-scaling pattern) -- watch wall-clock time
  at 10 draws x 32 repos to extrapolate whether 300 draws is feasible in the time budget; if DOA recomputation per window
  is expensive, consider caching per-commit author/file data once per repo and only re-aggregating per window. 4. Run Test
  A (regression) and immediately print convergence diagnostics (coefficient magnitudes, standard errors) before trusting any
  p-value; log cell counts for every planned stratification before attempting it. 5. Run Test B (matched-pairs) and log the
  achieved match count at each caliper width tried -- if the tightest caliper gives 0 pairs, do not silently widen without
  logging the widening as a documented methodological choice. 6. Run the new window-boundary-noise control last (Test 6) since
  it depends on having working window-recomputation code from Test C. 7. Before finalizing, cross-check that the reported
  r/p-values for the true pre-departure window are computed identically to prior iteration's method (same DOA formula, same
  commit-share definition) so the comparison to r=0.180/p=0.615 is apples-to-apples -- if the unified corpus changes these
  numbers, explicitly report both old and new values side by side.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_0qwvnbyIv0EL
type: research
title: Founder-Departure Mining Recipe Verified
summary: >-
  This research artifact verifies, against the two primary Avelino et al. papers (ICPC 2016, arXiv:1604.06766; ESEM 2019,
  arXiv:1906.08058), the exact reproducible methodology needed to mine founder Truck Factor Developer Detachment (TFDD) events
  and study pre-departure authority-diffusion trajectories from public git histories. Key deliverables: (1) the verified Degree-of-Authorship
  (DOA) formula DOA=3.293+1.098*FA+0.164*DL-0.321*ln(1+AC) with FA/DL/AC precisely defined -- critically, DL is confirmed
  to be a raw commit-count term (number of the developer's own commits to the file), NOT a recency/days-since-last-change
  term as an earlier working hypothesis assumed, and this correction is load-bearing for any downstream implementation; (2)
  the exact 0.75-normalized / 3.293-absolute authorship threshold and its empirical tuning method; (3) the greedy Truck Factor
  algorithm pseudocode with exact coverage-check-before-removal semantics; (4) the verified 1-year abandoner threshold with
  the FULL five-way harmonic-mean sensitivity table (3mo/6mo/1yr/1.5yr/2yr); (5) confirmation that Active/Inactive/survival
  is a strictly BINARY state machine keyed to the LAST observed TFDD (not a graded thriving/dormant/dead framing, which has
  no basis in the primary sources) and that there is no fixed post-TFDD survival window (e.g. no 18-month cutoff exists in
  the paper -- survival is measured via yearly TF recomputation through the dataset collection date); (6) confirmation that
  DOA/TF was only ever validated at YEARLY full-history snapshots, never on arbitrary sub-year windows, meaning any 'pre-departure
  6-12 month window' DOA recomputation is a genuine unvalidated methodological extension that must be built and justified
  independently, with an explicit note on the FA window-boundary ambiguity this creates; (7) a concrete PyDriller-based local
  extraction code sketch for computing per-file per-author FA/DL/AC from a full local clone with no GitHub API dependency;
  (8) a local identity-resolution heuristic (normalize name/email, special-case GitHub noreply numeric IDs, union-find merge,
  bot exclusion, VCS-migration-artifact screening) offered as an explicitly UNVALIDATED substitute for Avelino et al.'s own
  GitHub-API-based alias resolution (median 11% alias rate); (9) pointer to the original authors' public Java reference implementation
  (aserg-ufmg/Truck-Factor, ~240 stars) as the correctness check of record; (10) a vetted 10-entry candidate seed list of
  real founder-handoff open-source repositories with explicit EXCLUDE/CAUTION flags (e.g. node-sass is project death not succession;
  youtube-dl->yt-dlp is a fork not a same-repo handoff; Homebrew and scikit-learn are likely already TF>1 and poor fits for
  a strict single-founder TF=1 construct), offered as a DATASET-artifact starting point rather than a claim of confirmed TFDD
  status. All corpus-selection parameters (top-500-starred x 6 languages, 1,932-project final corpus, exclusion criteria)
  are reproduced exactly. Eight explicit gaps/flags are documented where the primary sources under-specify a needed detail
  (tie-breaking rule, exact history-corruption detection threshold, etc.), so downstream DATASET/EXPERIMENT artifacts know
  precisely where they must make and document their own methodological choices rather than assuming full parity with the published
  pipeline.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_dependency_files:
  file_list:
  - research_out.json

--- Dependency 2 ---
id: art_24Q1bYB_ULpu
type: dataset
title: Founder-Departure OSS Truck-Factor Corpus
summary: >-
  This dataset mines real GitHub repositories to test whether pre-departure authority diffusion predicts whether an open-source
  project survives its founder stepping away. Candidates (1,615 repos) were discovered via the GitHub Search API stratified
  across 6 languages (Python, JavaScript, Go, Rust, Java, Ruby) and 3 star-count buckets (100-2000, 2000-10000, >10000) to
  avoid confounding popularity with survival. Full commit history for each candidate was pulled via `git clone --filter=blob:none`
  (partial clone, no blob content, unlimited by GitHub API rate limits) plus `git log --name-only`, giving per-commit (author
  email, date, files changed) tuples with no cloning-scale API cost. From this raw history the pipeline computes, per year,
  the exact Degree-of-Authorship metric from Avelino et al. (ICPC 2016): DOA(d,f) = 3.293 + 1.098*FirstAuthor(d,f) + 0.164*Deliveries(d,f)
  - 0.321*ln(1+Acceptances(d,f)), and the Truck Factor via the paper's greedy algorithm (repeatedly remove the highest-file-count
  DOA-primary author while remaining authors still cover >=50% of files). A Truck-Factor-Developer-Detachment (TFDD) is flagged
  the first year the sole (TF=1) truck-factor developer has been silent >=1 year and is confirmed to be the project's founder
  (earliest committer with dominant early-commit share). Algorithm correctness was validated against the paper's own worked
  example (composer/satis): the reproduced TF sequence (1,1,1,2,2,2,...) and TFDD detection matches the paper's Figure 1 exactly.
  Of 216 candidates processed, 32 qualified with a founder-only TFDD plus >=3 years of subsequent history (avoiding right-censoring);
  184 were discarded and logged with reasons (no qualifying TFDD 120, non-software/low-code-fraction 24, too few commits 15,
  right-censored 11, migration/squash mining artifact 11, history too large 3). Each of the 32 output rows (dataset group
  'founder_departure_tfdd_corpus' in full_data_out.json, schema exp_sel_data_out.json) has `input` = a JSON string of pre-TFDD/TFDD-snapshot
  covariates (founder's pre-departure commit share, count of new non-founder DOA-primary file owners in the 6-12mo pre-TFDD
  window, founder's early authorship share, stars, forks, contributor count, language, license, project age, total commits/files,
  history span) and `output` = the survival label (Active_survived / Inactive_did_not_survive per Avelino et al.'s Active/Inactive
  model: did a new truck-factor developer arrive and commit activity persist for >=6 months post-TFDD). Rich metadata_* fields
  on every example carry the full per-year DOA/TF developer-set tables, TFDD date/developer/silence-duration, the pre-TFDD
  window details, TFDD-snapshot covariates, the 18-month post-TFDD monthly commit-count time series, activity bucket (thriving/maintained/dormant/dead),
  repo identity/URL/stars/language/license, and first/last commit dates -- enough for downstream experiment code to recompute
  or verify the authority-diffusion trajectory without re-cloning any repository. The corpus spans 5 languages (Go 7, Ruby
  11, JavaScript 6, Java 5, Rust 3) and both survival outcomes (20 Active_survived, 12 Inactive_did_not_survive), is 175KB
  (well under the 300MB budget), and passed exp_sel_data_out.json schema validation. Mining code (search_candidates.py, mine_repo.py,
  run_mining.py, data.py) is included for full reproducibility and to extend the corpus further if a downstream experiment
  wants a larger sample.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json

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
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

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
TODO 2. Read preview files from dependencies to understand data structure. Use ALL datasets provided — do not skip or select a subset. Read domain handbook if applicable (see <available_domain_handbooks>). Test basic functionality with 'uv run'.
TODO 3. Fully implement our method AND baseline (comparison) as described in artifact plan in './method.py'. Use exp_gen_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant methods or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
```

### [14] HUMAN-USER prompt · 2026-08-21 18:05:02 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [15] SYSTEM-USER prompt · 2026-08-21 18:12:51 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx2
type: experiment
title: Unified-Corpus Re-Test of Pre-Departure Authority Diffusion
summary: >-
  Re-run the three pre-registered tests (BH-FDR regression, matched-pairs bootstrap, within-repo placebo at >=200 draws) on
  the single unified 32-repo dataset artifact instead of independently re-mined data, and add a new window-boundary-noise
  control using non-TFDD repos to separate measurement noise from genuine signal.
runpod_compute_profile: gpu
implementation_pseudocode: |-
  # method.py

  ## 0. Setup
  - load full_data_out.json from dataset dependency (art_24Q1bYB_ULpu), group 'founder_departure_tfdd_corpus'
  - parse each row's `input` JSON string -> covariates dict; `output` -> survival label (Active_survived / Inactive_did_not_survive)
  - parse metadata_* fields -> per-year DOA/TF developer-set tables, TFDD date/developer, pre-TFDD window details, post-TFDD monthly commit series, repo identity/stars/language/license
  - log n=32 total rows, breakdown by language (Go7/Ruby11/JS6/Java5/Rust3) and outcome (20 survived/12 not)
  - if n < 32 or schema mismatch vs dataset summary -> hard fail loudly (do NOT silently drop rows) since corpus-provenance unification is the whole point of this iteration

  ## 1. Baseline replication checks (compare against Avelino et al. and dataset artifact summary)
  - founder-only-TFDD rate in corpus (sanity: should match the 32/216 mining yield already reported)
  - survival rate = 20/32 = 62.5% -> report alongside Avelino et al.'s unconditioned 41% baseline (note directionally different denominator: this is founder-only-TF=1 TFDDs, not all TFDDs)
  - snapshot Cohen's d for developers/commits/files between survivors and non-survivors AT the TFDD year (using existing per-year DOA/TF tables in metadata) -> replicate Avelino et al.'s d=0.13-0.26 negligible-small finding on this corpus as a validity check

  ## 2. Core covariates (reuse from method.py in prior iteration's experiment artifact if available in workspace context; otherwise recompute from metadata fields already present in dataset -- do NOT re-clone/re-mine)
  - founder_pre_departure_commit_share (6-12mo window before TFDD)
  - n_new_nonfounder_doa_owners (distinct accounts reaching DOA-primary file ownership in that window)
  - controls: stars, forks, contributor_count, language (categorical), license (categorical), project_age_days, total_commits, total_files, history_span_days

  ## 3. Test A: BH-FDR logistic + ordinal regression
  - outcome: survival (binary Active_survived/Inactive_did_not_survive); if graded labels exist in metadata (thriving/maintained/dormant/dead activity bucket), ALSO fit ordinal logit as secondary model
  - predictors: founder_pre_departure_commit_share, n_new_nonfounder_doa_owners + controls above
  - with n=32 (20/12 split) and up to 8 predictors, explicitly check separation/rank-deficiency BEFORE fitting: use statsmodels Logit with regularization (L2, small C) as primary if unregularized MLE fails to converge or produces |coef|>10 (classic complete-separation symptom); report convergence diagnostics explicitly
  - apply Benjamini-Hochberg correction across the family of predictor p-values (both diffusion predictors + controls), alpha=0.05, per Avelino et al.'s own procedure
  - report standardized effect sizes (Cohen's d equivalents from standardized logistic coefficients) for diffusion predictors vs size/popularity controls -- success criterion #2 needs the head-to-head comparison
  - IMPORTANT: given last iteration's zero-usable-cell failure, explicitly log cell counts for every stratification (language x outcome, popularity-bucket x outcome) BEFORE attempting stratified analysis; if any planned stratified cell has <3 observations, fall back to a single pooled model with strata as covariates rather than per-stratum fits, and document this deviation

  ## 4. Test B: Matched-pairs nearest-neighbor bootstrap
  - define popularity/size bucket via stars+forks+contributor_count (e.g., k-NN on standardized [log(stars), log(forks), log(contributors)] or simple tercile bucketing given n=32)
  - for each survivor, find nearest non-survivor(s) within bucket (or vice versa) differing in founder_pre_departure_commit_share/n_new_nonfounder_doa_owners
  - if exact matched pairs are too sparse at n=32 (this is what killed the test last iteration): use CALIPER-based matching (accept nearest neighbor within a distance threshold rather than requiring exact bucket equality) and report the caliper value and how many usable pairs it yields; sweep 2-3 caliper widths and report sensitivity
  - bootstrap (>=2000 resamples) the paired difference in survival rate between high-diffusion (founder-share<50% AND >=2 non-founder owners) vs low-diffusion (founder-share>=80%) matched groups; report 95% CI
  - if usable pairs remain 0 even under relaxed caliper: explicitly report as UNTESTABLE (not as a negative result), state the achieved match count, and report the unmatched raw group difference with a big caveat instead of fabricating a bootstrap CI

  ## 5. Test C: Within-repo random-window placebo (raise draws 25 -> 300)
  - for each of the 32 repos, draw 300 random 6-12mo windows from that repo's OWN pre-TFDD history (excluding the true window)
  - recompute founder-share/n_new_nonfounder_doa_owners for each placebo window using the same DOA logic as the true window
  - compute correlation (founder-share vs survival) for each placebo draw -> build empirical null distribution (300 draws x however many repos have sufficient history length for windowing)
  - report true window's r against this refined percentile (finer resolution than prior 25-draw 40th percentile / p=0.615)
  - fixed random seed, log it, for reproducibility

  ## 6. NEW: window-boundary validation control (this iteration's main addition)
  - select 10-15 NON-TFDD repos from the corpus's original candidate pool if available in dataset metadata (repos processed but excluded for 'no qualifying TFDD') -- check mine_repo.py / data.py outputs in dataset artifact workspace for a log of the 120 'no qualifying TFDD' discards; if raw candidate logs aren't retrievable, instead use STABLE (non-departure) periods from repos already in the TFDD corpus itself (e.g., a 6-12mo window >=2 years before the TFDD, far from any detachment event)
  - for each, recompute DOA-based founder-share at 3-5 different 6-12mo windows within that stable period
  - compute within-repo variance of founder-share across these stable-period windows -> this is the 'boundary-noise floor'
  - compare: is the true pre-departure window's effect size (r=0.180 from prior iteration, or newly computed r) distinguishable from this noise floor? Report noise-floor variance alongside the true-window vs placebo-window comparison from Test C
  - this directly tests the reviewer's concern: is window computation itself (not the mechanism) responsible for weak signal

  ## 7. Output
  - write method_out.json: all three test results (A/B/C) + window-boundary-noise control results + baseline replication numbers, each tagged EXECUTED/UNTESTABLE with reasons, confidence intervals, and explicit comparison to prior iteration's numbers (r=0.180, p=0.615, n=30)
  - include a clearly-labeled section: 'What changed vs iter1: unified corpus (32 vs 62/30-usable), placebo draws 25->300, new boundary-noise control'
fallback_plan: >-
  If BH-FDR regression still returns a rank-deficient/non-converging fit even after L2 regularization at n=32 (very plausible
  with ~8 predictors and 12 minority-class events): drop to a minimal 2-3 predictor model (just founder_pre_departure_commit_share
  + n_new_nonfounder_doa_owners + one size control like log(stars)) and report that as the primary regression, with the full
  model reported separately as exploratory/unstable. If matched-pairs bootstrap still yields zero usable pairs even with a
  wide caliper: report it as UNTESTABLE at this corpus size (as required by the artifact direction's honesty framing), and
  substitute a simple unmatched two-group comparison (Mann-Whitney U on survival rate or founder-share) with an explicit caveat
  that popularity is not controlled. If the dataset artifact's metadata does not contain enough granularity to recompute placebo/stable-period
  windows without re-cloning (e.g., missing per-commit timestamps needed for arbitrary window slicing): fall back to using
  only the windows/years already present in metadata_* (the yearly DOA/TF tables) rather than attempting fine-grained re-slicing,
  and clearly note this as a resolution limitation rather than silently interpolating. If the non-TFDD stable-period repos
  are unavailable from dataset metadata: use TFDD repos' own multi-year-before-departure windows as the stable-period proxy,
  clearly labeled as a substitution.
testing_plan: >-
  1. First load and validate the dataset artifact's full_data_out.json: assert exactly 32 rows in the founder_departure_tfdd_corpus
  group, spot-check 2-3 rows' parsed `input`/`output`/metadata against the dataset artifact's own textual summary (20 survived/12
  not, language breakdown Go7/Ruby11/JS6/Java5/Rust3) before writing any analysis code -- this catches parsing bugs immediately
  rather than after hours of downstream computation. 2. Run the baseline-replication step (Test 0) first, alone, and check
  the reproduced snapshot Cohen's d is in a similar negligible-small range to Avelino et al.'s d=0.13-0.26 -- if wildly different,
  the covariate parsing or DOA replication has a bug, fix before proceeding. 3. Run Test C (placebo) at only 10 draws per
  repo first as a smoke test to confirm the windowing/DOA recomputation code runs without error and produces a sane correlation
  distribution, THEN scale to the full 300 draws (per aii-long-running-tasks staged-scaling pattern) -- watch wall-clock time
  at 10 draws x 32 repos to extrapolate whether 300 draws is feasible in the time budget; if DOA recomputation per window
  is expensive, consider caching per-commit author/file data once per repo and only re-aggregating per window. 4. Run Test
  A (regression) and immediately print convergence diagnostics (coefficient magnitudes, standard errors) before trusting any
  p-value; log cell counts for every planned stratification before attempting it. 5. Run Test B (matched-pairs) and log the
  achieved match count at each caliper width tried -- if the tightest caliper gives 0 pairs, do not silently widen without
  logging the widening as a documented methodological choice. 6. Run the new window-boundary-noise control last (Test 6) since
  it depends on having working window-recomputation code from Test C. 7. Before finalizing, cross-check that the reported
  r/p-values for the true pre-departure window are computed identically to prior iteration's method (same DOA formula, same
  commit-share definition) so the comparison to r=0.180/p=0.615 is apples-to-apples -- if the unified corpus changes these
  numbers, explicitly report both old and new values side by side.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_0qwvnbyIv0EL
type: research
title: Founder-Departure Mining Recipe Verified
summary: >-
  This research artifact verifies, against the two primary Avelino et al. papers (ICPC 2016, arXiv:1604.06766; ESEM 2019,
  arXiv:1906.08058), the exact reproducible methodology needed to mine founder Truck Factor Developer Detachment (TFDD) events
  and study pre-departure authority-diffusion trajectories from public git histories. Key deliverables: (1) the verified Degree-of-Authorship
  (DOA) formula DOA=3.293+1.098*FA+0.164*DL-0.321*ln(1+AC) with FA/DL/AC precisely defined -- critically, DL is confirmed
  to be a raw commit-count term (number of the developer's own commits to the file), NOT a recency/days-since-last-change
  term as an earlier working hypothesis assumed, and this correction is load-bearing for any downstream implementation; (2)
  the exact 0.75-normalized / 3.293-absolute authorship threshold and its empirical tuning method; (3) the greedy Truck Factor
  algorithm pseudocode with exact coverage-check-before-removal semantics; (4) the verified 1-year abandoner threshold with
  the FULL five-way harmonic-mean sensitivity table (3mo/6mo/1yr/1.5yr/2yr); (5) confirmation that Active/Inactive/survival
  is a strictly BINARY state machine keyed to the LAST observed TFDD (not a graded thriving/dormant/dead framing, which has
  no basis in the primary sources) and that there is no fixed post-TFDD survival window (e.g. no 18-month cutoff exists in
  the paper -- survival is measured via yearly TF recomputation through the dataset collection date); (6) confirmation that
  DOA/TF was only ever validated at YEARLY full-history snapshots, never on arbitrary sub-year windows, meaning any 'pre-departure
  6-12 month window' DOA recomputation is a genuine unvalidated methodological extension that must be built and justified
  independently, with an explicit note on the FA window-boundary ambiguity this creates; (7) a concrete PyDriller-based local
  extraction code sketch for computing per-file per-author FA/DL/AC from a full local clone with no GitHub API dependency;
  (8) a local identity-resolution heuristic (normalize name/email, special-case GitHub noreply numeric IDs, union-find merge,
  bot exclusion, VCS-migration-artifact screening) offered as an explicitly UNVALIDATED substitute for Avelino et al.'s own
  GitHub-API-based alias resolution (median 11% alias rate); (9) pointer to the original authors' public Java reference implementation
  (aserg-ufmg/Truck-Factor, ~240 stars) as the correctness check of record; (10) a vetted 10-entry candidate seed list of
  real founder-handoff open-source repositories with explicit EXCLUDE/CAUTION flags (e.g. node-sass is project death not succession;
  youtube-dl->yt-dlp is a fork not a same-repo handoff; Homebrew and scikit-learn are likely already TF>1 and poor fits for
  a strict single-founder TF=1 construct), offered as a DATASET-artifact starting point rather than a claim of confirmed TFDD
  status. All corpus-selection parameters (top-500-starred x 6 languages, 1,932-project final corpus, exclusion criteria)
  are reproduced exactly. Eight explicit gaps/flags are documented where the primary sources under-specify a needed detail
  (tie-breaking rule, exact history-corruption detection threshold, etc.), so downstream DATASET/EXPERIMENT artifacts know
  precisely where they must make and document their own methodological choices rather than assuming full parity with the published
  pipeline.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_dependency_files:
  file_list:
  - research_out.json

--- Dependency 2 ---
id: art_24Q1bYB_ULpu
type: dataset
title: Founder-Departure OSS Truck-Factor Corpus
summary: >-
  This dataset mines real GitHub repositories to test whether pre-departure authority diffusion predicts whether an open-source
  project survives its founder stepping away. Candidates (1,615 repos) were discovered via the GitHub Search API stratified
  across 6 languages (Python, JavaScript, Go, Rust, Java, Ruby) and 3 star-count buckets (100-2000, 2000-10000, >10000) to
  avoid confounding popularity with survival. Full commit history for each candidate was pulled via `git clone --filter=blob:none`
  (partial clone, no blob content, unlimited by GitHub API rate limits) plus `git log --name-only`, giving per-commit (author
  email, date, files changed) tuples with no cloning-scale API cost. From this raw history the pipeline computes, per year,
  the exact Degree-of-Authorship metric from Avelino et al. (ICPC 2016): DOA(d,f) = 3.293 + 1.098*FirstAuthor(d,f) + 0.164*Deliveries(d,f)
  - 0.321*ln(1+Acceptances(d,f)), and the Truck Factor via the paper's greedy algorithm (repeatedly remove the highest-file-count
  DOA-primary author while remaining authors still cover >=50% of files). A Truck-Factor-Developer-Detachment (TFDD) is flagged
  the first year the sole (TF=1) truck-factor developer has been silent >=1 year and is confirmed to be the project's founder
  (earliest committer with dominant early-commit share). Algorithm correctness was validated against the paper's own worked
  example (composer/satis): the reproduced TF sequence (1,1,1,2,2,2,...) and TFDD detection matches the paper's Figure 1 exactly.
  Of 216 candidates processed, 32 qualified with a founder-only TFDD plus >=3 years of subsequent history (avoiding right-censoring);
  184 were discarded and logged with reasons (no qualifying TFDD 120, non-software/low-code-fraction 24, too few commits 15,
  right-censored 11, migration/squash mining artifact 11, history too large 3). Each of the 32 output rows (dataset group
  'founder_departure_tfdd_corpus' in full_data_out.json, schema exp_sel_data_out.json) has `input` = a JSON string of pre-TFDD/TFDD-snapshot
  covariates (founder's pre-departure commit share, count of new non-founder DOA-primary file owners in the 6-12mo pre-TFDD
  window, founder's early authorship share, stars, forks, contributor count, language, license, project age, total commits/files,
  history span) and `output` = the survival label (Active_survived / Inactive_did_not_survive per Avelino et al.'s Active/Inactive
  model: did a new truck-factor developer arrive and commit activity persist for >=6 months post-TFDD). Rich metadata_* fields
  on every example carry the full per-year DOA/TF developer-set tables, TFDD date/developer/silence-duration, the pre-TFDD
  window details, TFDD-snapshot covariates, the 18-month post-TFDD monthly commit-count time series, activity bucket (thriving/maintained/dormant/dead),
  repo identity/URL/stars/language/license, and first/last commit dates -- enough for downstream experiment code to recompute
  or verify the authority-diffusion trajectory without re-cloning any repository. The corpus spans 5 languages (Go 7, Ruby
  11, JavaScript 6, Java 5, Rust 3) and both survival outcomes (20 Active_survived, 12 Inactive_did_not_survive), is 175KB
  (well under the 300MB budget), and passed exp_sel_data_out.json schema validation. Mining code (search_candidates.py, mine_repo.py,
  run_mining.py, data.py) is included for full reproducibility and to extend the corpus further if a downstream experiment
  wants a larger sample.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json

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
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

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
TODO 1. Use aii-json skill's format script with `--input method_out.json` to generate full, mini, and preview versions. If not in your workspace (see <workspace> above), copy them there. Run 'ls -lh' to verify these three files exist (DO NOT read them).
TODO 2. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to method_out.json and full_method_out.json.
TODO 3. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ExperimentExpectedFiles": {
      "description": "All expected output files from experiment artifact.",
      "properties": {
        "script": {
          "description": "Path to method.py script. Example: 'method.py'",
          "title": "Script",
          "type": "string"
        },
        "full_output": {
          "description": "Full method output JSON file. Example: 'full_method_out.json'",
          "title": "Full Output",
          "type": "string"
        },
        "mini_output": {
          "description": "Mini method output JSON file. Example: 'mini_method_out.json'",
          "title": "Mini Output",
          "type": "string"
        },
        "preview_output": {
          "description": "Preview method output JSON file. Example: 'preview_method_out.json'",
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
      "title": "ExperimentExpectedFiles",
      "type": "object"
    }
  },
  "description": "Experiment artifact \u2014 structured output + file metadata.\n\nImplements research methodology with baseline comparison.\nProduces method.py and method_out.json files.",
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
      "$ref": "#/$defs/ExperimentExpectedFiles",
      "description": "All output files you created. Must include method.py script plus full/mini/preview method output JSON files."
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
  "title": "ExperimentArtifact",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````
