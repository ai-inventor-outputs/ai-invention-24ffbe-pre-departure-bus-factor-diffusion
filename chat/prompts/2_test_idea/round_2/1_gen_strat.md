# gen_strat_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_strat`
> Run: `iter1_0b7b616dce39` — Does Pre-Departure Authority Diffusion Predict Open-Source Project Survival? A Unified-Corpus Retest with a Window-Boundary-Noise Control
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_strat_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 17:41:23 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A strategy planner (Step 3.1: GEN_STRAT in the invention loop)

Each iteration of the invention loop runs: GEN_STRAT → GEN_PLAN → GEN_ART → GEN_PAPER_TEXT → REVIEW_PAPER → UPD_HYPO
Artifact types: RESEARCH (web search), EXPERIMENT (code), DATASET (data collection), EVALUATION (metrics), PROOF (Lean 4)
State persists across iterations: strategies, plans, artifacts, paper_texts (read from the run tree)

You received the hypothesis, iteration status (current + remaining), previous iteration's strategies, available artifact types, existing artifacts, and reviewer feedback.
Your strategy governs THIS iteration only. You define what artifacts to create NOW.

Focused strategy → efficient progress. Scattered strategy → wasted iteration.
</your_role>
</ai_inventor_context>

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

<time_budgets>

Each artifact executor has a fixed time budget (including writing code, debugging, testing, and fixing errors):

- research: 3h
- dataset: 6h
- experiment: 6h
- evaluation: 3h
- proof: 3h

</time_budgets>

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

<research_methodology>
Think like a researcher planning a study for a top venue.

- All strategies run in parallel and their artifacts combine into one pool. Together they must build toward a publishable paper — each strategy contributes a distinct, necessary piece. No strategy should be a standalone island.
- Ask yourself: what would a reviewer need to see? Proper baselines, controlled comparisons, ablations that isolate what matters. Plan artifacts that preempt reviewer objections.
- Depth over breadth. One well-designed experiment with proper controls beats five shallow ones.
- Match your evaluation to your claims. Measure what the hypothesis actually asserts.
- When results are weak or partial, vary the approach before writing it off. One failed method doesn't falsify the hypothesis.
- If iterations remain, think about what the NEXT iteration will need. Leave useful building blocks — datasets, baselines, preliminary results — that future strategies can build on, refine, or compare against.
</research_methodology>

<principles>
1. FOCUS ON NOVELTY - every strategy must lead to a genuinely novel contribution
2. MAXIMIZE PARALLELIZATION - all artifacts in your strategy run in parallel
3. BUILD ON EXISTING WORK - use completed artifacts from previous iterations, learn from failures
4. ITERATE ON THE METHOD - a negative result is about the approach, not the hypothesis. Try different methods, parameters, data, or formulations within the hypothesis bounds.
5. DIAGNOSE BEFORE DECIDING - before each iteration, review what worked, what didn't, and why. Use that to choose what to try next. Gaps are action items, not conclusions.
6. SET DEPENDENCIES WISELY - depends_on is a list of {id, label} objects referencing existing artifacts; each label is a short free-text type (a word or two, e.g. "dataset", "validates", "extends") that tags how the dep is used
7. PLAN FOR DEPENDENCIES - if an artifact depends on another (e.g. experiments need datasets), ensure prerequisites exist first or plan them this iteration for the next
</principles>

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
Your strategy should advance this hypothesis.

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
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for study design, proper baselines, and the evaluation/validity norms this field demands.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<iteration_status>
Current iteration: 2 of 2
Remaining (including this one): 1
</iteration_status>

<previous_strategies>
Strategies from the PREVIOUS iteration. You can CONTINUE these directions,
ADAPT based on what worked and what didn't in the artifacts produced, or PIVOT if results suggest a better path.

