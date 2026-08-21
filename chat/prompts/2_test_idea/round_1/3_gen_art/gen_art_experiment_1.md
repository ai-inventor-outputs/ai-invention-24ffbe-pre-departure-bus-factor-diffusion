# gen_art_experiment_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `iter1_0b7b616dce39` — Does Pre-Departure Authority Diffusion Predict Open-Source Project Survival? A Unified-Corpus Retest with a Window-Boundary-Noise Control
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 15:43:02 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx3
type: experiment
title: Does Authority Diffusion Before Founder Exit Predict Survival
summary: >-
  Recompute Avelino et al.'s (ESEM 2019) DOA/Truck-Factor/TFDD pipeline on GitHub repos, add a NEW pre-departure (6-12 months
  before TFDD) authority-diffusion measurement (founder commit-share, count of independent non-founder DOA file-owners), score
  18-month post-TFDD survival with their Active/Inactive/recovery model, and test via regression + matched-pairs + window-shuffle
  placebo whether the pre-departure trajectory predicts survival better than the snapshot size/popularity covariates their
  paper showed were null (d=0.13-0.26).
runpod_compute_profile: cpu_heavy
implementation_pseudocode: "# === STAGE 0: Setup & repo selection (depends on DATASET artifact of GitHub repo git histories)\
  \ ===\n# This EXPERIMENT depends on a DATASET artifact providing cloned/clonable git histories\n# (or pre-extracted commit/file-change\
  \ logs) for a sample of popular GitHub repos across\n# multiple languages, analogous to Avelino et al.'s 1,932-repo corpus\
  \ (top-starred repos,\n# 6 languages: Java, Python, JavaScript, C++, Ruby, PHP or similar). Load that dataset's\n# manifest\
  \ (repo_id, clone_url_or_local_path, stars, forks, contributor_count, language,\n# license, first_commit_date, last_commit_date).\n\
  #\n# FILTER (mirrors Avelino et al. 'perils of mining GitHub' exclusions):\n#   - drop repos with < 2 years of commit history\
  \ (need room for pre-TFDD window + TFDD +\n#     18mo post-TFDD survival window without right-censoring => require >= 3\
  \ yrs total, per\n#     the hypothesis's own assumption)\n#   - drop non-software repos (awesome-lists, book/doc repos):\
  \ heuristic filter on file\n#     extensions (>= 60% of tracked files must have a recognized source-code extension for\n\
  #     the repo's declared language) + repo-name/description regex for 'awesome-', 'book',\n#     'course', 'interview-questions'\
  \ etc.\n#   - drop repos with obvious history-loss artifacts (first commit timestamp suspiciously\n#     dense/batched,\
  \ i.e. > 50% of a repo's commits sharing the exact same author-date\n#     within a 60-second window -- signature of a squashed/re-imported\
  \ history)\n# LOG every exclusion with reason and count so the executor can report a CONSORT-style\n# filtering table in\
  \ the output JSON.\n\n# === STAGE 1: Build per-repo commit/file-change event log ===\nfor repo in filtered_repos:\n    events\
  \ = extract_commit_log(repo)  # (commit_sha, author_email, author_date, files_touched[])\n    resolve_author_aliases(events)\
  \     # merge same-person accounts via GitHub-API noreply-email\n                                        # pattern (id+username@users.noreply.github.com)\
  \ and by\n                                        # exact-name-match fallback when API email lookup fails;\n           \
  \                             # log alias-merge rate per repo (Avelino et al. median 11%)\n    events = sort_by(author_date)\n\
  \n# === STAGE 2: Yearly DOA + Truck Factor (Avelino et al. 2016 ICPC algorithm, reused verbatim) ===\n# DOA(a, f) = 3.293\
  \ + 1.098*FA(a,f) - 0.164*ln(1+DL(a,f)) + 0.321*ln(1+AC(a,f))\n#   FA(a,f)  = 1 if a authored file f's FIRST commit, else\
  \ 0\n#   AC(a,f)  = count of a's commits touching f (as of the snapshot date)\n#   DL(a,f)  = number of a's OWN commits\
  \ to f that happened after a's LAST commit to f\n#              minus... (verify exact DL definition against Fritz et al.\
  \ 2014 / Avelino 2016\n#              ICPC paper text at snapshot time -- executor MUST fetch and fetch_grep the ICPC\n\
  #              2016 paper (arXiv or ACM DL) for the precise DL formula before implementing;\n#              do not guess\
  \ it from memory)\n# For each repo, for each MONTHLY (not just yearly -- we need finer granularity to locate the\n# founder-only\
  \ TFDD month and the 6-12mo pre-window precisely) snapshot date:\n#   - compute DOA(a,f) for every (author, file) pair using\
  \ only commits with author_date <= snapshot\n#   - primary_owner(f, snapshot) = argmax_a DOA(a,f) restricted to top-DOA\
  \ holder\n#   - TF(snapshot) = greedily remove authors (highest total number of files they are\n#     primary_owner of)\
  \ one at a time until < 50% of repo's files have a remaining primary\n#     owner with DOA above the Avelino DOA-authorship\
  \ threshold (>= 3.293, i.e. FA=1 baseline);\n#     TF = number of authors removed to cross that threshold\n#   - TF_developer_set(snapshot)\
  \ = the set of authors removed in that greedy process\n\n# === STAGE 3: Identify each repo's founder & first founder-only\
  \ TFDD ===\nfor repo in repos_with_doa_computed:\n    founder = author of repo's very first commit (or first N=3 commits\
  \ if the true first\n              commit is a scaffolding/README-only commit -- use first commit with >=1\n           \
  \   source file changed)\n    # TFDD = point at which every developer in the CURRENT TF_developer_set has gone silent\n\
  \    # (no commits) for >= 1 year (Avelino et al.'s empirically-selected best threshold,\n    # harmonic-mean precision\
  \ 0.66). Scan monthly snapshots forward in time; a TFDD occurs\n    # at month m if TF_developer_set(m) all have zero commits\
  \ in [m, m+12mo).\n    tfdd_events = detect_tfdd_events(repo)  # list of (month, tf_developer_set_at_detachment)\n    founder_only_tfdds\
  \ = [e for e in tfdd_events if e.tf_developer_set == {founder} and\n                           founder in e.tf_developer_set\
  \ and len(e.tf_developer_set) == 1]\n    if not founder_only_tfdds: skip repo  # not in the target subset (~66% of TFDDs\
  \ are TF=1\n                                            # per Avelino et al., so expect most founder-led\n             \
  \                               # single-TF-dev repos to qualify -- but ALSO require\n                                 \
  \           # founder to literally BE that lone TF developer,\n                                            # which is a\
  \ stricter subset the plan must track)\n    first_founder_tfdd = min(founder_only_tfdds, key=lambda e: e.month)\n    # require\
  \ >= 12 months of history BEFORE this TFDD (for the pre-window) and >= 18 months\n    # AFTER it (for survival scoring)\
  \ -- else skip (right/left-censored)\n\n# === STAGE 4: NEW measurement -- pre-departure authority-diffusion trajectory ===\n\
  for repo in repos_with_founder_tfdd:\n    tfdd_month = first_founder_tfdd.month\n    window = [tfdd_month - 12mo, tfdd_month\
  \ - 6mo]   # the 6-12-month PRE-departure window\n    commits_in_window = events filtered to author_date in window\n   \
  \ founder_share = count(commits_in_window where author==founder) / count(commits_in_window)\n    # distinct non-founder\
  \ DOA-file-owners reached DURING the window: for each month-end\n    # snapshot INSIDE the window, recompute primary_owner(f,\
  \ snapshot) for all files touched\n    # up to that snapshot; collect the set of non-founder authors who are primary_owner\
  \ of\n    # >= 1 file at ANY snapshot inside the window (use the running DOA state already computed\n    # in Stage 2, just\
  \ re-slice it to the window's snapshot dates -- do NOT recompute from\n    # scratch, reuse memoized per-snapshot DOA tables\
  \ for efficiency)\n    n_doa_owners = len(distinct non-founder primary owners across window snapshots)\n    diffusion_score\
  \ = {founder_share, n_doa_owners}  # primary predictors\n\n# === STAGE 5: Survival outcome (Avelino et al.'s Active/Inactive/recovery\
  \ model) ===\nfor repo in repos_with_diffusion_score:\n    post = events filtered to author_date in [tfdd_month, tfdd_month\
  \ + 18mo]\n    # Active/Inactive state machine: repo is Inactive from tfdd_month until a NEW developer\n    # (not in the\
  \ departed TF set) attains TF-developer status (joins the current\n    # TF_developer_set at some post-TFDD monthly snapshot)\
  \ -- that event flips it back Active.\n    recovered = any(post-TFDD snapshot where a new author is in TF_developer_set)\n\
  \    # graded outcome (thriving/maintained/dormant/dead) -- define via post-TFDD commit\n    # velocity relative to pre-TFDD\
  \ baseline, using quartile cut points the executor derives\n    # empirically from the corpus's own post-TFDD commit-count\
  \ distribution (report the exact\n    # cutpoints used, since Avelino et al.'s paper does not give exact numeric thresholds\
  \ for\n    # the 4 labels -- executor should fetch_grep the ESEM 2019 paper for their operational\n    # definition of the\
  \ 4 states before inventing one from scratch)\n    binary_survival = recovered  # matches Avelino et al.'s binary survive/not-survive\
  \ stat\n\n# === STAGE 6: Confound controls ===\nfor repo: controls = {log_stars, log_forks, contributor_count, language,\
  \ license,\n                       developers_at_tfdd, commits_at_tfdd, files_at_tfdd}  # the snapshot\n               \
  \        # covariates Avelino et al. found null (d=0.13-0.26) -- MUST be\n                       # recomputed here identically\
  \ to compare standardized effect sizes\n\n# === STAGE 7: Analysis (a) regression ===\nX = [founder_share, n_doa_owners,\
  \ log_stars, log_forks, contributor_count,\n     developers_at_tfdd, commits_at_tfdd, files_at_tfdd] + language/license\
  \ one-hot\nlogit_model = sm.Logit(binary_survival, standardize(X)).fit()          # statsmodels\nordinal_model = statsmodels.miscmodels.ordinal_model.OrderedModel(\n\
  \                    graded_outcome, standardize(X), distr='logit').fit()\nBH_correct(p_values_of_all_coefficients)  # statsmodels.stats.multitest.multipletests,\
  \ method='fdr_bh'\nreport: standardized_coef, BH_p, compare |coef(founder_share)|, |coef(n_doa_owners)| vs\n        |coef(log_stars)|,\
  \ |coef(developers_at_tfdd)| etc.\n\n# === STAGE 8: Analysis (b) matched-pairs / stratified comparison ===\nbuckets = stratify_by(log_stars_decile,\
  \ log_forks_decile, contributor_count_bucket)\nhigh_diffusion = repos where founder_share < 0.50 AND n_doa_owners >= 2\n\
  low_diffusion  = repos where founder_share >= 0.80\nfor each bucket: pair high_diffusion repos to low_diffusion repos via\
  \ nearest-neighbor on\n                 (log_stars, log_forks, contributor_count) using sklearn NearestNeighbors\n     \
  \            or scipy cKDTree, caliper = 0.2 * pooled std of matching covariates\nsurvival_rate_ratio = mean(binary_survival\
  \ | high_diffusion, matched) / \n                       mean(binary_survival | low_diffusion, matched)\nbootstrap_CI = bootstrap(survival_rate_ratio,\
  \ n_resamples=10000, method='percentile')\nreport ratio, 95% CI, compare against Avelino et al.'s unconditioned 41% baseline\n\
  \n# === STAGE 9: Falsification / placebo check ===\nnull_ratios = []\nfor trial in range(1000):\n    for repo: relocate\
  \ window to a uniformly random start month in\n              [first_commit_date, tfdd_month - window_length - 1mo]  # same\
  \ length, must stay\n              strictly before the TRUE window's start to avoid leakage; recompute\n              founder_share_null,\
  \ n_doa_owners_null using the SAME memoized per-snapshot DOA\n              tables from Stage 2 (cheap re-slice, no recomputation)\n\
  \    rerun analysis (a) and (b) with the null-window predictors\n    null_ratios.append(placebo_survival_rate_ratio)\nreport:\
  \ true_effect_percentile_in_null_distribution, empirical p-value =\n        (1 + sum(null_ratios >= true_ratio)) / (1 +\
  \ len(null_ratios))\n\n# === STAGE 10: Assemble method_out.json ===\noutput = {\n  'corpus_stats': {n_repos_input, n_repos_after_filters,\
  \ n_founder_only_tfdds, exclusion_table},\n  'baseline_replication': {tfdd_rate, survival_rate, snapshot_effect_sizes},\
  \  # sanity check\n                                                                              # against Avelino\n   \
  \                                                                           # et al.'s reported\n                      \
  \                                                        # 16% TFDD rate /\n                                           \
  \                                   # 41% survival / d\n  'regression_results': {...},\n  'matched_pairs_results': {...},\n\
  \  'placebo_results': {...},\n  'success_criteria_verdict': {criterion_1_pass_bool, criterion_2_pass_bool,\n           \
  \                     criterion_3_pass_bool, notes}\n}"
