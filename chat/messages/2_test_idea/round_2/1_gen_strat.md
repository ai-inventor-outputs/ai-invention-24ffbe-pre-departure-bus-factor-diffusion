# gen_strat_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_strat`
> Run: `iter1_0b7b616dce39` — Scaling the Corpus, Auditing the Power, and Reconciling the Sign: What Happens When a Founder-Diffusion Survival Test Is Finally Interrogated Rather Than Just Run
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_strat_1` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-08-21 19:43:06 UTC

```
model: claude-sonnet-5 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/gen_strat/gen_strat_1
```

### [2] SYSTEM-USER prompt · 2026-08-21 19:43:14 UTC

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
title: Pre-Departure Authority Diffusion and OSS Survival
hypothesis: >-
  An open-source project's survival after its founder stops committing (a founder-only Truck Factor Developer Detachment,
  or TFDD, in Avelino et al.'s ESEM 2019 terminology) is hypothesized to depend less on the project's popularity or size at
  the moment of departure -- which Avelino et al. already show is statistically indistinguishable between survivors and non-survivors
  at the TFDD snapshot (d=0.13-0.26) -- and more on how diffused DOA-based commit/file authority already was among non-founder
  contributors in the 6-12 months BEFORE departure. Two iterations of testing establish the following, in order of evidential
  strength. (1) STRONGLY SUPPORTED: a fame-conditioned corpus (repositories selected for being famous/actively-maintained
  today) structurally cannot test this hypothesis, because it excludes non-surviving founder-only TFDD events by construction
  (prior corpus: 5/5 events, 100% survival, z=2.70 vs Avelino et al.'s reference rate, p=0.011). A stratified, popularity-independent
  sampling frame across 6 languages and 3 star strata (chosen deliberately, since Nourry et al.'s 36,000-project TFDD study
  does not report explicitly avoiding present-day-popularity conditioning) restores real outcome variance -- 16 strict / 20
  relaxed founder-only TFDD events at 31.3%/45.0% survival, consistent with Avelino et al.'s 40.6% reference -- and this corpus-construction
  method is itself now the load-bearing, reusable contribution. (2) NOT YET SUPPORTED OR REFUTED: with outcome variance restored,
  the core diffusion-predicts-survival test ran for the first time (logistic regression, matched-pairs, Mann-Whitney) and
  found coefficients in the hypothesis-consistent direction (founder-share -5.56, diffused-owner-count -0.174) but none reaching
  significance after BH correction at n=16-20 (BH p=0.60), zero eligible matched pairs, and non-significant Mann-Whitney (p=0.66,
  p=0.28). This is read as an ordinary underpowered first pass (n=16-20 vs. the ~40-event target implied by the original power
  analysis), not as evidence against the hypothesis, and the hypothesis's central causal claim remains open pending a scaled
  corpus (target 200-300+ processed repositories via the same stratified frame). (3) OPEN TENSION TO RESOLVE: Medappa et al.'s
  well-powered (n=5,762) finding that a higher STATIC ratio of write-access contributors reduces survival is the opposite
  sign from this hypothesis's DYNAMIC, founder-specific, pre-departure-window diffusion measure; the working reconciliation
  to test explicitly in the next iteration is that diffusion is protective specifically as a succession-planning signal concentrated
  in the months immediately preceding a founder's departure (this hypothesis's operationalization), while a permanently high
  write-access ratio is destabilizing as a coordination-cost effect (Medappa et al.'s operationalization) -- these are not
  necessarily the same construct despite superficial similarity, and distinguishing them (e.g., via the placebo/window-relocation
  check already implemented) is now a first-class part of the investigation rather than a footnote.
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
  Same TFDD/DOA frame; corpus fix validated, core test underpowered, scope narrowed to scaling + Medappa reconciliation.
_confidence_delta: unchanged
_key_changes:
- >-
  Elevated the corpus-construction fix (fame-independent stratified sampling) to a first-class, empirically validated contribution
  distinct from the still-open causal claim.
- >-
  Reframed the core diffusion-predicts-survival test as an underpowered first pass (n=16-20 vs ~40 target) rather than either
  confirmed or disconfirmed, per this iteration's actual results.
- >-
  Added explicit reconciliation of the Medappa et al. contrary finding (static write-access ratio reduces survival) as a required
  next-iteration test, per reviewer MAJOR feedback.
- >-
  Added filtering-funnel transparency and single-dominant-founder selection-bias check to assumptions/investigation_approach,
  per reviewer MINOR feedback.
- >-
  Flagged the unresolved dataset-artifact provenance discrepancy (121-repo pilot vs 270-repo scaled corpus) as an item to
  resolve next iteration.
- >-
  Added explicit comparison to Nourry et al.'s sampling approach to substantiate (or temper) the fame-independence novelty
  claim.
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
title: Pre-Departure Authority Diffusion Predicts Survival
objective: >-
  Establish, from real GitHub commit history, whether the DIFFUSION of DOA-based file authority and commit share away from
  a project's founder in the 6-12 months before their Truck-Factor Developer Detachment (TFDD) predicts 18-month post-departure
  survival better than size/popularity covariates measured at the TFDD snapshot itself (Avelino et al.'s null result).
rationale: >-
  Avelino et al. (ESEM 2019) built the DOA/TF/TFDD/Active-Inactive machinery and showed size does not separate survivors from
  non-survivors AT the snapshot, but never tested the pre-departure TREND. This iteration's job is to build the one artifact
  chain that can actually settle that: a real corpus of founder-only TFDD events with longitudinal DOA computed in the run-up
  to departure, a matched-pairs/regression test of the diffusion hypothesis, and a placebo/shuffle check that is the single
  strongest thing a reviewer would demand before believing the effect is temporally specific rather than 'active projects
  are just generally diffused.' Packing dataset+experiment+eval into one iteration (rather than spreading dataset-only across
  two) leaves iteration 2 free to refine the method (e.g. alternative diffusion definitions, robustness to alias resolution)
  rather than still be assembling data.
artifact_directions:
- id: dataset_iter1_dir1
  type: dataset
  objective: >-
    Build a corpus of real GitHub repositories with full commit/file history sufficient to (a) identify founder-only TFDD
    events via a DOA-based Truck Factor computation, and (b) support an 18-month post-TFDD survival label plus >=6 months
    of pre-TFDD commit/file-ownership history per repo.
  approach: >-
    Use the GitHub REST/GraphQL API (or a suitable HuggingFace/GH-archive mirror of commit metadata) to sample popular repositories
    across several languages and popularity strata, mirroring Avelino et al.'s top-starred-repo sampling but restricted to
    repos with a single clearly dominant original committer in their first commits and with at least 3 years of history after
    their earliest plausible core-team formation (to allow full pre/post TFDD windows without right-censoring). Pull per-commit
    metadata: author email/login, timestamp, and per-file diff stats (lines added/removed, file path) needed to run the DOA
    algorithm (file creation credit + relative-change-share). Resolve author aliases by email/login as far as feasible (flag
    known-limitation cases). Output standardized rows keyed by (repo, commit) with fields: repo_id, stars, forks, contributor_count,
    language, license, author_id, timestamp, files_touched (with per-file added/removed/is_creation), so downstream experiment
    code can run DOA/TF/TFDD entirely from this table without re-hitting the API. Aim for at least 150-250 qualifying founder-only-TFDD
    candidate repos after filtering (Avelino et al.'s TF=1 TFDD rate of 66% among 315 TFDDs suggests a corpus of ~1000-1500
    candidate popular repos is needed before filtering) — sample toward that scale within GitHub API rate limits and the size
    cap, and clearly report how many repos survive each filter stage (history length, mining artifacts, single-founder start)
    even if the final count falls short.
  depends_on: []
- id: experiment_iter1_dir2
  type: experiment
  objective: >-
    Implement Avelino et al.'s DOA/Truck-Factor/TFDD/Active-Inactive pipeline exactly as specified, apply it per-repo to detect
    founder-only TFDD events, compute the NEW pre-departure authority-diffusion trajectory metrics (founder commit-share and
    count of independent non-founder DOA file-owners in the 6-12 months before TFDD) not present in their published pipeline,
    compute the 18-month post-TFDD survival outcome, and fit the matched-pairs comparison plus logistic/ordinal regression
    from the investigation_approach and success_criteria.
  approach: >-
    For each repo in the dataset, compute yearly (or rolling 6-month) DOA scores per (developer, file) using Fritz et al.'s
    formula as specified by Avelino et al., derive the yearly Truck Factor set, and scan chronologically for the first TFDD
    where the detaching TF set has size 1 (founder-only). For each such event, compute (a) founder's share of authored commits
    in the 6-12 months immediately preceding TFDD, (b) count of distinct non-founder accounts that reached primary DOA ownership
    of >=1 file in that same window, and (c) the standard Avelino et al. snapshot covariates (developers/commits/files) AT
    the TFDD for comparison. Compute the survival label via the Active/Inactive recovery model over the 18 months after TFDD
    (thriving/maintained/dormant/dead, and a binary survived/not for the headline test). Build matched pairs within equal-size
    buckets (stars/forks/contributor-count/language) contrasting founder-share<50%+>=2 diffused-owners vs founder-share>=80%,
    and fit a Benjamini-Hochberg-corrected logistic/ordinal regression of survival on the diffusion predictors controlling
    for stars/forks/contributor-count/language/license, reporting standardized effect sizes against Avelino et al.'s reported
    d=0.13-0.26 for their snapshot covariates. Report the unconditioned survival rate among detected founder-TFDD events for
    direct comparability with Avelino et al.'s 41%.
  depends_on: []
- id: evaluation_iter1_dir3
  type: evaluation
  objective: >-
    Run the falsification/placebo check (randomly relocating the 'pre-departure window' within each project's history) and
    broader validity checks to determine whether the diffusion-survival association is genuinely specific to the pre-TFDD
    period, and audit robustness of the DOA/TFDD detection pipeline.
  approach: >-
    Using the experiment's per-repo longitudinal DOA/commit-share time series, re-run the diffusion-score computation with
    the '6-12 months pre-departure' window replaced by a randomly selected same-length window elsewhere in each project's
    pre-TFDD history (matched within survivor and non-survivor groups separately, per success_criteria #3), refit the same
    matched-pairs and regression tests on the shuffled window, and compare effect sizes/CI overlap against the true-window
    results to test whether the association collapses. Additionally stratify results by language and popularity bucket to
    check the effect isn't driven by one ecosystem, sanity-check the DOA/TF/TFDD implementation against Avelino et al.'s reported
    aggregate statistics (TFDD rate ~16% of projects, 66% at TF=1, 41% survival) as a pipeline-validity check, and report
    calibration of the survival regression (e.g. via bootstrap CIs) to support the significance claims in success_criteria
    #1-2.
  depends_on: []
expected_outcome: >-
  A real, standardized GitHub commit-history dataset of founder-only TFDD events with pre-departure longitudinal DOA/commit-share
  data; a working reimplementation of Avelino et al.'s DOA/TF/TFDD/survival pipeline extended with the novel pre-departure
  authority-diffusion metrics; and matched-pairs/regression results (with placebo check) reporting whether pre-departure diffusion
  predicts survival independent of, and more strongly than, the size covariates Avelino et al. found had negligible-to-small
  effect — the empirical core the paper needs, with iteration 2 free to refine metric definitions, add robustness checks,
  or address reviewer gaps.
summary: >-
  Build a real commit-history corpus of founder-only Truck-Factor departures, reimplement and extend Avelino et al.'s DOA/TFDD
  pipeline with a new pre-departure authority-diffusion trajectory metric, and test via matched-pairs regression plus a window-shuffle
  placebo whether that trajectory predicts post-founder survival where their own snapshot covariates do not.
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
id: art_ZbwYXh1VlhVp
type: dataset
title: GitHub Founder-Departure Commit Corpus
summary: >-
  Built from 121 real GitHub repositories sampled via the GitHub REST search API across JavaScript/Python/Java/Go and 3 popularity
  strata (100-1k, 1k-10k, 10k+ stars), each fully cloned locally (git clone --bare) and mined with `git log --numstat` for
  complete per-commit, per-file authorship history (no GitHub API rate-limit bottleneck on commit-level data). A filter funnel
  (documented in temp/funnel_report.json) reduced these to 34 'founder-only TFDD candidate' repos meeting: >=100 total commits,
  no history-loss/squash artifact (no single commit touching >90% of all files ever seen), and a single author holding >=70%
  share of commits in the first ~50-commit/6-month window. Author aliases are resolved via GitHub's `<id>+<login>@users.noreply.github.com`
  pattern and exact email/name matching; repos with >20% bot/generic-email commits are flagged via `metadata_alias_ambiguous_repo`.
  Each of the 70,260 output examples is one (commit, file) row: `input` is a JSON string of observable commit/file-change
  features (commit index, days since repo creation, file path/extension, lines added/removed, is_creation, repo stars/forks/language)
  with author identity withheld; `output` is the 'founder'/'other' authorship label; `metadata_*` fields carry repo_id, full_name,
  license, repo_created_at, commit_sha, commit_timestamp, author_alias_key/email/name, the dominant-founder first-window share,
  and the alias-ambiguity flag. Repos with more than 4000 rows are systematically strided down to that cap (every Nth row,
  chronological order preserved) to keep multi-year histories from a few huge repos (e.g. jenkinsci/jenkins, langchain-ai/langchain)
  from dominating the corpus and to respect the size budget. Final scope (34 repos, 4 languages) is a documented reduced-scope
  fallback from the 150-250/6-language target: GitHub's unauthenticated search API caps at 10 req/min and repo cloning is
  network/time bound, so language and strata breadth were narrowed to what fit the time budget while still meeting the single-founder-start,
  >=100-commit, and non-artifact filters. Known limitation: `days_since_repo_created` can be negative for repos whose GitHub
  creation date postdates their earliest preserved commit (e.g. imported from another VCS with original timestamps kept) --
  this is a genuine provenance quirk of GitHub metadata, not a pipeline bug, and downstream users should be aware some repos
  carry pre-GitHub-import history. Validated against the exp_sel_data_out.json schema; full_data_out.json is 75MB (under the
  100MB per-file and 300MB total caps).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
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
id: art_4CZ-9Ou1G5ty
type: experiment
title: Does Founder Authority Diffusion Predict OSS Survival?
summary: >-
  Re-implements Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure
  (TFDD) / Active-Inactive survival pipeline directly from real GitHub commit histories via the GitHub REST search API and
  `git log --numstat` history walks (no mocked or synthetic data). Sampled 270 candidate repositories across 6 languages (Python,
  JavaScript, Go, Ruby, Java, C++) stratified by popularity tier; 69 survived the age/size filters and were fully processed
  (clone -> per-file DOA snapshots -> yearly Truck-Factor sets -> TFDD detection). Detected 16 strict founder-only (TF=1)
  TFDD events and 20 relaxed (TF<=2) TFDD events. Unconditioned 18-month post-TFDD survival rate was 31.25% (strict) / 45%
  (relaxed), in the same neighborhood as Avelino et al.'s reported ~41%, cross-validating the DOA/TF/TFDD re-implementation.
  The new contribution (our_method) is a pre-departure authority-diffusion trajectory computed in the 12-to-6-month window
  before each TFDD event: founder_share (fraction of window commits made by the founder) and n_diffused_owners (count of independent
  non-founder DOA file-owners at window end). This is compared against Avelino et al.'s own approach (baseline): snapshot
  size/popularity covariates (stars, forks, developer count) measured AT the TFDD event with no temporal trajectory information.
  Both are fit as BH-corrected logistic regressions on the same 16-event strict sample, plus a within-repo placebo/falsification
  check that recomputes the same diffusion metrics on a random non-TFDD-adjacent window (15/16 events had a valid placebo
  window) to test whether the signal is specific to the pre-departure period rather than a generic property of any window.
  A matched-pairs bootstrap risk-ratio design (stars/forks/language-bucketed low-diffusion vs high-diffusion event pairs)
  was also implemented per the plan but found 0 matchable pairs at this sample size (n_pairs=0, risk_ratio=NaN) and is reported
  honestly as inconclusive at this scale rather than fabricated. In the realized logistic fit, our_method's founder_share
  coefficient is negative (-5.56, i.e. higher founder commit-share pre-departure associates with lower survival) and n_diffused_owners
  is also negative (-0.17) in this small sample, but neither survives BH correction at n=16 (BH p>0.6 for all covariates in
  both our_method and the baseline); pseudo-R^2 is 0.175 (our_method) vs 0.211 (baseline snapshot-only), so the baseline explains
  marginally more deviance in this small realized sample. The placebo regression on random non-TFDD windows shows a much larger,
  non-significant coefficient on placebo_founder_share (-164.5, p=1.0), consistent with the placebo metric being poorly identified
  in a non-TFDD-adjacent window rather than a real effect. All numbers here are the genuine output of one completed pipeline
  run (906.7s wall-clock) with no placeholders; the honest headline is that with only 16 founder-only TFDD events the study
  is underpowered to detect a significant BH-corrected effect, and this is reported transparently (raw coefficients, p-values,
  and both BH-corrected and uncorrected results are all present in the output) rather than oversold. method.py implements
  Stages 0-9 exactly as specified in the artifact plan: GitHub API sampling with popularity stratification, exclusion-criteria
  filtering (age/size/fork), `git log --numstat` commit-history extraction, the Fritz-et-al DOA formula (3.293 + 1.098*FA
  - 0.164*sqrt(AC) + 0.230*ln(1+DL)), greedy Truck-Factor-set computation, yearly TFDD scanning with a 1-year silence threshold,
  both strict (TF=1) and relaxed (TF<=2) TFDD detection reported separately, 12-to-6-month pre-departure diffusion metrics,
  18-month post-TFDD Active/Inactive survival labeling, a within-repo placebo window falsification check, matched-pairs bootstrap
  risk-ratio, and BH-corrected logistic regression for both our_method and the baseline, with all per-event rows preserved
  in method_out.json (16 example rows under the exp_gen_sol_out schema, `dataset='founder_authority_diffusion_tfdd_survival'`,
  `input`=repo/founder identity JSON, `output`=full event record JSON, plus `predict_our_method_survived_prob` and `predict_baseline_survived_prob`
  per-example predicted probabilities). Full/mini/preview variants were generated and both files (21KB) are far under the
  100MB size-limit threshold, so no splitting was required. Downstream GEN_PAPER_TEXT should present this as a genuine re-implementation
  validated against Avelino et al.'s published survival rate, with the new pre-departure diffusion signal reported as a directionally-consistent
  but not-yet-statistically-significant finding at n=16, and should NOT claim the matched-pairs risk-ratio result since it
  produced 0 matched pairs at this scale.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
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
id: art_wWTWRqndgmX9
type: evaluation
title: Placebo-Window Falsification Audit for Founder Exit
summary: >-
  This evaluation artifact (eval.py, eval_out.json) implements the Placebo-Window Falsification and Robustness Audit for the
  founder-exit authority-diffusion / OSS-survival experiment (gen_art_experiment_1). It reads the upstream experiment's per-repo
  TFDD event tables, founder pre-departure diffusion scores, and 18-month survival labels, then runs four independent checks:
  (1) placebo_test — for each founder-TFDD project it enumerates valid non-overlapping 6-12 month windows in pre-TFDD history,
  draws one placebo window per project uniformly at random within the survivor and non-survivor groups separately (>=3 fixed
  seeds for seed-sensitivity), recomputes the diffusion score with the experiment's exact scoring function, refits the same
  matched-pairs survival-rate-ratio and BH-corrected logistic/ordinal regression used on the true window, and classifies the
  result PASS/WEAK/FAIL via a permutation/paired-bootstrap test of true-vs-placebo effect size (operationalizing success_criteria
  #3); (2) stratified_robustness — reruns the true-window matched-pairs and regression separately per language and popularity
  bucket, flags underpowered strata (n<10), and computes a heterogeneity check (Cochran's Q / range-vs-pooled-CI) to detect
  Simpson's-paradox-style ecosystem dominance; (3) pipeline_validity — sanity-checks the DOA/TF/TFDD reimplementation against
  Avelino et al.'s published aggregate statistics (TFDD rate ~16%, TF=1 share 66%, unconditioned TFDD survival 41%) with Wilson/bootstrap
  95% CIs and an explicit PASS/CONCERN flag within a 1.5x relative-distance band, documenting that some divergence is expected
  given this run's founder-only, stratified-sampled corpus versus Avelino et al.'s full top-500-per-language corpus; (4) calibration
  — bootstraps (>=1000 resamples) a predicted-probability-decile calibration curve, Brier score, per-coefficient 95% CIs,
  and AUC/C-statistic with CI for the true-window survival regression, to stress-test the significance claims in success_criteria
  #1-2 beyond a single point-estimate p-value. All four checks, plus a top-level overall_verdict and a free-text caveats field,
  are written to eval_out.json with clear per-check status keys (COMPUTED or UNAVAILABLE with a specific reason) so that any
  missing upstream field (e.g. no full window time series, only a single true-window score) is flagged explicitly as a pipeline
  gap rather than silently skipped or fabricated. At the time this artifact was finalized, the upstream gen_art_experiment_1
  artifact had not yet produced its method_out.json / results/ output (still mid-run), so eval.py's own gap-handling logic
  correctly recorded every check as UNAVAILABLE with overall_verdict='UNDETERMINED_PIPELINE_GAP' and a detailed caveats string
  naming exactly which upstream files/fields were missing (results/method_summary.json, per-repo event tables with founder_share/n_diffused_owners/survived
  columns, etc.) rather than fabricating placeholder statistics. eval.py is fully implemented, self-contained, and re-runnable:
  once the upstream experiment finishes, re-invoking `uv run eval.py` against the same workspace paths will populate all four
  checks with real point estimates, CIs, and PASS/WEAK/FAIL/CONCERN verdicts using the exact same code path documented above,
  with no changes needed to the script itself. Downstream consumers (GEN_PAPER_TEXT) should treat this artifact's current
  eval_out.json as reporting an incomplete-upstream-data state, not a negative or null result on the underlying falsification
  hypothesis, and should prefer re-running eval.py against a completed experiment artifact before citing any of its numeric
  verdicts in the paper.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1
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

Open-source software projects routinely depend on the sustained attention of one or two people, and when the developer who founded such a project stops committing -- a Truck-Factor Developer Detachment (TFDD) in Avelino et al.'s terminology, the point at which every developer in a project's minimal Truck-Factor set has gone silent for a validated twelve-month threshold -- some projects go dark permanently while others are picked up and continue for years [1]. Avelino et al. showed the obvious predictor of which outcome a project gets does not work: at the TFDD snapshot itself, surviving and non-surviving projects are statistically indistinguishable in size (Cohen's d = 0.13-0.26). A prior iteration of this project built the instrument needed to ask the natural follow-up question -- does the trend of authority concentration in the months before departure, rather than the size snapshot at departure, carry the missing signal -- and found that instrument sound but untestable: a corpus assembled from repositories that are famous and actively maintained today structurally excludes the non-surviving projects the hypothesis needs to observe, so every founder-only TFDD event that corpus contained had, by construction, survived.

This paper reports the direct fix to that defect and what happens once it is applied. We build a second corpus using a stratified sampling frame across six languages (Python, JavaScript, Go, Java, Ruby, C++) and three star-count strata (50-500, 500-5,000, 5,000-100,000), explicitly designed not to condition candidate selection on whether a repository is still notable today, starting from 270 sampled repositories and retaining 69 after filtering for sufficient history, single-founder dominance, and freedom from mining artifacts. Run through the same reimplemented Degree-of-Authorship (DOA) / Truck-Factor / TFDD pipeline as the prior iteration, this corpus produces 16 founder-only TFDD events under a strict founder-identification rule (20 under a relaxed rule) with a survival rate of 31.3% (45.0% relaxed) -- both now overlapping Avelino et al.'s published 41% reference rate, in sharp contrast to the prior corpus's uniform 100%. The corpus-construction problem is solved.

What that solved problem buys is the ability to finally run the tests the prior iteration specified but could not execute -- and we report exactly what they show. A logistic regression of survival on pre-departure founder commit-share and non-founder DOA-owner count, alongside the original at-TFDD snapshot covariates, finds coefficients in the hypothesis-consistent direction (more diffusion, i.e. lower founder share and more distinct owners, associated with higher survival odds) but none reaching significance after Benjamini-Hochberg correction at n=16 (BH-corrected p=0.60 for founder share). A matched-pairs comparison of high- versus low-diffusion projects, matched on size and language, finds zero eligible pairs at this sample size. A non-parametric Mann-Whitney comparison of the two diffusion predictors between survivors and non-survivors returns p=0.66 and p=0.28. None of this is a null result in the strong sense the prior iteration's zero-outcome-variance corpus produced -- it is an underpowered result, the ordinary and expected state of a first test on 16-20 events, and we report it as such rather than either overclaiming the hypothesis-consistent direction of the coefficients or treating non-significance as disconfirmation.

We also report a defect discovered in the course of this iteration rather than omit it: the independent evaluation harness responsible for a placebo-window falsification test and a stratified robustness audit of this corpus executed against an incomplete version of the upstream experiment output -- a race condition between the experiment and evaluation stages, documented in the evaluation's own machine-readable caveats -- and produced no usable robustness result for this corpus. This is a pipeline-engineering gap, not a scientific finding, and we distinguish it clearly from the (also negative, but statistically meaningful) underpowered-regression result above.

**What this paper is, concretely.** A corpus-construction fix, demonstrated to work by the statistic that mattered (outcome variance restored, survival rate now consistent with the published reference population rather than pinned at a boundary); the first actual run, on real data, of the causal test this line of work has been building toward across two iterations, reported at the power level it was run at rather than inflated by selective emphasis; and a disclosed pipeline-engineering gap in the evaluation stage, reported alongside a concrete fix, so a reader can tell the difference between "the hypothesis was tested and found weak" and "part of the pipeline did not run."

[FIGURE:fig1]

**Summary of Contributions**

- A stratified, fame-independent corpus (six languages, three popularity strata, 270 sampled / 69 processed repositories) that restores real 18-month survival-outcome variance among founder-only TFDD events -- 31.3% strict / 45.0% relaxed survival, versus the prior iteration's corpus-wide 100% -- and is statistically consistent with Avelino et al.'s published 41% reference rate.
- The first execution, on real data across this two-iteration project, of the full statistical test battery the diffusion hypothesis requires -- logistic regression with Benjamini-Hochberg correction, matched-pairs comparison, and a Mann-Whitney non-parametric check -- reported at actual sample size (n=16-20) with exact coefficients, p-values, and pseudo-R2 rather than only a verdict.
- A disclosed pipeline-engineering defect: the evaluation stage ran against an incomplete upstream experiment artifact due to a race condition, invalidating this iteration's independent placebo-window and robustness audit, reported with its exact machine-logged diagnosis and a scoped fix rather than silently omitted.
- An honest accounting of what remains open after two iterations -- a working, fame-independent corpus-construction method and a hypothesis test run at real but low statistical power -- and the specific next step (scaling the same sampling frame, and fixing the evaluation race condition) that separates this from a study able to confirm or refute the founder-diffusion-predicts-survival hypothesis.

# Related Work

**Truck Factor and Degree of Authorship.** The Truck Factor -- the minimal number of developers whose combined departure would incapacitate a project -- was formalized computationally by Avelino et al., who estimate it via a greedy algorithm over per-file Degree-of-Authorship (DOA) scores rather than raw commit counts [2]. DOA itself originates with Fritz et al., who model developer expertise on a file as a function of file creation, subsequent edits relative to other contributors, and, in the interactive variant, IDE interaction events [7]; Avelino et al. use the authorship-only variant, weighting first-authorship, subsequent-edit count, and edits by others with empirically fit coefficients. Ferreira et al. compare three Truck-Factor estimation algorithms, including Avelino et al.'s DOA-based approach, and find it the most defensible of the three on a manually labeled sample [3]. This paper reuses the DOA/Truck-Factor computation from [1, 2] verbatim -- same weights, same greedy set construction -- rather than proposing a new expertise metric, so any new result is attributable to the new pre-departure measurement and the new corpus rather than to a re-tuned authorship model.

**Abandonment and survival.** Avelino et al.'s study is this paper's direct empirical basis [1]. Mining 1,932 popular GitHub repositories, they define TFDD -- the point at which every developer in a project's Truck-Factor set has been silent for the validated one-year threshold -- and score survival 18 months after each TFDD on a four-level Active/Inactive scale. They report that 315 projects (16%) experience a TFDD, that 66% of TFDDs occur at Truck Factor 1, that 128 of 315 (41%) survive, and that surviving and non-surviving projects are statistically indistinguishable in size at the TFDD snapshot (Cohen's d = 0.13-0.26). Their pipeline is never run before the TFDD; this paper's methodological departure, carried over from the prior iteration, is to run the identical DOA/Truck-Factor machinery one window earlier and treat the resulting trend, rather than the snapshot, as the candidate signal -- now on a corpus built to actually contain the survival-outcome variance that test requires.

**Why projects fail, self-reported.** Coelho and Valente survey maintainers of 104 curated failed GitHub projects and report nine failure reasons spanning team, project, and environment factors [4]. They also find failed projects adopt fewer maintenance-practice signals than surviving ones -- contributing guidelines (16% vs. 72%) and continuous integration (27% vs. 68%) -- plausible downstream correlates of the diffusion process this paper measures directly, though their unit of analysis is a single maintainer's retrospective account, not a multi-contributor measurement of pre-departure authority structure.

**Dependency abandonment from the consumer's side.** Miller et al. study how developers who depend on open-source packages detect and cope with a dependency going unmaintained [5]. Their focus is downstream -- how consumers navigate an abandonment they did not cause -- complementary to this paper's producer-side question of whether a project's own pre-departure authority structure predicts whether such navigation becomes necessary.

**Diffusion of write access and core-team loss.** Medappa et al. analyze a matched sample of 5,762 GitHub projects and find that a higher proportion of contributors holding write access -- a static, project-level analogue of the diffusion measured here dynamically and specifically before a founder's departure -- increases novelty but reduces survival [9]. This is a genuine complication for the mechanism this paper investigates: it shows diffusion of formal authority is not uniformly protective when measured as a static ratio, so this paper's diffusion-precedes-departure framing needs to hold up against a literature where the same underlying variable, measured differently, points the other way -- a tension this iteration's regression coefficients (negative, hypothesis-consistent, but not significant) neither resolve nor deepen. Nourry et al. re-examine the TFDD construct at over 36,000 projects and report that only 27% of abandoned projects attract a new Truck-Factor developer afterward [10] -- a base rate this iteration's 31.3-45.0% strict/relaxed survival range brackets, lending some external plausibility to the new corpus's numbers. Jabrayilzade et al. survey 269 practicing engineers and find informal judgments of who is "hard to replace" often diverge from commit-based Truck-Factor estimates [11], a reminder that DOA-based founder and authority-owner identification is a proxy grounded in version-control activity, not organizational knowledge.

**Contributor-diversity metrics and onboarding.** CHAOSS defines Contributor Absence Factor (formerly Bus Factor) as the count of top contributors needed to reach half of a project's contributions, noting the metric "can be measured both ways," as a snapshot or longitudinally [12]; it names the longitudinal option but does not formalize a pre-departure trend or validate one against an outcome, which this paper's diffusion measurement operationalizes and, now with real outcome variance, actually tests. The Apache Software Foundation Incubator's graduation guide instead judges "diversity" as a binary, committee-assessed gate at graduation. Jergensen, Sarma, and Wagstrom's "onion" model describes contributors migrating from periphery to core [13], and Steinmacher et al.'s systematic review of 20 studies organizes newcomer barriers into five categories [14]; both study the inward trajectory, while this paper studies the mirror-image outward trajectory of a founder's own authority dispersing before departure.

**Mining-methodology controls.** Because this study mines GitHub commit history to infer developer identity and project lifecycle, it inherits the hazards Kalliamvakou et al. document under "the perils of mining GitHub" [6] -- most relevantly, bulk-imported repository histories whose first commit touches an implausibly large fraction of files in an implausibly short window. This paper applies the same greater-than-80%-of-files-in-the-first-week heuristic from [6] that Avelino et al. use to filter such artifacts before founder identification.

**Succession outside software.** Ahn's study of 64 matched pairs of surviving and delisted Korean founder-led firms finds that founder-succession characteristics -- including how authority was transferred -- are associated with long-term post-succession survival independent of firm size at the time of transition [8], structurally paralleling the diffused-versus-concentrated-authority distinction this paper operationalizes for open-source commit and file-ownership authority, now finally tested against real survival variance rather than a degenerate all-survivor sample.

# Method

The pipeline is unchanged from the prior iteration in its core mechanics -- the same reimplemented DOA / Truck-Factor / TFDD machinery [1, 2], the same pre-departure authority-diffusion measurement, and the same statistical test battery -- and this section summarizes it briefly before describing the one substantive change: a redesigned corpus-construction step built specifically to avoid conditioning candidate selection on present-day fame.

**Alias resolution, DOA, and TFDD detection.** Commit authors are collapsed to individuals via normalized email and GitHub-login matching. Cumulative-window DOA is computed year by year per file per author using the Fritz et al. weights as reused by Avelino et al. (FA = 3.293, DL = 1.098, AC = -1.017) [7, 1]. The yearly Truck-Factor set is the greedy minimal set of primary-DOA-owning developers whose removal leaves more than half of a project's files without a primary owner (a 0.5 coverage threshold). A TFDD is recorded the first time every developer in the current Truck-Factor set has made no commits for the validated twelve-month (365-day) abandoner threshold. Founder-only TFDDs are isolated under a strict rule (the departing set has size one and its sole member is the repository's first human committer) and, separately, under a relaxed rule that admits a small number of additional founder-identification edge cases; first commits touching more than 80% of files within the first week are excluded as bulk-import artifacts, following [6].

**Pre-departure authority diffusion and survival outcome.** For each founder-only TFDD, the pipeline computes, over a pre-departure window (near boundary 180 days, far boundary 365 days before detachment), the founder's commit-share and the count of distinct non-founder accounts already holding primary DOA ownership on at least one file. Post-TFDD survival is scored over an 18-month (548-day) window, following Avelino et al.'s Active/Inactive grading collapsed to a binary flag.

**Statistical tests.** Four analyses run on the founder-only-TFDD subset: (1) a matched-pairs bootstrap comparing high- versus low-diffusion projects, matched on size and language; (2) Benjamini-Hochberg-corrected logistic regression of survival on diffusion predictors plus snapshot covariates (developers, stars, forks at TFDD), run separately under the strict founder rule (n=16) and the relaxed rule (n=20), alongside a snapshot-only baseline regression for direct comparison; (3) a placebo/window-relocation regression using a relocated pre-departure window in place of the true one, to check the true-window effect is not reproduced when the window itself is wrong; and (4) Cohen's-d effect sizes and a Mann-Whitney U test comparing diffusion predictors between the survivor and non-survivor groups directly, without a parametric model. All bootstrap resampling uses 5,000 draws with a fixed random seed (20260821) for reproducibility.

# Experimental Setup

**Corpus construction.** The corpus is built from a stratified sample across six languages (Python, JavaScript, Go, Java, Ruby, C++) and three star-count strata (50-500, 500-5,000, 5,000-100,000 stars), explicitly chosen so that candidate selection does not condition on a repository being currently popular or actively maintained -- the defect the prior iteration's corpus had. 270 repositories were sampled across this language-by-strata grid; each was cloned and its full commit history (SHA, author name and email, ISO timestamp, per-file insertion/deletion counts) extracted via `git log --numstat`, which is unauthenticated-rate-limit-free and therefore complete for every cloned repository. Candidates were required to have at least 1,095 days (3 years) of history to allow full pre- and post-TFDD windows without right-censoring, and were filtered to remove mining artifacts (bulk-import first commits, per [6]) and repositories without a single dominant early committer. Of the 270 sampled repositories, 69 survive filtering and are processed through the full DOA/Truck-Factor/TFDD pipeline.

**Founder-only TFDD sample and the outcome-variance fix.** Running the pipeline over the 69 processed repositories detects 16 founder-only TFDD events under the strict founder-identification rule and 20 under the relaxed rule -- roughly three to four times the prior iteration's 5 complete founder-only events, and, more importantly, no longer uniformly survivors. The strict-rule survival rate is 31.3% (5 of 16; standard error 0.120) and the relaxed-rule rate is 45.0% (9 of 20; standard error 0.114), both statistically consistent with Avelino et al.'s published 40.6% reference rate (128/315) [1] -- in sharp contrast to the prior iteration's corpus, whose 100% survival rate among 5 founder-only events differed from the same reference by a two-proportion z of 2.70 (p = 0.011). This is the corpus-construction fix working as intended: a sampling frame that does not select on present-day fame produces a founder-only-TFDD population whose survival rate lands inside the range a fame-independent published study reports, rather than at a boundary a survivorship-biased frame would predict.

**Baselines.** As in the prior iteration, the comparison is against Avelino et al.'s own published statistics [1] (TFDD incidence 16.3%, founder-only share 66%, 18-month survival 40.6%, snapshot Cohen's d = 0.13-0.26) rather than an external competing method, plus the same snapshot covariates (developers, stars, forks at TFDD) recomputed on this corpus's founder-only subset as the within-study baseline the diffusion predictors are compared against.

# Results

**Outcome variance is restored, and the corpus is now consistent with the published reference rate.** The central corpus-level result is that the defect identified in the prior iteration is fixed: strict-rule survival is 31.3% (SE 0.120) and relaxed-rule survival is 45.0% (SE 0.114) among 16 and 20 founder-only TFDD events respectively, both overlapping Avelino et al.'s published 40.6% reference rate (128/315) [1] rather than sitting at the prior corpus's degenerate 100%. This is the necessary precondition for every test in this section -- a matched-pairs comparison, a logistic regression, and a placebo test are all statistically undefined on a sample with zero outcome variance, which is exactly the state the prior corpus was in.

[FIGURE:fig2]

**The diffusion hypothesis, run for the first time on real outcome variance.** With outcome variance present, the logistic regression of survival on pre-departure diffusion predictors (founder commit-share, count of distinct non-founder DOA owners) plus snapshot covariates (log stars, log developers at TFDD) runs on n=16 (strict rule). Both diffusion coefficients point in the hypothesis-consistent direction -- founder share coefficient -5.56 (uncorrected p=0.426, BH-corrected p=0.60), diffused-owner-count coefficient -0.174 (uncorrected p=0.340, BH-corrected p=0.60) -- meaning higher founder concentration and fewer non-founder owners are associated with lower survival odds, as the hypothesis predicts. Neither reaches significance after correction, and the model's pseudo-R2 (0.175) is lower than the snapshot-only baseline model's (0.211, n=16, log-stars coefficient 1.40, uncorrected p=0.080), meaning the new diffusion predictors do not yet outperform the size-based covariates they were built to beat. The relaxed-rule regression (n=20) shows the same qualitative pattern at somewhat larger magnitude (founder-share coefficient -27.9, uncorrected p=0.150) but again does not survive correction (BH-corrected p=0.27), and its pseudo-R2 (0.500) is higher than the strict model's but computed on a different, less strictly defined event set.

The matched-pairs comparison -- pairing high- and low-diffusion projects on standardized log-stars, log-forks, and log-contributor-count within language -- finds zero eligible pairs at either founder-identification rule (n_pairs=0), so the survival-rate-lift confidence interval this test was designed to report is undefined rather than null; 16-20 events split across six languages and two diffusion strata simply does not leave enough same-language, similarly-sized projects on both sides of the diffusion split to match.

A direct, model-free comparison -- Mann-Whitney U tests of founder commit-share and diffused-owner count between the survivor and non-survivor groups -- returns U=23.0, p=0.661 for founder share and U=17.5, p=0.279 for diffused-owner count (strict rule, n=16). Neither is significant. The snapshot-covariate Cohen's-d values computed on this corpus's founder-only subset are 0.053 (developers at TFDD), -0.371 (commits at TFDD), -0.774 (files at TFDD), -0.388 (founder-share), and -0.293 (diffused-owner count) -- larger in magnitude than Avelino et al.'s reported snapshot range of 0.13-0.26 for several covariates, but computed on a much smaller sample (16 versus their 315) and with signs that require careful reading given the different covariate definitions, so we report these as descriptive statistics rather than as evidence the effect is larger here.

[FIGURE:fig3]

**The placebo-window regression, and a disclosed evaluation-pipeline defect.** A placebo regression -- identical in form to the main regression but using a relocated (incorrect) pre-departure window in place of the true one -- runs on n=15 (one event lacks a valid placebo window) and finds a large, unstable founder-share coefficient (-164.5) with a p-value of essentially 1.0 after correction (0.9999), consistent with the placebo window carrying no real signal, as intended, though the instability of the coefficient itself at this sample size means this should be read as a sanity check rather than a precise estimate.

Beyond this within-experiment placebo check, this iteration's independent evaluation harness -- the component responsible for an out-of-pipeline placebo-window falsification test and a stratified robustness audit, run separately from the experiment code above as a check on it -- did not produce a usable result for this corpus. Its own machine-logged output records the cause exactly: the evaluation stage executed at a point when the upstream experiment artifact (`method_out.json`) had not yet been written, found only an empty in-progress scratch directory, and consequently marked every downstream check (placebo test, stratified robustness, pipeline-validity cross-check against Avelino et al., and regression calibration) `UNAVAILABLE`, returning an overall verdict of `UNDETERMINED_PIPELINE_GAP` rather than a false pass or a fabricated statistic. We confirmed independently that this is a timing defect rather than a data defect: the experiment's final results were written after the evaluation stage had already run and exited. We report this rather than omit it, re-run the evaluation informally against a synthetic stand-in dataset to confirm the evaluation code itself is functional when given complete input (verdict PASS, one minor gap flagged, on that synthetic run), and specify the fix in the Discussion below: the evaluation stage needs to wait on, rather than race, the experiment stage's completion signal before this corpus's placebo and robustness results can be independently audited.

# Discussion

**What this iteration demonstrates.** The specific defect the prior iteration identified -- a corpus that structurally cannot contain a non-surviving founder-only TFDD event because it selects candidates by present-day fame -- is fixed by a stratified, fame-independent sampling frame, and the fix is demonstrated by the statistic that actually mattered: survival rate among founder-only events moved from a degenerate 100% to 31.3-45.0%, statistically consistent with Avelino et al.'s own published 40.6% reference rate. This is not a claim that the new corpus is a perfect random sample of the population Avelino et al. studied -- it is smaller (69 processed repositories versus their 1,932) and built under different constraints -- but it removes the specific mechanism (selection on present-day survival) that made the prior corpus's TFDD and survival rates provably inconsistent with the reference population at high confidence.

**Why the hypothesis is still untested, and why that is now an ordinary power problem rather than a structural one.** With outcome variance restored, every test the diffusion hypothesis needs can finally run, and every one of them ran. None reached significance: the regression coefficients point the right direction but do not survive multiple-comparison correction at n=16-20, the matched-pairs test cannot construct eligible pairs at this sample size, and the model-free Mann-Whitney comparison finds no difference between survivors and non-survivors on either diffusion predictor. This is qualitatively different from the prior iteration's result. There, the test could not be run at all, for a reason (zero outcome variance) that no larger sample from the same flawed frame would fix. Here, the test ran and did not find a significant effect, at a sample size (16-20 events) that is an order of magnitude below what a matched-pairs test with moderate effect size would need to detect -- the prior iteration's own power analysis specified roughly 40 founder-only events as the target, and this corpus reaches 40-50% of that target. A non-significant result at 40-50% of the specified power is evidence of insufficient power first and evidence about the hypothesis only weakly, and we report it as such rather than treating the hypothesis-consistent sign of the coefficients as partial confirmation or the lack of significance as disconfirmation.

**The evaluation-pipeline defect, and why it is reported separately from the scientific result.** The independent evaluation harness's failure to produce a robustness or placebo audit for this corpus is a software-engineering defect -- a race condition between two pipeline stages -- not a finding about the diffusion hypothesis, and conflating the two would misrepresent both. We verified the evaluation code is functional on complete input (a synthetic dry run passes) and that the specific failure mode is exactly what its own logs report: it ran before the experiment stage finished writing its output. This is a fixable sequencing bug; it does not retroactively call into question the experiment-stage results reported above, which were computed by different code, run to completion, and cross-checked internally (the placebo regression within the experiment code, as distinct from the evaluation harness's separate placebo audit, did complete and is reported above).

**Limitations.** Beyond statistical power, four further limitations bound how these results should be read. First, the 69-repository processed corpus, while stratified across six languages and three star strata by design, is still small relative to Avelino et al.'s 1,932-repository frame, so its language and popularity composition may not match theirs closely enough to make every direct rate comparison exact rather than approximate. Second, the strict-versus-relaxed founder-identification rule produces materially different event sets (16 versus 20) and somewhat different regression coefficients, and this iteration does not have the sample size to determine which rule is the better-calibrated one against ground truth. Third, the evaluation harness's independent robustness and placebo audit did not run for this corpus, so several checks the prior iteration's methodology specifies -- founder-identification-heuristic sensitivity, an alias-resolution spot-check against live contributor data, and an age-at-TFDD confound check -- are unaudited here even though the underlying data would now support them at n=16-20, unlike the prior iteration's n=5. Fourth, the placebo regression within the experiment code itself runs on only 15 events and produces an unstable coefficient estimate, so its reassurance that the true-window effect is not an artifact of the regression machinery itself should be read as a sanity check rather than a precise falsification test.

# Conclusion

Two iterations into this line of work, the corpus-construction problem that made the founder-diffusion-predicts-survival hypothesis untestable is solved: a stratified, fame-independent sampling frame across six languages and three popularity strata produces a founder-only-TFDD population whose 31.3-45.0% survival rate is consistent with Avelino et al.'s own published 40.6% reference, in place of the prior iteration's degenerate 100%. With real outcome variance finally present, this paper runs, for the first time on real data, every test the hypothesis requires -- a Benjamini-Hochberg-corrected logistic regression, a matched-pairs comparison, and a model-free Mann-Whitney test -- and reports what they show rather than only whether they ran: coefficients pointing in the hypothesis-consistent direction that do not survive correction at n=16-20, a matched-pairs test with zero eligible pairs at this sample size, and no significant model-free difference between survivors and non-survivors. We also disclose, rather than omit, a genuine pipeline defect: this iteration's independent evaluation harness raced the experiment stage and produced no usable robustness audit for this corpus, a fixable sequencing bug distinct from the (separately reported, code-complete) experiment-stage results. The next step is now the ordinary one a first underpowered result calls for -- scale the same fame-independent sampling frame from 69 to several hundred processed repositories to reach the roughly 40-event target the original power analysis specified, and fix the evaluation race condition so the robustness and placebo audit this corpus's real outcome variance now supports can actually run -- rather than the structural fix, a new sampling frame entirely, that the prior iteration required.

</current_paper>

<reviewer_feedback>
Paper reviewer feedback from the previous iteration. Your strategy MUST address these critiques.
Prioritize major issues — these are the most impactful improvements to make.

- [MAJOR] (evidence) The paper's central hypothesis test (logistic regression, matched-pairs, Mann-Whitney) is run on n=16 (strict) / n=20 (relaxed) founder-only TFDD events, which the paper itself states is 40-50% of the ~40-event target specified by the prior iteration's own power analysis. None of the four statistical tests returns a significant or even a fully defined result (matched-pairs finds zero eligible pairs). As written, the paper cannot support any claim about whether founder authority diffusion predicts survival — the question posed in the introduction is left open, which is a major issue for a paper whose title contribution is 'the first execution of the full statistical test battery.'
  Action: Either (a) scale the corpus substantially (the stratified, fame-independent frame is documented and reusable, so scaling from 69 to 200-300+ processed repositories should be feasible) to approach the stated 40-event target before resubmission, or (b) explicitly reframe the paper's contribution and title/abstract around the corpus-construction fix and the methodological lesson (how to avoid survivorship bias in this kind of study), demoting the hypothesis test to a secondary, clearly-labeled 'first pass, underpowered' result rather than a headline contribution.
- [MAJOR] (evidence) There is an unreconciled discrepancy between the paper's reported corpus construction (270 sampled repositories, 6 languages, 69 processed) and the supplementary GEN_ART dataset artifact (121 repositories sampled via GitHub REST search API, 4 languages, 34 founder-only-TFDD candidates, different star strata: 100-1k/1k-10k/10k+ vs. the paper's 50-500/500-5,000/5,000-100,000). The experiment artifact (art_4CZ-9Ou1G5ty) does match the paper's 270/69/16/20 numbers, suggesting the dataset artifact (art_ZbwYXh1VlhVp) may be a superseded or parallel attempt, but the paper never mentions this artifact or explains the relationship, leaving a reviewer unable to determine which corpus was actually used to produce the reported statistics.
  Action: Add a sentence in Experimental Setup clarifying the relationship between the two corpus-construction efforts (e.g., 'an earlier 121-repository pilot corpus, described in [artifact], was superseded by the 270-repository stratified frame reported here because...'), or remove/update the stale dataset artifact if it is not the one underlying the reported results, so the supplementary materials do not contradict the paper's numbers.
- [MAJOR] (methodology) The Related Work section flags a direct empirical tension with Medappa et al. (2019), who find that higher proportions of contributors with write access reduce survival — the opposite direction from this paper's hypothesis-consistent (negative, i.e., protective) diffusion coefficients. The paper acknowledges this tension exists but does not attempt to reconcile it (e.g., via differing time-scales, static vs. pre-departure-dynamic measurement, or differing dependent variables) beyond noting that the current regression 'neither resolve[s] nor deepen[s]' it. For a paper whose whole premise is that diffusion is protective, an unreconciled contradictory finding from a well-powered study (5,762 projects) in the closest prior work is a significant threat to the paper's motivating claim.
  Action: Add a paragraph in Discussion (not just Related Work) directly engaging with why Medappa et al.'s static write-access-ratio measure might diverge from a founder-specific, pre-departure-window diffusion measure — e.g., hypothesize that diffusion is protective specifically when it happens shortly before a departure event (succession-planning signal) versus destabilizing when present as a permanent structural feature (coordination-cost mechanism), and note this as a testable distinction for future work rather than leaving the contradiction unaddressed.
- [MINOR] (rigor) The paper reports Cohen's-d values for snapshot covariates on the new 16-event corpus (e.g., -0.774 for files at TFDD) as 'larger in magnitude' than Avelino et al.'s 0.13-0.26 range, but Avelino et al.'s effect sizes were computed on 315 events versus this paper's 16, so the comparison is essentially uninformative (a d of -0.774 on n=16 per group has an enormous confidence interval that likely spans zero and well beyond Avelino et al.'s range). The paper does hedge this appropriately in one sentence but the numbers are still presented prominently in the Results section in a way that risks being over-read.
  Action: Report confidence intervals (or at minimum standard errors) alongside each Cohen's-d value in the Results paragraph, not just the caveat sentence, so a reader can immediately see the interval likely contains Avelino et al.'s reference range rather than having to infer this from prose.
- [MINOR] (clarity) The paper reuses near-identical phrasing ('degenerate 100%', 'ordinary power problem rather than a structural one', 'the corpus-construction problem is solved') across the Introduction, Results, Discussion, and Conclusion sections. This repetition inflates the paper's apparent length without adding information and can read as an attempt to compensate rhetorically for the underpowered central result.
  Action: Deduplicate: state the corpus-fix statistic prominently once in Results, and in later sections refer back to it briefly ('as shown above') rather than re-deriving the same sentence. Redirect the saved space to a fuller power/sample-size analysis or an expanded limitations discussion of the strict-vs-relaxed founder-rule sensitivity.
- [MINOR] (scope) The paper does not report what fraction of the 270 sampled repositories were excluded at each filtering stage (age/size threshold, mining-artifact removal, single-dominant-committer requirement) or discuss whether these filters could themselves reintroduce a selection bias relevant to the survival outcome (e.g., requiring 'a single dominant early committer' could disproportionately exclude certain project structures that correlate with the very diffusion pattern being studied).
  Action: Add a filtering funnel table (sampled -> excluded for insufficient history -> excluded for mining artifacts -> excluded for no dominant founder -> final 69) with counts at each stage, and add one sentence addressing whether the 'single dominant early committer' filter could itself correlate with eventual diffusion outcomes, since this determines corpus eligibility before the diffusion measurement is even taken.
- [MINOR] (novelty) The paper does not clearly state whether a stratified, popularity-independent sampling frame for OSS abandonment/survival studies has been used before in this specific literature (e.g., in Nourry et al.'s 36,000-project re-examination of TFDD, or elsewhere); if such designs are already standard practice for avoiding survivorship bias in software-engineering mining studies, the corpus-construction contribution is less novel than the framing implies.
  Action: Add one sentence in Related Work or Method explicitly comparing the sampling strategy here to Nourry et al.'s (36,000-project) sampling approach — do they condition on present popularity or not? — to substantiate or temper the novelty claim around the fame-independent frame.
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

### [3] HUMAN-USER prompt · 2026-08-21 19:43:14 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [4] TOOL CALL — Write · 2026-08-21 19:43:50 UTC

```
File: /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json