--- Strategy 1 ---
kind: strategy
id: gen_strat_1_idx1
title: Pre-departure authority diffusion beats snapshot size
objective: >-
  Build a founder-TFDD corpus with re-derived Truck-Factor/DOA histories, compute a NEW pre-departure authority-diffusion
  trajectory metric (founder commit share + count of independent non-founder DOA file-owners in the 6-12 months before the
  founder's Truck Factor Developer Detachment), and test whether this trajectory predicts Avelino et al.'s 18-month post-TFDD
  survival outcome better than the snapshot covariates (stars, forks, contributors) their ESEM 2019 paper already showed are
  non-predictive.
rationale: >-
  Avelino et al. built and validated the exact DOA/TF/TFDD machinery this hypothesis needs but never looked backward in time
  from the detachment point — their own published null result (size doesn't separate survivors from non-survivors AT the TFDD)
  is the gap. Re-running their pipeline one window earlier on a real, freshly-mined GitHub corpus is the single artifact that
  can confirm or kill the hypothesis: everything else (matched pairs, regression, falsification shuffle) is a robustness check
  on top of one core measurement. A dedicated mining/labeling dataset artifact plus one comprehensive analysis experiment
  covers the full success criteria within budget, and a focused research artifact de-risks the trickiest engineering step
  (reliable git history mining + identity resolution) before the dataset build starts.
artifact_directions:
- id: research_iter1_dir1
  type: research
  objective: >-
    Pin down a concrete, reproducible recipe for (a) selecting a founder-TFDD-eligible GitHub corpus at meaningful scale within
    time/cost limits, (b) computing DOA and Truck Factor per Avelino et al.'s (ESEM 2019 / ICPC 2016) exact formulas from
    raw git log data, and (c) resolving contributor identity (email/name aliasing) well enough to track 'the founder' and
    'non-founder DOA owners' across a repo's history.
  approach: >-
    Fetch and fetch_grep both Avelino et al. papers (arXiv:1906.08058 for TFDD/Active-Inactive/1-year threshold; the 2016
    ICPC Truck Factor paper for the DOA formula: first-author bonus, weighted recency of commits/changes per file) to extract
    the exact DOA equation, the TF greedy-selection algorithm, and the validated abandoner threshold. Research practical git-mining
    approaches usable inside a Python EXPERIMENT/DATASET sandbox without a GitHub API token bottleneck: cloning shallow-vs-full
    repo histories via GitPython/pydriller, extracting per-file per-author change history, and simple email-normalization
    heuristics (lowercase+strip, name-collision merging) as a lighter substitute for Avelino et al.'s GitHub-API alias resolution.
    Identify 15-30 candidate popular single-founder OSS repos (spanning at least 3 languages and a range of star counts) with
    public git history reachable via `git clone` (e.g. via GitHub search/trending or curated awesome-lists) that plausibly
    already experienced a founder handoff, to seed the dataset artifact's search.
  depends_on: []
- id: dataset_iter1_dir2
  type: dataset
  objective: >-
    Produce a labeled corpus of OSS repos with per-repo: full commit/file-author history, computed yearly DOA and Truck-Factor
    sets, the identified founder-only TFDD event (if any) and its date, and pre/post-TFDD windows — the raw substrate the
    main experiment needs to compute authority-diffusion trajectories and survival outcomes.
  approach: >-
    Using pydriller/GitPython, shallow-clone ~40-80 popular single-founder-origin GitHub repos across multiple languages and
    popularity strata (sampled to avoid a popularity confound, not just take the biggest repos), each with >=3 years of history
    after any departure point so an 18-month survival window is never right-censored. For each repo compute yearly DOA (first-author
    bonus + weighted share of subsequent file changes, per Avelino et al.) and yearly Truck Factor via their greedy DOA-descending
    removal algorithm; detect the first TFDD where the departing TF set has size 1 (founder-only) using the validated 1-year
    silence threshold; exclude 'perils of mining GitHub' artifacts (history-losing migrations, non-code/awesome-list repos,
    forks with <2 years own history). Output each repo's full per-year DOA/TF table, the TFDD date, founder identity (normalized
    email/name), star/fork/contributor-count/language/license covariates at the TFDD snapshot, and the post-TFDD activity
    time series (commits/releases per month for 18+ months) needed to score Active/Inactive survival. Aim for at least 25-35
    qualifying founder-only-TFDD repos to leave enough power for the matched-pairs and regression tests downstream.
  depends_on: []
- id: experiment_iter1_dir3
  type: experiment
  objective: >-
    Compute the pre-departure authority-diffusion trajectory metric for every founder-TFDD repo in the dataset, score post-TFDD
    survival per Avelino et al.'s Active/Inactive/recovery model, and test whether diffusion predicts survival better than
    snapshot size/popularity covariates via (1) an ordinal/logistic regression with Benjamini-Hochberg-corrected coefficients
    and standardized-effect-size comparison against stars/forks/contributor-count, (2) a matched-pairs comparison stratified
    by size bucket contrasting founder-share<50%-plus->=2-DOA-owners projects against founder-share>=80% projects, and (3)
    the pre-registered falsification check that randomly relocates the 6-12-month 'pre-departure' window within each project's
    own history to confirm the effect is specific to the true pre-TFDD window and not a general-activity artifact.
  approach: >-
    For each dataset repo, from the 6-12 months immediately preceding its founder-only TFDD compute: founder's share of authored/merged
    commits, and the count of distinct non-founder accounts that had already reached top-DOA (primary ownership) on at least
    one file in that window. Fit (a) a logistic regression predicting binary survival and an ordinal regression predicting
    the graded thriving/maintained/dormant/dead outcome, with diffusion predictors plus stars/forks/contributor-count/language/license
    as controls, reporting standardized coefficients and BH-corrected p-values; (b) bucket repos into size-matched pairs/strata
    (approximate nearest-neighbor matching on log-stars/log-forks/contributor-count) and compute the survival-rate ratio between
    high-diffusion and low-diffusion projects with a bootstrap 95% CI; (c) rerun both analyses 500-1000 times with the pre-departure
    window relocated to a uniformly random point in each project's pre-TFDD history (same window length) to build a null distribution
    and report where the true-window effect falls relative to it. Report all three results against Avelino et al.'s published
    41% baseline TFDD survival rate and their d=0.13-0.26 snapshot effect sizes as reference points.
  depends_on: []
expected_outcome: >-
  A validated, reusable founder-TFDD corpus (dataset) with computed per-repo pre-departure authority-diffusion scores and
  post-TFDD survival labels, plus a completed statistical test (regression + matched-pairs + falsification shuffle) reporting
  whether the diffusion trajectory predicts survival with an effect size exceeding the snapshot covariates Avelino et al.
  found negligible-to-small — either confirming the core hypothesis with a concrete, comparable effect size (feeding directly
  into the paper's headline result) or producing a clear negative/boundary finding (e.g. diffusion predicts but the falsification
  shuffle shows it isn't window-specific) that the next iteration can refine with alternative diffusion formulations, larger
  samples, or corpus fixes.
summary: >-
  Re-mine a founder-TFDD OSS corpus and re-run Avelino et al.'s own DOA/Truck-Factor pipeline one time-window earlier to test
  whether pre-departure authority diffusion, not post-departure snapshot size, predicts project survival.
</previous_strategies>

<dependency_rules>
- depends_on is a list of objects {id, label} — each entry references an existing artifact and tags how it is being used
- "id" can ONLY reference IDs from <existing_artifacts> — never IDs you are proposing (all new artifacts run in parallel)
- "label" is a SHORT free-text type label (a word or two, NOT a sentence) describing what role the dep plays — e.g. "dataset", "validates", "extends", "supersedes". Required on every dep.
- Setting depends_on provides the dependency's out_dependency_files to your artifact at execution time
- If no suitable existing artifacts exist, use empty depends_on
- New artifact IDs are assigned by the system after submission — do not invent IDs for your proposed artifacts
</dependency_rules>

<available_artifact_types>
Artifact types you can plan. Use this to choose the right types for your strategy objectives.

<artifact_types>
RESEARCH
Web research to answer key questions — like a researcher making decisions.
Runtime: LLM Agent, no code execution.
Tools: the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text).
Capabilities: Find, synthesize, and compare information across sources; survey SOTA and best practices.
Deps: REQUIRED none | OPTIONAL other RESEARCH to build on prior findings

EXPERIMENT
Run code to test hypotheses, implement methods, and collect empirical results.
Runtime: Python 3.12, UV (any pip package), isolated workspace, gradual scaling (mini → full data).
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Implement and run any code-based experiment, compare method vs baselines.
Deps: REQUIRED at least one DATASET | OPTIONAL RESEARCH for methodology guidance

DATASET
Collect, prepare, and merge datasets for experiments and analysis.
Runtime: Python 3.12, UV, isolated workspace.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-hf-datasets (HuggingFace Hub — ML datasets, many UCI/OpenML/Kaggle mirrors), aii-owid-datasets (Our World in Data — global statistics), aii-json (schema validation). Also any Python source (sklearn.datasets, openml, direct URLs, APIs) — must verify within 300MB limit.
Capabilities: Search, acquire, transform, combine, and standardize data from any available source.
Deps: REQUIRED none | OPTIONAL RESEARCH for guidance on what data to collect

EVALUATION
Evaluate experiment results with metrics, statistical analysis, and validity checks.
Runtime: Python 3.12, UV (any evaluation library), isolated workspace, gradual scaling matching experiment.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Compute any quantitative metrics and statistical tests, analyze validity and robustness.
Deps: REQUIRED at least one EXPERIMENT | OPTIONAL DATASET if reference data needed

PROOF
Formally prove mathematical statements in Lean 4 with automated iteration.
Runtime: LLM agent with Lean 4 compiler feedback loop.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-lean (proof verification, Mathlib search, tactics: ring, linarith, nlinarith, omega, simp, etc.)
Capabilities: Formally verify properties and inequalities, iterative proof development, lemma decomposition.
Deps: REQUIRED none | OPTIONAL RESEARCH for mathematical background
</artifact_types>
</available_artifact_types>

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

RESEARCH executor scope:
  Output: research_out.json with {answer, sources, follow_up_questions} + research_report.md
  DOES: Web research — search, read, synthesize information from papers/docs/APIs into a structured report
  DOES NOT: Run code, download files, execute scripts, compute anything — no shell/Python access
  Use for literature surveys, API documentation, technical specifications — pure information gathering

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results

DATASET executor scope:
  Output: data_out.json with rows of {input, output, metadata_fold, ...} — raw data only, no derived computations
  DOES: Download/generate datasets, analyze candidates to pick the best ones, standardize to JSON schema (features, labels, folds, metadata), validate schema, split into full/mini/preview
  DOES NOT: Run experiments, train models, compute derived statistics (PID/MI/correlations/synergy matrices) as final output
  If you need to COMPUTE something from data (synergy matrices, MI scores, timing benchmarks), use an EXPERIMENT artifact instead

EVALUATION executor scope:
  Output: eval_out.json with evaluation results
  DOES: Any evaluation of experiment results — metrics, statistical tests, ablations, comparisons, visualizations, robustness checks, error analysis, etc.
  DOES NOT: Implement new methods (use EXPERIMENT), collect data (use DATASET)
  This is for analyzing experiment outputs from any angle

PROOF executor scope:
  Output: Lean 4 proof files (.lean) with verified theorems
  DOES: Write and verify Lean 4 formal proofs with Mathlib, iterative compilation
  DOES NOT: Run Python experiments, collect data, do empirical analysis
  Use only when formal mathematical guarantees are needed
</artifact_executor_scope>

<artifact_planning_rules>
RESEARCH: Plan early — findings guide dataset selection, experiment design, and methodology.
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
DATASET:
- Plan for REAL third-party datasets (HuggingFace, Kaggle, direct-download URLs) — downloadable within time and size constraints
- Describe dataset criteria (domain, size, format) — executors find exact sources, but you can suggest candidates or search directions
- ALWAYS prefer real datasets over synthetic. Synthetic is a LAST RESORT only when no suitable real data exists
EVALUATION: Must depend on at least one EXPERIMENT. Focus on statistical rigor and validity checks.
PROOF: Use only when the hypothesis requires formal mathematical guarantees. Lean 4 + Mathlib.
</artifact_planning_rules>

<existing_artifacts>
--- Item 1 ---
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
out_expected_files:
- research_out.json
out_dependency_files:
  file_list:
  - research_out.json

--- Item 2 ---
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
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json
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

--- Item 3 ---
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
</existing_artifacts>

<current_paper>
The current paper draft — represents the research story so far.

Use this to understand what's working, what's not, and what gaps remain.
Gaps and weak results signal what to try differently — not what to conclude.

# 1. Introduction

Single-founder open-source projects are a recognized failure mode in software engineering: a project with Truck Factor 1 -- one developer whose departure would immediately strand a majority of the codebase -- can vanish the day that developer stops committing [Avelino2016]. Avelino et al. formalized this event as a Truck-Factor-Developer-Detachment (TFDD) and, in a follow-up study of 1,932 GitHub projects, found that 315 (16%) experienced one, of which only 128 (41%) survived it [Avelino2019]. Understanding which departures a project survives is directly actionable: it tells maintainers, funders, and platform operators which projects are worth a targeted succession intervention before the founder leaves, rather than after.

This question matters at scale. Foundation-scale audits of package ecosystems put single-maintainer exposure in the tens of percent of actively used packages [Jabrayilzade2022, Coelho2017], and turnover studies across RubyGems, npm, and Rust show departure is a recurring, not rare, event [Constantinou2017, Fan2025]. A cheap, well-calibrated early-warning signal -- computed from public git history alone, with no access to private roadmaps or contributor sentiment -- would let a platform or foundation triage which projects to approach before, rather than after, the truck factor drops to zero.

The obvious signal is hard to extract cleanly. Avelino et al.'s own predictor is a *snapshot*: project size, developer count, and commit volume measured at the moment of the TFDD, with reported effect sizes in the small range (Cohen's d 0.13-0.26) [Avelino2019]. A snapshot, by construction, cannot see whether the project was already quietly redistributing ownership before the founder left, or whether the founder's exit came as a genuine surprise with no prior diffusion at all -- two situations a snapshot taken after the fact cannot tell apart, but which plausibly predict different outcomes. Testing a *trajectory* signal instead requires reconstructing, file by file and year by year, the same Degree-of-Authorship (DOA) computation the original papers used, applying it not once at a fixed snapshot but continuously over a 6-12 month pre-departure window, and doing so on a corpus of TFDD events that is large enough to give the resulting statistic power -- three requirements that, together, no prior study has satisfied for this exact class of event.