fallback_plan: >-
  Layer the fallbacks by what breaks first, from cheapest degradation to most fundamental: (1) FULL git clones too slow/large
  -- if the DATASET artifact only supplies shallow clones or pre-extracted commit logs without full blob history, that's fine:
  DOA only needs (author, file, commit_date) triples, not blob contents, so nothing in the pipeline actually requires full
  clones; explicitly do NOT re-clone anything, use whatever the dataset provides. (2) Corpus too small after filtering (e.g.,
  <40-50 founder-only-TFDD repos survive the >=3-year-history + founder-only-TF=1 filters) -- relax the TF=1-at-departure
  requirement to TF<=2 with founder in the departing set and note the deviation explicitly in the output, since Avelino et
  al. themselves report 66% of TFDDs are TF=1 so a large corpus should still clear the stricter filter; if it still doesn't,
  reduce required post-TFDD survival window from 18 to 12 months (report both) rather than dropping repos, and flag this as
  a limitation rather than silently changing the headline metric. (3) DOA/TF computation too slow at monthly granularity across
  the full corpus -- switch from monthly to quarterly snapshots for Stage 2's running DOA state (this is the compute-heavy
  step: O(commits x files) per snapshot); the pre-departure window (6-12mo) and TFDD detection can tolerate quarterly resolution
  with a documented +/-1.5 month fuzz on the TFDD date, which does not materially change founder_share or n_doa_owners since
  both are already window-aggregate statistics. (4) statsmodels' OrderedModel fails to converge on the graded 4-level outcome
  (common with small/imbalanced strata) -- fall back to the binary logistic regression only for the primary claim (success
  criterion 2 only requires the diffusion predictors' significance, which the binary model alone can establish) and report
  the ordinal model as exploratory/best-effort with a convergence-failure caveat rather than blocking the whole artifact on
  it. (5) Matched-pairs bucket has too few pairs per stratum for a stable bootstrap CI (e.g., <10 pairs in the high-diffusion
  vs low-diffusion contrast within a size bucket) -- pool across size buckets and instead include the matching covariates
  (log_stars, log_forks, contributor_count) as regression adjustors in a single pooled matched-set analysis (essentially collapsing
  (a) and (b) into one covariate-adjusted comparison), clearly labeled as a fallback deviation from the pre-registered stratified
  design in success_criteria_verdict.notes. (6) If the DATASET artifact this experiment depends on does not actually provide
  enough repos with the founder-identifiable-first-commit property (e.g., many repos were imported from an external VCS with
  no clean initial commit) -- restrict founder identification to repos where the first commit's author authored >= 3 of the
  first 5 commits (a robustness check against a single miscategorized scaffolding commit), and report the fraction of repos
  excluded for unidentifiable founders as part of the exclusion table so the reader can judge the founder-only subset's representativeness.
  Under no circumstances should the executor fabricate or downsample results to hit the success-criteria thresholds -- report
  a null/negative result plainly if the corpus and analysis genuinely produce one; a rigorous null result on this question
  is itself a valid, reportable outcome given Avelino et al.'s own snapshot-null precedent.
testing_plan: >-
  1. UNIT-TEST DOA/TF logic on a synthetic 3-file, 4-author toy repo with hand-computed expected DOA values and a known TF
  set BEFORE running on any real data -- construct commit sequences where the expected primary owner, TF size, and TFDD timing
  are unambiguous by hand-derivation, and assert the code reproduces them exactly. This catches formula/off-by-one errors
  cheaply since the full DOA formula (particularly the DL term) must be verified against the ICPC 2016 paper text rather than
  guessed. 2. SMOKE TEST on 3-5 real, well-known single-founder repos with a documented founder departure the executor can
  sanity-check by eye (e.g., search for OSS projects with public 'founder handed off maintenance' blog posts/README history)
  -- confirm the pipeline's detected TFDD month is within a few months of the publicly known handoff date, and that the pre-TFDD
  founder_share trend direction (declining vs not) matches what a manual `git shortlog` inspection of that repo's commit history
  shows for the year before handoff. 3. BASELINE-REPLICATION CHECK on the full filtered corpus before running the NEW diffusion
  analysis: verify the pipeline's own aggregate stats are in the right ballpark against Avelino et al.'s published numbers
  -- TFDD rate should land near their 16% (not required to match exactly since the corpus differs, but order-of-magnitude
  and general directionality, e.g. TFDD rate should not come out as 90% or 1%, would indicate a pipeline bug), TF=1-at-departure
  share near their 66%, and overall post-TFDD binary survival rate near their 41% -- treat large deviations (e.g., >2x off)
  as a signal to debug the TFDD-detection or survival-scoring logic before trusting the new diffusion results. Also directly
  recompute the size/popularity snapshot effect sizes (developers/commits/files at TFDD, survivors vs non-survivors) and confirm
  they replicate as negligible-to-small (d roughly in the 0.1-0.3 range, same sign direction) as reported in the ESEM 2019
  paper -- this is the load-bearing sanity check, since the entire hypothesis is that the NEW pre-departure signal succeeds
  precisely where this snapshot signal is known to fail; if the replication check itself produces a strong snapshot effect
  where Avelino et al. found none, that indicates a corpus-construction or measurement discrepancy needing resolution before
  proceeding to the novel analysis. 4. SCALE GRADUALLY: run the full pipeline (Stages 1-6) on a 20-30 repo mini-sample first,
  inspect the diffusion-score distribution and survival labels by hand for a handful of cases, confirm nothing is degenerate
  (e.g., founder_share always exactly 0 or 1, n_doa_owners always 0) before scaling to the full corpus and before launching
  the 500-1000-iteration placebo loop, which is the single most expensive step and should only run once Stages 1-8 are validated
  end-to-end on the mini-sample. 5. Track and report cumulative OpenRouter spend if any LLM calls are used for repo/language
  filtering heuristics (should be $0 or near-$0 for this artifact -- the entire pipeline is deterministic git-log analysis
  and statistics, not LLM-driven; if the executor finds itself needing an LLM call anywhere in this pipeline, that is a signal
  the approach has drifted from what was planned and should be reconsidered).
</artifact_plan>



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

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
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

### [2] HUMAN-USER prompt · 2026-08-21 15:43:02 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-json · 2026-08-21 15:43:38 UTC

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

### [4] SKILL-INPUT — aii-python · 2026-08-21 15:43:46 UTC

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

### [5] SYSTEM-USER prompt · 2026-08-21 15:54:17 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx3
type: experiment
title: Does Authority Diffusion Before Founder Exit Predict Survival
summary: >-
  Recompute Avelino et al.'s (ESEM 2019) DOA/Truck-Factor/TFDD pipeline on GitHub repos, add a NEW pre-departure (6-12 months
  before TFDD) authority-diffusion measurement (founder commit-share, count of independent non-founder DOA file-owners), score
  18-month post-TFDD survival with their Active/Inactive/recovery model, and test via regression + matched-pairs + window-shuffle
  placebo whether the pre-departure trajectory predicts survival better than the snapshot size/popularity covariates their
  paper showed were null (d=0.13-0.26).
