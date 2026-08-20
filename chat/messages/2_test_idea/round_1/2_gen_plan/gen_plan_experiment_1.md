# gen_plan_experiment_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_plan`
> Run: `run_5SMkWpWKNLxk` — Measuring Authority Diffusion Before Founders Leave Open Source Projects
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_experiment_1` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-08-20 19:02:05 UTC

```
model: claude-sonnet-5 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_1/gen_plan/gen_plan_experiment_1
```

### [2] SYSTEM-USER prompt · 2026-08-20 19:02:15 UTC

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

id: experiment_iter1_dir2
type: experiment
objective: >-
  Implement Avelino et al.'s DOA-based Truck Factor / TFDD pipeline, locate each project's first founder-only (TF=1) TFDD,
  compute the NEW pre-departure authority-diffusion trajectory (founder commit-share and distinct non-founder DOA-file-owner
  count in the 6-12 months immediately before that TFDD) alongside the snapshot covariates Avelino et al. use (developers/commits/files
  AT the TFDD), and compute the 18-month post-TFDD survival outcome per their Active/Inactive model.
approach: >-
  Reimplement Fritz et al.'s DOA formula (first-authorship + acceptance-ratio-weighted change ownership) per file per year
  exactly as specified in Avelino et al. 2016/2019, derive per-year Truck-Factor sets, detect the first TFDD where the detaching
  TF set has size 1, and label 6-12-months-pre-TFDD authority diffusion vs the at-TFDD snapshot. Fit (a) a matched-pairs comparison
  bucketed by stars/forks/contributor-count comparing survival rates for high- vs low-pre-departure-diffusion projects, and
  (b) a logistic/ordinal regression of survival on diffusion predictors plus snapshot/popularity controls (BH-corrected p-values,
  standardized effect sizes vs Avelino et al.'s reported d=0.13-0.26). Include the placebo/shuffle check: relocate the 'pre-departure
  window' randomly within each project's history and confirm the effect weakens. Uses the raw commit-history dataset planned
  in this same strategy as its input once it completes.
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
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/user_uploads`. Check this folder for anything relevant to your task.
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

### [3] HUMAN-USER prompt · 2026-08-20 19:02:15 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [4] TOOL CALL — Write · 2026-08-20 19:03:20 UTC