This gap has not been closed before now for a specific reason: the pre-departure window computation is a genuine methodological extension, not a direct reproduction. Avelino et al.'s DOA/TF pipeline was validated only at yearly full-history snapshots; recomputing it on an arbitrary sub-year window changes the meaning of first-authorship at the window boundary in a way the original validation never tested. Building this extension correctly first requires resolving several under-specified details in the primary sources -- the exact meaning of the "Deliveries" term in the DOA formula, the tie-breaking rule in the greedy Truck-Factor algorithm, and the boundary semantics of a sub-year authorship window -- each of which we verify explicitly against the primary sources before running the pipeline (Section 2).

We build this pipeline, mine a corpus of founder-only TFDD events directly from public git history, and pre-register a three-criterion test of the pre-departure authority-diffusion hypothesis: (i) BH-FDR-corrected statistical significance, (ii) an effect size that exceeds the snapshot covariates', and (iii) survival against a within-repo random-window placebo control that rules out the possibility that *any* 6-12 month window, not specifically the one before departure, would show the same correlation. Mining yields 30 founder-only TFDD events with sufficient pre- and post-departure history out of 62 candidate repositories. At this sample size, the regression and matched-pairs tests cannot be run for lack of usable within-corpus outcome variance, and the placebo test that does run places the true pre-departure window's founder-share correlation (r=0.180) at the 40th percentile of a 25-draw null distribution (empirical p=0.615) -- statistically indistinguishable from a randomly chosen window. All three pre-registered criteria fail. We report this as a negative result rather than retuning the protocol post hoc, and we document precisely where the corpus size, not the underlying question, is the binding constraint, so that a future study with a larger founder-only TFDD corpus can pick up exactly where the sample-size ceiling here leaves off.

