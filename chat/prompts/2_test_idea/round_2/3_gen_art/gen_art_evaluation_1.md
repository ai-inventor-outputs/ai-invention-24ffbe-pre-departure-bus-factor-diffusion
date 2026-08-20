# gen_art_evaluation_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `run_5SMkWpWKNLxk` — Measuring Authority Diffusion Before Founders Leave Open Source Projects
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_evaluation_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-08-20 20:11:06 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/file.py`, `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_evaluation_1_idx3
type: evaluation
title: Closing the Rigor Gaps in the Diffusion Pipeline
summary: >-
  Extends the prior eval.py against the DATASET (art_ZuMis522AEPF) and EXPERIMENT (art_I5KoOp16hub5) artifacts to close five
  reviewer-named gaps without collecting new repos or building new methods: (1) fully disclose the permutation scheme used
  for the placebo/window-shuffle check and re-run it at a larger budget to show p-value stability; (2) compute a Wilson 95%
  CI for Avelino et al.'s reported 66% TF=1 statistic (n=315) and report it side-by-side with this study's own CI instead
  of asserting 'overlap' informally; (3) manually spot-check the alias-resolution diagnostic against live GitHub contributor
  pages for 2-3 corpus repos via aii-web-tools; (4) emit an exact, full repository table (name, language, stars, history length,
  TFDD/survival status) matching the dataset artifact's real output for use as a paper table; (5) explicitly quantify and
  narrate the survivorship-bias direction/magnitude versus Avelino et al.'s published rates, and (since no expanded/non-conditioned
  corpus exists among the dependencies) formally document that the design-flaw-not-power-problem claim rests on structural
  argument plus the existing single-frame evidence, not on a second frame -- reporting this as a residual limitation rather
  than silently treating the comparison as already done.
runpod_compute_profile: gpu
metrics_descriptions: |-
  All computations run in a new eval.py inside this artifact's workspace, loading full_method_out.json from the EXPERIMENT dependency (art_I5KoOp16hub5) and full_data_out.json from the DATASET dependency (art_ZuMis522AEPF) by their absolute dependency workspace_path files -- do not re-derive data, only re-analyze what those artifacts already produced (recompute the placebo/permutation test at higher budget using the EXPERIMENT's own method.py functions/logic where feasible, since that is legitimate re-analysis, not new data collection).

  (A) PERMUTATION-SCHEME DISCLOSURE + CONVERGENCE. From method_out.json's placebo/window-shuffle block (500 iterations reported in the EXPERIMENT summary) and the underlying per-repo history-length metadata in full_data_out.json, compute for EACH of the n_founder_tfdd_events=6 founder-only-TFDD repos: the number of feasible distinct 6-12-month relocatable windows given that repo's total history length in months (e.g. a repo with H months of usable history and a 6-month window has roughly H-6 distinct start-month positions, so state this arithmetic explicitly per repo and sum/report the combinatorial space size). State explicitly whether the reported 500 (or the original run's cited '60/40') shuffle draws were i.i.d. samples WITH or WITHOUT replacement from that space (read this from method.py's actual placebo-generation code, do not assume) and whether the same random seed reused across strata induces any dependence between the survivor and non-survivor shuffle sets. Derive the theoretical minimum achievable two-sided p-value given the placebo sample count k as 1/(k+1) (standard permutation-test resolution bound), and report it next to the actually-computed p-value so a reader can judge whether the reported p-value is bounded away from that floor or sitting on it (a p-value equal to the floor value is a red flag that more permutations are needed, not evidence of significance). Then RE-RUN the placebo test at a substantially larger budget -- target 2000 iterations per stratum if the small n=6 event corpus and its capped/cached DOA recomputation make this fast (state the actual wall-clock observed; if 2000 is infeasible within the time budget, fall back to the largest budget achieved within roughly 20 minutes of compute and report exactly what budget that was and why, rather than silently using fewer). Report the placebo p-value (and effect-size null-distribution mean/SD) at each of at least 3 budgets (e.g. original ~60/40, an intermediate step, and the final larger budget) in a convergence table, and state explicitly whether the qualitative conclusion (effect specific to the true pre-departure window vs. not) is stable across budgets or flips.

  (B) AVELINO ET AL. 66% TF=1 WILSON CI. Using n=315 (Avelino et al.'s reported total TFDD count) and the reported proportion 0.66 (208 of 315, computing the exact count as round(0.66*315) and stating that rounding explicitly since the paper does not give the raw numerator), compute a Wilson score 95% CI (not the normal-approximation Wald interval, which is unreliable near 0/1 and for the moderate n here -- use the standard Wilson formula: center = (phat + z^2/(2n)) / (1 + z^2/n), halfwidth = z*sqrt(phat*(1-phat)/n + z^2/(4n^2)) / (1 + z^2/n), z=1.959964 for 95%). Compute the SAME Wilson CI for this study's own TF=1 founder-TFDD fraction using this study's own n (the count of ALL TFDD events found in the 15-repo corpus, not just the founder-only subset of 6 -- pull both numbers from method_out.json's diagnostic fields) and report both CIs side by side in a small table with an explicit overlap/non-overlap determination (do not just eyeball it -- state the numeric bounds of both intervals and whether they intersect). Given the small denominator on this study's side, explicitly flag if the interval is very wide and caution against over-reading 'overlap' as validation when this study's own CI could contain almost any plausible fraction.

  (C) ALIAS-RESOLUTION SPOT-CHECK. Select 2-3 of the 15 corpus repos (prefer ones with the highest reported alias-collapse-rate variance or the ones contributing founder-only TFDD events, since those drive the headline numbers) and for each: use the aii-web-tools skill's web fetch/fetch_grep to pull the live GitHub repo's /graphs/contributors page or the repo's README/CONTRIBUTORS file and its top-committer list, and cross-reference the distinct author emails/logins the EXPERIMENT pipeline counted as 'distinct non-founder DOA file-owners' against what GitHub's own UI presents as distinct human contributors. Explicitly look for: (i) bot accounts (e.g. dependabot, github-actions[bot]) miscounted as human authority-holders, (ii) the same human appearing under 2+ emails/handles that the pipeline's alias-resolution did NOT merge (under-merging, which would inflate the diffusion score), and (iii) the reverse -- two distinct humans merged into one identity (over-merging, which would deflate it). Report per-repo: number of identities checked, number found to be bots, number found to be split identities of the same human, and whether correcting these would change that repo's founder-only-TFDD classification or diffusion score materially. State clearly this is a spot-check on 2-3 repos, not a full audit, and describe what fraction of the corpus this leaves unchecked.

  (D) FULL REPOSITORY TABLE. Parse full_data_out.json's per-repo records (one example per repo under the github_founder_departure_commits group) and full_method_out.json's per-repo TFDD/survival outputs, and emit ONE row per repo (all repos present in the dataset artifact, whatever the final count is -- verify it is 15 by counting live records rather than assuming the number from the dependency summary) with columns: repo full_name, primary language, stars, forks, total commit-history span in years, whether a TFDD was detected, whether it was founder-only (TF=1 at detachment), the pre-departure diffusion score (founder commit-share, distinct non-founder DOA-owner count) if applicable, and the 18-month post-TFDD survival grade (thriving/maintained/dormant/dead) if applicable. Cross-check every field against the two source JSON files exactly (no invented or rounded-from-memory values) and flag any repo where a field is missing/null in the source data rather than silently omitting the row.

  (E) SURVIVORSHIP-BIAS QUANTIFICATION AND DESIGN-FLAW ARGUMENT. Recompute directly from the EXPERIMENT/DATASET outputs: this corpus's TFDD incidence rate (TFDDs / total usable repos) and 18-month survival rate among TFDD repos, and place them next to Avelino et al.'s published 16.3% incidence and 40.6% survival (cite the exact source numbers/section from the ESEM 2019 paper via a fresh aii-web-tools fetch_grep against the arXiv PDF, do not rely on memory of the hypothesis text) with a formal statistical comparison (a two-proportion z-test or exact binomial test against Avelino et al.'s rate treated as the null, reporting the test statistic, p-value, and a plain-language direction/magnitude statement, e.g. 'this corpus's TFDD-survival rate is X percentage points higher, z=..., p=...'). Since no expanded or non-conditioned corpus exists among this artifact's dependencies (the DATASET artifact's ~104-repo candidate pipeline was checkpointed but not completed, and the artifact direction's re-run-on-expanded-corpus step is therefore not executable from the given dependencies), do NOT fabricate or simulate a second corpus -- instead write an explicit 'Residual Limitation' section documenting: the structural argument for why conditioning on present-day liveness necessarily biases toward survivors (a short formal statement: any sampling frame requiring a repo to be 'currently famous and still maintained' assigns zero sampling probability to the non-survivor stratum this study needs to observe fully, so incidence/survival estimates from it are not just imprecise but inconsistent estimators of the population quantities), the fact that this study's own evidence is 15 out of a 104-repo candidate list with the remainder blocked by the unauthenticated 60-req/hour GitHub API cap (quote the exact numbers from the DATASET artifact's summary), and a concrete, falsifiable prediction of what a valid non-conditioned corpus run through the same pipeline should show (e.g. 'incidence should approach Avelino et al.'s 16.3% and survival should approach 40.6% within the CI computed in part B') so a future GEN_DATASET/GEN_EXPERIMENT artifact with GITHUB_TOKEN access has a stated, checkable target rather than a vague aspiration.

  All five parts write into a single eval_out.json (plus mini/preview variants per aii-json skill conventions) with clearly named top-level keys per part (permutation_disclosure, tf1_ci_comparison, alias_spotcheck, repo_table, survivorship_bias_quantification) and a top-level overall_verdict summarizing, in 3-5 sentences, which reviewer gaps are now fully closed with data (A, B, D, E's quantification half) versus which remain structurally open pending a new corpus (E's second-frame comparison, explicitly NOT run here). Validate the final JSON against the eval_out schema via the aii-json skill before finishing, and check output file sizes against the aii-file-size-limit skill.
metrics_justification: >-
  These five checks target exactly the methodology-rigor gaps a careful reviewer would flag on the prior 15-repo pipeline
  result, and each closes a specific, nameable threat to validity rather than adding generic robustness noise: (A) a permutation
  p-value reported without its achievable resolution (1/(k+1)) or its sampling scheme (with/without replacement, dependence
  across strata) is uninterpretable -- a p-value of 0.025 from 40 draws is at the theoretical floor and means something different
  from the same number at 2000 draws, so disclosing the scheme and showing budget-convergence is the minimum bar for trusting
  the placebo/window-shuffle result that underlies the paper's construct-validity claim. (B) A bare 'our TF=1 rate looks similar
  to their 66%' claim without confidence intervals on BOTH sides is not a comparison at all, especially with this study's
  tiny n; the Wilson interval (rather than the Wald normal approximation) is the standard correct choice for a proportion
  with a moderate-to-small denominator and one anchored near neither 0 nor 1, and reporting both intervals turns an assertion
  into a falsifiable statistical statement. (C) The diffusion measurement's core claim (distinct non-founder DOA owners) is
  only as good as identity resolution; since the EXPERIMENT reported a suspicious 0.0-median alias-collapse-rate, a live spot-check
  against GitHub's actual contributor graph is the cheapest available external validity check on whether that diffusion count
  is inflated by bots or under-merged identities -- exactly the kind of concrete, checkable evidence a reviewer would ask
  for instead of trusting an internal QA metric produced by the same pipeline being validated. (D) An exact, complete repository
  table is table-stakes for reproducibility and lets a reader (or downstream paper-writing step) verify every headline number
  against raw per-repo facts rather than trusting aggregate statistics alone -- it also surfaces silently-dropped or null-field
  repos that aggregate summaries can hide. (E) The hypothesis's central claim is that the 15-repo corpus's deviation from
  Avelino et al.'s published rates is a SAMPLING-FRAME defect, not a power shortfall; formalizing that as a statistical test
  against the published null (rather than an eyeballed 53.3% vs 16.3% comparison) plus an explicit, honestly-scoped limitations
  statement about what remains unverified (since no second, non-conditioned corpus exists to run head-to-head) is what turns
  a plausible narrative into a defensible, appropriately-hedged scientific claim -- and prevents the paper from either overclaiming
  a resolved comparison or understating how much of the design-flaw argument is currently structural reasoning versus direct
  empirical contrast.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_ZuMis522AEPF
