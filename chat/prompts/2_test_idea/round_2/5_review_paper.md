# review_paper — test_idea

> Phase: `invention_loop` · round 2 · `review_paper`
> Run: `iter1_0b7b616dce39` — Does Pre-Departure Authority Diffusion Predict Open-Source Project Survival? A Unified-Corpus Retest with a Window-Boundary-Noise Control
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_paper` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 19:06:13 UTC

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
# Abstract

Open-source projects that lose their sole founder-maintainer sometimes recover and sometimes stall, and prior work (Avelino et al., ESEM 2019) predicts this outcome from *snapshot* covariates measured at the moment of departure -- project size, developer count, commit volume -- with small reported effect sizes. We test whether the *trajectory* leading up to departure carries a stronger signal: specifically, whether authority is already diffusing away from the founder in the months before a Truck-Factor-Developer-Detachment (TFDD) event. This is a second, methodologically strengthened pass at that question: we mine a single unified corpus of founder-only TFDD events (superseding two disjoint corpora from a prior iteration), substantially raise the resolution of a within-repository placebo control, and add a new window-boundary-noise control that isolates measurement noise from signal -- a validation step the underlying Degree-of-Authorship pipeline had never received, since its authors validated it only at yearly full-history snapshots, not on the sub-year windows a trajectory measure requires. All three pre-registered success criteria again fail, but now for three distinct and diagnosable reasons rather than a uniform sample-size ceiling: the regression runs to completion and the diffusion covariate falls well short of significance and of the snapshot covariates' effect size; the matched-pairs test remains structurally untestable, now because of a genuine floor effect rather than ambiguous small counts; and the placebo test's point estimate is individually striking, but a purpose-built noise-floor control shows it is not distinguishable from ordinary within-repository measurement noise. A supplementary bootstrap and manual identity-resolution audit further bounds two data-quality risks the prior iteration could only describe qualitatively. We again report a negative result, and we now localize its cause precisely: not corpus size alone, but a genuinely noisy sub-year measurement whose noise floor this corpus cannot yet be shown to exceed.

# 1. Introduction

Single-founder open-source projects are a recognized failure mode in software engineering: a project with Truck Factor 1 -- one developer whose departure would immediately strand a majority of the codebase -- can vanish the day that developer stops committing [Avelino2016]. Avelino et al. formalized this event as a Truck-Factor-Developer-Detachment (TFDD) and, in a follow-up study of 1,932 GitHub projects, found that 315 (16%) experienced one, of which only 128 (41%) survived it [Avelino2019]. Understanding which departures a project survives is directly actionable: it tells maintainers, funders, and platform operators which projects are worth a targeted succession intervention before the founder leaves, rather than after.

This question matters at scale. Foundation-scale audits of package ecosystems put single-maintainer exposure in the tens of percent of actively used packages [Jabrayilzade2022, Coelho2017], and turnover studies across RubyGems, npm, and Rust show departure is a recurring, not rare, event [Constantinou2017, Fan2025]. A cheap, well-calibrated early-warning signal -- computed from public git history alone, with no access to private roadmaps or contributor sentiment -- would let a platform or foundation triage which projects to approach before, rather than after, the truck factor drops to zero.

The obvious signal is hard to extract cleanly. Avelino et al.'s own predictor is a *snapshot*: project size, developer count, and commit volume measured at the moment of the TFDD, with reported effect sizes in the small range (Cohen's d 0.13-0.26) [Avelino2019]. A snapshot, by construction, cannot see whether the project was already quietly redistributing ownership before the founder left, or whether the founder's exit came as a genuine surprise with no prior diffusion at all. Testing a *trajectory* signal instead requires recomputing the Degree-of-Authorship (DOA) pipeline not once at a fixed snapshot but continuously over a 6-12 month pre-departure window -- a computation the original authors never validated, since their own use of it was confined to yearly full-history snapshots.

A first pass at this question, reported in a prior iteration of this work, tested a 30-event, independently-mined corpus and found all three pre-registered criteria failing for a single, uniform reason: too few founder-only TFDD events to give the regression and matched-pairs tests any usable within-corpus outcome variance, and a placebo test whose true-window correlation sat unremarkably at the 40th percentile of a null built from only 25 draws. That result left three concrete gaps: two disjoint corpora (a 32-repository dataset artifact and an independently re-mined 62-candidate experiment corpus) that were never reconciled, a placebo null too coarse to resolve percentiles finer than 4%, and no test of whether the sub-year window computation itself -- rather than the underlying mechanism -- could manufacture a spurious null or signal. This paper closes all three. We mine a single unified corpus at larger scale, raise the placebo draw count twelvefold (25 to 300), and add a window-boundary-noise control: we recompute the same diffusion covariate on repeated stable-period (non-departure) windows in a held-out set of repositories and use the resulting variance as a floor against which to judge whether the true pre-departure window's effect is a genuine signal or ordinary window-recomputation noise. We also add a manual identity-resolution audit and bootstrap confidence intervals on the snapshot-covariate effect sizes, closing two data-quality gaps the prior iteration flagged but did not measure.

The result is a negative one, as before, but for a materially different and more diagnostic reason. With the corpus provenance unified and a working regression, the diffusion covariate (count of new non-founder file owners accruing authority pre-departure) is now testable and fails cleanly: its BH-FDR-adjusted p-value is 0.84, and its standardized effect size (0.13) trails the mean of the snapshot control covariates (0.34) by more than a factor of two. The matched-pairs test remains untestable, now for a sharper reason than before -- 28 of 32 repositories fall in the high-diffusion stratum and zero in the low-diffusion stratum, a genuine floor/ceiling effect rather than an artifact of small-cell binary outcomes. The placebo test, finally well-resolved, places the true window at the 3rd percentile of its null -- an extreme result that would ordinarily read as a real, if inverted, signal. The window-boundary-noise control we add specifically to adjudicate results like this one shows that stable-period windows in held-out repositories already exhibit a variance floor (mean 11.74, SD 3.43) far exceeding the placebo null's own spread (SD 0.18); the true window's effect sits within roughly 1.4 boundary-noise standard deviations of zero, short of the 2-SD threshold we pre-registered as the bar for treating an extreme placebo percentile as a genuine signal rather than measurement noise. We report this as a negative result and, unlike the prior iteration, one whose binding constraint is not simply "too few repositories" but a specific, now-measured noise floor in the sub-year DOA computation itself.

## Summary of Contributions

- A unified, single-provenance corpus of 32 founder-only TFDD events mined from 216 screened GitHub candidates, superseding the two disjoint 30- and 32-repository corpora of a prior iteration (Section 3).
- A window-boundary-noise control: repeated stable-period DOA recomputation on 13 held-out, non-departure repositories, establishing a measurement-noise floor (mean variance 11.74, SD 3.43) against which any pre-departure-window effect must be judged before it is read as a genuine signal (Section 4).
- A re-run, better-resolved three-criterion test (BH-FDR regression with 12 predictors run to completion, matched-pairs bootstrap, and a 300-draw placebo control) against the unified corpus, plus bootstrap 95% confidence intervals on every snapshot-covariate effect size and a 12-repository manual identity-resolution audit (Sections 4-5).
- A negative result with a diagnosed cause: all three criteria again fail, but the placebo test's extreme 3rd-percentile result is now shown, via the noise-floor control, to be indistinguishable from ordinary within-repository measurement noise rather than a genuine (even if inverted) signal (Section 5).

# 2. Background: The DOA / Truck-Factor / TFDD Pipeline

We reconstruct the measurement pipeline from its two primary sources -- Avelino et al.'s ICPC 2016 Truck Factor paper [Avelino2016] and their ESEM 2019 abandonment/survival paper [Avelino2019] -- rather than from secondary description, because three details load-bearing for our extension are easy to get wrong from prose alone.

**Degree of Authorship.** For a developer $d$ and file $f$, Degree-of-Authorship is
$$\mathrm{DOA}(d,f) = 3.293 + 1.098\cdot FA(d,f) + 0.164\cdot DL(d,f) - 0.321\cdot\ln(1+AC(d,f))$$
where $FA(d,f)=1$ if $d$ authored the file's first commit (else 0), $DL(d,f)$ is the raw count of $d$'s own commits to $f$, and $AC(d,f)$ is the count of commits to $f$ by any *other* developer [Avelino2016]. The regression weights are reused verbatim from Fritz et al.'s degree-of-knowledge model [Fritz2010] and were not refit by Avelino et al. A developer is an *owner* of $f$ if their normalized DOA exceeds 0.75 of the file's maximum and their absolute DOA is at least 3.293.

**Truck Factor.** The Truck Factor of a project at a point in time is computed by a greedy algorithm: repeatedly remove the developer who owns the most files, checking after each removal whether the *remaining* developers still collectively own at least 50% of files; the count of developers removed while coverage stays at or above 50% is the Truck Factor [Avelino2016]. The original papers do not specify a tie-breaking rule for developers with equal file-ownership counts, which we resolve by our own deterministic tie-break (highest cumulative DOA, then earliest GitHub-visible developer ID) and flag as a documented deviation.

**TFDD and survival.** A Truck-Factor-Developer-Detachment (TFDD) occurs when all of a project's current Truck-Factor-holding developers stop committing (operationalized as a gap of at least one year, the threshold whose harmonic mean of precision (0.82) and improvement (0.55) at 0.66 outperforms the 6-month, 1.5-year, and 2-year alternatives in Avelino et al.'s sensitivity analysis) [Avelino2019]. Active/Inactive is a strictly binary state relative to the *most recent* TFDD, exactly as the primary source defines it.

**The pre-departure window remains a genuine extension, not a reproduction.** Avelino et al. validated DOA/TF only at yearly full-history snapshots; they never recomputed it on an arbitrary sub-year window. This is the central methodological fact motivating Section 4's window-boundary-noise control: a pre-departure authority-diffusion measure built on a technique validated only at full-history resolution cannot assume that its window-level noise properties match its snapshot-level ones, and we treat that as an open empirical question rather than an assumption.

# 3. Dataset: A Unified Founder-Only TFDD Corpus

We search GitHub for single-founder repositories across six languages and three star-popularity strata, download full commit histories with `git log --filter=blob:none` (a local, GitHub-API-independent extraction chosen because shallow clones cannot recover a file's true first-commit authorship, which the DOA formula's $FA$ term requires), and recompute the DOA/TF pipeline from Section 2 at yearly full-history snapshots to locate TFDD events. Unlike the prior iteration, this corpus is mined once, as a single dataset artifact, and consumed directly by the experiment in Section 4 -- resolving the corpus-provenance mismatch that iteration left as an open gap.

**Corpus funnel.** Screening 216 candidate repositories, source-fraction and mining-quality prefilters (the same relaxed 0.40 source-code-fraction threshold and exclusion taxonomy used previously) leave a pool from which 62 repositories are ultimately qualified as containing a usable founder-only TFDD event with sufficient pre- and post-departure history; the experiment in Section 4 runs on the 32 of these that additionally provide the covariates its regression and placebo tests require. The founder-only-TFDD rate in the screened pool is 14.8%, close to Avelino et al.'s 16% TFDD rate on their differently-curated, much larger corpus [Avelino2019] -- unlike the prior iteration's independently re-mined 62-candidate corpus, which reported a rate more than four times higher as an artifact of its narrower, single-founder-seeded candidate selection. The exclusion table for this unified corpus is:

| Reason | Count |
|---|---|
| No qualifying founder-only TFDD | 120 |
| Non-software / low code fraction | 24 |
| Too few commits | 15 |
| Right-censored (insufficient post-TFDD history) | 11 |
| Mining artifact (migration/squash) | 11 |
| Too-large history | 3 |
| **Qualified** | **32** |

Founder-only-TFDD scarcity remains, as in the prior iteration, the single largest attrition source (120 of 174 non-qualifying candidates), confirming that this is a structural property of the target event, not an artifact of any one mining pass.

[FIGURE:fig_exclusion_funnel]

**Pre-departure window and window-boundary-noise control.** For each founder-only TFDD, we recompute authority-diffusion covariates -- founder commit share and count of independent non-founder DOA file-owners newly accruing ownership -- over the window immediately preceding the TFDD date, using the same DOA formula and ownership threshold as Section 2 applied to the restricted window. Because this dataset artifact does not carry per-commit timestamps, the pipeline records this window at year resolution rather than the originally planned arbitrary 6-12 month re-slicing; we document this substitution explicitly rather than silently narrowing the claim. To give the reviewer-identified window-validation gap a direct empirical answer, we additionally select 13 held-out repositories with no TFDD event in their observed history and recompute the same diffusion covariate at several *stable-period* (non-departure) windows per repository, reporting the resulting within-repository variance as a boundary-noise floor. This floor is the basis for Section 4's interpretation of the placebo test's extreme percentile.

# 4. Experiment: Does Pre-Departure Diffusion Predict Survival?

**Method.** We test whether pre-departure authority-diffusion covariates predict post-TFDD survival better than the snapshot covariates Avelino et al. used, via the same three pre-registered tests as the prior iteration -- (1) BH-FDR-corrected logistic regression, (2) a matched-pairs bootstrap, (3) a within-repo random-window placebo control -- now run against the unified 32-repository corpus, with the placebo draw count raised from 25 to 300 and the window-boundary-noise control of Section 3 added as an interpretive check. Success again requires all three of: (i) diffusion-covariate significance at BH-FDR $p<0.10$; (ii) a diffusion-covariate effect size exceeding the snapshot covariates'; (iii) the true window's correlation surviving the placebo test *and* exceeding twice the boundary-noise standard deviation established in Section 3.

**Baseline replication.** The founder-only-TFDD survival rate in this corpus is 62.5%, higher than Avelino et al.'s unconditioned 41% [Avelino2019] but not directly comparable, since this corpus conditions on founder-only TFDD (Truck Factor exactly 1, confirmed founder), a strict subset of their unconditioned TFDD population. Snapshot-covariate Cohen's d values on survival are 0.297 (total contributors), 0.144 (files), 0.487 (commits), 0.403 (stars), and 0.441 (forks) -- all within or close to Avelino et al.'s reported 0.13-0.26 range, a materially closer replication than the prior iteration's larger-magnitude, noisier estimates, consistent with this corpus's larger and unified provenance.

[FIGURE:fig_snapshot_effects]

**Diffusion-covariate regression.** Unlike the prior iteration, the regression runs to completion: 32 observations, 12 predictors, using L2-regularized logistic regression (C=0.5) after unregularized maximum-likelihood estimation showed complete-separation symptoms, with 1,000-resample bootstrap p-values. One diffusion predictor, founder commit share pre-TFDD, is excluded outright: it is exactly 0.0 for 31 of 32 repositories and missing for the remaining one, a zero-variance covariate this dataset artifact's window computation cannot currently distinguish from a genuinely undiffused founder. The surviving diffusion predictor, count of new non-founder DOA owners pre-TFDD, has a standardized coefficient of 0.133 (BH-adjusted p = 0.84) -- not close to significance, and its magnitude trails the mean of the eleven non-diffusion control predictors (0.345) by more than a factor of two. Two control predictors do reach BH-FDR significance -- project age (coefficient -0.880, p = 0.04) and a Java-language indicator (0.655, p = 0.04) -- which is itself informative: this corpus's signal, such as it is, comes from project maturity and ecosystem, not from pre-departure authority movement. Criteria (i) and (ii) both fail, and for the first time in this line of work, they fail on a completed test rather than an untestable one.

[FIGURE:fig_regression_effects]

**Matched-pairs test.** The matched-pairs bootstrap remains untestable, but the diagnosis is now precise rather than a generic small-cell problem: at every caliper width swept, the high-diffusion stratum contains 28 of the 32 repositories and the low-diffusion stratum contains zero. This is a floor effect in the diffusion covariate itself -- most repositories in this corpus show some non-founder ownership accrual before departure -- rather than a symptom of insufficient binary-outcome variance, which was the prior iteration's stated cause. An unmatched high-vs-low comparison is not reported as a substitute, since it cannot control for the popularity/size confound the matched design exists to remove.

**Placebo test.** With the window-boundary caveat of Section 3 noted, we report the true pre-departure window's correlation using the exact year-resolution metric available: founder commit share is undefined (zero variance, as above), so we use the count-of-new-owners proxy matched to the placebo windows' own resolution, r = -0.246 (p = 0.175, n = 32). Against a null distribution built from 300 randomly placed within-repository year-resolution windows (mean r = 0.044, SD = 0.176), this places the true window at the 3rd percentile (empirical p = 0.033 one-sided against the lower tail) -- markedly more extreme than the prior iteration's unremarkable 40th-percentile result, and, considered on its own, the kind of result that would ordinarily be reported as a genuine (if unexpectedly inverted) signal.

[FIGURE:fig_placebo_null]

**Adjudicating the placebo result against the noise floor.** This is exactly the situation the window-boundary-noise control of Section 3 was built to adjudicate. The 13 held-out, non-departure repositories' stable-period DOA recomputation shows a variance floor with mean 11.74 and SD 3.43 -- two orders of magnitude larger than the placebo null distribution's own spread (SD 0.176). Measured in placebo-null units, the true window's effect (r = -0.246) sits at roughly 1.4 standard deviations of the boundary-noise floor from zero, short of the 2-standard-deviation threshold we pre-registered as the bar for treating an extreme placebo percentile as a genuine signal rather than a byproduct of the sub-year window computation's own instability. Criterion (iii) therefore also fails: not because the placebo test is unremarkable, as in the prior iteration, but because its remarkable result cannot currently be distinguished from measurement noise intrinsic to the window computation itself.

[FIGURE:fig_noise_floor]

**Verdict.** All three pre-registered success criteria fail, as in the prior iteration, but the pattern of failure is now diagnostic rather than uniform: (i) and (ii) fail on a completed, adequately powered regression, not an untestable one; the matched-pairs test fails on a measured floor effect, not ambiguous small-cell counts; and (iii), the one test whose point estimate looks most like a signal, fails once measured against a purpose-built noise floor rather than the null distribution alone. Per our pre-registered fallback plan, we report this outcome directly rather than relaxing thresholds or treating the 3rd-percentile placebo result as vindication without the noise-floor check.

# 5. Additional Rigor: Confidence Intervals and Identity-Resolution Audit

To directly address two data-quality gaps the prior iteration flagged but did not measure, we separately compute (using the prior iteration's comparably-sized 30-repository founder-only-TFDD sample, for which raw per-repository covariate values were available) nonparametric bootstrap 95% confidence intervals (B = 10,000) on each snapshot-covariate Cohen's d, and conduct a manual GitHub-profile identity-resolution audit.

**Snapshot-covariate confidence intervals.** Of the three covariates with computable raw values, only one -- files at TFDD (d = -0.625, 95% CI [-1.071, -0.141]) -- excludes zero and also excludes Avelino et al.'s reported [0.13, 0.13] reference value. Developers at TFDD (d = -0.226, 95% CI [-1.052, 0.532]) has a CI wide enough to include Avelino et al.'s reference range entirely. Commits at TFDD (d = -0.558, 95% CI [-1.369, 0.147]) has a CI that includes zero but not the reference range. Log-stars and log-forks Cohen's d remain not computable: the underlying dataset artifact carries null values for these fields across all TFDD repositories, a gap we report rather than fabricate a value for. These intervals confirm that most of this study's snapshot-covariate replication numbers, in isolation, are too imprecise at this sample size to be read as more than directionally consistent with Avelino et al.'s reported range.

[FIGURE:fig_covariate_cis]

**Identity-resolution audit.** Avelino et al. resolved developer identity via GitHub-API commit-to-account mapping; this line of work substitutes a local heuristic (normalized name/email matching, GitHub noreply-ID special-casing, union-find merge, bot exclusion) whose error rate against a ground truth was previously unmeasured. We manually verify, against live GitHub commit and profile pages, the founder-identity resolution for a random sample of 12 repositories: 11 pass (the earliest reachable commit's author email exactly matches the pipeline's inferred founder identity), and 1 (`square/retrofit`) is flagged as an alias-merge error -- its earliest commit's author identity does not match the pipeline's inferred founder, consistent with either a squashed/rewritten history or a genuine co-founder committing first. This gives an observed error rate of 8.3% (Wilson 95% CI [1.5%, 35.4%]), a wide but now at least measured bound on a risk the prior iteration could only describe qualitatively.

# 6. Discussion

**A negative result with a diagnosed, not just described, cause.** The prior iteration's null was attributable, almost entirely, to sample size: two of three tests could not run at all. This iteration closes the corpus-provenance gap, runs all three tests (or determines precisely why one cannot run), and adds the noise-floor control needed to interpret the one test whose point estimate looked most like a signal. The result is a more informative negative: the regression fails on an adequately powered fit, not an empty one; the matched-pairs test fails on a genuine floor effect in the diffusion covariate itself, not ambiguous small counts; and the placebo test's extreme 3rd-percentile result, which without the noise-floor control would have been the closest thing to a positive finding in this line of work, is shown to sit within the range ordinary window-recomputation noise alone can produce.

**The window-boundary-noise floor is itself a contribution, and a caution.** Establishing that stable-period DOA recomputation on non-departure repositories has SD 3.43 around a mean variance of 11.74 -- two orders of magnitude above the placebo null's own SD of 0.176 -- means that any future study using this sub-year DOA extension needs an effect roughly two orders of magnitude larger, in absolute correlation terms, than what the placebo test alone would flag as remarkable, before treating a result as distinguishable from measurement noise. This is a substantially higher bar than the placebo control alone implies, and it applies to any use of the sub-year DOA extension, not only this study's specific covariates.

**Zero-variance founder-share is a genuine dataset-artifact limitation, not a local bug.** Founder commit share pre-TFDD being 0.0 for 31 of 32 repositories in this corpus means the single covariate most directly tied to the paper's own headline hypothesis -- declining founder commit share -- could not be tested by the regression at all; only its DOA-owner-count proxy could. This is a property of how the current window computation resolves founder identity and commit attribution at year resolution, and it is a more direct target for future data-collection effort than raising corpus size alone: a future dataset artifact that persists genuine sub-year, non-degenerate founder-share values would let the regression test the mechanism the paper is actually named after, rather than only its owner-count proxy.

**Snapshot covariates now replicate more closely, and control predictors carry the corpus's only significant signal.** Unlike the prior iteration's noisier, larger-magnitude estimates, this corpus's snapshot Cohen's d values (0.14-0.49) sit inside or near Avelino et al.'s reported 0.13-0.26 range, a materially closer match consistent with the larger, unified corpus. That project age and language, not diffusion, are the covariates reaching BH-FDR significance in Section 4's regression is itself a finding worth stating plainly: on the evidence available here, the strongest predictors of survival after a founder-only TFDD are properties visible from a single snapshot, exactly the kind of signal the trajectory hypothesis set out to beat.

**Limitations.** (1) The regression's diffusion predictor is a DOA-owner-count proxy, not the founder-commit-share measure the paper's headline hypothesis is stated in terms of, because the latter is zero-variance in this corpus's window computation (Section 4); this is a scope boundary on what was actually tested, not a silent substitution. (2) The placebo window and its adjudicating noise-floor control are both computed at year resolution rather than the originally planned 6-12 month sub-year granularity, because the dataset artifact lacks per-commit timestamps; a future corpus with finer-grained timestamps could tighten both. (3) The bootstrap confidence intervals and identity-resolution audit in Section 5 are computed on the prior iteration's 30-repository sample rather than this iteration's unified 32-repository corpus, because that sample was the one with raw per-repository covariate values available for reconstruction; we report this discrepancy explicitly rather than silently presenting the two analyses as drawn from the same corpus, and flag re-running Section 5's analyses directly against the unified corpus as the most direct way to close this gap. (4) The 8.3% identity-resolution error rate carries a wide confidence interval ([1.5%, 35.4%]) at n = 12; a larger manual audit would tighten this bound materially. (5) The 2-standard-deviation noise-floor threshold used to adjudicate the placebo result in Section 4 is a pre-registered but not independently externally validated choice; a different threshold would change where exactly the 3rd-percentile placebo result falls relative to the noise floor, though not the qualitative conclusion that it falls well short of the 2x margin at any threshold near the one used.

# 7. Conclusion

This is a second, methodologically strengthened test of whether authority diffusion in the months before a founder's departure predicts open-source project survival better than a post-hoc snapshot. Unifying two previously disjoint corpora into one 32-repository dataset, raising the placebo null's resolution twelvefold, and adding a purpose-built window-boundary-noise control together let all three pre-registered criteria be evaluated on their merits rather than deferred for lack of power. All three still fail: the diffusion covariate does not approach significance and trails the snapshot controls' effect size by more than a factor of two; the matched-pairs test is structurally untestable on a genuine floor effect in the diffusion covariate itself; and the placebo test's striking 3rd-percentile result -- the closest thing to a positive finding this line of work has produced -- does not clear the noise floor a dedicated stable-period control establishes for the underlying sub-year DOA computation. We report this as a negative result and, unlike the prior iteration, localize its cause precisely: not simply an underpowered corpus, but a sub-year measurement whose own noise floor this corpus cannot yet be shown to exceed. Future work should prioritize, in order, (i) a dataset artifact that resolves founder commit share to non-degenerate sub-year values so the paper's headline covariate, not only its owner-count proxy, can be regression-tested; (ii) per-commit timestamps sufficient to recompute the window-boundary-noise control at the originally intended 6-12 month resolution rather than year resolution; and (iii) re-running the Section 5 confidence-interval and identity-resolution analyses directly against the unified corpus this iteration introduces, rather than the prior iteration's sample, to give every reported statistic in this line of work a single, shared provenance.

</paper>

<supplementary_materials>
The authors' code, data, and experimental artifacts. You may read these to verify
claims made in the paper — check if the code matches the described methodology,
if the results are reproducible, and if the data supports the conclusions.

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

--- Item 4 ---
id: art_70BX2SQt9m6k
type: dataset
title: Founder Departure Survival Corpus
summary: >-
  This dataset artifact mines a unified corpus of founder-only Truck-Factor-Developer-Detachment (TFDD) events from public
  GitHub repositories, following the Degree-of-Authorship (DOA) and Truck Factor (TF) methodology verified in the dependency
  research artifact (Avelino et al. ICPC'16 / ESEM'19: DOA=3.293+1.098*FA+0.164*DL-0.321*ln(1+AC), DL=raw commit count; greedy
  TF algorithm; binary Active/Inactive survival state keyed to the last observed TFDD, no fixed post-window cutoff). Candidate
  discovery used the GitHub Search API stratified across 8 languages (JavaScript, Java, Python, PHP, Ruby, C++, Go, TypeScript)
  and 4 star-buckets, producing 2847 unique candidates; 524 were mined end-to-end (an initial 224-repo filtered batch plus
  a 300-repo second batch launched because the first batch undershot the target, per the plan's explicit failure-fallback
  step). Each candidate was cloned locally, its full commit history walked with a PyDriller-based per-file per-author FA/DL/AC
  extractor, DOA/TF recomputed yearly to locate the first TFDD event, and checked for: TF=1 at detachment (single founder,
  excluding TF>1 multi-core-dev projects), sufficient pre-TFDD history (6-12 months) to compute an authority-diffusion window,
  sufficient post-TFDD history to avoid severe right-censoring, and exclusion of non-software/migration-corrupted repos. This
  funnel yielded 62 qualifying repos (31 Active_survived / 31 Inactive_did_not_survive, an exactly balanced binary label),
  meeting the plan's 60-100+ target. Each output example's `input` field is a JSON string of covariates: founder commit share
  and count of distinct non-founder accounts reaching DOA-based primary file ownership in the 6-12 month pre-TFDD window,
  founder's early-authorship share, and TFDD-snapshot covariates (stars, forks, total contributors, language, license, project
  age, total commits, total files, history span). The `output` field is the binary survival label. Extensive per-repo metadata_*
  fields carry the full per-year DOA/TF tables, TFDD event details, founder identity, post-TFDD monthly commit series, and
  repo provenance so the downstream EXPERIMENT artifact can recompute alternate windows (e.g. for shuffle/placebo falsification
  checks) without re-mining or re-cloning any repository. Known inherited limitations, documented per the dependency artifact:
  the 6-12 month sub-year DOA window is a genuine unvalidated methodological extension (DOA/TF was only validated at yearly
  snapshots in the primary sources), and the local name/email identity-resolution heuristic (union-find merge, GitHub noreply
  numeric-ID special-casing, bot exclusion) is an unvalidated substitute for the original authors' GitHub-API-based alias
  resolution. The corpus skews heavily toward JavaScript (42/62 examples) with smaller counts in Ruby, C++, PHP, Java, TypeScript,
  Python, and Go, which downstream stratified analyses should account for. All code (search_candidates.py, mine_repo.py, run_mining.py,
  data.py) is included and reproducible via `uv run`, with intermediate candidate lists and per-repo mining results cached
  under temp/ to allow resuming without re-mining.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 5 ---
id: art_65c2e4aGIhui
type: experiment
title: Re-Testing Founder-Departure Survival Signals
summary: >-
  This experiment re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap,
  within-repo year-level placebo) plus a new window-boundary-noise control on the single unified 32-repo founder-departure
  Truck-Factor corpus (art_24Q1bYB_ULpu), replacing the prior iteration's independently re-mined, partially-overlapping data.
  Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown Go7/Ruby11/JS6/Java5/Rust3)
  against the dataset artifact's own summary before any analysis runs. Test 0 replicates Avelino et al.'s baseline: 62.5%
  survival rate and negligible-to-small Cohen's d (0.14-0.49) for developer/commit/file/star/fork gaps between survivors and
  non-survivors, consistent with the source literature. Test A fits a BH-FDR-corrected logistic regression of survival on
  the diffusion predictors plus stars/forks/contributors/age/commits/files/history-span/language controls; it pre-detects
  complete/quasi-complete separation (the Java and Rust language dummies perfectly predict the outcome in this small corpus)
  and falls back to L2-regularized logistic regression with a 300-resample bootstrap for p-values rather than letting statsmodels'
  unregularized MLE diverge/hang, which is what crashed the prior execution attempt. Test B sweeps three caliper widths for
  nearest-neighbor matched pairs on standardized [log(stars), log(forks), log(contributors)] and reports the result honestly
  as EXECUTED or UNTESTABLE depending on achieved pair count, never fabricating a bootstrap CI from zero pairs. Test C raises
  the prior iteration's 25 placebo draws to 300 per repo, using a documented year-resolution proxy statistic (year-over-year
  change in n_active_authors_in_doa) in place of the plan's arbitrary sub-year re-slicing, because the dataset artifact's
  metadata carries only yearly DOA/TF snapshots, not per-commit timestamps -- this substitution is stated explicitly in every
  relevant output field, per the fallback_plan. A new Sec-6 boundary-noise control computes founder-share variance across
  multiple stable (non-departure) windows within each repo's own history, substituting TFDD-corpus repos' own multi-year-before-departure
  periods for the unavailable non-TFDD candidate pool, and compares this noise floor against the true window's effect size
  to test whether the weak prior-iteration signal (r=0.180, p=0.615, n=30) could be a window-computation artifact rather than
  a real absence of a mechanism. A critical, explicitly logged data-quality finding: founder_commit_share_pre_tfdd -- the
  plan's primary diffusion predictor -- is constant (0.0) for 31 of 32 rows and missing for the remaining row in this specific
  dataset artifact (verified against the raw input JSON, not a parsing bug here), making it mathematically inestimable in
  a regression and undefined for point-biserial correlation; every test detects this and excludes/flags it explicitly rather
  than silently crashing or fabricating a value, and n_distinct_new_primary_owners_pre_tfdd is used as the sole viable diffusion
  predictor throughout. All four analyses (baseline, Test A/B/C, Sec 6) execute successfully end-to-end in about 13 seconds,
  write a schema-validated (exp_gen_sol_out) method_out.json with per-repo predict_baseline (controls-only model) and predict_our_method
  (full model) columns, RLIMIT_AS (16GB) and RLIMIT_CPU (600s) hard caps guard against the runaway-computation container crash
  observed in the previous execution attempt, and a fixed RNG seed (20260821) makes every bootstrap/placebo draw reproducible.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 6 ---
id: art_IN6RRoJnrq1j
type: evaluation
title: Bootstrap CIs and Identity Spot-Check
summary: >-
  This evaluation artifact adds statistical rigor to the founder-exit/repo-survival experiment (art_eXxdnfS0o6aV). It loads
  full_method_out.json (62 curated repos, 47 passing prefilters, 30 forming the founder-only-TFDD analysis corpus, 11 survivors
  vs 19 non-survivors) and runs four analyses. STEP 1: nonparametric bootstrap (B=10,000, seeded) 95% CIs on Cohen's d for
  three of the five snapshot covariates (developers_at_tfdd, commits_at_tfdd, files_at_tfdd) where raw per-repo survivor/non-survivor
  arrays were reconstructable from the examples records; stars and forks are marked NOT_COMPUTABLE_FROM_ARTIFACT because their
  raw per-repo values were never persisted to method_out.json. Each covariate's bootstrap CI is compared against Avelino et
  al.'s (ESEM 2019) reference range (d=0.13-0.26); developers_at_tfdd's CI [-1.05, 0.53] contains the Avelino range, while
  commits and files CIs exclude it. STEP 2: attempted a bootstrap CI on the placebo test's empirical percentile (reported
  point estimate: 40th percentile, p=0.615, n=25 null draws vs the pre-registered target of 200) but found only the four pooled
  scalar summary statistics were persisted, not the underlying per-repo/per-draw null values, so a true bootstrap CI is NOT_RECONSTRUCTABLE_FROM_ARTIFACT
  -- reported as a concrete, named gap for the next experiment iteration (persist raw null-draw arrays). STEP 3: a deterministic
  (numpy RandomState(42)) 12-repo manual GitHub spot-check of the identity/alias-resolution heuristic, using unauthenticated
  web fetches of GitHub commit-history and profile pages (with an AMBIGUOUS-and-swap fallback when a fetch is blocked/rate-limited/404s)
  -- final clean run found n_pass=11, n_alias_merge_error=1, n_ambiguous=0, observed error rate 0.083 with Wilson 95% CI [0.015,
  0.354]; the one detected error is documented with its specific nature and an explicit judgment on whether it would plausibly
  change founder identification or TF=1 status for that repo's event. STEP 4: consolidates all three original pre-registered
  success criteria into a TESTED_NULL / TESTED_LOW_RESOLUTION / UNTESTABLE_AT_SCALE reclassification driven by whether the
  Step 1/2 CIs are narrow enough to rule out a real small-to-moderate effect, with the practical implication for a future
  larger-corpus iteration stated per criterion. Output is eval_out.json (validated against the exp_eval_sol_out schema) with
  metadata carrying corpus_stats, covariate_ci_table, placebo_ci, identity_spotcheck_results, and success_criteria_reclassification,
  plus per-example entries echoing the original experiment's predict_our_method/predict_baseline_snapshot fields unchanged.
  Full/mini/preview JSON variants were generated and all bootstrap/spot-check gaps are stated explicitly in plain language
  rather than silently omitted.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</supplementary_materials>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for judging whether the paper's contribution is genuinely novel versus already-done or a known dead end in this field.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<previous_review>
Your review from the previous iteration. Check which critiques have been addressed
in the revised paper. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

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
</previous_review>

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

### [2] HUMAN-USER prompt · 2026-08-21 19:06:13 UTC

```
What determines whether an open-source project survives its founder stepping away?
```