## Summary of Contributions

- A verified, citation-anchored reconstruction of the Avelino et al. DOA / Truck-Factor / TFDD pipeline, including three corrections to working assumptions about the DOA formula, the survival state machine, and the yearly-snapshot validation scope (Section 2).
- A from-scratch corpus of 30 single-founder, founder-only TFDD events mined directly from public git history, with a fully reported exclusion funnel from 62 candidate repositories (Section 3).
- A pre-registered, three-criterion test of a new pre-departure authority-diffusion signal against Avelino et al.'s snapshot covariates, using logistic regression, matched-pairs comparison, and a within-repo placebo control (Section 4).
- A negative result: all three criteria fail at this corpus size, with the placebo test placing the true pre-departure window at the 40th percentile of its null distribution, and an explicit accounting of where sample size, rather than the underlying hypothesis, is the binding constraint (Section 5).

# 2. Background: The DOA / Truck-Factor / TFDD Pipeline

We reconstruct the measurement pipeline from its two primary sources -- Avelino et al.'s ICPC 2016 Truck Factor paper [Avelino2016] and their ESEM 2019 abandonment/survival paper [Avelino2019] -- rather than from secondary description, because three details load-bearing for our extension are easy to get wrong from prose alone.

**Degree of Authorship.** For a developer $d$ and file $f$, Degree-of-Authorship is
$$\mathrm{DOA}(d,f) = 3.293 + 1.098\cdot FA(d,f) + 0.164\cdot DL(d,f) - 0.321\cdot\ln(1+AC(d,f))$$
where $FA(d,f)=1$ if $d$ authored the file's first commit (else 0), $DL(d,f)$ is the raw count of $d$'s own commits to $f$, and $AC(d,f)$ is the count of commits to $f$ by any *other* developer [Avelino2016]. The regression weights are reused verbatim from Fritz et al.'s degree-of-knowledge model [Fritz2010] and were not refit by Avelino et al. A developer is an *owner* of $f$ if their normalized DOA exceeds 0.75 of the file's maximum and their absolute DOA is at least 3.293.

**Truck Factor.** The Truck Factor of a project at a point in time is computed by a greedy algorithm: repeatedly remove the developer who owns the most files, checking after each removal whether the *remaining* developers still collectively own at least 50% of files; the count of developers removed while coverage stays at or above 50% is the Truck Factor [Avelino2016]. The original papers do not specify a tie-breaking rule for developers with equal file-ownership counts, which we resolve by our own deterministic tie-break (highest cumulative DOA, then earliest GitHub-visible developer ID) and flag as a documented deviation.

**TFDD and survival.** A Truck-Factor-Developer-Detachment (TFDD) occurs when all of a project's current Truck-Factor-holding developers stop committing (operationalized as a gap of at least one year, the threshold whose harmonic mean of precision (0.82) and improvement (0.55) at 0.66 outperforms the 6-month, 1.5-year, and 2-year alternatives in Avelino et al.'s sensitivity analysis) [Avelino2019]. Active/Inactive is a strictly binary state relative to the *most recent* TFDD -- a project returns to Active the moment any new developer accrues Truck-Factor-holding DOA, and there is no fixed post-TFDD survival window in the primary source. We verified this explicitly because an earlier working hypothesis in our own planning assumed a graded thriving/maintained/dormant/dead outcome and an 18-month fixed observation window; neither has a basis in the primary sources, and we correct for this by defining survival relative to the last observed TFDD only, exactly as the source does.