type: dataset
title: GitHub Founder-Departure Commit Corpus
summary: >-
  Built a real corpus of 15 well-known, well-documented open-source GitHub repositories (e.g. pallets/flask, BurntSushi/ripgrep,
  psf/black, Textualize/rich, httpie/cli, pyenv/pyenv, tiangolo/typer), each with full commit history obtained via `git clone`
  + `git log --numstat` (SHA, author name/email, ISO date, per-file insertions/deletions for every commit, newest-first, capped
  at 5,000 commits/repo with an explicit truncation flag) plus repo-level metadata from the GitHub REST API (stars, forks,
  primary language, license, created_at, pushed_at, open_issues, README excerpt). Each repo record also carries an empirically-computed
  `founder_signal`: the fraction of commits in the repo's first 365 days made by its single top-committing author email, and
  the top author's email. This directly operationalizes the plan's inclusion criterion (single-founder dominance >=70% of
  year-1 commits) without asserting it a priori -- it is measured from the real cloned git log. Repos span multiple languages
  (Python, Rust) and star bands (15k-72k stars in the current sample) and multi-year histories (6.6-16.4 years), giving enough
  post-founding history for an 18-month post-departure survival window. IMPORTANT SCOPE LIMITATION: this environment has no
  GITHUB_TOKEN, so the GitHub REST API is capped at 60 unauthenticated requests/hour (2 calls per repo: /repos/{full_name}
  and its /readme). This makes the plan's 150-250 repo target infeasible within the artifact time budget -- 15 repos were
  completed and checkpointed (12 in the final checkpoint snapshot, 15 repo-record files on disk) before the artifact needed
  to finalize; git clone itself (smart-HTTP) is NOT rate-limited, so every completed repo's commit history is complete and
  untruncated for its cap, only the TOTAL repo count is reduced. code/build_dataset.py and code/candidates.py contain a ~104-repo
  candidate list spanning Python/JS/Go/Ruby/Rust/C++/Java and a checkpointed, resumable pipeline (temp/checkpoint.json) that
  a downstream step can re-run with a GITHUB_TOKEN (raising the limit to 5,000 req/hour) to scale to the full 150-250 target
  without re-doing completed work. A HuggingFace candidate (kamalkishor1991/commit-messages-dataset, sampled commit diffs
  for commit-message generation) was evaluated and explicitly rejected as the primary source because it lacks per-repo lifecycle,
  author-identity-over-time, and per-file structure. data.py standardizes the corpus into the exp_sel_data_out.json schema:
  one dataset group `github_founder_departure_commits`, one example per repo, `input` = JSON-encoded {repo_metadata, founder_signal,
  truncated, commit_cap, commits[]}, `output` = derived label 'founder_dominant'/'not_founder_dominant' from the 0.7 year-1-share
  threshold, plus flat `metadata_*` fields (full_name, stars, language, history_years, n_commits, truncated, year1_top_author_share,
  task_type). Validated against the exp_sel_data_out schema (PASSED); full_data_out.json is 13.8MB (well under the 100MB limit),
  with mini_data_out.json and preview_data_out.json also produced.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
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

--- Dependency 2 ---
id: art_I5KoOp16hub5
type: experiment
title: Does authority spreading before founders leave keep projects alive?
summary: >-
  Reimplemented Avelino et al.'s (ESEM 2019) Degree-of-Authorship / Truck-Factor / Truck-Factor-Detachment-Departure (TFDD)
  pipeline end-to-end in method.py, run against the DATASET dependency's mined GitHub commit histories (15 usable repos with
  full per-file commit logs, out of 3427 raw records also containing an unrelated HuggingFace commit-message corpus that the
  loader correctly skips via a 'no_commits' filter). For each repo the pipeline: (1) resolves author aliases via normalized
  email/github-login matching and logs a per-repo alias-collapse-rate QA metric; (2) computes yearly cumulative-window DOA
  (Degree of Authorship) per file per author using Fritz et al.'s weights (FA=3.293, DL=1.098, AC=-1.017) as used by Avelino
  et al.; (3) derives the yearly greedy Truck-Factor set from primary DOA ownership; (4) detects Truck-Factor-Detachment-Departure
  events (a TF-set fully silent for 12 months) and isolates founder-only TFDDs (TF=1 and the sole departing developer is the
  repo's first human committer, with bulk-import first commits filtered per the Kalliamvakou et al. 2014 'perils of mining
  GitHub' heuristic of >80% of files touched within the first week); (5) computes a NEW pre-departure authority-diffusion
  trajectory over the 6-12 months before each TFDD -- founder commit-share and count of distinct non-founder DOA file-owners
  -- alongside Avelino et al.'s original at-TFDD snapshot covariates (developers/commits/files at detachment); (6) classifies
  18-month post-TFDD survival into Avelino's four-level active/inactive grades (thriving/maintained/dormant/dead) plus a binary
  survived flag; (7) runs a matched-pairs bootstrap comparison (nearest-neighbor matching on standardized log-stars/log-forks/log-contributors
  within language, comparing high- vs low-diffusion projects) with 10,000-resample 95% CIs; (8) fits BH-corrected logistic
  and ordinal (statsmodels OrderedModel) regressions of survival on diffusion predictors plus snapshot covariates, reporting
  standardized effect sizes comparable to Avelino et al.'s reported d=0.13 (files) / 0.25-0.26 (developers, commits); (9)
  runs a 500-iteration placebo/window-shuffle check that redraws the pre-departure window from elsewhere in project history
  and refits the regression, to test whether the true diffusion-window effect exceeds the null distribution of effects from
  arbitrary windows. All steps implement both the proposed authority-diffusion predictor AND Avelino et al.'s original snapshot-covariate
  baseline side-by-side in the same regression and matched-pairs machinery, so the two are directly comparable under identical
  data and identical statistical procedures -- baseline_predict and ourmethod_predict columns are both emitted per example.
  The run found n_repos_total=3427 raw dataset records (3409 filtered as non-repo commit-message rows lacking file-level structure;
  the dataset dependency's GitHub API rate limiting -- 60 unauthenticated requests/hour -- constrained the usable repo count
  to 15, well below the plan's 150-250 target), yielding n_founder_tfdd_events=6, which falls below the ~40 events the plan's
  own fallback_plan identifies as needed for a well-powered matched-pairs test; per that fallback plan this limitation is
  reported explicitly in the output metadata (extended_sample_used_TFle2 flag, doa_approximation_used flag, alias_qa block)
  rather than silently presented as adequately powered, and all regression/matched-pairs/placebo numbers in method_out.json
  should be read as a small-n pilot demonstrating the pipeline mechanics rather than a well-powered test of the founder-diffusion-predicts-survival
  hypothesis. A bug where the dataset dependency's example-wrapper format (repo records JSON-encoded inside an 'input' string
  field, per the exp_gen_sol_out schema) was not being unwrapped -- causing every repo to be misread as having zero commits
  -- was found and fixed during this run; the corrected loader now parses that wrapper and the pipeline runs end-to-end in
  ~90 seconds. Output method_out.json / full_method_out.json / mini_method_out.json / preview_method_out.json validate cleanly
  against the exp_gen_sol_out.json schema (0 errors) and are all under 9KB, far below the 100MB size limit. Downstream users
  (GEN_PAPER_TEXT) should present this as a methodology-validation / small-sample pilot result: the pipeline itself (DOA/TF/TFDD
  replication, diffusion-trajectory measurement, survival classification, matched-pairs + regression + placebo statistical
  machinery) is fully implemented and tested (smoke tests on synthetic hand-constructed repos, mini-run sanity checks, and
  the full corpus run all pass), but the headline finding is data-starved (n=6 events) due to upstream GitHub API rate limiting
  documented in the DATASET dependency's own metadata, not a pipeline defect.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
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
TODO 2. Read preview files from dependencies to understand prediction format. Evaluate ALL experiments provided — do not skip or select a subset. Avoid re-training or re-executing the method unless absolutely necessary; prefer loading predictions from each dependency's method_out.json / predict_* fields. Read domain handbook if applicable (see <available_domain_handbooks>). Decide evaluation metrics based on artifact plan. Test basic functionality with 'uv run'.
TODO 3. Fully implement evaluation as described in artifact plan in './eval.py'. Use exp_eval_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant metrics or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
```

### [2] HUMAN-USER prompt · 2026-08-20 20:11:06 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-python · 2026-08-20 20:11:10 UTC

The agent loaded the **aii-python** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-python
description: Python coding standards for experiment and evaluation scripts. Covers environment setup, logging, error handling, and code structure.
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

### [4] SKILL-INPUT — aii-web-tools · 2026-08-20 20:12:36 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Web research toolkit: free-first web search (general or scholarly, Serper fallback), web page fetch as markdown (HTML and PDF), and regex grep over full page/PDF text. Use whenever a task needs to search the web, read a page, mine a paper/PDF, verify citations, or extract exact quotes, numbers, or methodology from a URL."
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

### [5] SKILL-INPUT — aii-json · 2026-08-20 20:12:36 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: JSON validation and formatting toolkit. Validate JSON files against schemas for experiment pipelines, and generate full/mini/preview versions of JSON datasets. Use for validating pipeline outputs, checking schema compliance, or creating size-optimized JSON variants.
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

### [6] SKILL-INPUT — aii-file-size-limit · 2026-08-20 20:12:36 UTC

The agent loaded the **aii-file-size-limit** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

```
---
name: aii-file-size-limit
description: File size check procedure for splitting oversized output files. Use after generating JSON output files to check and split files exceeding the provided size limit.
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

### [7] SYSTEM-USER prompt · 2026-08-20 20:19:40 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/file.py`, `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_evaluation_1_idx3
type: evaluation
title: Closing the Rigor Gaps in the Diffusion Pipeline
summary: >-
  Extends the prior eval.py against the DATASET (art_ZuMis522AEPF) and EXPERIMENT (art_I5KoOp16hub5) artifacts to close five
  reviewer-named gaps without collecting new repos or building new methods: (1) fully disclose the permutation scheme used
  for the placebo/window-shuffle check and re-run it at a larger budget to show p-value stability; (2) compute a Wilson 95%
  CI for Avelino et al.'s reported 66% TF=1 statistic (n=315) and report it side-by-side with this study's own CI instead
  of asserting 'overlap' informally; (3) manually spot-check the alias-resolution diagnostic against live GitHub contributor
  pages for 2-3 corpus repos via aii-web-tools; (4) emit an exact, full repository table (name, language, stars, history length,
  TFDD/survival status) matching the dataset artifact's real output for use as a paper table; (5) explicitly quantify and
  narrate the survivorship-bias direction/magnitude versus Avelino et al.'s published rates, and (since no expanded/non-conditioned
  corpus exists among the dependencies) formally document that the design-flaw-not-power-problem claim rests on structural
  argument plus the existing single-frame evidence, not on a second frame -- reporting this as a residual limitation rather
  than silently treating the comparison as already done.