{
  "strategies": [
    {
      "title": "Scale the Corpus, Test Diffusion vs Medappa",
      "objective": "Take the founder-diffusion-predicts-survival test from an underpowered 16-20-event first pass to a scale (target 200-300 processed repositories) that can plausibly reach significance, fix the evaluation race condition so the placebo/robustness audit actually runs, and directly adjudicate the Medappa et al. tension by testing whether diffusion timing (pre-departure vs permanent) is what determines its sign.",
      "rationale": "The reviewer's MAJOR points converge on one root cause: n=16-20 is too small to settle anything, and the paper does not reconcile its hypothesis-consistent-but-null coefficients against Medappa et al.'s well-powered opposite-sign finding. Both are fixable with the reusable stratified frame already validated last iteration -- it just needs to run at 3-5x scale, with the funnel reported transparently (reviewer MINOR) and an explicit test isolating whether diffusion's protective sign depends on WHEN it occurs (shortly before departure, a succession-planning signal) versus being a permanent structural ratio (Medappa's coordination-cost measure). This also finally lets the existing but never-executed evaluation harness run against complete data, producing the placebo/stratified-robustness/calibration results the paper currently lacks entirely.",
      "artifact_directions": [
        {
          "type": "dataset",
          "objective": "Scale the fame-independent, stratified GitHub corpus from 69 to 200-300+ processed repositories using the exact same six-language x three-star-strata sampling frame validated last iteration, with a fully transparent filtering funnel.",
          "approach": "Reuse the prior iteration's sampling design (Python, JavaScript, Go, Java, Ruby, C++ x 50-500/500-5,000/5,000-100,000 stars) but widen the initial GitHub search sample substantially (target ~800-1200 candidates, budgeting for the same ~25% pass-rate observed at 270->69) so post-filter processed repos land in the 200-300 range. Reuse `git log --numstat` cloning (no API rate-limit bottleneck) and the same exclusion criteria (>=1,095 days history, bulk-import artifact detection at >80% files touched in week 1 per Kalliamvakou et al., single-dominant-early-committer requirement). Record and output a per-stage filtering funnel table (sampled -> excluded-insufficient-history -> excluded-mining-artifact -> excluded-no-dominant-founder -> final processed count), broken out by language and star stratum, as first-class output fields -- not just a summary count -- directly resolving the reviewer's funnel-transparency ask. Additionally tag each retained repo with metadata needed for the reconciliation test in the experiment artifact: total historical tenure of write-access grantees and the timing of write-access grants relative to founder TFDD, so the downstream experiment can distinguish 'permanent write-access ratio' (Medappa's construct) from 'pre-departure diffusion window' (this hypothesis's construct) on the same repos rather than needing a second corpus.",
          "depends_on": [
            {"id": "art_ZbwYXh1VlhVp", "label": "prior corpus"}
          ]
        },
        {
          "type": "experiment",
          "objective": "Re-run the DOA/Truck-Factor/TFDD/survival pipeline and the full diffusion-predicts-survival statistical battery on the scaled corpus, and add a new explicit test that adjudicates the Medappa et al. tension by comparing a pre-departure-window diffusion measure against a permanent/whole-history write-access-ratio measure as competing predictors in the same model.",
          "approach": "Apply the identical, already-validated DOA/TF/TFDD/diffusion/survival code from the prior experiment artifact to the scaled corpus, targeting 40+ founder-only strict TFDD events (and a correspondingly larger relaxed set) to approach the power analysis's stated target. Re-run the BH-corrected logistic regression, matched-pairs bootstrap (now with enough same-language/size-bucket density to actually form matched pairs), and Mann-Whitney tests at this larger n. Add the reconciliation test: construct, per founder-only-TFDD project, both (a) this study's pre-departure (6-12 month) diffusion score and (b) a Medappa-style permanent write-access ratio computed over the project's FULL pre-TFDD history (proportion of all-time contributors ever reaching DOA file-ownership, not windowed), then fit a joint regression with both predictors plus an interaction/timing term (e.g. whether diffusion accrued mostly within vs. outside the pre-departure window) to test whether it is specifically the TIMING of diffusion, not diffusion's mere presence, that flips its association with survival from Medappa's negative to this hypothesis's proposed positive. Report power/sample-size context explicitly (achieved n vs. the ~40-event target) and report Cohen's-d values for snapshot covariates together with bootstrap confidence intervals, not as bare point estimates, per the reviewer's MINOR note.",
          "depends_on": [
            {"id": "art_4CZ-9Ou1G5ty", "label": "prior pipeline"}
          ]
        },
        {
          "type": "evaluation",
          "objective": "Run the placebo-window falsification test and stratified robustness audit against the complete, scaled experiment output (fixing the previously disclosed race condition), and add a power/sensitivity analysis quantifying how close the scaled result comes to a well-powered test.",
          "approach": "Re-invoke the existing, already-implemented eval.py logic (validated functional in a synthetic dry run last iteration) against the new scaled experiment artifact's completed method_out.json, ensuring sequencing so the evaluation only runs after the experiment has fully written its output, eliminating the previously disclosed race condition. Report placebo_test, stratified_robustness (by language and popularity bucket, now with enough n per stratum to be meaningful), pipeline_validity cross-check against Avelino et al.'s published aggregate rates, and calibration (bootstrap CIs, Brier score, AUC) at the new sample size. Add a dedicated power/sensitivity analysis: given the achieved effect sizes and n, compute the minimum detectable effect at 80% power and compare it against the observed coefficients, so the paper can state precisely whether the scaled result is adequately powered, still underpowered by a quantifiable margin, or has in fact crossed into significance -- replacing the previous iteration's qualitative '40-50% of target' claim with an exact number.",
          "depends_on": [
            {"id": "art_wWTWRqndgmX9", "label": "prior eval harness"}
          ]
        }
      ],
      "expected_outcome": "A 200-300+ repository scaled corpus with a transparent filtering funnel; a rerun of the full diffusion-predicts-survival statistical battery at meaningfully higher power, plus a new joint model that directly tests whether pre-departure-window timing (not mere diffusion) reconciles this hypothesis's protective sign with Medappa et al.'s opposite-sign permanent-ratio finding; and a completed (no longer race-blocked) placebo/robustness/calibration audit with an exact power analysis -- together either producing the paper's first significant result or, if still null, a precisely quantified and much stronger-powered null that closes the major open reviewer concerns.",
      "summary": "Scale the validated fame-independent corpus 3-5x, rerun the hypothesis test battery at real power, fix the evaluation race condition, and add a direct timing-based reconciliation of this hypothesis's diffusion signal against Medappa et al.'s contrary finding."
    }
  ]
}
```

### [5] TOOL RESULT — Write · 2026-08-21 19:43:50 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"strategies\": [\n    {\n      \"title\": \"Scale the Corpus, Test Diffusion vs Medappa\",\n      \"objective\": \"Take the founder-diffusion-predicts-survival test from an underpowered 16-20-event first pass to a scale (target 200-300 processed repositories) that can plausibly reach significance, fix the evaluation race condition so the placebo/robustness audit actually runs, and directly adjudicate the Medappa et al. tension by testing whether diffusion timing (pre-departure vs permanent) is what determines its sign.\",\n      \"rationale\": \"The reviewer's MAJOR points converge on one root cause: n=16-20 is too small to settle anything, and the paper does not reconcile its hypothesis-consistent-but-null coefficients against Medappa et al.'s well-powered opposite-sign finding. Both are fixable with the reusable stratified frame already validated last iteration -- it just needs to run at 3-5x scale, with the funnel reported transparently (reviewer MINOR) and an explicit test isolating whether diffusion's protective sign depends on WHEN it occurs (shortly before departure, a succession-planning signal) versus being a permanent structural ratio (Medappa's coordination-cost measure). This also finally lets the existing but never-executed evaluation harness run against complete data, producing the placebo/stratified-robustness/calibration results the paper currently lacks entirely.\",\n      \"artifact_directions\": [\n        {\n          \"type\": \"dataset\",\n          \"objective\": \"Scale the fame-independent, stratified GitHub corpus from 69 to 200-300+ processed repositories using the exact same six-language x three-star-strata sampling frame validated last iteration, with a fully transparent filtering funnel.\",\n          \"approach\": \"Reuse the prior iteration's sampling design (Python, JavaScript, Go, Java, Ruby, C++ x 50-500/500-5,000/5,000-100,000 stars) but widen the initial GitHub search sample substantially (target ~800-1200 candidates, budgeting for the same ~25% pass-rate observed at 270->69) so post-filter processed repos land in the 200-300 range. Reuse `git log --numstat` cloning (no API rate-limit bottleneck) and the same exclusion criteria (>=1,095 days history, bulk-import artifact detection at >80% files touched in week 1 per Kalliamvakou et al., single-dominant-early-committer requirement). Record and output a per-stage filtering funnel table (sampled -> excluded-insufficient-history -> excluded-mining-artifact -> excluded-no-dominant-founder -> final processed count), broken out by language and star stratum, as first-class output fields -- not just a summary count -- directly resolving the reviewer's funnel-transparency ask. Additionally tag each retained repo with metadata needed for the reconciliation test in the experiment artifact: total historical tenure of write-access grantees and the timing of write-access grants relative to founder TFDD, so the downstream experiment can distinguish 'permanent write-access ratio' (Medappa's construct) from 'pre-departure diffusion window' (this hypothesis's construct) on the same repos rather than needing a second corpus.\",\n          \"depends_on\": [\n            {\"id\": \"art_ZbwYXh1VlhVp\", \"label\": \"prior corpus\"}\n          ]\n        },\n        {\n          \"type\": \"experiment\",\n          \"objective\": \"Re-run the DOA/Truck-Factor/TFDD/survival pipeline and the full diffusion-predicts-survival statistical battery on the scaled corpus, and add a new explicit test that adjudicates the Medappa et al. tension by comparing a pre-departure-window diffusion measure against a permanent/whole-history write-access-ratio measure as competing predictors in the same model.\",\n          \"approach\": \"Apply the identical, already-validated DOA/TF/TFDD/diffusion/survival code from the prior experiment artifact to the scaled corpus, targeting 40+ founder-only strict TFDD events (and a correspondingly larger relaxed set) to approach the power analysis's stated target. Re-run the BH-corrected logistic regression, matched-pairs bootstrap (now with enough same-language/size-bucket density to actually form matched pairs), and Mann-Whitney tests at this larger n. Add the reconciliation test: construct, per founder-only-TFDD project, both (a) this study's pre-departure (6-12 month) diffusion score and (b) a Medappa-style permanent write-access ratio computed over the project's FULL pre-TFDD history (proportion of all-time contributors ever reaching DOA file-ownership, not windowed), then fit a joint regression with both predictors plus an interaction/timing term (e.g. whether diffusion accrued mostly within vs. outside the pre-departure window) to test whether it is specifically the TIMING of diffusion, not diffusion's mere presence, that flips its association with survival from Medappa's negative to this hypothesis's proposed positive. Report power/sample-size context explicitly (achieved n vs. the ~40-event target) and report Cohen's-d values for snapshot covariates together with bootstrap confidence intervals, not as bare point estimates, per the reviewer's MINOR note.\",\n          \"depends_on\": [\n            {\"id\": \"art_4CZ-9Ou1G5ty\", \"label\": \"prior pipeline\"}\n          ]\n        },\n        {\n          \"type\": \"evaluation\",\n          \"objective\": \"Run the placebo-window falsification test and stratified robustness audit against the complete, scaled experiment output (fixing the previously disclosed race condition), and add a power/sensitivity analysis quantifying how close the scaled result comes to a well-powered test.\",\n          \"approach\": \"Re-invoke the existing, already-implemented eval.py logic (validated functional in a synthetic dry run last iteration) against the new scaled experiment artifact's completed method_out.json, ensuring sequencing so the evaluation only runs after the experiment has fully written its output, eliminating the previously disclosed race condition. Report placebo_test, stratified_robustness (by language and popularity bucket, now with enough n per stratum to be meaningful), pipeline_validity cross-check against Avelino et al.'s published aggregate rates, and calibration (bootstrap CIs, Brier score, AUC) at the new sample size. Add a dedicated power/sensitivity analysis: given the achieved effect sizes and n, compute the minimum detectable effect at 80% power and compare it against the observed coefficients, so the paper can state precisely whether the scaled result is adequately powered, still underpowered by a quantifiable margin, or has in fact crossed into significance -- replacing the previous iteration's qualitative '40-50% of target' claim with an exact number.\",\n          \"depends_on\": [\n            {\"id\": \"art_wWTWRqndgmX9\", \"label\": \"prior eval harness\"}\n          ]\n        }\n      ],\n      \"expected_outcome\": \"A 200-300+ repository scaled corpus with a transparent filtering funnel; a rerun of the full diffusion-predicts-survival statistical battery at meaningfully higher power, plus a new joint model that directly tests whether pre-departure-window timing (not mere diffusion) reconciles this hypothesis's protective sign with Medappa et al.'s opposite-sign permanent-ratio finding; and a completed (no longer race-blocked) placebo/robustness/calibration audit with an exact power analysis -- together either producing the paper's first significant result or, if still null, a precisely quantified and much stronger-powered null that closes the major open reviewer concerns.\",\n      \"summary\": \"Scale the validated fame-independent corpus 3-5x, rerun the hypothesis test battery at real power, fix the evaluation race condition, and add a direct timing-based reconciliation of this hypothesis's diffusion signal against Medappa et al.'s contrary finding.\"\n    }\n  ]\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [6] ASSISTANT · 2026-08-21 19:43:51 UTC

```
Strategy written to `.terminal_claude_agent_struct_out.json`: scale the corpus to 200-300+ repos, rerun the full statistical battery at higher power, fix the evaluation race condition, and add a timing-based test reconciling the diffusion hypothesis with Medappa et al.'s opposite-sign finding.
```

### [7] SYSTEM-USER prompt · 2026-08-21 19:43:54 UTC

```
<verification_results>
Your previous response had issues that need fixing:

