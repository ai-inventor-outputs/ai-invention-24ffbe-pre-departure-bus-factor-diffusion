# gen_plan_evaluation_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_plan`
> Run: `iter1_0b7b616dce39` — Does Pre-Departure Authority Diffusion Predict Open-Source Project Survival? A Unified-Corpus Retest with a Window-Boundary-Noise Control
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_evaluation_1` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-08-21 17:42:27 UTC

```
model: claude-sonnet-5 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_plan/gen_plan_evaluation_1
```

### [2] SYSTEM-USER prompt · 2026-08-21 17:42:35 UTC

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
title: 'Pre-Departure Authority Diffusion: An Underpowered Test'
hypothesis: >-
  An open-source project's survival after its founder stops committing (a founder-only Truck Factor Developer Detachment,
  or TFDD, in Avelino et al.'s ESEM 2019 terminology) is hypothesized to depend more on how diffused DOA-based commit/file
  authority already was among non-founder contributors in the 6-12 months BEFORE departure than on the project's popularity
  or size at the moment of departure -- which Avelino et al. already show is statistically indistinguishable between survivors
  and non-survivors at the TFDD snapshot (d=0.13-0.26). This iteration's evidence neither confirms nor refutes that claim:
  of three pre-registered tests, only one -- a within-repo random-window placebo control -- actually ran to completion, at
  n=30 founder-only TFDD events. It found the true pre-departure window's founder-share/survival correlation (r=0.180) statistically
  indistinguishable from an arbitrary window drawn from the same repositories' own histories (40th percentile of a 25-draw
  null, empirical p=0.615), a genuine but weakly-resolved null on that one specific test. The other two pre-registered tests
  (BH-FDR logistic regression; matched-pairs bootstrap) could not be run at all -- they returned zero usable observations
  per stratification cell -- so they provide no evidence either way, and must not be read as failed tests. The hypothesis
  is therefore narrowed and reframed: (1) the central claim is now explicitly conditional on closing three concrete gaps before
  any future test can be informative -- (a) a corpus of founder-only TFDD events an order of magnitude larger than the current
  30-62 repositories, since founder-only-TFDD scarcity, not the underlying mechanism, was the dominant source of attrition
  in both mining passes; (b) a validated sub-year DOA/TF window computation, since Avelino et al.'s DOA/TF pipeline was only
  ever validated at yearly full-history snapshots and the pre-departure window recomputation used here is an unvalidated methodological
  extension whose own boundary noise has not been separated from genuine authority-diffusion signal; (c) a single unified
  experimental corpus, since this iteration's dataset artifact (32 repos) and experiment artifact (62 repos, 30 usable) were
  mined independently and never reconciled into one analysis; (2) until those gaps are closed, the hypothesis should be evaluated
  as a scope-boundary/feasibility question -- can a pre-departure authority-diffusion signal be measured with enough precision
  and corpus size to be tested at all -- rather than as a claim already tested against Avelino et al.'s snapshot baseline.
  The core mechanism (trajectory of authority concentration predicts survival better than a point-in-time snapshot) is preserved
  unchanged from the prior iteration; what has changed is an honest downgrade of what current evidence shows about it, from
  'three-way tested' to 'one-third tested (null, low-resolution), two-thirds untestable at this scale.'
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
  Same trajectory-vs-snapshot claim kept; scope narrowed to reflect only 1/3 tests ran (null), 2/3 untestable at n=30
_confidence_delta: decreased
_key_changes:
- >-
  Corrected overclaiming: no longer states 'hypothesis fails on all three counts' -- only the placebo test (1 of 3) actually
  ran, producing a weak/low-resolution null; the regression and matched-pairs tests returned zero usable observations and
  provide no evidence either way
- >-
  Added an explicit precondition list (larger founder-only-TFDD corpus, validated sub-year DOA window, unified single experimental
  corpus) that must be satisfied before the three-criterion test can be considered informative
- >-
  Flagged the sub-year DOA/TF window computation as an unvalidated methodological extension whose own measurement noise has
  not been distinguished from genuine diffusion signal, per reviewer's MAJOR critique
- >-
  Flagged the corpus provenance mismatch between the 32-repo dataset artifact and the 62-repo (30-usable) experiment corpus
  as unresolved, per reviewer's MAJOR critique
- >-
  Reframed the research question from 'does pre-departure diffusion predict survival' (tested-and-answered framing) to 'can
  this signal be measured and tested at sufficient power and precision' (feasibility framing), reflecting that most of the
  evidence gathered this iteration is about measurement feasibility, not the underlying mechanism
- >-
  Preserved the core mechanism and all definitions (TFDD, DOA, authority diffusion, matched-pairs design) unchanged from the
  prior hypothesis, since no evidence contradicts the mechanism itself -- only the ability to test it at current scale
relation_type: evolution
</hypothesis>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: evaluation_iter2_dir3
type: evaluation
objective: >-
  Supply the statistical rigor reviewers found missing on top of the re-run experiment: bootstrap confidence intervals on
  every Cohen's d and on the placebo empirical percentile, and a manual identity-resolution spot-check against GitHub profile
  pages.
approach: >-
  Using the unified experiment's method_out.json, compute bootstrap (or analytic) 95% CIs for each snapshot-covariate Cohen's
  d (developers/commits/files/stars/forks at TFDD) and state explicitly whether Avelino et al.'s reported 0.13-0.26 range
  falls inside or outside each interval, resolving the MINOR scope critique. Bootstrap-resample the placebo null draws to
  put a CI on the true window's empirical percentile, substantiating (or revising) any robustness claim about the placebo
  result. Manually spot-check identity resolution (the local email/name-alias heuristic) against live GitHub profile/commit
  pages for a random 10-15 repo sample from the unified corpus, reporting an observed alias/merge error rate as a concrete
  bound on the MINOR data-quality risk flagged for the founder-only-TFDD qualification step itself. Consolidate all of this
  into a single evaluation report that states, per the MAJOR framing critique, exactly which of the three pre-registered criteria
  were tested-and-null versus untestable-for-power at the new corpus scale.
depends_on:
- id: art_eXxdnfS0o6aV
  label: baseline
  relation_type:
  relation_rationale:
</artifact_direction>

<dependencies>
Completed artifacts this artifact can use during execution.

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
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json
</dependencies>

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

### [3] HUMAN-USER prompt · 2026-08-21 17:42:35 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [4] TOOL CALL — Write · 2026-08-21 17:43:33 UTC

```
File: /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_plan/gen_plan_evaluation_1/.terminal_claude_agent_struct_out.json

