# gen_plan_evaluation_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_plan`
> Run: `iter1_0b7b616dce39` — Scaling the Corpus, Auditing the Power, and Reconciling the Sign: What Happens When a Founder-Diffusion Survival Test Is Finally Interrogated Rather Than Just Run
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_evaluation_1` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-08-21 16:25:44 UTC

```
model: claude-sonnet-5 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_plan/gen_plan_evaluation_1
```

### [2] SYSTEM-USER prompt · 2026-08-21 16:25:56 UTC

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
You are expanding an artifact direction of type: EVALUATION

EVALUATION
Evaluate experiment results with metrics, statistical analysis, and validity checks.
Runtime: Python 3.12, UV (any evaluation library), isolated workspace, gradual scaling matching experiment.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Compute any quantitative metrics and statistical tests, analyze validity and robustness.
Deps: REQUIRED at least one EXPERIMENT | OPTIONAL DATASET if reference data needed
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

The evaluation executor has 3h total (including writing code, debugging, testing, and fixing errors).

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

id: evaluation_iter1_dir3
type: evaluation
objective: >-
  Run the falsification/placebo check (randomly relocating the 'pre-departure window' within each project's history) and broader
  validity checks to determine whether the diffusion-survival association is genuinely specific to the pre-TFDD period, and
  audit robustness of the DOA/TFDD detection pipeline.
approach: >-
  Using the experiment's per-repo longitudinal DOA/commit-share time series, re-run the diffusion-score computation with the
  '6-12 months pre-departure' window replaced by a randomly selected same-length window elsewhere in each project's pre-TFDD
  history (matched within survivor and non-survivor groups separately, per success_criteria #3), refit the same matched-pairs
  and regression tests on the shuffled window, and compare effect sizes/CI overlap against the true-window results to test
  whether the association collapses. Additionally stratify results by language and popularity bucket to check the effect isn't
  driven by one ecosystem, sanity-check the DOA/TF/TFDD implementation against Avelino et al.'s reported aggregate statistics
  (TFDD rate ~16% of projects, 66% at TF=1, 41% survival) as a pipeline-validity check, and report calibration of the survival
  regression (e.g. via bootstrap CIs) to support the significance claims in success_criteria #1-2.
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

EVALUATION executor scope:
  Output: eval_out.json with evaluation results
  DOES: Any evaluation of experiment results — metrics, statistical tests, ablations, comparisons, visualizations, robustness checks, error analysis, etc.
  DOES NOT: Implement new methods (use EXPERIMENT), collect data (use DATASET)
  This is for analyzing experiment outputs from any angle
</artifact_executor_scope>

<artifact_planning_rules>
EVALUATION: Must depend on at least one EXPERIMENT. Focus on statistical rigor and validity checks.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for evaluation artifacts:
  - gpu: 1x NVIDIA RTX A4500, 20GB VRAM, 7 vCPUs, 29GB RAM — ML training, CUDA, large models (fallback: GPUs cheap→expensive: 2000 Ada → A4000 → 4000 Ada → L4 → 4090 → 5090)
  - cpu_heavy: 4 vCPUs, 32GB RAM — large datasets, memory-intensive processing (fallback: CPUs cheap→expensive, then GPU hosts cheap→expensive (all ≥32GB RAM))

Set runpod_compute_profile to one of these exact tier names.
</compute_profiles>
GOOD PLANS: specific, actionable, consider failure scenarios, build on the suggested approach.
BAD PLANS: vague hand-waving, ignoring the suggested approach, missing critical executor details.
</instructions><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/user_uploads`. Check this folder for anything relevant to your task.
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
  "description": "Plan for an EVALUATION artifact.",
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
    "metrics_descriptions": {
      "description": "What metrics will be computed and how they're defined",
      "title": "Metrics Descriptions",
      "type": "string"
    },
    "metrics_justification": {
      "description": "Why these metrics are the right ones - what do they tell us about the hypothesis",
      "title": "Metrics Justification",
      "type": "string"
    }
  },
  "required": [
    "title",
    "metrics_descriptions",
    "metrics_justification"
  ],
  "title": "EvaluationPlan",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [3] HUMAN-USER prompt · 2026-08-21 16:25:57 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [4] TOOL CALL — Write · 2026-08-21 16:26:39 UTC

