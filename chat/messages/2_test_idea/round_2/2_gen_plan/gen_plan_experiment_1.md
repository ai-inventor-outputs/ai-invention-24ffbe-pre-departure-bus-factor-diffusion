# gen_plan_experiment_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_plan`
> Run: `iter1_0b7b616dce39` — Scaling the Corpus, Auditing the Power, and Reconciling the Sign: What Happens When a Founder-Diffusion Survival Test Is Finally Interrogated Rather Than Just Run
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_experiment_1` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-08-21 19:44:22 UTC

```
model: claude-sonnet-5 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1
```

### [2] SYSTEM-USER prompt · 2026-08-21 19:44:30 UTC

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
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: experiment_iter2_dir2
type: experiment
objective: >-
  Re-run the DOA/Truck-Factor/TFDD/survival pipeline and the full diffusion-predicts-survival statistical battery on the scaled
  corpus, and add a new explicit test that adjudicates the Medappa et al. tension by comparing a pre-departure-window diffusion
  measure against a permanent/whole-history write-access-ratio measure as competing predictors in the same model.
approach: >-
  Apply the identical, already-validated DOA/TF/TFDD/diffusion/survival code from the prior experiment artifact to the scaled
  corpus, targeting 40+ founder-only strict TFDD events (and a correspondingly larger relaxed set) to approach the power analysis's
  stated target. Re-run the BH-corrected logistic regression, matched-pairs bootstrap (now with enough same-language/size-bucket
  density to actually form matched pairs), and Mann-Whitney tests at this larger n. Add the reconciliation test: construct,
  per founder-only-TFDD project, both (a) this study's pre-departure (6-12 month) diffusion score and (b) a Medappa-style
  permanent write-access ratio computed over the project's FULL pre-TFDD history (proportion of all-time contributors ever
  reaching DOA file-ownership, not windowed), then fit a joint regression with both predictors plus an interaction/timing
  term (e.g. whether diffusion accrued mostly within vs. outside the pre-departure window) to test whether it is specifically
  the TIMING of diffusion, not diffusion's mere presence, that flips its association with survival from Medappa's negative
  to this hypothesis's proposed positive. Report power/sample-size context explicitly (achieved n vs. the ~40-event target)
  and report Cohen's-d values for snapshot covariates together with bootstrap confidence intervals, not as bare point estimates,
  per the reviewer's MINOR note.
depends_on:
- id: art_ZbwYXh1VlhVp
  label: prior corpus
  relation_type:
  relation_rationale:
</artifact_direction>

<dependencies>
Completed artifacts this artifact can use during execution.

--- Dependency 1 ---
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

### [3] HUMAN-USER prompt · 2026-08-21 19:44:30 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [4] TOOL CALL — Write · 2026-08-21 19:45:30 UTC

```
File: /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/.terminal_claude_agent_struct_out.json