DEPENDENCY ERRORS (depends_on can ONLY reference IDs from <existing_artifacts>):
  - Strategy 1: Artifact 'dataset_iter2_dir1' (dataset): dependency 'art_ZbwYXh1VlhVp' has type 'dataset' which is not allowed (allowed: {'research'})
  - Strategy 1: Artifact 'experiment_iter2_dir2' (experiment): dependency 'art_4CZ-9Ou1G5ty' has type 'experiment' which is not allowed (allowed: {'research', 'dataset'})
  - Strategy 1: Artifact 'experiment_iter2_dir2' (experiment): missing required dependency. Must have at least one dependency of type: {'dataset'}
  - Strategy 1: Artifact 'evaluation_iter2_dir3' (evaluation): dependency 'art_wWTWRqndgmX9' has type 'evaluation' which is not allowed (allowed: {'experiment', 'dataset'})
  - Strategy 1: Artifact 'evaluation_iter2_dir3' (evaluation): missing required dependency. Must have at least one dependency of type: {'experiment'}

INSUFFICIENT VALID ARTIFACTS:
  Required: at least 1 valid artifacts
  Found: 0 valid out of 3 total
  Artifacts with invalid types, duplicate IDs, or invalid dependencies don't count as valid.

</verification_results>

<task>
Fix ALL issues above and regenerate your strategies:

1. Fix dependency errors:
   - depends_on is a list of {id, label} objects — every entry MUST have a non-empty short label
   - id can ONLY reference IDs from <existing_artifacts>
   - You CANNOT reference artifacts you are proposing in this strategy as dependencies (they all run in parallel)
   - Follow the dependency type rules (e.g., experiments require datasets)
   - If no suitable existing artifacts exist, use depends_on: []
2. Ensure at least 1 artifacts are fully valid (correct types, no ID conflicts, valid dependencies)

Output the corrected JSON with the fixed strategies.
</task>
```

### [8] TOOL CALL — Edit · 2026-08-21 19:44:17 UTC

```
File: /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json
OLD:           "depends_on": [
            {"id": "art_ZbwYXh1VlhVp", "label": "prior corpus"}
          ]
        },
        {
          "type": "experiment",
          "objective": "Re-run the DOA/Truck-Factor/TFDD/survival pipeline and the full diffusion-predicts-survival statistical battery on the scaled corpus, and add a new explicit test that adjudicates the Medappa et al. tension by comparing a pre-departure-window diffusion measure against a permanent/whole-history write-access-ratio measure as competing predictors in the same model.",
          "approach": "Apply the identical, already-validated DOA/TF/TFDD/diffusion/survival code from the prior experiment artifact to the scaled corpus, targeting 40+ founder-only strict TFDD events (and a correspondingly larger relaxed set) to approach the power analysis's stated target. Re-run the BH-corrected logistic regression, matched-pairs bootstrap (now with enough same-language/size-bucket density to actually form matched pairs), and Mann-Whitney tests at this larger n. Add the reconciliation test: construct, per founder-only-TFDD project, both (a) this study's pre-departure (6-12 month) diffusion score and (b) a Medappa-style permanent write-access ratio computed over the project's FULL pre-TFDD history (proportion of all-time contributors ever reaching DOA file-ownership, not windowed), then fit a joint regression with both predictors plus an interaction/timing term (e.g. whether diffusion accrued mostly within vs. outside the pre-departure window) to test whether it is specifically the TIMING of diffusion, not diffusion's mere presence, that flips its association with survival from Medappa's negative to this hypothesis's proposed positive. Report power/sample-size context explicitly (achieved n vs. the ~40-event target) and report Cohen's-d values for snapshot covariates together with bootstrap confidence intervals, not as bare point estimates, per the reviewer's MINOR note.",
          "depends_on": [
            {"id": "art_4CZ-9Ou1G5ty", "label": "prior pipeline"}
          ]
        },
        {
          "type": "evaluation",
          "objective": "Run the placebo-window falsification test and stratified robustness audit against the complete, scaled experiment output (fixing the previously disclosed race condition), and add a power/sensitivity analysis quantifying how close the scaled result comes to a well-powered test.",
          "approach": "Re-invoke the existing, already-implemented eval.py logic (validated functional in a synthetic dry run last iteration) against the new scaled experiment artifact's completed method_out.json, ensuring sequencing so the evaluation only runs after the experiment has fully written its output, eliminating the previously disclosed race condition. Report placebo_test, stratified_robustness (by language and popularity bucket, now with enough n per stratum to be meaningful), pipeline_validity cross-check against Avelino et al.'s published aggregate rates, and calibration (bootstrap CIs, Brier score, AUC) at the new sample size. Add a dedicated power/sensitivity analysis: given the achieved effect sizes and n, compute the minimum detectable effect at 80% power and compare it against the observed coefficients, so the paper can state precisely whether the scaled result is adequately powered, still underpowered by a quantifiable margin, or has in fact crossed into significance -- replacing the previous iteration's qualitative '40-50% of target' claim with an exact number.",
          "depends_on": [
            {"id": "art_wWTWRqndgmX9", "label": "prior eval harness"}
          ]
        }