runpod_compute_profile: cpu_heavy
implementation_pseudocode: "# === STAGE 0: Setup & repo selection (depends on DATASET artifact of GitHub repo git histories)\
  \ ===\n# This EXPERIMENT depends on a DATASET artifact providing cloned/clonable git histories\n# (or pre-extracted commit/file-change\
  \ logs) for a sample of popular GitHub repos across\n# multiple languages, analogous to Avelino et al.'s 1,932-repo corpus\
  \ (top-starred repos,\n# 6 languages: Java, Python, JavaScript, C++, Ruby, PHP or similar). Load that dataset's\n# manifest\
  \ (repo_id, clone_url_or_local_path, stars, forks, contributor_count, language,\n# license, first_commit_date, last_commit_date).\n\
  #\n# FILTER (mirrors Avelino et al. 'perils of mining GitHub' exclusions):\n#   - drop repos with < 2 years of commit history\
  \ (need room for pre-TFDD window + TFDD +\n#     18mo post-TFDD survival window without right-censoring => require >= 3\
  \ yrs total, per\n#     the hypothesis's own assumption)\n#   - drop non-software repos (awesome-lists, book/doc repos):\
  \ heuristic filter on file\n#     extensions (>= 60% of tracked files must have a recognized source-code extension for\n\
  #     the repo's declared language) + repo-name/description regex for 'awesome-', 'book',\n#     'course', 'interview-questions'\
  \ etc.\n#   - drop repos with obvious history-loss artifacts (first commit timestamp suspiciously\n#     dense/batched,\
  \ i.e. > 50% of a repo's commits sharing the exact same author-date\n#     within a 60-second window -- signature of a squashed/re-imported\
  \ history)\n# LOG every exclusion with reason and count so the executor can report a CONSORT-style\n# filtering table in\
  \ the output JSON.\n\n# === STAGE 1: Build per-repo commit/file-change event log ===\nfor repo in filtered_repos:\n    events\
  \ = extract_commit_log(repo)  # (commit_sha, author_email, author_date, files_touched[])\n    resolve_author_aliases(events)\
  \     # merge same-person accounts via GitHub-API noreply-email\n                                        # pattern (id+username@users.noreply.github.com)\
  \ and by\n                                        # exact-name-match fallback when API email lookup fails;\n           \
  \                             # log alias-merge rate per repo (Avelino et al. median 11%)\n    events = sort_by(author_date)\n\
  \n# === STAGE 2: Yearly DOA + Truck Factor (Avelino et al. 2016 ICPC algorithm, reused verbatim) ===\n# DOA(a, f) = 3.293\
  \ + 1.098*FA(a,f) - 0.164*ln(1+DL(a,f)) + 0.321*ln(1+AC(a,f))\n#   FA(a,f)  = 1 if a authored file f's FIRST commit, else\
  \ 0\n#   AC(a,f)  = count of a's commits touching f (as of the snapshot date)\n#   DL(a,f)  = number of a's OWN commits\
  \ to f that happened after a's LAST commit to f\n#              minus... (verify exact DL definition against Fritz et al.\
  \ 2014 / Avelino 2016\n#              ICPC paper text at snapshot time -- executor MUST fetch and fetch_grep the ICPC\n\
  #              2016 paper (arXiv or ACM DL) for the precise DL formula before implementing;\n#              do not guess\
  \ it from memory)\n# For each repo, for each MONTHLY (not just yearly -- we need finer granularity to locate the\n# founder-only\
  \ TFDD month and the 6-12mo pre-window precisely) snapshot date:\n#   - compute DOA(a,f) for every (author, file) pair using\
  \ only commits with author_date <= snapshot\n#   - primary_owner(f, snapshot) = argmax_a DOA(a,f) restricted to top-DOA\
  \ holder\n#   - TF(snapshot) = greedily remove authors (highest total number of files they are\n#     primary_owner of)\
  \ one at a time until < 50% of repo's files have a remaining primary\n#     owner with DOA above the Avelino DOA-authorship\
  \ threshold (>= 3.293, i.e. FA=1 baseline);\n#     TF = number of authors removed to cross that threshold\n#   - TF_developer_set(snapshot)\
  \ = the set of authors removed in that greedy process\n\n# === STAGE 3: Identify each repo's founder & first founder-only\
  \ TFDD ===\nfor repo in repos_with_doa_computed:\n    founder = author of repo's very first commit (or first N=3 commits\
  \ if the true first\n              commit is a scaffolding/README-only commit -- use first commit with >=1\n           \
  \   source file changed)\n    # TFDD = point at which every developer in the CURRENT TF_developer_set has gone silent\n\
  \    # (no commits) for >= 1 year (Avelino et al.'s empirically-selected best threshold,\n    # harmonic-mean precision\
  \ 0.66). Scan monthly snapshots forward in time; a TFDD occurs\n    # at month m if TF_developer_set(m) all have zero commits\
  \ in [m, m+12mo).\n    tfdd_events = detect_tfdd_events(repo)  # list of (month, tf_developer_set_at_detachment)\n    founder_only_tfdds\
  \ = [e for e in tfdd_events if e.tf_developer_set == {founder} and\n                           founder in e.tf_developer_set\
  \ and len(e.tf_developer_set) == 1]\n    if not founder_only_tfdds: skip repo  # not in the target subset (~66% of TFDDs\
  \ are TF=1\n                                            # per Avelino et al., so expect most founder-led\n             \
  \                               # single-TF-dev repos to qualify -- but ALSO require\n                                 \
  \           # founder to literally BE that lone TF developer,\n                                            # which is a\
  \ stricter subset the plan must track)\n    first_founder_tfdd = min(founder_only_tfdds, key=lambda e: e.month)\n    # require\
  \ >= 12 months of history BEFORE this TFDD (for the pre-window) and >= 18 months\n    # AFTER it (for survival scoring)\
  \ -- else skip (right/left-censored)\n\n# === STAGE 4: NEW measurement -- pre-departure authority-diffusion trajectory ===\n\
  for repo in repos_with_founder_tfdd:\n    tfdd_month = first_founder_tfdd.month\n    window = [tfdd_month - 12mo, tfdd_month\
  \ - 6mo]   # the 6-12-month PRE-departure window\n    commits_in_window = events filtered to author_date in window\n   \
  \ founder_share = count(commits_in_window where author==founder) / count(commits_in_window)\n    # distinct non-founder\
  \ DOA-file-owners reached DURING the window: for each month-end\n    # snapshot INSIDE the window, recompute primary_owner(f,\
  \ snapshot) for all files touched\n    # up to that snapshot; collect the set of non-founder authors who are primary_owner\
  \ of\n    # >= 1 file at ANY snapshot inside the window (use the running DOA state already computed\n    # in Stage 2, just\
  \ re-slice it to the window's snapshot dates -- do NOT recompute from\n    # scratch, reuse memoized per-snapshot DOA tables\
  \ for efficiency)\n    n_doa_owners = len(distinct non-founder primary owners across window snapshots)\n    diffusion_score\
  \ = {founder_share, n_doa_owners}  # primary predictors\n\n# === STAGE 5: Survival outcome (Avelino et al.'s Active/Inactive/recovery\
  \ model) ===\nfor repo in repos_with_diffusion_score:\n    post = events filtered to author_date in [tfdd_month, tfdd_month\
  \ + 18mo]\n    # Active/Inactive state machine: repo is Inactive from tfdd_month until a NEW developer\n    # (not in the\
  \ departed TF set) attains TF-developer status (joins the current\n    # TF_developer_set at some post-TFDD monthly snapshot)\
  \ -- that event flips it back Active.\n    recovered = any(post-TFDD snapshot where a new author is in TF_developer_set)\n\
  \    # graded outcome (thriving/maintained/dormant/dead) -- define via post-TFDD commit\n    # velocity relative to pre-TFDD\
  \ baseline, using quartile cut points the executor derives\n    # empirically from the corpus's own post-TFDD commit-count\
  \ distribution (report the exact\n    # cutpoints used, since Avelino et al.'s paper does not give exact numeric thresholds\
  \ for\n    # the 4 labels -- executor should fetch_grep the ESEM 2019 paper for their operational\n    # definition of the\
  \ 4 states before inventing one from scratch)\n    binary_survival = recovered  # matches Avelino et al.'s binary survive/not-survive\
  \ stat\n\n# === STAGE 6: Confound controls ===\nfor repo: controls = {log_stars, log_forks, contributor_count, language,\
  \ license,\n                       developers_at_tfdd, commits_at_tfdd, files_at_tfdd}  # the snapshot\n               \
  \        # covariates Avelino et al. found null (d=0.13-0.26) -- MUST be\n                       # recomputed here identically\
  \ to compare standardized effect sizes\n\n# === STAGE 7: Analysis (a) regression ===\nX = [founder_share, n_doa_owners,\
  \ log_stars, log_forks, contributor_count,\n     developers_at_tfdd, commits_at_tfdd, files_at_tfdd] + language/license\
  \ one-hot\nlogit_model = sm.Logit(binary_survival, standardize(X)).fit()          # statsmodels\nordinal_model = statsmodels.miscmodels.ordinal_model.OrderedModel(\n\
  \                    graded_outcome, standardize(X), distr='logit').fit()\nBH_correct(p_values_of_all_coefficients)  # statsmodels.stats.multitest.multipletests,\
  \ method='fdr_bh'\nreport: standardized_coef, BH_p, compare |coef(founder_share)|, |coef(n_doa_owners)| vs\n        |coef(log_stars)|,\
  \ |coef(developers_at_tfdd)| etc.\n\n# === STAGE 8: Analysis (b) matched-pairs / stratified comparison ===\nbuckets = stratify_by(log_stars_decile,\
  \ log_forks_decile, contributor_count_bucket)\nhigh_diffusion = repos where founder_share < 0.50 AND n_doa_owners >= 2\n\
  low_diffusion  = repos where founder_share >= 0.80\nfor each bucket: pair high_diffusion repos to low_diffusion repos via\
  \ nearest-neighbor on\n                 (log_stars, log_forks, contributor_count) using sklearn NearestNeighbors\n     \
  \            or scipy cKDTree, caliper = 0.2 * pooled std of matching covariates\nsurvival_rate_ratio = mean(binary_survival\
  \ | high_diffusion, matched) / \n                       mean(binary_survival | low_diffusion, matched)\nbootstrap_CI = bootstrap(survival_rate_ratio,\
  \ n_resamples=10000, method='percentile')\nreport ratio, 95% CI, compare against Avelino et al.'s unconditioned 41% baseline\n\
  \n# === STAGE 9: Falsification / placebo check ===\nnull_ratios = []\nfor trial in range(1000):\n    for repo: relocate\
  \ window to a uniformly random start month in\n              [first_commit_date, tfdd_month - window_length - 1mo]  # same\
  \ length, must stay\n              strictly before the TRUE window's start to avoid leakage; recompute\n              founder_share_null,\
  \ n_doa_owners_null using the SAME memoized per-snapshot DOA\n              tables from Stage 2 (cheap re-slice, no recomputation)\n\
  \    rerun analysis (a) and (b) with the null-window predictors\n    null_ratios.append(placebo_survival_rate_ratio)\nreport:\
  \ true_effect_percentile_in_null_distribution, empirical p-value =\n        (1 + sum(null_ratios >= true_ratio)) / (1 +\
  \ len(null_ratios))\n\n# === STAGE 10: Assemble method_out.json ===\noutput = {\n  'corpus_stats': {n_repos_input, n_repos_after_filters,\
  \ n_founder_only_tfdds, exclusion_table},\n  'baseline_replication': {tfdd_rate, survival_rate, snapshot_effect_sizes},\
  \  # sanity check\n                                                                              # against Avelino\n   \
  \                                                                           # et al.'s reported\n                      \
  \                                                        # 16% TFDD rate /\n                                           \
  \                                   # 41% survival / d\n  'regression_results': {...},\n  'matched_pairs_results': {...},\n\
  \  'placebo_results': {...},\n  'success_criteria_verdict': {criterion_1_pass_bool, criterion_2_pass_bool,\n           \
  \                     criterion_3_pass_bool, notes}\n}"