runpod_compute_profile: gpu
metrics_descriptions: |-
  All computations run in a new eval.py inside this artifact's workspace, loading full_method_out.json from the EXPERIMENT dependency (art_I5KoOp16hub5) and full_data_out.json from the DATASET dependency (art_ZuMis522AEPF) by their absolute dependency workspace_path files -- do not re-derive data, only re-analyze what those artifacts already produced (recompute the placebo/permutation test at higher budget using the EXPERIMENT's own method.py functions/logic where feasible, since that is legitimate re-analysis, not new data collection).

  (A) PERMUTATION-SCHEME DISCLOSURE + CONVERGENCE. From method_out.json's placebo/window-shuffle block (500 iterations reported in the EXPERIMENT summary) and the underlying per-repo history-length metadata in full_data_out.json, compute for EACH of the n_founder_tfdd_events=6 founder-only-TFDD repos: the number of feasible distinct 6-12-month relocatable windows given that repo's total history length in months (e.g. a repo with H months of usable history and a 6-month window has roughly H-6 distinct start-month positions, so state this arithmetic explicitly per repo and sum/report the combinatorial space size). State explicitly whether the reported 500 (or the original run's cited '60/40') shuffle draws were i.i.d. samples WITH or WITHOUT replacement from that space (read this from method.py's actual placebo-generation code, do not assume) and whether the same random seed reused across strata induces any dependence between the survivor and non-survivor shuffle sets. Derive the theoretical minimum achievable two-sided p-value given the placebo sample count k as 1/(k+1) (standard permutation-test resolution bound), and report it next to the actually-computed p-value so a reader can judge whether the reported p-value is bounded away from that floor or sitting on it (a p-value equal to the floor value is a red flag that more permutations are needed, not evidence of significance). Then RE-RUN the placebo test at a substantially larger budget -- target 2000 iterations per stratum if the small n=6 event corpus and its capped/cached DOA recomputation make this fast (state the actual wall-clock observed; if 2000 is infeasible within the time budget, fall back to the largest budget achieved within roughly 20 minutes of compute and report exactly what budget that was and why, rather than silently using fewer). Report the placebo p-value (and effect-size null-distribution mean/SD) at each of at least 3 budgets (e.g. original ~60/40, an intermediate step, and the final larger budget) in a convergence table, and state explicitly whether the qualitative conclusion (effect specific to the true pre-departure window vs. not) is stable across budgets or flips.

  (B) AVELINO ET AL. 66% TF=1 WILSON CI. Using n=315 (Avelino et al.'s reported total TFDD count) and the reported proportion 0.66 (208 of 315, computing the exact count as round(0.66*315) and stating that rounding explicitly since the paper does not give the raw numerator), compute a Wilson score 95% CI (not the normal-approximation Wald interval, which is unreliable near 0/1 and for the moderate n here -- use the standard Wilson formula: center = (phat + z^2/(2n)) / (1 + z^2/n), halfwidth = z*sqrt(phat*(1-phat)/n + z^2/(4n^2)) / (1 + z^2/n), z=1.959964 for 95%). Compute the SAME Wilson CI for this study's own TF=1 founder-TFDD fraction using this study's own n (the count of ALL TFDD events found in the 15-repo corpus, not just the founder-only subset of 6 -- pull both numbers from method_out.json's diagnostic fields) and report both CIs side by side in a small table with an explicit overlap/non-overlap determination (do not just eyeball it -- state the numeric bounds of both intervals and whether they intersect). Given the small denominator on this study's side, explicitly flag if the interval is very wide and caution against over-reading 'overlap' as validation when this study's own CI could contain almost any plausible fraction.

  (C) ALIAS-RESOLUTION SPOT-CHECK. Select 2-3 of the 15 corpus repos (prefer ones with the highest reported alias-collapse-rate variance or the ones contributing founder-only TFDD events, since those drive the headline numbers) and for each: use the aii-web-tools skill's web fetch/fetch_grep to pull the live GitHub repo's /graphs/contributors page or the repo's README/CONTRIBUTORS file and its top-committer list, and cross-reference the distinct author emails/logins the EXPERIMENT pipeline counted as 'distinct non-founder DOA file-owners' against what GitHub's own UI presents as distinct human contributors. Explicitly look for: (i) bot accounts (e.g. dependabot, github-actions[bot]) miscounted as human authority-holders, (ii) the same human appearing under 2+ emails/handles that the pipeline's alias-resolution did NOT merge (under-merging, which would inflate the diffusion score), and (iii) the reverse -- two distinct humans merged into one identity (over-merging, which would deflate it). Report per-repo: number of identities checked, number found to be bots, number found to be split identities of the same human, and whether correcting these would change that repo's founder-only-TFDD classification or diffusion score materially. State clearly this is a spot-check on 2-3 repos, not a full audit, and describe what fraction of the corpus this leaves unchecked.

  (D) FULL REPOSITORY TABLE. Parse full_data_out.json's per-repo records (one example per repo under the github_founder_departure_commits group) and full_method_out.json's per-repo TFDD/survival outputs, and emit ONE row per repo (all repos present in the dataset artifact, whatever the final count is -- verify it is 15 by counting live records rather than assuming the number from the dependency summary) with columns: repo full_name, primary language, stars, forks, total commit-history span in years, whether a TFDD was detected, whether it was founder-only (TF=1 at detachment), the pre-departure diffusion score (founder commit-share, distinct non-founder DOA-owner count) if applicable, and the 18-month post-TFDD survival grade (thriving/maintained/dormant/dead) if applicable. Cross-check every field against the two source JSON files exactly (no invented or rounded-from-memory values) and flag any repo where a field is missing/null in the source data rather than silently omitting the row.

  (E) SURVIVORSHIP-BIAS QUANTIFICATION AND DESIGN-FLAW ARGUMENT. Recompute directly from the EXPERIMENT/DATASET outputs: this corpus's TFDD incidence rate (TFDDs / total usable repos) and 18-month survival rate among TFDD repos, and place them next to Avelino et al.'s published 16.3% incidence and 40.6% survival (cite the exact source numbers/section from the ESEM 2019 paper via a fresh aii-web-tools fetch_grep against the arXiv PDF, do not rely on memory of the hypothesis text) with a formal statistical comparison (a two-proportion z-test or exact binomial test against Avelino et al.'s rate treated as the null, reporting the test statistic, p-value, and a plain-language direction/magnitude statement, e.g. 'this corpus's TFDD-survival rate is X percentage points higher, z=..., p=...'). Since no expanded or non-conditioned corpus exists among this artifact's dependencies (the DATASET artifact's ~104-repo candidate pipeline was checkpointed but not completed, and the artifact direction's re-run-on-expanded-corpus step is therefore not executable from the given dependencies), do NOT fabricate or simulate a second corpus -- instead write an explicit 'Residual Limitation' section documenting: the structural argument for why conditioning on present-day liveness necessarily biases toward survivors (a short formal statement: any sampling frame requiring a repo to be 'currently famous and still maintained' assigns zero sampling probability to the non-survivor stratum this study needs to observe fully, so incidence/survival estimates from it are not just imprecise but inconsistent estimators of the population quantities), the fact that this study's own evidence is 15 out of a 104-repo candidate list with the remainder blocked by the unauthenticated 60-req/hour GitHub API cap (quote the exact numbers from the DATASET artifact's summary), and a concrete, falsifiable prediction of what a valid non-conditioned corpus run through the same pipeline should show (e.g. 'incidence should approach Avelino et al.'s 16.3% and survival should approach 40.6% within the CI computed in part B') so a future GEN_DATASET/GEN_EXPERIMENT artifact with GITHUB_TOKEN access has a stated, checkable target rather than a vague aspiration.

  All five parts write into a single eval_out.json (plus mini/preview variants per aii-json skill conventions) with clearly named top-level keys per part (permutation_disclosure, tf1_ci_comparison, alias_spotcheck, repo_table, survivorship_bias_quantification) and a top-level overall_verdict summarizing, in 3-5 sentences, which reviewer gaps are now fully closed with data (A, B, D, E's quantification half) versus which remain structurally open pending a new corpus (E's second-frame comparison, explicitly NOT run here). Validate the final JSON against the eval_out schema via the aii-json skill before finishing, and check output file sizes against the aii-file-size-limit skill.
metrics_justification: >-
  These five checks target exactly the methodology-rigor gaps a careful reviewer would flag on the prior 15-repo pipeline
  result, and each closes a specific, nameable threat to validity rather than adding generic robustness noise: (A) a permutation
  p-value reported without its achievable resolution (1/(k+1)) or its sampling scheme (with/without replacement, dependence
  across strata) is uninterpretable -- a p-value of 0.025 from 40 draws is at the theoretical floor and means something different
  from the same number at 2000 draws, so disclosing the scheme and showing budget-convergence is the minimum bar for trusting
  the placebo/window-shuffle result that underlies the paper's construct-validity claim. (B) A bare 'our TF=1 rate looks similar
  to their 66%' claim without confidence intervals on BOTH sides is not a comparison at all, especially with this study's
  tiny n; the Wilson interval (rather than the Wald normal approximation) is the standard correct choice for a proportion
  with a moderate-to-small denominator and one anchored near neither 0 nor 1, and reporting both intervals turns an assertion
  into a falsifiable statistical statement. (C) The diffusion measurement's core claim (distinct non-founder DOA owners) is
  only as good as identity resolution; since the EXPERIMENT reported a suspicious 0.0-median alias-collapse-rate, a live spot-check
  against GitHub's actual contributor graph is the cheapest available external validity check on whether that diffusion count
  is inflated by bots or under-merged identities -- exactly the kind of concrete, checkable evidence a reviewer would ask
  for instead of trusting an internal QA metric produced by the same pipeline being validated. (D) An exact, complete repository
  table is table-stakes for reproducibility and lets a reader (or downstream paper-writing step) verify every headline number
  against raw per-repo facts rather than trusting aggregate statistics alone -- it also surfaces silently-dropped or null-field
  repos that aggregate summaries can hide. (E) The hypothesis's central claim is that the 15-repo corpus's deviation from
  Avelino et al.'s published rates is a SAMPLING-FRAME defect, not a power shortfall; formalizing that as a statistical test
  against the published null (rather than an eyeballed 53.3% vs 16.3% comparison) plus an explicit, honestly-scoped limitations
  statement about what remains unverified (since no second, non-conditioned corpus exists to run head-to-head) is what turns
  a plausible narrative into a defensible, appropriately-hedged scientific claim -- and prevents the paper from either overclaiming
  a resolved comparison or understating how much of the design-flaw argument is currently structural reasoning versus direct
  empirical contrast.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_ZuMis522AEPF