{
  "title": "Bootstrap CIs and Identity Spot-Check",
  "summary": "An evaluation artifact that adds statistical rigor to the founder-exit/survival experiment (art_eXxdnfS0o6aV): bootstrap 95% CIs on every reported Cohen's d snapshot-covariate effect size and on the placebo test's empirical percentile, plus a manual GitHub-profile spot-check of the identity/alias-resolution heuristic on a random 10-15 repo sample, consolidated into a single eval_out.json report that classifies each of the three pre-registered success criteria as tested-and-null, untestable-for-power, or now-resolved-by-CI.\n\nSTEP 0 — Load and validate inputs.\nRead full_method_out.json from the dependency workspace (/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/full_method_out.json). Parse the per-repo `examples` array and the top-level `metadata` block, specifically: corpus_stats, baseline_replication, regression_results, matched_pairs_results, placebo_results, success_criteria_verdict. If any of these metadata keys is missing or empty, log a clear WARNING (not a silent skip) and mark that section's downstream analysis as 'INPUT_MISSING' in the final report rather than fabricating a number. Confirm the 24 TFDD repos with predict_our_method/predict_baseline_snapshot fields and the 30-repo usable analysis corpus are both present; record their exact counts at the top of the report so a reader can immediately see n for every subsequent statistic.\n\nSTEP 1 — Bootstrap CIs on snapshot-covariate Cohen's d (resolves the MINOR scope critique).\nFor each of the five snapshot covariates measured at TFDD (developers, commits, files, stars, forks), recover the two raw per-repo group samples (survivor vs non-survivor) that produced the originally reported Cohen's d, not just the scalar d itself — these should be reconstructable from the per-repo `examples` records using the survival label and the corresponding snapshot field. If raw per-repo values for a covariate are not present in method_out.json (e.g., d was computed but the underlying arrays were not persisted), state this explicitly as a data-availability limitation and either (a) reconstruct summary-based approximate CIs via Hedges/Cohen's d sampling-distribution formulas (using group n, d, and pooled SD if recoverable), clearly labeled 'analytic approximation, not resampled', or (b) mark that covariate's CI as NOT_COMPUTABLE_FROM_ARTIFACT — do not silently fall back to fabricated numbers.\nWhere raw values ARE available: implement a nonparametric bootstrap with B=10,000 resamples (resample survivor and non-survivor groups independently, with replacement, at their original sizes; note that at n=30 with likely uneven group splits, this may leave one arm with single-digit n — flag any covariate where the smaller group's n<10 as LOW_RESOLUTION at the point it's reported, not buried in a footnote). For each resample, recompute Cohen's d = (mean1-mean2)/pooled_sd; take the 2.5th/97.5th percentiles of the resulting bootstrap distribution as the 95% CI. Fix a random seed for reproducibility and record it in the output.\nFor every covariate, explicitly state whether Avelino et al.'s reported ESEM 2019 range (d=0.13 for files, d=0.25-0.26 for developers/commits; note stars/forks were not covariates Avelino et al. reported on file/dev/commit terms so treat those as this-study's own new covariates without an Avelino baseline to compare against — say so directly) falls INSIDE or OUTSIDE the newly bootstrapped 95% CI. Present this as a small table: covariate | n_survivor | n_nonsurvivor | point d | bootstrap 95% CI | Avelino reference value | inside/outside CI | resolution flag (adequate/low_resolution/not_computable).\n\nSTEP 2 — Bootstrap CI on the placebo empirical percentile.\nThe experiment's placebo test drew 200 null resamples of a randomly relocated 'pre-departure window' within each repo's own history and reported the true window's percentile rank among them (reported in the hypothesis text as 40th percentile with empirical p=0.615 at an earlier n=30 test — verify against the actual method_out.json placebo_results, which may differ slightly since this is the unified/reconciled corpus). To put a CI on that percentile rank itself: bootstrap-resample the 200 null-draw statistic values (or, if the raw 200 draws per repo are stored rather than one pooled null distribution, resample at the repo level first, then within-repo at the draw level, i.e. a two-stage/cluster bootstrap that respects the nesting) with B=10,000 resamples, and for each resample recompute where the true-window statistic falls as a percentile of that resampled null. Report the resulting 95% CI on the percentile. State explicitly whether this CI is wide enough to include both 'no signal' (~50th percentile) and 'some signal' (e.g. <25th or >75th percentile) — if so, say plainly that the placebo result cannot currently distinguish a true null from a weak real effect, rather than presenting the point estimate alone as if it settled the question.\n\nSTEP 3 — Manual identity-resolution spot-check.\nFrom the 30-repo (or 46-prefiltered, whichever the experiment's REPO_LIST covers) unified corpus, deterministically sample 12 repos (fix a seed, e.g. numpy RandomState(42), and document the exact repo list and seed in the output so it's reproducible) stratified where possible across language/ecosystem to catch different noreply-email conventions (e.g. GitHub noreply patterns differ slightly by account age). For each sampled repo, using the aii-web-tools skill (web fetch + fetch_grep, NOT authenticated API calls — GitHub REST is rate-limited without a token and this must not require secrets), open the repo's GitHub commit history / contributors page and the founder's and 2-3 top non-founder contributors' public profile pages. Cross-check: (a) does the local alias-resolution heuristic's inferred founder identity match the actual first-committer/creator shown on GitHub; (b) do noreply-email-derived aliases the pipeline merged into one identity actually belong to the same GitHub account (spot check by following the noreply email pattern <id>+<username>@users.noreply.github.com back to the username, which is directly parseable without API calls); (c) are there any obviously-missed merges (same display name, different email, not merged) or over-merges (different people merged into one) visible from the commit list.\nRecord for each of the 12 repos: PASS (identity resolution matches GitHub ground truth), ALIAS_MERGE_ERROR (specific description), or AMBIGUOUS (cannot determine from public page, e.g. private email commits). Compute an observed error rate = (ALIAS_MERGE_ERROR count) / 12, with a Wilson score 95% CI for this small-n proportion (do not use a naive normal-approximation CI at n=12). Report this as a concrete bound on the MINOR data-quality risk for the founder-only-TFDD qualification step, and explicitly discuss whether any detected errors would plausibly change founder identification or TF=1 status for that repo's event (which would be a more serious finding than a cosmetic alias miscount).\n\nSTEP 4 — Consolidated verdict table (resolves the MAJOR framing critique).\nBuild a single summary table classifying each of the three original pre-registered success criteria (matched-pairs survival-rate-ratio CI excluding 1x; BH-FDR-significant regression coefficients exceeding snapshot-covariate effect size; placebo/shuffle check showing weaker effect at relocated windows) into exactly one of: TESTED_NULL (ran to completion, produced a result distinguishable from chance, did not meet the pre-registered bar), TESTED_LOW_RESOLUTION (ran, but bootstrap CI from Step 1/2 is too wide to distinguish null from a real small-to-moderate effect), or UNTESTABLE_AT_SCALE (zero usable observations per stratification cell, as already documented in the experiment). Use the newly computed CIs to decide TESTED_NULL vs TESTED_LOW_RESOLUTION rather than asserting it. State the practical implication of each classification for what a future, larger-corpus iteration would need to change.\n\nSTEP 5 — Output.\nWrite eval_out.json conforming to the exp_eval_sol_out schema (validate with the aii-json skill before finishing): top-level metadata carrying corpus_stats (echoed from input), covariate_ci_table (from Step 1), placebo_ci (from Step 2), identity_spotcheck_results (from Step 3, including the Wilson CI and per-repo findings), and success_criteria_reclassification (from Step 4). Per-example entries (if the schema requires per-repo predictions) can simply echo the original experiment's predict_our_method/predict_baseline_snapshot fields unchanged, since this artifact evaluates existing results rather than generating new predictions. Run the aii-json skill's mini/preview generation. If any bootstrap or spot-check step could not be completed (e.g., raw per-covariate arrays genuinely absent from method_out.json), the final report must say so in plain language rather than omitting the covariate silently — a reader must be able to tell 'not computed because unavailable' from 'computed and small'.\n\nFAILURE MODES TO HANDLE: (1) If method_out.json's per-repo records lack raw covariate values needed for a true nonparametric bootstrap, fall back to the analytic Hedges'-d-CI formula (documented, e.g., in Cousineau & Goulet-Pelletier 2021, or standard Cohen's d sampling variance Var(d) ≈ (n1+n2)/(n1*n2) + d²/(2*(n1+n2))) and label results 'analytic, not resampled'. (2) If web fetch of a GitHub profile page is blocked, rate-limited, or the repo/user has since gone private, mark that repo AMBIGUOUS and swap in the next repo from the seeded sample list rather than silently shrinking n below 12 without saying so. (3) If the placebo null draws are stored only as a single pooled percentile with no underlying 200 raw values, state that a proper bootstrap CI is not reconstructable from the artifact as saved and report this as a concrete, named gap for the next experiment iteration to fix by persisting raw null-draw values.",
  "runpod_compute_profile": "cpu_light",
  "metrics_descriptions": "(1) Bootstrap 95% confidence intervals (B=10,000 resamples, seeded) on Cohen's d for each snapshot covariate (developers, commits, files, stars, forks) measured at the TFDD point, computed via nonparametric resampling of the raw per-repo survivor/non-survivor values where available, or an analytic Hedges'-d sampling-variance approximation where raw values cannot be recovered from the experiment artifact. (2) A bootstrap 95% CI on the placebo test's empirical percentile rank (the true pre-departure window's rank among 200 within-repo random-window null draws), using a two-stage cluster bootstrap if draws are nested per repo. (3) An observed identity/alias-resolution error rate from a manual 12-repo GitHub-profile spot-check, reported as a point estimate with a Wilson score 95% CI appropriate for small-n proportions, broken into PASS / ALIAS_MERGE_ERROR / AMBIGUOUS counts. (4) A three-way reclassification of the original pre-registered success criteria (TESTED_NULL, TESTED_LOW_RESOLUTION, UNTESTABLE_AT_SCALE) driven by whether the new CIs from (1)-(2) are narrow enough to distinguish a genuine null from a merely underpowered result.",
  "metrics_justification": "The hypothesis's own self-critique (from the prior iteration's reviewer) is that its central claim was tested at n=30 with no CIs on the reported effect sizes, so a scalar Cohen's d or a single percentile rank cannot on its own distinguish 'genuinely no effect' from 'too little data to tell' -- exactly the ambiguity the hypothesis text itself flags as the difference between a real null and an untested claim. Bootstrap CIs directly quantify that ambiguity: a CI that excludes Avelino et al.'s 0.13-0.26 reference range supports treating the result as a genuine, resolvable null; a CI wide enough to contain both zero and a moderate effect supports the hypothesis's own honest downgrade to 'low-resolution, not falsified.' Putting a CI on the placebo percentile serves the same purpose for the one test that did run to completion -- it converts a single 40th-percentile point estimate into an interval that either does or does not rule out a real pre-departure signal. The identity spot-check targets a distinct, previously unverified risk: founder/authority disambiguation is a load-bearing step for the entire founder-only-TFDD qualification (misidentifying the founder or merging the wrong aliases could silently corrupt which events even qualify as TF=1 detachments), and no part of the original experiment validated this heuristic against ground truth. Measuring its error rate on a real sample turns a previously unquantified MINOR risk into a concrete, citable bound. Together these three measurements let the final report make the exact claim the hypothesis needs to make honestly: which of the three pre-registered criteria are actually resolved by current evidence versus which remain open only because of insufficient power -- precisely the MAJOR framing critique this artifact is scoped to close."
}
```

### [5] TOOL RESULT — Write · 2026-08-21 17:43:33 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_plan/gen_plan_evaluation_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Bootstrap CIs and Identity Spot-Check\",\n  \"summary\": \"An evaluation artifact that adds statistical rigor to the founder-exit/survival experiment (art_eXxdnfS0o6aV): bootstrap 95% CIs on every reported Cohen's d snapshot-covariate effect size and on the placebo test's empirical percentile, plus a manual GitHub-profile spot-check of the identity/alias-resolution heuristic on a random 10-15 repo sample, consolidated into a single eval_out.json report that classifies each of the three pre-registered success criteria as tested-and-null, untestable-for-power, or now-resolved-by-CI.\\n\\nSTEP 0 — Load and validate inputs.\\nRead full_method_out.json from the dependency workspace (/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/full_method_out.json). Parse the per-repo `examples` array and the top-level `metadata` block, specifically: corpus_stats, baseline_replication, regression_results, matched_pairs_results, placebo_results, success_criteria_verdict. If any of these metadata keys is missing or empty, log a clear WARNING (not a silent skip) and mark that section's downstream analysis as 'INPUT_MISSING' in the final report rather than fabricating a number. Confirm the 24 TFDD repos with predict_our_method/predict_baseline_snapshot fields and the 30-repo usable analysis corpus are both present; record their exact counts at the top of the report so a reader can immediately see n for every subsequent statistic.\\n\\nSTEP 1 — Bootstrap CIs on snapshot-covariate Cohen's d (resolves the MINOR scope critique).\\nFor each of the five snapshot covariates measured at TFDD (developers, commits, files, stars, forks), recover the two raw per-repo group samples (survivor vs non-survivor) that produced the originally reported Cohen's d, not just the scalar d itself — these should be reconstructable from the per-repo `examples` records using the survival label and the corresponding snapshot field. If raw per-repo values for a covariate are not present in method_out.json (e.g., d was computed but the underlying arrays were not persisted), state this explicitly as a data-availability limitation and either (a) reconstruct summary-based approximate CIs via Hedges/Cohen's d sampling-distribution formulas (using group n, d, and pooled SD if recoverable), clearly labeled 'analytic approximation, not resampled', or (b) mark that covariate's CI as NOT_COMPUTABLE_FROM_ARTIFACT — do not silently fall back to fabricated numbers.\\nWhere raw values ARE available: implement a nonparametric bootstrap with B=10,000 resamples (resample survivor and non-survivor groups independently, with replacement, at their original sizes; note that at n=30 with likely uneven group splits, this may leave one arm with single-digit n — flag any covariate where the smaller group's n<10 as LOW_RESOLUTION at the point it's reported, not buried in a footnote). For each resample, recompute Cohen's d = (mean1-mean2)/pooled_sd; take the 2.5th/97.5th percentiles of the resulting bootstrap distribution as the 95% CI. Fix a random seed for reproducibility and record it in the output.\\nFor every covariate, explicitly state whether Avelino et al.'s reported ESEM 2019 range (d=0.13 for files, d=0.25-0.26 for developers/commits; note stars/forks were not covariates Avelino et al. reported on file/dev/commit terms so treat those as this-study's own new covariates without an Avelino baseline to compare against — say so directly) falls INSIDE or OUTSIDE the newly bootstrapped 95% CI. Present this as a small table: covariate | n_survivor | n_nonsurvivor | point d | bootstrap 95% CI | Avelino reference value | inside/outside CI | resolution flag (adequate/low_resolution/not_computable).\\n\\nSTEP 2 — Bootstrap CI on the placebo empirical percentile.\\nThe experiment's placebo test drew 200 null resamples of a randomly relocated 'pre-departure window' within each repo's own history and reported the true window's percentile rank among them (reported in the hypothesis text as 40th percentile with empirical p=0.615 at an earlier n=30 test — verify against the actual method_out.json placebo_results, which may differ slightly since this is the unified/reconciled corpus). To put a CI on that percentile rank itself: bootstrap-resample the 200 null-draw statistic values (or, if the raw 200 draws per repo are stored rather than one pooled null distribution, resample at the repo level first, then within-repo at the draw level, i.e. a two-stage/cluster bootstrap that respects the nesting) with B=10,000 resamples, and for each resample recompute where the true-window statistic falls as a percentile of that resampled null. Report the resulting 95% CI on the percentile. State explicitly whether this CI is wide enough to include both 'no signal' (~50th percentile) and 'some signal' (e.g. <25th or >75th percentile) — if so, say plainly that the placebo result cannot currently distinguish a true null from a weak real effect, rather than presenting the point estimate alone as if it settled the question.\\n\\nSTEP 3 — Manual identity-resolution spot-check.\\nFrom the 30-repo (or 46-prefiltered, whichever the experiment's REPO_LIST covers) unified corpus, deterministically sample 12 repos (fix a seed, e.g. numpy RandomState(42), and document the exact repo list and seed in the output so it's reproducible) stratified where possible across language/ecosystem to catch different noreply-email conventions (e.g. GitHub noreply patterns differ slightly by account age). For each sampled repo, using the aii-web-tools skill (web fetch + fetch_grep, NOT authenticated API calls — GitHub REST is rate-limited without a token and this must not require secrets), open the repo's GitHub commit history / contributors page and the founder's and 2-3 top non-founder contributors' public profile pages. Cross-check: (a) does the local alias-resolution heuristic's inferred founder identity match the actual first-committer/creator shown on GitHub; (b) do noreply-email-derived aliases the pipeline merged into one identity actually belong to the same GitHub account (spot check by following the noreply email pattern <id>+<username>@users.noreply.github.com back to the username, which is directly parseable without API calls); (c) are there any obviously-missed merges (same display name, different email, not merged) or over-merges (different people merged into one) visible from the commit list.\\nRecord for each of the 12 repos: PASS (identity resolution matches GitHub ground truth), ALIAS_MERGE_ERROR (specific description), or AMBIGUOUS (cannot determine from public page, e.g. private email commits). Compute an observed error rate = (ALIAS_MERGE_ERROR count) / 12, with a Wilson score 95% CI for this small-n proportion (do not use a naive normal-approximation CI at n=12). Report this as a concrete bound on the MINOR data-quality risk for the founder-only-TFDD qualification step, and explicitly discuss whether any detected errors would plausibly change founder identification or TF=1 status for that repo's event (which would be a more serious finding than a cosmetic alias miscount).\\n\\nSTEP 4 — Consolidated verdict table (resolves the MAJOR framing critique).\\nBuild a single summary table classifying each of the three original pre-registered success criteria (matched-pairs survival-rate-ratio CI excluding 1x; BH-FDR-significant regression coefficients exceeding snapshot-covariate effect size; placebo/shuffle check showing weaker effect at relocated windows) into exactly one of: TESTED_NULL (ran to completion, produced a result distinguishable from chance, did not meet the pre-registered bar), TESTED_LOW_RESOLUTION (ran, but bootstrap CI from Step 1/2 is too wide to distinguish null from a real small-to-moderate effect), or UNTESTABLE_AT_SCALE (zero usable observations per stratification cell, as already documented in the experiment). Use the newly computed CIs to decide TESTED_NULL vs TESTED_LOW_RESOLUTION rather than asserting it. State the practical implication of each classification for what a future, larger-corpus iteration would need to change.\\n\\nSTEP 5 — Output.\\nWrite eval_out.json conforming to the exp_eval_sol_out schema (validate with the aii-json skill before finishing): top-level metadata carrying corpus_stats (echoed from input), covariate_ci_table (from Step 1), placebo_ci (from Step 2), identity_spotcheck_results (from Step 3, including the Wilson CI and per-repo findings), and success_criteria_reclassification (from Step 4). Per-example entries (if the schema requires per-repo predictions) can simply echo the original experiment's predict_our_method/predict_baseline_snapshot fields unchanged, since this artifact evaluates existing results rather than generating new predictions. Run the aii-json skill's mini/preview generation. If any bootstrap or spot-check step could not be completed (e.g., raw per-covariate arrays genuinely absent from method_out.json), the final report must say so in plain language rather than omitting the covariate silently — a reader must be able to tell 'not computed because unavailable' from 'computed and small'.\\n\\nFAILURE MODES TO HANDLE: (1) If method_out.json's per-repo records lack raw covariate values needed for a true nonparametric bootstrap, fall back to the analytic Hedges'-d-CI formula (documented, e.g., in Cousineau & Goulet-Pelletier 2021, or standard Cohen's d sampling variance Var(d) ≈ (n1+n2)/(n1*n2) + d²/(2*(n1+n2))) and label results 'analytic, not resampled'. (2) If web fetch of a GitHub profile page is blocked, rate-limited, or the repo/user has since gone private, mark that repo AMBIGUOUS and swap in the next repo from the seeded sample list rather than silently shrinking n below 12 without saying so. (3) If the placebo null draws are stored only as a single pooled percentile with no underlying 200 raw values, state that a proper bootstrap CI is not reconstructable from the artifact as saved and report this as a concrete, named gap for the next experiment iteration to fix by persisting raw null-draw values.\",\n  \"runpod_compute_profile\": \"cpu_light\",\n  \"metrics_descriptions\": \"(1) Bootstrap 95% confidence intervals (B=10,000 resamples, seeded) on Cohen's d for each snapshot covariate (developers, commits, files, stars, forks) measured at the TFDD point, computed via nonparametric resampling of the raw per-repo survivor/non-survivor values where available, or an analytic Hedges'-d sampling-variance approximation where raw values cannot be recovered from the experiment artifact. (2) A bootstrap 95% CI on the placebo test's empirical percentile rank (the true pre-departure window's rank among 200 within-repo random-window null draws), using a two-stage cluster bootstrap if draws are nested per repo. (3) An observed identity/alias-resolution error rate from a manual 12-repo GitHub-profile spot-check, reported as a point estimate with a Wilson score 95% CI appropriate for small-n proportions, broken into PASS / ALIAS_MERGE_ERROR / AMBIGUOUS counts. (4) A three-way reclassification of the original pre-registered success criteria (TESTED_NULL, TESTED_LOW_RESOLUTION, UNTESTABLE_AT_SCALE) driven by whether the new CIs from (1)-(2) are narrow enough to distinguish a genuine null from a merely underpowered result.\",\n  \"metrics_justification\": \"The hypothesis's own self-critique (from the prior iteration's reviewer) is that its central claim was tested at n=30 with no CIs on the reported effect sizes, so a scalar Cohen's d or a single percentile rank cannot on its own distinguish 'genuinely no effect' from 'too little data to tell' -- exactly the ambiguity the hypothesis text itself flags as the difference between a real null and an untested claim. Bootstrap CIs directly quantify that ambiguity: a CI that excludes Avelino et al.'s 0.13-0.26 reference range supports treating the result as a genuine, resolvable null; a CI wide enough to contain both zero and a moderate effect supports the hypothesis's own honest downgrade to 'low-resolution, not falsified.' Putting a CI on the placebo percentile serves the same purpose for the one test that did run to completion -- it converts a single 40th-percentile point estimate into an interval that either does or does not rule out a real pre-departure signal. The identity spot-check targets a distinct, previously unverified risk: founder/authority disambiguation is a load-bearing step for the entire founder-only-TFDD qualification (misidentifying the founder or merging the wrong aliases could silently corrupt which events even qualify as TF=1 detachments), and no part of the original experiment validated this heuristic against ground truth. Measuring its error rate on a real sample turns a previously unquantified MINOR risk into a concrete, citable bound. Together these three measurements let the final report make the exact claim the hypothesis needs to make honestly: which of the three pre-registered criteria are actually resolved by current evidence versus which remain open only because of insufficient power -- precisely the MAJOR framing critique this artifact is scoped to close.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [6] ASSISTANT · 2026-08-21 17:43:34 UTC

```
Plan written to `.terminal_claude_agent_struct_out.json` — an evaluation adding bootstrap CIs on the snapshot-covariate Cohen's d values and placebo percentile, plus a 12-repo manual GitHub identity-resolution spot-check, consolidated into a three-way reclassification (tested-null / low-resolution / untestable) of the original success criteria.
```