```
File: /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_1/gen_plan/gen_plan_experiment_1/.terminal_claude_agent_struct_out.json

{
  "title": "Does authority spread before founders leave predict survival?",
  "summary": "Reimplement Avelino et al.'s (ESEM 2019) DOA/Truck-Factor/TFDD pipeline on the DATASET dependency's mined commit histories, locate each project's first founder-only (TF=1) TFDD, compute a NEW pre-departure authority-diffusion trajectory (founder commit-share and count of distinct non-founder DOA file-owners in the 6-12 months before the TFDD) alongside the AT-TFDD snapshot covariates Avelino et al. use, compute 18-month post-TFDD survival via their Active/Inactive model, then test whether pre-departure diffusion predicts survival beyond size/popularity via a matched-pairs comparison, a BH-corrected logistic/ordinal regression, and a window-shuffle placebo check.",
  "runpod_compute_profile": "cpu_heavy",
  "implementation_pseudocode": "# INPUT: relies on the DATASET dependency artifact producing, per repo, a commit log with\n#   (commit_sha, author_email/login, timestamp, list_of_files_touched, insertions/deletions or diff per file)\n#   plus repo metadata (stars, forks, language, license, first_commit_date, last_commit_date).\n# If that dataset schema differs, adapt field names in STEP 0 only -- do not redesign the pipeline.\n\nimport pandas as pd, numpy as np, json, itertools\nfrom scipy import stats\nfrom statsmodels.stats.multitest import multipletests\nimport statsmodels.api as sm\n\n# ---------- STEP 0: Load & alias-resolve ----------\nfor repo in dataset.repos:\n    commits = load_commits(repo)  # columns: sha, author_id, ts, files[]\n    # Alias resolution: group by (name, email) exact match first, then normalize\n    # emails (lowercase, strip +tags, strip noreply github ids -> map to canonical login\n    # via GitHub API user lookup if available in dataset; else fall back to email domain\n    # heuristics). Record resolution rate; Avelino et al. report median 11% alias rate --\n    # log per-repo alias-collapse rate as a QA metric, flag repos where >40% collapse\n    # (likely mis-resolution) for manual exclusion.\n    commits['author_id'] = resolve_aliases(commits)\n\n# ---------- STEP 1: Yearly DOA per file per author (Fritz et al. formula, as used by Avelino) ----------\n# DOA(author, file, year) = FA_weight*is_first_author(author,file)\n#                            + LOG_weight*log(1+num_deliveries_since(author,file,year))\n#                            - AC_weight*log(1+num_accepted_others_deliveries(file,year))\n# Avelino et al. use Fritz's original weights: FA=3.293, DL=1.098, AC=-1.017 on log(1+n) terms\n# (deliveries = commits touching the file; 'first author' = earliest commit creating/touching file).\n# Recompute per calendar year using a CUMULATIVE commit window (all commits up to and including\n# that year, matching Avelino et al.'s yearly-snapshot design) so DOA reflects ownership-to-date.\ndef compute_doa_table(commits, year):\n    window = commits[commits.ts <= year_end(year)]\n    doa = {}\n    for file, group in window.groupby('file'):\n        first_author = group.sort_values('ts').iloc[0].author_id\n        counts = group.author_id.value_counts()  # deliveries per author\n        total = counts.sum()\n        for author, n in counts.items():\n            others = total - n\n            doa[(file, author, year)] = (\n                3.293 * (author == first_author)\n                + 1.098 * np.log1p(n)\n                - 1.017 * np.log1p(others)\n            )\n    return doa\n\n# Primary DOA owner of a file in a year = argmax author over doa[(file, *, year)]\n# (ties broken by earliest commit -> matches Avelino's tie-break note; log any tie count)\n\n# ---------- STEP 2: Yearly Truck Factor set (greedy DOA-based TF algorithm, Avelino 2016 ICPC) ----------\ndef truck_factor_set(doa_table, year):\n    # Assign each file to its primary-DOA author for that year (only authors with DOA > 0\n    # AND DOA within Avelino's coverage threshold are eligible authors, per ICPC 2016 Sec 3)\n    file_owner = argmax_owner_per_file(doa_table, year)\n    owned_files = defaultdict(set)\n    for file, owner in file_owner.items():\n        owned_files[owner].add(file)\n    # Greedy: repeatedly remove the author owning the most files until <50% of files remain\n    # covered by remaining authors (Avelino/Cataldo 'half of files' criterion)\n    remaining = set(file_owner.keys())\n    tf_set = []\n    total_files = len(remaining)\n    while covered_fraction(remaining, owned_files, tf_set) < 0.5:\n        top_author = max(owned_files, key=lambda a: len(owned_files[a] & remaining))\n        tf_set.append(top_author)\n        remaining -= owned_files[top_author]\n    return tf_set  # Truck Factor = len(tf_set)\n\n# ---------- STEP 3: Detect TFDD events ----------\n# For each repo, for each year Y with a TF set S_Y:\n#   TFDD at year Y+1 if EVERY developer in S_Y has zero commits in the ABANDONER window\n#   (Avelino's validated 1-year silence threshold) starting at their last commit.\n# Founder-only TFDD = first such event where |S_Y| == 1 AND that single developer is the\n# repo's FOUNDER, defined as the author of the repo's first commit (or first N commits if\n# the true first commit is a bulk import -- flag and use first HUMAN commit heuristically:\n# exclude commits with >80% of repo's files touched in one shot within first week, a known\n# 'perils of mining GitHub' import artifact per Avelino et al./Kalliamvakou et al. 2014).\nfor repo in repos:\n    yearly_tf = {y: truck_factor_set(doa_tables[y], y) for y in years(repo)}\n    tfdd_year = first_year_where_tf_set_fully_silent(yearly_tf, silence_months=12)\n    if tfdd_year is None: continue\n    departing_set = yearly_tf[tfdd_year - 1]\n    if len(departing_set) != 1: continue  # not founder-only\n    if departing_set[0] != repo.founder_id: continue\n    founder_tfdd_events.append((repo, tfdd_year, departing_set[0]))\n\n# ---------- STEP 4: NEW pre-departure diffusion trajectory (6-12mo before TFDD date) ----------\nfor repo, tfdd_date, founder in founder_tfdd_events:\n    window_start, window_end = tfdd_date - 12*months, tfdd_date - 6*months\n    wc = commits[(commits.ts >= window_start) & (commits.ts < window_end)]\n    founder_share = (wc.author_id == founder).sum() / max(len(wc), 1)\n    # distinct non-founder accounts with primary DOA ownership on >=1 file, computed on the\n    # CUMULATIVE window up to window_end (DOA needs history, not just the 6mo slice)\n    doa_pre = compute_doa_table(commits[commits.ts < window_end], year=window_end.year)\n    owners_pre = set(argmax_owner_per_file(doa_pre, window_end.year).values())\n    n_diffuse_owners = len(owners_pre - {founder})\n    diffusion_score = combine(founder_share, n_diffuse_owners)  # keep both raw + composite\n\n# ---------- STEP 5: AT-TFDD snapshot covariates (Avelino et al.'s original metrics, for comparison) ----------\n#   developers_at_tfdd, commits_at_tfdd, files_at_tfdd  (counts in the year of TFDD)\n\n# ---------- STEP 6: Survival outcome (Avelino's Active/Inactive, 18mo window) ----------\n# Active again = a NEW developer (not in departing_set) reaches TF-set membership within\n# 18 months post-TFDD, evidenced by >=1 commit and DOA-based ownership growth.\n# Grade: thriving (regains TF>=2 & sustained commit rate>=pre-TFDD median),\n#        maintained (regains TF=1, commit rate present but lower),\n#        dormant (sporadic commits, no new TF developer),\n#        dead (zero commits 18mo post-TFDD)\nfor repo, tfdd_date, founder in founder_tfdd_events:\n    survival_label = classify_survival(commits, tfdd_date, window=18*months)\n    survived_binary = survival_label in ('thriving', 'maintained')\n\n# ---------- STEP 7: Matched-pairs comparison ----------\n# Bucket by (stars decile, forks decile, contributor_count decile, language) using\n# nearest-neighbor matching (sklearn NearestNeighbors on standardized [log_stars, log_forks,\n# log_contributors] within same language); pair each high-diffusion project\n# (founder_share<0.5 AND n_diffuse_owners>=2) to nearest low-diffusion project\n# (founder_share>=0.8) within the SAME bucket. Compute survival-rate lift with\n# bootstrap 95% CI (10,000 resamples of matched pairs) via paired difference-in-proportions.\n\n# ---------- STEP 8: Logistic / ordinal regression ----------\n# survived_binary ~ founder_share_pre + n_diffuse_owners_pre + log_stars + log_forks\n#                    + contributor_count + C(language) + C(license)\n# ordinal model (statsmodels OrderedModel) on the 4-level survival_label as robustness check.\n# BH-correct p-values across the diffusion-predictor coefficients + snapshot-covariate\n# coefficients tested jointly (Avelino et al.'s own multiple-comparison procedure).\n# Report standardized (beta) effect sizes; compare diffusion betas vs snapshot-covariate\n# betas (Avelino's d=0.13 files / 0.25-0.26 developers,commits) using Cohen's d equivalents.\n\n# ---------- STEP 9: Placebo / shuffle check ----------\n# For each founder-TFDD project, redraw a random 6mo window from anywhere in [first_commit,\n# tfdd_date - 18mo] (excluding the true pre-departure window), recompute founder_share and\n# n_diffuse_owners on that placebo window, refit Step 8's regression with placebo predictors\n# in place of true ones. Repeat 500 times; report the distribution of placebo effect sizes\n# and the fraction that reach the true predictor's significance -- expect near/below alpha.\n\n# ---------- OUTPUT: method_out.json ----------\n# {\n#   'n_repos_total', 'n_founder_tfdd_events', 'alias_qa': {...},\n#   'matched_pairs': {'n_pairs', 'survival_lift', 'ci_95', 'p_value'},\n#   'regression': {'logistic': {...coeffs, se, p_bh, std_effect...},\n#                   'ordinal': {...}},\n#   'snapshot_vs_diffusion_effect_sizes': {...},\n#   'placebo_check': {'true_effect', 'placebo_null_distribution_summary', 'fraction_placebo_ge_true'},\n#   'per_repo_records': [...]  # for downstream figure generation\n# }",
  "fallback_plan": "If the DATASET dependency does not provide full per-file diff/blame-level history (only commit metadata without file lists), fall back to a coarser DOA proxy: approximate first-authorship and delivery counts from (author, file-path) pairs derivable from commit 'files changed' lists alone (available from the GitHub API commits endpoint even without full diffs), dropping the AC (acceptance-ratio-of-others) term's line-level weighting and instead weighting by commit count only -- document this deviation explicitly in the output JSON under a 'doa_approximation_used' flag so downstream comparisons to Avelino et al.'s d=0.13-0.26 baselines are appropriately caveated. If the number of founder-only TFDD events after filtering (mining artifacts, alias-collapse QA failures, <3yr post-departure history) falls below ~40 -- too few for a well-powered matched-pairs test -- relax the founder-only (TF=1) restriction to include TF<=2 departures where one departing member is identifiably the founder, clearly labeling this as an extended sample distinct from the strict TF=1 headline result, and report both. If GitHub API alias resolution/user lookups are unavailable (no network/API budget), use email+display-name exact-match only for alias collapsing and report the (lower) resulting alias-collapse rate as a limitation rather than blocking the pipeline. If the matched-pairs nearest-neighbor design finds too few eligible pairs per language, relax matching to pool across languages with language as a regression control only, and note the matched-pairs analysis is then unstratified by language. If compute time for full DOA-per-year recomputation across the whole corpus is prohibitive within the 6h budget, restrict DOA computation to files touched within a 2-year window centered on the TFDD (rather than full project history) -- Avelino et al.'s DOA formula only needs deliveries up to the year of interest, and truncating pre-window history has second-order effect on the primary-owner argmax for most files.",
  "testing_plan": "1) SMOKE TEST on 3-5 small synthetic/toy repos with hand-constructed commit logs (e.g., a 2-author repo with a clear founder->co-maintainer authority handoff, a 1-author repo with no handoff, a repo with an obvious import-artifact bulk commit) to verify DOA computation, TF-set extraction, and TFDD detection produce the expected, hand-checkable outputs before touching real data. 2) VALIDATE DOA/TF implementation against Avelino et al.'s own reported aggregate numbers on a random sample of ~20-30 real repos from the DATASET dependency: confirm the TF distribution and TFDD rate roughly track their reported 16% TFDD rate and 66% TF=1-at-detachment share (large deviations indicate an implementation bug, not necessarily a substantive finding, since this is a replication of their published pipeline). 3) MINI RUN: execute the full pipeline (DOA -> TF -> TFDD -> diffusion trajectory -> survival -> regression -> placebo) end-to-end on ~50-100 repos first, checking for crashes, degenerate distributions (e.g., founder_share always 0 or 1, indicating a windowing bug), and sane survival-label proportions (roughly near Avelino's 41% baseline before conditioning). 4) Only after the mini run passes basic sanity checks, scale to the full DATASET-provided corpus, log per-repo processing time to confirm the full run fits the compute budget, and checkpoint intermediate DOA/TF tables to disk so a crash mid-corpus does not require full recomputation. 5) Before finalizing, spot-check 5-10 individual founder-TFDD events by eye against the raw commit log (does the flagged 'founder' really look like the original author; does the diffusion window really precede the detected TFDD date) to catch systematic date-alignment or off-by-one-year errors in the yearly-snapshot logic."
}
```

