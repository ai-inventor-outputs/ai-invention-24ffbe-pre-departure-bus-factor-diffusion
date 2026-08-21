# gen_plan_experiment_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_plan`
> Run: `iter1_0b7b616dce39` — Does Pre-Departure Authority Diffusion Predict Open-Source Project Survival? A Unified-Corpus Retest with a Window-Boundary-Noise Control
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_experiment_1` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-08-21 15:38:19 UTC

```
model: claude-sonnet-5 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_plan/gen_plan_experiment_1
```

### [2] SYSTEM-USER prompt · 2026-08-21 15:38:27 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A plan generator (Step 3.2: GEN_PLAN in the invention loop)

You received the hypothesis, an artifact direction to elaborate, and dependency artifacts relevant to the plan.
Your job: elaborate this direction into a detailed, actionable plan for the executor agent.

Specific, actionable plan → valuable artifact. Vague plan → wasted execution.
</your_role>
</ai_inventor_context>

<artifact_type_info>
You are expanding an artifact direction of type: EXPERIMENT

EXPERIMENT
Run code to test hypotheses, implement methods, and collect empirical results.
Runtime: Python 3.12, UV (any pip package), isolated workspace, gradual scaling (mini → full data).
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Implement and run any code-based experiment, compare method vs baselines.
Deps: REQUIRED at least one DATASET | OPTIONAL RESEARCH for methodology guidance
</artifact_type_info>

<available_resources>
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

<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **SPEND BUDGET**: at most $10 USD of OpenRouter API calls for this artifact. Nothing outside your own code enforces this — the key you are given has no per-artifact cap — so it holds only if you track cumulative cost after every call and stop when you approach it. Budget the work up front: estimate the per-call cost and the number of calls BEFORE starting a sweep, not after it overruns. Exceeding it spends real money that the run cannot recover.
</software_constraints>
</available_resources>

<time_budget>

The experiment executor has 6h total (including writing code, debugging, testing, and fixing errors).

</time_budget>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape. Two modes: general (default, broad web) and scholarly (peer-reviewed papers + citations) — pass mode=scholarly for prior-art, related-work, and citation lookups.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<plan_guidelines>
You are expanding an artifact direction from the strategy into a detailed plan.
The artifact direction specifies what to do at a high level (type, objective, approach, dependencies).
Your job is to make it concrete and actionable as a detailed plan.
Use web research to look up technical details, verify feasibility, and find reference materials
that will make your plan more concrete and actionable for the executor.

GOOD PLANS:
- Make each component SPECIFIC and actionable (not vague platitudes)
- Consider both success AND failure scenarios
- Build on the approach in the artifact direction
- Add concrete details the executor needs

BAD PLANS:
- Vague hand-waving ("do research on X")
- Ignoring the approach in the artifact direction
- Missing critical details the executor needs
</plan_guidelines>

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

<hypothesis>
kind: hypothesis
title: Pre-Departure Bus-Factor Diffusion Predicts Post-Founder Project Survival
hypothesis: >-
  An open-source project's survival after its founder stops committing (a founder-only Truck Factor Developer Detachment,
  or TFDD, in Avelino et al.'s ESEM 2019 terminology) is determined less by the project's popularity or size at the moment
  of departure — which Avelino et al. already show is statistically indistinguishable between survivors and non-survivors
  at the TFDD snapshot (d=0.13-0.26) — and more by how diffused DOA-based commit/file authority already was among non-founder
  contributors in the 6-12 months BEFORE departure. Specifically, projects where the founder's share of authored commits had
  already fallen below ~50% and at least 2 non-founder contributors had independently reached primary DOA ownership on a file
  (not just submitted patches) prior to the founder's TFDD survive (measured via Avelino et al.'s own 18-month Active/Inactive
  recovery criterion) at a substantially higher rate than matched projects with equal stars/forks/contributor-count but where
  the founder still dominated authorship up to the point of departure. In other words, survival is predicted by a pre-departure
  'authority diffusion' trajectory that Avelino et al.'s published pipeline does not measure, not by the post-TFDD snapshot
  covariates their pipeline does.
motivation: >-
  The folk narrative around OSS abandonment treats founder departure as an exogenous shock whose outcome is explained after
  the fact by project popularity ('it was big enough to survive') or luck (a 'benevolent dictator' successor happened to appear).
  Avelino et al.'s full-text-verified ESEM 2019 results directly undercut the popularity explanation: at the TFDD snapshot
  itself, surviving and non-surviving projects show no meaningful difference in developers, commits, or files. That leaves
  a genuine open question their paper does not answer — if size doesn't predict survival at the moment of departure, what
  does? This hypothesis proposes that the missing signal is temporal rather than cross-sectional: it lives in the TREND of
  authority concentration in the run-up to departure, not in any single snapshot. If true, this gives foundations (e.g. Apache
  Incubator, NumFOCUS, Software Freedom Conservancy) an actionable, pre-departure-observable predictor — computable from Avelino
  et al.'s own published, validated DOA/TF pipeline run one time-window earlier — rather than only a post-hoc explanation
  of who happened to survive.
assumptions:
- >-
  Founder departure can be operationalized, following Avelino et al.'s validated Truck Factor Developer Detachment (TFDD)
  construct (ESEM 2019), as the point at which every developer in the project's Truck-Factor set (the minimal set of highest-Degree-of-Authorship
  contributors) has gone silent; Avelino et al. empirically selected a 1-year abandoner threshold as the least error-sensitive
  of five candidates they tested (harmonic-mean precision 0.66 vs 0.44-0.64 for the alternatives), which this study reuses
  rather than re-deriving
- >-
  Truck Factor / core-developer status can be computed per year with the Degree-of-Authorship (DOA) algorithm Avelino et al.
  use (also validated against 67 projects in their 2016 ICPC paper), operationalizing 'authority' as file-level primary ownership
  rather than raw commit count
- >-
  Projects included have at least 3 years of history after the identified departure point, so an 18-month post-departure survival
  window can be measured without right-censoring; Avelino et al.'s own dataset required only 2 years of history and required
  manually excluding 'perils of mining GitHub' artifacts (repos that lost history on migration, non-software repos, book/awesome-list
  repos) which this study must also filter
- >-
  Survival is operationalized as a graded outcome from post-departure activity, following Avelino et al.'s Active/Inactive
  state model (a project is Inactive once its full Truck-Factor set has detached, Active again once a new TF developer is
  attracted) rather than any formal declaration of abandonment, since Coelho & Valente (FSE 2017) found the large majority
  of failed projects never post such a declaration (only 76 of their 618 failed projects had an explicit README deprecation
  notice; the rest were identified purely from a >1-year commit silence)
- >-
  The founder's identity and the set of non-founder authority-holders can be disambiguated via the GitHub-API email-to-account
  mapping Avelino et al. used for alias resolution (median 11% of a project's contributors are aliases in their dataset),
  acknowledging their own noted limitation that this does not catch developers with multiple distinct GitHub accounts
investigation_approach: >-
  1. Assemble a corpus in the same spirit as Avelino et al.'s 1,932-project dataset (top-500-starred repos per language across
  6 languages, filtered for mining artifacts and <2-years history), but restricted to the single-founder subset needed here:
  repos with one clearly dominant original committer, sampled across popularity strata to avoid confounding by size. 2. For
  each repo, recompute yearly Truck Factor and TF-developer sets with the DOA algorithm exactly as Avelino et al. specify,
  and identify each project's FIRST TFDD event where the departing TF set is a single founder (TF=1 at detachment) — Avelino
  et al. report 66% of TFDDs in their corpus occur at TF=1, so this founder-only subset is a large, well-populated slice of
  their existing framework, not a rare edge case. 3. NEW measurement, not present in Avelino et al.: for the 6-12 months immediately
  preceding that TFDD, compute the founder's share of merged/authored commits and the count of distinct non-founder accounts
  that had already reached DOA-based file ownership on at least one file, i.e. an authority-diffusion TRAJECTORY leading up
  to the snapshot Avelino et al. only measure AT and AFTER the TFDD. 4. Compute the survival outcome using Avelino et al.'s
  own Active/Inactive/recovery definition (18-month post-TFDD activity, graded thriving/maintained/dormant/dead) so results
  are directly comparable to their reported 41% survival rate. 5. Fit a logistic/ordinal regression and a matched-pairs comparison
  (equal star/fork/contributor-count bucket, differing pre-TFDD authority-diffusion score) predicting survival from pre-departure
  diffusion, controlling for stars, forks, contributor count, language, and license — including the covariates Avelino et
  al. found NOT to differ between survivors and non-survivors at the TFDD snapshot itself (developers, commits, files — negligible-to-small
  effect sizes, d=0.13-0.26) to test whether the pre-departure trend outperforms those snapshot covariates. 6. Falsification
  check: shuffle which 6-12-month window is treated as 'pre-departure' within both survivor and non-survivor groups to confirm
  the effect is specific to the window immediately preceding TFDD and not an artifact of generally-active projects having
  generally-diffused authority throughout their history.
success_criteria: >-
  1. In the matched-pairs comparison (equal size/popularity bucket), founder-TFDD projects with pre-departure founder authorship-share
  below 50% AND >=2 independent non-founder DOA-file-owners survive at a rate at least 1.5x higher than matched projects where
  the founder retained >=80% authorship share up to departure, with a 95% CI that excludes 1x — a real lift over Avelino et
  al.'s unconditioned 41% baseline survival rate for TFDDs generally. 2. In the regression, the authority-diffusion predictors
  (founder authorship-share, distinct pre-departure DOA-owner count) remain statistically significant (p<0.05, Benjamini-Hochberg
  corrected, following Avelino et al.'s own multiple-comparison procedure) after controlling for stars, forks, and contributor
  count, and their standardized effect size exceeds that of the size/popularity covariates Avelino et al. found had only negligible-to-small
  effect (d=0.13 for files, d=0.25-0.26 for developers/commits) at the TFDD snapshot. 3. The placebo/shuffle check shows the
  effect is significantly weaker or absent when the 'pre-departure window' is randomly relocated within the project's history,
  supporting that it is specifically the pre-departure diffusion trajectory — not generally-active projects having generally-diffused
  authority throughout — doing the predictive work.
related_works:
- >-
  Avelino, Constantinou, Valente & Serebrenik, 'On the abandonment and survival of open source projects: An empirical investigation'
  (ESEM 2019, arXiv:1906.08058) — VERIFIED BY FULL-TEXT READ. Mines 1,932 popular GitHub repos, computes yearly Truck Factor
  via the DOA algorithm, and defines TFDD (Truck Factor Developer Detachment) plus an Active/Inactive survival model with
  a validated 1-year abandoner threshold. Reports 315 projects (16%) face a TFDD, 66% of TFDDs occur at TF=1 (single core
  developer), 128/315 (41%) survive their TFDD (usually via a single new TF developer, 86% of cases; newcomers specifically
  drove 48% of recoveries), and at the TFDD snapshot itself surviving vs non-surviving projects show NO meaningful difference
  in developers/commits/files (d=0.13-0.26, negligible-small) while surviving projects are significantly YOUNGER (1095 vs
  1460 days, p=3.4e-7). This is the direct empirical basis this hypothesis builds on and diverges from: Avelino et al. measure
  diffusion/recovery strictly AT and AFTER the TFDD snapshot ('did a new TF developer arrive afterward'), and explicitly do
  not analyze the pre-TFDD trend in authority concentration — their own snapshot-covariate null result (size doesn't predict
  survival) is what motivates testing whether a PRE-departure trajectory succeeds where the snapshot fails.
- >-
  Avelino, Ferreira, Valente et al., 'A novel approach for estimating Truck Factor' (ICPC 2016) — the DOA-based TF-estimation
  algorithm reused verbatim by the ESEM 2019 paper and by this proposal; validated against a manual survey of 67 GitHub projects,
  but the original paper only computes TF as a single-time-point risk score and does not connect it longitudinally to post-departure
  survival outcomes.
- >-
  Coelho & Valente, 'Why Modern Open Source Projects Fail' (FSE 2017, arXiv:1707.02327) — VERIFIED BY FULL-TEXT READ. Surveys
  maintainers of 104 curated failed GitHub projects (out of 618 identified failures among the top-5,000 starred repos) and
  reports nine failure reasons grouped into team (lack of time 18, lack of interest 18, conflicts 3), project (obsolete 20,
  outdated tech 14, low maintainability 7), and environment (usurped by competitor 27, legal 2, acquisition 1) causes; also
  finds failed projects adopt far fewer best-practice maintenance signals than top projects (contributing guidelines: 16%
  vs 72%, large effect; CI: 27% vs 68%, medium effect). This is single-maintainer self-reported ABANDONMENT (why did YOU stop),
  a different unit and mechanism from this hypothesis's multi-contributor SUCCESSION question (did authority already exist
  elsewhere before the founder left); it corroborates that pre-existing maintenance-practice signals (correlates of authority
  diffusion, e.g. contributing guidelines) are already known to associate with failure risk, but does not test a specific
  pre-departure diffusion metric or timeline.
- >-
  Zhou & Mockus and related individual-contributor-turnover-prediction literature — models WHICH developer will leave next,
  a related but distinct outcome from this hypothesis's PROJECT-level survival question conditioned on the founder specifically
  having already left.
inspiration: >-
  The inspiration is an analogy to organizational succession research outside software: family businesses and founder-led
  companies are known to survive founder exit better when authority was already delegated to a management team beforehand,
  rather than concentrated with the founder until the moment of transition ('planned succession' vs 'crisis succession').
  Reading Avelino et al.'s full ESEM 2019 paper sharpened this: they build exactly the TFDD/survival measurement machinery
  needed, but report that at the moment of detachment, surviving and non-surviving projects look statistically indistinguishable
  on size (developers, commits, files) — a genuine null result for the 'was it big enough' folk explanation. That null is
  the opening for this hypothesis: if a SNAPSHOT at departure carries no signal, the signal may instead live in the TREND
  of authority concentration in the months leading up to it — not 'how many people could keep this alive right now,' but 'was
  authority already flowing to others before it had to.' This shift from a snapshot metric to a trajectory-of-decentralization
  metric is directly testable by re-running Avelino et al.'s own DOA/TF pipeline one window earlier in time.
terms:
- term: Truck Factor Developer Detachment (TFDD)
  definition: >-
    Avelino et al.'s (ESEM 2019) term for the event at which every developer in a project's current Truck-Factor set has gone
    silent for at least the validated 1-year abandoner threshold; this hypothesis's 'founder departure point' is the specific
    subset of TFDDs where the detaching TF set has size 1 (a single founder), which Avelino et al. report as 66% of all observed
    TFDDs.
- term: Degree of Authorship (DOA)
  definition: >-
    The file-level expertise metric (Fritz et al., reused by Avelino et al.'s TF algorithm) combining whether a developer
    created a file and how many of its subsequent changes are theirs relative to others; a developer is a file's primary author,
    and thus a candidate Truck-Factor / authority holder, when their DOA is highest among that file's contributors.
- term: Pre-departure authority diffusion
  definition: >-
    The degree to which DOA-based file ownership and authored-commit share had already shifted away from the founder to other
    contributors during the 6-12 months immediately before the founder's TFDD, measured as (a) the founder's share of authored/merged
    commits and (b) the count of distinct non-founder accounts that had already reached primary DOA ownership on at least
    one file in that window — a trajectory measurement Avelino et al.'s published methodology does not compute, since their
    TF/TFDD pipeline is evaluated only at and after the detachment point.
- term: Truck factor / bus factor
  definition: >-
    A classical software-engineering risk metric (Avelino et al. 2016 ICPC) estimating the minimal set of developers whose
    combined loss would put a project in serious trouble, computed via DOA at a single point in time; used here as a validated
    static baseline contrasted with the dynamic pre-departure trajectory this hypothesis targets.
- term: Post-departure survival
  definition: >-
    Following Avelino et al.'s Active/Inactive model: whether a project transitions back to Active (attracts a new TF developer)
    and shows non-trivial commit/release activity persisting at least 18 months after the founder's TFDD, rather than any
    formal abandonment announcement — consistent with Coelho & Valente's finding that most failed projects (542 of 618 in
    their sample) never post an explicit deprecation notice and must be identified from commit silence instead.
- term: Matched-pairs comparison
  definition: >-
    A study design that pairs founder-TFDD projects with similar confounding characteristics (stars, forks, total contributor
    count, language ecosystem, license type) but differing pre-departure authority-diffusion scores, isolating the diffusion
    trajectory's association with survival from the effect of raw project size or popularity — the latter of which Avelino
    et al. already show has negligible-to-small effect (d=0.13-0.26) at the TFDD snapshot itself.
summary: >-
  Whether an open-source project survives its founder stepping away is predicted not by its popularity or contributor count
  at the moment of departure — Avelino et al. (ESEM 2019) show these are statistically indistinguishable between survivors
  and non-survivors at the TFDD snapshot itself — but by whether commit/file authority had already diffused away from the
  founder to at least two other independent contributors in the 6-12 months BEFORE that departure. This reframes truck factor
  from Avelino et al.'s validated but purely at/after-the-fact snapshot metric into a leading, longitudinal 'authority diffusion
  trajectory' signal, directly testable by re-running their own published DOA/TF/TFDD pipeline one time-window earlier, and
  offers foundations an actionable, pre-departure-observable predictor rather than a post-hoc explanation.
</hypothesis>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: experiment_iter1_dir3
type: experiment
objective: >-
  Compute the pre-departure authority-diffusion trajectory metric for every founder-TFDD repo in the dataset, score post-TFDD
  survival per Avelino et al.'s Active/Inactive/recovery model, and test whether diffusion predicts survival better than snapshot
  size/popularity covariates via (1) an ordinal/logistic regression with Benjamini-Hochberg-corrected coefficients and standardized-effect-size
  comparison against stars/forks/contributor-count, (2) a matched-pairs comparison stratified by size bucket contrasting founder-share<50%-plus->=2-DOA-owners
  projects against founder-share>=80% projects, and (3) the pre-registered falsification check that randomly relocates the
  6-12-month 'pre-departure' window within each project's own history to confirm the effect is specific to the true pre-TFDD
  window and not a general-activity artifact.
approach: >-
  For each dataset repo, from the 6-12 months immediately preceding its founder-only TFDD compute: founder's share of authored/merged
  commits, and the count of distinct non-founder accounts that had already reached top-DOA (primary ownership) on at least
  one file in that window. Fit (a) a logistic regression predicting binary survival and an ordinal regression predicting the
  graded thriving/maintained/dormant/dead outcome, with diffusion predictors plus stars/forks/contributor-count/language/license
  as controls, reporting standardized coefficients and BH-corrected p-values; (b) bucket repos into size-matched pairs/strata
  (approximate nearest-neighbor matching on log-stars/log-forks/contributor-count) and compute the survival-rate ratio between
  high-diffusion and low-diffusion projects with a bootstrap 95% CI; (c) rerun both analyses 500-1000 times with the pre-departure
  window relocated to a uniformly random point in each project's pre-TFDD history (same window length) to build a null distribution
  and report where the true-window effect falls relative to it. Report all three results against Avelino et al.'s published
  41% baseline TFDD survival rate and their d=0.13-0.26 snapshot effect sizes as reference points.
depends_on: []
</artifact_direction>



<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results
</artifact_executor_scope>

<artifact_planning_rules>
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for experiment artifacts:
  - gpu: 1x NVIDIA RTX A4500, 20GB VRAM, 7 vCPUs, 29GB RAM — ML training, CUDA, large models (fallback: GPUs cheap→expensive: 2000 Ada → A4000 → 4000 Ada → L4 → 4090 → 5090)
  - cpu_heavy: 4 vCPUs, 32GB RAM — large datasets, memory-intensive processing (fallback: CPUs cheap→expensive, then GPU hosts cheap→expensive (all ≥32GB RAM))

Set runpod_compute_profile to one of these exact tier names.
</compute_profiles>
GOOD PLANS: specific, actionable, consider failure scenarios, build on the suggested approach.
BAD PLANS: vague hand-waving, ignoring the suggested approach, missing critical executor details.
</instructions><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "description": "Plan for an EXPERIMENT artifact.",
  "properties": {
    "title": {
      "description": "Plan title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Brief summary",
      "title": "Summary",
      "type": "string"
    },
    "runpod_compute_profile": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "cpu_light",
      "description": "Compute tier for execution \u2014 pick from the available profiles list (e.g., 'gpu', 'cpu_heavy', 'cpu_light'). Only used in RunPod mode.",
      "title": "Runpod Compute Profile"
    },
    "implementation_pseudocode": {
      "description": "High-level pseudocode for the experiment implementation",
      "title": "Implementation Pseudocode",
      "type": "string"
    },
    "fallback_plan": {
      "description": "What to do if the primary approach fails - alternative methods, simplified versions",
      "title": "Fallback Plan",
      "type": "string"
    },
    "testing_plan": {
      "description": "How to validate the experiment works: start with small/fast tests, look for confirmation signals before running full-scale experiments",
      "title": "Testing Plan",
      "type": "string"
    }
  },
  "required": [
    "title",
    "implementation_pseudocode",
    "fallback_plan",
    "testing_plan"
  ],
  "title": "ExperimentPlan",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [3] HUMAN-USER prompt · 2026-08-21 15:38:27 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [4] TOOL CALL — Write · 2026-08-21 15:39:55 UTC

```
File: /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_plan/gen_plan_experiment_1/.terminal_claude_agent_struct_out.json