type: dataset
title: GitHub Founder-Departure Commit Corpus
summary: >-
  Built a real corpus of 15 well-known, well-documented open-source GitHub repositories (e.g. pallets/flask, BurntSushi/ripgrep,
  psf/black, Textualize/rich, httpie/cli, pyenv/pyenv, tiangolo/typer), each with full commit history obtained via `git clone`
  + `git log --numstat` (SHA, author name/email, ISO date, per-file insertions/deletions for every commit, newest-first, capped
  at 5,000 commits/repo with an explicit truncation flag) plus repo-level metadata from the GitHub REST API (stars, forks,
  primary language, license, created_at, pushed_at, open_issues, README excerpt). Each repo record also carries an empirically-computed
  `founder_signal`: the fraction of commits in the repo's first 365 days made by its single top-committing author email, and
  the top author's email. This directly operationalizes the plan's inclusion criterion (single-founder dominance >=70% of
  year-1 commits) without asserting it a priori -- it is measured from the real cloned git log. Repos span multiple languages
  (Python, Rust) and star bands (15k-72k stars in the current sample) and multi-year histories (6.6-16.4 years), giving enough
  post-founding history for an 18-month post-departure survival window. IMPORTANT SCOPE LIMITATION: this environment has no
  GITHUB_TOKEN, so the GitHub REST API is capped at 60 unauthenticated requests/hour (2 calls per repo: /repos/{full_name}
  and its /readme). This makes the plan's 150-250 repo target infeasible within the artifact time budget -- 15 repos were
  completed and checkpointed (12 in the final checkpoint snapshot, 15 repo-record files on disk) before the artifact needed
  to finalize; git clone itself (smart-HTTP) is NOT rate-limited, so every completed repo's commit history is complete and
  untruncated for its cap, only the TOTAL repo count is reduced. code/build_dataset.py and code/candidates.py contain a ~104-repo
  candidate list spanning Python/JS/Go/Ruby/Rust/C++/Java and a checkpointed, resumable pipeline (temp/checkpoint.json) that
  a downstream step can re-run with a GITHUB_TOKEN (raising the limit to 5,000 req/hour) to scale to the full 150-250 target
  without re-doing completed work. A HuggingFace candidate (kamalkishor1991/commit-messages-dataset, sampled commit diffs
  for commit-message generation) was evaluated and explicitly rejected as the primary source because it lacks per-repo lifecycle,
  author-identity-over-time, and per-file structure. data.py standardizes the corpus into the exp_sel_data_out.json schema:
  one dataset group `github_founder_departure_commits`, one example per repo, `input` = JSON-encoded {repo_metadata, founder_signal,
  truncated, commit_cap, commits[]}, `output` = derived label 'founder_dominant'/'not_founder_dominant' from the 0.7 year-1-share
  threshold, plus flat `metadata_*` fields (full_name, stars, language, history_years, n_commits, truncated, year1_top_author_share,
  task_type). Validated against the exp_sel_data_out schema (PASSED); full_data_out.json is 13.8MB (well under the 100MB limit),
  with mini_data_out.json and preview_data_out.json also produced.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
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