Two points bear directly on our extension. First, Avelino et al. validated DOA/TF only at yearly full-history snapshots; they never recomputed it on an arbitrary sub-year window. Our 6-12 month pre-departure authority-diffusion measure is therefore a genuine methodological extension, not a reproduction, and the meaning of first-authorship at a window boundary (a file first touched *before* the window opens) is a choice we make explicit in Section 3 rather than one the source resolves for us. Second, corpus-level replication numbers (the 1,932-project corpus, 16% TFDD rate, 41% survival rate, and Cohen's d effect sizes of 0.13-0.26 for snapshot covariates) come from a curated corpus an order of magnitude larger than ours; we report our own corpus's replication numbers against these figures directly in Section 4 rather than assuming parity.

# 3. Dataset: Founder-Only TFDD Corpus

We search GitHub for single-founder repositories, download full commit histories with `git log --filter=blob:none` (a local, GitHub-API-independent extraction chosen because shallow clones cannot recover a file's true first-commit authorship, which the DOA formula's $FA$ term requires), and recompute the DOA/TF pipeline from Section 2 at yearly full-history snapshots to locate TFDD events.

**Corpus funnel.** Of 62 candidate repositories, mining and filtering yields 47 that pass a source-code-fraction prefilter, of which 30 exhibit a *founder-only* TFDD -- a TFDD whose Truck-Factor-holding developer set at the moment of detachment is exactly the project's original founder -- with sufficient commit history both before and after the event to compute both a 6-12 month pre-departure window and a post-TFDD survival outcome. The exclusion table is:

| Reason | Count |
|---|---|
| Passed all filters | 47 |
| Not mostly source code | 1 |
| No commits extracted (mining failure) | 14 |
| No founder-only TFDD found | 13 |
| Insufficient pre-TFDD history | 2 |
| Insufficient post-TFDD history | 2 |

A companion, independently-run dataset-construction pass over a separate 32-repository sample applies a stricter discard taxonomy and reports discard reasons of no qualifying founder-only TFDD (120), non-software low code fraction (24), too few commits (15), right-censored insufficient post-TFDD history (11), migration/squash mining artifacts (11), and too-large history (3), yielding 32 qualified examples labeled `Active_survived` (20) or `Inactive_did_not_survive` (12), spanning activity buckets thriving (12), maintained (8), dormant (11), and dead (1). We report both funnels because the experiment in Section 4 runs on its own independently mined 62-repository curation rather than consuming this dataset artifact directly (Section 5 discusses this as a limitation); the two funnels are consistent in shape -- founder-only-TFDD scarcity and post-departure right-censoring are the two largest attrition sources in both -- which is the evidence we have that the 30- and 32-repository corpora are drawn from the same underlying population rather than differing systematically in construction.

[FIGURE:fig_exclusion_funnel]

**Pre-departure window.** For each founder-only TFDD, we recompute two authority-diffusion covariates over the 6-12 months immediately preceding the TFDD date: *founder commit share* (the founder's fraction of commits in the window) and *count of independent non-founder DOA file-owners* newly accruing ownership in the window. Both are computed with the same DOA formula and ownership threshold as Section 2, applied to the restricted window rather than the full history -- the extension flagged there. Snapshot covariates (stars, forks, total contributors, language, project age) are captured at the TFDD date itself, at quarterly granularity with a documented approximately 1.5-month TFDD-date fuzz, matching the temporal resolution Avelino et al.'s own snapshot measurement used.

# 4. Experiment: Does Pre-Departure Diffusion Predict Survival?

**Method.** We test whether the pre-departure authority-diffusion covariates (founder commit share, count of independent non-founder DOA owners) predict 18-month post-TFDD survival better than the snapshot covariates Avelino et al. used, via three pre-registered tests: (1) BH-FDR-corrected logistic regression of survival on the diffusion covariates; (2) a matched-pairs bootstrap comparing survival rates between high- and low-diffusion repositories matched on snapshot covariates; (3) a within-repo random-window placebo control, which recomputes the founder-share correlation on 25 randomly placed 6-12 month windows drawn from each repository's own history (not necessarily immediately pre-TFDD) to test whether the true pre-departure window's correlation is distinguishable from an arbitrary window's. Success requires all three of: (i) diffusion-covariate significance at BH-FDR $p<0.10$; (ii) a diffusion-covariate effect size exceeding the corresponding snapshot-covariate effect size; (iii) the true window's correlation surviving the placebo test at empirical $p<0.10$.

**Baseline replication.** Among the 47 filtered candidate repositories, the founder-only-TFDD rate is 63.8%, against Avelino et al.'s reported 16% TFDD rate in their much larger, differently-curated corpus; survival is 36.7% here against their reported 41%. The large gap in TFDD rate is an artifact of our candidate selection, which deliberately seeds and filters toward single-founder projects likely to exhibit exactly this event, rather than sampling top-starred repositories broadly as the original corpus did -- it is a targeted, not representative, sample by construction, and we flag it as such rather than as a replication failure. Snapshot-covariate effect sizes on survival in our corpus are Cohen's d = -0.226 (developers at TFDD), -0.558 (commits at TFDD), and -0.625 (files at TFDD); log-stars and log-forks effect sizes could not be computed (undefined variance in this corpus). These magnitudes are larger in absolute value than Avelino et al.'s reported 0.13-0.26 range, consistent with our smaller, more targeted corpus producing noisier point estimates rather than with a genuinely stronger snapshot effect.

[FIGURE:fig_snapshot_effects]

**Diffusion-covariate tests.** The logistic regression could not be run to completion: with 30 founder-only TFDD repositories and the covariate set specified, the fitted model reduces to zero usable observations (`n_used=0`) because of insufficient outcome variance within cells after covariate stratification. The matched-pairs bootstrap fails for the same underlying reason: stratifying the 30 repositories into high- and low-diffusion groups matched on snapshot covariates leaves zero repositories in each matched group (`n_high=0, n_low=0`) at the sample size available. Both criteria (i) and (ii) are therefore unmet -- not because the diffusion covariates were tested and found insignificant, but because the corpus is too small to run the test as pre-registered at all.

**Placebo test.** The one test that does run is the within-repo placebo control. The true pre-departure window's founder-share correlation with survival is r = 0.180. Against a null distribution built from 25 randomly placed within-repo windows, this places the true window at the 40th percentile (empirical p = 0.615) -- the true pre-departure window is *less* extreme than a majority of arbitrary windows drawn from the same repositories' histories. Criterion (iii) fails.

[FIGURE:fig_placebo_null]

**Verdict.** All three pre-registered success criteria fail: no BH-FDR-significant diffusion effect (untestable at this sample size), no diffusion effect exceeding the snapshot covariates' (untestable at this sample size), and no placebo-surviving correlation (tested and rejected, r=0.180 at the 40th percentile of null). Per our pre-registered fallback plan, we report this outcome directly rather than relaxing thresholds, pooling additional covariates, or down-sampling the snapshot baseline to manufacture a comparison the diffusion signal could win.

# 5. Discussion

**What failed, and what did not.** The pre-departure authority-diffusion hypothesis does not fail because the underlying mechanism was tested and refuted with a clean null correlation -- the placebo test result (r=0.180, 40th percentile) is a genuine, informative null, but the regression and matched-pairs tests never ran to completion at all. A corpus of 30 founder-only TFDD events, once split by a binary survival outcome and further stratified for covariate matching, does not leave enough repositories per cell for the tests as pre-registered. This is a sample-size ceiling, not evidence against the hypothesis: 30 events is small relative to the 315 TFDDs Avelino et al. observed in their much larger corpus, and our own funnel (Section 3) shows that founder-only-TFDD scarcity, not any downstream filtering choice, is the dominant source of attrition (13 of 62 candidates excluded for lacking a qualifying event at all, and a comparable pattern -- 120 of the dataset artifact's discards -- in the independently mined companion corpus). Scaling the candidate pool by roughly an order of magnitude, matching Avelino et al.'s original corpus size, is the direct next step this result points to, and the exclusion funnel in Section 3 gives an explicit basis for estimating how large a candidate pool that requires.

**The window-boundary extension remains unvalidated in isolation.** Because DOA/TF was validated by its original authors only at yearly full-history snapshots, our sub-year pre-departure window computation is inherently an extension whose calibration we cannot separately verify against a ground truth the primary sources provide. We mitigate this by using the identical DOA formula and ownership threshold inside the window as at the full-history snapshot, changing only the commit-history slice the formula is computed over, but we cannot rule out that some of the variance in our diffusion-covariate estimates reflects window-boundary artifacts (a file whose true first commit falls before the window opens, for instance) rather than genuine pre-departure ownership change. A future study with a larger corpus should budget for this validation directly, for example by checking window-recomputed DOA against full-history DOA on a held-out set of non-TFDD projects where no departure-driven change is expected.

**Corpus provenance mismatch.** The experiment in Section 4 runs on its own 62-repository curation rather than consuming the 32-repository dataset artifact of Section 3 directly, because the dataset artifact was not yet available at experiment run time. We report both funnels rather than silently reconciling them; their consistent attrition pattern is the evidence available that this did not introduce a systematic selection difference, but it is not a substitute for re-running the experiment against the dataset artifact's exact 32 repositories, which we flag as the most direct way to close this gap.

**Identity resolution.** Avelino et al.'s own developer-identity resolution used GitHub-API commit-to-account mapping (median 11% alias rate); we substitute a local heuristic (normalized name/email matching, GitHub noreply-ID special-casing, union-find merge, bot exclusion) because API-scale access was not available, and this heuristic is unvalidated against the API-based reference rate. A residual alias rate higher than 11% would inflate the apparent number of distinct authors and could bias the diffusion covariates -- specifically, the count of independent non-founder DOA owners -- toward undercounting genuine authority diffusion if a returning founder's alternate identity is mistaken for a new contributor, or overcounting it in the reverse case.

**Limitations.** (1) The regression and matched-pairs tests are untested, not refuted, at this corpus size; we report their non-completion explicitly rather than substituting a weaker proxy test that could be run. (2) The 63.8% founder-only-TFDD rate in our filtered corpus reflects targeted candidate selection, not a representative base rate, and should not be read as a revised estimate of TFDD prevalence. (3) Snapshot-covariate effect sizes measured on our corpus (d = -0.23 to -0.63) are not directly comparable in magnitude to Avelino et al.'s reported 0.13-0.26, both because of corpus-size noise and because our targeted sample composition differs from theirs. (4) The pre-departure window extension's boundary semantics are a documented methodological choice, not a validated reproduction of a technique the original papers tested. (5) The placebo null distribution uses 25 draws (reduced from a planned 1,000 for compute budget), which limits the resolution of the empirical p-value; a p-value of 0.615 is unlikely to change qualitative conclusion under a finer null, but the exact percentile is imprecise at this draw count.

# 6. Conclusion

We set out to test whether authority diffusion in the months before a founder's departure predicts open-source project survival better than the snapshot covariates a prior study used. Building the measurement pipeline required resolving three under-specified details in the primary sources and constructing a from-scratch corpus of 30 founder-only TFDD events from public git history. Against a pre-registered three-criterion protocol, the hypothesis fails on all three counts: two tests could not be run at this sample size for lack of within-corpus outcome variance, and the one test that did run -- a within-repo placebo control -- places the true pre-departure window at the 40th percentile of a null distribution built from arbitrary windows in the same repositories' histories (r=0.180, empirical p=0.615). We report this as a negative result rather than relaxing the pre-registered thresholds, and we localize the binding constraint precisely: founder-only-TFDD scarcity, not the underlying mechanism, is what our corpus funnel shows is limiting statistical power. Future work should scale the candidate pool toward parity with the 1,932-project corpus the original snapshot result was measured on, separately validate the sub-year DOA window extension against a held-out non-departure control, and re-run the diffusion-covariate tests directly against the dataset artifact's 32-repository corpus rather than an independently mined 62-repository curation, before drawing a conclusion about whether pre-departure trajectory information adds anything a post-hoc snapshot does not.
</current_paper>

<reviewer_feedback>
Paper reviewer feedback from the previous iteration. Your strategy MUST address these critiques.
Prioritize major issues — these are the most impactful improvements to make.

- [MAJOR] (evidence) Two of the three pre-registered success criteria (BH-FDR logistic regression and matched-pairs bootstrap) do not run to completion -- n_used=0 and n_high=0/n_low=0 respectively. The paper's abstract and conclusion nonetheless state that 'the hypothesis fails on all three counts' and treat this as a negative result about the underlying mechanism. A test that cannot execute provides zero evidence either for or against the hypothesis; conflating 'untestable' with 'tested and failed' materially overstates what the paper shows.
  Action: Reframe every top-level claim (abstract, contributions list, Section 4 verdict, conclusion) to separate 'untested for lack of power' (2/3 criteria) from 'tested and null' (1/3 criteria, the placebo). Do not use language like 'the hypothesis fails on all three counts' -- state instead that the protocol could only execute one of three pre-registered tests, and that test alone is inconclusive-to-null.
- [MAJOR] (methodology) The experiment (Section 4) is run on an independently-mined 62-repository curation, not on the paper's own 32-repository dataset artifact (Section 3's 'companion' funnel). The paper acknowledges this only in the Discussion as a limitation, attributing it to the dataset artifact 'not yet being available at experiment run time.' This means the paper's headline dataset contribution (30 founder-only TFDD events with full exclusion funnel) and its headline experimental result are drawn from two different, only qualitatively-compared corpora -- a significant internal inconsistency for a paper whose central claim rests on corpus construction rigor.
  Action: Either (a) re-run the experiment against the 32-repository dataset artifact and report both results side by side, or (b) if that is infeasible in this iteration, merge Sections 3 and 4 to describe only the 62-repository experimental corpus as the paper's dataset, and present the 32-repository artifact separately and explicitly as a distinct, not-yet-integrated resource -- do not imply methodological unity between the two where none currently exists.
- [MAJOR] (methodology) The core measurement extension -- computing DOA/Truck-Factor over a 6-12 month sub-year window rather than Avelino et al.'s validated yearly full-history snapshot -- is acknowledged as 'unvalidated' throughout the paper (Section 2, Section 5) but is nonetheless used as the paper's primary independent variable. No sensitivity or robustness check (e.g., varying window width, or the proposed held-out non-TFDD validation) is actually run in this iteration; it is deferred entirely to 'future work.' Given that this window computation is the paper's stated central technical extension over prior work, leaving it fully unvalidated is a significant gap -- if the window computation is itself noisy or biased at the boundary, that alone could explain the null placebo result without implicating the underlying hypothesis.
  Action: Run the proposed validation check now, even on a small held-out set: compute window-recomputed DOA on a handful of non-TFDD projects (no departure event) at several 6-12 month windows drawn from stable periods, and report how much window-boundary noise alone contributes to founder-share variance. Without this, the paper cannot distinguish 'the diffusion signal is genuinely absent' from 'the measurement of the diffusion signal is too noisy to detect anything.'
- [MINOR] (rigor) The placebo null distribution uses only 25 draws (Section 4, Limitation 5), reduced from a planned 1,000 for compute budget. At n=25, the empirical percentile (40th) has coarse resolution -- individual draws move the percentile by 4 points -- and the paper's claim that 'a p-value of 0.615 is unlikely to change qualitative conclusion under a finer null' is asserted without any supporting calculation (e.g., a binomial CI on the percentile, or a parametric approximation of the null).
  Action: Either increase the draw count to at least 200-500 (the compute cost of a placebo re-draw should be modest relative to the rest of the pipeline) or report a confidence interval on the empirical percentile (e.g., via bootstrap resampling of the 25 draws, or a normal approximation to the underlying correlation-null) to substantiate the robustness claim rather than asserting it.
- [MINOR] (scope) Snapshot-covariate effect sizes reported in the paper's own corpus (Cohen's d = -0.226 to -0.625) are 2-3x larger in absolute magnitude than Avelino et al.'s reported 0.13-0.26, and the paper attributes this entirely to 'corpus-size noise' from the smaller, targeted sample. This is plausible but not verified -- no confidence intervals are reported alongside these point estimates, so a reader cannot assess whether the discrepancy is within sampling noise or reflects a genuine difference in the targeted-corpus population (e.g., systematically larger/more visible projects, given the seed-list construction described in the research artifact).
  Action: Report bootstrap or analytic confidence intervals on all Cohen's d effect sizes in Section 4's baseline replication, and explicitly state whether Avelino et al.'s original 0.13-0.26 range falls inside or outside those intervals -- this converts a hand-waved attribution into a checkable claim.
- [MINOR] (clarity) The paper reports a founder-only-TFDD rate of 63.8% in its filtered corpus against Avelino et al.'s reported 16%, a 4x difference explained as an artifact of targeted candidate selection. This explanation is plausible, but the mechanics of how the candidate list was constructed (Section 3 mentions only 'we search GitHub for single-founder repositories') are underspecified relative to the level of detail given elsewhere in the paper -- the supplementary research artifact reveals a curated 10-entry seed list with explicit exclude/caution flags, which is not described in the main text at all.
  Action: Add a short paragraph to Section 3 describing the candidate-selection procedure (seed-list curation, exclusion of known non-single-founder or fork-not-handoff projects such as youtube-dl/yt-dlp) so the 4x TFDD-rate discrepancy is explainable from the main text alone rather than requiring the supplementary artifact.
- [MINOR] (novelty) The paper positions its contribution primarily as testing a new trajectory-based signal against Avelino et al.'s snapshot covariates, but does not engage with the broader bus-factor/knowledge-concentration prediction literature beyond the two Avelino et al. papers and brief citations to ecosystem-turnover studies (Jabrayilzade2022, Coelho2017, Constantinou2017, Fan2025). Related work on predicting OSS project abandonment or 'survival' more broadly (e.g., using activity time-series, issue/PR dynamics, or social network features) is not discussed, making it hard to judge whether a 'trajectory vs. snapshot' framing is itself a known distinction in adjacent prediction literatures.
  Action: Add a short related-work paragraph situating the trajectory-vs-snapshot distinction against general OSS-abandonment-prediction literature (which often already uses time-series/activity-trend features, not just point-in-time snapshots), to clarify what specifically is new here: the DOA-based authority-diffusion operationalization, not the general idea of using trends rather than snapshots.
- [MINOR] (methodology) Identity resolution (Section 5, 'Identity resolution') uses an unvalidated local heuristic in place of Avelino et al.'s GitHub-API-based alias resolution (median 11% alias rate), and the paper correctly flags that this could bias the diffusion covariate (count of independent non-founder DOA owners) in either direction. At n=30 with an already-underpowered test, even modest misclassification of author identity could materially shift which repositories qualify as 'founder-only' TFDD events in the first place -- this is a data-quality risk affecting corpus construction, not just covariate noise.
  Action: Spot-check identity resolution against GitHub API results (even without full-scale API access, a random 10-15 repo sample checked manually against GitHub profile pages would suffice) and report the observed alias/merge error rate on that sample, to give readers a concrete bound rather than an open-ended caveat.
</reviewer_feedback>

<task>
Generate 1 research strategy for THIS iteration.

**ARTIFACT LIMIT: Each strategy may contain AT MOST 3 artifact directions.** Focus on the highest-impact artifacts. Quality over quantity.

Each strategy should:
1. Define a clear OBJECTIVE - what novel contribution we're building toward
2. Plan artifacts to execute NOW - specify type, objective, approach, and depends_on for each
3. Account for parallel execution - all strategies and all planned artifacts run simultaneously, their artifacts are combined into one shared pool

**BROADER IS NOT THE SAME AS DEEPER.** Adding models, datasets, or settings to
an experiment that already ran makes the table bigger; it does not make the
contribution stronger, and it is the default a strategy generator drifts into
when it has nothing sharper to propose. Spend an artifact on scale only when
the SPREAD itself is the finding (a scaling trend, a regime boundary, a
generalisation claim the paper actually makes). Otherwise spend it on
something that could change the conclusion: the mechanism behind an observed
effect, the condition under which it disappears, the confound that would
explain it away, or the baseline whose absence a reviewer would name first.


</task><user_data>
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
  "$defs": {
    "ArtifactDep": {
      "description": "A single dependency on an existing artifact, with a short type label.\n\n``id`` and ``label`` are LLM-generated at strategy time. ``label`` is free-text but\nshort \u2014 a word or two naming the type of dependency, not a sentence.\n\n``relation_type`` and ``relation_rationale`` are populated later, in upd_hypo,\nusing the MultiCite citation-function typology (Lauscher et al., NAACL 2022).\nThey are absent at strategy time and may stay absent for legacy runs.",
      "properties": {
        "id": {
          "description": "ID of an existing artifact this artifact depends on",
          "title": "Id",
          "type": "string"
        },
        "label": {
          "description": "Short free-text label naming the type of this dependency (a word or two, not a sentence)",
          "title": "Label",
          "type": "string"
        }
      },
      "required": [
        "id",
        "label"
      ],
      "title": "ArtifactDep",
      "type": "object"
    },
    "ArtifactDirection": {
      "description": "High-level direction for an artifact to execute this iteration.\n\nID is code-assigned (LLMPrompt only \u2014 visible in prompts, not LLM-generated).",
      "properties": {
        "type": {
          "description": "Type of artifact to create",
          "enum": [
            "experiment",
            "research",
            "proof",
            "evaluation",
            "dataset"
          ],
          "title": "Type",
          "type": "string"
        },
        "objective": {
          "description": "What we want to achieve with this artifact",
          "title": "Objective",
          "type": "string"
        },
        "approach": {
          "description": "High-level direction/method",
          "title": "Approach",
          "type": "string"
        },
        "depends_on": {
          "description": "Existing artifacts this depends on, each with a short type label",
          "items": {
            "$ref": "#/$defs/ArtifactDep"
          },
          "title": "Depends On",
          "type": "array"
        }
      },
      "required": [
        "type",
        "objective",
        "approach"
      ],
      "title": "ArtifactDirection",
      "type": "object"
    },
    "Strategy": {
      "description": "A research strategy.\n\nContent fields have LLMPrompt + LLMStructOut markers.\n``id`` is code-assigned (LLMPrompt only \u2014 visible in prompts, not LLM-generated).\n\nID format: gen_strat_idx{N}",
      "properties": {
        "title": {
          "description": "Strategy name in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "objective": {
          "description": "The novel contribution we're building toward",
          "title": "Objective",
          "type": "string"
        },
        "rationale": {
          "description": "Why this strategy is promising",
          "title": "Rationale",
          "type": "string"
        },
        "artifact_directions": {
          "description": "Artifacts to execute THIS iteration",
          "items": {
            "$ref": "#/$defs/ArtifactDirection"
          },
          "title": "Artifact Directions",
          "type": "array"
        },
        "expected_outcome": {
          "description": "What we'll have after this iteration's artifacts complete",
          "title": "Expected Outcome",
          "type": "string"
        },
        "summary": {
          "default": "",
          "description": "Brief summary of the strategy and its expected contribution",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "title",
        "objective",
        "rationale",
        "artifact_directions",
        "expected_outcome"
      ],
      "title": "Strategy",
      "type": "object"
    }
  },
  "description": "Top-level wrapper for LLM strategy generation output.",
  "properties": {
    "strategies": {
      "description": "List of generated strategies",
      "items": {
        "$ref": "#/$defs/Strategy"
      },
      "title": "Strategies",
      "type": "array"
    }
  },
  "required": [
    "strategies"
  ],
  "title": "Strategies",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-21 17:41:23 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SYSTEM-USER prompt · 2026-08-21 17:42:07 UTC

```
<verification_results>
Your previous response had issues that need fixing:

DEPENDENCY ERRORS (depends_on can ONLY reference IDs from <existing_artifacts>):
  - Strategy 1: Artifact 'dataset_iter2_dir1' (dataset): dependency 'art_24Q1bYB_ULpu' has type 'dataset' which is not allowed (allowed: {'research'})
  - Strategy 1: Artifact 'dataset_iter2_dir1' (dataset): dependency 'art_eXxdnfS0o6aV' has type 'experiment' which is not allowed (allowed: {'research'})
  - Strategy 1: Artifact 'experiment_iter2_dir2' (experiment): dependency 'art_eXxdnfS0o6aV' has type 'experiment' which is not allowed (allowed: {'dataset', 'research'})
  - Strategy 1: Artifact 'experiment_iter2_dir2' (experiment): missing required dependency. Must have at least one dependency of type: {'dataset'}

</verification_results>

<task>
Fix ALL issues above and regenerate your strategies:

1. Fix dependency errors:
   - depends_on is a list of {id, label} objects — every entry MUST have a non-empty short label
   - id can ONLY reference IDs from <existing_artifacts>
   - You CANNOT reference artifacts you are proposing in this strategy as dependencies (they all run in parallel)
   - Follow the dependency type rules (e.g., experiments require datasets)
   - If no suitable existing artifacts exist, use depends_on: []

Output the corrected JSON with the fixed strategies.
</task>
```