{
  "title": "Does Authority Diffusion Before Founder Exit Predict Survival",
  "summary": "Recompute Avelino et al.'s (ESEM 2019) DOA/Truck-Factor/TFDD pipeline on GitHub repos, add a NEW pre-departure (6-12 months before TFDD) authority-diffusion measurement (founder commit-share, count of independent non-founder DOA file-owners), score 18-month post-TFDD survival with their Active/Inactive/recovery model, and test via regression + matched-pairs + window-shuffle placebo whether the pre-departure trajectory predicts survival better than the snapshot size/popularity covariates their paper showed were null (d=0.13-0.26).",
  "runpod_compute_profile": "cpu_heavy",
  "implementation_pseudocode": "# === STAGE 0: Setup & repo selection (depends on DATASET artifact of GitHub repo git histories) ===\n# This EXPERIMENT depends on a DATASET artifact providing cloned/clonable git histories\n# (or pre-extracted commit/file-change logs) for a sample of popular GitHub repos across\n# multiple languages, analogous to Avelino et al.'s 1,932-repo corpus (top-starred repos,\n# 6 languages: Java, Python, JavaScript, C++, Ruby, PHP or similar). Load that dataset's\n# manifest (repo_id, clone_url_or_local_path, stars, forks, contributor_count, language,\n# license, first_commit_date, last_commit_date).\n#\n# FILTER (mirrors Avelino et al. 'perils of mining GitHub' exclusions):\n#   - drop repos with < 2 years of commit history (need room for pre-TFDD window + TFDD +\n#     18mo post-TFDD survival window without right-censoring => require >= 3 yrs total, per\n#     the hypothesis's own assumption)\n#   - drop non-software repos (awesome-lists, book/doc repos): heuristic filter on file\n#     extensions (>= 60% of tracked files must have a recognized source-code extension for\n#     the repo's declared language) + repo-name/description regex for 'awesome-', 'book',\n#     'course', 'interview-questions' etc.\n#   - drop repos with obvious history-loss artifacts (first commit timestamp suspiciously\n#     dense/batched, i.e. > 50% of a repo's commits sharing the exact same author-date\n#     within a 60-second window -- signature of a squashed/re-imported history)\n# LOG every exclusion with reason and count so the executor can report a CONSORT-style\n# filtering table in the output JSON.\n\n# === STAGE 1: Build per-repo commit/file-change event log ===\nfor repo in filtered_repos:\n    events = extract_commit_log(repo)  # (commit_sha, author_email, author_date, files_touched[])\n    resolve_author_aliases(events)     # merge same-person accounts via GitHub-API noreply-email\n                                        # pattern (id+username@users.noreply.github.com) and by\n                                        # exact-name-match fallback when API email lookup fails;\n                                        # log alias-merge rate per repo (Avelino et al. median 11%)\n    events = sort_by(author_date)\n\n# === STAGE 2: Yearly DOA + Truck Factor (Avelino et al. 2016 ICPC algorithm, reused verbatim) ===\n# DOA(a, f) = 3.293 + 1.098*FA(a,f) - 0.164*ln(1+DL(a,f)) + 0.321*ln(1+AC(a,f))\n#   FA(a,f)  = 1 if a authored file f's FIRST commit, else 0\n#   AC(a,f)  = count of a's commits touching f (as of the snapshot date)\n#   DL(a,f)  = number of a's OWN commits to f that happened after a's LAST commit to f\n#              minus... (verify exact DL definition against Fritz et al. 2014 / Avelino 2016\n#              ICPC paper text at snapshot time -- executor MUST fetch and fetch_grep the ICPC\n#              2016 paper (arXiv or ACM DL) for the precise DL formula before implementing;\n#              do not guess it from memory)\n# For each repo, for each MONTHLY (not just yearly -- we need finer granularity to locate the\n# founder-only TFDD month and the 6-12mo pre-window precisely) snapshot date:\n#   - compute DOA(a,f) for every (author, file) pair using only commits with author_date <= snapshot\n#   - primary_owner(f, snapshot) = argmax_a DOA(a,f) restricted to top-DOA holder\n#   - TF(snapshot) = greedily remove authors (highest total number of files they are\n#     primary_owner of) one at a time until < 50% of repo's files have a remaining primary\n#     owner with DOA above the Avelino DOA-authorship threshold (>= 3.293, i.e. FA=1 baseline);\n#     TF = number of authors removed to cross that threshold\n#   - TF_developer_set(snapshot) = the set of authors removed in that greedy process\n\n# === STAGE 3: Identify each repo's founder & first founder-only TFDD ===\nfor repo in repos_with_doa_computed:\n    founder = author of repo's very first commit (or first N=3 commits if the true first\n              commit is a scaffolding/README-only commit -- use first commit with >=1\n              source file changed)\n    # TFDD = point at which every developer in the CURRENT TF_developer_set has gone silent\n    # (no commits) for >= 1 year (Avelino et al.'s empirically-selected best threshold,\n    # harmonic-mean precision 0.66). Scan monthly snapshots forward in time; a TFDD occurs\n    # at month m if TF_developer_set(m) all have zero commits in [m, m+12mo).\n    tfdd_events = detect_tfdd_events(repo)  # list of (month, tf_developer_set_at_detachment)\n    founder_only_tfdds = [e for e in tfdd_events if e.tf_developer_set == {founder} and\n                           founder in e.tf_developer_set and len(e.tf_developer_set) == 1]\n    if not founder_only_tfdds: skip repo  # not in the target subset (~66% of TFDDs are TF=1\n                                            # per Avelino et al., so expect most founder-led\n                                            # single-TF-dev repos to qualify -- but ALSO require\n                                            # founder to literally BE that lone TF developer,\n                                            # which is a stricter subset the plan must track)\n    first_founder_tfdd = min(founder_only_tfdds, key=lambda e: e.month)\n    # require >= 12 months of history BEFORE this TFDD (for the pre-window) and >= 18 months\n    # AFTER it (for survival scoring) -- else skip (right/left-censored)\n\n# === STAGE 4: NEW measurement -- pre-departure authority-diffusion trajectory ===\nfor repo in repos_with_founder_tfdd:\n    tfdd_month = first_founder_tfdd.month\n    window = [tfdd_month - 12mo, tfdd_month - 6mo]   # the 6-12-month PRE-departure window\n    commits_in_window = events filtered to author_date in window\n    founder_share = count(commits_in_window where author==founder) / count(commits_in_window)\n    # distinct non-founder DOA-file-owners reached DURING the window: for each month-end\n    # snapshot INSIDE the window, recompute primary_owner(f, snapshot) for all files touched\n    # up to that snapshot; collect the set of non-founder authors who are primary_owner of\n    # >= 1 file at ANY snapshot inside the window (use the running DOA state already computed\n    # in Stage 2, just re-slice it to the window's snapshot dates -- do NOT recompute from\n    # scratch, reuse memoized per-snapshot DOA tables for efficiency)\n    n_doa_owners = len(distinct non-founder primary owners across window snapshots)\n    diffusion_score = {founder_share, n_doa_owners}  # primary predictors\n\n# === STAGE 5: Survival outcome (Avelino et al.'s Active/Inactive/recovery model) ===\nfor repo in repos_with_diffusion_score:\n    post = events filtered to author_date in [tfdd_month, tfdd_month + 18mo]\n    # Active/Inactive state machine: repo is Inactive from tfdd_month until a NEW developer\n    # (not in the departed TF set) attains TF-developer status (joins the current\n    # TF_developer_set at some post-TFDD monthly snapshot) -- that event flips it back Active.\n    recovered = any(post-TFDD snapshot where a new author is in TF_developer_set)\n    # graded outcome (thriving/maintained/dormant/dead) -- define via post-TFDD commit\n    # velocity relative to pre-TFDD baseline, using quartile cut points the executor derives\n    # empirically from the corpus's own post-TFDD commit-count distribution (report the exact\n    # cutpoints used, since Avelino et al.'s paper does not give exact numeric thresholds for\n    # the 4 labels -- executor should fetch_grep the ESEM 2019 paper for their operational\n    # definition of the 4 states before inventing one from scratch)\n    binary_survival = recovered  # matches Avelino et al.'s binary survive/not-survive stat\n\n# === STAGE 6: Confound controls ===\nfor repo: controls = {log_stars, log_forks, contributor_count, language, license,\n                       developers_at_tfdd, commits_at_tfdd, files_at_tfdd}  # the snapshot\n                       # covariates Avelino et al. found null (d=0.13-0.26) -- MUST be\n                       # recomputed here identically to compare standardized effect sizes\n\n# === STAGE 7: Analysis (a) regression ===\nX = [founder_share, n_doa_owners, log_stars, log_forks, contributor_count,\n     developers_at_tfdd, commits_at_tfdd, files_at_tfdd] + language/license one-hot\nlogit_model = sm.Logit(binary_survival, standardize(X)).fit()          # statsmodels\nordinal_model = statsmodels.miscmodels.ordinal_model.OrderedModel(\n                    graded_outcome, standardize(X), distr='logit').fit()\nBH_correct(p_values_of_all_coefficients)  # statsmodels.stats.multitest.multipletests, method='fdr_bh'\nreport: standardized_coef, BH_p, compare |coef(founder_share)|, |coef(n_doa_owners)| vs\n        |coef(log_stars)|, |coef(developers_at_tfdd)| etc.\n\n# === STAGE 8: Analysis (b) matched-pairs / stratified comparison ===\nbuckets = stratify_by(log_stars_decile, log_forks_decile, contributor_count_bucket)\nhigh_diffusion = repos where founder_share < 0.50 AND n_doa_owners >= 2\nlow_diffusion  = repos where founder_share >= 0.80\nfor each bucket: pair high_diffusion repos to low_diffusion repos via nearest-neighbor on\n                 (log_stars, log_forks, contributor_count) using sklearn NearestNeighbors\n                 or scipy cKDTree, caliper = 0.2 * pooled std of matching covariates\nsurvival_rate_ratio = mean(binary_survival | high_diffusion, matched) / \n                       mean(binary_survival | low_diffusion, matched)\nbootstrap_CI = bootstrap(survival_rate_ratio, n_resamples=10000, method='percentile')\nreport ratio, 95% CI, compare against Avelino et al.'s unconditioned 41% baseline\n\n# === STAGE 9: Falsification / placebo check ===\nnull_ratios = []\nfor trial in range(1000):\n    for repo: relocate window to a uniformly random start month in\n              [first_commit_date, tfdd_month - window_length - 1mo]  # same length, must stay\n              strictly before the TRUE window's start to avoid leakage; recompute\n              founder_share_null, n_doa_owners_null using the SAME memoized per-snapshot DOA\n              tables from Stage 2 (cheap re-slice, no recomputation)\n    rerun analysis (a) and (b) with the null-window predictors\n    null_ratios.append(placebo_survival_rate_ratio)\nreport: true_effect_percentile_in_null_distribution, empirical p-value =\n        (1 + sum(null_ratios >= true_ratio)) / (1 + len(null_ratios))\n\n# === STAGE 10: Assemble method_out.json ===\noutput = {\n  'corpus_stats': {n_repos_input, n_repos_after_filters, n_founder_only_tfdds, exclusion_table},\n  'baseline_replication': {tfdd_rate, survival_rate, snapshot_effect_sizes},  # sanity check\n                                                                              # against Avelino\n                                                                              # et al.'s reported\n                                                                              # 16% TFDD rate /\n                                                                              # 41% survival / d\n  'regression_results': {...},\n  'matched_pairs_results': {...},\n  'placebo_results': {...},\n  'success_criteria_verdict': {criterion_1_pass_bool, criterion_2_pass_bool,\n                                criterion_3_pass_bool, notes}\n}",
  "fallback_plan": "Layer the fallbacks by what breaks first, from cheapest degradation to most fundamental: (1) FULL git clones too slow/large -- if the DATASET artifact only supplies shallow clones or pre-extracted commit logs without full blob history, that's fine: DOA only needs (author, file, commit_date) triples, not blob contents, so nothing in the pipeline actually requires full clones; explicitly do NOT re-clone anything, use whatever the dataset provides. (2) Corpus too small after filtering (e.g., <40-50 founder-only-TFDD repos survive the >=3-year-history + founder-only-TF=1 filters) -- relax the TF=1-at-departure requirement to TF<=2 with founder in the departing set and note the deviation explicitly in the output, since Avelino et al. themselves report 66% of TFDDs are TF=1 so a large corpus should still clear the stricter filter; if it still doesn't, reduce required post-TFDD survival window from 18 to 12 months (report both) rather than dropping repos, and flag this as a limitation rather than silently changing the headline metric. (3) DOA/TF computation too slow at monthly granularity across the full corpus -- switch from monthly to quarterly snapshots for Stage 2's running DOA state (this is the compute-heavy step: O(commits x files) per snapshot); the pre-departure window (6-12mo) and TFDD detection can tolerate quarterly resolution with a documented +/-1.5 month fuzz on the TFDD date, which does not materially change founder_share or n_doa_owners since both are already window-aggregate statistics. (4) statsmodels' OrderedModel fails to converge on the graded 4-level outcome (common with small/imbalanced strata) -- fall back to the binary logistic regression only for the primary claim (success criterion 2 only requires the diffusion predictors' significance, which the binary model alone can establish) and report the ordinal model as exploratory/best-effort with a convergence-failure caveat rather than blocking the whole artifact on it. (5) Matched-pairs bucket has too few pairs per stratum for a stable bootstrap CI (e.g., <10 pairs in the high-diffusion vs low-diffusion contrast within a size bucket) -- pool across size buckets and instead include the matching covariates (log_stars, log_forks, contributor_count) as regression adjustors in a single pooled matched-set analysis (essentially collapsing (a) and (b) into one covariate-adjusted comparison), clearly labeled as a fallback deviation from the pre-registered stratified design in success_criteria_verdict.notes. (6) If the DATASET artifact this experiment depends on does not actually provide enough repos with the founder-identifiable-first-commit property (e.g., many repos were imported from an external VCS with no clean initial commit) -- restrict founder identification to repos where the first commit's author authored >= 3 of the first 5 commits (a robustness check against a single miscategorized scaffolding commit), and report the fraction of repos excluded for unidentifiable founders as part of the exclusion table so the reader can judge the founder-only subset's representativeness. Under no circumstances should the executor fabricate or downsample results to hit the success-criteria thresholds -- report a null/negative result plainly if the corpus and analysis genuinely produce one; a rigorous null result on this question is itself a valid, reportable outcome given Avelino et al.'s own snapshot-null precedent.",
  "testing_plan": "1. UNIT-TEST DOA/TF logic on a synthetic 3-file, 4-author toy repo with hand-computed expected DOA values and a known TF set BEFORE running on any real data -- construct commit sequences where the expected primary owner, TF size, and TFDD timing are unambiguous by hand-derivation, and assert the code reproduces them exactly. This catches formula/off-by-one errors cheaply since the full DOA formula (particularly the DL term) must be verified against the ICPC 2016 paper text rather than guessed. 2. SMOKE TEST on 3-5 real, well-known single-founder repos with a documented founder departure the executor can sanity-check by eye (e.g., search for OSS projects with public 'founder handed off maintenance' blog posts/README history) -- confirm the pipeline's detected TFDD month is within a few months of the publicly known handoff date, and that the pre-TFDD founder_share trend direction (declining vs not) matches what a manual `git shortlog` inspection of that repo's commit history shows for the year before handoff. 3. BASELINE-REPLICATION CHECK on the full filtered corpus before running the NEW diffusion analysis: verify the pipeline's own aggregate stats are in the right ballpark against Avelino et al.'s published numbers -- TFDD rate should land near their 16% (not required to match exactly since the corpus differs, but order-of-magnitude and general directionality, e.g. TFDD rate should not come out as 90% or 1%, would indicate a pipeline bug), TF=1-at-departure share near their 66%, and overall post-TFDD binary survival rate near their 41% -- treat large deviations (e.g., >2x off) as a signal to debug the TFDD-detection or survival-scoring logic before trusting the new diffusion results. Also directly recompute the size/popularity snapshot effect sizes (developers/commits/files at TFDD, survivors vs non-survivors) and confirm they replicate as negligible-to-small (d roughly in the 0.1-0.3 range, same sign direction) as reported in the ESEM 2019 paper -- this is the load-bearing sanity check, since the entire hypothesis is that the NEW pre-departure signal succeeds precisely where this snapshot signal is known to fail; if the replication check itself produces a strong snapshot effect where Avelino et al. found none, that indicates a corpus-construction or measurement discrepancy needing resolution before proceeding to the novel analysis. 4. SCALE GRADUALLY: run the full pipeline (Stages 1-6) on a 20-30 repo mini-sample first, inspect the diffusion-score distribution and survival labels by hand for a handful of cases, confirm nothing is degenerate (e.g., founder_share always exactly 0 or 1, n_doa_owners always 0) before scaling to the full corpus and before launching the 500-1000-iteration placebo loop, which is the single most expensive step and should only run once Stages 1-8 are validated end-to-end on the mini-sample. 5. Track and report cumulative OpenRouter spend if any LLM calls are used for repo/language filtering heuristics (should be $0 or near-$0 for this artifact -- the entire pipeline is deterministic git-log analysis and statistics, not LLM-driven; if the executor finds itself needing an LLM call anywhere in this pipeline, that is a signal the approach has drifted from what was planned and should be reconsidered)."
}
```

### [5] TOOL RESULT — Write · 2026-08-21 15:39:55 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_plan/gen_plan_experiment_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Does Authority Diffusion Before Founder Exit Predict Survival\",\n  \"summary\": \"Recompute Avelino et al.'s (ESEM 2019) DOA/Truck-Factor/TFDD pipeline on GitHub repos, add a NEW pre-departure (6-12 months before TFDD) authority-diffusion measurement (founder commit-share, count of independent non-founder DOA file-owners), score 18-month post-TFDD survival with their Active/Inactive/recovery model, and test via regression + matched-pairs + window-shuffle placebo whether the pre-departure trajectory predicts survival better than the snapshot size/popularity covariates their paper showed were null (d=0.13-0.26).\",\n  \"runpod_compute_profile\": \"cpu_heavy\",\n  \"implementation_pseudocode\": \"# === STAGE 0: Setup & repo selection (depends on DATASET artifact of GitHub repo git histories) ===\\n# This EXPERIMENT depends on a DATASET artifact providing cloned/clonable git histories\\n# (or pre-extracted commit/file-change logs) for a sample of popular GitHub repos across\\n# multiple languages, analogous to Avelino et al.'s 1,932-repo corpus (top-starred repos,\\n# 6 languages: Java, Python, JavaScript, C++, Ruby, PHP or similar). Load that dataset's\\n# manifest (repo_id, clone_url_or_local_path, stars, forks, contributor_count, language,\\n# license, first_commit_date, last_commit_date).\\n#\\n# FILTER (mirrors Avelino et al. 'perils of mining GitHub' exclusions):\\n#   - drop repos with < 2 years of commit history (need room for pre-TFDD window + TFDD +\\n#     18mo post-TFDD survival window without right-censoring => require >= 3 yrs total, per\\n#     the hypothesis's own assumption)\\n#   - drop non-software repos (awesome-lists, book/doc repos): heuristic filter on file\\n#     extensions (>= 60% of tracked files must have a recognized source-code extension for\\n#     the repo's declared language) + repo-name/description regex for 'awesome-', 'book',\\n#     'course', 'interview-questions' etc.\\n#   - drop repos with obvious history-loss artifacts (first commit timestamp suspiciously\\n#     dense/batched, i.e. > 50% of a repo's commits sharing the exact same author-date\\n#     within a 60-second window -- signature of a squashed/re-imported history)\\n# LOG every exclusion with reason and count so the executor can report a CONSORT-style\\n# filtering table in the output JSON.\\n\\n# === STAGE 1: Build per-repo commit/file-change event log ===\\nfor repo in filtered_repos:\\n    events = extract_commit_log(repo)  # (commit_sha, author_email, author_date, files_touched[])\\n    resolve_author_aliases(events)     # merge same-person accounts via GitHub-API noreply-email\\n                                        # pattern (id+username@users.noreply.github.com) and by\\n                                        # exact-name-match fallback when API email lookup fails;\\n                                        # log alias-merge rate per repo (Avelino et al. median 11%)\\n    events = sort_by(author_date)\\n\\n# === STAGE 2: Yearly DOA + Truck Factor (Avelino et al. 2016 ICPC algorithm, reused verbatim) ===\\n# DOA(a, f) = 3.293 + 1.098*FA(a,f) - 0.164*ln(1+DL(a,f)) + 0.321*ln(1+AC(a,f))\\n#   FA(a,f)  = 1 if a authored file f's FIRST commit, else 0\\n#   AC(a,f)  = count of a's commits touching f (as of the snapshot date)\\n#   DL(a,f)  = number of a's OWN commits to f that happened after a's LAST commit to f\\n#              minus... (verify exact DL definition against Fritz et al. 2014 / Avelino 2016\\n#              ICPC paper text at snapshot time -- executor MUST fetch and fetch_grep the ICPC\\n#              2016 paper (arXiv or ACM DL) for the precise DL formula before implementing;\\n#              do not guess it from memory)\\n# For each repo, for each MONTHLY (not just yearly -- we need finer granularity to locate the\\n# founder-only TFDD month and the 6-12mo pre-window precisely) snapshot date:\\n#   - compute DOA(a,f) for every (author, file) pair using only commits with author_date <= snapshot\\n#   - primary_owner(f, snapshot) = argmax_a DOA(a,f) restricted to top-DOA holder\\n#   - TF(snapshot) = greedily remove authors (highest total number of files they are\\n#     primary_owner of) one at a time until < 50% of repo's files have a remaining primary\\n#     owner with DOA above the Avelino DOA-authorship threshold (>= 3.293, i.e. FA=1 baseline);\\n#     TF = number of authors removed to cross that threshold\\n#   - TF_developer_set(snapshot) = the set of authors removed in that greedy process\\n\\n# === STAGE 3: Identify each repo's founder & first founder-only TFDD ===\\nfor repo in repos_with_doa_computed:\\n    founder = author of repo's very first commit (or first N=3 commits if the true first\\n              commit is a scaffolding/README-only commit -- use first commit with >=1\\n              source file changed)\\n    # TFDD = point at which every developer in the CURRENT TF_developer_set has gone silent\\n    # (no commits) for >= 1 year (Avelino et al.'s empirically-selected best threshold,\\n    # harmonic-mean precision 0.66). Scan monthly snapshots forward in time; a TFDD occurs\\n    # at month m if TF_developer_set(m) all have zero commits in [m, m+12mo).\\n    tfdd_events = detect_tfdd_events(repo)  # list of (month, tf_developer_set_at_detachment)\\n    founder_only_tfdds = [e for e in tfdd_events if e.tf_developer_set == {founder} and\\n                           founder in e.tf_developer_set and len(e.tf_developer_set) == 1]\\n    if not founder_only_tfdds: skip repo  # not in the target subset (~66% of TFDDs are TF=1\\n                                            # per Avelino et al., so expect most founder-led\\n                                            # single-TF-dev repos to qualify -- but ALSO require\\n                                            # founder to literally BE that lone TF developer,\\n                                            # which is a stricter subset the plan must track)\\n    first_founder_tfdd = min(founder_only_tfdds, key=lambda e: e.month)\\n    # require >= 12 months of history BEFORE this TFDD (for the pre-window) and >= 18 months\\n    # AFTER it (for survival scoring) -- else skip (right/left-censored)\\n\\n# === STAGE 4: NEW measurement -- pre-departure authority-diffusion trajectory ===\\nfor repo in repos_with_founder_tfdd:\\n    tfdd_month = first_founder_tfdd.month\\n    window = [tfdd_month - 12mo, tfdd_month - 6mo]   # the 6-12-month PRE-departure window\\n    commits_in_window = events filtered to author_date in window\\n    founder_share = count(commits_in_window where author==founder) / count(commits_in_window)\\n    # distinct non-founder DOA-file-owners reached DURING the window: for each month-end\\n    # snapshot INSIDE the window, recompute primary_owner(f, snapshot) for all files touched\\n    # up to that snapshot; collect the set of non-founder authors who are primary_owner of\\n    # >= 1 file at ANY snapshot inside the window (use the running DOA state already computed\\n    # in Stage 2, just re-slice it to the window's snapshot dates -- do NOT recompute from\\n    # scratch, reuse memoized per-snapshot DOA tables for efficiency)\\n    n_doa_owners = len(distinct non-founder primary owners across window snapshots)\\n    diffusion_score = {founder_share, n_doa_owners}  # primary predictors\\n\\n# === STAGE 5: Survival outcome (Avelino et al.'s Active/Inactive/recovery model) ===\\nfor repo in repos_with_diffusion_score:\\n    post = events filtered to author_date in [tfdd_month, tfdd_month + 18mo]\\n    # Active/Inactive state machine: repo is Inactive from tfdd_month until a NEW developer\\n    # (not in the departed TF set) attains TF-developer status (joins the current\\n    # TF_developer_set at some post-TFDD monthly snapshot) -- that event flips it back Active.\\n    recovered = any(post-TFDD snapshot where a new author is in TF_developer_set)\\n    # graded outcome (thriving/maintained/dormant/dead) -- define via post-TFDD commit\\n    # velocity relative to pre-TFDD baseline, using quartile cut points the executor derives\\n    # empirically from the corpus's own post-TFDD commit-count distribution (report the exact\\n    # cutpoints used, since Avelino et al.'s paper does not give exact numeric thresholds for\\n    # the 4 labels -- executor should fetch_grep the ESEM 2019 paper for their operational\\n    # definition of the 4 states before inventing one from scratch)\\n    binary_survival = recovered  # matches Avelino et al.'s binary survive/not-survive stat\\n\\n# === STAGE 6: Confound controls ===\\nfor repo: controls = {log_stars, log_forks, contributor_count, language, license,\\n                       developers_at_tfdd, commits_at_tfdd, files_at_tfdd}  # the snapshot\\n                       # covariates Avelino et al. found null (d=0.13-0.26) -- MUST be\\n                       # recomputed here identically to compare standardized effect sizes\\n\\n# === STAGE 7: Analysis (a) regression ===\\nX = [founder_share, n_doa_owners, log_stars, log_forks, contributor_count,\\n     developers_at_tfdd, commits_at_tfdd, files_at_tfdd] + language/license one-hot\\nlogit_model = sm.Logit(binary_survival, standardize(X)).fit()          # statsmodels\\nordinal_model = statsmodels.miscmodels.ordinal_model.OrderedModel(\\n                    graded_outcome, standardize(X), distr='logit').fit()\\nBH_correct(p_values_of_all_coefficients)  # statsmodels.stats.multitest.multipletests, method='fdr_bh'\\nreport: standardized_coef, BH_p, compare |coef(founder_share)|, |coef(n_doa_owners)| vs\\n        |coef(log_stars)|, |coef(developers_at_tfdd)| etc.\\n\\n# === STAGE 8: Analysis (b) matched-pairs / stratified comparison ===\\nbuckets = stratify_by(log_stars_decile, log_forks_decile, contributor_count_bucket)\\nhigh_diffusion = repos where founder_share < 0.50 AND n_doa_owners >= 2\\nlow_diffusion  = repos where founder_share >= 0.80\\nfor each bucket: pair high_diffusion repos to low_diffusion repos via nearest-neighbor on\\n                 (log_stars, log_forks, contributor_count) using sklearn NearestNeighbors\\n                 or scipy cKDTree, caliper = 0.2 * pooled std of matching covariates\\nsurvival_rate_ratio = mean(binary_survival | high_diffusion, matched) / \\n                       mean(binary_survival | low_diffusion, matched)\\nbootstrap_CI = bootstrap(survival_rate_ratio, n_resamples=10000, method='percentile')\\nreport ratio, 95% CI, compare against Avelino et al.'s unconditioned 41% baseline\\n\\n# === STAGE 9: Falsification / placebo check ===\\nnull_ratios = []\\nfor trial in range(1000):\\n    for repo: relocate window to a uniformly random start month in\\n              [first_commit_date, tfdd_month - window_length - 1mo]  # same length, must stay\\n              strictly before the TRUE window's start to avoid leakage; recompute\\n              founder_share_null, n_doa_owners_null using the SAME memoized per-snapshot DOA\\n              tables from Stage 2 (cheap re-slice, no recomputation)\\n    rerun analysis (a) and (b) with the null-window predictors\\n    null_ratios.append(placebo_survival_rate_ratio)\\nreport: true_effect_percentile_in_null_distribution, empirical p-value =\\n        (1 + sum(null_ratios >= true_ratio)) / (1 + len(null_ratios))\\n\\n# === STAGE 10: Assemble method_out.json ===\\noutput = {\\n  'corpus_stats': {n_repos_input, n_repos_after_filters, n_founder_only_tfdds, exclusion_table},\\n  'baseline_replication': {tfdd_rate, survival_rate, snapshot_effect_sizes},  # sanity check\\n                                                                              # against Avelino\\n                                                                              # et al.'s reported\\n                                                                              # 16% TFDD rate /\\n                                                                              # 41% survival / d\\n  'regression_results': {...},\\n  'matched_pairs_results': {...},\\n  'placebo_results': {...},\\n  'success_criteria_verdict': {criterion_1_pass_bool, criterion_2_pass_bool,\\n                                criterion_3_pass_bool, notes}\\n}\",\n  \"fallback_plan\": \"Layer the fallbacks by what breaks first, from cheapest degradation to most fundamental: (1) FULL git clones too slow/large -- if the DATASET artifact only supplies shallow clones or pre-extracted commit logs without full blob history, that's fine: DOA only needs (author, file, commit_date) triples, not blob contents, so nothing in the pipeline actually requires full clones; explicitly do NOT re-clone anything, use whatever the dataset provides. (2) Corpus too small after filtering (e.g., <40-50 founder-only-TFDD repos survive the >=3-year-history + founder-only-TF=1 filters) -- relax the TF=1-at-departure requirement to TF<=2 with founder in the departing set and note the deviation explicitly in the output, since Avelino et al. themselves report 66% of TFDDs are TF=1 so a large corpus should still clear the stricter filter; if it still doesn't, reduce required post-TFDD survival window from 18 to 12 months (report both) rather than dropping repos, and flag this as a limitation rather than silently changing the headline metric. (3) DOA/TF computation too slow at monthly granularity across the full corpus -- switch from monthly to quarterly snapshots for Stage 2's running DOA state (this is the compute-heavy step: O(commits x files) per snapshot); the pre-departure window (6-12mo) and TFDD detection can tolerate quarterly resolution with a documented +/-1.5 month fuzz on the TFDD date, which does not materially change founder_share or n_doa_owners since both are already window-aggregate statistics. (4) statsmodels' OrderedModel fails to converge on the graded 4-level outcome (common with small/imbalanced strata) -- fall back to the binary logistic regression only for the primary claim (success criterion 2 only requires the diffusion predictors' significance, which the binary model alone can establish) and report the ordinal model as exploratory/best-effort with a convergence-failure caveat rather than blocking the whole artifact on it. (5) Matched-pairs bucket has too few pairs per stratum for a stable bootstrap CI (e.g., <10 pairs in the high-diffusion vs low-diffusion contrast within a size bucket) -- pool across size buckets and instead include the matching covariates (log_stars, log_forks, contributor_count) as regression adjustors in a single pooled matched-set analysis (essentially collapsing (a) and (b) into one covariate-adjusted comparison), clearly labeled as a fallback deviation from the pre-registered stratified design in success_criteria_verdict.notes. (6) If the DATASET artifact this experiment depends on does not actually provide enough repos with the founder-identifiable-first-commit property (e.g., many repos were imported from an external VCS with no clean initial commit) -- restrict founder identification to repos where the first commit's author authored >= 3 of the first 5 commits (a robustness check against a single miscategorized scaffolding commit), and report the fraction of repos excluded for unidentifiable founders as part of the exclusion table so the reader can judge the founder-only subset's representativeness. Under no circumstances should the executor fabricate or downsample results to hit the success-criteria thresholds -- report a null/negative result plainly if the corpus and analysis genuinely produce one; a rigorous null result on this question is itself a valid, reportable outcome given Avelino et al.'s own snapshot-null precedent.\",\n  \"testing_plan\": \"1. UNIT-TEST DOA/TF logic on a synthetic 3-file, 4-author toy repo with hand-computed expected DOA values and a known TF set BEFORE running on any real data -- construct commit sequences where the expected primary owner, TF size, and TFDD timing are unambiguous by hand-derivation, and assert the code reproduces them exactly. This catches formula/off-by-one errors cheaply since the full DOA formula (particularly the DL term) must be verified against the ICPC 2016 paper text rather than guessed. 2. SMOKE TEST on 3-5 real, well-known single-founder repos with a documented founder departure the executor can sanity-check by eye (e.g., search for OSS projects with public 'founder handed off maintenance' blog posts/README history) -- confirm the pipeline's detected TFDD month is within a few months of the publicly known handoff date, and that the pre-TFDD founder_share trend direction (declining vs not) matches what a manual `git shortlog` inspection of that repo's commit history shows for the year before handoff. 3. BASELINE-REPLICATION CHECK on the full filtered corpus before running the NEW diffusion analysis: verify the pipeline's own aggregate stats are in the right ballpark against Avelino et al.'s published numbers -- TFDD rate should land near their 16% (not required to match exactly since the corpus differs, but order-of-magnitude and general directionality, e.g. TFDD rate should not come out as 90% or 1%, would indicate a pipeline bug), TF=1-at-departure share near their 66%, and overall post-TFDD binary survival rate near their 41% -- treat large deviations (e.g., >2x off) as a signal to debug the TFDD-detection or survival-scoring logic before trusting the new diffusion results. Also directly recompute the size/popularity snapshot effect sizes (developers/commits/files at TFDD, survivors vs non-survivors) and confirm they replicate as negligible-to-small (d roughly in the 0.1-0.3 range, same sign direction) as reported in the ESEM 2019 paper -- this is the load-bearing sanity check, since the entire hypothesis is that the NEW pre-departure signal succeeds precisely where this snapshot signal is known to fail; if the replication check itself produces a strong snapshot effect where Avelino et al. found none, that indicates a corpus-construction or measurement discrepancy needing resolution before proceeding to the novel analysis. 4. SCALE GRADUALLY: run the full pipeline (Stages 1-6) on a 20-30 repo mini-sample first, inspect the diffusion-score distribution and survival labels by hand for a handful of cases, confirm nothing is degenerate (e.g., founder_share always exactly 0 or 1, n_doa_owners always 0) before scaling to the full corpus and before launching the 500-1000-iteration placebo loop, which is the single most expensive step and should only run once Stages 1-8 are validated end-to-end on the mini-sample. 5. Track and report cumulative OpenRouter spend if any LLM calls are used for repo/language filtering heuristics (should be $0 or near-$0 for this artifact -- the entire pipeline is deterministic git-log analysis and statistics, not LLM-driven; if the executor finds itself needing an LLM call anywhere in this pipeline, that is a signal the approach has drifted from what was planned and should be reconsidered).\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [6] ASSISTANT · 2026-08-21 15:39:58 UTC

```
Plan written to `.terminal_claude_agent_struct_out.json` — covers DOA/TF recomputation, founder-only TFDD detection, the new pre-departure diffusion metric, survival scoring, the three analyses (regression/matched-pairs/placebo), fallbacks for corpus-size and compute issues, and a testing plan anchored on replicating Avelino et al.'s baseline stats first.
```
