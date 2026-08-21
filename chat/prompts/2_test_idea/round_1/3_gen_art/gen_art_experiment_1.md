# gen_art_experiment_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `iter1_0b7b616dce39` — Scaling the Corpus, Auditing the Power, and Reconciling the Sign: What Happens When a Founder-Diffusion Survival Test Is Finally Interrogated Rather Than Just Run
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 16:28:50 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_1_idx2
type: experiment
title: Does authority diffusion before founder exit predict OSS survival?
summary: >-
  Re-implements Avelino et al.'s (ESEM 2019) DOA/Truck-Factor/TFDD/Active-Inactive pipeline from GitHub commit histories,
  detects founder-only TFDD events, adds a NEW pre-departure metric (founder commit-share and count of independent non-founder
  DOA file-owners in the 6-12 months before TFDD) that their published pipeline does not compute, labels 18-month post-TFDD
  survival, and tests whether this pre-departure authority-diffusion trajectory predicts survival better than size/popularity
  covariates via matched pairs and a BH-corrected regression.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  # === STAGE 0: repo sampling (self-contained, no DATASET dependency available) ===
  # Use GitHub REST API (via `requests`, authenticated with GITHUB_TOKEN env var if present,
  # else unauthenticated at 60 req/hr -- budget calls accordingly) OR the `pydriller`/`PyGithub`
  # PyPI packages for repo cloning + commit walking. Do NOT scrape git objects manually.
  import requests, subprocess, time
  from pydriller import Repository  # pip: pydriller -- walks full commit history incl. file diffs

  LANGUAGES = ['Python','JavaScript','Java','Go','Ruby','C++']  # subset of Avelino et al.'s 6
  SAMPLE_PER_LANG = 40  # 6*40=240 candidate repos -- gradual scaling, see testing_plan

  candidates = []
  for lang in LANGUAGES:
      # GitHub search API: sort by stars, paginate to get popularity STRATA not just top-N
      # (avoids confounding survival analysis with "only mega-popular repos" bias)
      for page_bucket in ['stars:>5000','stars:500..5000','stars:50..500']:
          resp = github_search_repos(f'language:{lang} {page_bucket}', per_page=SAMPLE_PER_LANG//3)
          candidates += resp
      time.sleep(2)  # respect rate limit

  # === STAGE 1: filter mining artifacts (Avelino et al.'s exclusion criteria) ===
  filtered = []
  for repo in candidates:
      meta = get_repo_metadata(repo)
      if meta['age_days'] < 2*365: continue           # need >=2yr history (Avelino) -- we need 3yr (TFDD + 18mo)
      if meta['age_days'] < 3*365: continue            # our stricter requirement per assumptions
      if is_fork(meta) or is_archive_list(repo) or not has_code_files(repo): continue  # 'perils of mining GitHub'
      filtered.append(repo)

  # === STAGE 2: clone shallow-but-full-history, walk commits with PyDriller ===
  for repo in filtered:
      subprocess.run(['git','clone','--bare', repo['clone_url'], f'/tmp/repos/{repo["id"]}.git'], timeout=600)
      commits = []
      for c in Repository(f'/tmp/repos/{repo["id"]}.git').traverse_commits():
          commits.append({
              'hash': c.hash, 'author_email': resolve_alias(c.author.email),  # GitHub API email->account map
              'date': c.committer_date, 'files': [(m.new_path, m.added_lines, m.deleted_lines) for m in c.modified_files]
          })
      save_commits(repo['id'], commits)

  # === STAGE 3: DOA computation (Fritz et al. formula, as specified by Avelino ICPC 2016 / ESEM 2019) ===
  # DOA(dev, file, t) = 3.293 + 1.098*FA - 0.164*(AC^(1/2)) + 0.230*ln(1+DL)
  #   FA = 1 if dev is first author of file else 0
  #   AC = number of dev's changes to file up to time t
  #   DL = deletions dev made to file (churn) -- exact formula per paper; verify against ICPC2016 arXiv text
  # Compute DOA for EVERY (dev,file) pair using ONLY commits up to each yearly (or 6-month rolling) cutoff t.
  # A dev is 'primary owner'/core of a file at t if their DOA(dev,file,t) is the MAX among all devs who touched
  # that file AND DOA > threshold used by Avelino et al. (paper reports the exact cutoff, e.g. DOA>3.293 baseline).

  def compute_doa_snapshot(commits, cutoff_date):
      file_dev_stats = defaultdict(lambda: defaultdict(lambda: {'first_author': None, 'ac': 0, 'dl': 0}))
      for c in commits:
          if c['date'] > cutoff_date: continue
          for (path, added, deleted) in c['files']:
              s = file_dev_stats[path][c['author_email']]
              if s['first_author'] is None: s['first_author'] = c['author_email']
              s['ac'] += 1; s['dl'] += deleted
      doa = {}
      for path, devs in file_dev_stats.items():
          first_author = next(iter(devs))  # actual first author = earliest commit's author for that file
          for dev, s in devs.items():
              fa = 1 if dev == first_author else 0
              doa[(dev,path)] = 3.293 + 1.098*fa - 0.164*(s['ac']**0.5) + 0.230*log(1+s['dl'])
      return doa

  # Truck Factor set at t = greedy min set of devs whose removal drops 'coverage'
  # (files with an unambiguous owner) below 50% -- reuse Avelino et al.'s exact TF greedy algorithm.
  def truck_factor_set(doa_snapshot):
      file_owner = {}
      for (dev,path), score in doa_snapshot.items():
          if path not in file_owner or score > file_owner[path][1]:
              file_owner[path] = (dev, score)
      owned_files_per_dev = Counter(dev for dev,_ in file_owner.values())
      total_files = len(file_owner)
      tf_set, covered = [], 0
      for dev, n in owned_files_per_dev.most_common():
          tf_set.append(dev); covered += n
          if covered >= 0.5*total_files: break
      return tf_set

  # === STAGE 4: TFDD detection -- scan yearly snapshots chronologically ===
  for repo in filtered:
      commits = load_commits(repo['id'])
      yearly_dates = pd.date_range(repo['created_at'], repo['last_commit'], freq='365D')
      tf_history = [(d, truck_factor_set(compute_doa_snapshot(commits, d))) for d in yearly_dates]
      last_active = {dev: max(c['date'] for c in commits if c['author_email']==dev) for dev in all_devs}
      for i, (d, tf_set) in enumerate(tf_history):
          # TFDD: every dev in tf_set has been silent >= 1yr (validated threshold) as of d
          if tf_set and all((d - last_active[dev]).days >= 365 for dev in tf_set):
              if len(tf_set) == 1:  # FOUNDER-ONLY TFDD -- the subset this study targets
                  founder = tf_set[0]
                  tfdd_date = min(last_active[founder] + timedelta(365), d)
                  record_tfdd_event(repo['id'], founder, tfdd_date)
                  break  # first founder-only TFDD only, per investigation_approach step 2

  # === STAGE 5: pre-departure diffusion metrics (THE NEW MEASUREMENT) ===
  for event in tfdd_events:
      window_start = event.tfdd_date - timedelta(days=365)   # 12mo before
      window_end   = event.tfdd_date - timedelta(days=180)    # 6mo before
      window_commits = [c for c in commits if window_start <= c['date'] < window_end]
      founder_commits = sum(1 for c in window_commits if c['author_email']==event.founder)
      founder_share = founder_commits / max(1,len(window_commits))
      doa_at_window_end = compute_doa_snapshot(commits, window_end)
      file_owner = argmax_owner_per_file(doa_at_window_end)
      non_founder_owners = {dev for dev,path in file_owner.items() if dev != event.founder}
      event.founder_share = founder_share
      event.n_diffused_owners = len(non_founder_owners)
      # snapshot covariates AT TFDD for comparison to Avelino et al.'s d=0.13-0.26 result
      event.devs_at_tfdd, event.commits_at_tfdd, event.files_at_tfdd = snapshot_covariates(commits, event.tfdd_date)

  # === STAGE 6: survival label (Avelino et al. Active/Inactive model, 18mo window) ===
  for event in tfdd_events:
      post = [c for c in commits if event.tfdd_date <= c['date'] < event.tfdd_date+timedelta(days=548)]
      new_tf_devs = {c['author_email'] for c in post} - {event.founder}
      doa_post = compute_doa_snapshot(commits, event.tfdd_date+timedelta(days=548))
      recovered_tf = truck_factor_set(doa_post)
      event.survived = bool(recovered_tf) and any(d != event.founder for d in recovered_tf)
      event.grade = classify_thriving_maintained_dormant_dead(post, recovered_tf)

  # === STAGE 7: falsification / placebo check ===
  for event in tfdd_events:
      random_window = sample_random_window(event.repo, exclude=near_tfdd)
      event.placebo_founder_share, event.placebo_n_diffused = compute_window_metrics(random_window)

  # === STAGE 8: matched pairs + regression ===
  buckets = bucket_by(stars=log_deciles, forks=log_deciles, n_contributors=log_deciles, language=exact)
  matched_pairs = []
  for bucket, events in groupby(tfdd_events, buckets):
      lo = [e for e in events if e.founder_share < 0.50 and e.n_diffused_owners >= 2]
      hi = [e for e in events if e.founder_share >= 0.80]
      matched_pairs += greedy_nearest_neighbor_match(lo, hi, on=['stars','forks','n_contributors'])

  risk_ratio, ci95 = bootstrap_survival_rate_ratio(matched_pairs, n_boot=5000)

  import statsmodels.api as sm
  X = df[['founder_share','n_diffused_owners','log_stars','log_forks','n_contributors','language_dummies','license_dummies']]
  model = sm.Logit(df['survived'], sm.add_constant(X)).fit()
  pvals_bh = benjamini_hochberg(model.pvalues)
  std_effect_sizes = standardized_coefs(model, X)  # compare vs Avelino et al. d=0.13(files)/0.25-0.26(devs,commits)

  # placebo comparison: refit model with placebo_founder_share / placebo_n_diffused instead
  placebo_model = sm.Logit(df['survived'], sm.add_constant(df[['placebo_founder_share','placebo_n_diffused', ...]])).fit()

  # === STAGE 9: write method_out.json ===
  results = {
    'n_repos_sampled': ..., 'n_founder_tfdd_events': ..., 'unconditioned_survival_rate': ...,  # vs Avelino 41%
    'matched_pair_risk_ratio': risk_ratio, 'ci95': ci95,
    'regression_coefs': model.params.to_dict(), 'pvals_bh': pvals_bh, 'std_effect_sizes': std_effect_sizes,
    'placebo_coefs': placebo_model.params.to_dict(),
    'snapshot_covariate_effect_sizes_d': cohens_d(devs_at_tfdd, commits_at_tfdd, files_at_tfdd, by=survived),
    'per_event_records': [...]  # full row-level table for downstream paper artifact
  }
  json.dump(results, open('method_out.json','w'), indent=2)
fallback_plan: |-
  Primary risk is DATA VOLUME/TIME, not algorithmic novelty -- the DOA/TF pipeline is fully specified in Avelino et al. and Fritz et al., so implement it exactly rather than approximate it. Layered fallbacks, in order:
  1. If GitHub API rate limits (60/hr unauthenticated, 5000/hr with a token) block reaching ~240 candidate repos within the 6h budget, drop SAMPLE_PER_LANG to 15-20 and/or restrict to 3 languages (Python, JavaScript, Go) -- still enough for matched pairs if founder-only TFDDs are ~16%*66%=~10% of repos (Avelino et al.'s own rates), i.e. expect ~10-25 usable events from 150-240 repos; if fewer than ~15 founder-TFDD events are found, RELAX the founder-only TF=1 requirement's downstream matched-pair bucket granularity (fewer bucket dimensions: drop 'license' from matching, keep only stars+language) rather than abandoning the matched-pairs design, and report the regression as the primary result with matched-pairs as a secondary/exploratory check, clearly labeled with the reduced n.
  2. If `git clone --bare` of large repos (e.g. large C++ projects) times out or exceeds disk, use `git clone --bare --filter=blob:none` (partial clone, still gives full commit/path history which is all DOA needs) or cap repo size by GitHub API `size` field before selection (exclude repos >500MB).
  3. If PyDriller is too slow walking full history for large repos (some real repos have 50k+ commits), fall back to raw `git log --numstat --format='%H|%ae|%cI'` parsed manually via subprocess -- much faster, same information needed (author, date, per-file added/deleted lines).
  4. If GitHub's search API cannot cleanly stratify by popularity bucket (search API caps at 1000 results per query), issue multiple queries partitioning by star-count ranges as already planned in Stage 0 -- this is the mitigation, not a fallback trigger.
  5. If DOA-based TFDD detection finds zero or very few founder-only (TF=1) TFDD events after scanning all sampled repos (possible if the sample skews toward large multi-founder projects), explicitly RELAX the founder-only definition to 'founder retained TF-set membership until departure, TF-set size <=2 at detachment' and report both the strict (TF=1) and relaxed (TF<=2) results separately -- do not silently substitute one for the other.
  6. If the 18-month post-TFDD survival window right-censors too many events (repo's total history <3yr from birth to TFDD+18mo), drop those events from the labeled set but KEEP them in a separate 'right-censored, excluded' count reported in method_out.json for transparency -- do not impute or guess their outcome.
  7. If statsmodels' logistic regression fails to converge (e.g., quasi-separation with a small n and multiple dummy variables), reduce covariates to a parsimonious set (founder_share, n_diffused_owners, log_stars, log_n_contributors only, dropping language/license dummies or collapsing them to 2-3 groups) and report this explicitly as a deviation from the full model in success_criteria point 2.
  8. If time runs out before the full logistic + BH correction can be fit, still produce and save: (a) the founder-only TFDD event table with all raw metrics, (b) the unconditioned survival rate for direct Avelino-et-al comparability, and (c) a simple two-group t-test/Mann-Whitney comparison of founder_share and n_diffused_owners between survivors and non-survivors -- a minimally complete result beats an unfinished full regression.
testing_plan: |-
  Gradual scaling per aii-long-running-tasks pattern -- validate correctness on a tiny, fully-inspectable slice before scaling to the full sample:
  1. MINI TEST (5 repos, hand-picked, ~15 min of runtime budget): pick 5 well-known repos with KNOWN founder-departure histories the executor can sanity-check by eye (e.g. a small abandoned utility library where a single early README/commit-log inspection confirms one dominant early committer who later went silent). Clone, run DOA computation for just 2-3 yearly snapshots, and MANUALLY verify: (a) the computed first-author-per-file matches `git log --diff-filter=A --follow -- <file>` for a handful of spot-checked files, (b) the DOA formula output is a plausible positive number in the same range as Fritz et al.'s reported examples, (c) the greedy TF-set algorithm on this tiny repo returns a sensible minimal set (e.g. TF=1 for a single-maintainer repo). This catches formula transcription errors and alias-resolution bugs before they propagate.
  2. PIPELINE-SHAPE TEST (10-15 repos): run the FULL pipeline (Stages 0-9) end-to-end on a small sample to confirm every stage produces non-degenerate output -- specifically check: TFDD detection finds at least 1-2 founder-only events (not zero, which would indicate a bug in the 1-year-silence or TF=1 logic), pre-departure metrics are in [0,1] for founder_share and non-negative integers for n_diffused_owners, and survival labels split into both True and False (not all-one-class, which would break the regression). If TFDD events = 0 at this scale, debug the silence-threshold and TF-set logic before scaling up -- do not proceed to full sampling with an undetected bug.
  3. CROSS-CHECK AGAINST AVELINO ET AL.'S PUBLISHED NUMBERS: on whatever founder-only TFDD events are found in the eventual full run, report the UNCONDITIONED survival rate and sanity-check it is in a plausible neighborhood of their reported 41% (not required to match exactly -- different sample -- but a wildly different rate, e.g. 95% or 2%, signals a bug in survival labeling, most likely the Active/Inactive recovery criterion being mis-implemented as 'any commit at all' rather than 'a new TF developer attracted').
  4. SCALE UP in 2-3 steps (e.g. 15 -> 80 -> 240 repos) per the gradual-scaling pattern, checking wall-clock time and GitHub API quota consumption at each step before committing to the next, and stopping early (documenting n achieved) if the 6h budget is at risk -- prioritize finishing Stages 1-9 on a smaller-than-planned sample over running out of time mid-clone.
  5. FINAL VALIDATION: before writing method_out.json, confirm (a) no NaN/inf in the regression design matrix, (b) the BH correction is applied to the RIGHT set of p-values (the diffusion predictors, not all covariates indiscriminately, per success_criteria point 2), (c) the placebo/shuffle check (Stage 7) was actually run on a comparable number of events to the main analysis, not skipped.
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

### [2] HUMAN-USER prompt · 2026-08-21 16:28:50 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-json · 2026-08-21 16:31:20 UTC

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

### [4] SKILL-INPUT — aii-python · 2026-08-21 16:31:20 UTC

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

### [5] SYSTEM-USER prompt · 2026-08-21 16:41:09 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_1_idx2
type: experiment
title: Does authority diffusion before founder exit predict OSS survival?
summary: >-
  Re-implements Avelino et al.'s (ESEM 2019) DOA/Truck-Factor/TFDD/Active-Inactive pipeline from GitHub commit histories,
  detects founder-only TFDD events, adds a NEW pre-departure metric (founder commit-share and count of independent non-founder
  DOA file-owners in the 6-12 months before TFDD) that their published pipeline does not compute, labels 18-month post-TFDD
  survival, and tests whether this pre-departure authority-diffusion trajectory predicts survival better than size/popularity
  covariates via matched pairs and a BH-corrected regression.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  # === STAGE 0: repo sampling (self-contained, no DATASET dependency available) ===
  # Use GitHub REST API (via `requests`, authenticated with GITHUB_TOKEN env var if present,
  # else unauthenticated at 60 req/hr -- budget calls accordingly) OR the `pydriller`/`PyGithub`
  # PyPI packages for repo cloning + commit walking. Do NOT scrape git objects manually.
  import requests, subprocess, time
  from pydriller import Repository  # pip: pydriller -- walks full commit history incl. file diffs

  LANGUAGES = ['Python','JavaScript','Java','Go','Ruby','C++']  # subset of Avelino et al.'s 6
  SAMPLE_PER_LANG = 40  # 6*40=240 candidate repos -- gradual scaling, see testing_plan

  candidates = []
  for lang in LANGUAGES:
      # GitHub search API: sort by stars, paginate to get popularity STRATA not just top-N
      # (avoids confounding survival analysis with "only mega-popular repos" bias)
      for page_bucket in ['stars:>5000','stars:500..5000','stars:50..500']:
          resp = github_search_repos(f'language:{lang} {page_bucket}', per_page=SAMPLE_PER_LANG//3)
          candidates += resp
      time.sleep(2)  # respect rate limit

  # === STAGE 1: filter mining artifacts (Avelino et al.'s exclusion criteria) ===
  filtered = []
  for repo in candidates:
      meta = get_repo_metadata(repo)
      if meta['age_days'] < 2*365: continue           # need >=2yr history (Avelino) -- we need 3yr (TFDD + 18mo)
      if meta['age_days'] < 3*365: continue            # our stricter requirement per assumptions
      if is_fork(meta) or is_archive_list(repo) or not has_code_files(repo): continue  # 'perils of mining GitHub'
      filtered.append(repo)

  # === STAGE 2: clone shallow-but-full-history, walk commits with PyDriller ===
  for repo in filtered:
      subprocess.run(['git','clone','--bare', repo['clone_url'], f'/tmp/repos/{repo["id"]}.git'], timeout=600)
      commits = []
      for c in Repository(f'/tmp/repos/{repo["id"]}.git').traverse_commits():
          commits.append({
              'hash': c.hash, 'author_email': resolve_alias(c.author.email),  # GitHub API email->account map
              'date': c.committer_date, 'files': [(m.new_path, m.added_lines, m.deleted_lines) for m in c.modified_files]
          })
      save_commits(repo['id'], commits)

  # === STAGE 3: DOA computation (Fritz et al. formula, as specified by Avelino ICPC 2016 / ESEM 2019) ===
  # DOA(dev, file, t) = 3.293 + 1.098*FA - 0.164*(AC^(1/2)) + 0.230*ln(1+DL)
  #   FA = 1 if dev is first author of file else 0
  #   AC = number of dev's changes to file up to time t
  #   DL = deletions dev made to file (churn) -- exact formula per paper; verify against ICPC2016 arXiv text
  # Compute DOA for EVERY (dev,file) pair using ONLY commits up to each yearly (or 6-month rolling) cutoff t.
  # A dev is 'primary owner'/core of a file at t if their DOA(dev,file,t) is the MAX among all devs who touched
  # that file AND DOA > threshold used by Avelino et al. (paper reports the exact cutoff, e.g. DOA>3.293 baseline).

  def compute_doa_snapshot(commits, cutoff_date):
      file_dev_stats = defaultdict(lambda: defaultdict(lambda: {'first_author': None, 'ac': 0, 'dl': 0}))
      for c in commits:
          if c['date'] > cutoff_date: continue
          for (path, added, deleted) in c['files']:
              s = file_dev_stats[path][c['author_email']]
              if s['first_author'] is None: s['first_author'] = c['author_email']
              s['ac'] += 1; s['dl'] += deleted
      doa = {}
      for path, devs in file_dev_stats.items():
          first_author = next(iter(devs))  # actual first author = earliest commit's author for that file
          for dev, s in devs.items():
              fa = 1 if dev == first_author else 0
              doa[(dev,path)] = 3.293 + 1.098*fa - 0.164*(s['ac']**0.5) + 0.230*log(1+s['dl'])
      return doa

  # Truck Factor set at t = greedy min set of devs whose removal drops 'coverage'
  # (files with an unambiguous owner) below 50% -- reuse Avelino et al.'s exact TF greedy algorithm.
  def truck_factor_set(doa_snapshot):
      file_owner = {}
      for (dev,path), score in doa_snapshot.items():
          if path not in file_owner or score > file_owner[path][1]:
              file_owner[path] = (dev, score)
      owned_files_per_dev = Counter(dev for dev,_ in file_owner.values())
      total_files = len(file_owner)
      tf_set, covered = [], 0
      for dev, n in owned_files_per_dev.most_common():
          tf_set.append(dev); covered += n
          if covered >= 0.5*total_files: break
      return tf_set

  # === STAGE 4: TFDD detection -- scan yearly snapshots chronologically ===
  for repo in filtered:
      commits = load_commits(repo['id'])
      yearly_dates = pd.date_range(repo['created_at'], repo['last_commit'], freq='365D')
      tf_history = [(d, truck_factor_set(compute_doa_snapshot(commits, d))) for d in yearly_dates]
      last_active = {dev: max(c['date'] for c in commits if c['author_email']==dev) for dev in all_devs}
      for i, (d, tf_set) in enumerate(tf_history):
          # TFDD: every dev in tf_set has been silent >= 1yr (validated threshold) as of d
          if tf_set and all((d - last_active[dev]).days >= 365 for dev in tf_set):
              if len(tf_set) == 1:  # FOUNDER-ONLY TFDD -- the subset this study targets
                  founder = tf_set[0]
                  tfdd_date = min(last_active[founder] + timedelta(365), d)
                  record_tfdd_event(repo['id'], founder, tfdd_date)
                  break  # first founder-only TFDD only, per investigation_approach step 2

  # === STAGE 5: pre-departure diffusion metrics (THE NEW MEASUREMENT) ===
  for event in tfdd_events:
      window_start = event.tfdd_date - timedelta(days=365)   # 12mo before
      window_end   = event.tfdd_date - timedelta(days=180)    # 6mo before
      window_commits = [c for c in commits if window_start <= c['date'] < window_end]
      founder_commits = sum(1 for c in window_commits if c['author_email']==event.founder)
      founder_share = founder_commits / max(1,len(window_commits))
      doa_at_window_end = compute_doa_snapshot(commits, window_end)
      file_owner = argmax_owner_per_file(doa_at_window_end)
      non_founder_owners = {dev for dev,path in file_owner.items() if dev != event.founder}
      event.founder_share = founder_share
      event.n_diffused_owners = len(non_founder_owners)
      # snapshot covariates AT TFDD for comparison to Avelino et al.'s d=0.13-0.26 result
      event.devs_at_tfdd, event.commits_at_tfdd, event.files_at_tfdd = snapshot_covariates(commits, event.tfdd_date)

  # === STAGE 6: survival label (Avelino et al. Active/Inactive model, 18mo window) ===
  for event in tfdd_events:
      post = [c for c in commits if event.tfdd_date <= c['date'] < event.tfdd_date+timedelta(days=548)]
      new_tf_devs = {c['author_email'] for c in post} - {event.founder}
      doa_post = compute_doa_snapshot(commits, event.tfdd_date+timedelta(days=548))
      recovered_tf = truck_factor_set(doa_post)
      event.survived = bool(recovered_tf) and any(d != event.founder for d in recovered_tf)
      event.grade = classify_thriving_maintained_dormant_dead(post, recovered_tf)

  # === STAGE 7: falsification / placebo check ===
  for event in tfdd_events:
      random_window = sample_random_window(event.repo, exclude=near_tfdd)
      event.placebo_founder_share, event.placebo_n_diffused = compute_window_metrics(random_window)

  # === STAGE 8: matched pairs + regression ===
  buckets = bucket_by(stars=log_deciles, forks=log_deciles, n_contributors=log_deciles, language=exact)
  matched_pairs = []
  for bucket, events in groupby(tfdd_events, buckets):
      lo = [e for e in events if e.founder_share < 0.50 and e.n_diffused_owners >= 2]
      hi = [e for e in events if e.founder_share >= 0.80]
      matched_pairs += greedy_nearest_neighbor_match(lo, hi, on=['stars','forks','n_contributors'])

  risk_ratio, ci95 = bootstrap_survival_rate_ratio(matched_pairs, n_boot=5000)

  import statsmodels.api as sm
  X = df[['founder_share','n_diffused_owners','log_stars','log_forks','n_contributors','language_dummies','license_dummies']]
  model = sm.Logit(df['survived'], sm.add_constant(X)).fit()
  pvals_bh = benjamini_hochberg(model.pvalues)
  std_effect_sizes = standardized_coefs(model, X)  # compare vs Avelino et al. d=0.13(files)/0.25-0.26(devs,commits)

  # placebo comparison: refit model with placebo_founder_share / placebo_n_diffused instead
  placebo_model = sm.Logit(df['survived'], sm.add_constant(df[['placebo_founder_share','placebo_n_diffused', ...]])).fit()

  # === STAGE 9: write method_out.json ===
  results = {
    'n_repos_sampled': ..., 'n_founder_tfdd_events': ..., 'unconditioned_survival_rate': ...,  # vs Avelino 41%
    'matched_pair_risk_ratio': risk_ratio, 'ci95': ci95,
    'regression_coefs': model.params.to_dict(), 'pvals_bh': pvals_bh, 'std_effect_sizes': std_effect_sizes,
    'placebo_coefs': placebo_model.params.to_dict(),
    'snapshot_covariate_effect_sizes_d': cohens_d(devs_at_tfdd, commits_at_tfdd, files_at_tfdd, by=survived),
    'per_event_records': [...]  # full row-level table for downstream paper artifact
  }
  json.dump(results, open('method_out.json','w'), indent=2)
fallback_plan: |-
  Primary risk is DATA VOLUME/TIME, not algorithmic novelty -- the DOA/TF pipeline is fully specified in Avelino et al. and Fritz et al., so implement it exactly rather than approximate it. Layered fallbacks, in order:
  1. If GitHub API rate limits (60/hr unauthenticated, 5000/hr with a token) block reaching ~240 candidate repos within the 6h budget, drop SAMPLE_PER_LANG to 15-20 and/or restrict to 3 languages (Python, JavaScript, Go) -- still enough for matched pairs if founder-only TFDDs are ~16%*66%=~10% of repos (Avelino et al.'s own rates), i.e. expect ~10-25 usable events from 150-240 repos; if fewer than ~15 founder-TFDD events are found, RELAX the founder-only TF=1 requirement's downstream matched-pair bucket granularity (fewer bucket dimensions: drop 'license' from matching, keep only stars+language) rather than abandoning the matched-pairs design, and report the regression as the primary result with matched-pairs as a secondary/exploratory check, clearly labeled with the reduced n.
  2. If `git clone --bare` of large repos (e.g. large C++ projects) times out or exceeds disk, use `git clone --bare --filter=blob:none` (partial clone, still gives full commit/path history which is all DOA needs) or cap repo size by GitHub API `size` field before selection (exclude repos >500MB).
  3. If PyDriller is too slow walking full history for large repos (some real repos have 50k+ commits), fall back to raw `git log --numstat --format='%H|%ae|%cI'` parsed manually via subprocess -- much faster, same information needed (author, date, per-file added/deleted lines).
  4. If GitHub's search API cannot cleanly stratify by popularity bucket (search API caps at 1000 results per query), issue multiple queries partitioning by star-count ranges as already planned in Stage 0 -- this is the mitigation, not a fallback trigger.
  5. If DOA-based TFDD detection finds zero or very few founder-only (TF=1) TFDD events after scanning all sampled repos (possible if the sample skews toward large multi-founder projects), explicitly RELAX the founder-only definition to 'founder retained TF-set membership until departure, TF-set size <=2 at detachment' and report both the strict (TF=1) and relaxed (TF<=2) results separately -- do not silently substitute one for the other.
  6. If the 18-month post-TFDD survival window right-censors too many events (repo's total history <3yr from birth to TFDD+18mo), drop those events from the labeled set but KEEP them in a separate 'right-censored, excluded' count reported in method_out.json for transparency -- do not impute or guess their outcome.
  7. If statsmodels' logistic regression fails to converge (e.g., quasi-separation with a small n and multiple dummy variables), reduce covariates to a parsimonious set (founder_share, n_diffused_owners, log_stars, log_n_contributors only, dropping language/license dummies or collapsing them to 2-3 groups) and report this explicitly as a deviation from the full model in success_criteria point 2.
  8. If time runs out before the full logistic + BH correction can be fit, still produce and save: (a) the founder-only TFDD event table with all raw metrics, (b) the unconditioned survival rate for direct Avelino-et-al comparability, and (c) a simple two-group t-test/Mann-Whitney comparison of founder_share and n_diffused_owners between survivors and non-survivors -- a minimally complete result beats an unfinished full regression.
testing_plan: |-
  Gradual scaling per aii-long-running-tasks pattern -- validate correctness on a tiny, fully-inspectable slice before scaling to the full sample:
  1. MINI TEST (5 repos, hand-picked, ~15 min of runtime budget): pick 5 well-known repos with KNOWN founder-departure histories the executor can sanity-check by eye (e.g. a small abandoned utility library where a single early README/commit-log inspection confirms one dominant early committer who later went silent). Clone, run DOA computation for just 2-3 yearly snapshots, and MANUALLY verify: (a) the computed first-author-per-file matches `git log --diff-filter=A --follow -- <file>` for a handful of spot-checked files, (b) the DOA formula output is a plausible positive number in the same range as Fritz et al.'s reported examples, (c) the greedy TF-set algorithm on this tiny repo returns a sensible minimal set (e.g. TF=1 for a single-maintainer repo). This catches formula transcription errors and alias-resolution bugs before they propagate.
  2. PIPELINE-SHAPE TEST (10-15 repos): run the FULL pipeline (Stages 0-9) end-to-end on a small sample to confirm every stage produces non-degenerate output -- specifically check: TFDD detection finds at least 1-2 founder-only events (not zero, which would indicate a bug in the 1-year-silence or TF=1 logic), pre-departure metrics are in [0,1] for founder_share and non-negative integers for n_diffused_owners, and survival labels split into both True and False (not all-one-class, which would break the regression). If TFDD events = 0 at this scale, debug the silence-threshold and TF-set logic before scaling up -- do not proceed to full sampling with an undetected bug.
  3. CROSS-CHECK AGAINST AVELINO ET AL.'S PUBLISHED NUMBERS: on whatever founder-only TFDD events are found in the eventual full run, report the UNCONDITIONED survival rate and sanity-check it is in a plausible neighborhood of their reported 41% (not required to match exactly -- different sample -- but a wildly different rate, e.g. 95% or 2%, signals a bug in survival labeling, most likely the Active/Inactive recovery criterion being mis-implemented as 'any commit at all' rather than 'a new TF developer attracted').
  4. SCALE UP in 2-3 steps (e.g. 15 -> 80 -> 240 repos) per the gradual-scaling pattern, checking wall-clock time and GitHub API quota consumption at each step before committing to the next, and stopping early (documenting n achieved) if the 6h budget is at risk -- prioritize finishing Stages 1-9 on a smaller-than-planned sample over running out of time mid-clone.
  5. FINAL VALIDATION: before writing method_out.json, confirm (a) no NaN/inf in the regression design matrix, (b) the BH correction is applied to the RIGHT set of p-values (the diffusion predictors, not all covariates indiscriminately, per success_criteria point 2), (c) the placebo/shuffle check (Stage 7) was actually run on a comparable number of events to the main analysis, not skipped.
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

### [6] SYSTEM-USER prompt · 2026-08-21 16:44:23 UTC

```
<validation-feedback>
Attempt 1 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [7] SYSTEM-USER prompt · 2026-08-21 16:45:01 UTC

```
<validation-feedback>
Attempt 2 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [8] SYSTEM-USER prompt · 2026-08-21 16:45:35 UTC

```
[Your previous response had no visible output. Please continue and produce a user-visible response.]
```

### [9] SYSTEM-USER prompt · 2026-08-21 16:45:41 UTC

```
<validation-feedback>
Attempt 3 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [10] SYSTEM-USER prompt · 2026-08-21 17:38:48 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_1_idx2
type: experiment
title: Does authority diffusion before founder exit predict OSS survival?
summary: >-
  Re-implements Avelino et al.'s (ESEM 2019) DOA/Truck-Factor/TFDD/Active-Inactive pipeline from GitHub commit histories,
  detects founder-only TFDD events, adds a NEW pre-departure metric (founder commit-share and count of independent non-founder
  DOA file-owners in the 6-12 months before TFDD) that their published pipeline does not compute, labels 18-month post-TFDD
  survival, and tests whether this pre-departure authority-diffusion trajectory predicts survival better than size/popularity
  covariates via matched pairs and a BH-corrected regression.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  # === STAGE 0: repo sampling (self-contained, no DATASET dependency available) ===
  # Use GitHub REST API (via `requests`, authenticated with GITHUB_TOKEN env var if present,
  # else unauthenticated at 60 req/hr -- budget calls accordingly) OR the `pydriller`/`PyGithub`
  # PyPI packages for repo cloning + commit walking. Do NOT scrape git objects manually.
  import requests, subprocess, time
  from pydriller import Repository  # pip: pydriller -- walks full commit history incl. file diffs

  LANGUAGES = ['Python','JavaScript','Java','Go','Ruby','C++']  # subset of Avelino et al.'s 6
  SAMPLE_PER_LANG = 40  # 6*40=240 candidate repos -- gradual scaling, see testing_plan

  candidates = []
  for lang in LANGUAGES:
      # GitHub search API: sort by stars, paginate to get popularity STRATA not just top-N
      # (avoids confounding survival analysis with "only mega-popular repos" bias)
      for page_bucket in ['stars:>5000','stars:500..5000','stars:50..500']:
          resp = github_search_repos(f'language:{lang} {page_bucket}', per_page=SAMPLE_PER_LANG//3)
          candidates += resp
      time.sleep(2)  # respect rate limit

  # === STAGE 1: filter mining artifacts (Avelino et al.'s exclusion criteria) ===
  filtered = []
  for repo in candidates:
      meta = get_repo_metadata(repo)
      if meta['age_days'] < 2*365: continue           # need >=2yr history (Avelino) -- we need 3yr (TFDD + 18mo)
      if meta['age_days'] < 3*365: continue            # our stricter requirement per assumptions
      if is_fork(meta) or is_archive_list(repo) or not has_code_files(repo): continue  # 'perils of mining GitHub'
      filtered.append(repo)

  # === STAGE 2: clone shallow-but-full-history, walk commits with PyDriller ===
  for repo in filtered:
      subprocess.run(['git','clone','--bare', repo['clone_url'], f'/tmp/repos/{repo["id"]}.git'], timeout=600)
      commits = []
      for c in Repository(f'/tmp/repos/{repo["id"]}.git').traverse_commits():
          commits.append({
              'hash': c.hash, 'author_email': resolve_alias(c.author.email),  # GitHub API email->account map
              'date': c.committer_date, 'files': [(m.new_path, m.added_lines, m.deleted_lines) for m in c.modified_files]
          })
      save_commits(repo['id'], commits)

  # === STAGE 3: DOA computation (Fritz et al. formula, as specified by Avelino ICPC 2016 / ESEM 2019) ===
  # DOA(dev, file, t) = 3.293 + 1.098*FA - 0.164*(AC^(1/2)) + 0.230*ln(1+DL)
  #   FA = 1 if dev is first author of file else 0
  #   AC = number of dev's changes to file up to time t
  #   DL = deletions dev made to file (churn) -- exact formula per paper; verify against ICPC2016 arXiv text
  # Compute DOA for EVERY (dev,file) pair using ONLY commits up to each yearly (or 6-month rolling) cutoff t.
  # A dev is 'primary owner'/core of a file at t if their DOA(dev,file,t) is the MAX among all devs who touched
  # that file AND DOA > threshold used by Avelino et al. (paper reports the exact cutoff, e.g. DOA>3.293 baseline).

  def compute_doa_snapshot(commits, cutoff_date):
      file_dev_stats = defaultdict(lambda: defaultdict(lambda: {'first_author': None, 'ac': 0, 'dl': 0}))
      for c in commits:
          if c['date'] > cutoff_date: continue
          for (path, added, deleted) in c['files']:
              s = file_dev_stats[path][c['author_email']]
              if s['first_author'] is None: s['first_author'] = c['author_email']
              s['ac'] += 1; s['dl'] += deleted
      doa = {}
      for path, devs in file_dev_stats.items():
          first_author = next(iter(devs))  # actual first author = earliest commit's author for that file
          for dev, s in devs.items():
              fa = 1 if dev == first_author else 0
              doa[(dev,path)] = 3.293 + 1.098*fa - 0.164*(s['ac']**0.5) + 0.230*log(1+s['dl'])
      return doa

  # Truck Factor set at t = greedy min set of devs whose removal drops 'coverage'
  # (files with an unambiguous owner) below 50% -- reuse Avelino et al.'s exact TF greedy algorithm.
  def truck_factor_set(doa_snapshot):
      file_owner = {}
      for (dev,path), score in doa_snapshot.items():
          if path not in file_owner or score > file_owner[path][1]:
              file_owner[path] = (dev, score)
      owned_files_per_dev = Counter(dev for dev,_ in file_owner.values())
      total_files = len(file_owner)
      tf_set, covered = [], 0
      for dev, n in owned_files_per_dev.most_common():
          tf_set.append(dev); covered += n
          if covered >= 0.5*total_files: break
      return tf_set

  # === STAGE 4: TFDD detection -- scan yearly snapshots chronologically ===
  for repo in filtered:
      commits = load_commits(repo['id'])
      yearly_dates = pd.date_range(repo['created_at'], repo['last_commit'], freq='365D')
      tf_history = [(d, truck_factor_set(compute_doa_snapshot(commits, d))) for d in yearly_dates]
      last_active = {dev: max(c['date'] for c in commits if c['author_email']==dev) for dev in all_devs}
      for i, (d, tf_set) in enumerate(tf_history):
          # TFDD: every dev in tf_set has been silent >= 1yr (validated threshold) as of d
          if tf_set and all((d - last_active[dev]).days >= 365 for dev in tf_set):
              if len(tf_set) == 1:  # FOUNDER-ONLY TFDD -- the subset this study targets
                  founder = tf_set[0]
                  tfdd_date = min(last_active[founder] + timedelta(365), d)
                  record_tfdd_event(repo['id'], founder, tfdd_date)
                  break  # first founder-only TFDD only, per investigation_approach step 2

  # === STAGE 5: pre-departure diffusion metrics (THE NEW MEASUREMENT) ===
  for event in tfdd_events:
      window_start = event.tfdd_date - timedelta(days=365)   # 12mo before
      window_end   = event.tfdd_date - timedelta(days=180)    # 6mo before
      window_commits = [c for c in commits if window_start <= c['date'] < window_end]
      founder_commits = sum(1 for c in window_commits if c['author_email']==event.founder)
      founder_share = founder_commits / max(1,len(window_commits))
      doa_at_window_end = compute_doa_snapshot(commits, window_end)
      file_owner = argmax_owner_per_file(doa_at_window_end)
      non_founder_owners = {dev for dev,path in file_owner.items() if dev != event.founder}
      event.founder_share = founder_share
      event.n_diffused_owners = len(non_founder_owners)
      # snapshot covariates AT TFDD for comparison to Avelino et al.'s d=0.13-0.26 result
      event.devs_at_tfdd, event.commits_at_tfdd, event.files_at_tfdd = snapshot_covariates(commits, event.tfdd_date)

  # === STAGE 6: survival label (Avelino et al. Active/Inactive model, 18mo window) ===
  for event in tfdd_events:
      post = [c for c in commits if event.tfdd_date <= c['date'] < event.tfdd_date+timedelta(days=548)]
      new_tf_devs = {c['author_email'] for c in post} - {event.founder}
      doa_post = compute_doa_snapshot(commits, event.tfdd_date+timedelta(days=548))
      recovered_tf = truck_factor_set(doa_post)
      event.survived = bool(recovered_tf) and any(d != event.founder for d in recovered_tf)
      event.grade = classify_thriving_maintained_dormant_dead(post, recovered_tf)

  # === STAGE 7: falsification / placebo check ===
  for event in tfdd_events:
      random_window = sample_random_window(event.repo, exclude=near_tfdd)
      event.placebo_founder_share, event.placebo_n_diffused = compute_window_metrics(random_window)

  # === STAGE 8: matched pairs + regression ===
  buckets = bucket_by(stars=log_deciles, forks=log_deciles, n_contributors=log_deciles, language=exact)
  matched_pairs = []
  for bucket, events in groupby(tfdd_events, buckets):
      lo = [e for e in events if e.founder_share < 0.50 and e.n_diffused_owners >= 2]
      hi = [e for e in events if e.founder_share >= 0.80]
      matched_pairs += greedy_nearest_neighbor_match(lo, hi, on=['stars','forks','n_contributors'])

  risk_ratio, ci95 = bootstrap_survival_rate_ratio(matched_pairs, n_boot=5000)

  import statsmodels.api as sm
  X = df[['founder_share','n_diffused_owners','log_stars','log_forks','n_contributors','language_dummies','license_dummies']]
  model = sm.Logit(df['survived'], sm.add_constant(X)).fit()
  pvals_bh = benjamini_hochberg(model.pvalues)
  std_effect_sizes = standardized_coefs(model, X)  # compare vs Avelino et al. d=0.13(files)/0.25-0.26(devs,commits)

  # placebo comparison: refit model with placebo_founder_share / placebo_n_diffused instead
  placebo_model = sm.Logit(df['survived'], sm.add_constant(df[['placebo_founder_share','placebo_n_diffused', ...]])).fit()

  # === STAGE 9: write method_out.json ===
  results = {
    'n_repos_sampled': ..., 'n_founder_tfdd_events': ..., 'unconditioned_survival_rate': ...,  # vs Avelino 41%
    'matched_pair_risk_ratio': risk_ratio, 'ci95': ci95,
    'regression_coefs': model.params.to_dict(), 'pvals_bh': pvals_bh, 'std_effect_sizes': std_effect_sizes,
    'placebo_coefs': placebo_model.params.to_dict(),
    'snapshot_covariate_effect_sizes_d': cohens_d(devs_at_tfdd, commits_at_tfdd, files_at_tfdd, by=survived),
    'per_event_records': [...]  # full row-level table for downstream paper artifact
  }
  json.dump(results, open('method_out.json','w'), indent=2)
fallback_plan: |-
  Primary risk is DATA VOLUME/TIME, not algorithmic novelty -- the DOA/TF pipeline is fully specified in Avelino et al. and Fritz et al., so implement it exactly rather than approximate it. Layered fallbacks, in order:
  1. If GitHub API rate limits (60/hr unauthenticated, 5000/hr with a token) block reaching ~240 candidate repos within the 6h budget, drop SAMPLE_PER_LANG to 15-20 and/or restrict to 3 languages (Python, JavaScript, Go) -- still enough for matched pairs if founder-only TFDDs are ~16%*66%=~10% of repos (Avelino et al.'s own rates), i.e. expect ~10-25 usable events from 150-240 repos; if fewer than ~15 founder-TFDD events are found, RELAX the founder-only TF=1 requirement's downstream matched-pair bucket granularity (fewer bucket dimensions: drop 'license' from matching, keep only stars+language) rather than abandoning the matched-pairs design, and report the regression as the primary result with matched-pairs as a secondary/exploratory check, clearly labeled with the reduced n.
  2. If `git clone --bare` of large repos (e.g. large C++ projects) times out or exceeds disk, use `git clone --bare --filter=blob:none` (partial clone, still gives full commit/path history which is all DOA needs) or cap repo size by GitHub API `size` field before selection (exclude repos >500MB).
  3. If PyDriller is too slow walking full history for large repos (some real repos have 50k+ commits), fall back to raw `git log --numstat --format='%H|%ae|%cI'` parsed manually via subprocess -- much faster, same information needed (author, date, per-file added/deleted lines).
  4. If GitHub's search API cannot cleanly stratify by popularity bucket (search API caps at 1000 results per query), issue multiple queries partitioning by star-count ranges as already planned in Stage 0 -- this is the mitigation, not a fallback trigger.
  5. If DOA-based TFDD detection finds zero or very few founder-only (TF=1) TFDD events after scanning all sampled repos (possible if the sample skews toward large multi-founder projects), explicitly RELAX the founder-only definition to 'founder retained TF-set membership until departure, TF-set size <=2 at detachment' and report both the strict (TF=1) and relaxed (TF<=2) results separately -- do not silently substitute one for the other.
  6. If the 18-month post-TFDD survival window right-censors too many events (repo's total history <3yr from birth to TFDD+18mo), drop those events from the labeled set but KEEP them in a separate 'right-censored, excluded' count reported in method_out.json for transparency -- do not impute or guess their outcome.
  7. If statsmodels' logistic regression fails to converge (e.g., quasi-separation with a small n and multiple dummy variables), reduce covariates to a parsimonious set (founder_share, n_diffused_owners, log_stars, log_n_contributors only, dropping language/license dummies or collapsing them to 2-3 groups) and report this explicitly as a deviation from the full model in success_criteria point 2.
  8. If time runs out before the full logistic + BH correction can be fit, still produce and save: (a) the founder-only TFDD event table with all raw metrics, (b) the unconditioned survival rate for direct Avelino-et-al comparability, and (c) a simple two-group t-test/Mann-Whitney comparison of founder_share and n_diffused_owners between survivors and non-survivors -- a minimally complete result beats an unfinished full regression.
testing_plan: |-
  Gradual scaling per aii-long-running-tasks pattern -- validate correctness on a tiny, fully-inspectable slice before scaling to the full sample:
  1. MINI TEST (5 repos, hand-picked, ~15 min of runtime budget): pick 5 well-known repos with KNOWN founder-departure histories the executor can sanity-check by eye (e.g. a small abandoned utility library where a single early README/commit-log inspection confirms one dominant early committer who later went silent). Clone, run DOA computation for just 2-3 yearly snapshots, and MANUALLY verify: (a) the computed first-author-per-file matches `git log --diff-filter=A --follow -- <file>` for a handful of spot-checked files, (b) the DOA formula output is a plausible positive number in the same range as Fritz et al.'s reported examples, (c) the greedy TF-set algorithm on this tiny repo returns a sensible minimal set (e.g. TF=1 for a single-maintainer repo). This catches formula transcription errors and alias-resolution bugs before they propagate.
  2. PIPELINE-SHAPE TEST (10-15 repos): run the FULL pipeline (Stages 0-9) end-to-end on a small sample to confirm every stage produces non-degenerate output -- specifically check: TFDD detection finds at least 1-2 founder-only events (not zero, which would indicate a bug in the 1-year-silence or TF=1 logic), pre-departure metrics are in [0,1] for founder_share and non-negative integers for n_diffused_owners, and survival labels split into both True and False (not all-one-class, which would break the regression). If TFDD events = 0 at this scale, debug the silence-threshold and TF-set logic before scaling up -- do not proceed to full sampling with an undetected bug.
  3. CROSS-CHECK AGAINST AVELINO ET AL.'S PUBLISHED NUMBERS: on whatever founder-only TFDD events are found in the eventual full run, report the UNCONDITIONED survival rate and sanity-check it is in a plausible neighborhood of their reported 41% (not required to match exactly -- different sample -- but a wildly different rate, e.g. 95% or 2%, signals a bug in survival labeling, most likely the Active/Inactive recovery criterion being mis-implemented as 'any commit at all' rather than 'a new TF developer attracted').
  4. SCALE UP in 2-3 steps (e.g. 15 -> 80 -> 240 repos) per the gradual-scaling pattern, checking wall-clock time and GitHub API quota consumption at each step before committing to the next, and stopping early (documenting n achieved) if the 6h budget is at risk -- prioritize finishing Stages 1-9 on a smaller-than-planned sample over running out of time mid-clone.
  5. FINAL VALIDATION: before writing method_out.json, confirm (a) no NaN/inf in the regression design matrix, (b) the BH correction is applied to the RIGHT set of p-values (the diffusion predictors, not all covariates indiscriminately, per success_criteria point 2), (c) the placebo/shuffle check (Stage 7) was actually run on a comparable number of events to the main analysis, not skipped.
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

### [11] HUMAN-USER prompt · 2026-08-21 17:38:48 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [12] SYSTEM-USER prompt · 2026-08-21 17:48:24 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_1_idx2
type: experiment
title: Does authority diffusion before founder exit predict OSS survival?
summary: >-
  Re-implements Avelino et al.'s (ESEM 2019) DOA/Truck-Factor/TFDD/Active-Inactive pipeline from GitHub commit histories,
  detects founder-only TFDD events, adds a NEW pre-departure metric (founder commit-share and count of independent non-founder
  DOA file-owners in the 6-12 months before TFDD) that their published pipeline does not compute, labels 18-month post-TFDD
  survival, and tests whether this pre-departure authority-diffusion trajectory predicts survival better than size/popularity
  covariates via matched pairs and a BH-corrected regression.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  # === STAGE 0: repo sampling (self-contained, no DATASET dependency available) ===
  # Use GitHub REST API (via `requests`, authenticated with GITHUB_TOKEN env var if present,
  # else unauthenticated at 60 req/hr -- budget calls accordingly) OR the `pydriller`/`PyGithub`
  # PyPI packages for repo cloning + commit walking. Do NOT scrape git objects manually.
  import requests, subprocess, time
  from pydriller import Repository  # pip: pydriller -- walks full commit history incl. file diffs

  LANGUAGES = ['Python','JavaScript','Java','Go','Ruby','C++']  # subset of Avelino et al.'s 6
  SAMPLE_PER_LANG = 40  # 6*40=240 candidate repos -- gradual scaling, see testing_plan

  candidates = []
  for lang in LANGUAGES:
      # GitHub search API: sort by stars, paginate to get popularity STRATA not just top-N
      # (avoids confounding survival analysis with "only mega-popular repos" bias)
      for page_bucket in ['stars:>5000','stars:500..5000','stars:50..500']:
          resp = github_search_repos(f'language:{lang} {page_bucket}', per_page=SAMPLE_PER_LANG//3)
          candidates += resp
      time.sleep(2)  # respect rate limit

  # === STAGE 1: filter mining artifacts (Avelino et al.'s exclusion criteria) ===
  filtered = []
  for repo in candidates:
      meta = get_repo_metadata(repo)
      if meta['age_days'] < 2*365: continue           # need >=2yr history (Avelino) -- we need 3yr (TFDD + 18mo)
      if meta['age_days'] < 3*365: continue            # our stricter requirement per assumptions
      if is_fork(meta) or is_archive_list(repo) or not has_code_files(repo): continue  # 'perils of mining GitHub'
      filtered.append(repo)

  # === STAGE 2: clone shallow-but-full-history, walk commits with PyDriller ===
  for repo in filtered:
      subprocess.run(['git','clone','--bare', repo['clone_url'], f'/tmp/repos/{repo["id"]}.git'], timeout=600)
      commits = []
      for c in Repository(f'/tmp/repos/{repo["id"]}.git').traverse_commits():
          commits.append({
              'hash': c.hash, 'author_email': resolve_alias(c.author.email),  # GitHub API email->account map
              'date': c.committer_date, 'files': [(m.new_path, m.added_lines, m.deleted_lines) for m in c.modified_files]
          })
      save_commits(repo['id'], commits)

  # === STAGE 3: DOA computation (Fritz et al. formula, as specified by Avelino ICPC 2016 / ESEM 2019) ===
  # DOA(dev, file, t) = 3.293 + 1.098*FA - 0.164*(AC^(1/2)) + 0.230*ln(1+DL)
  #   FA = 1 if dev is first author of file else 0
  #   AC = number of dev's changes to file up to time t
  #   DL = deletions dev made to file (churn) -- exact formula per paper; verify against ICPC2016 arXiv text
  # Compute DOA for EVERY (dev,file) pair using ONLY commits up to each yearly (or 6-month rolling) cutoff t.
  # A dev is 'primary owner'/core of a file at t if their DOA(dev,file,t) is the MAX among all devs who touched
  # that file AND DOA > threshold used by Avelino et al. (paper reports the exact cutoff, e.g. DOA>3.293 baseline).

  def compute_doa_snapshot(commits, cutoff_date):
      file_dev_stats = defaultdict(lambda: defaultdict(lambda: {'first_author': None, 'ac': 0, 'dl': 0}))
      for c in commits:
          if c['date'] > cutoff_date: continue
          for (path, added, deleted) in c['files']:
              s = file_dev_stats[path][c['author_email']]
              if s['first_author'] is None: s['first_author'] = c['author_email']
              s['ac'] += 1; s['dl'] += deleted
      doa = {}
      for path, devs in file_dev_stats.items():
          first_author = next(iter(devs))  # actual first author = earliest commit's author for that file
          for dev, s in devs.items():
              fa = 1 if dev == first_author else 0
              doa[(dev,path)] = 3.293 + 1.098*fa - 0.164*(s['ac']**0.5) + 0.230*log(1+s['dl'])
      return doa

  # Truck Factor set at t = greedy min set of devs whose removal drops 'coverage'
  # (files with an unambiguous owner) below 50% -- reuse Avelino et al.'s exact TF greedy algorithm.
  def truck_factor_set(doa_snapshot):
      file_owner = {}
      for (dev,path), score in doa_snapshot.items():
          if path not in file_owner or score > file_owner[path][1]:
              file_owner[path] = (dev, score)
      owned_files_per_dev = Counter(dev for dev,_ in file_owner.values())
      total_files = len(file_owner)
      tf_set, covered = [], 0
      for dev, n in owned_files_per_dev.most_common():
          tf_set.append(dev); covered += n
          if covered >= 0.5*total_files: break
      return tf_set

  # === STAGE 4: TFDD detection -- scan yearly snapshots chronologically ===
  for repo in filtered:
      commits = load_commits(repo['id'])
      yearly_dates = pd.date_range(repo['created_at'], repo['last_commit'], freq='365D')
      tf_history = [(d, truck_factor_set(compute_doa_snapshot(commits, d))) for d in yearly_dates]
      last_active = {dev: max(c['date'] for c in commits if c['author_email']==dev) for dev in all_devs}
      for i, (d, tf_set) in enumerate(tf_history):
          # TFDD: every dev in tf_set has been silent >= 1yr (validated threshold) as of d
          if tf_set and all((d - last_active[dev]).days >= 365 for dev in tf_set):
              if len(tf_set) == 1:  # FOUNDER-ONLY TFDD -- the subset this study targets
                  founder = tf_set[0]
                  tfdd_date = min(last_active[founder] + timedelta(365), d)
                  record_tfdd_event(repo['id'], founder, tfdd_date)
                  break  # first founder-only TFDD only, per investigation_approach step 2

  # === STAGE 5: pre-departure diffusion metrics (THE NEW MEASUREMENT) ===
  for event in tfdd_events:
      window_start = event.tfdd_date - timedelta(days=365)   # 12mo before
      window_end   = event.tfdd_date - timedelta(days=180)    # 6mo before
      window_commits = [c for c in commits if window_start <= c['date'] < window_end]
      founder_commits = sum(1 for c in window_commits if c['author_email']==event.founder)
      founder_share = founder_commits / max(1,len(window_commits))
      doa_at_window_end = compute_doa_snapshot(commits, window_end)
      file_owner = argmax_owner_per_file(doa_at_window_end)
      non_founder_owners = {dev for dev,path in file_owner.items() if dev != event.founder}
      event.founder_share = founder_share
      event.n_diffused_owners = len(non_founder_owners)
      # snapshot covariates AT TFDD for comparison to Avelino et al.'s d=0.13-0.26 result
      event.devs_at_tfdd, event.commits_at_tfdd, event.files_at_tfdd = snapshot_covariates(commits, event.tfdd_date)

  # === STAGE 6: survival label (Avelino et al. Active/Inactive model, 18mo window) ===
  for event in tfdd_events:
      post = [c for c in commits if event.tfdd_date <= c['date'] < event.tfdd_date+timedelta(days=548)]
      new_tf_devs = {c['author_email'] for c in post} - {event.founder}
      doa_post = compute_doa_snapshot(commits, event.tfdd_date+timedelta(days=548))
      recovered_tf = truck_factor_set(doa_post)
      event.survived = bool(recovered_tf) and any(d != event.founder for d in recovered_tf)
      event.grade = classify_thriving_maintained_dormant_dead(post, recovered_tf)

  # === STAGE 7: falsification / placebo check ===
  for event in tfdd_events:
      random_window = sample_random_window(event.repo, exclude=near_tfdd)
      event.placebo_founder_share, event.placebo_n_diffused = compute_window_metrics(random_window)

  # === STAGE 8: matched pairs + regression ===
  buckets = bucket_by(stars=log_deciles, forks=log_deciles, n_contributors=log_deciles, language=exact)
  matched_pairs = []
  for bucket, events in groupby(tfdd_events, buckets):
      lo = [e for e in events if e.founder_share < 0.50 and e.n_diffused_owners >= 2]
      hi = [e for e in events if e.founder_share >= 0.80]
      matched_pairs += greedy_nearest_neighbor_match(lo, hi, on=['stars','forks','n_contributors'])

  risk_ratio, ci95 = bootstrap_survival_rate_ratio(matched_pairs, n_boot=5000)

  import statsmodels.api as sm
  X = df[['founder_share','n_diffused_owners','log_stars','log_forks','n_contributors','language_dummies','license_dummies']]
  model = sm.Logit(df['survived'], sm.add_constant(X)).fit()
  pvals_bh = benjamini_hochberg(model.pvalues)
  std_effect_sizes = standardized_coefs(model, X)  # compare vs Avelino et al. d=0.13(files)/0.25-0.26(devs,commits)

  # placebo comparison: refit model with placebo_founder_share / placebo_n_diffused instead
  placebo_model = sm.Logit(df['survived'], sm.add_constant(df[['placebo_founder_share','placebo_n_diffused', ...]])).fit()

  # === STAGE 9: write method_out.json ===
  results = {
    'n_repos_sampled': ..., 'n_founder_tfdd_events': ..., 'unconditioned_survival_rate': ...,  # vs Avelino 41%
    'matched_pair_risk_ratio': risk_ratio, 'ci95': ci95,
    'regression_coefs': model.params.to_dict(), 'pvals_bh': pvals_bh, 'std_effect_sizes': std_effect_sizes,
    'placebo_coefs': placebo_model.params.to_dict(),
    'snapshot_covariate_effect_sizes_d': cohens_d(devs_at_tfdd, commits_at_tfdd, files_at_tfdd, by=survived),
    'per_event_records': [...]  # full row-level table for downstream paper artifact
  }
  json.dump(results, open('method_out.json','w'), indent=2)
fallback_plan: |-
  Primary risk is DATA VOLUME/TIME, not algorithmic novelty -- the DOA/TF pipeline is fully specified in Avelino et al. and Fritz et al., so implement it exactly rather than approximate it. Layered fallbacks, in order:
  1. If GitHub API rate limits (60/hr unauthenticated, 5000/hr with a token) block reaching ~240 candidate repos within the 6h budget, drop SAMPLE_PER_LANG to 15-20 and/or restrict to 3 languages (Python, JavaScript, Go) -- still enough for matched pairs if founder-only TFDDs are ~16%*66%=~10% of repos (Avelino et al.'s own rates), i.e. expect ~10-25 usable events from 150-240 repos; if fewer than ~15 founder-TFDD events are found, RELAX the founder-only TF=1 requirement's downstream matched-pair bucket granularity (fewer bucket dimensions: drop 'license' from matching, keep only stars+language) rather than abandoning the matched-pairs design, and report the regression as the primary result with matched-pairs as a secondary/exploratory check, clearly labeled with the reduced n.
  2. If `git clone --bare` of large repos (e.g. large C++ projects) times out or exceeds disk, use `git clone --bare --filter=blob:none` (partial clone, still gives full commit/path history which is all DOA needs) or cap repo size by GitHub API `size` field before selection (exclude repos >500MB).
  3. If PyDriller is too slow walking full history for large repos (some real repos have 50k+ commits), fall back to raw `git log --numstat --format='%H|%ae|%cI'` parsed manually via subprocess -- much faster, same information needed (author, date, per-file added/deleted lines).
  4. If GitHub's search API cannot cleanly stratify by popularity bucket (search API caps at 1000 results per query), issue multiple queries partitioning by star-count ranges as already planned in Stage 0 -- this is the mitigation, not a fallback trigger.
  5. If DOA-based TFDD detection finds zero or very few founder-only (TF=1) TFDD events after scanning all sampled repos (possible if the sample skews toward large multi-founder projects), explicitly RELAX the founder-only definition to 'founder retained TF-set membership until departure, TF-set size <=2 at detachment' and report both the strict (TF=1) and relaxed (TF<=2) results separately -- do not silently substitute one for the other.
  6. If the 18-month post-TFDD survival window right-censors too many events (repo's total history <3yr from birth to TFDD+18mo), drop those events from the labeled set but KEEP them in a separate 'right-censored, excluded' count reported in method_out.json for transparency -- do not impute or guess their outcome.
  7. If statsmodels' logistic regression fails to converge (e.g., quasi-separation with a small n and multiple dummy variables), reduce covariates to a parsimonious set (founder_share, n_diffused_owners, log_stars, log_n_contributors only, dropping language/license dummies or collapsing them to 2-3 groups) and report this explicitly as a deviation from the full model in success_criteria point 2.
  8. If time runs out before the full logistic + BH correction can be fit, still produce and save: (a) the founder-only TFDD event table with all raw metrics, (b) the unconditioned survival rate for direct Avelino-et-al comparability, and (c) a simple two-group t-test/Mann-Whitney comparison of founder_share and n_diffused_owners between survivors and non-survivors -- a minimally complete result beats an unfinished full regression.
testing_plan: |-
  Gradual scaling per aii-long-running-tasks pattern -- validate correctness on a tiny, fully-inspectable slice before scaling to the full sample:
  1. MINI TEST (5 repos, hand-picked, ~15 min of runtime budget): pick 5 well-known repos with KNOWN founder-departure histories the executor can sanity-check by eye (e.g. a small abandoned utility library where a single early README/commit-log inspection confirms one dominant early committer who later went silent). Clone, run DOA computation for just 2-3 yearly snapshots, and MANUALLY verify: (a) the computed first-author-per-file matches `git log --diff-filter=A --follow -- <file>` for a handful of spot-checked files, (b) the DOA formula output is a plausible positive number in the same range as Fritz et al.'s reported examples, (c) the greedy TF-set algorithm on this tiny repo returns a sensible minimal set (e.g. TF=1 for a single-maintainer repo). This catches formula transcription errors and alias-resolution bugs before they propagate.
  2. PIPELINE-SHAPE TEST (10-15 repos): run the FULL pipeline (Stages 0-9) end-to-end on a small sample to confirm every stage produces non-degenerate output -- specifically check: TFDD detection finds at least 1-2 founder-only events (not zero, which would indicate a bug in the 1-year-silence or TF=1 logic), pre-departure metrics are in [0,1] for founder_share and non-negative integers for n_diffused_owners, and survival labels split into both True and False (not all-one-class, which would break the regression). If TFDD events = 0 at this scale, debug the silence-threshold and TF-set logic before scaling up -- do not proceed to full sampling with an undetected bug.
  3. CROSS-CHECK AGAINST AVELINO ET AL.'S PUBLISHED NUMBERS: on whatever founder-only TFDD events are found in the eventual full run, report the UNCONDITIONED survival rate and sanity-check it is in a plausible neighborhood of their reported 41% (not required to match exactly -- different sample -- but a wildly different rate, e.g. 95% or 2%, signals a bug in survival labeling, most likely the Active/Inactive recovery criterion being mis-implemented as 'any commit at all' rather than 'a new TF developer attracted').
  4. SCALE UP in 2-3 steps (e.g. 15 -> 80 -> 240 repos) per the gradual-scaling pattern, checking wall-clock time and GitHub API quota consumption at each step before committing to the next, and stopping early (documenting n achieved) if the 6h budget is at risk -- prioritize finishing Stages 1-9 on a smaller-than-planned sample over running out of time mid-clone.
  5. FINAL VALIDATION: before writing method_out.json, confirm (a) no NaN/inf in the regression design matrix, (b) the BH correction is applied to the RIGHT set of p-values (the diffusion predictors, not all covariates indiscriminately, per success_criteria point 2), (c) the placebo/shuffle check (Stage 7) was actually run on a comparable number of events to the main analysis, not skipped.
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

### [13] SYSTEM-USER prompt · 2026-08-21 17:49:52 UTC

```
<validation-feedback>
Attempt 1 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [14] SYSTEM-USER prompt · 2026-08-21 17:50:27 UTC

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

### [15] SYSTEM-USER prompt · 2026-08-21 19:01:31 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_1_idx2
type: experiment
title: Does authority diffusion before founder exit predict OSS survival?
summary: >-
  Re-implements Avelino et al.'s (ESEM 2019) DOA/Truck-Factor/TFDD/Active-Inactive pipeline from GitHub commit histories,
  detects founder-only TFDD events, adds a NEW pre-departure metric (founder commit-share and count of independent non-founder
  DOA file-owners in the 6-12 months before TFDD) that their published pipeline does not compute, labels 18-month post-TFDD
  survival, and tests whether this pre-departure authority-diffusion trajectory predicts survival better than size/popularity
  covariates via matched pairs and a BH-corrected regression.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: |-
  # === STAGE 0: repo sampling (self-contained, no DATASET dependency available) ===
  # Use GitHub REST API (via `requests`, authenticated with GITHUB_TOKEN env var if present,
  # else unauthenticated at 60 req/hr -- budget calls accordingly) OR the `pydriller`/`PyGithub`
  # PyPI packages for repo cloning + commit walking. Do NOT scrape git objects manually.
  import requests, subprocess, time
  from pydriller import Repository  # pip: pydriller -- walks full commit history incl. file diffs

  LANGUAGES = ['Python','JavaScript','Java','Go','Ruby','C++']  # subset of Avelino et al.'s 6
  SAMPLE_PER_LANG = 40  # 6*40=240 candidate repos -- gradual scaling, see testing_plan

  candidates = []
  for lang in LANGUAGES:
      # GitHub search API: sort by stars, paginate to get popularity STRATA not just top-N
      # (avoids confounding survival analysis with "only mega-popular repos" bias)
      for page_bucket in ['stars:>5000','stars:500..5000','stars:50..500']:
          resp = github_search_repos(f'language:{lang} {page_bucket}', per_page=SAMPLE_PER_LANG//3)
          candidates += resp
      time.sleep(2)  # respect rate limit

  # === STAGE 1: filter mining artifacts (Avelino et al.'s exclusion criteria) ===
  filtered = []
  for repo in candidates:
      meta = get_repo_metadata(repo)
      if meta['age_days'] < 2*365: continue           # need >=2yr history (Avelino) -- we need 3yr (TFDD + 18mo)
      if meta['age_days'] < 3*365: continue            # our stricter requirement per assumptions
      if is_fork(meta) or is_archive_list(repo) or not has_code_files(repo): continue  # 'perils of mining GitHub'
      filtered.append(repo)

  # === STAGE 2: clone shallow-but-full-history, walk commits with PyDriller ===
  for repo in filtered:
      subprocess.run(['git','clone','--bare', repo['clone_url'], f'/tmp/repos/{repo["id"]}.git'], timeout=600)
      commits = []
      for c in Repository(f'/tmp/repos/{repo["id"]}.git').traverse_commits():
          commits.append({
              'hash': c.hash, 'author_email': resolve_alias(c.author.email),  # GitHub API email->account map
              'date': c.committer_date, 'files': [(m.new_path, m.added_lines, m.deleted_lines) for m in c.modified_files]
          })
      save_commits(repo['id'], commits)

  # === STAGE 3: DOA computation (Fritz et al. formula, as specified by Avelino ICPC 2016 / ESEM 2019) ===
  # DOA(dev, file, t) = 3.293 + 1.098*FA - 0.164*(AC^(1/2)) + 0.230*ln(1+DL)
  #   FA = 1 if dev is first author of file else 0
  #   AC = number of dev's changes to file up to time t
  #   DL = deletions dev made to file (churn) -- exact formula per paper; verify against ICPC2016 arXiv text
  # Compute DOA for EVERY (dev,file) pair using ONLY commits up to each yearly (or 6-month rolling) cutoff t.
  # A dev is 'primary owner'/core of a file at t if their DOA(dev,file,t) is the MAX among all devs who touched
  # that file AND DOA > threshold used by Avelino et al. (paper reports the exact cutoff, e.g. DOA>3.293 baseline).

  def compute_doa_snapshot(commits, cutoff_date):
      file_dev_stats = defaultdict(lambda: defaultdict(lambda: {'first_author': None, 'ac': 0, 'dl': 0}))
      for c in commits:
          if c['date'] > cutoff_date: continue
          for (path, added, deleted) in c['files']:
              s = file_dev_stats[path][c['author_email']]
              if s['first_author'] is None: s['first_author'] = c['author_email']
              s['ac'] += 1; s['dl'] += deleted
      doa = {}
      for path, devs in file_dev_stats.items():
          first_author = next(iter(devs))  # actual first author = earliest commit's author for that file
          for dev, s in devs.items():
              fa = 1 if dev == first_author else 0
              doa[(dev,path)] = 3.293 + 1.098*fa - 0.164*(s['ac']**0.5) + 0.230*log(1+s['dl'])
      return doa

  # Truck Factor set at t = greedy min set of devs whose removal drops 'coverage'
  # (files with an unambiguous owner) below 50% -- reuse Avelino et al.'s exact TF greedy algorithm.
  def truck_factor_set(doa_snapshot):
      file_owner = {}
      for (dev,path), score in doa_snapshot.items():
          if path not in file_owner or score > file_owner[path][1]:
              file_owner[path] = (dev, score)
      owned_files_per_dev = Counter(dev for dev,_ in file_owner.values())
      total_files = len(file_owner)
      tf_set, covered = [], 0
      for dev, n in owned_files_per_dev.most_common():
          tf_set.append(dev); covered += n
          if covered >= 0.5*total_files: break
      return tf_set

  # === STAGE 4: TFDD detection -- scan yearly snapshots chronologically ===
  for repo in filtered:
      commits = load_commits(repo['id'])
      yearly_dates = pd.date_range(repo['created_at'], repo['last_commit'], freq='365D')
      tf_history = [(d, truck_factor_set(compute_doa_snapshot(commits, d))) for d in yearly_dates]
      last_active = {dev: max(c['date'] for c in commits if c['author_email']==dev) for dev in all_devs}
      for i, (d, tf_set) in enumerate(tf_history):
          # TFDD: every dev in tf_set has been silent >= 1yr (validated threshold) as of d
          if tf_set and all((d - last_active[dev]).days >= 365 for dev in tf_set):
              if len(tf_set) == 1:  # FOUNDER-ONLY TFDD -- the subset this study targets
                  founder = tf_set[0]
                  tfdd_date = min(last_active[founder] + timedelta(365), d)
                  record_tfdd_event(repo['id'], founder, tfdd_date)
                  break  # first founder-only TFDD only, per investigation_approach step 2

  # === STAGE 5: pre-departure diffusion metrics (THE NEW MEASUREMENT) ===
  for event in tfdd_events:
      window_start = event.tfdd_date - timedelta(days=365)   # 12mo before
      window_end   = event.tfdd_date - timedelta(days=180)    # 6mo before
      window_commits = [c for c in commits if window_start <= c['date'] < window_end]
      founder_commits = sum(1 for c in window_commits if c['author_email']==event.founder)
      founder_share = founder_commits / max(1,len(window_commits))
      doa_at_window_end = compute_doa_snapshot(commits, window_end)
      file_owner = argmax_owner_per_file(doa_at_window_end)
      non_founder_owners = {dev for dev,path in file_owner.items() if dev != event.founder}
      event.founder_share = founder_share
      event.n_diffused_owners = len(non_founder_owners)
      # snapshot covariates AT TFDD for comparison to Avelino et al.'s d=0.13-0.26 result
      event.devs_at_tfdd, event.commits_at_tfdd, event.files_at_tfdd = snapshot_covariates(commits, event.tfdd_date)

  # === STAGE 6: survival label (Avelino et al. Active/Inactive model, 18mo window) ===
  for event in tfdd_events:
      post = [c for c in commits if event.tfdd_date <= c['date'] < event.tfdd_date+timedelta(days=548)]
      new_tf_devs = {c['author_email'] for c in post} - {event.founder}
      doa_post = compute_doa_snapshot(commits, event.tfdd_date+timedelta(days=548))
      recovered_tf = truck_factor_set(doa_post)
      event.survived = bool(recovered_tf) and any(d != event.founder for d in recovered_tf)
      event.grade = classify_thriving_maintained_dormant_dead(post, recovered_tf)

  # === STAGE 7: falsification / placebo check ===
  for event in tfdd_events:
      random_window = sample_random_window(event.repo, exclude=near_tfdd)
      event.placebo_founder_share, event.placebo_n_diffused = compute_window_metrics(random_window)

  # === STAGE 8: matched pairs + regression ===
  buckets = bucket_by(stars=log_deciles, forks=log_deciles, n_contributors=log_deciles, language=exact)
  matched_pairs = []
  for bucket, events in groupby(tfdd_events, buckets):
      lo = [e for e in events if e.founder_share < 0.50 and e.n_diffused_owners >= 2]
      hi = [e for e in events if e.founder_share >= 0.80]
      matched_pairs += greedy_nearest_neighbor_match(lo, hi, on=['stars','forks','n_contributors'])

  risk_ratio, ci95 = bootstrap_survival_rate_ratio(matched_pairs, n_boot=5000)

  import statsmodels.api as sm
  X = df[['founder_share','n_diffused_owners','log_stars','log_forks','n_contributors','language_dummies','license_dummies']]
  model = sm.Logit(df['survived'], sm.add_constant(X)).fit()
  pvals_bh = benjamini_hochberg(model.pvalues)
  std_effect_sizes = standardized_coefs(model, X)  # compare vs Avelino et al. d=0.13(files)/0.25-0.26(devs,commits)

  # placebo comparison: refit model with placebo_founder_share / placebo_n_diffused instead
  placebo_model = sm.Logit(df['survived'], sm.add_constant(df[['placebo_founder_share','placebo_n_diffused', ...]])).fit()

  # === STAGE 9: write method_out.json ===
  results = {
    'n_repos_sampled': ..., 'n_founder_tfdd_events': ..., 'unconditioned_survival_rate': ...,  # vs Avelino 41%
    'matched_pair_risk_ratio': risk_ratio, 'ci95': ci95,
    'regression_coefs': model.params.to_dict(), 'pvals_bh': pvals_bh, 'std_effect_sizes': std_effect_sizes,
    'placebo_coefs': placebo_model.params.to_dict(),
    'snapshot_covariate_effect_sizes_d': cohens_d(devs_at_tfdd, commits_at_tfdd, files_at_tfdd, by=survived),
    'per_event_records': [...]  # full row-level table for downstream paper artifact
  }
  json.dump(results, open('method_out.json','w'), indent=2)
fallback_plan: |-
  Primary risk is DATA VOLUME/TIME, not algorithmic novelty -- the DOA/TF pipeline is fully specified in Avelino et al. and Fritz et al., so implement it exactly rather than approximate it. Layered fallbacks, in order:
  1. If GitHub API rate limits (60/hr unauthenticated, 5000/hr with a token) block reaching ~240 candidate repos within the 6h budget, drop SAMPLE_PER_LANG to 15-20 and/or restrict to 3 languages (Python, JavaScript, Go) -- still enough for matched pairs if founder-only TFDDs are ~16%*66%=~10% of repos (Avelino et al.'s own rates), i.e. expect ~10-25 usable events from 150-240 repos; if fewer than ~15 founder-TFDD events are found, RELAX the founder-only TF=1 requirement's downstream matched-pair bucket granularity (fewer bucket dimensions: drop 'license' from matching, keep only stars+language) rather than abandoning the matched-pairs design, and report the regression as the primary result with matched-pairs as a secondary/exploratory check, clearly labeled with the reduced n.
  2. If `git clone --bare` of large repos (e.g. large C++ projects) times out or exceeds disk, use `git clone --bare --filter=blob:none` (partial clone, still gives full commit/path history which is all DOA needs) or cap repo size by GitHub API `size` field before selection (exclude repos >500MB).
  3. If PyDriller is too slow walking full history for large repos (some real repos have 50k+ commits), fall back to raw `git log --numstat --format='%H|%ae|%cI'` parsed manually via subprocess -- much faster, same information needed (author, date, per-file added/deleted lines).
  4. If GitHub's search API cannot cleanly stratify by popularity bucket (search API caps at 1000 results per query), issue multiple queries partitioning by star-count ranges as already planned in Stage 0 -- this is the mitigation, not a fallback trigger.
  5. If DOA-based TFDD detection finds zero or very few founder-only (TF=1) TFDD events after scanning all sampled repos (possible if the sample skews toward large multi-founder projects), explicitly RELAX the founder-only definition to 'founder retained TF-set membership until departure, TF-set size <=2 at detachment' and report both the strict (TF=1) and relaxed (TF<=2) results separately -- do not silently substitute one for the other.
  6. If the 18-month post-TFDD survival window right-censors too many events (repo's total history <3yr from birth to TFDD+18mo), drop those events from the labeled set but KEEP them in a separate 'right-censored, excluded' count reported in method_out.json for transparency -- do not impute or guess their outcome.
  7. If statsmodels' logistic regression fails to converge (e.g., quasi-separation with a small n and multiple dummy variables), reduce covariates to a parsimonious set (founder_share, n_diffused_owners, log_stars, log_n_contributors only, dropping language/license dummies or collapsing them to 2-3 groups) and report this explicitly as a deviation from the full model in success_criteria point 2.
  8. If time runs out before the full logistic + BH correction can be fit, still produce and save: (a) the founder-only TFDD event table with all raw metrics, (b) the unconditioned survival rate for direct Avelino-et-al comparability, and (c) a simple two-group t-test/Mann-Whitney comparison of founder_share and n_diffused_owners between survivors and non-survivors -- a minimally complete result beats an unfinished full regression.
testing_plan: |-
  Gradual scaling per aii-long-running-tasks pattern -- validate correctness on a tiny, fully-inspectable slice before scaling to the full sample:
  1. MINI TEST (5 repos, hand-picked, ~15 min of runtime budget): pick 5 well-known repos with KNOWN founder-departure histories the executor can sanity-check by eye (e.g. a small abandoned utility library where a single early README/commit-log inspection confirms one dominant early committer who later went silent). Clone, run DOA computation for just 2-3 yearly snapshots, and MANUALLY verify: (a) the computed first-author-per-file matches `git log --diff-filter=A --follow -- <file>` for a handful of spot-checked files, (b) the DOA formula output is a plausible positive number in the same range as Fritz et al.'s reported examples, (c) the greedy TF-set algorithm on this tiny repo returns a sensible minimal set (e.g. TF=1 for a single-maintainer repo). This catches formula transcription errors and alias-resolution bugs before they propagate.
  2. PIPELINE-SHAPE TEST (10-15 repos): run the FULL pipeline (Stages 0-9) end-to-end on a small sample to confirm every stage produces non-degenerate output -- specifically check: TFDD detection finds at least 1-2 founder-only events (not zero, which would indicate a bug in the 1-year-silence or TF=1 logic), pre-departure metrics are in [0,1] for founder_share and non-negative integers for n_diffused_owners, and survival labels split into both True and False (not all-one-class, which would break the regression). If TFDD events = 0 at this scale, debug the silence-threshold and TF-set logic before scaling up -- do not proceed to full sampling with an undetected bug.
  3. CROSS-CHECK AGAINST AVELINO ET AL.'S PUBLISHED NUMBERS: on whatever founder-only TFDD events are found in the eventual full run, report the UNCONDITIONED survival rate and sanity-check it is in a plausible neighborhood of their reported 41% (not required to match exactly -- different sample -- but a wildly different rate, e.g. 95% or 2%, signals a bug in survival labeling, most likely the Active/Inactive recovery criterion being mis-implemented as 'any commit at all' rather than 'a new TF developer attracted').
  4. SCALE UP in 2-3 steps (e.g. 15 -> 80 -> 240 repos) per the gradual-scaling pattern, checking wall-clock time and GitHub API quota consumption at each step before committing to the next, and stopping early (documenting n achieved) if the 6h budget is at risk -- prioritize finishing Stages 1-9 on a smaller-than-planned sample over running out of time mid-clone.
  5. FINAL VALIDATION: before writing method_out.json, confirm (a) no NaN/inf in the regression design matrix, (b) the BH correction is applied to the RIGHT set of p-values (the diffusion predictors, not all covariates indiscriminately, per success_criteria point 2), (c) the placebo/shuffle check (Stage 7) was actually run on a comparable number of events to the main analysis, not skipped.
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

### [16] HUMAN-USER prompt · 2026-08-21 19:01:31 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [17] SKILL-INPUT — aii-long-running-tasks · 2026-08-21 19:02:37 UTC

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

### [18] SYSTEM-USER prompt · 2026-08-21 19:03:35 UTC

```
<task-notification>
<task-id>bbwc7f4se</task-id>
<summary>Monitor event: "watch method.py progress or completion/crash"</summary>
<event>==&gt; logs/run.log &lt;==
2026-08-21 19:03:33.484 | INFO     | __main__:main:640 - === STAGE 0-1: sampling and filtering candidate repos ===
2026-08-21 19:03:33.492 | INFO     | __main__:stage0_sample_repos:128 - [stage0] search: language:Python stars:50..500 archived:false
==&gt; logs/stdout.log &lt;==
19:03:33|INFO   |=== STAGE 0-1: sampling and filtering candidate repos ===
19:03:33|INFO   |[stage0] search: language:Python stars:50..500 archived:false</event>
</task-notification>
```

### [19] SYSTEM-USER prompt · 2026-08-21 19:04:02 UTC

```
<task-notification>
<task-id>bbwc7f4se</task-id>
<summary>Monitor event: "watch method.py progress or completion/crash"</summary>
<event>==&gt; logs/run.log &lt;==
2026-08-21 19:03:58.017 | INFO     | __main__:stage0_sample_repos:128 - [stage0] search: language:Go stars:500..5000 archived:false
==&gt; logs/stdout.log &lt;==
19:03:58|INFO   |[stage0] search: language:Go stars:500..5000 archived:false</event>
</task-notification>
```

### [20] SYSTEM-USER prompt · 2026-08-21 19:04:02 UTC

```
<task-notification>
<task-id>bbwc7f4se</task-id>
<summary>Monitor event: "watch method.py progress or completion/crash"</summary>
<event>==&gt; logs/run.log &lt;==
2026-08-21 19:04:01.537 | INFO     | __main__:stage0_sample_repos:128 - [stage0] search: language:Go stars:5000..100000 archived:false
==&gt; logs/stdout.log &lt;==
19:04:01|INFO   |[stage0] search: language:Go stars:5000..100000 archived:false</event>
</task-notification>
```

### [21] SYSTEM-USER prompt · 2026-08-21 19:04:29 UTC

```
<validation-feedback>
Attempt 2 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [22] SYSTEM-USER prompt · 2026-08-21 19:04:45 UTC

```
<validation-feedback>
Attempt 3 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```