--- Dependency 2 ---
id: art_I5KoOp16hub5
type: experiment
title: Does authority spreading before founders leave keep projects alive?
summary: >-
  Reimplemented Avelino et al.'s (ESEM 2019) Degree-of-Authorship / Truck-Factor / Truck-Factor-Detachment-Departure (TFDD)
  pipeline end-to-end in method.py, run against the DATASET dependency's mined GitHub commit histories (15 usable repos with
  full per-file commit logs, out of 3427 raw records also containing an unrelated HuggingFace commit-message corpus that the
  loader correctly skips via a 'no_commits' filter). For each repo the pipeline: (1) resolves author aliases via normalized
  email/github-login matching and logs a per-repo alias-collapse-rate QA metric; (2) computes yearly cumulative-window DOA
  (Degree of Authorship) per file per author using Fritz et al.'s weights (FA=3.293, DL=1.098, AC=-1.017) as used by Avelino
  et al.; (3) derives the yearly greedy Truck-Factor set from primary DOA ownership; (4) detects Truck-Factor-Detachment-Departure
  events (a TF-set fully silent for 12 months) and isolates founder-only TFDDs (TF=1 and the sole departing developer is the
  repo's first human committer, with bulk-import first commits filtered per the Kalliamvakou et al. 2014 'perils of mining
  GitHub' heuristic of >80% of files touched within the first week); (5) computes a NEW pre-departure authority-diffusion
  trajectory over the 6-12 months before each TFDD -- founder commit-share and count of distinct non-founder DOA file-owners
  -- alongside Avelino et al.'s original at-TFDD snapshot covariates (developers/commits/files at detachment); (6) classifies
  18-month post-TFDD survival into Avelino's four-level active/inactive grades (thriving/maintained/dormant/dead) plus a binary
  survived flag; (7) runs a matched-pairs bootstrap comparison (nearest-neighbor matching on standardized log-stars/log-forks/log-contributors
  within language, comparing high- vs low-diffusion projects) with 10,000-resample 95% CIs; (8) fits BH-corrected logistic
  and ordinal (statsmodels OrderedModel) regressions of survival on diffusion predictors plus snapshot covariates, reporting
  standardized effect sizes comparable to Avelino et al.'s reported d=0.13 (files) / 0.25-0.26 (developers, commits); (9)
  runs a 500-iteration placebo/window-shuffle check that redraws the pre-departure window from elsewhere in project history
  and refits the regression, to test whether the true diffusion-window effect exceeds the null distribution of effects from
  arbitrary windows. All steps implement both the proposed authority-diffusion predictor AND Avelino et al.'s original snapshot-covariate
  baseline side-by-side in the same regression and matched-pairs machinery, so the two are directly comparable under identical
  data and identical statistical procedures -- baseline_predict and ourmethod_predict columns are both emitted per example.
  The run found n_repos_total=3427 raw dataset records (3409 filtered as non-repo commit-message rows lacking file-level structure;
  the dataset dependency's GitHub API rate limiting -- 60 unauthenticated requests/hour -- constrained the usable repo count
  to 15, well below the plan's 150-250 target), yielding n_founder_tfdd_events=6, which falls below the ~40 events the plan's
  own fallback_plan identifies as needed for a well-powered matched-pairs test; per that fallback plan this limitation is
  reported explicitly in the output metadata (extended_sample_used_TFle2 flag, doa_approximation_used flag, alias_qa block)
  rather than silently presented as adequately powered, and all regression/matched-pairs/placebo numbers in method_out.json
  should be read as a small-n pilot demonstrating the pipeline mechanics rather than a well-powered test of the founder-diffusion-predicts-survival
  hypothesis. A bug where the dataset dependency's example-wrapper format (repo records JSON-encoded inside an 'input' string
  field, per the exp_gen_sol_out schema) was not being unwrapped -- causing every repo to be misread as having zero commits
  -- was found and fixed during this run; the corrected loader now parses that wrapper and the pipeline runs end-to-end in
  ~90 seconds. Output method_out.json / full_method_out.json / mini_method_out.json / preview_method_out.json validate cleanly
  against the exp_gen_sol_out.json schema (0 errors) and are all under 9KB, far below the 100MB size limit. Downstream users
  (GEN_PAPER_TEXT) should present this as a methodology-validation / small-sample pilot result: the pipeline itself (DOA/TF/TFDD
  replication, diffusion-trajectory measurement, survival classification, matched-pairs + regression + placebo statistical
  machinery) is fully implemented and tested (smoke tests on synthetic hand-constructed repos, mini-run sanity checks, and
  the full corpus run all pass), but the headline finding is data-starved (n=6 events) due to upstream GitHub API rate limiting
  documented in the DATASET dependency's own metadata, not a pipeline defect.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
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

### [8] SYSTEM-USER prompt · 2026-08-20 20:19:52 UTC

```
<validation-feedback>
Attempt 1 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [9] SYSTEM-USER prompt · 2026-08-20 20:20:10 UTC

```
<validation-feedback>
Attempt 2 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [10] SYSTEM-USER prompt · 2026-08-20 20:20:22 UTC

```
<validation-feedback>
Attempt 3 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [11] SYSTEM-USER prompt · 2026-08-20 20:21:24 UTC

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

<CRITICAL_WARNING__PREVIOUS_ATTEMPT_CRASHED>
YOUR PREVIOUS EXECUTION ATTEMPT CATASTROPHICALLY FAILED.
The entire worker container crashed after 625s.
Error: output_format validation failed after 3 retries: The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Last messages before the crash:
  - [agent_tool_call: Bash] Tool: Bash
ls -lh; ps aux | grep eval.py | grep -v grep; tail -60 logs/run.log 2>/dev/null
  - [agent_tool_result: Bash] Tool: Bash
Result:
{"stdout": "total 41K\n-rw-rw-rw- 1 root root 40K Aug 20 20:17 eval.py\ndrwxrwxrwx 2 root root   1 Aug 20 20:18 logs\n-rw-rw-rw- 1 root root 274 Aug 20 20:13 pyproject.toml\nroot         302  0.0  0.0   4492  3404 ?        Ss   20:17   0:00 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1787256669014-rgfikr.sh 2>/dev/null || true && shopt -u extglob 2>/dev/null || true && { \\builtin unalias -- 'unsetenv'; \\builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'timeout 600 .venv/bin/python eval.py 2>&1 | tail -80' < /dev/null && pwd -P >| /tmp/claude-a45d-cwd\nroot         304  0.0  0.0   2928  1740 ?        S    20:17   0:00 timeout 600 .venv/bin/python eval.py\nroot         306  9.2  0.0 4220120 185912 ?      Sl   20:17   0:14 .venv/bin/python eval.py", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
  - [agent_tool_call: Bash] Tool: Bash
cat /tmp/claude-0/-ai-inventor-aii-data-runs-run-5SMkWpWKNLxk-3-invention-loop-iter-2-gen-art-gen-art-evaluation-1/5cabd562-f1e9-4242-8b36-3a0cc3b5fb2a/tasks/bunicpbwu.output 2>/dev/null | tail -80
  - [agent_tool_result: Bash] Tool: Bash
Result:
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
  - [agent_tool_call: Monitor] Tool: Monitor
{'command': 'tail -f /tmp/claude-0/-ai-inventor-aii-data-runs-run-5SMkWpWKNLxk-3-invention-loop-iter-2-gen-art-gen-art-evaluation-1/5cabd562-f1e9-4242-8b36-3a0cc3b5fb2a/tasks/bunicpbwu.output', 'description': 'stream eval.py output as it runs', 'timeout_ms': 600000, 'persistent': False}
  - [agent_tool_result: Monitor] Tool: Monitor
Result:
{"taskId": "brjk0lu9q", "timeoutMs": 600000, "persistent": false}
  - [agent_response] Waiting for eval.py's output stream — nothing has printed yet, likely still in slow cold imports (pandas/statsmodels). I'll continue once output or completion appears.
  - [agent_tool_call: Bash] Tool: Bash
ls -lh; ps aux | grep eval.py | grep -v grep; echo ---; wc -l /tmp/claude-0/-ai-inventor-aii-data-runs-run-5SMkWpWKNLxk-3-invention-loop-iter-2-gen-art-gen-art-evaluation-1/5cabd562-f1e9-4242-8b36-3a0cc3b5fb2a/tasks/bunicpbwu.output 2>/dev/null
  - [agent_tool_result: Bash] Tool: Bash
Result:
{"stdout": "total 41K\n-rw-rw-rw- 1 root root 40K Aug 20 20:17 eval.py\ndrwxrwxrwx 2 root root   1 Aug 20 20:18 logs\n-rw-rw-rw- 1 root root 274 Aug 20 20:13 pyproject.toml\nroot         302  0.0  0.0   4492  3404 ?        Ss   20:17   0:00 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1787256669014-rgfikr.sh 2>/dev/null || true && shopt -u extglob 2>/dev/null || true && { \\builtin unalias -- 'unsetenv'; \\builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'timeout 600 .venv/bin/python eval.py 2>&1 | tail -80' < /dev/null && pwd -P >| /tmp/claude-a45d-cwd\nroot         304  0.0  0.0   2928  1740 ?        S    20:17   0:00 timeout 600 .venv/bin/python eval.py\nroot         306 13.6  0.1 4303644 269420 ?      Rl   20:17   0:24 .venv/bin/python eval.py\n---\n0 /tmp/claude-0/-ai-inventor-aii-data-runs-run-5SMkWpWKNLxk-3-invention-loop-iter-2-gen-art-gen-art-evaluation-1/5cabd562-f1e9-4242-8b36-3a0cc3b5fb2a/tasks/bunicpbwu.output", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
  - [agent_tool_call: Monitor] Tool: Monitor
{'command': 'until [ -f /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/eval_out.json ] || ! kill -0 306 2>/dev/null; do sleep 5; done; echo "eval.py finished"; ls -lh /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/', 'description': 'wait for eval_out.json to appear or process to exit', 'timeout_ms': 600000, 'persistent': False}
  - [agent_tool_result: Monitor] Tool: Monitor
Result:
{"taskId": "bcdlky2ip", "timeoutMs": 600000, "persistent": false}
  - [agent_response] Waiting for eval.py (PID 306) to finish and produce eval_out.json.
  - [agent_tool_call: Bash] Tool: Bash
ls -lh /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/; ps aux | grep eval.py | grep -v grep
  - [agent_tool_result: Bash] Tool: Bash
Result:
{"stdout": "total 41K\n-rw-rw-rw- 1 root root 40K Aug 20 20:17 eval.py\ndrwxrwxrwx 2 root root   1 Aug 20 20:18 logs\n-rw-rw-rw- 1 root root 274 Aug 20 20:13 pyproject.toml\nroot         302  0.0  0.0   4492  3404 ?        Ss   20:17   0:00 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1787256669014-rgfikr.sh 2>/dev/null || true && shopt -u extglob 2>/dev/null || true && { \\builtin unalias -- 'unsetenv'; \\builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'timeout 600 .venv/bin/python eval.py 2>&1 | tail -80' < /dev/null && pwd -P >| /tmp/claude-a45d-cwd\nroot         304  0.0  0.0   2928  1740 ?        S    20:17   0:00 timeout 600 .venv/bin/python eval.py\nroot         306 18.8  0.1 4303644 269424 ?      Rl   20:17   0:35 .venv/bin/python eval.py\nroot         525  0.0  0.0   4492  3356 ?        Ss   20:20   0:00 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1787256669014-rgfikr.sh 2>/dev/null || true && shopt -u extglob 2>/dev/null || true && { \\builtin unalias -- 'unsetenv'; \\builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'until [ -f /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/eval_out.json ] || ! kill -0 306 2>/dev/null; do sleep 5; done; echo \"eval.py finished\"; ls -lh /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/' < /dev/null && pwd -P >| /tmp/claude-40f0-cwd", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
  - [agent_response] Still running (35s CPU, 600s timeout limit set on it). I'll keep waiting for the Monitor to notify completion.

This was NOT a normal code error — the entire container died. Study the error
and last messages above carefully. Identify what caused the crash and be
EXTREMELY careful to avoid repeating it. Do NOT use the same approach.
</CRITICAL_WARNING__PREVIOUS_ATTEMPT_CRASHED>

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/file.py`, `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_evaluation_1_idx3
type: evaluation
title: Closing the Rigor Gaps in the Diffusion Pipeline
summary: >-
  Extends the prior eval.py against the DATASET (art_ZuMis522AEPF) and EXPERIMENT (art_I5KoOp16hub5) artifacts to close five
  reviewer-named gaps without collecting new repos or building new methods: (1) fully disclose the permutation scheme used
  for the placebo/window-shuffle check and re-run it at a larger budget to show p-value stability; (2) compute a Wilson 95%
  CI for Avelino et al.'s reported 66% TF=1 statistic (n=315) and report it side-by-side with this study's own CI instead
  of asserting 'overlap' informally; (3) manually spot-check the alias-resolution diagnostic against live GitHub contributor
  pages for 2-3 corpus repos via aii-web-tools; (4) emit an exact, full repository table (name, language, stars, history length,
  TFDD/survival status) matching the dataset artifact's real output for use as a paper table; (5) explicitly quantify and
  narrate the survivorship-bias direction/magnitude versus Avelino et al.'s published rates, and (since no expanded/non-conditioned
  corpus exists among the dependencies) formally document that the design-flaw-not-power-problem claim rests on structural
  argument plus the existing single-frame evidence, not on a second frame -- reporting this as a residual limitation rather
  than silently treating the comparison as already done.
runpod_compute_profile: gpu
metrics_descriptions: |-
  All computations run in a new eval.py inside this artifact's workspace, loading full_method_out.json from the EXPERIMENT dependency (art_I5KoOp16hub5) and full_data_out.json from the DATASET dependency (art_ZuMis522AEPF) by their absolute dependency workspace_path files -- do not re-derive data, only re-analyze what those artifacts already produced (recompute the placebo/permutation test at higher budget using the EXPERIMENT's own method.py functions/logic where feasible, since that is legitimate re-analysis, not new data collection).

  (A) PERMUTATION-SCHEME DISCLOSURE + CONVERGENCE. From method_out.json's placebo/window-shuffle block (500 iterations reported in the EXPERIMENT summary) and the underlying per-repo history-length metadata in full_data_out.json, compute for EACH of the n_founder_tfdd_events=6 founder-only-TFDD repos: the number of feasible distinct 6-12-month relocatable windows given that repo's total history length in months (e.g. a repo with H months of usable history and a 6-month window has roughly H-6 distinct start-month positions, so state this arithmetic explicitly per repo and sum/report the combinatorial space size). State explicitly whether the reported 500 (or the original run's cited '60/40') shuffle draws were i.i.d. samples WITH or WITHOUT replacement from that space (read this from method.py's actual placebo-generation code, do not assume) and whether the same random seed reused across strata induces any dependence between the survivor and non-survivor shuffle sets. Derive the theoretical minimum achievable two-sided p-value given the placebo sample count k as 1/(k+1) (standard permutation-test resolution bound), and report it next to the actually-computed p-value so a reader can judge whether the reported p-value is bounded away from that floor or sitting on it (a p-value equal to the floor value is a red flag that more permutations are needed, not evidence of significance). Then RE-RUN the placebo test at a substantially larger budget -- target 2000 iterations per stratum if the small n=6 event corpus and its capped/cached DOA recomputation make this fast (state the actual wall-clock observed; if 2000 is infeasible within the time budget, fall back to the largest budget achieved within roughly 20 minutes of compute and report exactly what budget that was and why, rather than silently using fewer). Report the placebo p-value (and effect-size null-distribution mean/SD) at each of at least 3 budgets (e.g. original ~60/40, an intermediate step, and the final larger budget) in a convergence table, and state explicitly whether the qualitative conclusion (effect specific to the true pre-departure window vs. not) is stable across budgets or flips.

  (B) AVELINO ET AL. 66% TF=1 WILSON CI. Using n=315 (Avelino et al.'s reported total TFDD count) and the reported proportion 0.66 (208 of 315, computing the exact count as round(0.66*315) and stating that rounding explicitly since the paper does not give the raw numerator), compute a Wilson score 95% CI (not the normal-approximation Wald interval, which is unreliable near 0/1 and for the moderate n here -- use the standard Wilson formula: center = (phat + z^2/(2n)) / (1 + z^2/n), halfwidth = z*sqrt(phat*(1-phat)/n + z^2/(4n^2)) / (1 + z^2/n), z=1.959964 for 95%). Compute the SAME Wilson CI for this study's own TF=1 founder-TFDD fraction using this study's own n (the count of ALL TFDD events found in the 15-repo corpus, not just the founder-only subset of 6 -- pull both numbers from method_out.json's diagnostic fields) and report both CIs side by side in a small table with an explicit overlap/non-overlap determination (do not just eyeball it -- state the numeric bounds of both intervals and whether they intersect). Given the small denominator on this study's side, explicitly flag if the interval is very wide and caution against over-reading 'overlap' as validation when this study's own CI could contain almost any plausible fraction.

  (C) ALIAS-RESOLUTION SPOT-CHECK. Select 2-3 of the 15 corpus repos (prefer ones with the highest reported alias-collapse-rate variance or the ones contributing founder-only TFDD events, since those drive the headline numbers) and for each: use the aii-web-tools skill's web fetch/fetch_grep to pull the live GitHub repo's /graphs/contributors page or the repo's README/CONTRIBUTORS file and its top-committer list, and cross-reference the distinct author emails/logins the EXPERIMENT pipeline counted as 'distinct non-founder DOA file-owners' against what GitHub's own UI presents as distinct human contributors. Explicitly look for: (i) bot accounts (e.g. dependabot, github-actions[bot]) miscounted as human authority-holders, (ii) the same human appearing under 2+ emails/handles that the pipeline's alias-resolution did NOT merge (under-merging, which would inflate the diffusion score), and (iii) the reverse -- two distinct humans merged into one identity (over-merging, which would deflate it). Report per-repo: number of identities checked, number found to be bots, number found to be split identities of the same human, and whether correcting these would change that repo's founder-only-TFDD classification or diffusion score materially. State clearly this is a spot-check on 2-3 repos, not a full audit, and describe what fraction of the corpus this leaves unchecked.

  (D) FULL REPOSITORY TABLE. Parse full_data_out.json's per-repo records (one example per repo under the github_founder_departure_commits group) and full_method_out.json's per-repo TFDD/survival outputs, and emit ONE row per repo (all repos present in the dataset artifact, whatever the final count is -- verify it is 15 by counting live records rather than assuming the number from the dependency summary) with columns: repo full_name, primary language, stars, forks, total commit-history span in years, whether a TFDD was detected, whether it was founder-only (TF=1 at detachment), the pre-departure diffusion score (founder commit-share, distinct non-founder DOA-owner count) if applicable, and the 18-month post-TFDD survival grade (thriving/maintained/dormant/dead) if applicable. Cross-check every field against the two source JSON files exactly (no invented or rounded-from-memory values) and flag any repo where a field is missing/null in the source data rather than silently omitting the row.

  (E) SURVIVORSHIP-BIAS QUANTIFICATION AND DESIGN-FLAW ARGUMENT. Recompute directly from the EXPERIMENT/DATASET outputs: this corpus's TFDD incidence rate (TFDDs / total usable repos) and 18-month survival rate among TFDD repos, and place them next to Avelino et al.'s published 16.3% incidence and 40.6% survival (cite the exact source numbers/section from the ESEM 2019 paper via a fresh aii-web-tools fetch_grep against the arXiv PDF, do not rely on memory of the hypothesis text) with a formal statistical comparison (a two-proportion z-test or exact binomial test against Avelino et al.'s rate treated as the null, reporting the test statistic, p-value, and a plain-language direction/magnitude statement, e.g. 'this corpus's TFDD-survival rate is X percentage points higher, z=..., p=...'). Since no expanded or non-conditioned corpus exists among this artifact's dependencies (the DATASET artifact's ~104-repo candidate pipeline was checkpointed but not completed, and the artifact direction's re-run-on-expanded-corpus step is therefore not executable from the given dependencies), do NOT fabricate or simulate a second corpus -- instead write an explicit 'Residual Limitation' section documenting: the structural argument for why conditioning on present-day liveness necessarily biases toward survivors (a short formal statement: any sampling frame requiring a repo to be 'currently famous and still maintained' assigns zero sampling probability to the non-survivor stratum this study needs to observe fully, so incidence/survival estimates from it are not just imprecise but inconsistent estimators of the population quantities), the fact that this study's own evidence is 15 out of a 104-repo candidate list with the remainder blocked by the unauthenticated 60-req/hour GitHub API cap (quote the exact numbers from the DATASET artifact's summary), and a concrete, falsifiable prediction of what a valid non-conditioned corpus run through the same pipeline should show (e.g. 'incidence should approach Avelino et al.'s 16.3% and survival should approach 40.6% within the CI computed in part B') so a future GEN_DATASET/GEN_EXPERIMENT artifact with GITHUB_TOKEN access has a stated, checkable target rather than a vague aspiration.

  All five parts write into a single eval_out.json (plus mini/preview variants per aii-json skill conventions) with clearly named top-level keys per part (permutation_disclosure, tf1_ci_comparison, alias_spotcheck, repo_table, survivorship_bias_quantification) and a top-level overall_verdict summarizing, in 3-5 sentences, which reviewer gaps are now fully closed with data (A, B, D, E's quantification half) versus which remain structurally open pending a new corpus (E's second-frame comparison, explicitly NOT run here). Validate the final JSON against the eval_out schema via the aii-json skill before finishing, and check output file sizes against the aii-file-size-limit skill.
metrics_justification: >-
  These five checks target exactly the methodology-rigor gaps a careful reviewer would flag on the prior 15-repo pipeline
  result, and each closes a specific, nameable threat to validity rather than adding generic robustness noise: (A) a permutation
  p-value reported without its achievable resolution (1/(k+1)) or its sampling scheme (with/without replacement, dependence
  across strata) is uninterpretable -- a p-value of 0.025 from 40 draws is at the theoretical floor and means something different
  from the same number at 2000 draws, so disclosing the scheme and showing budget-convergence is the minimum bar for trusting
  the placebo/window-shuffle result that underlies the paper's construct-validity claim. (B) A bare 'our TF=1 rate looks similar
  to their 66%' claim without confidence intervals on BOTH sides is not a comparison at all, especially with this study's
  tiny n; the Wilson interval (rather than the Wald normal approximation) is the standard correct choice for a proportion
  with a moderate-to-small denominator and one anchored near neither 0 nor 1, and reporting both intervals turns an assertion
  into a falsifiable statistical statement. (C) The diffusion measurement's core claim (distinct non-founder DOA owners) is
  only as good as identity resolution; since the EXPERIMENT reported a suspicious 0.0-median alias-collapse-rate, a live spot-check
  against GitHub's actual contributor graph is the cheapest available external validity check on whether that diffusion count
  is inflated by bots or under-merged identities -- exactly the kind of concrete, checkable evidence a reviewer would ask
  for instead of trusting an internal QA metric produced by the same pipeline being validated. (D) An exact, complete repository
  table is table-stakes for reproducibility and lets a reader (or downstream paper-writing step) verify every headline number
  against raw per-repo facts rather than trusting aggregate statistics alone -- it also surfaces silently-dropped or null-field
  repos that aggregate summaries can hide. (E) The hypothesis's central claim is that the 15-repo corpus's deviation from
  Avelino et al.'s published rates is a SAMPLING-FRAME defect, not a power shortfall; formalizing that as a statistical test
  against the published null (rather than an eyeballed 53.3% vs 16.3% comparison) plus an explicit, honestly-scoped limitations
  statement about what remains unverified (since no second, non-conditioned corpus exists to run head-to-head) is what turns
  a plausible narrative into a defensible, appropriately-hedged scientific claim -- and prevents the paper from either overclaiming
  a resolved comparison or understating how much of the design-flaw argument is currently structural reasoning versus direct
  empirical contrast.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_ZuMis522AEPF
type: dataset
title: GitHub Founder-Departure Commit Corpus
summary: >-
  Built a real corpus of 15 well-known, well-documented open-source GitHub repositories (e.g. pallets/flask, BurntSushi/ripgrep,
  psf/black, Textualize/rich, httpie/cli, pyenv/pyenv, tiangolo/typer), each with full commit history obtained via `git clone`
  + `git log --numstat` (SHA, author name/email, ISO date, per-file insertions/deletions for every commit, newest-first, capped
  at 5,000 commits/repo with an explicit truncation flag) plus repo-level metadata from the GitHub REST API (stars, forks,
  primary language, license, created_at, pushed_at, open_issues, README excerpt). Each repo record also carries an empirically-computed
  `founder_signal`: the fraction of commits in the repo's first 365 days made by its single top-committing author email, and
  the top author's email. This directly operationalizes the plan's inclusion criterion (single-founder dominance >=70% of
  year-1 commits) without asserting it a priori -- it is measured from the real cloned git log. Repos span multiple languages
  (Python, Rust) and star bands (15k-72k stars in the current sample) and multi-year histories (6.6-16.4 years), giving enough
  post-founding history for an 18-month post-departure survival window. IMPORTANT SCOPE LIMITATION: this environment has no
  GITHUB_TOKEN, so the GitHub REST API is capped at 60 unauthenticated requests/hour (2 calls per repo: /repos/{full_name}
  and its /readme). This makes the plan's 150-250 repo target infeasible within the artifact time budget -- 15 repos were
  completed and checkpointed (12 in the final checkpoint snapshot, 15 repo-record files on disk) before the artifact needed
  to finalize; git clone itself (smart-HTTP) is NOT rate-limited, so every completed repo's commit history is complete and
  untruncated for its cap, only the TOTAL repo count is reduced. code/build_dataset.py and code/candidates.py contain a ~104-repo
  candidate list spanning Python/JS/Go/Ruby/Rust/C++/Java and a checkpointed, resumable pipeline (temp/checkpoint.json) that
  a downstream step can re-run with a GITHUB_TOKEN (raising the limit to 5,000 req/hour) to scale to the full 150-250 target
  without re-doing completed work. A HuggingFace candidate (kamalkishor1991/commit-messages-dataset, sampled commit diffs
  for commit-message generation) was evaluated and explicitly rejected as the primary source because it lacks per-repo lifecycle,
  author-identity-over-time, and per-file structure. data.py standardizes the corpus into the exp_sel_data_out.json schema:
  one dataset group `github_founder_departure_commits`, one example per repo, `input` = JSON-encoded {repo_metadata, founder_signal,
  truncated, commit_cap, commits[]}, `output` = derived label 'founder_dominant'/'not_founder_dominant' from the 0.7 year-1-share
  threshold, plus flat `metadata_*` fields (full_name, stars, language, history_years, n_commits, truncated, year1_top_author_share,
  task_type). Validated against the exp_sel_data_out schema (PASSED); full_data_out.json is 13.8MB (well under the 100MB limit),
  with mini_data_out.json and preview_data_out.json also produced.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
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

--- Dependency 2 ---
id: art_I5KoOp16hub5
type: experiment
title: Does authority spreading before founders leave keep projects alive?
summary: >-
  Reimplemented Avelino et al.'s (ESEM 2019) Degree-of-Authorship / Truck-Factor / Truck-Factor-Detachment-Departure (TFDD)
  pipeline end-to-end in method.py, run against the DATASET dependency's mined GitHub commit histories (15 usable repos with
  full per-file commit logs, out of 3427 raw records also containing an unrelated HuggingFace commit-message corpus that the
  loader correctly skips via a 'no_commits' filter). For each repo the pipeline: (1) resolves author aliases via normalized
  email/github-login matching and logs a per-repo alias-collapse-rate QA metric; (2) computes yearly cumulative-window DOA
  (Degree of Authorship) per file per author using Fritz et al.'s weights (FA=3.293, DL=1.098, AC=-1.017) as used by Avelino
  et al.; (3) derives the yearly greedy Truck-Factor set from primary DOA ownership; (4) detects Truck-Factor-Detachment-Departure
  events (a TF-set fully silent for 12 months) and isolates founder-only TFDDs (TF=1 and the sole departing developer is the
  repo's first human committer, with bulk-import first commits filtered per the Kalliamvakou et al. 2014 'perils of mining
  GitHub' heuristic of >80% of files touched within the first week); (5) computes a NEW pre-departure authority-diffusion
  trajectory over the 6-12 months before each TFDD -- founder commit-share and count of distinct non-founder DOA file-owners
  -- alongside Avelino et al.'s original at-TFDD snapshot covariates (developers/commits/files at detachment); (6) classifies
  18-month post-TFDD survival into Avelino's four-level active/inactive grades (thriving/maintained/dormant/dead) plus a binary
  survived flag; (7) runs a matched-pairs bootstrap comparison (nearest-neighbor matching on standardized log-stars/log-forks/log-contributors
  within language, comparing high- vs low-diffusion projects) with 10,000-resample 95% CIs; (8) fits BH-corrected logistic
  and ordinal (statsmodels OrderedModel) regressions of survival on diffusion predictors plus snapshot covariates, reporting
  standardized effect sizes comparable to Avelino et al.'s reported d=0.13 (files) / 0.25-0.26 (developers, commits); (9)
  runs a 500-iteration placebo/window-shuffle check that redraws the pre-departure window from elsewhere in project history
  and refits the regression, to test whether the true diffusion-window effect exceeds the null distribution of effects from
  arbitrary windows. All steps implement both the proposed authority-diffusion predictor AND Avelino et al.'s original snapshot-covariate
  baseline side-by-side in the same regression and matched-pairs machinery, so the two are directly comparable under identical
  data and identical statistical procedures -- baseline_predict and ourmethod_predict columns are both emitted per example.
  The run found n_repos_total=3427 raw dataset records (3409 filtered as non-repo commit-message rows lacking file-level structure;
  the dataset dependency's GitHub API rate limiting -- 60 unauthenticated requests/hour -- constrained the usable repo count
  to 15, well below the plan's 150-250 target), yielding n_founder_tfdd_events=6, which falls below the ~40 events the plan's
  own fallback_plan identifies as needed for a well-powered matched-pairs test; per that fallback plan this limitation is
  reported explicitly in the output metadata (extended_sample_used_TFle2 flag, doa_approximation_used flag, alias_qa block)
  rather than silently presented as adequately powered, and all regression/matched-pairs/placebo numbers in method_out.json
  should be read as a small-n pilot demonstrating the pipeline mechanics rather than a well-powered test of the founder-diffusion-predicts-survival
  hypothesis. A bug where the dataset dependency's example-wrapper format (repo records JSON-encoded inside an 'input' string
  field, per the exp_gen_sol_out schema) was not being unwrapped -- causing every repo to be misread as having zero commits
  -- was found and fixed during this run; the corrected loader now parses that wrapper and the pipeline runs end-to-end in
  ~90 seconds. Output method_out.json / full_method_out.json / mini_method_out.json / preview_method_out.json validate cleanly
  against the exp_gen_sol_out.json schema (0 errors) and are all under 9KB, far below the 100MB size limit. Downstream users
  (GEN_PAPER_TEXT) should present this as a methodology-validation / small-sample pilot result: the pipeline itself (DOA/TF/TFDD
  replication, diffusion-trajectory measurement, survival classification, matched-pairs + regression + placebo statistical
  machinery) is fully implemented and tested (smoke tests on synthetic hand-constructed repos, mini-run sanity checks, and
  the full corpus run all pass), but the headline finding is data-starved (n=6 events) due to upstream GitHub API rate limiting
  documented in the DATASET dependency's own metadata, not a pipeline defect.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
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
TODO 2. Read preview files from dependencies to understand prediction format. Evaluate ALL experiments provided — do not skip or select a subset. Avoid re-training or re-executing the method unless absolutely necessary; prefer loading predictions from each dependency's method_out.json / predict_* fields. Read domain handbook if applicable (see <available_domain_handbooks>). Decide evaluation metrics based on artifact plan. Test basic functionality with 'uv run'.
TODO 3. Fully implement evaluation as described in artifact plan in './eval.py'. Use exp_eval_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant metrics or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
```

### [12] HUMAN-USER prompt · 2026-08-20 20:21:24 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [13] SYSTEM-USER prompt · 2026-08-20 20:23:50 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/file.py`, `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_evaluation_1_idx3
type: evaluation
title: Closing the Rigor Gaps in the Diffusion Pipeline
summary: >-
  Extends the prior eval.py against the DATASET (art_ZuMis522AEPF) and EXPERIMENT (art_I5KoOp16hub5) artifacts to close five
  reviewer-named gaps without collecting new repos or building new methods: (1) fully disclose the permutation scheme used
  for the placebo/window-shuffle check and re-run it at a larger budget to show p-value stability; (2) compute a Wilson 95%
  CI for Avelino et al.'s reported 66% TF=1 statistic (n=315) and report it side-by-side with this study's own CI instead
  of asserting 'overlap' informally; (3) manually spot-check the alias-resolution diagnostic against live GitHub contributor
  pages for 2-3 corpus repos via aii-web-tools; (4) emit an exact, full repository table (name, language, stars, history length,
  TFDD/survival status) matching the dataset artifact's real output for use as a paper table; (5) explicitly quantify and
  narrate the survivorship-bias direction/magnitude versus Avelino et al.'s published rates, and (since no expanded/non-conditioned
  corpus exists among the dependencies) formally document that the design-flaw-not-power-problem claim rests on structural
  argument plus the existing single-frame evidence, not on a second frame -- reporting this as a residual limitation rather
  than silently treating the comparison as already done.
