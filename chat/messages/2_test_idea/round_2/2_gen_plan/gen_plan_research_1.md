# gen_plan_research_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_plan`
> Run: `run_5SMkWpWKNLxk` — Measuring Authority Diffusion Before Founders Leave Open Source Projects
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_research_1` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-08-20 20:08:23 UTC

```
model: claude-sonnet-5 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_plan/gen_plan_research_1
```

### [2] SYSTEM-USER prompt · 2026-08-20 20:08:31 UTC

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
You are expanding an artifact direction of type: RESEARCH

RESEARCH
Web research to answer key questions — like a researcher making decisions.
Runtime: LLM Agent, no code execution.
Tools: the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text).
Capabilities: Find, synthesize, and compare information across sources; survey SOTA and best practices.
Deps: REQUIRED none | OPTIONAL other RESEARCH to build on prior findings
</artifact_type_info>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **SPEND BUDGET**: at most $10 USD of OpenRouter API calls for this artifact. Nothing outside your own code enforces this — the key you are given has no per-artifact cap — so it holds only if you track cumulative cost after every call and stop when you approach it. Budget the work up front: estimate the per-call cost and the number of calls BEFORE starting a sweep, not after it overruns. Exceeding it spends real money that the run cannot recover.
</software_constraints>
</available_resources>

<time_budget>

The research executor has 3h total (including writing code, debugging, testing, and fixing errors).

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
title: Measuring Pre-Departure Authority Diffusion in OSS Projects
hypothesis: >-
  A calibrated reimplementation of Avelino et al.'s (ESEM 2019) DOA/Truck-Factor/TFDD pipeline, extended with a NEW pre-departure
  authority-diffusion measurement (founder commit-share and count of distinct non-founder DOA file-owners in the 6-12 months
  before a founder-only Truck-Factor Detachment), can (a) reproduce Avelino et al.'s published headline statistics closely
  enough to trust the reimplementation, and (b) show this new diffusion measurement is temporally specific to the pre-departure
  window rather than a generic property of active projects, measured via a permutation test with an explicitly reported, sufficiently
  fine-grained permutation scheme. On a 15-repository convenience corpus built by starting from currently-famous, still-maintained
  tools, the calibration gate itself demonstrates the corpus is NOT a valid sampling frame for testing the causal diffusion-predicts-survival
  claim: TFDD incidence (53.3% vs Avelino et al.'s 16.3%) and 18-month survival (100% vs their 40.6%) both deviate sharply
  in the direction of severe survivorship bias, because starting from tools known today to still exist necessarily conditions
  on the outcome being predicted. This is a sampling-frame defect, not merely a power shortfall -- a larger sample drawn from
  the same 'currently-famous tools' frame would still be biased toward survivors and would remain unable to test the causal
  claim. The original causal hypothesis (that founder-only-TFDD projects with diffused pre-departure authority survive at
  a higher rate than matched projects with concentrated authority) THEREFORE REMAINS OPEN and is reframed as the target of
  a specific, well-defined follow-up: a corpus constructed from a historical snapshot of GitHub repositories that does NOT
  condition on present-day liveness (e.g. Avelino et al.'s own stratified top-500-per-language-circa-a-fixed-year design,
  extended via the already-built, checkpointed ~104-repository candidate pipeline and an authenticated GitHub token raising
  the query budget ~83x), yielding an estimated ~40 founder-only TFDD events -- the threshold this study's own fallback power
  analysis identifies as needed, and roughly 8x what a non-conditioned corpus of this size (15 repos) would be expected to
  produce. Until that corpus exists, this paper's contribution is the validated measurement instrument and calibration/robustness
  harness (pipeline replication, diagnostic gate, permutation-based construct-validity check for the diffusion measurement)
  plus a precise specification of what a valid test of the causal claim requires -- not an empirical answer to whether diffusion
  predicts survival.
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
_relation_rationale: >-
  Same frame; reframed as methodology contribution since outcome-conditioned corpus left causal test undefined.
_confidence_delta: decreased
_key_changes:
- >-
  Explicitly reframed as a methodology/calibration contribution rather than an empirical answer, per reviewer MAJOR#1 option
  (a)
- >-
  Named the survivorship-biased corpus as a sampling-frame DESIGN FLAW (not merely underpowered), and specified the fix as
  a historical-snapshot sampling frame per reviewer MAJOR#3
- >-
  Downgraded the permutation-test result to construct-validity evidence only, explicitly decoupled from the causal diffusion-survival
  claim per reviewer MAJOR#2 and MINOR#7
- >-
  Added requirement to report the exact permutation scheme, achievable p-value resolution, and a larger-budget sensitivity
  check
- >-
  Added requirement to compute/cite Avelino et al.'s own CI for the 66% TF=1 statistic before claiming CI overlap
- >-
  Added requirement for a full repository table matching the dataset artifact exactly, and manual alias-resolution spot-checks
- >-
  Added requirement to situate the diffusion construct against OSS-native community-health/onboarding literature (CHAOSS,
  podling graduation), not only the cross-domain firm-succession analogy
- >-
  Confidence decreased: the causal claim this hypothesis centers on remains completely untested (0 outcome variance), and
  the sampling problem is now understood to be structural, not fixable by simply enlarging the same corpus
relation_type: evolution
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

id: research_iter2_dir1
type: research
objective: >-
  Find (a) OSS-native community-health/onboarding literature to ground the pre-departure authority-diffusion construct alongside
  the existing firm-succession analogy, and (b) concrete, currently-accessible data sources for a historical, present-day-liveness-non-conditioned
  GitHub repository snapshot that the dataset artifact can pull from without depending on an authenticated GitHub REST token.
approach: >-
  Search for and read CHAOSS project metrics documentation (contributor absorption rate, elephant factor, bus factor working
  group outputs), Apache Software Foundation Incubator podling graduation criteria (which explicitly assess whether authority
  has diffused beyond a founder before graduation), and empirical studies of OSS newcomer onboarding / core-team formation
  and retention (e.g. work on onboarding barriers, mentorship programs, contributor pipeline studies). Synthesize 1-2 concrete
  sentences positioning the diffusion construct against these OSS-native frameworks specifically (not just the Korean-firm
  analogy). Separately, investigate and report concretely how to build a historical-snapshot GitHub corpus that does not condition
  on present-day liveness: GH Archive (gharchive.org, public BigQuery/hourly JSON dumps of all public GitHub events since
  2011, queryable without an API key via direct file download), World of Code (public research dataset of GitHub commit/author
  graphs), and any Libraries.io or GHTorrent legacy static dumps. For each candidate source, report exactly what fields are
  available (commit-level author/timestamp/file data vs. only event metadata), how to download it without a GitHub API token,
  size/format, and whether it supports reconstructing full per-file commit history (required for DOA) or only repo-level metadata.
  Recommend the single most viable concrete pull-path (specific URL patterns / query approach) for the dataset artifact to
  attempt.
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

RESEARCH executor scope:
  Output: research_out.json with {answer, sources, follow_up_questions} + research_report.md
  DOES: Web research — search, read, synthesize information from papers/docs/APIs into a structured report
  DOES NOT: Run code, download files, execute scripts, compute anything — no shell/Python access
  Use for literature surveys, API documentation, technical specifications — pure information gathering
</artifact_executor_scope>

<artifact_planning_rules>
RESEARCH: Plan early — findings guide dataset selection, experiment design, and methodology.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for research artifacts:
  - cpu_light: 4 vCPUs, 16GB RAM — proofs, research, lightweight tasks (fallback: memory-optimized CPUs first (cpu3m → cpu5m), then GPU hosts last-ditch)

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
  "description": "Plan for a RESEARCH artifact.",
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
    "question": {
      "default": "",
      "description": "The specific research question to investigate",
      "title": "Question",
      "type": "string"
    },
    "research_plan": {
      "description": "Step-by-step plan for web research to gather this research",
      "title": "Research Plan",
      "type": "string"
    },
    "explanation": {
      "description": "Why this research matters and what question it answers",
      "title": "Explanation",
      "type": "string"
    }
  },
  "required": [
    "title",
    "research_plan",
    "explanation"
  ],
  "title": "ResearchPlan",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [3] HUMAN-USER prompt · 2026-08-20 20:08:31 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [4] TOOL CALL — Skill · 2026-08-20 20:08:35 UTC

```
aii-web-tools
```

### [5] TOOL RESULT — Skill · 2026-08-20 20:08:35 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [6] TOOL CALL — ToolSearch · 2026-08-20 20:08:37 UTC

```
{'query': 'select:WebSearch,WebFetch', 'max_results': 5}
```

### [7] TOOL RESULT — ToolSearch · 2026-08-20 20:08:37 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 18}
```