```
File: /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_plan/gen_plan_evaluation_1/.terminal_claude_agent_struct_out.json

{
  "title": "Placebo-Window Falsification and Robustness Audit",
  "summary": "Evaluates the pre-departure authority-diffusion experiment by re-running the matched-pairs/regression tests with randomly relocated 'pre-departure windows' (within-group shuffle, survivors vs non-survivors separately), comparing effect sizes/CIs against the true-window results, stratifying by language and popularity bucket, sanity-checking the DOA/TF/TFDD pipeline against Avelino et al.'s published aggregate statistics (TFDD~16%, 66% at TF=1, 41% survival), and bootstrapping calibration/CIs for the survival regression to support or refute success_criteria #1-3.",
  "runpod_compute_profile": "cpu_heavy",
  "metrics_descriptions": "This evaluation consumes the upstream EXPERIMENT artifact's per-repo longitudinal outputs: (a) yearly DOA/TF/TFDD event tables per project, (b) the identified founder-only TFDD timestamp per project, (c) the per-window time series of founder commit-share and count of non-founder DOA file-owners, (d) the true pre-departure (6-12mo) diffusion score and the survival label (18-month Active/Inactive/graded outcome per Avelino et al.), and (e) covariates (stars, forks, contributor count, language, license). Load these from the experiment's output JSON/CSV; if any field is missing (e.g. no full time series, only the single true-window score), FLAG this explicitly as a pipeline gap in eval_out.json rather than fabricating a window series, and fall back to whatever partial checks the available data supports.\n\nStep 1 — Reconstruct the placebo/shuffle test (success_criteria #3): For each project with a founder-TFDD, enumerate all valid same-length (6-12 month) windows in its pre-TFDD history that do NOT overlap the true pre-departure window and that leave enough history before them to compute DOA (per experiment's minimum-history rule). Within the survivor group and non-survivor group SEPARATELY, draw one placebo window per project uniformly at random from its own valid-window set (not pooled across groups, to preserve the group's compositional confounds while breaking the temporal specificity of the diffusion signal) — implement with a fixed, recorded random seed for reproducibility, and repeat with >=3 different seeds to report seed-sensitivity of the placebo result rather than a single draw. Recompute the diffusion score (founder authorship-share, distinct non-founder DOA-owner count) for each placebo window using the exact scoring function the experiment used for the true window.\n\nStep 2 — Refit identical statistical tests on placebo data: (a) the matched-pairs comparison (same star/fork/contributor-count buckets used in the true-window analysis, survival-rate ratio with 95% CI via bootstrap or exact binomial per bucket then pooled), and (b) the logistic/ordinal regression (diffusion predictors + stars/forks/contributor-count/language/license controls, BH-corrected p-values), using the SAME model specification, bucket boundaries, and covariate set as the true-window analysis (read these from the experiment/prior evaluation artifact's config so nothing is re-derived ad hoc). Report point estimates and CIs for placebo runs alongside the true-window numbers already computed upstream (recompute the true-window numbers too if not directly available, using the same code path, so the comparison is apples-to-apples on identical statistical code).\n\nStep 3 — Falsification verdict: Compute (i) the ratio and CI-overlap between true-window and placebo-window survival-rate lift, (ii) the ratio/overlap between true-window and placebo regression coefficients (or standardized effect sizes) for the diffusion predictors, and (iii) a formal test of the difference (e.g. permutation test comparing the true-window effect estimate against the empirical distribution of the placebo effect across all seeds/draws, or a paired bootstrap difference-in-effect with CI excluding 0). Classify each as PASS (true effect significantly exceeds placebo, CI of the difference excludes 0), WEAK (true effect nominally larger but CIs overlap substantially), or FAIL (placebo effect matches or exceeds true effect) — this directly operationalizes success_criteria #3's 'significantly weaker or absent'.\n\nStep 4 — Stratified robustness: Re-run the true-window matched-pairs comparison and regression separately within each of the 6 languages and within each popularity-bucket stratum used upstream. Report per-stratum effect size, CI, and n; flag any stratum with n too small (e.g. <10 founder-TFDD projects) as underpowered rather than silently omitting it or overinterpreting a wide CI. Compute a heterogeneity check (e.g. Cochran's Q or simple range-of-effect-sizes-vs-pooled-CI) to state whether the pooled effect is driven by one ecosystem/bucket.\n\nStep 5 — Pipeline-validity sanity check against Avelino et al.'s published aggregates: On the evaluation's own corpus (or the experiment's full corpus before founder-only filtering, whichever the upstream data provides), compute (a) fraction of projects experiencing at least one TFDD (compare to Avelino et al.'s ~16%, i.e. 315/1932), (b) fraction of TFDDs occurring at TF=1 (compare to their 66%), and (c) unconditioned TFDD survival rate under the 18-month Active/Inactive criterion (compare to their 41%, 128/315). Report each as a point estimate with a 95% CI (Wilson or bootstrap) and an explicit PASS/CONCERN flag: PASS if the CI contains or is within ~1.5x relative distance of Avelino et al.'s figure, CONCERN otherwise — noting that some divergence is expected given the corpus here is a founder-only, stratified-sampled subset rather than Avelino et al.'s full top-500-per-language corpus, and document that expected-divergence caveat rather than treating any mismatch as an automatic pipeline bug.\n\nStep 6 — Regression calibration: Using the true-window regression fit upstream (or refit here with the same specification if only predictions/labels are available), compute a bootstrap-based calibration curve (predicted-probability deciles vs observed survival rate) with >=1000 resamples, report the Brier score and a bootstrap 95% CI on each regression coefficient (to cross-check the significance claims already made in success_criteria #1-2 rather than trust a single-fit p-value), and report AUC/C-statistic with bootstrap CI as an overall discrimination summary.\n\nAll numeric outputs (effect sizes, CIs, p-values, PASS/WEAK/FAIL/CONCERN flags per check) go into eval_out.json with clear keys per check (placebo_test, stratified_robustness, pipeline_validity, calibration), plus a top-level overall_verdict field summarizing whether success_criteria #3 (falsification/specificity) is supported, and a brief free-text 'caveats' field listing any data limitations encountered (e.g. missing time series forcing partial checks, small strata, corpus-size mismatches vs Avelino et al.).",
  "metrics_justification": "The hypothesis's central falsifiable claim (success_criteria #3) is that the diffusion-survival association is specific to the immediate pre-TFDD window, not an artifact of generally-active projects having generally-diffused authority throughout their history. A placebo/shuffle test relocating the measurement window is the direct, pre-registered way to test this: if the effect survives equally well at a random earlier point in the same projects' histories, the 'trajectory-of-decentralization' story collapses into a restatement of 'diffused projects are diffused' rather than a genuine leading indicator, which is exactly the alternative explanation the hypothesis must rule out to be a real contribution beyond Avelino et al.'s snapshot null. Within-group (survivor vs non-survivor) random window selection is essential rather than pooled random selection, because pooling would also shuffle away the group-level confounds (size, age, ecosystem) that the matched-pairs design is meant to hold fixed — the placebo must isolate temporal specificity, not reintroduce compositional differences.\n\nStratifying by language and popularity bucket addresses external validity and the risk that a pooled result is a Simpson's-paradox artifact of one dominant, unusually diffusion-friendly ecosystem (e.g. a language with strong bus-factor norms) rather than a general phenomenon — directly relevant since Avelino et al.'s own corpus spans 6 languages and reports meaningful cross-language variation in TF dynamics.\n\nThe pipeline-validity sanity check against Avelino et al.'s three headline aggregate statistics (TFDD rate, TF=1 share, 41% survival) is the cheapest and highest-value check available: since this evaluation's entire causal claim rests on a faithful reimplementation of Avelino et al.'s validated DOA/TF/TFDD algorithm, any large divergence from their published numbers is a red flag that the reimplementation has a bug (e.g. wrong DOA formula, wrong silence-threshold, wrong Active/Inactive state transition) that would invalidate every downstream statistical result, independent of whether the diffusion hypothesis itself is true or false — this is the difference between 'the hypothesis is false' and 'the code is broken,' which the executor MUST be able to distinguish.\n\nBootstrap calibration and coefficient CIs address the risk that success_criteria #1-2's significance claims rest on a single point-estimate p-value from a possibly small, unbalanced founder-TFDD sample; reporting Brier score, AUC with CI, and a calibration curve gives a fuller, harder-to-game picture of whether the regression's predictive claim is robust to resampling noise, which is the standard rigor bar for a claim that is meant to generalize to foundations' actionable pre-departure predictions (per the motivation section) rather than only describe this specific sample."
}
```