runpod_compute_profile: gpu
metrics_descriptions: |-
  All computations run in a new eval.py inside this artifact's workspace, loading full_method_out.json from the EXPERIMENT dependency (art_I5KoOp16hub5) and full_data_out.json from the DATASET dependency (art_ZuMis522AEPF) by their absolute dependency workspace_path files -- do not re-derive data, only re-analyze what those artifacts already produced (recompute the placebo/permutation test at higher budget using the EXPERIMENT's own method.py functions/logic where feasible, since that is legitimate re-analysis, not new data collection).

  (A) PERMUTATION-SCHEME DISCLOSURE + CONVERGENCE. From method_out.json's placebo/window-shuffle block (500 iterations reported in the EXPERIMENT summary) and the underlying per-repo history-length metadata in full_data_out.json, compute for EACH of the n_founder_tfdd_events=6 founder-only-TFDD repos: the number of feasible distinct 6-12-month relocatable windows given that repo's total history length in months (e.g. a repo with H months of usable history and a 6-month window has roughly H-6 distinct start-month positions, so state this arithmetic explicitly per repo and sum/report the combinatorial space size). State explicitly whether the reported 500 (or the original run's cited '60/40') shuffle draws were i.i.d. samples WITH or WITHOUT replacement from that space (read this from method.py's actual placebo-generation code, do not assume) and whether the same random seed reused across strata induces any dependence between the survivor and non-survivor shuffle sets. Derive the theoretical minimum achievable two-sided p-value given the placebo sample count k as 1/(k+1) (standard permutation-test resolution bound), and report it next to the actually-computed p-value so a reader can judge whether the reported p-value is bounded away from that floor or sitting on it (a p-value equal to the floor value is a red flag that more permutations are needed, not evidence of significance). Then RE-RUN the placebo test at a substantially larger budget -- target 2000 iterations per stratum if the small n=6 event corpus and its capped/cached DOA recomputation make this fast (state the actual wall-clock observed; if 2000 is infeasible within the time budget, fall back to the largest budget achieved within roughly 20 minutes of compute and report exactly what budget that was and why, rather than silently using fewer). Report the placebo p-value (and effect-size null-distribution mean/SD) at each of at least 3 budgets (e.g. original ~60/40, an intermediate step, and the final larger budget) in a convergence table, and state explicitly whether the qualitative conclusion (effect specific to the true pre-departure window vs. not) is stable across budgets or flips.

  (B) AVELINO ET AL. 66% TF=1 WILSON CI. Using n=315 (Avelino et al.'s reported total TFDD count) and the reported proportion 0.66 (208 of 315, computing the exact count as round(0.66*315) and stating that rounding explicitly since the paper does not give the raw numerator), compute a Wilson score 95% CI (not the normal-approximation Wald interval, which is unreliable near 0/1 and for the moderate n here -- use the standard Wilson formula: center = (phat + z^2/(2n)) / (1 + z^2/n), halfwidth = z*sqrt(phat*(1-phat)/n + z^2/(4n^2)) / (1 + z^2/n), z=1.959964 for 95%). Compute the SAME Wilson CI for this study's own TF=1 founder-TFDD fraction using this study's own n (the count of ALL TFDD events found in the 15-repo corpus, not just the founder-only subset of 6 -- pull both numbers from method_out.json's diagnostic fields) and report both CIs side by side in a small table with an explicit overlap/non-overlap determination (do not just eyeball it -- state the numeric bounds of both intervals and whether they intersect). Given the small denominator on this study's side, explicitly flag if the interval is very wide and caution against over-reading 'overlap' as validation when this study's own CI could contain almost any plausible fraction.

  (C) ALIAS-RESOLUTION SPOT-CHECK. Select 2-3 of the 15 corpus repos (prefer ones with the highest reported alias-collapse-rate variance or the ones contributing founder-only TFDD events, since those drive the headline numbers) and for each: use the aii-web-tools skill's web fetch/fetch_grep to pull the live GitHub repo's /graphs/contributors page or the repo's README/CONTRIBUTORS file and its top-committer list, and cross-reference the distinct author emails/logins the EXPERIMENT pipeline counted as 'distinct non-founder DOA file-owners' against what GitHub's own UI presents as distinct human contributors. Explicitly look for: (i) bot accounts (e.g. dependabot, github-actions[bot]) miscounted as human authority-holders, (ii) the same human appearing under 2+ emails/handles that the pipeline's alias-resolution did NOT merge (under-merging, which would inflate the diffusion score), and (iii) the reverse -- two distinct humans merged into one identity (over-merging, which would deflate it). Report per-repo: number of identities checked, number found to be bots, number found to be split identities of the same human, and whether correcting these would change that repo's founder-only-TFDD classification or diffusion score materially. State clearly this is a spot-check on 2-3 repos, not a full audit, and describe what fraction of the corpus this leaves unchecked.

  (D) FULL REPOSITORY TABLE. Parse full_data_out.json's per-repo records (one example per repo under the github_founder_departure_commits group) and full_method_out.json's per-repo TFDD/survival outputs, and emit ONE row per repo (all repos present in the dataset artifact, whatever the final count is -- verify it is 15 by counting live records rather than assuming the number from the dependency summary) with columns: repo full_name, primary language, stars, forks, total commit-history span in years, whether a TFDD was detected, whether it was founder-only (TF=1 at detachment), the pre-departure diffusion score (founder commit-share, distinct non-founder DOA-owner count) if applicable, and the 18-month post-TFDD survival grade (thriving/maintained/dormant/dead) if applicable. Cross-check every field against the two source JSON files exactly (no invented or rounded-from-memory values) and flag any repo where a field is missing/null in the source data rather than silently omitting the row.

  (E) SURVIVORSHIP-BIAS QUANTIFICATION AND DESIGN-FLAW ARGUMENT. Recompute directly from the EXPERIMENT/DATASET outputs: this corpus's TFDD incidence rate (TFDDs / total usable repos) and 18-month survival rate among TFDD repos, and place them next to Avelino et al.'s published 16.3% incidence and 40.6% survival (cite the exact source numbers/section from the ESEM 2019 paper via a fresh aii-web-tools fetch_grep against the arXiv PDF, do not rely on memory of the hypothesis text) with a formal statistical comparison (a two-proportion z-test or exact binomial test against Avelino et al.'s rate treated as the null, reporting the test statistic, p-value, and a plain-language direction/magnitude statement, e.g. 'this corpus's TFDD-survival rate is X percentage points higher, z=..., p=...'). Since no expanded or non-conditioned corpus exists among this artifact's dependencies (the DATASET artifact's ~104-repo candidate pipeline was checkpointed but not completed, and the artifact direction's re-run-on-expanded-corpus step is therefore not executable from the given dependencies), do NOT fabricate or simulate a second corpus -- instead write an explicit 'Residual Limitation' section documenting: the structural argument for why conditioning on present-day liveness necessarily biases toward survivors (a short formal statement: any sampling frame requiring a repo to be 'currently famous and still maintained' assigns zero sampling probability to the non-survivor stratum this study needs to observe fully, so incidence/survival estimates from it are not just imprecise but inconsistent estimators of the population quantities), the fact that this study's own evidence is 15 out of a 104-repo candidate list with the remainder blocked by the unauthenticated 60-req/hour GitHub API cap (quote the exact numbers from the DATASET artifact's summary), and a concrete, falsifiable prediction of what a valid non-conditioned corpus run through the same pipeline should show (e.g. 'incidence should approach Avelino et al.'s 16.3% and survival should approach 40.6% within the CI computed in part B') so a future GEN_DATASET/GEN_EXPERIMENT artifact with GITHUB_TOKEN access has a stated, checkable target rather than a vague aspiration.

  All five parts write into a single eval_out.json (plus mini/preview variants per aii-json skill conventions) with clearly named top-level keys per part (permutation_disclosure, tf1_ci_comparison, alias_spotcheck, repo_table, survivorship_bias_quantification) and a top-level overall_verdict summarizing, in 3-5 sentences, which reviewer gaps are now fully closed with data (A, B, D, E's quantification half) versus which remain structurally open pending a new corpus (E's second-frame comparison, explicitly NOT run here). Validate the final JSON against the eval_out schema via the aii-json skill before finishing, and check output file sizes against the aii-file-size-limit skill.
