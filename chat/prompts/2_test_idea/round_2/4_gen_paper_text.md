# gen_paper_text — test_idea

> Phase: `invention_loop` · round 2 · `gen_paper_text`
> Run: `run_5SMkWpWKNLxk` — Measuring Authority Diffusion Before Founders Leave Open Source Projects
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_paper_text` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-08-20 20:51:08 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A research paper writer (Step 3.4: GEN_PAPER_TEXT in the invention loop)

You received the hypothesis, all artifacts, the previous paper draft (if any), and reviewer feedback.
Write a complete paper draft with figure placeholders.

Publication-quality paper → strong contribution. Weak paper → wasted iteration.
</your_role>
</ai_inventor_context>

<research_methodology>
Write like a researcher drafting a paper, not a chatbot summarizing bullet points.

- Structure as a paper would: research question → methodology → results → analysis → limitations. Not a list of "we did X, then Y."
- Ground every claim in specific artifacts and specific numbers. "Results show improvement" is empty — state effect sizes, baselines, and conditions.
- Be honest about what worked, what didn't, and why. Don't spin failures as "future work."
- The paper's headline contribution should be a positive or surprising finding. Negative results are valuable context but should not be the primary narrative — lead with what works.
- Address reviewer feedback from previous iterations explicitly — show you've thought about each critique.
</research_methodology>

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

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for related-work positioning and how this field frames a genuinely novel contribution.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>
<previous_paper>
STARTING POINT: This is your paper draft from the previous iteration.

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

</previous_paper>

<reviewer_feedback>
STEP 1 — REVIEW: A reviewer evaluated the previous paper draft above and produced this feedback.

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

<pipeline_steps>
STEP 2 — STRATEGY: The pipeline's strategy generator (gen_strat) read the reviewer feedback
and designed a new research strategy to address the critiques.

STEP 3 — PLANNING: The planner (gen_plan) turned the strategy into concrete artifact plans —
specific experiments, datasets, or research tasks to execute.

STEP 4 — EXECUTION: The executor (gen_art) ran those plans and produced the new artifacts
shown in <new_artifacts_this_iteration> below.
</pipeline_steps>

<hypothesis>
STEP 5 — HYPOTHESIS UPDATE: The hypothesis was revised based on evidence from previous iterations.

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

<all_artifacts>
FULL EVIDENCE BASE: All 6 research artifacts across all iterations.

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

--- Item 4 ---
id: art_ZAquYQUNc_3n
type: research
title: OSS Community-Health Positioning and Bias-Free Data Sources
summary: >-
  This research artifact grounds the paper's pre-departure authority-diffusion construct in OSS-native literature and identifies
  a concrete, token-free data pipeline for building a historically-snapshotted, liveness-non-conditioned repository corpus.
  Part A: CHAOSS's Contributor Absence Factor (ex-Bus Factor) can be computed as a snapshot or longitudinally per CHAOSS's
  own KB, but no CHAOSS metric formalizes or validates a pre-departure trend; the sibling Elephant Factor is explicitly snapshot-only.
  Apache Incubator's graduation guide operationalizes 'diversity' as a binary committee-judged gate (>=3 legally independent
  committers, no single essential company) rather than a continuous statistic; the Project Maturity Model's CD-series turned
  out to be code-governance criteria, not diversity criteria, and needs re-verification before citing by code. Onion-model
  (Jergensen/Sarma/Wagstrom) and Steinmacher et al.'s newcomer-barriers SLR study the mirror-image INWARD (periphery-to-core)
  trajectory, complementary to this hypothesis's OUTWARD (founder authority dispersing) trajectory. Part B: GH Archive's PushEvent
  payload is confirmed to carry only commit sha/author/message pointers, not file lists or diffs, so it can supply a repo-selection
  frame (via hourly JSON dumps or free BigQuery sandbox, no GitHub token) but not DOA input data. World of Code holds the
  right shape of full commit/blob/file/author data but is access-gated via an SSH registration process, making it a fallback
  rather than primary source for a short execution window. GHTorrent is confirmed dead infrastructure (its own domain now
  redirects to an unrelated site; its BigQuery mirror is stale since mid-2019). Libraries.io's Zenodo CSV dump is live and
  usable for repo-selection metadata but has no commit-level data. Recommended pull-path: build the repo-selection frame from
  GH Archive/BigQuery or Libraries.io frozen at a historical year Y, then obtain each selected repo's full commit/file history
  via plain unauthenticated git clone (unlimited, token-free, independent of the repo's current activity status), honestly
  noting that repos later made fully private or deleted will still be lost. Includes 18 numbered sources and explicit confidence/caveat
  notes on unverified specifics (BigQuery sandbox scan limits, exact Maturity Model diversity-criteria codes).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 5 ---
id: art_apZrIEHXfHos
type: dataset
title: Non-Survivorship-Biased Founder Departure Corpus
summary: >-
  This artifact builds github_founder_departure_commits_non_conditioned, a companion/superset corpus to iter_1's github_founder_departure_commits
  dataset for founder-departure Truck-Factor/DOA (departure-of-author) survival analysis. It pools two explicit sampling frames
  into one exp_sel_data_out-schema dataset, tagged per-example via metadata_sampling_frame: (1) 'liveness_non_conditioned'
  repos discovered this iteration via the GitHub Search API using queries that combine a historical repository-creation window
  (2009-2016), EITHER archived:true OR a stale pushed:<2020 filter, and a language sweep across 10 ecosystems -- with NO filter
  on current stars, fame, or liveness, unlike iter_1's hand-curated 'currently prominent' candidate list; and (2) 'liveness_conditioned'
  repos, the 12 successfully-extracted repos from iter_1's original corpus, carried forward unmodified and retro-tagged so
  downstream code can filter or stratify by frame instead of silently mixing a survivorship-biased sample with an unbiased
  one. code/find_candidates.py ran ~60 GitHub Search API queries (unauthenticated, 10 req/min limit -- no GITHUB_TOKEN was
  present in this environment, verified via curl against /rate_limit before writing the script) and discovered 700 unique
  liveness_non_conditioned candidate repos, checkpointed to temp/non_conditioned_candidates.json. code/build_dataset.py then
  attempted to fetch metadata (GitHub REST API, 60 req/hour) and clone+extract full commit history (git clone --bare + git
  log --numstat, matching iter_1's extraction method exactly: per-commit author email/name/date and per-file insertion/deletion
  counts, no blob content) for those candidates, deliberately WITHOUT iter_1's archived-repo rejection or star-count floor
  (the two filters that would reintroduce liveness/fame conditioning), keeping only a >=3.0 year total commit-history-span
  filter needed to run the DOA/Truck-Factor algorithm and score an 18-month post-departure survival window. Within the time
  this pipeline ran, 1 of ~28 attempted candidates (jquery-archive/jquery-metadata, archived=true, 40 commits, 4.0y history)
  passed the history filter and was extracted; the other ~27 were skipped almost entirely for insufficient_history (their
  total commit span never reached 3 years -- most archived/stale repos discovered by this method turn out to have been abandoned
  within 1-2 years of creation, before ever accumulating enough history to be usable for this analysis). This low yield is
  reported honestly and explicitly in full_data_out.json's metadata.yield_report, including the full skip-reason breakdown,
  rather than papered over: it is itself an informative finding (repos that both survive multiple years AND still end up archived/dead
  are a rare intersection versus the much larger population of repos that die early), and it means the specific gap this artifact
  targets -- a non-surviving founder-only TFDD event with sufficient post-departure history -- was NOT found in this batch,
  so downstream eval/experiment artifacts should treat statistical power for that specific claim as unproven from this corpus
  alone. The final dataset has 11 examples total (1 liveness_non_conditioned + 10 liveness_conditioned, matching iter_1's
  own successfully-loaded record count), each a full per-repo record (repo_metadata, commits[], founder_signal, sampling_frame,
  frame_construction_method) identical in shape to iter_1's schema, validated against exp_sel_data_out.json. Both find_candidates.py
  and build_dataset.py checkpoint to disk (temp/non_conditioned_candidates.json, temp/checkpoint.json) and are resumable,
  so a follow-up run with more wall-clock time or an authenticated GITHUB_TOKEN can extend this corpus directly without redoing
  the discovery sweep.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 6 ---
id: art_yOHrviKrh_11
type: evaluation
title: Closing the Rigor Gaps in the Diffusion Pipeline
summary: >-
  This evaluation artifact closes five reviewer-named rigor gaps in the prior founder-departure authority-diffusion pipeline
  (EXPERIMENT art_I5KoOp16hub5, DATASET art_ZuMis522AEPF) by re-analyzing their outputs in a new eval.py, without collecting
  new repos or new methods. (A) Discloses the placebo/window-shuffle permutation scheme exactly from method.py's source: continuous
  with-replacement sampling of window start offsets, per-repo shipped cap of 20 draws (not 500/60/40 as summarized), no cross-stratum
  seed dependence; reports the combinatorial feasible-window space per founder-TFDD repo (741 total feasible start-month positions
  across 5 founder-only-TFDD events found on re-run, vs 6 claimed in the EXPERIMENT summary); re-runs the placebo test at
  budgets 20/100/300 draws per repo (up to 300 achieved in ~113s wall-clock for the largest budget, well under a 20-minute
  cap), reporting a convergence table of null-distribution mean/SD and the theoretical minimum two-sided p-value (1/(k+1))
  at each budget; and proves no true-effect placebo p-value is computable at any budget because method.run_regressions requires
  n>=10 while n_founder_tfdd_events=5, so the disclosure gap is closed but the underlying power gap is not. (B) Computes Wilson
  95% CIs for Avelino et al.'s reported 66% TF=1 rate (n=315, CI [0.606, 0.710]) and this study's own all-TFDD-denominator
  TF=1 rate (CI [0.354, 0.848]), finding the intervals overlap, with an explicit caution that this study's wide small-n interval
  makes 'overlap' weak evidence rather than validation. (C) Spot-checks alias-resolution against live GitHub contributor data
  for 3 of 15 repos (20% of corpus, amoffat/sh, arrow-py/arrow, Kludex/starlette), finding no confirmed bot-as-authority-holder
  or over-merging, one plausible under-merged same-human pair (would slightly deflate diffusion score, not flip classification),
  and one unresolved bot-inflation risk (dependabot[bot] at 159 contributions on Kludex/starlette) that a contributor-list-only
  check cannot rule out without file-level DOA attribution. (D) Emits an exact 15-row repository table (verified live count
  matches the dataset's claimed 15) with repo name, language, stars, forks, history span, TFDD/TF=1/survival status, and diffusion
  metrics, cross-checked directly against the two source JSON files with missing-field flags where applicable. (E) Quantifies
  this corpus's TFDD incidence (73.3% at n=15) and survival rate (100% among detected TFDDs) against Avelino et al.'s published
  16.3% incidence and 40.6% survival via exact binomial and normal-approximation two-proportion tests, both showing large,
  statistically significant deviations in the direction consistent with survivorship bias; and documents a formal 'Residual
  Limitation' section explaining why a survivor-conditioned sampling frame is an inconsistent (not merely imprecise) estimator,
  quoting the DATASET artifact's own 60-req/hour GitHub API rate-limit constraint (15 of ~104 candidate repos completed),
  and giving a concrete falsifiable prediction for a future GITHUB_TOKEN-enabled run, explicitly not claiming the second-frame
  comparison was run. All five parts write into eval_out.json under clearly named top-level keys (permutation_disclosure,
  tf1_ci_comparison, alias_spotcheck, repo_table, survivorship_bias_quantification) plus a top-level overall_verdict summarizing
  which gaps are fully closed with data (A's disclosure, B, D, E's quantification) versus structurally open (A's power problem,
  E's second-frame comparison, C's full-corpus coverage). eval_out.json validates cleanly against the exp_eval_sol_out schema
  (0 errors, 0 warnings after adding numeric eval_* fields to every example); full/mini/preview variants (46KB/35KB/19KB)
  are all far under the 100MB size limit. pyproject.toml pins numpy==2.5.2, pandas==3.0.5, scipy==1.18.0, scikit-learn==1.9.0,
  statsmodels==0.14.6, loguru==0.7.3, psutil==7.2.2, matching the installed .venv exactly. Downstream GEN_PAPER_TEXT should
  present this as closing the disclosure/comparison/reproducibility gaps with concrete numbers while explicitly retaining
  two structurally open limitations (small-n placebo power, single-frame survivorship-bias evidence) as honest scope boundaries
  rather than resolved claims.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</all_artifacts>

<new_artifacts_this_iteration>
NEW THIS ITERATION: These 3 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

summary: >-
  This research artifact grounds the paper's pre-departure authority-diffusion construct in OSS-native literature and identifies
  a concrete, token-free data pipeline for building a historically-snapshotted, liveness-non-conditioned repository corpus.
  Part A: CHAOSS's Contributor Absence Factor (ex-Bus Factor) can be computed as a snapshot or longitudinally per CHAOSS's
  own KB, but no CHAOSS metric formalizes or validates a pre-departure trend; the sibling Elephant Factor is explicitly snapshot-only.
  Apache Incubator's graduation guide operationalizes 'diversity' as a binary committee-judged gate (>=3 legally independent
  committers, no single essential company) rather than a continuous statistic; the Project Maturity Model's CD-series turned
  out to be code-governance criteria, not diversity criteria, and needs re-verification before citing by code. Onion-model
  (Jergensen/Sarma/Wagstrom) and Steinmacher et al.'s newcomer-barriers SLR study the mirror-image INWARD (periphery-to-core)
  trajectory, complementary to this hypothesis's OUTWARD (founder authority dispersing) trajectory. Part B: GH Archive's PushEvent
  payload is confirmed to carry only commit sha/author/message pointers, not file lists or diffs, so it can supply a repo-selection
  frame (via hourly JSON dumps or free BigQuery sandbox, no GitHub token) but not DOA input data. World of Code holds the
  right shape of full commit/blob/file/author data but is access-gated via an SSH registration process, making it a fallback
  rather than primary source for a short execution window. GHTorrent is confirmed dead infrastructure (its own domain now
  redirects to an unrelated site; its BigQuery mirror is stale since mid-2019). Libraries.io's Zenodo CSV dump is live and
  usable for repo-selection metadata but has no commit-level data. Recommended pull-path: build the repo-selection frame from
  GH Archive/BigQuery or Libraries.io frozen at a historical year Y, then obtain each selected repo's full commit/file history
  via plain unauthenticated git clone (unlimited, token-free, independent of the repo's current activity status), honestly
  noting that repos later made fully private or deleted will still be lost. Includes 18 numbered sources and explicit confidence/caveat
  notes on unverified specifics (BigQuery sandbox scan limits, exact Maturity Model diversity-criteria codes).
type: research
title: OSS Community-Health Positioning and Bias-Free Data Sources
id: art_ZAquYQUNc_3n

summary: >-
  This artifact builds github_founder_departure_commits_non_conditioned, a companion/superset corpus to iter_1's github_founder_departure_commits
  dataset for founder-departure Truck-Factor/DOA (departure-of-author) survival analysis. It pools two explicit sampling frames
  into one exp_sel_data_out-schema dataset, tagged per-example via metadata_sampling_frame: (1) 'liveness_non_conditioned'
  repos discovered this iteration via the GitHub Search API using queries that combine a historical repository-creation window
  (2009-2016), EITHER archived:true OR a stale pushed:<2020 filter, and a language sweep across 10 ecosystems -- with NO filter
  on current stars, fame, or liveness, unlike iter_1's hand-curated 'currently prominent' candidate list; and (2) 'liveness_conditioned'
  repos, the 12 successfully-extracted repos from iter_1's original corpus, carried forward unmodified and retro-tagged so
  downstream code can filter or stratify by frame instead of silently mixing a survivorship-biased sample with an unbiased
  one. code/find_candidates.py ran ~60 GitHub Search API queries (unauthenticated, 10 req/min limit -- no GITHUB_TOKEN was
  present in this environment, verified via curl against /rate_limit before writing the script) and discovered 700 unique
  liveness_non_conditioned candidate repos, checkpointed to temp/non_conditioned_candidates.json. code/build_dataset.py then
  attempted to fetch metadata (GitHub REST API, 60 req/hour) and clone+extract full commit history (git clone --bare + git
  log --numstat, matching iter_1's extraction method exactly: per-commit author email/name/date and per-file insertion/deletion
  counts, no blob content) for those candidates, deliberately WITHOUT iter_1's archived-repo rejection or star-count floor
  (the two filters that would reintroduce liveness/fame conditioning), keeping only a >=3.0 year total commit-history-span
  filter needed to run the DOA/Truck-Factor algorithm and score an 18-month post-departure survival window. Within the time
  this pipeline ran, 1 of ~28 attempted candidates (jquery-archive/jquery-metadata, archived=true, 40 commits, 4.0y history)
  passed the history filter and was extracted; the other ~27 were skipped almost entirely for insufficient_history (their
  total commit span never reached 3 years -- most archived/stale repos discovered by this method turn out to have been abandoned
  within 1-2 years of creation, before ever accumulating enough history to be usable for this analysis). This low yield is
  reported honestly and explicitly in full_data_out.json's metadata.yield_report, including the full skip-reason breakdown,
  rather than papered over: it is itself an informative finding (repos that both survive multiple years AND still end up archived/dead
  are a rare intersection versus the much larger population of repos that die early), and it means the specific gap this artifact
  targets -- a non-surviving founder-only TFDD event with sufficient post-departure history -- was NOT found in this batch,
  so downstream eval/experiment artifacts should treat statistical power for that specific claim as unproven from this corpus
  alone. The final dataset has 11 examples total (1 liveness_non_conditioned + 10 liveness_conditioned, matching iter_1's
  own successfully-loaded record count), each a full per-repo record (repo_metadata, commits[], founder_signal, sampling_frame,
  frame_construction_method) identical in shape to iter_1's schema, validated against exp_sel_data_out.json. Both find_candidates.py
  and build_dataset.py checkpoint to disk (temp/non_conditioned_candidates.json, temp/checkpoint.json) and are resumable,
  so a follow-up run with more wall-clock time or an authenticated GITHUB_TOKEN can extend this corpus directly without redoing
  the discovery sweep.
type: dataset
title: Non-Survivorship-Biased Founder Departure Corpus
id: art_apZrIEHXfHos

summary: >-
  This evaluation artifact closes five reviewer-named rigor gaps in the prior founder-departure authority-diffusion pipeline
  (EXPERIMENT art_I5KoOp16hub5, DATASET art_ZuMis522AEPF) by re-analyzing their outputs in a new eval.py, without collecting
  new repos or new methods. (A) Discloses the placebo/window-shuffle permutation scheme exactly from method.py's source: continuous
  with-replacement sampling of window start offsets, per-repo shipped cap of 20 draws (not 500/60/40 as summarized), no cross-stratum
  seed dependence; reports the combinatorial feasible-window space per founder-TFDD repo (741 total feasible start-month positions
  across 5 founder-only-TFDD events found on re-run, vs 6 claimed in the EXPERIMENT summary); re-runs the placebo test at
  budgets 20/100/300 draws per repo (up to 300 achieved in ~113s wall-clock for the largest budget, well under a 20-minute
  cap), reporting a convergence table of null-distribution mean/SD and the theoretical minimum two-sided p-value (1/(k+1))
  at each budget; and proves no true-effect placebo p-value is computable at any budget because method.run_regressions requires
  n>=10 while n_founder_tfdd_events=5, so the disclosure gap is closed but the underlying power gap is not. (B) Computes Wilson
  95% CIs for Avelino et al.'s reported 66% TF=1 rate (n=315, CI [0.606, 0.710]) and this study's own all-TFDD-denominator
  TF=1 rate (CI [0.354, 0.848]), finding the intervals overlap, with an explicit caution that this study's wide small-n interval
  makes 'overlap' weak evidence rather than validation. (C) Spot-checks alias-resolution against live GitHub contributor data
  for 3 of 15 repos (20% of corpus, amoffat/sh, arrow-py/arrow, Kludex/starlette), finding no confirmed bot-as-authority-holder
  or over-merging, one plausible under-merged same-human pair (would slightly deflate diffusion score, not flip classification),
  and one unresolved bot-inflation risk (dependabot[bot] at 159 contributions on Kludex/starlette) that a contributor-list-only
  check cannot rule out without file-level DOA attribution. (D) Emits an exact 15-row repository table (verified live count
  matches the dataset's claimed 15) with repo name, language, stars, forks, history span, TFDD/TF=1/survival status, and diffusion
  metrics, cross-checked directly against the two source JSON files with missing-field flags where applicable. (E) Quantifies
  this corpus's TFDD incidence (73.3% at n=15) and survival rate (100% among detected TFDDs) against Avelino et al.'s published
  16.3% incidence and 40.6% survival via exact binomial and normal-approximation two-proportion tests, both showing large,
  statistically significant deviations in the direction consistent with survivorship bias; and documents a formal 'Residual
  Limitation' section explaining why a survivor-conditioned sampling frame is an inconsistent (not merely imprecise) estimator,
  quoting the DATASET artifact's own 60-req/hour GitHub API rate-limit constraint (15 of ~104 candidate repos completed),
  and giving a concrete falsifiable prediction for a future GITHUB_TOKEN-enabled run, explicitly not claiming the second-frame
  comparison was run. All five parts write into eval_out.json under clearly named top-level keys (permutation_disclosure,
  tf1_ci_comparison, alias_spotcheck, repo_table, survivorship_bias_quantification) plus a top-level overall_verdict summarizing
  which gaps are fully closed with data (A's disclosure, B, D, E's quantification) versus structurally open (A's power problem,
  E's second-frame comparison, C's full-corpus coverage). eval_out.json validates cleanly against the exp_eval_sol_out schema
  (0 errors, 0 warnings after adding numeric eval_* fields to every example); full/mini/preview variants (46KB/35KB/19KB)
  are all far under the 100MB size limit. pyproject.toml pins numpy==2.5.2, pandas==3.0.5, scipy==1.18.0, scikit-learn==1.9.0,
  statsmodels==0.14.6, loguru==0.7.3, psutil==7.2.2, matching the installed .venv exactly. Downstream GEN_PAPER_TEXT should
  present this as closing the disclosure/comparison/reproducibility gaps with concrete numbers while explicitly retaining
  two structurally open limitations (small-n placebo power, single-frame survivorship-bias evidence) as honest scope boundaries
  rather than resolved claims.
type: evaluation
title: Closing the Rigor Gaps in the Diffusion Pipeline
id: art_yOHrviKrh_11
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

YOUR TURN (gen_paper_text): Revise the paper.

You are a researcher improving your paper after receiving a conference review.
Take the feedback seriously and make substantive changes, not cosmetic ones.

1. ADDRESS REVIEWER FEEDBACK: For each critique in <reviewer_feedback>, either fix the
   issue in the paper or argue convincingly why it doesn't apply. Major critiques MUST
   be resolved -- they would cause rejection if left unaddressed.
2. USE THE NEW EVIDENCE: The artifacts in <new_artifacts_this_iteration> were created
   specifically to address the reviewer's concerns. Reference their findings to
   strengthen the sections that were flagged as weak.
3. REWRITE, DON'T PATCH: Don't just append new paragraphs. Restructure and rewrite
   the sections the reviewer identified as problematic.
4. MAINTAIN CONSISTENCY: Ensure the paper aligns with the updated hypothesis.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

FIGURE TYPE — set `figure_type` on every figure. One test decides it: does the figure plot numbers?
  "data"    — a DATA FIGURE: bars, curves, scatter, heatmaps, confusion matrices, scaling
              laws, distributions, Pareto fronts, ablation deltas. Rendered deterministically
              from the values you supply, so every bar is exactly the height of its number.
  "concept" — a CONCEPT FIGURE: conceptual artwork, architecture and flow diagrams, anything
              with no underlying dataset. Drawn by an image model.
If the figure has real numbers behind it, ALWAYS use "data". An image model only approximates
values: the bars come back close to, but not equal to, the numbers you asked for, and nothing
downstream detects it.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison — plots numbers, so a data figure):
  {"id": "fig3", "title": "Performance Comparison", "figure_type": "data", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. Categories: PostgreSQL, Bao, RLQOpt. One series 'Latency'. Values: 4.6, 2.8, 2.0 seconds. Errors: 0.8, 0.5, 0.3. X-axis label 'Optimizer'. Y-axis label 'Latency (s)', range 0-5.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero — no dataset, so a concept figure):
  {"id": "fig1", "title": "System Architecture", "figure_type": "concept", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description. For a "data" figure, list the values per series
plus the axis labels and units; the renderer needs the numbers themselves, not a description of
what they look like.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 4. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Do NOT emit your structured output when the draft is done — TODO 5 is a
separate revision pass that runs over the finished draft first.
TODO 5. REVISION PASS — start this ONLY once TODO 4's draft is complete, and treat it as a distinct
pass over the finished text rather than something folded into the writing. Read
`REVISION_CHECKLIST.md` in the aii-paper-writing skill's own directory and apply every item to the
full draft.

Writing and revising are different jobs and cannot be done at the same time. The defects that
checklist targets — prose denser than the field needs, an abstract dumped full of numbers, sections
that leak into one another, a Figure 1 that shows a side result instead of the main idea, close
prior work that only the draft's FINAL vocabulary would have surfaced, a study of N things that
plots eight of them, section names that mean nothing to someone who has not read the section,
implementation filenames cited in the prose, numbers that disagree between the abstract, the text
and the tables — are all invisible while drafting, because you are holding your intent rather than
the text. Every one is obvious to the first outside reader.

Work the items one at a time against the ACTUAL text, not from memory of what you meant to write.
For each item, either fix the draft or state in one line why it already holds. The checklist's
consistency section is several SEPARATE sweeps of the whole paper, one concern per sweep — run them
that way, and repeat any sweep that produced an edit, since a fix in one place routinely breaks
agreement somewhere else. Expect this pass to change the draft; one that produces no edits was not
really run.

Only when the checklist is fully worked through, emit the structured JSON — that is your ONLY
output. Do NOT compile LaTeX or generate image/figure files at any point.
</todos><user_data>
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
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1')",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Figure title in plain, everyday language \u2014 short and jargon-free. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "figure_type": {
          "description": "Which generator draws this figure. Decide by ONE test: does the figure plot numbers? 'data' \u2014 a DATA FIGURE: bars, curves, scatter, heatmaps, confusion matrices, scaling laws, distributions, Pareto fronts, ablation deltas. Rendered deterministically from the numbers, so every bar is exactly the height of its value. 'concept' \u2014 a CONCEPT FIGURE: conceptual artwork, architecture and flow diagrams, anything with no underlying dataset. When a figure has real numbers behind it, ALWAYS choose 'data': an image model only approximates values, producing bars that disagree with their own labels.",
          "enum": [
            "data",
            "concept"
          ],
          "title": "Figure Type",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "The generator's ONLY input \u2014 it cannot read files. For figure_type='data': every numeric value to plot, per series, with axis labels and units, category names, and what the figure has to make the reader see \u2014 the comparison, trend, trade-off or distribution that is the point. Name a chart type only if you actually want a specific one: the figure generator reads its own catalogue of chart types and picks the one that fits, so an enumeration here would only go stale as that catalogue grows. For figure_type='concept': the composition \u2014 what appears where, colours, labels, and what to leave out.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "aspect_ratio": {
          "default": "21:9",
          "description": "Shape of the figure. '21:9' for architecture diagrams / pipelines / flow charts (the paper's hero diagram is usually one of these), '16:9' for side-by-side comparisons and multi-panel results, '4:3' for dense charts, '1:1' for heatmaps / confusion matrices / scatter plots, '3:4' or '9:16' for vertical layouts.",
          "enum": [
            "1:1",
            "4:3",
            "3:2",
            "16:9",
            "21:9",
            "3:4",
            "9:16"
          ],
          "title": "Aspect Ratio",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "figure_type",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title \u2014 clear, plain-language, and short so a non-expert understands the main contribution at a glance. Aim for about 6-10 words; avoid jargon and acronyms.",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-20 20:51:08 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-paper-writing · 2026-08-20 20:51:10 UTC

The agent loaded the **aii-paper-writing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-writing
description: Academic paper writing guidance for AI research. Covers paper structure, figure placeholders, bibliography building with Semantic Scholar, citation rules, and the mandatory final revision checklist (REVISION_CHECKLIST.md) that every finished draft must be passed through. Does NOT cover LaTeX compilation or figure file generation — see aii-paper-to-latex for that.
---

## MANDATORY: the final revision pass

**`REVISION_CHECKLIST.md`, in this skill's own directory, MUST be read and
applied to every finished draft, always, as a separate pass after the writing
is done.** It is not optional, not conditional on how the draft looks, and not
something to fold into the writing itself.

Writing and revising are different jobs and cannot be done in one pass. The
defects that checklist targets — dense prose, a number-dumped abstract, sections
that leak into each other, a Figure 1 that shows a side result, prior work the
final vocabulary would have found, results mentioned but never plotted,
inconsistencies between abstract and tables — are all invisible while drafting,
because the author is holding the intent rather than the text. Every one of them
is obvious to the first outside reader. Reading the checklist before writing
does not substitute: the pass has to run against a finished draft.

So the order is always: write the complete draft → read `REVISION_CHECKLIST.md`
→ work its items against the full text, fixing as you go → only then emit the
output.

## Technical Papers

Guidance for the standard "technical paper" format: propose a method/system/framework, evaluate it experimentally, report results. This is the main track at most CS venues (NeurIPS, ICML, ICLR, ACL, AAAI, etc.). Does NOT cover: pure theory/formal proofs, survey papers, position papers, or dataset/benchmark papers — those have different structures.

### Paper Structure

Target 6-8 pages. Use formal academic language, third person. Support claims with evidence from artifacts.

#### Rough Page Budget (8-page paper)

| Section | Pages | Notes |
|---|---|---|
| Abstract | 0.3 | Problem, approach, key result |
| Introduction | 1.0-1.5 | The most important section |
| Related Work | 0.5-1.0 | Beginning or end (see below) |
| Methods | 1.5-2.0 | Architecture fig on page 1 |
| Experiments | 1.5-2.0 | Setup + results + ablations |
| Discussion | 0.5-1.0 | Limitations go here |
| Conclusion | 0.3-0.5 | Do not repeat the abstract |
| References | 0.5-1.0 | Not counted in page limit |

**Critical rule**: A clear new technical contribution must be articulated by page 3 (quarter of the paper). If the reader doesn't know what you did by then, you've lost them.

#### Section Details

**Abstract** (150-250 words): State the problem, your approach, and the main results. Be factual and comprehensive. Do not repeat the abstract word-for-word later in the paper.

**Introduction** — Follow this 5-paragraph structure:

1. **What is the problem?** Define the task concretely.
2. **Why is it interesting and important?** Real-world impact, scale.
3. **Why is it hard?** Why do naive approaches fail?
4. **Why hasn't it been solved before?** What's wrong with prior solutions? How does yours differ?
5. **What are the key components of your approach and results?** Include specific limitations.

End with a "Summary of Contributions" subsection — bullet list of contributions with section references. This doubles as an outline, saving space.

**Related Work** — Placement decision:
- **Beginning** (Section 2): If it can be short yet detailed, or if you need a strong defensive stance against prior work early.
- **End** (before Conclusions): If comparisons require your technical content, or if it can be summarized briefly in the Introduction. Can be titled "Discussion and Related Work."

**Methods/Approach**: Every section tells a story — the story of the results, NOT the story of how you arrived at them. Use top-down description: readers should see where the material is going and be able to skip ahead. Move gory details to appendices.

**Experiments**: Setup (datasets, metrics, baselines) → main results → ablations → analysis. Every claim needs quantitative evidence.

**Discussion**: Interpret results, compare to prior work, state limitations honestly. Limitations should be specific and actionable, not vague disclaimers.

**Conclusion**: Short summarizing paragraph. Do NOT repeat material from the Abstract or Introduction. Make original claims more concrete (e.g., reference quantitative results). Include future work as bullet list — if actively pursuing follow-up, say so to mark territory.

#### Writing Quality Rules

- Define all notation/terminology before use, only once. Group global definitions in Preliminaries.
- Do NOT use nonreferential "this", "that", "these", "it". Always specify the referent. BAD: "This is important because..." GOOD: "This accuracy gap is important because..."
- Do NOT use "etc." unless remaining items are completely obvious. BAD: "We measure volatility, scalability, etc." GOOD: "We measure volatility and scalability."
- Do NOT write "for various reasons" — state the actual reasons.
- "That" is defining, "which" is nondefining. "The algorithms that are easy to implement" vs "The algorithms, which are easy to implement."
- Use italics for definitions and quotes, not for emphasis. Context alone should provide emphasis.

### Figure Format

Figures use a hybrid marker + structured array approach. ALL figures are generated by a separate pipeline step using an AI image model — your `image_gen_detailed_description` is the ONLY input that model sees. It cannot read files or access data. Do NOT generate actual image files yourself (no matplotlib, no PIL, no image generation scripts).

**In paper_text**: Place `[FIGURE:fig_id]` markers where figures should appear.

**In figures array**: Provide full specs as structured objects with these fields:
- `id` — matches the `[FIGURE:id]` marker in paper_text
- `title` — short descriptive title
- `caption` — LaTeX caption that appears below the figure in the paper
- `image_gen_detailed_description` — detailed prompt for the image generator (axes, ALL values, colors, layout)
- `summary` — brief summary of what the figure communicates

Example in paper_text:
```
...our method achieves state-of-the-art results as shown below.