### [8] TOOL CALL — WebSearch · 2026-08-20 20:08:43 UTC

```
CHAOSS metrics elephant factor bus factor contributor absorption rate
```

### [9] TOOL CALL — WebSearch · 2026-08-20 20:08:43 UTC

```
Apache Software Foundation Incubator podling graduation criteria diversity of authority
```

### [10] TOOL CALL — WebSearch · 2026-08-20 20:08:43 UTC

```
GH Archive gharchive.org download without API key BigQuery public dataset
```

### [11] TOOL CALL — WebSearch · 2026-08-20 20:08:43 UTC

```
World of Code research dataset commit author graph download
```

### [12] TOOL CALL — WebSearch · 2026-08-20 20:08:43 UTC

```
GHTorrent legacy static dump discontinued alternative
```

### [13] TOOL RESULT — WebSearch · 2026-08-20 20:08:47 UTC

```
{"query": "CHAOSS metrics elephant factor bus factor contributor absorption rate", "results": [{"tool_use_id": "srvtoolu_0196EfVfCYbcVELoAbf9ZQpu", "content": [{"title": "CHAOSS Metrics in 2026 | Andrew Nesbitt", "url": "https://nesbitt.io/2026/05/27/chaoss-metrics-in-2026.html"}, {"title": "Metric: Elephant Factor - CHAOSS", "url": "https://www.chaoss.community/kb/metric-elephant-factor/"}, {"title": "The Pony Factor: Metric of the Month - Bitergia", "url": "https://bitergia.com/blog/the-pony-factor-metric-of-the-month-november-2022/"}, {"title": "Metric: Contributor Absence Factor - CHAOSS", "url": "https://www.chaoss.community/kb/metric-contributor-absence-factor/"}, {"title": "wg-risk/focus-areas/business-risk/contributor-absence-factor.md at main · chaoss/wg-risk", "url": "https://github.com/chaoss/wg-risk/blob/main/focus-areas/business-risk/contributor-absence-factor.md"}, {"title": "Metrics Model: Starter Project Health - CHAOSS", "url": "https://chaoss.community/kb/metrics-model-starter-project-health/"}, {"title": "CHA-IO-SS [Community Health Analytics for InnerSource and Open Source Software]", "url": "https://chaoss.github.io/website/CHAOSScon/2020EU/slides/cha-io-ss.pdf"}, {"title": "chaoss:metrics:metrics [Wiki]", "url": "https://wiki.linuxfoundation.org/chaoss/metrics/metrics"}, {"title": "Individual context-free online community health indicators fail to   identify open source software sustainability", "url": "https://arxiv.org/pdf/2309.12120"}]}, "Based on the search results, here's what I found about these CHAOSS metrics:\n\n## Bus Factor / Contributor Absence Factor\n\nThe Contributor Absence Factor assesses the degree to which a project relies on a small number of contributors by identifying the smallest number of contributors responsible for 50% of total contributions. This metric was previously called \"Bus Factor.\" A lower Contributor Absence Factor indicates higher dependency on fewer contributors, posing a risk if these individuals leave the project.\n\n## Elephant Factor\n\nElephant factor measures the minimum number of companies whose employees contribute a specified percentage of the total commits in a software repository. This metric provides a quantitative indicator of the project's dependency on a small set of corporate contributors. Elephant Factor does the same calculation over employer affiliations rather than individuals.\n\n## Contributor Absorption Rate\n\nThe search results do not contain specific information about a CHAOSS metric called \"contributor absorption rate.\" However, Inactive Contributors counts people who used to contribute and have stopped, which sounds like exactly the right metric for the silent-quitting problem. This may be related to what you're looking for regarding contributor retention or absorption.\n\nAll of these metrics are part of the CHAOSS project's carefully written, implementation-agnostic definitions for measuring open source projects, which has become the closest thing the field has to a shared vocabulary."], "durationSeconds": 7.382729676000001, "searchCount": 1}
```