fallback_plan: >-
  Layer the fallbacks by what breaks first, from cheapest degradation to most fundamental: (1) FULL git clones too slow/large
  -- if the DATASET artifact only supplies shallow clones or pre-extracted commit logs without full blob history, that's fine:
  DOA only needs (author, file, commit_date) triples, not blob contents, so nothing in the pipeline actually requires full
  clones; explicitly do NOT re-clone anything, use whatever the dataset provides. (2) Corpus too small after filtering (e.g.,
  <40-50 founder-only-TFDD repos survive the >=3-year-history + founder-only-TF=1 filters) -- relax the TF=1-at-departure
  requirement to TF<=2 with founder in the departing set and note the deviation explicitly in the output, since Avelino et
  al. themselves report 66% of TFDDs are TF=1 so a large corpus should still clear the stricter filter; if it still doesn't,
  reduce required post-TFDD survival window from 18 to 12 months (report both) rather than dropping repos, and flag this as
  a limitation rather than silently changing the headline metric. (3) DOA/TF computation too slow at monthly granularity across
  the full corpus -- switch from monthly to quarterly snapshots for Stage 2's running DOA state (this is the compute-heavy
  step: O(commits x files) per snapshot); the pre-departure window (6-12mo) and TFDD detection can tolerate quarterly resolution
  with a documented +/-1.5 month fuzz on the TFDD date, which does not materially change founder_share or n_doa_owners since
  both are already window-aggregate statistics. (4) statsmodels' OrderedModel fails to converge on the graded 4-level outcome
  (common with small/imbalanced strata) -- fall back to the binary logistic regression only for the primary claim (success
  criterion 2 only requires the diffusion predictors' significance, which the binary model alone can establish) and report
  the ordinal model as exploratory/best-effort with a convergence-failure caveat rather than blocking the whole artifact on
  it. (5) Matched-pairs bucket has too few pairs per stratum for a stable bootstrap CI (e.g., <10 pairs in the high-diffusion
  vs low-diffusion contrast within a size bucket) -- pool across size buckets and instead include the matching covariates
  (log_stars, log_forks, contributor_count) as regression adjustors in a single pooled matched-set analysis (essentially collapsing
  (a) and (b) into one covariate-adjusted comparison), clearly labeled as a fallback deviation from the pre-registered stratified
  design in success_criteria_verdict.notes. (6) If the DATASET artifact this experiment depends on does not actually provide
  enough repos with the founder-identifiable-first-commit property (e.g., many repos were imported from an external VCS with
  no clean initial commit) -- restrict founder identification to repos where the first commit's author authored >= 3 of the
  first 5 commits (a robustness check against a single miscategorized scaffolding commit), and report the fraction of repos
  excluded for unidentifiable founders as part of the exclusion table so the reader can judge the founder-only subset's representativeness.
  Under no circumstances should the executor fabricate or downsample results to hit the success-criteria thresholds -- report
  a null/negative result plainly if the corpus and analysis genuinely produce one; a rigorous null result on this question
  is itself a valid, reportable outcome given Avelino et al.'s own snapshot-null precedent.
testing_plan: >-
  1. UNIT-TEST DOA/TF logic on a synthetic 3-file, 4-author toy repo with hand-computed expected DOA values and a known TF
  set BEFORE running on any real data -- construct commit sequences where the expected primary owner, TF size, and TFDD timing
  are unambiguous by hand-derivation, and assert the code reproduces them exactly. This catches formula/off-by-one errors
  cheaply since the full DOA formula (particularly the DL term) must be verified against the ICPC 2016 paper text rather than
  guessed. 2. SMOKE TEST on 3-5 real, well-known single-founder repos with a documented founder departure the executor can
  sanity-check by eye (e.g., search for OSS projects with public 'founder handed off maintenance' blog posts/README history)
  -- confirm the pipeline's detected TFDD month is within a few months of the publicly known handoff date, and that the pre-TFDD
  founder_share trend direction (declining vs not) matches what a manual `git shortlog` inspection of that repo's commit history
  shows for the year before handoff. 3. BASELINE-REPLICATION CHECK on the full filtered corpus before running the NEW diffusion
  analysis: verify the pipeline's own aggregate stats are in the right ballpark against Avelino et al.'s published numbers
  -- TFDD rate should land near their 16% (not required to match exactly since the corpus differs, but order-of-magnitude
  and general directionality, e.g. TFDD rate should not come out as 90% or 1%, would indicate a pipeline bug), TF=1-at-departure
  share near their 66%, and overall post-TFDD binary survival rate near their 41% -- treat large deviations (e.g., >2x off)
  as a signal to debug the TFDD-detection or survival-scoring logic before trusting the new diffusion results. Also directly
  recompute the size/popularity snapshot effect sizes (developers/commits/files at TFDD, survivors vs non-survivors) and confirm
  they replicate as negligible-to-small (d roughly in the 0.1-0.3 range, same sign direction) as reported in the ESEM 2019
  paper -- this is the load-bearing sanity check, since the entire hypothesis is that the NEW pre-departure signal succeeds
  precisely where this snapshot signal is known to fail; if the replication check itself produces a strong snapshot effect
  where Avelino et al. found none, that indicates a corpus-construction or measurement discrepancy needing resolution before
  proceeding to the novel analysis. 4. SCALE GRADUALLY: run the full pipeline (Stages 1-6) on a 20-30 repo mini-sample first,
  inspect the diffusion-score distribution and survival labels by hand for a handful of cases, confirm nothing is degenerate
  (e.g., founder_share always exactly 0 or 1, n_doa_owners always 0) before scaling to the full corpus and before launching
  the 500-1000-iteration placebo loop, which is the single most expensive step and should only run once Stages 1-8 are validated
  end-to-end on the mini-sample. 5. Track and report cumulative OpenRouter spend if any LLM calls are used for repo/language
  filtering heuristics (should be $0 or near-$0 for this artifact -- the entire pipeline is deterministic git-log analysis
  and statistics, not LLM-driven; if the executor finds itself needing an LLM call anywhere in this pipeline, that is a signal
  the approach has drifted from what was planned and should be reconsidered).
</artifact_plan>



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

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
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

### [6] SKILL-INPUT — aii-file-size-limit · 2026-08-21 15:59:41 UTC

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

### [7] SYSTEM-USER prompt · 2026-08-21 15:59:55 UTC

```
<validation-feedback>
Attempt 1 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [8] SYSTEM-USER prompt · 2026-08-21 16:21:16 UTC

```
<validation-feedback>
Attempt 2 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `summary`: "Implements a full recomputation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship / Truck-Factor / Truck-Factor-Developer-Departure (TFDD) pipeline on real GitHub repositories, plus a new pre-departure authority-diffusion measurement and three analyses testing whether it predicts post-departure survival better than Avelino et al.'s null snapshot covariates. Because the upstream DATASET artifact this experiment was planned to depend on (gen_art_dataset_1) had an empty data_out/ at execution time, method.py is self-contained: it mines a curated corpus of 43 mature, well-known GitHub repositories (spanning JavaScript, Python, Ruby, PHP, Java, C++, Go) directly via metadata-only blobless git clones plus the unauthenticated GitHub REST API, documented explicitly in the output and in REPO_LIST. For each repo it builds a chronological (author, file, timestamp) commit event log with GitHub-noreply-email/name alias resolution, then computes the Fritz/Avelino Degree-of-Authorship formula (DOA = 3.293 + 1.098*FA - 0.164*ln(1+DL) + 0.321*ln(1+AC)) and greedy Truck-Factor at quarterly snapshots (monthly was infeasible at this compute budget; the fallback_plan explicitly sanctions quarterly resolution with a documented ~1.5-month TFDD-date fuzz). It identifies each repo's founder (robust to a single scaffolding first commit), scans forward for the first TFDD where the truck-factor set is the founder alone and stays silent 12+ months, and requires >=12mo of pre-history and >=18mo of post-history to avoid censoring. The new measurement (Stage 4) computes founder commit-share and the count of distinct non-founder DOA file-owners in the 6-12-month window before that TFDD. The outcome (Stage 5) is an Active/Inactive/recovery model: binary survival = whether any post-TFDD snapshot shows a new non-founder developer attaining truck-factor status, plus a graded post/pre commit-velocity ratio. Confound controls (Stage 6) recompute Avelino et al.'s own null snapshot covariates (log stars, log forks, contributor count, developers/commits/files at TFDD). Three analyses are run: (a) standardized logistic + ordinal regression with Benjamini-Hochberg FDR correction (statsmodels), comparing |coef(diffusion)| vs |coef(snapshot)|; (b) matched-pairs nearest-neighbor (sklearn) high- vs low-diffusion comparison with a 10,000-resample bootstrap CI on the survival-rate ratio; (c) a within-repo random-window placebo/falsification test computing an empirical p-value against 200 null draws (reduced from the plan's 1000 for CPU budget, documented). Of the 43 curated repos, 35 passed the CONSORT-style prefilters (>=3yr history, >=40% source-file fraction, no squashed-history artifact) and 24 yielded a usable founder-only TFDD event with sufficient pre/post history -- these 24 form the analysis corpus. The result is a genuine, non-fabricated NULL finding: none of the three pre-registered success criteria were met (diffusion predictors' BH-adjusted p-values ~0.77-0.81, not below 0.10; |coef(diffusion)|=0.75 did not exceed |coef(snapshot)|=1.00; placebo empirical p-value did not clear 0.10), which the fallback_plan explicitly treats as a valid, reportable outcome given Avelino et al.'s own snapshot-null precedent -- most plausibly attributable to the reduced sample size (n=24 vs. Avelino et al.'s much larger corpus) rather than to a pipeline defect, since the pipeline's own mechanics (DOA/TF/TFDD detection, alias resolution, regression, matched-pairs, placebo) all executed and converged without error. Two documented implementation deviations: (1) DL(a,f) uses the standard Fritz/Avelino textual definition (commits to f by OTHER authors after a's own last commit to f) without independently re-verifying against the ICPC 2016 paper's exact formula text, since fetching that paper was out of scope for this execution pass; (2) the source-file-fraction prefilter threshold was relaxed from the plan's 0.60 to 0.40 after a pilot run showed 0.60 rejected the large majority of real repos (test fixtures, source maps, docs). method.py writes method_out.json following the exp_gen_sol_out schema: one dataset ('github_repos_curated_corpus') with one example per repo (input = repo + research question, output = full per-repo JSON result including founder, TFDD date, founder_share, n_doa_owners, binary_survival, graded outcome, and all snapshot covariates), predict_our_method / predict_baseline_snapshot fields on the 24 repos with a usable TFDD, and a top-level metadata object carrying corpus_stats (with a full exclusion table), baseline_replication (Avelino et al.'s own TFDD-rate/survival-rate/snapshot-effect-size sanity checks), regression_results, matched_pairs_results, placebo_results, and success_criteria_verdict with explicit pass/fail booleans and notes. Downstream paper-writing steps should present this as a rigorous null result: the pipeline itself replicates Avelino et al.'s methodology faithfully on a real (if necessarily smaller) GitHub corpus, and the pre-departure authority-diffusion signal did not outperform the snapshot covariates at this sample size -- a scope-boundary finding, not evidence the underlying hypothesis is false." is too long (at most 5000 characters, got 5176)
Every required field must be present and every field type must match the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [9] SYSTEM-USER prompt · 2026-08-21 16:21:52 UTC

```
<verification_failed>
Your experiment output failed verification (attempt 1/10).
</verification_failed>

<file_errors>
MISSING OR UNREADABLE FILES:
  - Missing file: full_method_out.json
  - Missing file: mini_method_out.json
  - Missing file: preview_method_out.json

Fix: Create the missing files directly in your workspace (see <workspace> above for the exact path).
     Required files: method.py, method_out.json, full_method_out.json, mini_method_out.json, preview_method_out.json
     Use 'ls' to check what files exist.
</file_errors>

<task>
FIX THESE ISSUES:
1. Create all missing files by running method.py

After making changes, verify:
- 'ls -la' shows all required files
- 'uv run method.py' completes successfully
- JSON files are valid (use aii-json skill validation)
- full_method_out.json has at least 50 examples
</task>
```

### [10] SYSTEM-USER prompt · 2026-08-21 16:33:31 UTC

```
<verification_failed>
Your experiment output failed verification (attempt 2/10).
</verification_failed>

<file_errors>
MISSING OR UNREADABLE FILES:
  - Missing file: full_method_out.json
  - Missing file: mini_method_out.json
  - Missing file: preview_method_out.json

Fix: Create the missing files directly in your workspace (see <workspace> above for the exact path).
     Required files: method.py, method_out.json, full_method_out.json, mini_method_out.json, preview_method_out.json
     Use 'ls' to check what files exist.
</file_errors>

<task>
FIX THESE ISSUES:
1. Create all missing files by running method.py

After making changes, verify:
- 'ls -la' shows all required files
- 'uv run method.py' completes successfully
- JSON files are valid (use aii-json skill validation)
- full_method_out.json has at least 50 examples
</task>
```

### [11] SYSTEM-USER prompt · 2026-08-21 16:37:05 UTC

```
<verification_failed>
Your experiment output failed verification (attempt 3/10).
</verification_failed>

<schema_errors>
JSON SCHEMA / CODE VALIDATION ERRORS:
  - full_method_out.json: No predict_* fields found in any of the sampled examples (at least one required)
  - mini_method_out.json: No predict_* fields found in any of the sampled examples (at least one required)
  - preview_method_out.json: No predict_* fields found in any of the sampled examples (at least one required)

Fix: Your JSON files must follow the datasets-grouped exp_gen_sol_out.json schema:
     {
       "datasets": [
         {
           "dataset": "dataset_name",
           "examples": [
             {
               "input": "string (required)",
               "output": "string (required)",
               "metadata_fold": 2,
               "predict_<method_name>": "string - prediction per method"
             }
           ]
         }
       ]
     }

     NO 'split', 'dataset', or 'context' per-example. Dataset name at group level.
     Metadata via flat metadata_<name> fields.
     Read exp_gen_sol_out.json schema in aii-json skill.
     Then update method.py and regenerate the output files.

     If Python syntax errors: fix the syntax in method.py
</schema_errors>

<task>
FIX THESE ISSUES:
2. Fix schema/syntax errors in method.py
3. Re-run method.py to regenerate output files
4. Validate with aii-json skill: validate method_out.json against exp_gen_sol_out schema

After making changes, verify:
- 'ls -la' shows all required files
- 'uv run method.py' completes successfully
- JSON files are valid (use aii-json skill validation)
- full_method_out.json has at least 50 examples
</task>
```