### [5] TOOL RESULT — Write · 2026-08-21 16:26:39 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_plan/gen_plan_evaluation_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Placebo-Window Falsification and Robustness Audit\",\n  \"summary\": \"Evaluates the pre-departure authority-diffusion experiment by re-running the matched-pairs/regression tests with randomly relocated 'pre-departure windows' (within-group shuffle, survivors vs non-survivors separately), comparing effect sizes/CIs against the true-window results, stratifying by language and popularity bucket, sanity-checking the DOA/TF/TFDD pipeline against Avelino et al.'s published aggregate statistics (TFDD~16%, 66% at TF=1, 41% survival), and bootstrapping calibration/CIs for the survival regression to support or refute success_criteria #1-3.\",\n  \"runpod_compute_profile\": \"cpu_heavy\",\n  \"metrics_descriptions\": \"This evaluation consumes the upstream EXPERIMENT artifact's per-repo longitudinal outputs: (a) yearly DOA/TF/TFDD event tables per project, (b) the identified founder-only TFDD timestamp per project, (c) the per-window time series of founder commit-share and count of non-founder DOA file-owners, (d) the true pre-departure (6-12mo) diffusion score and the survival label (18-month Active/Inactive/graded outcome per Avelino et al.), and (e) covariates (stars, forks, contributor count, language, license). Load these from the experiment's output JSON/CSV; if any field is missing (e.g. no full time series, only the single true-window score), FLAG this explicitly as a pipeline gap in eval_out.json rather than fabricating a window series, and fall back to whatever partial checks the available data supports.\\n\\nStep 1 — Reconstruct the placebo/shuffle test (success_criteria #3): For each project with a founder-TFDD, enumerate all valid same-length (6-12 month) windows in its pre-TFDD history that do NOT overlap the true pre-departure window and that leave enough history before them to compute DOA (per experiment's minimum-history rule). Within the survivor group and non-survivor group SEPARATELY, draw one placebo window per project uniformly at random from its own valid-window set (not pooled across groups, to preserve the group's compositional confounds while breaking the temporal specificity of the diffusion signal) — implement with a fixed, recorded random seed for reproducibility, and repeat with >=3 different seeds to report seed-sensitivity of the placebo result rather than a single draw. Recompute the diffusion score (founder authorship-share, distinct non-founder DOA-owner count) for each placebo window using the exact scoring function the experiment used for the true window.\\n\\nStep 2 — Refit identical statistical tests on placebo data: (a) the matched-pairs comparison (same star/fork/contributor-count buckets used in the true-window analysis, survival-rate ratio with 95% CI via bootstrap or exact binomial per bucket then pooled), and (b) the logistic/ordinal regression (diffusion predictors + stars/forks/contributor-count/language/license controls, BH-corrected p-values), using the SAME model specification, bucket boundaries, and covariate set as the true-window analysis (read these from the experiment/prior evaluation artifact's config so nothing is re-derived ad hoc). Report point estimates and CIs for placebo runs alongside the true-window numbers already computed upstream (recompute the true-window numbers too if not directly available, using the same code path, so the comparison is apples-to-apples on identical statistical code).\\n\\nStep 3 — Falsification verdict: Compute (i) the ratio and CI-overlap between true-window and placebo-window survival-rate lift, (ii) the ratio/overlap between true-window and placebo regression coefficients (or standardized effect sizes) for the diffusion predictors, and (iii) a formal test of the difference (e.g. permutation test comparing the true-window effect estimate against the empirical distribution of the placebo effect across all seeds/draws, or a paired bootstrap difference-in-effect with CI excluding 0). Classify each as PASS (true effect significantly exceeds placebo, CI of the difference excludes 0), WEAK (true effect nominally larger but CIs overlap substantially), or FAIL (placebo effect matches or exceeds true effect) — this directly operationalizes success_criteria #3's 'significantly weaker or absent'.\\n\\nStep 4 — Stratified robustness: Re-run the true-window matched-pairs comparison and regression separately within each of the 6 languages and within each popularity-bucket stratum used upstream. Report per-stratum effect size, CI, and n; flag any stratum with n too small (e.g. <10 founder-TFDD projects) as underpowered rather than silently omitting it or overinterpreting a wide CI. Compute a heterogeneity check (e.g. Cochran's Q or simple range-of-effect-sizes-vs-pooled-CI) to state whether the pooled effect is driven by one ecosystem/bucket.\\n\\nStep 5 — Pipeline-validity sanity check against Avelino et al.'s published aggregates: On the evaluation's own corpus (or the experiment's full corpus before founder-only filtering, whichever the upstream data provides), compute (a) fraction of projects experiencing at least one TFDD (compare to Avelino et al.'s ~16%, i.e. 315/1932), (b) fraction of TFDDs occurring at TF=1 (compare to their 66%), and (c) unconditioned TFDD survival rate under the 18-month Active/Inactive criterion (compare to their 41%, 128/315). Report each as a point estimate with a 95% CI (Wilson or bootstrap) and an explicit PASS/CONCERN flag: PASS if the CI contains or is within ~1.5x relative distance of Avelino et al.'s figure, CONCERN otherwise — noting that some divergence is expected given the corpus here is a founder-only, stratified-sampled subset rather than Avelino et al.'s full top-500-per-language corpus, and document that expected-divergence caveat rather than treating any mismatch as an automatic pipeline bug.\\n\\nStep 6 — Regression calibration: Using the true-window regression fit upstream (or refit here with the same specification if only predictions/labels are available), compute a bootstrap-based calibration curve (predicted-probability deciles vs observed survival rate) with >=1000 resamples, report the Brier score and a bootstrap 95% CI on each regression coefficient (to cross-check the significance claims already made in success_criteria #1-2 rather than trust a single-fit p-value), and report AUC/C-statistic with bootstrap CI as an overall discrimination summary.\\n\\nAll numeric outputs (effect sizes, CIs, p-values, PASS/WEAK/FAIL/CONCERN flags per check) go into eval_out.json with clear keys per check (placebo_test, stratified_robustness, pipeline_validity, calibration), plus a top-level overall_verdict field summarizing whether success_criteria #3 (falsification/specificity) is supported, and a brief free-text 'caveats' field listing any data limitations encountered (e.g. missing time series forcing partial checks, small strata, corpus-size mismatches vs Avelino et al.).\",\n  \"metrics_justification\": \"The hypothesis's central falsifiable claim (success_criteria #3) is that the diffusion-survival association is specific to the immediate pre-TFDD window, not an artifact of generally-active projects having generally-diffused authority throughout their history. A placebo/shuffle test relocating the measurement window is the direct, pre-registered way to test this: if the effect survives equally well at a random earlier point in the same projects' histories, the 'trajectory-of-decentralization' story collapses into a restatement of 'diffused projects are diffused' rather than a genuine leading indicator, which is exactly the alternative explanation the hypothesis must rule out to be a real contribution beyond Avelino et al.'s snapshot null. Within-group (survivor vs non-survivor) random window selection is essential rather than pooled random selection, because pooling would also shuffle away the group-level confounds (size, age, ecosystem) that the matched-pairs design is meant to hold fixed — the placebo must isolate temporal specificity, not reintroduce compositional differences.\\n\\nStratifying by language and popularity bucket addresses external validity and the risk that a pooled result is a Simpson's-paradox artifact of one dominant, unusually diffusion-friendly ecosystem (e.g. a language with strong bus-factor norms) rather than a general phenomenon — directly relevant since Avelino et al.'s own corpus spans 6 languages and reports meaningful cross-language variation in TF dynamics.\\n\\nThe pipeline-validity sanity check against Avelino et al.'s three headline aggregate statistics (TFDD rate, TF=1 share, 41% survival) is the cheapest and highest-value check available: since this evaluation's entire causal claim rests on a faithful reimplementation of Avelino et al.'s validated DOA/TF/TFDD algorithm, any large divergence from their published numbers is a red flag that the reimplementation has a bug (e.g. wrong DOA formula, wrong silence-threshold, wrong Active/Inactive state transition) that would invalidate every downstream statistical result, independent of whether the diffusion hypothesis itself is true or false — this is the difference between 'the hypothesis is false' and 'the code is broken,' which the executor MUST be able to distinguish.\\n\\nBootstrap calibration and coefficient CIs address the risk that success_criteria #1-2's significance claims rest on a single point-estimate p-value from a possibly small, unbalanced founder-TFDD sample; reporting Brier score, AUC with CI, and a calibration curve gives a fuller, harder-to-game picture of whether the regression's predictive claim is robust to resampling noise, which is the standard rigor bar for a claim that is meant to generalize to foundations' actionable pre-departure predictions (per the motivation section) rather than only describe this specific sample.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [6] ASSISTANT · 2026-08-21 16:26:41 UTC

```
Plan written to `.terminal_claude_agent_struct_out.json` — it details the placebo/shuffle falsification test (within-group random window relocation), stratified robustness checks, a pipeline-validity sanity check against Avelino et al.'s published aggregates, and bootstrap calibration for the regression.
```