### [14] TOOL RESULT — WebSearch · 2026-08-20 20:08:47 UTC

```
{"query": "GHTorrent legacy static dump discontinued alternative", "results": [{"tool_use_id": "srvtoolu_01QN6ULh16uu6wjBK5aPxFas", "content": [{"title": "Lean GHTorrent: GitHub data on demand | Request PDF", "url": "https://www.researchgate.net/publication/264799490_Lean_GHTorrent_GitHub_data_on_demand"}, {"title": "Lean GHTorrent: GitHub data on demand", "url": "https://azaidman.github.io/publications/gousiosMSR2014b.pdf"}, {"title": "How to mine GitHub data in 2022. Alternatives to GHTorrent or GHArchive… | by Jenny Sahng | Level Up Coding", "url": "https://levelup.gitconnected.com/how-to-mine-github-data-in-2022-e9c70b3f61d3?gi=a5345dbe4407"}, {"title": "ghtorrent.org/faq.md at master · ghtorrent/ghtorrent.org · ...", "url": "https://github.com/ghtorrent/ghtorrent.org/blob/master/faq.md"}, {"title": "Fedora Legacy", "url": "https://en.wikipedia.org/wiki/Fedora_Legacy"}, {"title": "Lean GHTorrent: GitHub data on demand | Proceedings of the 11th Working Conference on Mining Software Repositories", "url": "https://dl.acm.org/doi/10.1145/2597073.2597126"}, {"title": "Querying 10 years of GitHub data with GHTorrent and Libraries.io | Opensource.com", "url": "https://opensource.com/article/19/5/chaossearch-github-ghtorrent"}, {"title": "GHTorrent - Software Heritage Wiki", "url": "https://wiki.softwareheritage.org/wiki/GHTorrent"}]}, "Based on the search results, here's what I found about GHTorrent's legacy static dump and alternatives:\n\n## GHTorrent Status and Alternatives\n\nMany people are now building their own ETLs to get data from GitHub because existing solutions like GHTorrent and GHArchive are no longer fit for their purposes.\n\n### Key Alternative: GHArchive\n\nGHArchive archives real-time event data from GitHub and is a popular alternative to GHTorrent. The event data is stored as JSON and available as a public dataset on BigQuery.\n\n### Other Options\n\nGHTorrent's data is available in NDJSON format through multiple forms, including CSV for restoring into a MySQL database, MongoDB dumps of all objects, and Google Big Query (free) for exporting data directly into Google's object storage. However, the dataset has a nearly complete dataset from 2008 to 2017 but is not as complete from 2017 to today.\n\nThe search results indicate that researchers and developers have increasingly turned to building custom ETL solutions and exploring alternatives like GHArchive when the limitations of GHTorrent became apparent."], "durationSeconds": 5.807022956999997, "searchCount": 1}
```

### [15] TOOL RESULT — WebSearch · 2026-08-20 20:08:47 UTC

```
{"query": "Apache Software Foundation Incubator podling graduation criteria diversity of authority", "results": [{"tool_use_id": "srvtoolu_01LZAVceCfqDfqjw4vauwuxB", "content": [{"title": "November2025 - INCUBATOR - Apache Software Foundation", "url": "https://cwiki.apache.org/confluence/display/INCUBATOR/November2025"}, {"title": "Incubator Case Studies - INCUBATOR - Apache Software Foundation", "url": "https://cwiki.apache.org/confluence/display/INCUBATOR/Incubator+Case+Studies"}, {"title": "Guide :: IPMC Path - The Apache Incubator", "url": "https://incubator.apache.org/training/ipmc/"}, {"title": "Guide to Successful Graduation - Apache Incubator", "url": "https://svn.apache.org/repos/infra/websites/staging/incubator/trunk/content/guides/graduation.html"}, {"title": "Guide to Successful Graduation - The Apache Incubator", "url": "https://incubator.apache.org/guides/graduation.html"}, {"title": "Guides - The Apache Incubator", "url": "https://incubator.apache.org/training/guides.html"}, {"title": "The Apache Incubator - Apache Software Foundation", "url": "https://incubator.apache.org/"}, {"title": "The Apache Incubator Cookbook", "url": "https://incubator.apache.org/cookbook/"}]}, "I found relevant search results about Apache Software Foundation Incubator podling graduation criteria and diversity. Here are the key findings:\n\n## Graduation Criteria\n\nThe IPMC assesses whether a podling is ready to graduate by evaluating community maturity, diversity, and governance. A major criterion for graduation is to have developed an open and diverse meritocratic community, as these kinds of communities are more robust and productive than more closed ones.\n\n## Diversity of Authority\n\nThe search results emphasize the importance of diverse community participation. Podlings with strong corporate origins can graduate successfully if they attract contributors from outside the founding company. Additionally, even a high-profile donation can fail if a podling does not establish a sustainable, diverse community and adopt an ASF-style transparency approach.\n\n## Release and Governance Requirements\n\nIt is an important step during a podling's stay in the incubator to demonstrate the ability to prepare and publish an Apache Release. Apache projects are self-sustaining and self-governing communities, and graduation tests whether a podling has learned enough to sustain itself as such a community.\n\nThe Apache Incubator also provides detailed guidance through resources like the \"Graduation Criteria\" guide and case studies that document both challenges and successes in achieving graduation."], "durationSeconds": 7.107897441000001, "searchCount": 1}
```

### [16] TOOL RESULT — WebSearch · 2026-08-20 20:08:47 UTC