metrics_justification: >-
  These five checks target exactly the methodology-rigor gaps a careful reviewer would flag on the prior 15-repo pipeline
  result, and each closes a specific, nameable threat to validity rather than adding generic robustness noise: (A) a permutation
  p-value reported without its achievable resolution (1/(k+1)) or its sampling scheme (with/without replacement, dependence
  across strata) is uninterpretable -- a p-value of 0.025 from 40 draws is at the theoretical floor and means something different
  from the same number at 2000 draws, so disclosing the scheme and showing budget-convergence is the minimum bar for trusting
  the placebo/window-shuffle result that underlies the paper's construct-validity claim. (B) A bare 'our TF=1 rate looks similar
  to their 66%' claim without confidence intervals on BOTH sides is not a comparison at all, especially with this study's
  tiny n; the Wilson interval (rather than the Wald normal approximation) is the standard correct choice for a proportion
  with a moderate-to-small denominator and one anchored near neither 0 nor 1, and reporting both intervals turns an assertion
  into a falsifiable statistical statement. (C) The diffusion measurement's core claim (distinct non-founder DOA owners) is
  only as good as identity resolution; since the EXPERIMENT reported a suspicious 0.0-median alias-collapse-rate, a live spot-check
  against GitHub's actual contributor graph is the cheapest available external validity check on whether that diffusion count
  is inflated by bots or under-merged identities -- exactly the kind of concrete, checkable evidence a reviewer would ask
  for instead of trusting an internal QA metric produced by the same pipeline being validated. (D) An exact, complete repository
  table is table-stakes for reproducibility and lets a reader (or downstream paper-writing step) verify every headline number
  against raw per-repo facts rather than trusting aggregate statistics alone -- it also surfaces silently-dropped or null-field
  repos that aggregate summaries can hide. (E) The hypothesis's central claim is that the 15-repo corpus's deviation from
  Avelino et al.'s published rates is a SAMPLING-FRAME defect, not a power shortfall; formalizing that as a statistical test
  against the published null (rather than an eyeballed 53.3% vs 16.3% comparison) plus an explicit, honestly-scoped limitations
  statement about what remains unverified (since no second, non-conditioned corpus exists to run head-to-head) is what turns
  a plausible narrative into a defensible, appropriately-hedged scientific claim -- and prevents the paper from either overclaiming
  a resolved comparison or understating how much of the design-flaw argument is currently structural reasoning versus direct
  empirical contrast.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_ZuMis522AEPF