### [5] TOOL RESULT — Write · 2026-08-20 19:03:20 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_1/gen_plan/gen_plan_experiment_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Does authority spread before founders leave predict survival?\",\n  \"summary\": \"Reimplement Avelino et al.'s (ESEM 2019) DOA/Truck-Factor/TFDD pipeline on the DATASET dependency's mined commit histories, locate each project's first founder-only (TF=1) TFDD, compute a NEW pre-departure authority-diffusion trajectory (founder commit-share and count of distinct non-founder DOA file-owners in the 6-12 months before the TFDD) alongside the AT-TFDD snapshot covariates Avelino et al. use, compute 18-month post-TFDD survival via their Active/Inactive model, then test whether pre-departure diffusion predicts survival beyond size/popularity via a matched-pairs comparison, a BH-corrected logistic/ordinal regression, and a window-shuffle placebo check.\",\n  \"runpod_compute_profile\": \"cpu_heavy\",\n  \"implementation_pseudocode\": \"# INPUT: relies on the DATASET dependency artifact producing, per repo, a commit log with\\n#   (commit_sha, author_email/login, timestamp, list_of_files_touched, insertions/deletions or diff per file)\\n#   plus repo metadata (stars, forks, language, license, first_commit_date, last_commit_date).\\n# If that dataset schema differs, adapt field names in STEP 0 only -- do not redesign the pipeline.\\n\\nimport pandas as pd, numpy as np, json, itertools\\nfrom scipy import stats\\nfrom statsmodels.stats.multitest import multipletests\\nimport statsmodels.api as sm\\n\\n# ---------- STEP 0: Load & alias-resolve ----------\\nfor repo in dataset.repos:\\n    commits = load_commits(repo)  # columns: sha, author_id, ts, files[]\\n    # Alias resolution: group by (name, email) exact match first, then normalize\\n    # emails (lowercase, strip +tags, strip noreply github ids -> map to canonical login\\n    # via GitHub API user lookup if available in dataset; else fall back to email domain\\n    # heuristics). Record resolution rate; Avelino et al. report median 11% alias rate --\\n    # log per-repo alias-collapse rate as a QA metric, flag repos where >40% collapse\\n    # (likely mis-resolution) for manual exclusion.\\n    commits['author_id'] = resolve_aliases(commits)\\n\\n# ---------- STEP 1: Yearly DOA per file per author (Fritz et al. formula, as used by Avelino) ----------\\n# DOA(author, file, year) = FA_weight*is_first_author(author,file)\\n#                            + LOG_weight*log(1+num_deliveries_since(author,file,year))\\n#                            - AC_weight*log(1+num_accepted_others_deliveries(file,year))\\n# Avelino et al. use Fritz's original weights: FA=3.293, DL=1.098, AC=-1.017 on log(1+n) terms\\n# (deliveries = commits touching the file; 'first author' = earliest commit creating/touching file).\\n# Recompute per calendar year using a CUMULATIVE commit window (all commits up to and including\\n# that year, matching Avelino et al.'s yearly-snapshot design) so DOA reflects ownership-to-date.\\ndef compute_doa_table(commits, year):\\n    window = commits[commits.ts <= year_end(year)]\\n    doa = {}\\n    for file, group in window.groupby('file'):\\n        first_author = group.sort_values('ts').iloc[0].author_id\\n        counts = group.author_id.value_counts()  # deliveries per author\\n        total = counts.sum()\\n        for author, n in counts.items():\\n            others = total - n\\n            doa[(file, author, year)] = (\\n                3.293 * (author == first_author)\\n                + 1.098 * np.log1p(n)\\n                - 1.017 * np.log1p(others)\\n            )\\n    return doa\\n\\n# Primary DOA owner of a file in a year = argmax author over doa[(file, *, year)]\\n# (ties broken by earliest commit -> matches Avelino's tie-break note; log any tie count)\\n\\n# ---------- STEP 2: Yearly Truck Factor set (greedy DOA-based TF algorithm, Avelino 2016 ICPC) ----------\\ndef truck_factor_set(doa_table, year):\\n    # Assign each file to its primary-DOA author for that year (only authors with DOA > 0\\n    # AND DOA within Avelino's coverage threshold are eligible authors, per ICPC 2016 Sec 3)\\n    file_owner = argmax_owner_per_file(doa_table, year)\\n    owned_files = defaultdict(set)\\n    for file, owner in file_owner.items():\\n        owned_files[owner].add(file)\\n    # Greedy: repeatedly remove the author owning the most files until <50% of files remain\\n    # covered by remaining authors (Avelino/Cataldo 'half of files' criterion)\\n    remaining = set(file_owner.keys())\\n    tf_set = []\\n    total_files = len(remaining)\\n    while covered_fraction(remaining, owned_files, tf_set) < 0.5:\\n        top_author = max(owned_files, key=lambda a: len(owned_files[a] & remaining))\\n        tf_set.append(top_author)\\n        remaining -= owned_files[top_author]\\n    return tf_set  # Truck Factor = len(tf_set)\\n\\n# ---------- STEP 3: Detect TFDD events ----------\\n# For each repo, for each year Y with a TF set S_Y:\\n#   TFDD at year Y+1 if EVERY developer in S_Y has zero commits in the ABANDONER window\\n#   (Avelino's validated 1-year silence threshold) starting at their last commit.\\n# Founder-only TFDD = first such event where |S_Y| == 1 AND that single developer is the\\n# repo's FOUNDER, defined as the author of the repo's first commit (or first N commits if\\n# the true first commit is a bulk import -- flag and use first HUMAN commit heuristically:\\n# exclude commits with >80% of repo's files touched in one shot within first week, a known\\n# 'perils of mining GitHub' import artifact per Avelino et al./Kalliamvakou et al. 2014).\\nfor repo in repos:\\n    yearly_tf = {y: truck_factor_set(doa_tables[y], y) for y in years(repo)}\\n    tfdd_year = first_year_where_tf_set_fully_silent(yearly_tf, silence_months=12)\\n    if tfdd_year is None: continue\\n    departing_set = yearly_tf[tfdd_year - 1]\\n    if len(departing_set) != 1: continue  # not founder-only\\n    if departing_set[0] != repo.founder_id: continue\\n    founder_tfdd_events.append((repo, tfdd_year, departing_set[0]))\\n\\n# ---------- STEP 4: NEW pre-departure diffusion trajectory (6-12mo before TFDD date) ----------\\nfor repo, tfdd_date, founder in founder_tfdd_events:\\n    window_start, window_end = tfdd_date - 12*months, tfdd_date - 6*months\\n    wc = commits[(commits.ts >= window_start) & (commits.ts < window_end)]\\n    founder_share = (wc.author_id == founder).sum() / max(len(wc), 1)\\n    # distinct non-founder accounts with primary DOA ownership on >=1 file, computed on the\\n    # CUMULATIVE window up to window_end (DOA needs history, not just the 6mo slice)\\n    doa_pre = compute_doa_table(commits[commits.ts < window_end], year=window_end.year)\\n    owners_pre = set(argmax_owner_per_file(doa_pre, window_end.year).values())\\n    n_diffuse_owners = len(owners_pre - {founder})\\n    diffusion_score = combine(founder_share, n_diffuse_owners)  # keep both raw + composite\\n\\n# ---------- STEP 5: AT-TFDD snapshot covariates (Avelino et al.'s original metrics, for comparison) ----------\\n#   developers_at_tfdd, commits_at_tfdd, files_at_tfdd  (counts in the year of TFDD)\\n\\n# ---------- STEP 6: Survival outcome (Avelino's Active/Inactive, 18mo window) ----------\\n# Active again = a NEW developer (not in departing_set) reaches TF-set membership within\\n# 18 months post-TFDD, evidenced by >=1 commit and DOA-based ownership growth.\\n# Grade: thriving (regains TF>=2 & sustained commit rate>=pre-TFDD median),\\n#        maintained (regains TF=1, commit rate present but lower),\\n#        dormant (sporadic commits, no new TF developer),\\n#        dead (zero commits 18mo post-TFDD)\\nfor repo, tfdd_date, founder in founder_tfdd_events:\\n    survival_label = classify_survival(commits, tfdd_date, window=18*months)\\n    survived_binary = survival_label in ('thriving', 'maintained')\\n\\n# ---------- STEP 7: Matched-pairs comparison ----------\\n# Bucket by (stars decile, forks decile, contributor_count decile, language) using\\n# nearest-neighbor matching (sklearn NearestNeighbors on standardized [log_stars, log_forks,\\n# log_contributors] within same language); pair each high-diffusion project\\n# (founder_share<0.5 AND n_diffuse_owners>=2) to nearest low-diffusion project\\n# (founder_share>=0.8) within the SAME bucket. Compute survival-rate lift with\\n# bootstrap 95% CI (10,000 resamples of matched pairs) via paired difference-in-proportions.\\n\\n# ---------- STEP 8: Logistic / ordinal regression ----------\\n# survived_binary ~ founder_share_pre + n_diffuse_owners_pre + log_stars + log_forks\\n#                    + contributor_count + C(language) + C(license)\\n# ordinal model (statsmodels OrderedModel) on the 4-level survival_label as robustness check.\\n# BH-correct p-values across the diffusion-predictor coefficients + snapshot-covariate\\n# coefficients tested jointly (Avelino et al.'s own multiple-comparison procedure).\\n# Report standardized (beta) effect sizes; compare diffusion betas vs snapshot-covariate\\n# betas (Avelino's d=0.13 files / 0.25-0.26 developers,commits) using Cohen's d equivalents.\\n\\n# ---------- STEP 9: Placebo / shuffle check ----------\\n# For each founder-TFDD project, redraw a random 6mo window from anywhere in [first_commit,\\n# tfdd_date - 18mo] (excluding the true pre-departure window), recompute founder_share and\\n# n_diffuse_owners on that placebo window, refit Step 8's regression with placebo predictors\\n# in place of true ones. Repeat 500 times; report the distribution of placebo effect sizes\\n# and the fraction that reach the true predictor's significance -- expect near/below alpha.\\n\\n# ---------- OUTPUT: method_out.json ----------\\n# {\\n#   'n_repos_total', 'n_founder_tfdd_events', 'alias_qa': {...},\\n#   'matched_pairs': {'n_pairs', 'survival_lift', 'ci_95', 'p_value'},\\n#   'regression': {'logistic': {...coeffs, se, p_bh, std_effect...},\\n#                   'ordinal': {...}},\\n#   'snapshot_vs_diffusion_effect_sizes': {...},\\n#   'placebo_check': {'true_effect', 'placebo_null_distribution_summary', 'fraction_placebo_ge_true'},\\n#   'per_repo_records': [...]  # for downstream figure generation\\n# }\",\n  \"fallback_plan\": \"If the DATASET dependency does not provide full per-file diff/blame-level history (only commit metadata without file lists), fall back to a coarser DOA proxy: approximate first-authorship and delivery counts from (author, file-path) pairs derivable from commit 'files changed' lists alone (available from the GitHub API commits endpoint even without full diffs), dropping the AC (acceptance-ratio-of-others) term's line-level weighting and instead weighting by commit count only -- document this deviation explicitly in the output JSON under a 'doa_approximation_used' flag so downstream comparisons to Avelino et al.'s d=0.13-0.26 baselines are appropriately caveated. If the number of founder-only TFDD events after filtering (mining artifacts, alias-collapse QA failures, <3yr post-departure history) falls below ~40 -- too few for a well-powered matched-pairs test -- relax the founder-only (TF=1) restriction to include TF<=2 departures where one departing member is identifiably the founder, clearly labeling this as an extended sample distinct from the strict TF=1 headline result, and report both. If GitHub API alias resolution/user lookups are unavailable (no network/API budget), use email+display-name exact-match only for alias collapsing and report the (lower) resulting alias-collapse rate as a limitation rather than blocking the pipeline. If the matched-pairs nearest-neighbor design finds too few eligible pairs per language, relax matching to pool across languages with language as a regression control only, and note the matched-pairs analysis is then unstratified by language. If compute time for full DOA-per-year recomputation across the whole corpus is prohibitive within the 6h budget, restrict DOA computation to files touched within a 2-year window centered on the TFDD (rather than full project history) -- Avelino et al.'s DOA formula only needs deliveries up to the year of interest, and truncating pre-window history has second-order effect on the primary-owner argmax for most files.\",\n  \"testing_plan\": \"1) SMOKE TEST on 3-5 small synthetic/toy repos with hand-constructed commit logs (e.g., a 2-author repo with a clear founder->co-maintainer authority handoff, a 1-author repo with no handoff, a repo with an obvious import-artifact bulk commit) to verify DOA computation, TF-set extraction, and TFDD detection produce the expected, hand-checkable outputs before touching real data. 2) VALIDATE DOA/TF implementation against Avelino et al.'s own reported aggregate numbers on a random sample of ~20-30 real repos from the DATASET dependency: confirm the TF distribution and TFDD rate roughly track their reported 16% TFDD rate and 66% TF=1-at-detachment share (large deviations indicate an implementation bug, not necessarily a substantive finding, since this is a replication of their published pipeline). 3) MINI RUN: execute the full pipeline (DOA -> TF -> TFDD -> diffusion trajectory -> survival -> regression -> placebo) end-to-end on ~50-100 repos first, checking for crashes, degenerate distributions (e.g., founder_share always 0 or 1, indicating a windowing bug), and sane survival-label proportions (roughly near Avelino's 41% baseline before conditioning). 4) Only after the mini run passes basic sanity checks, scale to the full DATASET-provided corpus, log per-repo processing time to confirm the full run fits the compute budget, and checkpoint intermediate DOA/TF tables to disk so a crash mid-corpus does not require full recomputation. 5) Before finalizing, spot-check 5-10 individual founder-TFDD events by eye against the raw commit log (does the flagged 'founder' really look like the original author; does the diffusion window really precede the detected TFDD date) to catch systematic date-alignment or off-by-one-year errors in the yearly-snapshot logic.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [6] ASSISTANT · 2026-08-20 19:03:23 UTC

```
Plan written to `.terminal_claude_agent_struct_out.json` — a full DOA/Truck-Factor/TFDD reimplementation plan (Fritz-formula pseudocode, founder-only TFDD detection, pre-departure diffusion trajectory, matched-pairs + BH-corrected regression + placebo shuffle test), with fallbacks for incomplete dataset schema, low event counts, and compute limits, plus a staged smoke-test → mini-run → full-scale validation plan.
```