NEW:           "depends_on": []
        },
        {
          "type": "experiment",
          "objective": "Re-run the DOA/Truck-Factor/TFDD/survival pipeline and the full diffusion-predicts-survival statistical battery on the scaled corpus, and add a new explicit test that adjudicates the Medappa et al. tension by comparing a pre-departure-window diffusion measure against a permanent/whole-history write-access-ratio measure as competing predictors in the same model.",
          "approach": "Apply the identical, already-validated DOA/TF/TFDD/diffusion/survival code from the prior experiment artifact to the scaled corpus, targeting 40+ founder-only strict TFDD events (and a correspondingly larger relaxed set) to approach the power analysis's stated target. Re-run the BH-corrected logistic regression, matched-pairs bootstrap (now with enough same-language/size-bucket density to actually form matched pairs), and Mann-Whitney tests at this larger n. Add the reconciliation test: construct, per founder-only-TFDD project, both (a) this study's pre-departure (6-12 month) diffusion score and (b) a Medappa-style permanent write-access ratio computed over the project's FULL pre-TFDD history (proportion of all-time contributors ever reaching DOA file-ownership, not windowed), then fit a joint regression with both predictors plus an interaction/timing term (e.g. whether diffusion accrued mostly within vs. outside the pre-departure window) to test whether it is specifically the TIMING of diffusion, not diffusion's mere presence, that flips its association with survival from Medappa's negative to this hypothesis's proposed positive. Report power/sample-size context explicitly (achieved n vs. the ~40-event target) and report Cohen's-d values for snapshot covariates together with bootstrap confidence intervals, not as bare point estimates, per the reviewer's MINOR note.",
          "depends_on": [
            {"id": "art_ZbwYXh1VlhVp", "label": "prior corpus"}
          ]
        },
        {
          "type": "evaluation",
          "objective": "Run the placebo-window falsification test and stratified robustness audit against the complete, scaled experiment output (fixing the previously disclosed race condition), and add a power/sensitivity analysis quantifying how close the scaled result comes to a well-powered test.",
          "approach": "Re-invoke the existing, already-implemented eval.py logic (validated functional in a synthetic dry run last iteration) against the new scaled experiment artifact's completed method_out.json, ensuring sequencing so the evaluation only runs after the experiment has fully written its output, eliminating the previously disclosed race condition. Report placebo_test, stratified_robustness (by language and popularity bucket, now with enough n per stratum to be meaningful), pipeline_validity cross-check against Avelino et al.'s published aggregate rates, and calibration (bootstrap CIs, Brier score, AUC) at the new sample size. Add a dedicated power/sensitivity analysis: given the achieved effect sizes and n, compute the minimum detectable effect at 80% power and compare it against the observed coefficients, so the paper can state precisely whether the scaled result is adequately powered, still underpowered by a quantifiable margin, or has in fact crossed into significance -- replacing the previous iteration's qualitative '40-50% of target' claim with an exact number.",
          "depends_on": [
            {"id": "art_4CZ-9Ou1G5ty", "label": "prior pipeline"},
            {"id": "art_ZbwYXh1VlhVp", "label": "prior corpus"}
          ]
        }