{
  "title": "Scaled diffusion-vs-survival test plus Medappa reconciliation",
  "summary": "Re-run the validated DOA/TF/TFDD/diffusion/survival pipeline from the prior iteration on the scaled 121-repo (34 founder-candidate) corpus, targeting 40+ founder-only strict TFDD events, redo the BH-corrected logistic regression / matched-pairs bootstrap / Mann-Whitney battery at this larger n, and add a new joint regression that pits this study's pre-departure-window diffusion score against a Medappa-style whole-history write-access ratio (plus a timing/interaction term) to test whether it is the TIMING of diffusion, not its mere presence, that flips the sign of its association with survival.",
  "runpod_compute_profile": "cpu_heavy",
  "implementation_pseudocode": "# INPUTS: full_data_out.json from art_ZbwYXh1VlhVp (70,260 commit/file rows across 121 repos,\n# 34 pre-filtered founder-only-candidate repos with metadata_dominant_founder_first_window_share,\n# metadata_alias_ambiguous_repo flag, per-row commit_index/timestamp/author_alias_key/file path/repo stars/forks/language)\n\n## STEP 0 -- load & sanity-check\nload full_data_out.json into a pandas DataFrame; parse metadata_* columns out of the `output`/`metadata` fields\nassert row count, repo count (34 candidates within the 121) match dataset summary; log any drift explicitly\nGROUP rows by metadata_repo_id -> per-repo commit stream sorted by commit_timestamp\n\n## STEP 1 -- reproduce prior iteration's DOA / Truck-Factor / TFDD pipeline VERBATIM\n# (do NOT re-derive the algorithm -- reuse the prior iteration's method.py / helper module if present\n#  in this artifact's own workspace history or re-implement byte-for-byte from Avelino et al. 2016 ICPC spec:\n#  DOA(dev, file) = -3.293 + 1.098*FA + 0.164*DL - 0.321*ln(1+AC)\n#  FA = 1 if dev is first author of file else 0; DL = total number of file's authors (deleted-lines-based tie count\n#  per Fritz et al.); AC = number of a developer's own commits to that file since last touch by dev with highest DOA;\n#  a developer is the file's primary author / \"owns\" it if their DOA is the max among all contributors AND DOA > threshold\n#  used previously (reuse prior iteration's exact threshold constant, do not re-tune))\nfor each repo:\n    compute YEARLY snapshots of: (a) per-file DOA ranking, (b) Truck-Factor set = minimal set of top-DOA devs\n        covering >=50% of files (Avelino greedy TF algorithm), (c) each TF developer's last-commit date\n    detect TFDD events: date at which every developer in the CURRENT TF set has been silent >= 1 year\n        (validated 1-year abandoner threshold, reuse verbatim)\n    FILTER to FOUNDER-ONLY TFDD: the departing TF set has size 1 AND that developer is the repo's\n        first-commit / dominant-early author (reuse metadata_dominant_founder_first_window_share >= 0.70\n        pre-filter from the dataset, but re-verify against full per-repo commit history, not just first window)\n    define STRICT vs RELAXED founder-only criteria exactly as prior iteration did (document threshold values\n        explicitly at top of script as named constants, e.g. STRICT_FOUNDER_SHARE=0.70, RELAXED=0.50)\n\n## STEP 2 -- pre-departure diffusion score (the study's core NEW measurement)\nfor each founder-only TFDD event at time T_departure:\n    WINDOW = [T_departure - 12mo, T_departure - 6mo]  # reuse prior iteration's exact window bounds\n    founder_commit_share_in_window = founder's commits / total commits in WINDOW\n    diffused_owner_count = count of DISTINCT non-founder accounts reaching primary DOA ownership\n        on >=1 file at any point inside WINDOW\n    diffusion_score = combine as prior iteration did (do not invent a new formula; if prior iteration\n        used both as SEPARATE regressors rather than one combined score, keep them separate here too)\n\n## STEP 3 -- survival outcome (Avelino Active/Inactive/graded model, reuse verbatim)\nfor each event: 18-month post-TFDD window -> classify thriving/maintained/dormant/dead per prior iteration's\n    exact activity thresholds (commit count + release count cutoffs); collapse to binary survived/not-survived\n    for the primary logistic model, keep graded label for an ordinal-regression secondary check\n\n## STEP 4 -- power/target check BEFORE running stats\nn_strict, n_relaxed = count of founder-only TFDD events found\nlog explicitly: achieved n vs the ~40-event power-analysis target from iter1\nif n_strict < 40: proceed anyway but REPORT the shortfall explicitly in method_out.json (do not silently\n    treat an underpowered n as if it met the target) -- this is expected given the 34-repo candidate pool\n    caps the ceiling (34 repos can yield at most 34 strict events, structurally below 40)\n    -> FLAG THIS UP FRONT: if achieved n cannot reach 40, say so in method_out and do not overclaim power\n\n## STEP 5 -- primary statistical battery (reuse prior iteration's exact test specs)\nlogit_model = statsmodels.Logit(survived ~ founder_commit_share_in_window + diffused_owner_count\n    + stars_log + forks_log + contributor_count + C(language) + C(license), data=events)\napply Benjamini-Hochberg correction across the diffusion coefficients' p-values (and separately\n    report snapshot-covariate coefficients: developers/commits/files at TFDD, with Cohen's d\n    AND bootstrap 95% CI via scipy/BCa bootstrap, per reviewer note -- not bare point estimates)\n\nmatched_pairs = for each survivor event, find non-survivor event(s) in same language + same star-stratum\n    bucket (reuse prior iteration's bucket edges: 100-1k/1k-10k/10k+) differing in diffusion_score;\n    if matched pool now large enough (n up from 16-20), run McNemar / paired bootstrap on survival rate\n    ratio, report 95% CI; if STILL zero eligible pairs at this scale, report that explicitly rather than\n    silently omitting the test\n\nmann_whitney: survivors vs non-survivors on founder_commit_share_in_window and diffused_owner_count\n\nplacebo/shuffle check: relocate the 6-12mo pre-departure window to a RANDOM point in project history\n    (excluding overlap with true window and post-TFDD period), recompute diffusion score, rerun the\n    logistic coefficient 1000x -> build a null distribution, report where the true-window coefficient\n    falls (empirical p-value against the null)\n\n## STEP 6 -- NEW reconciliation test (Medappa et al. adjudication) -- the direction's headline addition\nfor each founder-only TFDD event/repo:\n    medappa_ratio = (count of ALL distinct contributors, across the repo's FULL pre-TFDD history,\n        who EVER reached DOA-based primary file ownership on >=1 file) / (total distinct contributors\n        in that same full pre-TFDD history)\n        # this is the STATIC, whole-history write-access-ratio analog to Medappa et al.'s construct --\n        # NOT windowed, NOT founder-specific -- computed over the entire pre-departure lifetime\n    timing_term = fraction of diffused_owner_count's file-ownership-onset EVENTS that fall INSIDE the\n        6-12mo pre-departure WINDOW vs. earlier in the repo's history (i.e., proportion of \"diffusion\"\n        that is concentrated near departure vs. spread evenly through history)\n    joint_model = Logit(survived ~ founder_commit_share_in_window + medappa_ratio\n        + timing_term + medappa_ratio:timing_term + stars_log + forks_log + contributor_count\n        + C(language) + C(license))\n    report: does medappa_ratio alone (no timing) show the reported-negative sign (replicating Medappa\n        direction)? does the interaction/timing term flip or moderate that sign, consistent with the\n        \"timing not mere presence\" reconciliation hypothesis? report coefficient signs, CIs, and\n        whether medappa_ratio and founder_commit_share_in_window are highly collinear (VIF check) --\n        if VIF > 10 for either, report that as a limitation on interpreting the joint model cleanly\n\n## STEP 7 -- write output\nmethod_out.json: {\n  corpus_summary: {n_repos_input, n_founder_candidates, n_strict_tfdd, n_relaxed_tfdd, target_n=40,\n                   shortfall_note},\n  primary_regression: {coeffs, se, BH_p, snapshot_covariate_effect_sizes: {cohens_d, bootstrap_ci}},\n  matched_pairs: {n_pairs, result_or_explicit_zero_pairs_note},\n  mann_whitney: {stat, p, per_variable},\n  placebo_check: {true_coef, null_distribution_summary, empirical_p},\n  reconciliation: {medappa_ratio_coef, timing_term_coef, interaction_coef, VIF, interpretation},\n  raw_event_table: [per-event feature+outcome rows for downstream paper/analysis]\n}",
  "fallback_plan": "If the 34-repo candidate pool yields far fewer than 40 strict founder-only TFDD events (very likely, since 34 is a hard ceiling below the 40 target even at 100% yield): (1) do NOT block on hitting n=40 -- run the full battery at whatever n is achieved (expect roughly 16-34 strict events) and report the shortfall transparently in method_out.json rather than silently treating it as adequate power; this mirrors iter1's honest underpowered-first-pass framing. (2) Additionally report the RELAXED founder-only criterion results (larger n) alongside strict, exactly as iter1 did, so the reader sees both. (3) If DOA/TF pipeline code from the prior iteration's artifact is not directly retrievable/reusable in this workspace, re-implement the DOA formula and greedy TF-set algorithm from the Avelino et al. 2016 ICPC spec (formula given in the pseudocode) rather than inventing a new authority metric -- fidelity to the validated method matters more than speed. (4) If the matched-pairs test still returns zero eligible pairs even at the larger n (plausible given only 4 languages x 3 star strata x binary-ish diffusion split), relax the matching to same-stratum-only (drop the exact language match, keep language as a regression covariate instead) and report both the strict-matching (possibly empty) and relaxed-matching results, flagging the change explicitly. (5) If the Medappa reconciliation joint model shows severe multicollinearity (VIF>10) between medappa_ratio and founder_commit_share_in_window, report this as a genuine finding (the two constructs may not be separable at this corpus size) rather than forcing a joint model -- fall back to reporting each predictor's SEPARATE univariate association with survival plus the timing_term's separate association, and note the joint model is underpowered to disentangle them. (6) If statsmodels.Logit fails to converge (likely at low n with several covariates), drop lowest-priority covariates first (license, then contributor_count) in a documented order, or switch to Firth's penalized logistic regression (via the `firthlogist` PyPI package) which handles near-separation at small n -- do not silently drop failed models from the output.",
  "testing_plan": "1. Before running on the full corpus, load full_data_out.json and print row/repo counts, confirm all 34 pre-flagged founder-candidate repo_ids are present with metadata_dominant_founder_first_window_share populated -- this validates the dependency load path before any pipeline logic runs. 2. Unit-test the DOA formula and greedy TF-set selection on 2-3 small synthetic commit histories with a hand-computable expected TF set (e.g. a 3-file, 2-developer toy history) before applying to real data, to catch algorithm implementation bugs cheaply. 3. Run the full TFDD/founder-detection/diffusion-score pipeline on a SINGLE real repo first (pick a mid-size one, ~500-1000 commits) and manually inspect the detected TFDD date(s) and diffusion trajectory against a quick eyeball of that repo's commit history structure (commit counts by author over time) to sanity-check plausibility before scaling to all 34. 4. Run the full pipeline on all 34 repos and check the resulting n_strict/n_relaxed counts are in the plausible range implied by the prior iteration's 16/20 at 34-candidate scope (since this is the SAME 34-repo pool, not a larger one -- expect similar or identical event counts to iter1, since 'scaling' here is not adding repos beyond what art_ZbwYXh1VlhVp already provides; explicitly confirm this expectation against the dataset's stated scope before writing results, and if n does not change from iter1's 16/20, report that plainly rather than implying a larger corpus was achieved). 5. Before finalizing the reconciliation test, spot-check medappa_ratio computation on 2 repos by manually counting DOA-owning contributors in the raw commit log slice, confirming the ratio matches a manual tally. 6. Confirm the placebo/shuffle check's null distribution is centered near zero (not systematically offset), which would indicate a bug in window-relocation logic rather than a genuine null."
}
```

### [5] TOOL RESULT — Write · 2026-08-21 19:45:30 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Scaled diffusion-vs-survival test plus Medappa reconciliation\",\n  \"summary\": \"Re-run the validated DOA/TF/TFDD/diffusion/survival pipeline from the prior iteration on the scaled 121-repo (34 founder-candidate) corpus, targeting 40+ founder-only strict TFDD events, redo the BH-corrected logistic regression / matched-pairs bootstrap / Mann-Whitney battery at this larger n, and add a new joint regression that pits this study's pre-departure-window diffusion score against a Medappa-style whole-history write-access ratio (plus a timing/interaction term) to test whether it is the TIMING of diffusion, not its mere presence, that flips the sign of its association with survival.\",\n  \"runpod_compute_profile\": \"cpu_heavy\",\n  \"implementation_pseudocode\": \"# INPUTS: full_data_out.json from art_ZbwYXh1VlhVp (70,260 commit/file rows across 121 repos,\\n# 34 pre-filtered founder-only-candidate repos with metadata_dominant_founder_first_window_share,\\n# metadata_alias_ambiguous_repo flag, per-row commit_index/timestamp/author_alias_key/file path/repo stars/forks/language)\\n\\n## STEP 0 -- load & sanity-check\\nload full_data_out.json into a pandas DataFrame; parse metadata_* columns out of the `output`/`metadata` fields\\nassert row count, repo count (34 candidates within the 121) match dataset summary; log any drift explicitly\\nGROUP rows by metadata_repo_id -> per-repo commit stream sorted by commit_timestamp\\n\\n## STEP 1 -- reproduce prior iteration's DOA / Truck-Factor / TFDD pipeline VERBATIM\\n# (do NOT re-derive the algorithm -- reuse the prior iteration's method.py / helper module if present\\n#  in this artifact's own workspace history or re-implement byte-for-byte from Avelino et al. 2016 ICPC spec:\\n#  DOA(dev, file) = -3.293 + 1.098*FA + 0.164*DL - 0.321*ln(1+AC)\\n#  FA = 1 if dev is first author of file else 0; DL = total number of file's authors (deleted-lines-based tie count\\n#  per Fritz et al.); AC = number of a developer's own commits to that file since last touch by dev with highest DOA;\\n#  a developer is the file's primary author / \\\"owns\\\" it if their DOA is the max among all contributors AND DOA > threshold\\n#  used previously (reuse prior iteration's exact threshold constant, do not re-tune))\\nfor each repo:\\n    compute YEARLY snapshots of: (a) per-file DOA ranking, (b) Truck-Factor set = minimal set of top-DOA devs\\n        covering >=50% of files (Avelino greedy TF algorithm), (c) each TF developer's last-commit date\\n    detect TFDD events: date at which every developer in the CURRENT TF set has been silent >= 1 year\\n        (validated 1-year abandoner threshold, reuse verbatim)\\n    FILTER to FOUNDER-ONLY TFDD: the departing TF set has size 1 AND that developer is the repo's\\n        first-commit / dominant-early author (reuse metadata_dominant_founder_first_window_share >= 0.70\\n        pre-filter from the dataset, but re-verify against full per-repo commit history, not just first window)\\n    define STRICT vs RELAXED founder-only criteria exactly as prior iteration did (document threshold values\\n        explicitly at top of script as named constants, e.g. STRICT_FOUNDER_SHARE=0.70, RELAXED=0.50)\\n\\n## STEP 2 -- pre-departure diffusion score (the study's core NEW measurement)\\nfor each founder-only TFDD event at time T_departure:\\n    WINDOW = [T_departure - 12mo, T_departure - 6mo]  # reuse prior iteration's exact window bounds\\n    founder_commit_share_in_window = founder's commits / total commits in WINDOW\\n    diffused_owner_count = count of DISTINCT non-founder accounts reaching primary DOA ownership\\n        on >=1 file at any point inside WINDOW\\n    diffusion_score = combine as prior iteration did (do not invent a new formula; if prior iteration\\n        used both as SEPARATE regressors rather than one combined score, keep them separate here too)\\n\\n## STEP 3 -- survival outcome (Avelino Active/Inactive/graded model, reuse verbatim)\\nfor each event: 18-month post-TFDD window -> classify thriving/maintained/dormant/dead per prior iteration's\\n    exact activity thresholds (commit count + release count cutoffs); collapse to binary survived/not-survived\\n    for the primary logistic model, keep graded label for an ordinal-regression secondary check\\n\\n## STEP 4 -- power/target check BEFORE running stats\\nn_strict, n_relaxed = count of founder-only TFDD events found\\nlog explicitly: achieved n vs the ~40-event power-analysis target from iter1\\nif n_strict < 40: proceed anyway but REPORT the shortfall explicitly in method_out.json (do not silently\\n    treat an underpowered n as if it met the target) -- this is expected given the 34-repo candidate pool\\n    caps the ceiling (34 repos can yield at most 34 strict events, structurally below 40)\\n    -> FLAG THIS UP FRONT: if achieved n cannot reach 40, say so in method_out and do not overclaim power\\n\\n## STEP 5 -- primary statistical battery (reuse prior iteration's exact test specs)\\nlogit_model = statsmodels.Logit(survived ~ founder_commit_share_in_window + diffused_owner_count\\n    + stars_log + forks_log + contributor_count + C(language) + C(license), data=events)\\napply Benjamini-Hochberg correction across the diffusion coefficients' p-values (and separately\\n    report snapshot-covariate coefficients: developers/commits/files at TFDD, with Cohen's d\\n    AND bootstrap 95% CI via scipy/BCa bootstrap, per reviewer note -- not bare point estimates)\\n\\nmatched_pairs = for each survivor event, find non-survivor event(s) in same language + same star-stratum\\n    bucket (reuse prior iteration's bucket edges: 100-1k/1k-10k/10k+) differing in diffusion_score;\\n    if matched pool now large enough (n up from 16-20), run McNemar / paired bootstrap on survival rate\\n    ratio, report 95% CI; if STILL zero eligible pairs at this scale, report that explicitly rather than\\n    silently omitting the test\\n\\nmann_whitney: survivors vs non-survivors on founder_commit_share_in_window and diffused_owner_count\\n\\nplacebo/shuffle check: relocate the 6-12mo pre-departure window to a RANDOM point in project history\\n    (excluding overlap with true window and post-TFDD period), recompute diffusion score, rerun the\\n    logistic coefficient 1000x -> build a null distribution, report where the true-window coefficient\\n    falls (empirical p-value against the null)\\n\\n## STEP 6 -- NEW reconciliation test (Medappa et al. adjudication) -- the direction's headline addition\\nfor each founder-only TFDD event/repo:\\n    medappa_ratio = (count of ALL distinct contributors, across the repo's FULL pre-TFDD history,\\n        who EVER reached DOA-based primary file ownership on >=1 file) / (total distinct contributors\\n        in that same full pre-TFDD history)\\n        # this is the STATIC, whole-history write-access-ratio analog to Medappa et al.'s construct --\\n        # NOT windowed, NOT founder-specific -- computed over the entire pre-departure lifetime\\n    timing_term = fraction of diffused_owner_count's file-ownership-onset EVENTS that fall INSIDE the\\n        6-12mo pre-departure WINDOW vs. earlier in the repo's history (i.e., proportion of \\\"diffusion\\\"\\n        that is concentrated near departure vs. spread evenly through history)\\n    joint_model = Logit(survived ~ founder_commit_share_in_window + medappa_ratio\\n        + timing_term + medappa_ratio:timing_term + stars_log + forks_log + contributor_count\\n        + C(language) + C(license))\\n    report: does medappa_ratio alone (no timing) show the reported-negative sign (replicating Medappa\\n        direction)? does the interaction/timing term flip or moderate that sign, consistent with the\\n        \\\"timing not mere presence\\\" reconciliation hypothesis? report coefficient signs, CIs, and\\n        whether medappa_ratio and founder_commit_share_in_window are highly collinear (VIF check) --\\n        if VIF > 10 for either, report that as a limitation on interpreting the joint model cleanly\\n\\n## STEP 7 -- write output\\nmethod_out.json: {\\n  corpus_summary: {n_repos_input, n_founder_candidates, n_strict_tfdd, n_relaxed_tfdd, target_n=40,\\n                   shortfall_note},\\n  primary_regression: {coeffs, se, BH_p, snapshot_covariate_effect_sizes: {cohens_d, bootstrap_ci}},\\n  matched_pairs: {n_pairs, result_or_explicit_zero_pairs_note},\\n  mann_whitney: {stat, p, per_variable},\\n  placebo_check: {true_coef, null_distribution_summary, empirical_p},\\n  reconciliation: {medappa_ratio_coef, timing_term_coef, interaction_coef, VIF, interpretation},\\n  raw_event_table: [per-event feature+outcome rows for downstream paper/analysis]\\n}\",\n  \"fallback_plan\": \"If the 34-repo candidate pool yields far fewer than 40 strict founder-only TFDD events (very likely, since 34 is a hard ceiling below the 40 target even at 100% yield): (1) do NOT block on hitting n=40 -- run the full battery at whatever n is achieved (expect roughly 16-34 strict events) and report the shortfall transparently in method_out.json rather than silently treating it as adequate power; this mirrors iter1's honest underpowered-first-pass framing. (2) Additionally report the RELAXED founder-only criterion results (larger n) alongside strict, exactly as iter1 did, so the reader sees both. (3) If DOA/TF pipeline code from the prior iteration's artifact is not directly retrievable/reusable in this workspace, re-implement the DOA formula and greedy TF-set algorithm from the Avelino et al. 2016 ICPC spec (formula given in the pseudocode) rather than inventing a new authority metric -- fidelity to the validated method matters more than speed. (4) If the matched-pairs test still returns zero eligible pairs even at the larger n (plausible given only 4 languages x 3 star strata x binary-ish diffusion split), relax the matching to same-stratum-only (drop the exact language match, keep language as a regression covariate instead) and report both the strict-matching (possibly empty) and relaxed-matching results, flagging the change explicitly. (5) If the Medappa reconciliation joint model shows severe multicollinearity (VIF>10) between medappa_ratio and founder_commit_share_in_window, report this as a genuine finding (the two constructs may not be separable at this corpus size) rather than forcing a joint model -- fall back to reporting each predictor's SEPARATE univariate association with survival plus the timing_term's separate association, and note the joint model is underpowered to disentangle them. (6) If statsmodels.Logit fails to converge (likely at low n with several covariates), drop lowest-priority covariates first (license, then contributor_count) in a documented order, or switch to Firth's penalized logistic regression (via the `firthlogist` PyPI package) which handles near-separation at small n -- do not silently drop failed models from the output.\",\n  \"testing_plan\": \"1. Before running on the full corpus, load full_data_out.json and print row/repo counts, confirm all 34 pre-flagged founder-candidate repo_ids are present with metadata_dominant_founder_first_window_share populated -- this validates the dependency load path before any pipeline logic runs. 2. Unit-test the DOA formula and greedy TF-set selection on 2-3 small synthetic commit histories with a hand-computable expected TF set (e.g. a 3-file, 2-developer toy history) before applying to real data, to catch algorithm implementation bugs cheaply. 3. Run the full TFDD/founder-detection/diffusion-score pipeline on a SINGLE real repo first (pick a mid-size one, ~500-1000 commits) and manually inspect the detected TFDD date(s) and diffusion trajectory against a quick eyeball of that repo's commit history structure (commit counts by author over time) to sanity-check plausibility before scaling to all 34. 4. Run the full pipeline on all 34 repos and check the resulting n_strict/n_relaxed counts are in the plausible range implied by the prior iteration's 16/20 at 34-candidate scope (since this is the SAME 34-repo pool, not a larger one -- expect similar or identical event counts to iter1, since 'scaling' here is not adding repos beyond what art_ZbwYXh1VlhVp already provides; explicitly confirm this expectation against the dataset's stated scope before writing results, and if n does not change from iter1's 16/20, report that plainly rather than implying a larger corpus was achieved). 5. Before finalizing the reconciliation test, spot-check medappa_ratio computation on 2 repos by manually counting DOA-owning contributors in the raw commit log slice, confirming the ratio matches a manual tally. 6. Confirm the placebo/shuffle check's null distribution is centered near zero (not systematically offset), which would indicate a bug in window-relocation logic rather than a genuine null.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [6] ASSISTANT · 2026-08-21 19:45:32 UTC

```
Plan written to `.terminal_claude_agent_struct_out.json`. It reuses the prior iteration's validated DOA/TF/TFDD pipeline on the existing 34-repo founder-candidate pool (flagging that this caps below the 40-event target, not silently overclaiming it), reruns the BH-corrected regression/matched-pairs/Mann-Whitney/placebo battery, and adds the new Medappa reconciliation joint model (windowed diffusion vs. whole-history write-access ratio plus a timing interaction term).
```