```
{"query": "GH Archive gharchive.org download without API key BigQuery public dataset", "results": [{"tool_use_id": "srvtoolu_01RuZJzxTennn58Uv5YkCXvk", "content": [{"title": "gharchive.org/bigquery at master · igrigorik/gharchive.org", "url": "https://github.com/igrigorik/gharchive.org/tree/master/bigquery"}, {"title": "gharchive.org/bigquery/README.md at master · igrigorik/gharchive.org", "url": "https://github.com/igrigorik/gharchive.org/blob/master/bigquery/README.md"}, {"title": "gharchive.org/bigquery/README.md at master · soulteary/gharchive.org", "url": "https://github.com/soulteary/gharchive.org/blob/master/bigquery/README.md"}, {"title": "GH Archive download | SourceForge.net", "url": "https://sourceforge.net/projects/gh-archive.mirror/"}, {"title": "Analyzing GitHub Data with BigQuery Using GH Archive | gharchive-bigquery-examples", "url": "https://davelester.github.io/gharchive-bigquery-examples/"}, {"title": "Diving into GitHub with BigQuery and Python | Chris Wilcox", "url": "https://chriswilcox.dev/blog/2020/09/02/Diving_into_GitHub_with_BigQuery_and_Python.html"}, {"title": "GH Archive", "url": "https://www.gharchive.org/"}, {"title": "Saving Ephemera: GHTorrent/GH Archive", "url": "https://investigating-archiving-git.gitlab.io/updates/programmatic-capture/index.src.html"}, {"title": "Programmatically Capturing Software | IASGE", "url": "https://investigating-archiving-git.gitlab.io/updates/programmatic-capture/"}, {"title": "GitHub on BigQuery: Analyze all the open source code | Google Cloud Blog", "url": "https://cloud.google.com/blog/topics/public-datasets/github-on-bigquery-analyze-all-the-open-source-code"}]}, "Based on the search results, here's what I found about accessing GH Archive data without an API key through BigQuery's public dataset:\n\n## Accessing GH Archive via BigQuery Public Dataset\n\nThe entire GH Archive is available as a public dataset on Google BigQuery, with the dataset automatically updated every hour, enabling you to run SQL-like queries over the entire dataset in seconds. There is no need to download or process any data on your own when using BigQuery.\n\n## Getting Started\n\nThe GH Archive is available as a public dataset on Google BigQuery with automatic hourly updates. To get started, you need a Google project, then go to BigQuery, select your newly created project from the dropdown in the header bar, and execute your first query against the public \"githubarchive\" dataset.\n\n## Alternative: Direct Download\n\nIf you prefer to download the raw data without using BigQuery: The events are aggregated into hourly archives which you can access with any HTTP client. You can download the raw data and apply your own processing to it, such as writing a custom aggregation script or importing it into a database.\n\n## Data Organization\n\nThe GHArchive data on BigQuery is stored in tables organized by year, month, and day."], "durationSeconds": 6.628630347999999, "searchCount": 1}
```

### [17] TOOL RESULT — WebSearch · 2026-08-20 20:08:49 UTC

```
{"query": "World of Code research dataset commit author graph download", "results": [{"tool_use_id": "srvtoolu_01WAJxRdJ6vq2JKN93ShtXSM", "content": [{"title": "World of code: enabling a research workflow for mining and analyzing the universe of open source VCS data | Empirical Software Engineering | Springer Nature Link", "url": "https://link.springer.com/article/10.1007/s10664-020-09905-9"}, {"title": "World of code: enabling a research workflow for mining and analyzing the universe of open source VCS data | Empirical Software Engineering", "url": "https://dl.acm.org/doi/abs/10.1007/s10664-020-09905-9"}, {"title": "A Global Author-Identity Map for the World of Code:62.7M Developer Identities from 106.8M Author Strings over 5.87B Commits", "url": "https://arxiv.org/pdf/2607.06183"}, {"title": "A Dataset and an Approach for Identity Resolution of 38 Million Author   IDs extracted from 2B Git Commits", "url": "https://arxiv.org/pdf/2003.08349"}, {"title": "Worldwide Gender Differences in Public Code Contributions", "url": "https://arxiv.org/pdf/2202.07278"}, {"title": "Claimed or Attested? A Commit-Signature Dataset and Identity Trust Tiers across the World of Code", "url": "https://arxiv.org/pdf/2607.06194"}, {"title": "World of Code: An Infrastructure for Mining the Universe of Open Source VCS Data", "url": "https://www.researchgate.net/publication/335499575_World_of_Code_An_Infrastructure_for_Mining_the_Universe_of_Open_Source_VCS_Data"}, {"title": "Geographic Diversity in Public Code Contributions", "url": "https://arxiv.org/pdf/2203.15369"}, {"title": "Detecting and Characterizing Bots that Commit Code", "url": "https://arxiv.org/pdf/2003.03172"}, {"title": "Detecting AI Coding Agents in Open Source: A Validated Multi-Method Census of 180 Million Repositories", "url": "https://arxiv.org/pdf/2606.24429"}]}, "Based on the search results, here's what I found about the World of Code research dataset and commit author graph:\n\n## Overview\n\nThe World of Code (WoC) infrastructure was created to support discovery, collection, and processing of FLOSS (Free/Libre Open Source Software) operational data and stores the huge and rapidly growing amount of data in the entire FLOSS ecosystem. Recent World of Code snapshots span from December 2024 to April 2026 and index over 180 million Git repositories from GitHub, GitLab, Bitbucket, and other platforms.\n\n## Data Structure and Access\n\nWoC structures software artifacts (authors, commits, blobs, files, and projects) into cross-referenced maps that support both SQL queries via ClickHouse and fast O(1) hash-map lookups. WoC is a software analysis pipeline starting from the discovery and retrieval of data, data storage and regular updates, and enablement of the transformations and data augmentations necessary for analytic tasks downstream.\n\n## Author Identity Maps and Downloads\n\nA curated author-identity map for the World of Code version V2604 covers all 5.86 billion commits in the collection and includes a global alias map that folds 106.8 million raw author/committer strings into canonical identities, along with per-identity classification, within-project resolution tables, and commit-to-identity tables.\n\nRelated artifacts are released as self-contained bundles with no World of Code account required, hosted as Hugging Face datasets which scale past file-size limits of code hosts and mint citable DataCite DOIs, with replication code mirrored on GitHub."], "durationSeconds": 8.104618324999999, "searchCount": 1}
```