```

### [9] TOOL RESULT — Edit · 2026-08-21 19:44:17 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "oldString": "          \"depends_on\": [\n            {\"id\": \"art_ZbwYXh1VlhVp\", \"label\": \"prior corpus\"}\n          ]\n        },\n        {\n          \"type\": \"experiment\",\n          \"objective\": \"Re-run the DOA/Truck-Factor/TFDD/survival pipeline and the full diffusion-predicts-survival statistical battery on the scaled corpus, and add a new explicit test that adjudicates the Medappa et al. tension by comparing a pre-departure-window diffusion measure against a permanent/whole-history write-access-ratio measure as competing predictors in the same model.\",\n          \"approach\": \"Apply the identical, already-validated DOA/TF/TFDD/diffusion/survival code from the prior experiment artifact to the scaled corpus, targeting 40+ founder-only strict TFDD events (and a correspondingly larger relaxed set) to approach the power analysis's stated target. Re-run the BH-corrected logistic regression, matched-pairs bootstrap (now with enough same-language/size-bucket density to actually form matched pairs), and Mann-Whitney tests at this larger n. Add the reconciliation test: construct, per founder-only-TFDD project, both (a) this study's pre-departure (6-12 month) diffusion score and (b) a Medappa-style permanent write-access ratio computed over the project's FULL pre-TFDD history (proportion of all-time contributors ever reaching DOA file-ownership, not windowed), then fit a joint regression with both predictors plus an interaction/timing term (e.g. whether diffusion accrued mostly within vs. outside the pre-departure window) to test whether it is specifically the TIMING of diffusion, not diffusion's mere presence, that flips its association with survival from Medappa's negative to this hypothesis's proposed positive. Report power/sample-size context explicitly (achieved n vs. the ~40-event target) and report Cohen's-d values for snapshot covariates together with bootstrap confidence intervals, not as bare point estimates, per the reviewer's MINOR note.\",\n          \"depends_on\": [\n            {\"id\": \"art_4CZ-9Ou1G5ty\", \"label\": \"prior pipeline\"}\n          ]\n        },\n        {\n          \"type\": \"evaluation\",\n          \"objective\": \"Run the placebo-window falsification test and stratified robustness audit against the complete, scaled experiment output (fixing the previously disclosed race condition), and add a power/sensitivity analysis quantifying how close the scaled result comes to a well-powered test.\",\n          \"approach\": \"Re-invoke the existing, already-implemented eval.py logic (validated functional in a synthetic dry run last iteration) against the new scaled experiment artifact's completed method_out.json, ensuring sequencing so the evaluation only runs after the experiment has fully written its output, eliminating the previously disclosed race condition. Report placebo_test, stratified_robustness (by language and popularity bucket, now with enough n per stratum to be meaningful), pipeline_validity cross-check against Avelino et al.'s published aggregate rates, and calibration (bootstrap CIs, Brier score, AUC) at the new sample size. Add a dedicated power/sensitivity analysis: given the achieved effect sizes and n, compute the minimum detectable effect at 80% power and compare it against the observed coefficients, so the paper can state precisely whether the scaled result is adequately powered, still underpowered by a quantifiable margin, or has in fact crossed into significance -- replacing the previous iteration's qualitative '40-50% of target' claim with an exact number.\",\n          \"depends_on\": [\n            {\"id\": \"art_wWTWRqndgmX9\", \"label\": \"prior eval harness\"}\n          ]\n        }", "newString": "          \"depends_on\": []\n        },\n        {\n          \"type\": \"experiment\",\n          \"objective\": \"Re-run the DOA/Truck-Factor/TFDD/survival pipeline and the full diffusion-predicts-survival statistical battery on the scaled corpus, and add a new explicit test that adjudicates the Medappa et al. tension by comparing a pre-departure-window diffusion measure against a permanent/whole-history write-access-ratio measure as competing predictors in the same model.\",\n          \"approach\": \"Apply the identical, already-validated DOA/TF/TFDD/diffusion/survival code from the prior experiment artifact to the scaled corpus, targeting 40+ founder-only strict TFDD events (and a correspondingly larger relaxed set) to approach the power analysis's stated target. Re-run the BH-corrected logistic regression, matched-pairs bootstrap (now with enough same-language/size-bucket density to actually form matched pairs), and Mann-Whitney tests at this larger n. Add the reconciliation test: construct, per founder-only-TFDD project, both (a) this study's pre-departure (6-12 month) diffusion score and (b) a Medappa-style permanent write-access ratio computed over the project's FULL pre-TFDD history (proportion of all-time contributors ever reaching DOA file-ownership, not windowed), then fit a joint regression with both predictors plus an interaction/timing term (e.g. whether diffusion accrued mostly within vs. outside the pre-departure window) to test whether it is specifically the TIMING of diffusion, not diffusion's mere presence, that flips its association with survival from Medappa's negative to this hypothesis's proposed positive. Report power/sample-size context explicitly (achieved n vs. the ~40-event target) and report Cohen's-d values for snapshot covariates together with bootstrap confidence intervals, not as bare point estimates, per the reviewer's MINOR note.\",\n          \"depends_on\": [\n            {\"id\": \"art_ZbwYXh1VlhVp\", \"label\": \"prior corpus\"}\n          ]\n        },\n        {\n          \"type\": \"evaluation\",\n          \"objective\": \"Run the placebo-window falsification test and stratified robustness audit against the complete, scaled experiment output (fixing the previously disclosed race condition), and add a power/sensitivity analysis quantifying how close the scaled result comes to a well-powered test.\",\n          \"approach\": \"Re-invoke the existing, already-implemented eval.py logic (validated functional in a synthetic dry run last iteration) against the new scaled experiment artifact's completed method_out.json, ensuring sequencing so the evaluation only runs after the experiment has fully written its output, eliminating the previously disclosed race condition. Report placebo_test, stratified_robustness (by language and popularity bucket, now with enough n per stratum to be meaningful), pipeline_validity cross-check against Avelino et al.'s published aggregate rates, and calibration (bootstrap CIs, Brier score, AUC) at the new sample size. Add a dedicated power/sensitivity analysis: given the achieved effect sizes and n, compute the minimum detectable effect at 80% power and compare it against the observed coefficients, so the paper can state precisely whether the scaled result is adequately powered, still underpowered by a quantifiable margin, or has in fact crossed into significance -- replacing the previous iteration's qualitative '40-50% of target' claim with an exact number.\",\n          \"depends_on\": [\n            {\"id\": \"art_4CZ-9Ou1G5ty\", \"label\": \"prior pipeline\"},\n            {\"id\": \"art_ZbwYXh1VlhVp\", \"label\": \"prior corpus\"}\n          ]\n        }", "originalFile": "{\n  \"strategies\": [\n    {\n      \"title\": \"Scale the Corpus, Test Diffusion vs Medappa\",\n      \"objective\": \"Take the founder-diffusion-predicts-survival test from an underpowered 16-20-event first pass to a scale (target 200-300 processed repositories) that can plausibly reach significance, fix the evaluation race condition so the placebo/robustness audit actually runs, and directly adjudicate the Medappa et al. tension by testing whether diffusion timing (pre-departure vs permanent) is what determines its sign.\",\n      \"rationale\": \"The reviewer's MAJOR points converge on one root cause: n=16-20 is too small to settle anything, and the paper does not reconcile its hypothesis-consistent-but-null coefficients against Medappa et al.'s well-powered opposite-sign finding. Both are fixable with the reusable stratified frame already validated last iteration -- it just needs to run at 3-5x scale, with the funnel reported transparently (reviewer MINOR) and an explicit test isolating whether diffusion's protective sign depends on WHEN it occurs (shortly before departure, a succession-planning signal) versus being a permanent structural ratio (Medappa's coordination-cost measure). This also finally lets the existing but never-executed evaluation harness run against complete data, producing the placebo/stratified-robustness/calibration results the paper currently lacks entirely.\",\n      \"artifact_directions\": [\n        {\n          \"type\": \"dataset\",\n          \"objective\": \"Scale the fame-independent, stratified GitHub corpus from 69 to 200-300+ processed repositories using the exact same six-language x three-star-strata sampling frame validated last iteration, with a fully transparent filtering funnel.\",\n          \"approach\": \"Reuse the prior iteration's sampling design (Python, JavaScript, Go, Java, Ruby, C++ x 50-500/500-5,000/5,000-100,000 stars) but widen the initial GitHub search sample substantially (target ~800-1200 candidates, budgeting for the same ~25% pass-rate observed at 270->69) so post-filter processed repos land in the 200-300 range. Reuse `git log --numstat` cloning (no API rate-limit bottleneck) and the same exclusion criteria (>=1,095 days history, bulk-import artifact detection at >80% files touched in week 1 per Kalliamvakou et al., single-dominant-early-committer requirement). Record and output a per-stage filtering funnel table (sampled -> excluded-insufficient-history -> excluded-mining-artifact -> excluded-no-dominant-founder -> final processed count), broken out by language and star stratum, as first-class output fields -- not just a summary count -- directly resolving the reviewer's funnel-transparency ask. Additionally tag each retained repo with metadata needed for the reconciliation test in the experiment artifact: total historical tenure of write-access grantees and the timing of write-access grants relative to founder TFDD, so the downstream experiment can distinguish 'permanent write-access ratio' (Medappa's construct) from 'pre-departure diffusion window' (this hypothesis's construct) on the same repos rather than needing a second corpus.\",\n          \"depends_on\": [\n            {\"id\": \"art_ZbwYXh1VlhVp\", \"label\": \"prior corpus\"}\n          ]\n        },\n        {\n          \"type\": \"experiment\",\n          \"objective\": \"Re-run the DOA/Truck-Factor/TFDD/survival pipeline and the full diffusion-predicts-survival statistical battery on the scaled corpus, and add a new explicit test that adjudicates the Medappa et al. tension by comparing a pre-departure-window diffusion measure against a permanent/whole-history write-access-ratio measure as competing predictors in the same model.\",\n          \"approach\": \"Apply the identical, already-validated DOA/TF/TFDD/diffusion/survival code from the prior experiment artifact to the scaled corpus, targeting 40+ founder-only strict TFDD events (and a correspondingly larger relaxed set) to approach the power analysis's stated target. Re-run the BH-corrected logistic regression, matched-pairs bootstrap (now with enough same-language/size-bucket density to actually form matched pairs), and Mann-Whitney tests at this larger n. Add the reconciliation test: construct, per founder-only-TFDD project, both (a) this study's pre-departure (6-12 month) diffusion score and (b) a Medappa-style permanent write-access ratio computed over the project's FULL pre-TFDD history (proportion of all-time contributors ever reaching DOA file-ownership, not windowed), then fit a joint regression with both predictors plus an interaction/timing term (e.g. whether diffusion accrued mostly within vs. outside the pre-departure window) to test whether it is specifically the TIMING of diffusion, not diffusion's mere presence, that flips its association with survival from Medappa's negative to this hypothesis's proposed positive. Report power/sample-size context explicitly (achieved n vs. the ~40-event target) and report Cohen's-d values for snapshot covariates together with bootstrap confidence intervals, not as bare point estimates, per the reviewer's MINOR note.\",\n          \"depends_on\": [\n            {\"id\": \"art_4CZ-9Ou1G5ty\", \"label\": \"prior pipeline\"}\n          ]\n        },\n        {\n          \"type\": \"evaluation\",\n          \"objective\": \"Run the placebo-window falsification test and stratified robustness audit against the complete, scaled experiment output (fixing the previously disclosed race condition), and add a power/sensitivity analysis quantifying how close the scaled result comes to a well-powered test.\",\n          \"approach\": \"Re-invoke the existing, already-implemented eval.py logic (validated functional in a synthetic dry run last iteration) against the new scaled experiment artifact's completed method_out.json, ensuring sequencing so the evaluation only runs after the experiment has fully written its output, eliminating the previously disclosed race condition. Report placebo_test, stratified_robustness (by language and popularity bucket, now with enough n per stratum to be meaningful), pipeline_validity cross-check against Avelino et al.'s published aggregate rates, and calibration (bootstrap CIs, Brier score, AUC) at the new sample size. Add a dedicated power/sensitivity analysis: given the achieved effect sizes and n, compute the minimum detectable effect at 80% power and compare it against the observed coefficients, so the paper can state precisely whether the scaled result is adequately powered, still underpowered by a quantifiable margin, or has in fact crossed into significance -- replacing the previous iteration's qualitative '40-50% of target' claim with an exact number.\",\n          \"depends_on\": [\n            {\"id\": \"art_wWTWRqndgmX9\", \"label\": \"prior eval harness\"}\n          ]\n        }\n      ],\n      \"expected_outcome\": \"A 200-300+ repository scaled corpus with a transparent filtering funnel; a rerun of the full diffusion-predicts-survival statistical battery at meaningfully higher power, plus a new joint model that directly tests whether pre-departure-window timing (not mere diffusion) reconciles this hypothesis's protective sign with Medappa et al.'s opposite-sign permanent-ratio finding; and a completed (no longer race-blocked) placebo/robustness/calibration audit with an exact power analysis -- together either producing the paper's first significant result or, if still null, a precisely quantified and much stronger-powered null that closes the major open reviewer concerns.\",\n      \"summary\": \"Scale the validated fame-independent corpus 3-5x, rerun the hypothesis test battery at real power, fix the evaluation race condition, and add a direct timing-based reconciliation of this hypothesis's diffusion signal against Medappa et al.'s contrary finding.\"\n    }\n  ]\n}\n", "structuredPatch": [{"oldStart": 9, "oldLines": 16, "newStart": 9, "newLines": 14, "lines": ["           \"type\": \"dataset\",", "           \"objective\": \"Scale the fame-independent, stratified GitHub corpus from 69 to 200-300+ processed repositories using the exact same six-language x three-star-strata sampling frame validated last iteration, with a fully transparent filtering funnel.\",", "           \"approach\": \"Reuse the prior iteration's sampling design (Python, JavaScript, Go, Java, Ruby, C++ x 50-500/500-5,000/5,000-100,000 stars) but widen the initial GitHub search sample substantially (target ~800-1200 candidates, budgeting for the same ~25% pass-rate observed at 270->69) so post-filter processed repos land in the 200-300 range. Reuse `git log --numstat` cloning (no API rate-limit bottleneck) and the same exclusion criteria (>=1,095 days history, bulk-import artifact detection at >80% files touched in week 1 per Kalliamvakou et al., single-dominant-early-committer requirement). Record and output a per-stage filtering funnel table (sampled -> excluded-insufficient-history -> excluded-mining-artifact -> excluded-no-dominant-founder -> final processed count), broken out by language and star stratum, as first-class output fields -- not just a summary count -- directly resolving the reviewer's funnel-transparency ask. Additionally tag each retained repo with metadata needed for the reconciliation test in the experiment artifact: total historical tenure of write-access grantees and the timing of write-access grants relative to founder TFDD, so the downstream experiment can distinguish 'permanent write-access ratio' (Medappa's construct) from 'pre-departure diffusion window' (this hypothesis's construct) on the same repos rather than needing a second corpus.\",", "-          \"depends_on\": [", "-            {\"id\": \"art_ZbwYXh1VlhVp\", \"label\": \"prior corpus\"}", "-          ]", "+          \"depends_on\": []", "         },", "         {", "           \"type\": \"experiment\",", "           \"objective\": \"Re-run the DOA/Truck-Factor/TFDD/survival pipeline and the full diffusion-predicts-survival statistical battery on the scaled corpus, and add a new explicit test that adjudicates the Medappa et al. tension by comparing a pre-departure-window diffusion measure against a permanent/whole-history write-access-ratio measure as competing predictors in the same model.\",", "           \"approach\": \"Apply the identical, already-validated DOA/TF/TFDD/diffusion/survival code from the prior experiment artifact to the scaled corpus, targeting 40+ founder-only strict TFDD events (and a correspondingly larger relaxed set) to approach the power analysis's stated target. Re-run the BH-corrected logistic regression, matched-pairs bootstrap (now with enough same-language/size-bucket density to actually form matched pairs), and Mann-Whitney tests at this larger n. Add the reconciliation test: construct, per founder-only-TFDD project, both (a) this study's pre-departure (6-12 month) diffusion score and (b) a Medappa-style permanent write-access ratio computed over the project's FULL pre-TFDD history (proportion of all-time contributors ever reaching DOA file-ownership, not windowed), then fit a joint regression with both predictors plus an interaction/timing term (e.g. whether diffusion accrued mostly within vs. outside the pre-departure window) to test whether it is specifically the TIMING of diffusion, not diffusion's mere presence, that flips its association with survival from Medappa's negative to this hypothesis's proposed positive. Report power/sample-size context explicitly (achieved n vs. the ~40-event target) and report Cohen's-d values for snapshot covariates together with bootstrap confidence intervals, not as bare point estimates, per the reviewer's MINOR note.\",", "           \"depends_on\": [", "-            {\"id\": \"art_4CZ-9Ou1G5ty\", \"label\": \"prior pipeline\"}", "+            {\"id\": \"art_ZbwYXh1VlhVp\", \"label\": \"prior corpus\"}", "           ]", "         },", "         {"]}, {"oldStart": 26, "oldLines": 7, "newStart": 24, "newLines": 8, "lines": ["           \"objective\": \"Run the placebo-window falsification test and stratified robustness audit against the complete, scaled experiment output (fixing the previously disclosed race condition), and add a power/sensitivity analysis quantifying how close the scaled result comes to a well-powered test.\",", "           \"approach\": \"Re-invoke the existing, already-implemented eval.py logic (validated functional in a synthetic dry run last iteration) against the new scaled experiment artifact's completed method_out.json, ensuring sequencing so the evaluation only runs after the experiment has fully written its output, eliminating the previously disclosed race condition. Report placebo_test, stratified_robustness (by language and popularity bucket, now with enough n per stratum to be meaningful), pipeline_validity cross-check against Avelino et al.'s published aggregate rates, and calibration (bootstrap CIs, Brier score, AUC) at the new sample size. Add a dedicated power/sensitivity analysis: given the achieved effect sizes and n, compute the minimum detectable effect at 80% power and compare it against the observed coefficients, so the paper can state precisely whether the scaled result is adequately powered, still underpowered by a quantifiable margin, or has in fact crossed into significance -- replacing the previous iteration's qualitative '40-50% of target' claim with an exact number.\",", "           \"depends_on\": [", "-            {\"id\": \"art_wWTWRqndgmX9\", \"label\": \"prior eval harness\"}", "+            {\"id\": \"art_4CZ-9Ou1G5ty\", \"label\": \"prior pipeline\"},", "+            {\"id\": \"art_ZbwYXh1VlhVp\", \"label\": \"prior corpus\"}", "           ]", "         }", "       ],"]}], "userModified": false, "replaceAll": false}
```

### [10] ASSISTANT · 2026-08-21 19:44:17 UTC

```
Fixed the dependency types: dataset now has no deps, experiment depends on the prior dataset, and evaluation depends on the prior experiment (and dataset).
```
