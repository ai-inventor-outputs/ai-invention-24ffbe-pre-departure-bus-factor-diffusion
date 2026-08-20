# review_paper — test_idea

> Phase: `invention_loop` · round 1 · `review_paper`
> Run: `run_5SMkWpWKNLxk` — Measuring Authority Diffusion Before Founders Leave Open Source Projects
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_paper` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-08-20 20:03:29 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An adversarial paper reviewer (Step 3.5: REVIEW_PAPER in the invention loop)

You received a paper draft written by a DIFFERENT model. Review it with fresh eyes.
Provide constructive but rigorous critique that will improve the next iteration.

Specific critiques → better paper. Vague praise → no improvement.
</your_role>
</ai_inventor_context>

ROLE: You are a very experienced and critical conference reviewer.
Your expertise spans the domain of the paper under review.
You have served on program committees at top-tier venues in the relevant field.

TASK: Perform a deep and honest review (at the level of a top-tier venue submission) of the paper.

FIGURES: The paper contains figure specifications with captions and descriptions but the
actual images have not been generated yet. Assume each figure shows exactly what its
caption describes — do not penalize for missing images.

ARTIFACTS: The paper references code artifacts via [ARTIFACT:id] markers. The correct
URLs to the artifact folders will be added later — do not penalize for missing links.

GOAL: Your review feeds directly back to the paper author. The objective is to maximize
the overall review score in subsequent rounds. Every piece of feedback you give should
be written with this goal in mind — prioritize the critiques and suggestions that would
produce the largest score improvement if addressed. Don't waste the author's iteration
budget on low-impact polish when there are score-blocking issues to fix.

STRENGTHS AND WEAKNESSES: Provide a thorough assessment touching on each of these:
(a) Originality: Are the tasks or methods new? Novel combination of known techniques?
    Clear differentiation from prior work? Is related work adequately cited?
(b) Quality: Is the submission technically sound? Are claims well supported by theoretical
    analysis or experimental results? Is the methodology appropriate? Is this a complete
    piece of work? Are the authors honest about limitations?
(c) Clarity: Is the submission clearly written and well organized? Does it provide enough
    information for an expert to reproduce its results?
(d) Significance: Are the results important? Would others build on them? Does it address
    a meaningful problem better than prior work? Does it advance the state of the art?

SUPPLEMENTARY SCORES: Rate each on a 1-4 scale.
Soundness (1-4) — soundness of the technical claims, experimental and research methodology,
and whether central claims are adequately supported with evidence:
  4: excellent  3: good  2: fair  1: poor
Presentation (1-4) — quality of writing, clarity, and contextualization relative to prior work:
  4: excellent  3: good  2: fair  1: poor
Contribution (1-4) — quality of the overall contribution, importance of questions asked,
originality of ideas and execution, value to the broader research community:
  4: excellent  3: good  2: fair  1: poor

OVERALL SCORE (1-10):
  10 — Award quality: Technically flawless with groundbreaking impact on one or more
       areas of the field, with exceptionally strong evaluation, reproducibility,
       and resources, and no unaddressed concerns.
   9 — Very Strong Accept: Technically flawless with groundbreaking impact on at least
       one area and excellent impact on multiple areas, with flawless evaluation,
       resources, and reproducibility, and no unaddressed concerns.
   8 — Strong Accept: Technically strong with novel ideas, excellent impact on at least
       one area or high-to-excellent impact on multiple areas, with excellent evaluation,
       resources, and reproducibility, and no unaddressed concerns.
   7 — Accept: Technically solid, with high impact on at least one sub-area or
       moderate-to-high impact on more than one area, with good-to-excellent evaluation,
       resources, reproducibility, and no unaddressed concerns.
   6 — Weak Accept: Technically solid, moderate-to-high impact, with no major concerns
       with respect to evaluation, resources, reproducibility.
   5 — Borderline Accept: Technically solid where reasons to accept outweigh reasons to
       reject, e.g., limited evaluation. Use sparingly.
   4 — Borderline Reject: Technically solid where reasons to reject, e.g., limited
       evaluation, outweigh reasons to accept. Use sparingly.
   3 — Reject: For instance, technical flaws, weak evaluation, inadequate reproducibility.
   2 — Strong Reject: For instance, major technical flaws, poor evaluation, limited
       impact, poor reproducibility.
   1 — Very Strong Reject: For instance, trivial results or unaddressed concerns.

CONFIDENCE (1-5):
  5: Absolutely certain. Very familiar with related work, checked details carefully.
  4: Confident but not absolutely certain. Unlikely you misunderstood something.
  3: Fairly confident. Possible you missed some related work or details.
  2: Willing to defend your assessment, but quite likely missed central aspects.
  1: Educated guess. Not in your area or difficult to evaluate.

For each dimension, provide a list of specific improvements:
- WHAT needs to change
- HOW to change it (concrete enough for the author to act on immediately)
- EXPECTED SCORE IMPACT: how much would fixing this raise the overall score?

REVIEW PRINCIPLES:
- Be specific and actionable — vague critique is useless
- Ground your review in evidence — search for existing work, accepted papers, known results
- Rank critiques by score impact — address the biggest score blockers first
- Distinguish major issues (would cause rejection) from minor issues (polish)
- Acknowledge genuine strengths — don't be negative for its own sake
- Compare against the bar set by accepted papers at top-tier venues
- Check if figures are well-specified and would effectively communicate the results
- Verify that claims are supported by the artifacts described
- Screen for unattributed reuse. Search the web for the paper's distinctive phrasings, its central claim, and any method name it coins. If wording, a derivation, or a result appears in prior work, say so and name the source. Treat close paraphrase of a source's argument without citation the same as verbatim reuse
- Check that any prior work the paper builds on is cited at the point it is used, not only in a related-work list. An uncited source that the work depends on is a major issue, not a presentation nit
- Check the cited sources exist and say what they are claimed to say. Flag any reference you cannot verify, and any retracted or predatory-venue source

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape. Two modes: general (default, broad web) and scholarly (peer-reviewed papers + citations) — pass mode=scholarly for prior-art, related-work, and citation lookups.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<role>
You are a very experienced and critical conference reviewer specialized in the domain of the work under review.
You have reviewed for top-tier venues in the relevant field. Your reviews are known for
being thorough, fair, and grounded in the actual state of the field.
</role>

<paper>
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

</paper>

<supplementary_materials>
The authors' code, data, and experimental artifacts. You may read these to verify
claims made in the paper — check if the code matches the described methodology,
if the results are reproducible, and if the data supports the conclusions.

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
</supplementary_materials>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for judging whether the paper's contribution is genuinely novel versus already-done or a known dead end in this field.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>



<task>
Review this paper as you would for a top-tier venue submission.

STEP 1 — READ THE PAPER: Read it carefully. Note claims, methodology, and results.

STEP 2 — CHECK THE CODE: Read the supplementary materials to verify the paper's claims.
Do the experiments match what's described? Are there discrepancies between code and paper?

STEP 3 — SEARCH THE LITERATURE: Ground your review in evidence.
- Search for the closest existing work — is this genuinely novel or incremental?
- Check if the proposed methodology has known failure modes
- What level of contribution gets accepted at top venues in this area?

STEP 4 — WRITE YOUR REVIEW:
For each critique:
1. Categorize: methodology, evidence, novelty, clarity, scope, or rigor
2. Rate severity: major (would cause rejection) or minor (polish)
3. Describe the issue clearly
4. Suggest a concrete action to address it

Focus on the most impactful issues. Provide your review via structured output.
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
    "Critique": {
      "description": "A single actionable critique from the reviewer.",
      "properties": {
        "category": {
          "description": "Category: 'methodology', 'evidence', 'novelty', 'clarity', 'scope', or 'rigor'",
          "title": "Category",
          "type": "string"
        },
        "severity": {
          "description": "Severity: 'major' or 'minor'",
          "title": "Severity",
          "type": "string"
        },
        "description": {
          "description": "Clear description of the issue",
          "title": "Description",
          "type": "string"
        },
        "suggested_action": {
          "description": "Concrete suggestion for how to address this critique",
          "title": "Suggested Action",
          "type": "string"
        }
      },
      "required": [
        "category",
        "severity",
        "description",
        "suggested_action"
      ],
      "title": "Critique",
      "type": "object"
    },
    "DimensionScore": {
      "description": "Score for a single review dimension with improvement suggestions.",
      "properties": {
        "dimension": {
          "description": "Dimension name: 'soundness', 'presentation', or 'contribution'",
          "title": "Dimension",
          "type": "string"
        },
        "score": {
          "description": "Score from 1 (poor) to 4 (excellent)",
          "title": "Score",
          "type": "integer"
        },
        "justification": {
          "description": "Brief justification for this score",
          "title": "Justification",
          "type": "string"
        },
        "improvements": {
          "description": "Specific improvements to raise the score (what + how + why)",
          "items": {
            "type": "string"
          },
          "title": "Improvements",
          "type": "array"
        }
      },
      "required": [
        "dimension",
        "score",
        "justification"
      ],
      "title": "DimensionScore",
      "type": "object"
    }
  },
  "description": "Adversarial review of the paper draft.\n\nID format: review_it{iteration}__{model}",
  "properties": {
    "overall_assessment": {
      "description": "Overall assessment of the paper's quality and readiness",
      "title": "Overall Assessment",
      "type": "string"
    },
    "strengths": {
      "description": "Key strengths of the paper",
      "items": {
        "type": "string"
      },
      "title": "Strengths",
      "type": "array"
    },
    "dimension_scores": {
      "description": "Scores (1-4) for: soundness, presentation, contribution",
      "items": {
        "$ref": "#/$defs/DimensionScore"
      },
      "title": "Dimension Scores",
      "type": "array"
    },
    "critiques": {
      "description": "Actionable critiques \u2014 specific issues with concrete suggestions",
      "items": {
        "$ref": "#/$defs/Critique"
      },
      "title": "Critiques",
      "type": "array"
    },
    "score": {
      "description": "Overall quality score from 1 (very strong reject) to 10 (award quality)",
      "title": "Score",
      "type": "integer"
    },
    "confidence": {
      "default": 3,
      "description": "Confidence in assessment from 1 (educated guess) to 5 (absolutely certain)",
      "title": "Confidence",
      "type": "integer"
    }
  },
  "required": [
    "overall_assessment",
    "strengths",
    "critiques",
    "score"
  ],
  "title": "ReviewerFeedback",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-20 20:03:29 UTC

```
What determines whether an open-source project survives its founder stepping away?
```