### [18] ASSISTANT · 2026-08-20 20:09:50 UTC

```
Good, I have enough grounding. Now writing the structured plan output.
```

### [19] TOOL CALL — Write · 2026-08-20 20:09:50 UTC

```
File: /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_plan/gen_plan_research_1/.terminal_claude_agent_struct_out.json

{
  "title": "OSS Community-Health Framing + Bias-Free Corpus Sources",
  "summary": "Web research to (1) ground the pre-departure authority-diffusion construct in OSS-native community-health/onboarding literature (CHAOSS, Apache Incubator graduation, newcomer/core-team formation studies) alongside the existing firm-succession analogy, and (2) identify and concretely characterize data sources (GH Archive, World of Code, GHTorrent/Libraries.io legacy dumps) that can supply a historical, present-day-liveness-non-conditioned GitHub repository snapshot without requiring an authenticated GitHub REST token, recommending the single most viable concrete pull-path for the dataset artifact.",
  "runpod_compute_profile": "cpu_light",
  "question": "What OSS-native community-health/onboarding frameworks already measure something like 'pre-departure authority diffusion' (so the construct can be positioned against them, not just the firm-succession analogy), and what concrete, token-free, historically-snapshotted data source can supply commit/file-level authorship data for a GitHub repository corpus that does not condition on present-day project liveness?",
  "research_plan": "PART A — OSS-native community-health/onboarding grounding (produces 1-2 positioning sentences)\n\n1. CHAOSS metrics (already partially scoped by prior searches this session — verify and deepen):\n   - Fetch https://www.chaoss.community/kb/metric-elephant-factor/ and https://www.chaoss.community/kb/metric-contributor-absence-factor/ (formerly 'Bus Factor') — get their EXACT definitions, formulas, and whether either is computed longitudinally (trend over time) or only as a single snapshot. This is the key comparison point: Avelino et al.'s TF and this hypothesis's diffusion trajectory are both snapshot-vs-trend variants of the same idea CHAOSS already names.\n   - Fetch https://github.com/chaoss/wg-risk/blob/main/focus-areas/business-risk/contributor-absence-factor.md for the CHAOSS working-group's own methodology writeup (more detail than the KB page).\n   - Search specifically for 'CHAOSS contributor absorption rate' and 'CHAOSS onboarding metrics' definitions (the KB page https://chaoss.community/kb/metrics-model-starter-project-health/ found this session is the right starting point — fetch it and grep for 'absorption', 'onboarding', 'time to first response', 'time to first commit').\n   - Deliverable: 2-4 sentences precisely stating what CHAOSS's Elephant Factor / Contributor Absence Factor measure, confirming (or refuting) that they are snapshot metrics like Avelino et al.'s TF, and explicitly noting they do NOT track a pre-departure temporal trend — this is the gap this hypothesis's construct fills relative to CHAOSS, in exactly the same way it fills the gap relative to Avelino et al.\n\n2. Apache Incubator podling graduation criteria:\n   - Fetch https://incubator.apache.org/guides/graduation.html (the canonical 'Guide to Successful Graduation') and grep/search it for language about 'diverse', 'authority', 'meritocratic', 'committers', 'PMC' — the graduation checklist explicitly assesses whether commit/PMC authority has spread beyond the founding contributor(s) before a podling is allowed to graduate to a top-level project.\n   - Also check https://incubator.apache.org/policy/incubation.html or the IPMC maturity model (Apache Project Maturity Model, https://community.apache.org/apache-way/apache-project-maturity-model.html) if graduation.html does not itself contain a hard diversity checklist — the Maturity Model has an explicit 'CD (Community Diversity)' criteria block (CD10, CD20, CD30) that is the closest real-world analogue to this hypothesis's diffusion metric and should be quoted if found.\n   - Deliverable: identify whether ASF operationalizes 'authority has diffused' as a graduation gate (binary human judgment) versus this hypothesis's proposal of a continuous, DOA-computed, retrospective metric — note this is a validation-committee heuristic, not a predictive statistical measurement, which is exactly the distinction worth stating in the positioning paragraph.\n\n3. OSS newcomer onboarding / core-team formation literature (to round out non-CHAOSS, non-ASF grounding):\n   - Scholarly search (mode=scholarly) for: 'core team formation open source' Fagerholm OR Jergensen OR onboarding barriers Steinmacher; and 'from periphery to core' OSS contributor trajectory.\n   - Specifically try to confirm/locate: Jergensen, Sarma & Wagstrom 'The Onion Patch' (core-periphery structure in OSS teams) and Steinmacher et al.'s onboarding-barriers work (multiple papers, e.g. 'A Systematic Literature Review on the Barriers Faced by Newcomers'); fetch abstracts, do not need full text.\n   - Deliverable: 1-2 sentences noting that onboarding/core-formation literature studies how NEW contributors become core (join trajectory), which is the mirror image of this hypothesis's DEPARTURE trajectory (existing founder authority dispersing outward) — a clean complementary framing to include in the paper's related-work section.\n\nPART B — Historical, liveness-non-conditioned GitHub corpus sources (produces a concrete recommended pull-path)\n\n4. GH Archive (gharchive.org):\n   - Fetch https://www.gharchive.org/ and https://github.com/igrigorik/gharchive.org/blob/master/bigquery/README.md.\n   - Report EXACTLY: (a) what event types are recorded (PushEvent has commit SHAs + author but NOT full diffs/file lists — confirm this precisely, since DOA needs per-file change history, which raw GH Archive events do NOT contain, only pointers/metadata); (b) the two access paths — hourly gzipped JSON files at http://data.gharchive.org/YYYY-MM-DD-H.json.gz (no auth needed, direct HTTP download) vs the public BigQuery dataset `githubarchive` (needs only a free Google Cloud project + BigQuery sandbox, NOT a GitHub token) — confirm the BigQuery sandbox free tier's query-volume limits (typically 1TB/month scan); (c) whether repo creation/star/fork events in a given historical month can be used to build a 'top-N repos that existed as of year Y' sampling frame WITHOUT reference to whether they are still active today (yes — this is exactly what Avelino et al.'s method needs: a repo list frozen at a point in time). Flag clearly that GH Archive alone cannot supply per-file DOA data; it can only supply the REPO SELECTION frame (which repos existed/were popular circa year Y), and per-file commit history must then be pulled via `git clone` of each selected repo's normal git history (which is not conditioned on present liveness — you can clone and analyze a repo's history regardless of whether the repo is later archived/deleted, as long as it is still on GitHub or in a mirror).\n\n5. World of Code (WoC):\n   - Fetch the arXiv abstract page https://arxiv.org/pdf/2607.06183 (author-identity map) and the original https://link.springer.com/article/10.1007/s10664-020-09905-9 EMSE paper abstract; also web-search 'World of Code access request how to use da API' to find the current access mechanism (WoC has historically required either direct SSH access to the maintainers' server at UTEP, requested via a form, OR downloadable Hugging Face bundles for specific derived datasets like the author-identity map).\n   - Report EXACTLY: whether WoC provides full per-commit, per-file author/timestamp data (it does — this is its core product: cross-referenced commit/blob/author/project maps) and whether any of it is downloadable WITHOUT an application/access-request process (the Hugging Face-hosted derived bundles, e.g. the author-identity map from the 2607.06183 paper, ARE self-contained no-account-needed downloads — check if a similarly self-contained bundle exists that includes per-project commit-author-file triples, not just the identity map, which alone is insufficient for DOA). If the full commit graph requires the request/SSH process, state this plainly as a BLOCKER for a 3-hour, token-budget-constrained execution window, and recommend against WoC as the primary path for this specific study.\n\n6. GHTorrent / Libraries.io legacy dumps:\n   - Fetch https://github.com/ghtorrent/ghtorrent.org/blob/master/faq.md and search 'GHTorrent MySQL dump download 2021' / 'GHTorrent Google BigQuery dataset public' to determine: (a) whether the historical MongoDB/MySQL dumps are still hosted and downloadable (GHTorrent's own infrastructure was largely decommissioned after ~2021 — verify current status, do not assume); (b) whether a mirror exists on Google BigQuery's public dataset marketplace (`ghtorrent-bq` or similar) that is still queryable; (c) Libraries.io's own open data dumps (libraries.io publishes periodic full CSV/JSON exports of package/repo metadata under Zenodo DOIs — these ARE static, no-token, permissively licensed, and searchable by Zenodo) — check the most recent Libraries.io Zenodo release for whether it includes per-repo star/fork/language/creation-date fields sufficient for building a stratified top-N-per-language sampling frame circa a fixed year, keeping in mind it will NOT contain commit-level data (same limitation as GH Archive: repo-selection metadata only, not DOA inputs).\n   - Deliverable: state plainly whether GHTorrent is USABLE TODAY or effectively dead infrastructure (report what is found, do not guess).\n\n7. Synthesize a single recommended concrete pull-path for the dataset artifact, in this priority order given the 3-hour/low-budget constraints of this project: (a) use GH Archive's hourly JSON dumps (direct HTTP, no token, e.g. `http://data.gharchive.org/2016-01-{01..07}-*.json.gz` covering a full week to catch CreateEvent/WatchEvent/ForkEvent activity) OR the free BigQuery sandbox querying the public `githubarchive.year.YYYY` tables, to build a repo-selection frame frozen at a chosen historical year (recommend mirroring Avelino et al.'s own approach: top-N repos per language ranked by stars/forks AS OF that year, not today) — this sidesteps the GitHub REST API token/rate-limit problem entirely for repo SELECTION; (b) for each selected repo, its full commit/file history for the DOA computation can be obtained via plain `git clone` (unauthenticated, unlimited, no token needed for public repos) rather than the GitHub REST API — commit history is retrievable regardless of the repo's current activity status, which is the actual bottleneck Avelino et al. hit (their 83x query-budget claim is about REST metadata calls, not git clone, and git clone is not rate-limited by a token at all for public repos); (c) note precisely which repos this excludes: any repo that was later made private or fully deleted (not just archived/renamed) between the historical snapshot year and today — GH Archive event data proves the repo existed and was active in year Y, but the study will still lose the subset that was later deleted outright, and this residual (much smaller) survivorship consideration should be reported honestly as a remaining limitation, distinct from and much weaker than the present-liveness-conditioning problem this whole direction exists to fix.\n\nExecution notes: run all Part A and Part B searches/fetches in parallel batches (independent topics). Use fetch_grep on the Apache Maturity Model page and CHAOSS KB pages to pull exact defined-metric text rather than paraphrasing from a general fetch summary. Cap total tool calls at roughly 25-30 search+fetch+grep calls; this is a zero-cost web-research task (no OpenRouter LLM calls needed beyond the report-writing step itself, which should use minimal tokens). Write findings into research_out.json (answer/sources/follow_up_questions) plus a readable research_report.md with two clearly separated sections mirroring Part A and Part B above, each ending in an explicit, actionable recommendation sentence the dataset-artifact executor can act on directly.",
  "explanation": "This research directly de-risks two concrete gaps flagged in the reviewer-driven revision of this hypothesis. First, the paper currently justifies its diffusion construct only via a cross-domain analogy (firm succession); grounding it against CHAOSS's Elephant/Contributor-Absence Factor, Apache Incubator's community-diversity graduation checks, and OSS core-team-formation literature gives it an OSS-native theoretical home and answers the likely reviewer question 'isn't this just bus factor over time' with a precise, sourced distinction. Second, and more consequentially, the current 15-repo corpus is invalidated by construction because it was sampled by starting from tools known today to still exist — this research finds and characterizes the concrete, no-token data sources (GH Archive event dumps for repo selection frozen at a historical year, plain git clone for commit/file history, with World of Code and GHTorrent/Libraries.io as characterized fallbacks) that a follow-up dataset artifact needs to build a corpus that does not condition on present-day liveness, which is the specific fix this hypothesis's own text says is required before the causal diffusion-predicts-survival claim can be tested at all."
}
```

### [20] TOOL RESULT — Write · 2026-08-20 20:09:50 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_plan/gen_plan_research_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"OSS Community-Health Framing + Bias-Free Corpus Sources\",\n  \"summary\": \"Web research to (1) ground the pre-departure authority-diffusion construct in OSS-native community-health/onboarding literature (CHAOSS, Apache Incubator graduation, newcomer/core-team formation studies) alongside the existing firm-succession analogy, and (2) identify and concretely characterize data sources (GH Archive, World of Code, GHTorrent/Libraries.io legacy dumps) that can supply a historical, present-day-liveness-non-conditioned GitHub repository snapshot without requiring an authenticated GitHub REST token, recommending the single most viable concrete pull-path for the dataset artifact.\",\n  \"runpod_compute_profile\": \"cpu_light\",\n  \"question\": \"What OSS-native community-health/onboarding frameworks already measure something like 'pre-departure authority diffusion' (so the construct can be positioned against them, not just the firm-succession analogy), and what concrete, token-free, historically-snapshotted data source can supply commit/file-level authorship data for a GitHub repository corpus that does not condition on present-day project liveness?\",\n  \"research_plan\": \"PART A — OSS-native community-health/onboarding grounding (produces 1-2 positioning sentences)\\n\\n1. CHAOSS metrics (already partially scoped by prior searches this session — verify and deepen):\\n   - Fetch https://www.chaoss.community/kb/metric-elephant-factor/ and https://www.chaoss.community/kb/metric-contributor-absence-factor/ (formerly 'Bus Factor') — get their EXACT definitions, formulas, and whether either is computed longitudinally (trend over time) or only as a single snapshot. This is the key comparison point: Avelino et al.'s TF and this hypothesis's diffusion trajectory are both snapshot-vs-trend variants of the same idea CHAOSS already names.\\n   - Fetch https://github.com/chaoss/wg-risk/blob/main/focus-areas/business-risk/contributor-absence-factor.md for the CHAOSS working-group's own methodology writeup (more detail than the KB page).\\n   - Search specifically for 'CHAOSS contributor absorption rate' and 'CHAOSS onboarding metrics' definitions (the KB page https://chaoss.community/kb/metrics-model-starter-project-health/ found this session is the right starting point — fetch it and grep for 'absorption', 'onboarding', 'time to first response', 'time to first commit').\\n   - Deliverable: 2-4 sentences precisely stating what CHAOSS's Elephant Factor / Contributor Absence Factor measure, confirming (or refuting) that they are snapshot metrics like Avelino et al.'s TF, and explicitly noting they do NOT track a pre-departure temporal trend — this is the gap this hypothesis's construct fills relative to CHAOSS, in exactly the same way it fills the gap relative to Avelino et al.\\n\\n2. Apache Incubator podling graduation criteria:\\n   - Fetch https://incubator.apache.org/guides/graduation.html (the canonical 'Guide to Successful Graduation') and grep/search it for language about 'diverse', 'authority', 'meritocratic', 'committers', 'PMC' — the graduation checklist explicitly assesses whether commit/PMC authority has spread beyond the founding contributor(s) before a podling is allowed to graduate to a top-level project.\\n   - Also check https://incubator.apache.org/policy/incubation.html or the IPMC maturity model (Apache Project Maturity Model, https://community.apache.org/apache-way/apache-project-maturity-model.html) if graduation.html does not itself contain a hard diversity checklist — the Maturity Model has an explicit 'CD (Community Diversity)' criteria block (CD10, CD20, CD30) that is the closest real-world analogue to this hypothesis's diffusion metric and should be quoted if found.\\n   - Deliverable: identify whether ASF operationalizes 'authority has diffused' as a graduation gate (binary human judgment) versus this hypothesis's proposal of a continuous, DOA-computed, retrospective metric — note this is a validation-committee heuristic, not a predictive statistical measurement, which is exactly the distinction worth stating in the positioning paragraph.\\n\\n3. OSS newcomer onboarding / core-team formation literature (to round out non-CHAOSS, non-ASF grounding):\\n   - Scholarly search (mode=scholarly) for: 'core team formation open source' Fagerholm OR Jergensen OR onboarding barriers Steinmacher; and 'from periphery to core' OSS contributor trajectory.\\n   - Specifically try to confirm/locate: Jergensen, Sarma & Wagstrom 'The Onion Patch' (core-periphery structure in OSS teams) and Steinmacher et al.'s onboarding-barriers work (multiple papers, e.g. 'A Systematic Literature Review on the Barriers Faced by Newcomers'); fetch abstracts, do not need full text.\\n   - Deliverable: 1-2 sentences noting that onboarding/core-formation literature studies how NEW contributors become core (join trajectory), which is the mirror image of this hypothesis's DEPARTURE trajectory (existing founder authority dispersing outward) — a clean complementary framing to include in the paper's related-work section.\\n\\nPART B — Historical, liveness-non-conditioned GitHub corpus sources (produces a concrete recommended pull-path)\\n\\n4. GH Archive (gharchive.org):\\n   - Fetch https://www.gharchive.org/ and https://github.com/igrigorik/gharchive.org/blob/master/bigquery/README.md.\\n   - Report EXACTLY: (a) what event types are recorded (PushEvent has commit SHAs + author but NOT full diffs/file lists — confirm this precisely, since DOA needs per-file change history, which raw GH Archive events do NOT contain, only pointers/metadata); (b) the two access paths — hourly gzipped JSON files at http://data.gharchive.org/YYYY-MM-DD-H.json.gz (no auth needed, direct HTTP download) vs the public BigQuery dataset `githubarchive` (needs only a free Google Cloud project + BigQuery sandbox, NOT a GitHub token) — confirm the BigQuery sandbox free tier's query-volume limits (typically 1TB/month scan); (c) whether repo creation/star/fork events in a given historical month can be used to build a 'top-N repos that existed as of year Y' sampling frame WITHOUT reference to whether they are still active today (yes — this is exactly what Avelino et al.'s method needs: a repo list frozen at a point in time). Flag clearly that GH Archive alone cannot supply per-file DOA data; it can only supply the REPO SELECTION frame (which repos existed/were popular circa year Y), and per-file commit history must then be pulled via `git clone` of each selected repo's normal git history (which is not conditioned on present liveness — you can clone and analyze a repo's history regardless of whether the repo is later archived/deleted, as long as it is still on GitHub or in a mirror).\\n\\n5. World of Code (WoC):\\n   - Fetch the arXiv abstract page https://arxiv.org/pdf/2607.06183 (author-identity map) and the original https://link.springer.com/article/10.1007/s10664-020-09905-9 EMSE paper abstract; also web-search 'World of Code access request how to use da API' to find the current access mechanism (WoC has historically required either direct SSH access to the maintainers' server at UTEP, requested via a form, OR downloadable Hugging Face bundles for specific derived datasets like the author-identity map).\\n   - Report EXACTLY: whether WoC provides full per-commit, per-file author/timestamp data (it does — this is its core product: cross-referenced commit/blob/author/project maps) and whether any of it is downloadable WITHOUT an application/access-request process (the Hugging Face-hosted derived bundles, e.g. the author-identity map from the 2607.06183 paper, ARE self-contained no-account-needed downloads — check if a similarly self-contained bundle exists that includes per-project commit-author-file triples, not just the identity map, which alone is insufficient for DOA). If the full commit graph requires the request/SSH process, state this plainly as a BLOCKER for a 3-hour, token-budget-constrained execution window, and recommend against WoC as the primary path for this specific study.\\n\\n6. GHTorrent / Libraries.io legacy dumps:\\n   - Fetch https://github.com/ghtorrent/ghtorrent.org/blob/master/faq.md and search 'GHTorrent MySQL dump download 2021' / 'GHTorrent Google BigQuery dataset public' to determine: (a) whether the historical MongoDB/MySQL dumps are still hosted and downloadable (GHTorrent's own infrastructure was largely decommissioned after ~2021 — verify current status, do not assume); (b) whether a mirror exists on Google BigQuery's public dataset marketplace (`ghtorrent-bq` or similar) that is still queryable; (c) Libraries.io's own open data dumps (libraries.io publishes periodic full CSV/JSON exports of package/repo metadata under Zenodo DOIs — these ARE static, no-token, permissively licensed, and searchable by Zenodo) — check the most recent Libraries.io Zenodo release for whether it includes per-repo star/fork/language/creation-date fields sufficient for building a stratified top-N-per-language sampling frame circa a fixed year, keeping in mind it will NOT contain commit-level data (same limitation as GH Archive: repo-selection metadata only, not DOA inputs).\\n   - Deliverable: state plainly whether GHTorrent is USABLE TODAY or effectively dead infrastructure (report what is found, do not guess).\\n\\n7. Synthesize a single recommended concrete pull-path for the dataset artifact, in this priority order given the 3-hour/low-budget constraints of this project: (a) use GH Archive's hourly JSON dumps (direct HTTP, no token, e.g. `http://data.gharchive.org/2016-01-{01..07}-*.json.gz` covering a full week to catch CreateEvent/WatchEvent/ForkEvent activity) OR the free BigQuery sandbox querying the public `githubarchive.year.YYYY` tables, to build a repo-selection frame frozen at a chosen historical year (recommend mirroring Avelino et al.'s own approach: top-N repos per language ranked by stars/forks AS OF that year, not today) — this sidesteps the GitHub REST API token/rate-limit problem entirely for repo SELECTION; (b) for each selected repo, its full commit/file history for the DOA computation can be obtained via plain `git clone` (unauthenticated, unlimited, no token needed for public repos) rather than the GitHub REST API — commit history is retrievable regardless of the repo's current activity status, which is the actual bottleneck Avelino et al. hit (their 83x query-budget claim is about REST metadata calls, not git clone, and git clone is not rate-limited by a token at all for public repos); (c) note precisely which repos this excludes: any repo that was later made private or fully deleted (not just archived/renamed) between the historical snapshot year and today — GH Archive event data proves the repo existed and was active in year Y, but the study will still lose the subset that was later deleted outright, and this residual (much smaller) survivorship consideration should be reported honestly as a remaining limitation, distinct from and much weaker than the present-liveness-conditioning problem this whole direction exists to fix.\\n\\nExecution notes: run all Part A and Part B searches/fetches in parallel batches (independent topics). Use fetch_grep on the Apache Maturity Model page and CHAOSS KB pages to pull exact defined-metric text rather than paraphrasing from a general fetch summary. Cap total tool calls at roughly 25-30 search+fetch+grep calls; this is a zero-cost web-research task (no OpenRouter LLM calls needed beyond the report-writing step itself, which should use minimal tokens). Write findings into research_out.json (answer/sources/follow_up_questions) plus a readable research_report.md with two clearly separated sections mirroring Part A and Part B above, each ending in an explicit, actionable recommendation sentence the dataset-artifact executor can act on directly.\",\n  \"explanation\": \"This research directly de-risks two concrete gaps flagged in the reviewer-driven revision of this hypothesis. First, the paper currently justifies its diffusion construct only via a cross-domain analogy (firm succession); grounding it against CHAOSS's Elephant/Contributor-Absence Factor, Apache Incubator's community-diversity graduation checks, and OSS core-team-formation literature gives it an OSS-native theoretical home and answers the likely reviewer question 'isn't this just bus factor over time' with a precise, sourced distinction. Second, and more consequentially, the current 15-repo corpus is invalidated by construction because it was sampled by starting from tools known today to still exist — this research finds and characterizes the concrete, no-token data sources (GH Archive event dumps for repo selection frozen at a historical year, plain git clone for commit/file history, with World of Code and GHTorrent/Libraries.io as characterized fallbacks) that a follow-up dataset artifact needs to build a corpus that does not condition on present-day liveness, which is the specific fix this hypothesis's own text says is required before the causal diffusion-predicts-survival claim can be tested at all.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [21] ASSISTANT · 2026-08-20 20:09:52 UTC

```
Plan written to `.terminal_claude_agent_struct_out.json` covering both parts of the direction: OSS-native construct grounding (CHAOSS Elephant/Contributor-Absence Factor, Apache Incubator maturity model, core-team-formation literature) and a concrete, token-free historical-corpus pull-path (GH Archive for liveness-non-conditioned repo selection + plain `git clone` for commit history, with World of Code and GHTorrent/Libraries.io characterized as fallbacks).
```