[FIGURE:fig_1]

The results in Figure 1 demonstrate...
```

Example figure spec in figures array:
```json
{"id": "fig_1", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers on JOB benchmark. RLQOpt achieves 2.3x speedup over PostgreSQL.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: ModelA=0.847, ModelB=0.762, Baseline=0.531. Error bars with std: 0.02, 0.03, 0.05. Sans-serif font, white background.", "summary": "Compares accuracy of proposed methods vs baseline."}
```

Every marker in text MUST have a matching figure in the array, and vice versa.

#### Data Precision Requirement

`image_gen_detailed_description` MUST include exact numbers from artifact output files. Read the actual output files before writing figure specs.

- BAD: "Compare accuracy metrics across configurations"
- GOOD: "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: K=3: 0.765, K=5: 0.729, Baseline: 0.121."

#### Figure vs Table Decision

Do NOT create figures for tabular data (rows/columns of text or numbers). Use `\begin{table}` in LaTeX instead. Figures are for actual visualizations only (charts, plots, diagrams).

#### Figure Placement Strategy

Be intentional with figure ordering. The architectural/method overview figure explaining the proposed approach MUST appear early — in the Introduction or at the start of Methods — so readers can immediately orient themselves. Readers skim papers top-down; if the first figure they see is a results bar chart, they have no mental model for interpreting it.

Recommended ordering:
1. **Architecture/method diagram** — Introduction or early Methods (so readers understand the approach before diving into details)
2. **Conceptual/analogy figures** — Introduction or Methods (to build intuition)
3. **Results figures** (bar charts, line plots, scatter plots) — Results section
4. **Analysis/ablation figures** — Discussion or later Results

#### Guidelines

- Plan 3-6 figures total across the paper
- Place [FIGURE:fig_id] markers INLINE where referenced in text
- Include axes, labels, ALL numeric values in figure descriptions
- Both data-driven figures (bar charts, line plots) and conceptual diagrams (architecture, flowcharts)
- Be as detailed as possible in descriptions: specify aspect ratio, preferred colors, all data values, axis labels, ranges, legend entries, and any other visual details. The more specific the description, the better the generated figure

### Bibliography with Semantic Scholar

Build `./references.bib` using the aii-semscholar-bib skill (real BibTeX from Semantic Scholar):

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in one batch
3. Write the returned .bib text into `./references.bib`

Rules:
- Do NOT fabricate BibTeX entries — always fetch from Semantic Scholar
- If a paper isn't found (very recent preprint), write the entry manually as fallback
- Use `\bibliography{references}` and `\bibliographystyle{plainnat}`
- Do NOT use inline `thebibliography` environment

### Citation Format (for Research Artifacts)

When writing research with numbered citations:

1. Every factual claim MUST have a numbered citation: `[1]`, `[2]`, `[1, 3]`, etc.
2. Each source in the "sources" array MUST have an "index" field
3. The index MUST EXACTLY MATCH citation numbers in the text
4. NEVER cite a number without a matching source index
5. Example: "LLMs show 40% improvement with multi-agent collaboration [1]."
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-08-20 20:51:10 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````
