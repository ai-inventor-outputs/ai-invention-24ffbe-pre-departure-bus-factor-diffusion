# gen_strat_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_strat`
> Run: `run_5SMkWpWKNLxk` — Measuring Authority Diffusion Before Founders Leave Open Source Projects
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_strat_1` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-08-20 20:06:40 UTC

```
model: claude-sonnet-5 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_strat/gen_strat_1
```

### [2] SYSTEM-USER prompt · 2026-08-20 20:06:48 UTC

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
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for study design, proper baselines, and the evaluation/validity norms this field demands.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
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
title: Pre-Departure Authority Diffusion Predicts Survival
objective: >-
  Build a real-repo corpus of single-founder OSS projects, compute Avelino et al.'s DOA/Truck-Factor pipeline both AT and
  BEFORE each founder TFDD, and test whether the pre-departure authority-diffusion trajectory (founder commit share, count
  of independent non-founder DOA-file-owners in the 6-12 months before departure) predicts 18-month post-departure survival
  better than snapshot size covariates.
rationale: >-
  Avelino et al.'s ESEM 2019 paper establishes the exact TFDD/DOA/Active-Inactive machinery and reports the key null result
  this hypothesis exploits (size doesn't predict survival at the snapshot) but never computes a pre-departure trend. Reimplementing
  their published, validated DOA algorithm one window earlier is the single artifact that can confirm or refute the hypothesis
  directly — everything else (matched pairs, regression, placebo shuffle) is downstream analysis of that one computation.
  Concentrating this iteration on getting real commit-history data and a correct DOA/TFDD implementation running is higher-value
  than any breadth expansion, since without it there is no evidence to evaluate at all.
artifact_directions:
- id: dataset_iter1_dir1
  type: dataset
  objective: >-
    Assemble a real GitHub commit-history corpus of single-founder open-source projects with >=3 years of post-founder-departure
    history, sufficient to compute yearly DOA/Truck-Factor and identify founder-only TFDD events.
  approach: >-
    Use the GitHub REST/GraphQL API (or GH Archive / a HuggingFace mirror of GitHub metadata if available) to pull full commit
    logs (author email, timestamp, files changed, insertions/deletions) plus repo metadata (stars, forks, contributor count,
    language, license, creation date) for a stratified sample of ~150-250 popular repos across several languages, sampled
    across popularity strata (not just top-N, to avoid confounding diffusion with sheer size). Filter out repos with <3 years
    post-creation history, no clear single dominant original committer in year 1, or obvious 'mining GitHub' artifacts (squashed/migrated
    history, non-software repos, awesome-lists) per Avelino et al.'s exclusion criteria. Output per-repo: full per-commit
    author/file/timestamp records plus repo-level metadata, standardized to JSON with fold splits (train-style holdout by
    repo for later matched-pairs use), staying within the 300MB limit via targeted repo counts and commit-diff summarization
    rather than raw diffs.
  depends_on: []
- id: experiment_iter1_dir2
  type: experiment
  objective: >-
    Implement Avelino et al.'s DOA-based Truck Factor / TFDD pipeline, locate each project's first founder-only (TF=1) TFDD,
    compute the NEW pre-departure authority-diffusion trajectory (founder commit-share and distinct non-founder DOA-file-owner
    count in the 6-12 months immediately before that TFDD) alongside the snapshot covariates Avelino et al. use (developers/commits/files
    AT the TFDD), and compute the 18-month post-TFDD survival outcome per their Active/Inactive model.
  approach: >-
    Reimplement Fritz et al.'s DOA formula (first-authorship + acceptance-ratio-weighted change ownership) per file per year
    exactly as specified in Avelino et al. 2016/2019, derive per-year Truck-Factor sets, detect the first TFDD where the detaching
    TF set has size 1, and label 6-12-months-pre-TFDD authority diffusion vs the at-TFDD snapshot. Fit (a) a matched-pairs
    comparison bucketed by stars/forks/contributor-count comparing survival rates for high- vs low-pre-departure-diffusion
    projects, and (b) a logistic/ordinal regression of survival on diffusion predictors plus snapshot/popularity controls
    (BH-corrected p-values, standardized effect sizes vs Avelino et al.'s reported d=0.13-0.26). Include the placebo/shuffle
    check: relocate the 'pre-departure window' randomly within each project's history and confirm the effect weakens. Uses
    the raw commit-history dataset planned in this same strategy as its input once it completes.
  depends_on: []
- id: evaluation_iter1_dir3
  type: evaluation
  objective: >-
    Rigorously validate the DOA/TFDD implementation against Avelino et al.'s published aggregate statistics and stress-test
    the core diffusion-vs-survival finding for robustness and confound-freedom before it is trusted as evidence.
  approach: >-
    Sanity-check the reimplemented pipeline by comparing corpus-level aggregate rates (TFDD incidence, share of TFDDs at TF=1,
    overall 18-month survival rate) against Avelino et al.'s reported figures (16% TFDD rate, 66% at TF=1, 41% survival) as
    a validity check that the pipeline is computing what it claims; flag and diagnose any large deviation before trusting
    downstream results. Then run robustness checks on the main experiment's matched-pairs and regression results: sensitivity
    to the 6-12-month window boundary choice, sensitivity to the founder-identification heuristic (email/alias resolution),
    and a check that the diffusion effect is not simply proxying for repo age (since Avelino et al. found survivors are significantly
    younger) by re-running the regression with age as an added control. Report whether success criteria 1-3 from the hypothesis
    are met with confidence intervals.
  depends_on: []
expected_outcome: >-
  A validated real-data DOA/TFDD pipeline reproducing Avelino et al.'s aggregate statistics as a sanity check, plus a first
  empirical test of whether pre-departure authority-diffusion (founder commit-share drop, independent non-founder DOA-file-ownership
  count before TFDD) predicts post-founder survival beyond what snapshot popularity/size covariates predict — including a
  matched-pairs lift estimate, a BH-corrected regression, and a placebo/window-shuffle robustness check, giving the next iteration
  a decision point on whether to refine the diffusion metric, expand the corpus, or pivot the framing if the effect is null
  or confounded by age.
summary: ''
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

--- Item 2 ---
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

--- Item 3 ---
id: art_JvYoV94jgkuB
type: evaluation
title: Calibrating and Stress-Testing the Founder-Departure Diffusion Result
summary: >-
  Two-stage evaluation of the founder-authority-diffusion-vs-survival experiment. Stage A (calibration gate) recomputes Avelino
  et al. (ESEM 2019)'s three headline aggregate statistics -- Truck-Factor-Detachment-Departure (TFDD) incidence rate, share
  of TFDDs at TF=1, and overall 18-month survival rate -- over the 15-repo dataset dependency's raw commit event log, with
  95% Wilson CIs and PASS/FLAG_DEVIATION status per check, plus a snapshot-null Cohen's d replication and a 4-step diagnostic
  protocol (strata composition, abandoner-threshold parameter, hand-traced DOA sanity check, alias-collapse-rate spot check)
  that runs automatically whenever any check is flagged. Stage B runs five robustness/confound-freedom checks against the
  main experiment's founder-only-TFDD diffusion-vs-survival finding: (6) window-boundary sensitivity across a near/far/end-offset
  grid with BH-corrected logistic-regression p-values per variant and a sign-stability verdict; (7) founder-identification-heuristic
  sensitivity (first-commit author vs first-calendar-year plurality vs highest-lifetime-DOA) with a disagreement rate; (8)
  an age-at-TFDD confound check comparing diffusion-coefficient sign/significance before and after adding repo age as a covariate,
  plus VIF and a founder-share-vs-age correlation; (9) matched-pairs bucket-definition sensitivity (quartile vs log-scale
  star bins) with bootstrap CIs on the survival lift; and (10) an explicit permutation test (random relocation of the pre-departure
  window within project history) yielding a two-sided permutation p-value, split by eventual survivors vs non-survivors. All
  rate/effect-size outputs carry 95% CIs (Wilson for proportions, >=1000-resample bootstrap otherwise) and multi-test families
  are BH-adjusted. The three hypothesis success criteria are re-scored PASS/FAIL/PARTIAL with exact numeric evidence, and
  an overall verdict integrates the Stage A gate with the Stage B evidence. On this run: n_corpus=15, Stage A gate=FLAG_DEVIATION
  (small opportunistic sample vs Avelino's 1932-repo stratified corpus, so CIs are wide but still miss two of three reference
  rates), n_founder_tfdd_events=5 (severely underpowered for regression/permutation inference), and overall verdict=DOES_NOT_SUPPORT_PIPELINE_UNCALIBRATED
  -- the evaluation's central, actionable finding is that the pipeline needs a substantially larger corpus before its diffusion-vs-survival
  claim can be trusted, not that the effect itself is false. A prior execution attempt crashed the container because check10's
  permutation test called the O(n_commits) DOA-recomputation routine ~5000 times (bundles x 1000 permutations) with no caching,
  which this run fixed by hard-capping permutations to 60/40 draws -- eval.py now completes end-to-end in ~165s. Downstream
  artifacts should read eval_out.json's stage_a_calibration.gate_status and stage_b_robustness fields, and treat the power_caveat
  field in final_scoring as load-bearing given n_founder_tfdd_events=5.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
out_dependency_files:
  file_list:
  - eval.py
  - full_eval_out.json
  - mini_eval_out.json
  - preview_eval_out.json
</existing_artifacts>

<current_paper>
The current paper draft — represents the research story so far.

Use this to understand what's working, what's not, and what gaps remain.
Gaps and weak results signal what to try differently — not what to conclude.

# Introduction

Open-source software projects routinely depend on the sustained attention of one or two people. When the developer who founded such a project — usually its largest single contributor for years — stops committing, the project faces what Avelino et al. formalize as a Truck-Factor Developer Detachment (TFDD): every developer in the project's minimal Truck-Factor set has gone silent for at least a validated abandoner threshold of twelve months [1]. Some of these projects go dark permanently; others are picked up by new maintainers and continue for years. Predicting which outcome a given project will have, before it happens, is the problem this paper addresses.

The stakes are concrete rather than academic. Millions of downstream packages and companies depend transitively on a small number of widely-used repositories, many of which were built and are still nominally led by a single founding developer. Foundations that exist specifically to keep such software alive — the Apache Software Foundation's Incubator, NumFOCUS, the Software Freedom Conservancy — allocate limited staff time and money across candidate projects under exactly this uncertainty: which founder-led project is at real risk, and which will be fine regardless of intervention.

The problem is hard because the obvious predictor does not work. Avelino et al. mined 1,932 popular GitHub repositories, identified 315 TFDD events, and found that 128 of them (41%) survived — but at the TFDD snapshot itself, surviving and non-surviving projects are statistically indistinguishable in developers, commits, and files, with negligible-to-small effect sizes (Cohen's d = 0.13 for files, 0.25-0.26 for developers and commits) [1]. Popularity and size at the moment of departure, the folk explanation ("it was big enough to survive"), carries almost no signal in their data. A predictor built on that snapshot would perform little better than chance.

No prior work resolves this because no prior work looks earlier. Avelino et al.'s own Degree-of-Authorship (DOA) and Truck-Factor pipeline [1, 2] is validated and precise, but it is evaluated strictly at and after the TFDD: whether a new Truck-Factor developer is attracted afterward, not whether authority was already moving toward one before the founder left. Coelho and Valente's survey of 104 failed projects identifies why maintainers say they stopped, but that is a single-maintainer self-report about abandonment, not a multi-contributor measurement of whether authority existed elsewhere before departure [4]. The organizational-succession literature outside software offers the analogous distinction directly: family firms survive founder exit at higher rates when authority was delegated to a management team beforehand ("planned succession") rather than concentrated with the founder until the moment of transition ("crisis succession") [8]. If that structural distinction transfers to open source, the signal Avelino et al.'s snapshot misses should be visible one window earlier, in the trend of authority concentration during the months before departure rather than in any single measurement at departure.

This paper reimplements Avelino et al.'s DOA/Truck-Factor/TFDD pipeline end to end, adds a new pre-departure authority-diffusion measurement over the 6-12 months preceding each founder-only TFDD, and tests it under the same statistical machinery (matched-pairs comparison, BH-corrected regression, and a placebo permutation check) that the original snapshot covariates were shown to fail. Run against a corpus of 15 well-documented GitHub repositories, the reimplementation reproduces Avelino et al.'s central founder-only-detachment statistic almost exactly (87.5% of detachments occur at Truck Factor 1, against their reported 66%, with overlapping confidence intervals) and its independent hand-traced Degree-of-Authorship computations diverge from raw commit-count intuition in three of five spot checks, confirming DOA is doing genuinely different work than counting commits. A permutation test on the diffusion measurement itself shows the signal is temporally specific to the window immediately preceding departure rather than a property of generally active projects sampled at any point in their history (p = 0.016, two-sided, 60 permutations). At the same time, an automated calibration gate applied to the same corpus shows that the founder-only-TFDD sub-sample it produced — five events, all from currently thriving, famous tools, all of which survived — has zero outcome variance, which makes the central survival-prediction claim mathematically untestable on this corpus rather than confirmed or refuted. We report both results together, because the honest state of evidence is that the measurement machinery works and one specific piece of it (window-specificity) is validated, while the causal claim connecting diffusion to survival awaits a corpus large enough to contain a non-surviving founder-only TFDD event.

[FIGURE:fig1]

**Summary of Contributions**

- An open, validated reimplementation of Avelino et al.'s Degree-of-Authorship, Truck-Factor, and Truck-Factor-Detachment-Departure pipeline, calibrated against their three published headline statistics with explicit pass/flag status and 95% confidence intervals (Section 4).
- A new pre-departure authority-diffusion measurement — founder commit-share and count of distinct non-founder Degree-of-Authorship file-owners in the 6-12 months before a founder-only detachment — computed alongside Avelino et al.'s original at-detachment snapshot covariates under identical statistical procedures (Section 3).
- A permutation-test result showing this diffusion signal is specific to the pre-departure window rather than an artifact of generally-active projects (p = 0.016), directly answering the falsification check the hypothesis specifies (Section 5).
- A transparent calibration and robustness protocol — sampling-strata diagnostics, a hand-traced Degree-of-Authorship sanity check, founder-identification-heuristic sensitivity, and a numeric power threshold — that identifies exactly what a follow-up corpus needs to contain (at least one non-surviving founder-only TFDD event) before the central hypothesis can be tested (Section 6).

# Related Work

**Truck Factor and Degree of Authorship.** The Truck Factor — the minimal number of developers whose combined departure would incapacitate a project — was formalized computationally by Avelino et al., who estimate it via a greedy algorithm over per-file Degree-of-Authorship (DOA) scores rather than raw commit counts [2]. DOA itself originates with Fritz et al., who model developer expertise on a file as a function of file creation, subsequent edits by the developer relative to others, and (in the interactive variant) IDE interaction events [7]; Avelino et al. use the authorship-only variant, weighting first-authorship, subsequent-edit count, and edits by others with empirically fit coefficients. Ferreira et al. compare three Truck-Factor estimation algorithms, including Avelino et al.'s DOA-based approach, and find it the most defensible of the three on a manually-labeled sample [3]. This paper reuses the DOA/Truck-Factor computation from [1, 2] verbatim (same weights, same greedy set construction) rather than proposing a new expertise metric, so that any new result is attributable to the new pre-departure measurement rather than to a re-tuned authorship model.

**Abandonment and survival.** Avelino et al.'s ESEM 2019 study is the direct empirical basis and departure point for this paper [1]. Mining 1,932 popular GitHub repositories, they define the Truck-Factor Developer Detachment (TFDD) — the point at which every developer in a project's current Truck-Factor set has been silent for a validated one-year threshold — and a four-level Active/Inactive survival model (thriving, maintained, dormant, dead) scored 18 months after each TFDD. They report that 315 projects (16%) experience a TFDD, that 66% of TFDDs occur at Truck Factor 1 (a single core developer), that 128 of 315 (41%) survive, and — the result this paper builds on — that surviving and non-surviving projects are statistically indistinguishable in size at the TFDD snapshot itself (Cohen's d = 0.13-0.26). Their pipeline is not run at any point before the TFDD; the present paper's sole methodological departure is to run the identical DOA/Truck-Factor machinery one window earlier and treat the resulting trend, rather than the snapshot, as the candidate predictor.

**Why projects fail, self-reported.** Coelho and Valente survey maintainers of 104 curated failed GitHub projects (out of 618 identified failures among the top 5,000 starred repositories) and report nine failure reasons spanning team factors (lack of time, lack of interest, conflict), project factors (obsolescence, outdated technology, low maintainability), and environment factors (being usurped by a competitor, legal issues, acquisition) [4]. They also find failed projects adopt fewer maintenance-practice signals than surviving ones — contributing guidelines (16% vs. 72%) and continuous integration (27% vs. 68%) — which are plausible downstream correlates of the same authority-diffusion process this paper measures directly, though [4] does not measure diffusion or test a pre-departure trajectory; its unit of analysis is a single maintainer's retrospective account of why they personally stopped, not a multi-contributor measurement of whether authority already existed elsewhere.

**Dependency abandonment from the consumer's side.** Miller et al. interview and survey developers who depend on open-source packages about how they detect and cope with a dependency's abandonment [5]. Their focus is downstream — how consumers of a project navigate an abandonment they did not cause or predict — which is complementary to, and does not overlap with, this paper's producer-side question of whether a project's own pre-departure authority structure predicts whether it needs to be navigated around at all.

**Diffusion of write access and core-team loss.** Two recent studies bear directly on the mechanism this paper investigates. Medappa et al. analyze a matched sample of 5,762 GitHub projects and find that a higher proportion of contributors holding write access — a static, project-level analogue of the diffusion this paper measures dynamically and specifically before a founder's departure — increases novelty but *reduces* survival, attributing the effect to a division of labor in which non-write-access contributors, not the diffusely-empowered core, drive long-term reliability [9]. That finding is a genuine complication for the mechanism proposed here: it suggests diffusion of formal authority is not uniformly protective, and that this paper's positive framing (diffusion measured specifically in the run-up to a founder's exit, rather than as a static project-wide ratio) needs to hold up against a literature where the same underlying variable, measured differently, points the other way. Separately, Nourry et al. re-examine Avelino et al.'s TFDD construct at a larger scale (over 36,000 projects) and report that only 27% of abandoned projects attract a new Truck-Factor developer, arguing the "core-developer loss is critical" framing undersells how routine such losses are and how rarely they are reversed [11] — a caution this paper's own corpus-selection discussion (Section 6) independently arrives at from a different angle, since a corpus of currently-thriving repositories will systematically miss exactly the non-recoveries Nourry et al. show are the modal outcome. Jabrayilzade et al. survey 269 practicing engineers on how bus factor is understood and managed in industry, finding that practitioners' informal judgments of who is "hard to replace" often diverge from commit-based Truck-Factor estimates and are shaped by code-review and meeting participation the git history alone does not capture [10] — a reminder that this paper's DOA-based founder and authority-owner identification, like Avelino et al.'s, is a proxy for authority grounded in version-control activity, not a direct measurement of organizational knowledge.

**Mining-methodology controls.** Because this study, like [1], mines GitHub commit history to infer developer identity and project lifecycle, it inherits the methodological hazards Kalliamvakou et al. document under "the perils of mining GitHub" [6] — most relevantly, bulk-imported repository histories whose first commit touches an implausibly large fraction of files in an implausibly short window, which would masquerade as a single founder's massive first contribution. This paper applies the same >80%-of-files-in-the-first-week heuristic from [6] that Avelino et al. use to filter such artifacts before founder identification.

**Succession outside software.** The organizational-succession literature on founder-led firms outside software motivates, without formally testing in the same domain, the specific mechanism this paper investigates. Ahn's study of 64 matched pairs of surviving and delisted Korean founder-led firms finds that founder-succession characteristics — including how authority was transferred — are associated with long-term post-succession survival independent of firm size at the time of transition [8], structurally paralleling the "diffused vs. concentrated authority at the moment of exit" distinction this paper operationalizes for open-source commit and file-ownership authority. No existing work, to our knowledge, tests this pre-departure-trajectory hypothesis on open-source Truck-Factor data; that gap, and Avelino et al.'s own explicit snapshot-covariate null result, is what this paper is designed to close.

# Method

The pipeline reimplements Avelino et al.'s Degree-of-Authorship / Truck-Factor / TFDD machinery [1, 2] end to end, then extends it with a new pre-departure authority-diffusion measurement, four downstream statistical tests, and a two-stage calibration-and-robustness harness. All components run over the same per-repo commit history and emit both the original snapshot covariates and the new diffusion covariates side by side, so the two are compared under identical data and identical statistical procedures [ARTIFACT:art_I5KoOp16hub5].

**Alias resolution.** Each repository's commit authors are collapsed to individuals via normalized email and GitHub-login matching, following the alias-resolution step Avelino et al. describe; a per-repo alias-collapse-rate diagnostic is logged for later quality assurance.

**Degree of Authorship.** For each file and author, cumulative-window DOA is computed year by year using the Fritz et al. weights as reused by Avelino et al.: first-authorship weight FA = 3.293, per-subsequent-edit weight DL = 1.098, and per-edit-by-another-author weight AC = -1.017 [7, 1]. A developer is a file's primary owner in a given year when their DOA on that file is the highest among all contributors to it.

**Truck Factor and TFDD detection.** The yearly Truck-Factor set is the greedy minimal set of primary-DOA-owning developers whose combined removal would leave more than half of a project's files without a primary owner. A Truck-Factor-Detachment-Departure (TFDD) event is recorded the first time every developer in a project's current Truck-Factor set has made no commits for twelve consecutive months — the abandoner threshold Avelino et al. select empirically as the least error-sensitive of five candidates they test (harmonic-mean precision 0.66, versus 0.44-0.64 for the alternatives) [1]. Founder-only TFDDs are isolated as the subset where the departing Truck-Factor set has size one and its sole member is the repository's first human committer; first commits that touch more than 80% of a repository's files within the first week are treated as bulk imports rather than genuine founding activity and excluded, following the "perils of mining GitHub" heuristic [6].

**New measurement: pre-departure authority diffusion.** For each founder-only TFDD, the pipeline additionally computes, over the 6-12 months immediately preceding the detachment, (a) the founder's share of authored commits in that window and (b) the count of distinct non-founder accounts that had already reached primary DOA ownership on at least one file in that window; a composite diffusion score combines both. This trajectory measurement — as distinct from Avelino et al.'s at-TFDD snapshot covariates (developers, commits, and files at the moment of detachment, which the pipeline also computes for direct comparison) — is the paper's sole new construct, and is not present anywhere in [1] or [2].

**Survival outcome.** Post-TFDD survival is scored over an 18-month window using Avelino et al.'s four-level Active/Inactive grading (thriving / maintained / dormant / dead), collapsed to a binary survived flag for the matched-pairs and regression analyses, exactly as in [1].

**Statistical tests.** Four analyses are run, all on the founder-only-TFDD subset, with baseline (snapshot-only) and proposed (diffusion-augmented) predictors computed side by side: (1) a nearest-neighbor matched-pairs bootstrap comparing high- vs. low-diffusion projects, matched on standardized log-stars, log-forks, and log-contributor-count within language, with 10,000-resample 95% confidence intervals on the survival-rate lift; (2) Benjamini-Hochberg-corrected logistic and ordinal (statsmodels `OrderedModel`) regressions of survival on the diffusion predictors plus the original snapshot covariates, so that standardized effect sizes are directly comparable to Avelino et al.'s reported d = 0.13 (files) and d = 0.25-0.26 (developers, commits); (3) a placebo/window-shuffle check that redraws the "pre-departure" window from an arbitrary point elsewhere in each project's history and refits the diffusion measurement, comparing the true window's effect against the resulting null distribution via a two-sided permutation test; and (4) a snapshot-null Cohen's-d replication of Avelino et al.'s own negative result, as a sanity check that the reimplementation reproduces their reported effect-size range before trusting any new result built on the same pipeline.

**Calibration and robustness harness.** Because the pipeline is a reimplementation rather than a reuse of Avelino et al.'s original code or data, a two-stage evaluation is run before any diffusion result is interpreted [ARTIFACT:art_JvYoV94jgkuB]. Stage A recomputes Avelino et al.'s three headline aggregate statistics — TFDD incidence rate, share of TFDDs at Truck Factor 1, and overall 18-month survival rate — with 95% Wilson confidence intervals and a PASS / FLAG_DEVIATION status per statistic, automatically triggering a four-step diagnostic (sampling-strata composition, abandoner-threshold parameter check, a hand-traced DOA sanity check on individual repositories, and an alias-collapse-rate spot check) whenever any statistic is flagged. Stage B runs five additional robustness checks against the founder-only diffusion-vs-survival result specifically: window-boundary sensitivity across a near/far/end-offset grid; founder-identification-heuristic sensitivity (first-commit author vs. first-calendar-year plurality vs. highest-lifetime-DOA); an age-at-TFDD confound check with variance-inflation-factor diagnostics; matched-pairs bucket-definition sensitivity (quartile vs. log-scale star bins); and the permutation test described above, reported separately for eventual survivors and non-survivors where sample size allows.

# Experimental Setup

**Corpus.** The dataset consists of 15 well-known, actively-maintained GitHub repositories — including Textualize/rich, amoffat/sh, arrow-py/arrow, Kludex/starlette, jazzband/tablib, pallets/click, benoitc/gunicorn, cookiecutter/cookiecutter, and others spanning Python and one Shell repository, with star counts from 4,755 to 57,099 and commit histories from 6.6 to 16.4 years [ARTIFACT:art_ZuMis522AEPF]. Full commit history (SHA, author name and email, ISO timestamp, and per-file insertion/deletion counts for every commit) was obtained by cloning each repository and running `git log --numstat`, which is not rate-limited and is therefore complete and untruncated for every repository in the corpus up to a 5,000-commit-per-repository cap with an explicit truncation flag. Repository-level metadata (stars, forks, language, license, creation and last-push timestamps) came from the GitHub REST API, which in this environment had no authentication token and was consequently capped at 60 unauthenticated requests per hour — two calls per repository. This constraint, not a defect in the mining code, is what limited the corpus to 15 of the originally planned 150-250 repositories: git cloning itself scales without limit, so the pipeline's candidate list of roughly 104 repositories and its checkpointed, resumable state are already in place to extend the corpus given API credentials, without re-collecting any completed repository. A repository is labeled founder-dominant when a single committer's email accounts for at least 70% of commits in the repository's first year; this label is measured empirically from the cloned history rather than assumed.

**Founder-only TFDD sample.** Of 3,427 raw dataset records (3,409 of which belong to an unrelated HuggingFace commit-message corpus evaluated and rejected as a primary data source during dataset construction, and correctly filtered out by the pipeline's `no_commits` check), the pipeline identifies 6 founder-only TFDD events, collapsing to 5 distinct repositories after final quality-assurance de-duplication; the remainder of the corpus's detected TFDDs were excluded because the departing Truck-Factor set was not size-one (`not_founder_only_tfdd`, 4 events), no TFDD was detected in the observed history (`no_tfdd`, 6 repositories), or the post-TFDD survival window was right-censored by insufficient subsequent history (`right_censored`, 2 events).

**Baselines.** The comparison throughout is not against an external competing method but against Avelino et al.'s own published statistics [1] — their reported TFDD incidence rate (16.3%, 315/1,932), their reported founder-only (Truck-Factor-1) share of TFDDs (66%), their reported overall 18-month survival rate (40.6%, 128/315), and their reported snapshot-covariate effect-size range (Cohen's d = 0.13-0.26) — computed identically on this paper's 15-repository corpus, plus the same snapshot covariates recomputed on the founder-only subset as the direct within-study baseline the new diffusion predictors must beat.

# Results

## Pipeline calibration against Avelino et al.'s published statistics

Stage A recomputes Avelino et al.'s three headline statistics on the full 15-repository corpus (8 TFDD events of any Truck-Factor size). The founder-only-detachment share reproduces almost exactly: 87.5% of TFDDs occur at Truck Factor 1 (7 of 8, 95% CI [0.529, 0.978]) against Avelino et al.'s reported 66%, a PASS given the wide but overlapping interval. The abandoner-threshold parameter matches their validated choice of 12 months exactly. However, two of the three headline rates are flagged as deviations: the TFDD incidence rate is 53.3% (8/15, CI [0.301, 0.752]) against their reported 16.3% (315/1,932) — a 2.3x relative deviation — and the overall 18-month survival rate is 100% (8/8, CI [0.676, 1.0]) against their reported 40.6% (128/315) — a 1.5x relative deviation. The automatic diagnostic protocol these flags trigger identifies the same underlying cause for both: the corpus is a small, non-stratified sample of already-successful software (14 of 15 repositories are Python, one is Shell) rather than Avelino et al.'s stratified sample of the top 500 starred repositories across six languages, so both the incidence rate (long-lived, currently-thriving repositories are more likely to have already passed through a TFDD in their history) and the survival rate (currently-thriving repositories are, by construction of how they were selected for this corpus, disproportionately likely to have survived any TFDD they experienced) are biased upward by the same selection mechanism. The snapshot-null Cohen's-d replication (Avelino et al.'s reported d = 0.13-0.26) could not be computed at all on this corpus, because it requires both survivors and non-survivors and every one of the 8 TFDDs observed survived.

A separate hand-traced sanity check on five repositories compares each repository's top commit-count author against its top DOA-computed file owner directly; the two disagree in three of five cases (amoffat/sh, cookiecutter/cookiecutter, and arrow-py/arrow), confirming that the reimplemented DOA computation is capturing a genuinely different notion of ownership than raw commit volume, as intended, rather than silently degenerating into a commit-count proxy. The alias-resolution diagnostic found a median collapse rate of 0.0 across the corpus (no repository required merging developer identities), against Avelino et al.'s reported corpus-wide median of 11%, with zero repositories exceeding a 40% collapse rate.

[FIGURE:fig2]

## Founder-only pre-departure authority diffusion

The five founder-only TFDD events, with their pre-departure (6-12 months before detachment) founder commit-share, count of distinct non-founder DOA file-owners, composite diffusion score, and 18-month survival outcome, are: amoffat/sh (founder share 10.5%, 8 distinct owners, diffusion score 1.97, outcome *maintained*); arrow-py/arrow (3.1%, 4 owners, 1.56, *thriving*); Kludex/starlette (1.1%, 13 owners, 2.61, *thriving*); jazzband/tablib (2.2%, 7 owners, 2.03, *thriving*); and pallets/click (1.5%, 18 owners, 2.90, *thriving*). All five events show a founder commit-share well below the hypothesis's 50% threshold and at least two independent non-founder DOA-file-owners already established before departure, consistent with the diffused-authority profile the hypothesis predicts should survive — and all five did survive [ARTIFACT:art_I5KoOp16hub5].

[FIGURE:fig3]

That uniform outcome is also the sample's central limitation: with zero non-survivors among the five founder-only TFDD events, the matched-pairs comparison has no eligible pairs to construct (0 pairs), and both the logistic and ordinal regressions of survival on the diffusion predictors and snapshot covariates fail with `insufficient_n` at n = 5-6. Success criteria 1 (a >=1.5x survival-rate lift for high- vs. low-diffusion projects with a CI excluding 1x) and 2 (diffusion predictors remaining significant after controlling for age, with a standardized effect size exceeding Avelino et al.'s snapshot d = 0.13-0.26) are therefore not merely negative — they are unscored, because the statistical objects they require (variation in the outcome, and a fitted regression) do not exist on this corpus.

## Window-specificity of the diffusion signal

Success criterion 3 — that the true pre-departure window's effect exceeds a null distribution built from randomly relocating that window elsewhere in each project's history — is the one test in the plan that does not require outcome variance, since it evaluates the diffusion measurement's temporal specificity rather than its relationship to survival. Run with 60 permutations pooled across all five founder-only TFDD repositories, the true pre-departure window's mean diffusion effect is 2.214, against a null-permutation mean of 1.187 (SD 0.375) — a two-sided permutation p-value of 0.016. Restricting to the five survivors only (the only stratum with data; no non-survivor exists in this corpus, so the non-survivor-only variant is unavailable) with 40 permutations gives the same true effect of 2.214 against a permutation p-value of 0.024. Both results support the hypothesis's own falsification check: the measured rise in non-founder authority is concentrated specifically in the months immediately before the founder's detachment, not a property that would appear from any randomly chosen window in these projects' histories.

[FIGURE:fig4]

## Robustness checks

The remaining Stage B checks are consistent with a pipeline that is mechanically sound but numerically underpowered rather than one producing unstable or contradictory results. Window-boundary sensitivity across four near/far/end-offset variants of the 6-12-month definition could not be fit at n = 5 in any variant (all report `insufficient_n_for_fit`), so sign-stability across variants is undetermined rather than negative. Founder-identification-heuristic sensitivity compared three independent ways of naming the founder — first-commit author, first-calendar-year commit plurality, and highest lifetime DOA — and found zero disagreements across all five repositories (disagreement rate 0.0, against Avelino et al.'s reported median alias-ambiguity rate of 11%), indicating that on this corpus at least, "who is the founder" is not itself a source of measurement noise, even though the regressions built on that identification cannot yet be fit. The age-at-TFDD confound check is unavailable at n = 6. Matched-pairs bucket-definition sensitivity (quartile vs. log-scale star bins) finds zero usable buckets under either definition, again a direct consequence of the zero-variance outcome rather than an instability in the bucketing method itself.

# Discussion

The clearest positive result in this study is methodological rather than substantive: a reimplementation of a published, previously-validated pipeline reproduces that pipeline's own reported statistics closely enough to trust (founder-only-detachment share 87.5% vs. 66% reported, CI-overlapping; validated 12-month abandoner threshold matched exactly; DOA measurably diverging from commit-count intuition in the expected direction), and the new pre-departure authority-diffusion measurement this paper adds behaves exactly as its own falsification check demands — concentrated in the window immediately before departure (permutation p = 0.016), not smeared uniformly across project history. That combination is what makes the calibration and robustness protocol worth reporting in full rather than only reporting whichever numbers happened to come out significant: it demonstrates the instrument is measuring something real and temporally specific, which is a necessary condition for the causal claim, but it is not itself the causal claim.

The causal claim — that pre-departure diffusion predicts *survival* — is the one this study cannot yet speak to, and the reason is structural rather than statistical bad luck. The 15-repository corpus was assembled from well-known, currently-maintained tools reachable within a strict unauthenticated GitHub API budget of 60 requests per hour; that selection mechanism systematically favors software that is still alive today, which is exactly the population in which a founder-only TFDD is most likely to have been survived. The calibration gate makes this concrete rather than speculative: this corpus's TFDD incidence rate (53.3%) and 18-month survival rate (100%) both deviate sharply from Avelino et al.'s stratified reference rates (16.3% and 40.6% respectively), in the direction consistent with a survivorship-biased sample, while the one statistic insensitive to that bias — the founder-only share of TFDDs — matches closely. The result is a founder-only-TFDD sub-sample with literally zero outcome variance: five events, five survivors. No matched-pairs comparison, regression, or Cohen's-d snapshot-null replication is definable on a sample with a single outcome value, independent of how many repositories or predictors are added to it in this shape of corpus.

This distinguishes "underpowered" from "untestable." A larger draw from the same biased sampling frame — more famous, currently-thriving GitHub repositories — would not fix the problem, because it would still be biased toward the survived outcome; what is needed is specifically a corpus construction that does not condition on present-day liveness, of the kind Avelino et al.'s original stratified top-500-per-language design achieves by sampling popular repositories regardless of their current maintenance status and letting the TFDD/survival pipeline discover which ones failed after the fact. The pipeline built here already contains the mechanism to do this — a checkpointed, resumable collection process with an unused ~104-repository candidate list spanning seven languages — and is blocked only by the same unauthenticated rate limit that produced the 15-repository corpus; an authenticated GitHub API token raises that ceiling from 60 to 5,000 requests per hour, roughly an 83-fold increase, which is sufficient to reach the plan's original 150-250 repository target and, per the fallback power analysis specified when this study was planned, the roughly 40 founder-only TFDD events a well-powered matched-pairs test requires — about eight times the 5 events available here.

**Limitations.** Beyond the zero-variance sampling issue above, four further limitations bound how these results should be read. First, the corpus is linguistically narrow (14 of 15 repositories are Python), so nothing here speaks to whether authority-diffusion dynamics generalize across ecosystems with different contribution norms. Second, the DOA hand-trace disagreeing with raw commit-count intuition in three of five spot-checked repositories, while evidence the metric is doing real work, also means founder and authority-owner identification is sensitive to exactly which authorship signal is trusted; the founder-identification-heuristic check found perfect agreement across three heuristics on this specific five-repository sample, but that agreement was not itself tested under the corpus expansion this paper recommends. Third, the age-at-TFDD confound check specified in the original evaluation plan — verifying that any diffusion effect is not simply proxying for project age — could not run at all for lack of data, so it remains an open, not a closed, threat to validity for a future well-powered test. Fourth, the permutation test's own p-values (0.016 pooled, 0.024 survivors-only) are computed from only five repositories and 60 or 40 permutations respectively; they should be read as evidence the measurement construct behaves as designed on the data available, not as a precise estimate of an effect size that would replicate at scale.

# Conclusion

Founder departure is a recognized risk point for open-source projects, and Avelino et al. showed that the obvious predictor — project size and popularity at the moment of departure — carries essentially no signal about which projects survive it. This paper built and calibrated a pipeline capable of testing whether the real signal instead lives in the trajectory of authority concentration in the months before departure, reimplementing Avelino et al.'s Degree-of-Authorship and Truck-Factor machinery closely enough to reproduce their founder-only-detachment statistic (87.5% vs. their 66%) and adding a new pre-departure diffusion measurement that a permutation test confirms is temporally specific to the pre-departure window (p = 0.016) rather than a general property of active projects. What the pipeline could not do, on the 15-repository, 5-event corpus assembled under a strict unauthenticated API budget, is test the survival claim itself: every founder-only detachment observed happened to a project that ultimately survived, leaving zero outcome variance for any comparison to be built on. We report this as an honest intermediate result rather than either a confirmation or a refutation, release the full checkpointed, resumable pipeline and its unused ~104-repository candidate list, and specify the concrete next step precisely: an authenticated GitHub API token, an 83-fold increase in query budget, and roughly 40 founder-only TFDD events — about eight times what was available here — are what separate this pilot from a well-powered test of whether founders who let go early leave behind projects that live.

# References

[1] G. Avelino, E. Constantinou, M. T. Valente, and A. Serebrenik. On the abandonment and survival of open source projects: An empirical investigation. In *2019 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*, pages 1-12, 2019.

[2] G. Avelino, L. Passos, A. C. Hora, and M. T. Valente. A novel approach for estimating Truck Factors. In *2016 IEEE 24th International Conference on Program Comprehension (ICPC)*, pages 1-10, 2016.

[3] M. M. Ferreira, M. T. Valente, and K. Ferreira. A comparison of three algorithms for computing truck factors. In *2017 IEEE/ACM 25th International Conference on Program Comprehension (ICPC)*, pages 207-217, 2017.

[4] J. Coelho and M. T. Valente. Why modern open source projects fail. In *Proceedings of the 2017 11th Joint Meeting on Foundations of Software Engineering (ESEC/FSE)*, 2017.

[5] C. Miller, C. Kästner, and B. Vasilescu. "We Feel Like We're Winging It:" A Study on Navigating Open-Source Dependency Abandonment. In *Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE)*, 2023.

[6] E. Kalliamvakou, G. Gousios, K. Blincoe, L. Singer, D. M. German, and D. E. Damian. The promises and perils of mining GitHub. In *Proceedings of the 11th Working Conference on Mining Software Repositories (MSR)*, pages 92-101, 2014.

[7] T. Fritz, J. Ou, G. C. Murphy, and E. Murphy-Hill. A degree-of-knowledge model to capture source code familiarity. In *2010 ACM/IEEE 32nd International Conference on Software Engineering*, volume 1, pages 385-394, 2010.

[8] S.-Y. Ahn. Founder Succession, The Imprint of Founders' Legacies, and Long-Term Corporate Survival. *Sustainability*, 10(5):1485, 2018.

[9] P. K. Medappa, S. Srivastava, and S. D. Favaron. Write access provisioning and organizational ownership in open source software projects: Exploring the impact on project novelty and survival. *Research Policy*, 54(8), 2025.

[10] O. Nourry, M. Kondo, S. Saito, Y. Iimura, N. Ubayashi, and Y. Kamei. Myth: The loss of core developers is a critical issue for OSS communities. *arXiv preprint arXiv:2412.00313*, 2024.

[11] E. Jabrayilzade, M. Evtikhiev, E. Tüzün, and V. Kovalenko. Bus Factor in Practice. In *2022 IEEE/ACM 44th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP)*, pages 97-106, 2022.

</current_paper>

<reviewer_feedback>
Paper reviewer feedback from the previous iteration. Your strategy MUST address these critiques.
Prioritize major issues — these are the most impactful improvements to make.

- [MAJOR] (evidence) The paper's central hypothesis — that pre-departure authority diffusion predicts founder-detachment survival — is untestable on this corpus: all 5 founder-only TFDD events survived, so there is no outcome variance for the matched-pairs comparison, logistic/ordinal regression, or Cohen's-d replication. The paper says this is an 'honest intermediate result,' but a paper whose title question ('what determines whether an open-source project survives its founder stepping away') is not addressed by any testable evidence is a fundamentally incomplete piece of work for a research venue, regardless of how transparently the gap is reported.
  Action: Either (a) reframe the paper explicitly as a tools/methodology contribution (pipeline + calibration harness + power analysis for a follow-up study) rather than an empirical answer to the survival question, with the title and abstract changed accordingly, or (b) expand the corpus using the already-built but unused ~104-repository candidate list and an authenticated GitHub token (stated in the paper to be the only blocker) to obtain at least one non-surviving founder-only TFDD event before resubmission.
- [MAJOR] (methodology) The permutation test (p=0.016, 60 permutations, n=5 repos) is presented as the paper's one positive quantitative result, but with only 5 repositories and all 5 in the same survival class, it is unclear what population this generalizes to, and 60 permutations over 5 units gives coarse-grained achievable p-value resolution. The paper does not report how many distinct relocatable windows exist per repository, whether the 60 permutations are i.i.d. draws or an exhaustive enumeration, or a sensitivity analysis to permutation count.
  Action: Report the exact permutation scheme (window-relocation procedure, number of feasible distinct windows per repo, whether sampling was with or without replacement) and the theoretical minimum p-value achievable given this scheme and n. Re-run with a larger permutation budget if feasible and report convergence. State explicitly what population/generalization claim (if any) a within-corpus permutation test on 5 non-independent, hand-selected repositories can support.
- [MAJOR] (methodology) Two of the three Avelino et al. calibration statistics are flagged as deviating (TFDD incidence rate 53.3% vs. reported 16.3%, an ~3.3x absolute / 2.3x relative deviation; survival rate 100% vs. 40.6%, a large deviation), and the paper's own diagnostic attributes both to severe survivorship bias in the 15-repository convenience sample of already-famous, currently-thriving tools. This means the corpus is not merely underpowered but systematically biased in a way that would bias any hypothetical result toward finding 'diffusion predicts survival' even if a non-surviving case existed, because the sample was constructed by starting from tools that are known today to still be maintained.
  Action: Make explicit early in the paper (not only in Discussion) that the sampling frame itself is not a valid basis for causal inference about survival, independent of sample size — this should be stated as a design flaw, not just a power problem, since a bigger sample from the same 'famous tools that still exist' sampling frame would still be biased toward survivors. Describe concretely how the planned 150-250 repository expansion would avoid conditioning on present-day liveness (e.g., sampling from a fixed historical snapshot of GitHub repositories circa a chosen year, not from currently-popular-repository lists).
- [MINOR] (novelty) The organizational-succession analogy (Ahn 2018, planned vs. crisis succession in Korean firms) is the theoretical backbone motivating the new construct, but the paper does not discuss any other OSS-specific literature on bus-factor mitigation strategies, mentorship pipelines, or maintainer onboarding that might offer a more directly applicable theoretical grounding (e.g., work on OSS 'core team' formation, newcomer onboarding, or CHAOSS metrics for contributor diversity/retention).
  Action: Search CHAOSS/community-health metrics literature and OSS mentorship/onboarding studies (e.g., work on Apache podling graduation criteria, or studies of contributor pipeline/retention in mature OSS foundations) and add 1-2 sentences situating the diffusion construct relative to these more domain-native frameworks, not only the cross-domain firm-succession analogy.
- [MINOR] (clarity) The paper reports '87.5% of TFDDs occur at Truck Factor 1 (7 of 8...) against Avelino et al.'s reported 66%' as a PASS with 'overlapping confidence intervals,' but only one confidence interval (the paper's own, [0.529, 0.978]) is given — Avelino et al.'s reported 66% has no CI reported here for comparison, so 'overlapping' cannot be verified by the reader from the text alone.
  Action: Either compute or cite Avelino et al.'s CI for the 66% figure (derivable from their n=315*0.66 with a Wilson interval) and report both intervals side by side, or soften the PASS language to note the comparison CI was not available from the original paper.
- [MINOR] (scope) The corpus description in the main text ('15 well-documented GitHub repositories... including Textualize/rich, amoffat/sh, arrow-py/arrow, Kludex/starlette...') differs somewhat from the artifact's example list ('pallets/flask, BurntSushi/ripgrep, psf/black... Rust'), and the artifact mentions a Rust repository while the paper text says '14 of 15... Python, one Shell.' This is a minor inconsistency but could confuse a reader trying to reproduce the exact corpus composition from the paper alone.
  Action: Include the full, exact list of 15 repository names and their language/star/history-year values in a table (main text or appendix) rather than an illustrative partial list, and ensure it matches the artifact's actual dataset output exactly.
- [MINOR] (rigor) The paper states the alias-collapse-rate diagnostic found a median of 0.0 across the corpus (no repository required merging identities) versus Avelino et al.'s reported 11% median — this is presented as a neutral diagnostic result but could equally indicate the alias-resolution logic under-merges identities on this corpus (e.g., due to differences in how GitHub-login vs. email matching behaves on modern repos), which would silently misclassify some developers as distinct when they are the same person, potentially inflating the count of 'distinct non-founder DOA file-owners' used in the diffusion score.
  Action: Manually spot-check 2-3 repositories' contributor lists against their actual GitHub contributor pages to confirm the 0.0 median collapse rate is genuine and not a false negative of the alias-matching heuristic; report this as an explicit robustness check alongside the existing founder-identification-heuristic sensitivity analysis.
- [MINOR] (evidence) The abstract-level framing (in the summary of contributions and conclusion) leads with the permutation p=0.016 result as if it were meaningful support for the diffusion-survival mechanism, but the paper's own Results section correctly notes this test 'does not require outcome variance' and only shows temporal specificity of the measurement — it says nothing about whether the measurement predicts survival. A reader skimming only the abstract/contributions/conclusion could easily walk away believing the paper found supportive evidence for the causal claim.
  Action: Add one explicit sentence in the abstract and conclusion clarifying that the permutation result validates the measurement instrument's construct validity only, and explicitly does NOT provide evidence — positive or negative — about whether diffusion predicts survival, to prevent this being read as partial confirmation of the paper's title-level claim.
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

### [3] HUMAN-USER prompt · 2026-08-20 20:06:48 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [4] TOOL CALL — Bash · 2026-08-20 20:06:58 UTC

```
mkdir -p "$(dirname ./.terminal_claude_agent_struct_out.json)" 2>/dev/null; pwd
```

### [5] TOOL RESULT — Bash · 2026-08-20 20:07:00 UTC

```
{"stdout": "/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_strat/gen_strat_1", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [6] TOOL CALL — Write · 2026-08-20 20:07:46 UTC

```
File: /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json

{
  "strategies": [
    {
      "title": "Reframe as Calibrated Methodology, Fix Sampling Frame",
      "objective": "Convert the paper from an under-evidenced survival-prediction claim into a rigorously validated methodology-and-instrument contribution: (1) attempt a genuine historical, liveness-non-conditioned corpus expansion that could finally produce a non-surviving founder-only TFDD event and test the sampling-frame fix the current draft only proposes; (2) tighten the permutation-test methodology and calibration reporting so every MAJOR/MINOR reviewer critique about statistical rigor is closed with exact numbers rather than narrative; (3) ground the diffusion construct in OSS-native community-health literature (CHAOSS, podling graduation, onboarding) rather than only the cross-domain firm-succession analogy.",
      "rationale": "This is the final iteration, so the highest-value move is not broadening the existing pipeline but closing the exact gaps the reviewer named as blocking publication. The reviewer explicitly offered two acceptable paths: (a) reframe as tools/methodology, or (b) get a non-surviving event via the already-built ~104-candidate pipeline and a token-authenticated API. We pursue both simultaneously but budget for (a) as the guaranteed outcome: a DATASET artifact makes one real, time-boxed attempt at the historical-snapshot corpus expansion (using the existing checkpointed pipeline, and if a GITHUB_TOKEN is unavailable in this environment, falling back to GH Archive / gharchive.org historical event dumps and Libraries.io / World of Code snapshots that do not require live-repo listing APIs and are NOT conditioned on present-day liveness), reporting honestly whichever repos and outcome variance it obtains. An EVALUATION artifact fixes every methodology-rigor complaint on the EXISTING 15-repo result regardless of whether the dataset expansion succeeds: exact permutation-scheme reporting (feasible distinct windows per repo, sampling with/without replacement, achievable p-value resolution, convergence at a larger permutation budget), Avelino et al.'s own Wilson CI for the 66% TF=1 statistic computed from their reported n, a manual alias-resolution spot-check against real GitHub contributor pages, and a full exact repository table. A RESEARCH artifact grounds the construct in OSS-native literature (CHAOSS, Apache podling graduation, onboarding/retention pipelines) that the reviewer named as missing, and also researches concrete non-conditioned historical-snapshot corpus sources (GH Archive, World of Code, GHTorrent legacy dumps) to give the dataset artifact a validated source list before it starts pulling data. Together these three artifacts either (i) produce the first non-surviving founder-only TFDD event and a genuinely testable causal result, or (ii), failing that, leave the paper with an unambiguous, fully rigorous methodology contribution and zero remaining reviewer-named gaps in statistical reporting, novelty grounding, or reproducibility.",
      "artifact_directions": [
        {
          "type": "research",
          "objective": "Find (a) OSS-native community-health/onboarding literature to ground the pre-departure authority-diffusion construct alongside the existing firm-succession analogy, and (b) concrete, currently-accessible data sources for a historical, present-day-liveness-non-conditioned GitHub repository snapshot that the dataset artifact can pull from without depending on an authenticated GitHub REST token.",
          "approach": "Search for and read CHAOSS project metrics documentation (contributor absorption rate, elephant factor, bus factor working group outputs), Apache Software Foundation Incubator podling graduation criteria (which explicitly assess whether authority has diffused beyond a founder before graduation), and empirical studies of OSS newcomer onboarding / core-team formation and retention (e.g. work on onboarding barriers, mentorship programs, contributor pipeline studies). Synthesize 1-2 concrete sentences positioning the diffusion construct against these OSS-native frameworks specifically (not just the Korean-firm analogy). Separately, investigate and report concretely how to build a historical-snapshot GitHub corpus that does not condition on present-day liveness: GH Archive (gharchive.org, public BigQuery/hourly JSON dumps of all public GitHub events since 2011, queryable without an API key via direct file download), World of Code (public research dataset of GitHub commit/author graphs), and any Libraries.io or GHTorrent legacy static dumps. For each candidate source, report exactly what fields are available (commit-level author/timestamp/file data vs. only event metadata), how to download it without a GitHub API token, size/format, and whether it supports reconstructing full per-file commit history (required for DOA) or only repo-level metadata. Recommend the single most viable concrete pull-path (specific URL patterns / query approach) for the dataset artifact to attempt.",
          "depends_on": []
        },
        {
          "type": "dataset",
          "objective": "Attempt to build a founder-departure commit corpus sampled from a historical snapshot that does NOT condition on present-day liveness, using the research artifact's recommended source and the existing ~104-repo candidate pipeline/checkpoint as a starting point, in order to give the experiment/evaluation a chance at a non-surviving founder-only TFDD event and a genuinely non-survivorship-biased corpus.",
          "approach": "First check whether a GITHUB_TOKEN or equivalent authenticated credential is available in this environment; if so, resume the existing checkpointed 104-repo candidate pipeline (art_ZuMis522AEPF's code/build_dataset.py, code/candidates.py, temp/checkpoint.json) using it to raise the rate limit and pull full commit histories for as many additional candidates as the time budget allows, explicitly including repositories that are NOT currently famous/thriving (e.g. sampled from older, less-starred, or now-quiet repos in the candidate list) to avoid re-introducing the same survivorship bias. If no token is available, pull instead from GH Archive or another non-authenticated historical source identified by the research artifact: construct a sample of repositories that existed and were active in a fixed past window (e.g. repos with commit activity in a chosen year several years ago), explicitly NOT filtered by whether they are still maintained today, then `git clone` + `git log --numstat` each (unrated-limited) to get full commit history exactly as the existing dataset does. Standardize output to the same exp_sel_data_out schema as art_ZuMis522AEPF (repo_metadata, founder_signal, commits[]) so it is a drop-in-compatible superset/companion corpus, and explicitly report per-repo whether each was sampled by a liveness-conditioned or liveness-non-conditioned procedure via a new sampling_frame metadata field, so downstream analysis can compare or pool them honestly rather than silently mixing biased and unbiased samples.",
          "depends_on": [
            {"id": "art_ZuMis522AEPF", "label": "extends"}
          ]
        },
        {
          "type": "evaluation",
          "objective": "Close every reviewer-named methodology-rigor and reporting gap on the existing 15-repo pipeline result: exact permutation-scheme disclosure with convergence at higher budget, Avelino et al.'s own confidence interval for the 66% TF=1 statistic, a manual alias-resolution spot-check against live GitHub contributor pages, a full exact repository table, and (if the new dataset artifact produced additional or non-survivor data) a re-run of the calibration gate and permutation test on the combined/expanded corpus with an explicit comparison of biased vs. non-conditioned sampling frames.",
          "approach": "Extend eval.py's methodology: (1) report the exact permutation scheme used in the prior evaluation artifact — number of feasible distinct relocatable windows per repository given each project's history length, whether the 60/40 permutations were i.i.d. samples with or without replacement, the theoretical minimum achievable two-sided p-value given n and the permutation count, and re-run the permutation test at a substantially larger budget (e.g. 2000+ permutations per stratum, using the existing capped/cached DOA-recomputation fix) to report p-value convergence/stability versus the original 60/40-permutation result; (2) compute a Wilson 95% CI for Avelino et al.'s reported 66% TF=1 statistic from their stated n=315 TFDDs, and report it side-by-side with this paper's own CI rather than asserting 'overlapping' without the comparison interval; (3) manually spot-check the alias-resolution diagnostic's 0.0-median-collapse-rate finding against the actual GitHub contributor pages (via aii-web-tools fetch) for 2-3 corpus repositories, reporting whether any distinct-looking commit identities are actually the same contributor under a different email/handle, to test whether the diffusion score's 'distinct non-founder owner' counts are inflated by under-merging; (4) emit a full, exact table of all 15 (or more, if the dataset artifact's expansion completed) repositories with name, language, stars, commit-history years, and TFDD/survival status, matching the dataset artifact's actual output exactly, for inclusion as a paper table/appendix; (5) if the dataset artifact produced a non-conditioned or larger corpus, re-run Stage A calibration and the founder-only-TFDD extraction + permutation test on it and report explicitly whether TFDD incidence/survival rates move toward Avelino et al.'s reference values and whether outcome variance (a non-survivor) now exists, comparing this against the original 15-repo biased-frame results side by side as direct empirical evidence for the design-flaw-not-power-problem claim.",
          "depends_on": [
            {"id": "art_ZuMis522AEPF", "label": "dataset"},
            {"id": "art_I5KoOp16hub5", "label": "experiment"},
            {"id": "art_JvYoV94jgkuB", "label": "extends"}
          ]
        }
      ],
      "expected_outcome": "A methodologically airtight paper regardless of whether the corpus-expansion attempt succeeds: either (i) a non-conditioned historical corpus that yields at least one non-surviving founder-only TFDD event, turning the central hypothesis test from untestable into a real (even if still small-n) empirical result, directly resolving MAJOR#1 via option (b) and demonstrating MAJOR#3's proposed fix empirically rather than only prescriptively; or (ii), if the expansion cannot obtain such an event within budget, a paper explicitly and fully reframed as a validated methodology/instrument contribution (MAJOR#1 option (a)) with the sampling-frame defect stated as a design flaw up front rather than only in Discussion (MAJOR#3), an exact and convergence-tested permutation-scheme report (MAJOR#2), Avelino et al.'s own CI for the 66% comparison (MINOR), a manual alias spot-check (MINOR), an OSS-native theoretical grounding for the diffusion construct alongside the firm-succession analogy (MINOR), and a full exact repository table (MINOR) — closing every item in the reviewer feedback either way."
    }
  ]
}
```

### [7] TOOL RESULT — Write · 2026-08-20 20:07:46 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"strategies\": [\n    {\n      \"title\": \"Reframe as Calibrated Methodology, Fix Sampling Frame\",\n      \"objective\": \"Convert the paper from an under-evidenced survival-prediction claim into a rigorously validated methodology-and-instrument contribution: (1) attempt a genuine historical, liveness-non-conditioned corpus expansion that could finally produce a non-surviving founder-only TFDD event and test the sampling-frame fix the current draft only proposes; (2) tighten the permutation-test methodology and calibration reporting so every MAJOR/MINOR reviewer critique about statistical rigor is closed with exact numbers rather than narrative; (3) ground the diffusion construct in OSS-native community-health literature (CHAOSS, podling graduation, onboarding) rather than only the cross-domain firm-succession analogy.\",\n      \"rationale\": \"This is the final iteration, so the highest-value move is not broadening the existing pipeline but closing the exact gaps the reviewer named as blocking publication. The reviewer explicitly offered two acceptable paths: (a) reframe as tools/methodology, or (b) get a non-surviving event via the already-built ~104-candidate pipeline and a token-authenticated API. We pursue both simultaneously but budget for (a) as the guaranteed outcome: a DATASET artifact makes one real, time-boxed attempt at the historical-snapshot corpus expansion (using the existing checkpointed pipeline, and if a GITHUB_TOKEN is unavailable in this environment, falling back to GH Archive / gharchive.org historical event dumps and Libraries.io / World of Code snapshots that do not require live-repo listing APIs and are NOT conditioned on present-day liveness), reporting honestly whichever repos and outcome variance it obtains. An EVALUATION artifact fixes every methodology-rigor complaint on the EXISTING 15-repo result regardless of whether the dataset expansion succeeds: exact permutation-scheme reporting (feasible distinct windows per repo, sampling with/without replacement, achievable p-value resolution, convergence at a larger permutation budget), Avelino et al.'s own Wilson CI for the 66% TF=1 statistic computed from their reported n, a manual alias-resolution spot-check against real GitHub contributor pages, and a full exact repository table. A RESEARCH artifact grounds the construct in OSS-native literature (CHAOSS, Apache podling graduation, onboarding/retention pipelines) that the reviewer named as missing, and also researches concrete non-conditioned historical-snapshot corpus sources (GH Archive, World of Code, GHTorrent legacy dumps) to give the dataset artifact a validated source list before it starts pulling data. Together these three artifacts either (i) produce the first non-surviving founder-only TFDD event and a genuinely testable causal result, or (ii), failing that, leave the paper with an unambiguous, fully rigorous methodology contribution and zero remaining reviewer-named gaps in statistical reporting, novelty grounding, or reproducibility.\",\n      \"artifact_directions\": [\n        {\n          \"type\": \"research\",\n          \"objective\": \"Find (a) OSS-native community-health/onboarding literature to ground the pre-departure authority-diffusion construct alongside the existing firm-succession analogy, and (b) concrete, currently-accessible data sources for a historical, present-day-liveness-non-conditioned GitHub repository snapshot that the dataset artifact can pull from without depending on an authenticated GitHub REST token.\",\n          \"approach\": \"Search for and read CHAOSS project metrics documentation (contributor absorption rate, elephant factor, bus factor working group outputs), Apache Software Foundation Incubator podling graduation criteria (which explicitly assess whether authority has diffused beyond a founder before graduation), and empirical studies of OSS newcomer onboarding / core-team formation and retention (e.g. work on onboarding barriers, mentorship programs, contributor pipeline studies). Synthesize 1-2 concrete sentences positioning the diffusion construct against these OSS-native frameworks specifically (not just the Korean-firm analogy). Separately, investigate and report concretely how to build a historical-snapshot GitHub corpus that does not condition on present-day liveness: GH Archive (gharchive.org, public BigQuery/hourly JSON dumps of all public GitHub events since 2011, queryable without an API key via direct file download), World of Code (public research dataset of GitHub commit/author graphs), and any Libraries.io or GHTorrent legacy static dumps. For each candidate source, report exactly what fields are available (commit-level author/timestamp/file data vs. only event metadata), how to download it without a GitHub API token, size/format, and whether it supports reconstructing full per-file commit history (required for DOA) or only repo-level metadata. Recommend the single most viable concrete pull-path (specific URL patterns / query approach) for the dataset artifact to attempt.\",\n          \"depends_on\": []\n        },\n        {\n          \"type\": \"dataset\",\n          \"objective\": \"Attempt to build a founder-departure commit corpus sampled from a historical snapshot that does NOT condition on present-day liveness, using the research artifact's recommended source and the existing ~104-repo candidate pipeline/checkpoint as a starting point, in order to give the experiment/evaluation a chance at a non-surviving founder-only TFDD event and a genuinely non-survivorship-biased corpus.\",\n          \"approach\": \"First check whether a GITHUB_TOKEN or equivalent authenticated credential is available in this environment; if so, resume the existing checkpointed 104-repo candidate pipeline (art_ZuMis522AEPF's code/build_dataset.py, code/candidates.py, temp/checkpoint.json) using it to raise the rate limit and pull full commit histories for as many additional candidates as the time budget allows, explicitly including repositories that are NOT currently famous/thriving (e.g. sampled from older, less-starred, or now-quiet repos in the candidate list) to avoid re-introducing the same survivorship bias. If no token is available, pull instead from GH Archive or another non-authenticated historical source identified by the research artifact: construct a sample of repositories that existed and were active in a fixed past window (e.g. repos with commit activity in a chosen year several years ago), explicitly NOT filtered by whether they are still maintained today, then `git clone` + `git log --numstat` each (unrated-limited) to get full commit history exactly as the existing dataset does. Standardize output to the same exp_sel_data_out schema as art_ZuMis522AEPF (repo_metadata, founder_signal, commits[]) so it is a drop-in-compatible superset/companion corpus, and explicitly report per-repo whether each was sampled by a liveness-conditioned or liveness-non-conditioned procedure via a new sampling_frame metadata field, so downstream analysis can compare or pool them honestly rather than silently mixing biased and unbiased samples.\",\n          \"depends_on\": [\n            {\"id\": \"art_ZuMis522AEPF\", \"label\": \"extends\"}\n          ]\n        },\n        {\n          \"type\": \"evaluation\",\n          \"objective\": \"Close every reviewer-named methodology-rigor and reporting gap on the existing 15-repo pipeline result: exact permutation-scheme disclosure with convergence at higher budget, Avelino et al.'s own confidence interval for the 66% TF=1 statistic, a manual alias-resolution spot-check against live GitHub contributor pages, a full exact repository table, and (if the new dataset artifact produced additional or non-survivor data) a re-run of the calibration gate and permutation test on the combined/expanded corpus with an explicit comparison of biased vs. non-conditioned sampling frames.\",\n          \"approach\": \"Extend eval.py's methodology: (1) report the exact permutation scheme used in the prior evaluation artifact — number of feasible distinct relocatable windows per repository given each project's history length, whether the 60/40 permutations were i.i.d. samples with or without replacement, the theoretical minimum achievable two-sided p-value given n and the permutation count, and re-run the permutation test at a substantially larger budget (e.g. 2000+ permutations per stratum, using the existing capped/cached DOA-recomputation fix) to report p-value convergence/stability versus the original 60/40-permutation result; (2) compute a Wilson 95% CI for Avelino et al.'s reported 66% TF=1 statistic from their stated n=315 TFDDs, and report it side-by-side with this paper's own CI rather than asserting 'overlapping' without the comparison interval; (3) manually spot-check the alias-resolution diagnostic's 0.0-median-collapse-rate finding against the actual GitHub contributor pages (via aii-web-tools fetch) for 2-3 corpus repositories, reporting whether any distinct-looking commit identities are actually the same contributor under a different email/handle, to test whether the diffusion score's 'distinct non-founder owner' counts are inflated by under-merging; (4) emit a full, exact table of all 15 (or more, if the dataset artifact's expansion completed) repositories with name, language, stars, commit-history years, and TFDD/survival status, matching the dataset artifact's actual output exactly, for inclusion as a paper table/appendix; (5) if the dataset artifact produced a non-conditioned or larger corpus, re-run Stage A calibration and the founder-only-TFDD extraction + permutation test on it and report explicitly whether TFDD incidence/survival rates move toward Avelino et al.'s reference values and whether outcome variance (a non-survivor) now exists, comparing this against the original 15-repo biased-frame results side by side as direct empirical evidence for the design-flaw-not-power-problem claim.\",\n          \"depends_on\": [\n            {\"id\": \"art_ZuMis522AEPF\", \"label\": \"dataset\"},\n            {\"id\": \"art_I5KoOp16hub5\", \"label\": \"experiment\"},\n            {\"id\": \"art_JvYoV94jgkuB\", \"label\": \"extends\"}\n          ]\n        }\n      ],\n      \"expected_outcome\": \"A methodologically airtight paper regardless of whether the corpus-expansion attempt succeeds: either (i) a non-conditioned historical corpus that yields at least one non-surviving founder-only TFDD event, turning the central hypothesis test from untestable into a real (even if still small-n) empirical result, directly resolving MAJOR#1 via option (b) and demonstrating MAJOR#3's proposed fix empirically rather than only prescriptively; or (ii), if the expansion cannot obtain such an event within budget, a paper explicitly and fully reframed as a validated methodology/instrument contribution (MAJOR#1 option (a)) with the sampling-frame defect stated as a design flaw up front rather than only in Discussion (MAJOR#3), an exact and convergence-tested permutation-scheme report (MAJOR#2), Avelino et al.'s own CI for the 66% comparison (MINOR), a manual alias spot-check (MINOR), an OSS-native theoretical grounding for the diffusion construct alongside the firm-succession analogy (MINOR), and a full exact repository table (MINOR) — closing every item in the reviewer feedback either way.\"\n    }\n  ]\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [8] ASSISTANT · 2026-08-20 20:07:48 UTC

```
Strategy written to `.terminal_claude_agent_struct_out.json`: one strategy with 3 artifacts (research on OSS-native onboarding literature + non-conditioned historical data sources, dataset attempting a liveness-non-conditioned corpus expansion, evaluation closing all reviewer-named rigor gaps) that resolves the reviewer's MAJOR/MINOR feedback either via a genuine non-survivor event or a fully airtight methodology reframing.
```

### [9] SYSTEM-USER prompt · 2026-08-20 20:07:50 UTC

```
<verification_results>
Your previous response had issues that need fixing:

DEPENDENCY ERRORS (depends_on can ONLY reference IDs from <existing_artifacts>):
  - Strategy 1: Artifact 'dataset_iter2_dir2' (dataset): dependency 'art_ZuMis522AEPF' has type 'dataset' which is not allowed (allowed: {'research'})
  - Strategy 1: Artifact 'evaluation_iter2_dir3' (evaluation): dependency 'art_JvYoV94jgkuB' has type 'evaluation' which is not allowed (allowed: {'dataset', 'experiment'})

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

### [10] TOOL CALL — Edit · 2026-08-20 20:08:00 UTC

```
File: /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json
OLD:           "approach": "First check whether a GITHUB_TOKEN or equivalent authenticated credential is available in this environment; if so, resume the existing checkpointed 104-repo candidate pipeline (art_ZuMis522AEPF's code/build_dataset.py, code/candidates.py, temp/checkpoint.json) using it to raise the rate limit and pull full commit histories for as many additional candidates as the time budget allows, explicitly including repositories that are NOT currently famous/thriving (e.g. sampled from older, less-starred, or now-quiet repos in the candidate list) to avoid re-introducing the same survivorship bias. If no token is available, pull instead from GH Archive or another non-authenticated historical source identified by the research artifact: construct a sample of repositories that existed and were active in a fixed past window (e.g. repos with commit activity in a chosen year several years ago), explicitly NOT filtered by whether they are still maintained today, then `git clone` + `git log --numstat` each (unrated-limited) to get full commit history exactly as the existing dataset does. Standardize output to the same exp_sel_data_out schema as art_ZuMis522AEPF (repo_metadata, founder_signal, commits[]) so it is a drop-in-compatible superset/companion corpus, and explicitly report per-repo whether each was sampled by a liveness-conditioned or liveness-non-conditioned procedure via a new sampling_frame metadata field, so downstream analysis can compare or pool them honestly rather than silently mixing biased and unbiased samples.",
          "depends_on": [
            {"id": "art_ZuMis522AEPF", "label": "extends"}
          ]
NEW:           "approach": "First check whether a GITHUB_TOKEN or equivalent authenticated credential is available in this environment; if so, resume the existing checkpointed 104-repo candidate pipeline (the prior dataset artifact's code/build_dataset.py, code/candidates.py, temp/checkpoint.json, reused by re-reading that workspace's code) using it to raise the rate limit and pull full commit histories for as many additional candidates as the time budget allows, explicitly including repositories that are NOT currently famous/thriving (e.g. sampled from older, less-starred, or now-quiet repos in the candidate list) to avoid re-introducing the same survivorship bias. If no token is available, pull instead from GH Archive or another non-authenticated historical source identified by the research artifact: construct a sample of repositories that existed and were active in a fixed past window (e.g. repos with commit activity in a chosen year several years ago), explicitly NOT filtered by whether they are still maintained today, then `git clone` + `git log --numstat` each (unrated-limited) to get full commit history exactly as the existing dataset does. Standardize output to the same exp_sel_data_out schema as the existing dataset artifact (repo_metadata, founder_signal, commits[]) so it is a drop-in-compatible superset/companion corpus, and explicitly report per-repo whether each was sampled by a liveness-conditioned or liveness-non-conditioned procedure via a new sampling_frame metadata field, so downstream analysis can compare or pool them honestly rather than silently mixing biased and unbiased samples.",
          "depends_on": [
            {"id": "art_5rKf3placeholder", "label": "placeholder"}
          ]
```

### [11] TOOL RESULT — Edit · 2026-08-20 20:08:00 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "oldString": "          \"approach\": \"First check whether a GITHUB_TOKEN or equivalent authenticated credential is available in this environment; if so, resume the existing checkpointed 104-repo candidate pipeline (art_ZuMis522AEPF's code/build_dataset.py, code/candidates.py, temp/checkpoint.json) using it to raise the rate limit and pull full commit histories for as many additional candidates as the time budget allows, explicitly including repositories that are NOT currently famous/thriving (e.g. sampled from older, less-starred, or now-quiet repos in the candidate list) to avoid re-introducing the same survivorship bias. If no token is available, pull instead from GH Archive or another non-authenticated historical source identified by the research artifact: construct a sample of repositories that existed and were active in a fixed past window (e.g. repos with commit activity in a chosen year several years ago), explicitly NOT filtered by whether they are still maintained today, then `git clone` + `git log --numstat` each (unrated-limited) to get full commit history exactly as the existing dataset does. Standardize output to the same exp_sel_data_out schema as art_ZuMis522AEPF (repo_metadata, founder_signal, commits[]) so it is a drop-in-compatible superset/companion corpus, and explicitly report per-repo whether each was sampled by a liveness-conditioned or liveness-non-conditioned procedure via a new sampling_frame metadata field, so downstream analysis can compare or pool them honestly rather than silently mixing biased and unbiased samples.\",\n          \"depends_on\": [\n            {\"id\": \"art_ZuMis522AEPF\", \"label\": \"extends\"}\n          ]", "newString": "          \"approach\": \"First check whether a GITHUB_TOKEN or equivalent authenticated credential is available in this environment; if so, resume the existing checkpointed 104-repo candidate pipeline (the prior dataset artifact's code/build_dataset.py, code/candidates.py, temp/checkpoint.json, reused by re-reading that workspace's code) using it to raise the rate limit and pull full commit histories for as many additional candidates as the time budget allows, explicitly including repositories that are NOT currently famous/thriving (e.g. sampled from older, less-starred, or now-quiet repos in the candidate list) to avoid re-introducing the same survivorship bias. If no token is available, pull instead from GH Archive or another non-authenticated historical source identified by the research artifact: construct a sample of repositories that existed and were active in a fixed past window (e.g. repos with commit activity in a chosen year several years ago), explicitly NOT filtered by whether they are still maintained today, then `git clone` + `git log --numstat` each (unrated-limited) to get full commit history exactly as the existing dataset does. Standardize output to the same exp_sel_data_out schema as the existing dataset artifact (repo_metadata, founder_signal, commits[]) so it is a drop-in-compatible superset/companion corpus, and explicitly report per-repo whether each was sampled by a liveness-conditioned or liveness-non-conditioned procedure via a new sampling_frame metadata field, so downstream analysis can compare or pool them honestly rather than silently mixing biased and unbiased samples.\",\n          \"depends_on\": [\n            {\"id\": \"art_5rKf3placeholder\", \"label\": \"placeholder\"}\n          ]", "originalFile": null, "structuredPatch": [{"oldStart": 14, "oldLines": 9, "newStart": 14, "newLines": 9, "lines": ["         {", "           \"type\": \"dataset\",", "           \"objective\": \"Attempt to build a founder-departure commit corpus sampled from a historical snapshot that does NOT condition on present-day liveness, using the research artifact's recommended source and the existing ~104-repo candidate pipeline/checkpoint as a starting point, in order to give the experiment/evaluation a chance at a non-surviving founder-only TFDD event and a genuinely non-survivorship-biased corpus.\",", "-          \"approach\": \"First check whether a GITHUB_TOKEN or equivalent authenticated credential is available in this environment; if so, resume the existing checkpointed 104-repo candidate pipeline (art_ZuMis522AEPF's code/build_dataset.py, code/candidates.py, temp/checkpoint.json) using it to raise the rate limit and pull full commit histories for as many additional candidates as the time budget allows, explicitly including repositories that are NOT currently famous/thriving (e.g. sampled from older, less-starred, or now-quiet repos in the candidate list) to avoid re-introducing the same survivorship bias. If no token is available, pull instead from GH Archive or another non-authenticated historical source identified by the research artifact: construct a sample of repositories that existed and were active in a fixed past window (e.g. repos with commit activity in a chosen year several years ago), explicitly NOT filtered by whether they are still maintained today, then `git clone` + `git log --numstat` each (unrated-limited) to get full commit history exactly as the existing dataset does. Standardize output to the same exp_sel_data_out schema as art_ZuMis522AEPF (repo_metadata, founder_signal, commits[]) so it is a drop-in-compatible superset/companion corpus, and explicitly report per-repo whether each was sampled by a liveness-conditioned or liveness-non-conditioned procedure via a new sampling_frame metadata field, so downstream analysis can compare or pool them honestly rather than silently mixing biased and unbiased samples.\",", "+          \"approach\": \"First check whether a GITHUB_TOKEN or equivalent authenticated credential is available in this environment; if so, resume the existing checkpointed 104-repo candidate pipeline (the prior dataset artifact's code/build_dataset.py, code/candidates.py, temp/checkpoint.json, reused by re-reading that workspace's code) using it to raise the rate limit and pull full commit histories for as many additional candidates as the time budget allows, explicitly including repositories that are NOT currently famous/thriving (e.g. sampled from older, less-starred, or now-quiet repos in the candidate list) to avoid re-introducing the same survivorship bias. If no token is available, pull instead from GH Archive or another non-authenticated historical source identified by the research artifact: construct a sample of repositories that existed and were active in a fixed past window (e.g. repos with commit activity in a chosen year several years ago), explicitly NOT filtered by whether they are still maintained today, then `git clone` + `git log --numstat` each (unrated-limited) to get full commit history exactly as the existing dataset does. Standardize output to the same exp_sel_data_out schema as the existing dataset artifact (repo_metadata, founder_signal, commits[]) so it is a drop-in-compatible superset/companion corpus, and explicitly report per-repo whether each was sampled by a liveness-conditioned or liveness-non-conditioned procedure via a new sampling_frame metadata field, so downstream analysis can compare or pool them honestly rather than silently mixing biased and unbiased samples.\",", "           \"depends_on\": [", "-            {\"id\": \"art_ZuMis522AEPF\", \"label\": \"extends\"}", "+            {\"id\": \"art_5rKf3placeholder\", \"label\": \"placeholder\"}", "           ]", "         },", "         {"]}], "userModified": false, "replaceAll": false}
```

### [12] TOOL CALL — Edit · 2026-08-20 20:08:05 UTC

```
File: /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json
OLD:           "depends_on": [
            {"id": "art_5rKf3placeholder", "label": "placeholder"}
          ]
NEW:           "depends_on": []
```

### [13] TOOL RESULT — Edit · 2026-08-20 20:08:05 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "oldString": "          \"depends_on\": [\n            {\"id\": \"art_5rKf3placeholder\", \"label\": \"placeholder\"}\n          ]", "newString": "          \"depends_on\": []", "originalFile": null, "structuredPatch": [{"oldStart": 15, "oldLines": 9, "newStart": 15, "newLines": 7, "lines": ["           \"type\": \"dataset\",", "           \"objective\": \"Attempt to build a founder-departure commit corpus sampled from a historical snapshot that does NOT condition on present-day liveness, using the research artifact's recommended source and the existing ~104-repo candidate pipeline/checkpoint as a starting point, in order to give the experiment/evaluation a chance at a non-surviving founder-only TFDD event and a genuinely non-survivorship-biased corpus.\",", "           \"approach\": \"First check whether a GITHUB_TOKEN or equivalent authenticated credential is available in this environment; if so, resume the existing checkpointed 104-repo candidate pipeline (the prior dataset artifact's code/build_dataset.py, code/candidates.py, temp/checkpoint.json, reused by re-reading that workspace's code) using it to raise the rate limit and pull full commit histories for as many additional candidates as the time budget allows, explicitly including repositories that are NOT currently famous/thriving (e.g. sampled from older, less-starred, or now-quiet repos in the candidate list) to avoid re-introducing the same survivorship bias. If no token is available, pull instead from GH Archive or another non-authenticated historical source identified by the research artifact: construct a sample of repositories that existed and were active in a fixed past window (e.g. repos with commit activity in a chosen year several years ago), explicitly NOT filtered by whether they are still maintained today, then `git clone` + `git log --numstat` each (unrated-limited) to get full commit history exactly as the existing dataset does. Standardize output to the same exp_sel_data_out schema as the existing dataset artifact (repo_metadata, founder_signal, commits[]) so it is a drop-in-compatible superset/companion corpus, and explicitly report per-repo whether each was sampled by a liveness-conditioned or liveness-non-conditioned procedure via a new sampling_frame metadata field, so downstream analysis can compare or pool them honestly rather than silently mixing biased and unbiased samples.\",", "-          \"depends_on\": [", "-            {\"id\": \"art_5rKf3placeholder\", \"label\": \"placeholder\"}", "-          ]", "+          \"depends_on\": []", "         },", "         {", "           \"type\": \"evaluation\","]}], "userModified": false, "replaceAll": false}
```

### [14] ASSISTANT · 2026-08-20 20:08:11 UTC

```
Now fix the evaluation artifact's dependency on the evaluation-typed artifact.
```

### [15] TOOL CALL — Edit · 2026-08-20 20:08:11 UTC

```
File: /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json
OLD:           "depends_on": [
            {"id": "art_ZuMis522AEPF", "label": "dataset"},
            {"id": "art_I5KoOp16hub5", "label": "experiment"},
            {"id": "art_JvYoV94jgkuB", "label": "extends"}
          ]
NEW:           "depends_on": [
            {"id": "art_ZuMis522AEPF", "label": "dataset"},
            {"id": "art_I5KoOp16hub5", "label": "experiment"}
          ]
```

### [16] TOOL RESULT — Edit · 2026-08-20 20:08:11 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "oldString": "          \"depends_on\": [\n            {\"id\": \"art_ZuMis522AEPF\", \"label\": \"dataset\"},\n            {\"id\": \"art_I5KoOp16hub5\", \"label\": \"experiment\"},\n            {\"id\": \"art_JvYoV94jgkuB\", \"label\": \"extends\"}\n          ]", "newString": "          \"depends_on\": [\n            {\"id\": \"art_ZuMis522AEPF\", \"label\": \"dataset\"},\n            {\"id\": \"art_I5KoOp16hub5\", \"label\": \"experiment\"}\n          ]", "originalFile": null, "structuredPatch": [{"oldStart": 23, "oldLines": 8, "newStart": 23, "newLines": 7, "lines": ["           \"approach\": \"Extend eval.py's methodology: (1) report the exact permutation scheme used in the prior evaluation artifact — number of feasible distinct relocatable windows per repository given each project's history length, whether the 60/40 permutations were i.i.d. samples with or without replacement, the theoretical minimum achievable two-sided p-value given n and the permutation count, and re-run the permutation test at a substantially larger budget (e.g. 2000+ permutations per stratum, using the existing capped/cached DOA-recomputation fix) to report p-value convergence/stability versus the original 60/40-permutation result; (2) compute a Wilson 95% CI for Avelino et al.'s reported 66% TF=1 statistic from their stated n=315 TFDDs, and report it side-by-side with this paper's own CI rather than asserting 'overlapping' without the comparison interval; (3) manually spot-check the alias-resolution diagnostic's 0.0-median-collapse-rate finding against the actual GitHub contributor pages (via aii-web-tools fetch) for 2-3 corpus repositories, reporting whether any distinct-looking commit identities are actually the same contributor under a different email/handle, to test whether the diffusion score's 'distinct non-founder owner' counts are inflated by under-merging; (4) emit a full, exact table of all 15 (or more, if the dataset artifact's expansion completed) repositories with name, language, stars, commit-history years, and TFDD/survival status, matching the dataset artifact's actual output exactly, for inclusion as a paper table/appendix; (5) if the dataset artifact produced a non-conditioned or larger corpus, re-run Stage A calibration and the founder-only-TFDD extraction + permutation test on it and report explicitly whether TFDD incidence/survival rates move toward Avelino et al.'s reference values and whether outcome variance (a non-survivor) now exists, comparing this against the original 15-repo biased-frame results side by side as direct empirical evidence for the design-flaw-not-power-problem claim.\",", "           \"depends_on\": [", "             {\"id\": \"art_ZuMis522AEPF\", \"label\": \"dataset\"},", "-            {\"id\": \"art_I5KoOp16hub5\", \"label\": \"experiment\"},", "-            {\"id\": \"art_JvYoV94jgkuB\", \"label\": \"extends\"}", "+            {\"id\": \"art_I5KoOp16hub5\", \"label\": \"experiment\"}", "           ]", "         }", "       ],"]}], "userModified": false, "replaceAll": false}
```

### [17] ASSISTANT · 2026-08-20 20:08:15 UTC

```
Also fix the mention of "extends" reference to prior evaluation artifact in the approach text.
```

### [18] TOOL CALL — Edit · 2026-08-20 20:08:15 UTC

```
File: /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json
OLD:           "approach": "Extend eval.py's methodology: (1) report the exact permutation scheme used in the prior evaluation artifact —
NEW:           "approach": "Extend the prior evaluation's eval.py methodology: (1) report the exact permutation scheme used in that prior run —
```

### [19] TOOL RESULT — Edit · 2026-08-20 20:08:15 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "oldString": "          \"approach\": \"Extend eval.py's methodology: (1) report the exact permutation scheme used in the prior evaluation artifact —", "newString": "          \"approach\": \"Extend the prior evaluation's eval.py methodology: (1) report the exact permutation scheme used in that prior run —", "originalFile": null, "structuredPatch": [{"oldStart": 20, "oldLines": 7, "newStart": 20, "newLines": 7, "lines": ["         {", "           \"type\": \"evaluation\",", "           \"objective\": \"Close every reviewer-named methodology-rigor and reporting gap on the existing 15-repo pipeline result: exact permutation-scheme disclosure with convergence at higher budget, Avelino et al.'s own confidence interval for the 66% TF=1 statistic, a manual alias-resolution spot-check against live GitHub contributor pages, a full exact repository table, and (if the new dataset artifact produced additional or non-survivor data) a re-run of the calibration gate and permutation test on the combined/expanded corpus with an explicit comparison of biased vs. non-conditioned sampling frames.\",", "-          \"approach\": \"Extend eval.py's methodology: (1) report the exact permutation scheme used in the prior evaluation artifact — number of feasible distinct relocatable windows per repository given each project's history length, whether the 60/40 permutations were i.i.d. samples with or without replacement, the theoretical minimum achievable two-sided p-value given n and the permutation count, and re-run the permutation test at a substantially larger budget (e.g. 2000+ permutations per stratum, using the existing capped/cached DOA-recomputation fix) to report p-value convergence/stability versus the original 60/40-permutation result; (2) compute a Wilson 95% CI for Avelino et al.'s reported 66% TF=1 statistic from their stated n=315 TFDDs, and report it side-by-side with this paper's own CI rather than asserting 'overlapping' without the comparison interval; (3) manually spot-check the alias-resolution diagnostic's 0.0-median-collapse-rate finding against the actual GitHub contributor pages (via aii-web-tools fetch) for 2-3 corpus repositories, reporting whether any distinct-looking commit identities are actually the same contributor under a different email/handle, to test whether the diffusion score's 'distinct non-founder owner' counts are inflated by under-merging; (4) emit a full, exact table of all 15 (or more, if the dataset artifact's expansion completed) repositories with name, language, stars, commit-history years, and TFDD/survival status, matching the dataset artifact's actual output exactly, for inclusion as a paper table/appendix; (5) if the dataset artifact produced a non-conditioned or larger corpus, re-run Stage A calibration and the founder-only-TFDD extraction + permutation test on it and report explicitly whether TFDD incidence/survival rates move toward Avelino et al.'s reference values and whether outcome variance (a non-survivor) now exists, comparing this against the original 15-repo biased-frame results side by side as direct empirical evidence for the design-flaw-not-power-problem claim.\",", "+          \"approach\": \"Extend the prior evaluation's eval.py methodology: (1) report the exact permutation scheme used in that prior run — number of feasible distinct relocatable windows per repository given each project's history length, whether the 60/40 permutations were i.i.d. samples with or without replacement, the theoretical minimum achievable two-sided p-value given n and the permutation count, and re-run the permutation test at a substantially larger budget (e.g. 2000+ permutations per stratum, using the existing capped/cached DOA-recomputation fix) to report p-value convergence/stability versus the original 60/40-permutation result; (2) compute a Wilson 95% CI for Avelino et al.'s reported 66% TF=1 statistic from their stated n=315 TFDDs, and report it side-by-side with this paper's own CI rather than asserting 'overlapping' without the comparison interval; (3) manually spot-check the alias-resolution diagnostic's 0.0-median-collapse-rate finding against the actual GitHub contributor pages (via aii-web-tools fetch) for 2-3 corpus repositories, reporting whether any distinct-looking commit identities are actually the same contributor under a different email/handle, to test whether the diffusion score's 'distinct non-founder owner' counts are inflated by under-merging; (4) emit a full, exact table of all 15 (or more, if the dataset artifact's expansion completed) repositories with name, language, stars, commit-history years, and TFDD/survival status, matching the dataset artifact's actual output exactly, for inclusion as a paper table/appendix; (5) if the dataset artifact produced a non-conditioned or larger corpus, re-run Stage A calibration and the founder-only-TFDD extraction + permutation test on it and report explicitly whether TFDD incidence/survival rates move toward Avelino et al.'s reference values and whether outcome variance (a non-survivor) now exists, comparing this against the original 15-repo biased-frame results side by side as direct empirical evidence for the design-flaw-not-power-problem claim.\",", "           \"depends_on\": [", "             {\"id\": \"art_ZuMis522AEPF\", \"label\": \"dataset\"},", "             {\"id\": \"art_I5KoOp16hub5\", \"label\": \"experiment\"}"]}], "userModified": false, "replaceAll": false}
```

### [20] ASSISTANT · 2026-08-20 20:08:15 UTC

```
Dependencies fixed: the dataset artifact now has `depends_on: []` (dataset artifacts can only depend on research, and none exists yet), and the evaluation artifact depends only on the dataset and experiment artifacts (dropped the invalid evaluation→evaluation dependency).
```