type: dataset
title: GitHub Founder-Departure Commit Corpus
summary: >-
  Built a real corpus of 15 well-known, well-documented open-source GitHub repositories (e.g. pallets/flask, BurntSushi/ripgrep,
  psf/black, Textualize/rich, httpie/cli, pyenv/pyenv, tiangolo/typer), each with full commit history obtained via `git clone`
  + `git log --numstat` (SHA, author name/email, ISO date, per-file insertions/deletions for every commit, newest-first, capped
  at 5,000 commits/repo with an explicit truncation flag) plus repo-level metadata from the GitHub REST API (stars, forks,
  primary language, license, created_at, pushed_at, open_issues, README excerpt). Each repo record also carries an empirically-computed
  `founder_signal`: the fraction of commits in the repo's first 365 days made by its single top-committing author email, and
  the top author's email. This directly operationalizes the plan's inclusion criterion (single-founder dominance >=70% of
  year-1 commits) without asserting it a priori -- it is measured from the real cloned git log. Repos span multiple languages
  (Python, Rust) and star bands (15k-72k stars in the current sample) and multi-year histories (6.6-16.4 years), giving enough
  post-founding history for an 18-month post-departure survival window. IMPORTANT SCOPE LIMITATION: this environment has no
  GITHUB_TOKEN, so the GitHub REST API is capped at 60 unauthenticated requests/hour (2 calls per repo: /repos/{full_name}
  and its /readme). This makes the plan's 150-250 repo target infeasible within the artifact time budget -- 15 repos were
  completed and checkpointed (12 in the final checkpoint snapshot, 15 repo-record files on disk) before the artifact needed
  to finalize; git clone itself (smart-HTTP) is NOT rate-limited, so every completed repo's commit history is complete and
  untruncated for its cap, only the TOTAL repo count is reduced. code/build_dataset.py and code/candidates.py contain a ~104-repo
  candidate list spanning Python/JS/Go/Ruby/Rust/C++/Java and a checkpointed, resumable pipeline (temp/checkpoint.json) that
  a downstream step can re-run with a GITHUB_TOKEN (raising the limit to 5,000 req/hour) to scale to the full 150-250 target
  without re-doing completed work. A HuggingFace candidate (kamalkishor1991/commit-messages-dataset, sampled commit diffs
  for commit-message generation) was evaluated and explicitly rejected as the primary source because it lacks per-repo lifecycle,
  author-identity-over-time, and per-file structure. data.py standardizes the corpus into the exp_sel_data_out.json schema:
  one dataset group `github_founder_departure_commits`, one example per repo, `input` = JSON-encoded {repo_metadata, founder_signal,
  truncated, commit_cap, commits[]}, `output` = derived label 'founder_dominant'/'not_founder_dominant' from the 0.7 year-1-share
  threshold, plus flat `metadata_*` fields (full_name, stars, language, history_years, n_commits, truncated, year1_top_author_share,
  task_type). Validated against the exp_sel_data_out schema (PASSED); full_data_out.json is 13.8MB (well under the 100MB limit),
  with mini_data_out.json and preview_data_out.json also produced.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
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

--- Dependency 2 ---
id: art_I5KoOp16hub5
type: experiment
title: Does authority spreading before founders leave keep projects alive?
summary: >-
  Reimplemented Avelino et al.'s (ESEM 2019) Degree-of-Authorship / Truck-Factor / Truck-Factor-Detachment-Departure (TFDD)
  pipeline end-to-end in method.py, run against the DATASET dependency's mined GitHub commit histories (15 usable repos with
  full per-file commit logs, out of 3427 raw records also containing an unrelated HuggingFace commit-message corpus that the
  loader correctly skips via a 'no_commits' filter). For each repo the pipeline: (1) resolves author aliases via normalized
  email/github-login matching and logs a per-repo alias-collapse-rate QA metric; (2) computes yearly cumulative-window DOA
  (Degree of Authorship) per file per author using Fritz et al.'s weights (FA=3.293, DL=1.098, AC=-1.017) as used by Avelino
  et al.; (3) derives the yearly greedy Truck-Factor set from primary DOA ownership; (4) detects Truck-Factor-Detachment-Departure
  events (a TF-set fully silent for 12 months) and isolates founder-only TFDDs (TF=1 and the sole departing developer is the
  repo's first human committer, with bulk-import first commits filtered per the Kalliamvakou et al. 2014 'perils of mining
  GitHub' heuristic of >80% of files touched within the first week); (5) computes a NEW pre-departure authority-diffusion
  trajectory over the 6-12 months before each TFDD -- founder commit-share and count of distinct non-founder DOA file-owners
  -- alongside Avelino et al.'s original at-TFDD snapshot covariates (developers/commits/files at detachment); (6) classifies
  18-month post-TFDD survival into Avelino's four-level active/inactive grades (thriving/maintained/dormant/dead) plus a binary
  survived flag; (7) runs a matched-pairs bootstrap comparison (nearest-neighbor matching on standardized log-stars/log-forks/log-contributors
  within language, comparing high- vs low-diffusion projects) with 10,000-resample 95% CIs; (8) fits BH-corrected logistic
  and ordinal (statsmodels OrderedModel) regressions of survival on diffusion predictors plus snapshot covariates, reporting
  standardized effect sizes comparable to Avelino et al.'s reported d=0.13 (files) / 0.25-0.26 (developers, commits); (9)
  runs a 500-iteration placebo/window-shuffle check that redraws the pre-departure window from elsewhere in project history
  and refits the regression, to test whether the true diffusion-window effect exceeds the null distribution of effects from
  arbitrary windows. All steps implement both the proposed authority-diffusion predictor AND Avelino et al.'s original snapshot-covariate
  baseline side-by-side in the same regression and matched-pairs machinery, so the two are directly comparable under identical
  data and identical statistical procedures -- baseline_predict and ourmethod_predict columns are both emitted per example.
  The run found n_repos_total=3427 raw dataset records (3409 filtered as non-repo commit-message rows lacking file-level structure;
  the dataset dependency's GitHub API rate limiting -- 60 unauthenticated requests/hour -- constrained the usable repo count
  to 15, well below the plan's 150-250 target), yielding n_founder_tfdd_events=6, which falls below the ~40 events the plan's
  own fallback_plan identifies as needed for a well-powered matched-pairs test; per that fallback plan this limitation is
  reported explicitly in the output metadata (extended_sample_used_TFle2 flag, doa_approximation_used flag, alias_qa block)
  rather than silently presented as adequately powered, and all regression/matched-pairs/placebo numbers in method_out.json
  should be read as a small-n pilot demonstrating the pipeline mechanics rather than a well-powered test of the founder-diffusion-predicts-survival
  hypothesis. A bug where the dataset dependency's example-wrapper format (repo records JSON-encoded inside an 'input' string
  field, per the exp_gen_sol_out schema) was not being unwrapped -- causing every repo to be misread as having zero commits
  -- was found and fixed during this run; the corrected loader now parses that wrapper and the pipeline runs end-to-end in
  ~90 seconds. Output method_out.json / full_method_out.json / mini_method_out.json / preview_method_out.json validate cleanly
  against the exp_gen_sol_out.json schema (0 errors) and are all under 9KB, far below the 100MB size limit. Downstream users
  (GEN_PAPER_TEXT) should present this as a methodology-validation / small-sample pilot result: the pipeline itself (DOA/TF/TFDD
  replication, diffusion-trajectory measurement, survival classification, matched-pairs + regression + placebo statistical
  machinery) is fully implemented and tested (smoke tests on synthetic hand-constructed repos, mini-run sanity checks, and
  the full corpus run all pass), but the headline finding is data-starved (n=6 events) due to upstream GitHub API rate limiting
  documented in the DATASET dependency's own metadata, not a pipeline defect.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
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

### [14] SYSTEM-USER prompt · 2026-08-20 20:24:12 UTC

```
<validation-feedback>
Attempt 1 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [15] SYSTEM-USER prompt · 2026-08-20 20:24:36 UTC

```
<validation-feedback>
Attempt 2 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [16] SYSTEM-USER prompt · 2026-08-20 20:24:50 UTC

```
<validation-feedback>
Attempt 3 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [17] SYSTEM-USER prompt · 2026-08-20 20:50:32 UTC

```
Check eval.py background run status (PID 434) and continue: verify eval_out.json exists, generate mini/preview via aii-json skill, check file sizes via aii-file-size-limit, pin pyproject.toml deps, and produce the final .terminal_claude_agent_struct_out.json matching schema.
```
