# review_paper — test_idea

> Phase: `invention_loop` · round 2 · `review_paper`
> Run: `iter1_0b7b616dce39` — Scaling the Corpus, Auditing the Power, and Reconciling the Sign: What Happens When a Founder-Diffusion Survival Test Is Finally Interrogated Rather Than Just Run
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_paper` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 21:27:31 UTC

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

Open-source software projects routinely depend on the sustained attention of one or two people, and when the developer who founded such a project stops committing -- a Truck-Factor Developer Detachment (TFDD) in Avelino et al.'s terminology -- some projects go dark permanently while others continue for years [1]. A prior iteration of this project fixed the specific defect that had made the natural follow-up hypothesis (does pre-departure authority *diffusion*, rather than the size snapshot at departure, predict survival) untestable: a corpus selected by present-day fame contained zero non-surviving founder-only TFDD events by construction. A stratified, fame-independent sampling frame across six languages and three popularity strata fixed that, producing 16-20 founder-only events with a 31.3-45.0% survival rate consistent with Avelino et al.'s published 40.6% reference. But the test battery run on that corpus reached no significant result, and the paper reporting it could say only that this was "an ordinary power problem" -- without saying how large a problem, or whether a competing published finding pointing the opposite direction (Medappa et al.'s write-access-ratio study [9]) could be reconciled with more data or was measuring something genuinely different.

This paper interrogates both open questions rather than simply re-running the same test at a larger n. First, it scales the identical sampling frame at the search stage -- 1,170 candidate repositories sampled across the same six-language by three-star-stratum grid, versus 270 previously -- and reports the complete per-cell filtering funnel (sampled, excluded for insufficient history, excluded as mining artifacts, excluded for lacking a dominant early founder, final processed count), yielding 254 processed repositories against 69 previously. Second, it formalizes the power question the prior iteration could only state qualitatively: a 25x200-draw Monte Carlo simulation, sweeping true effect size and sample size independently, asks both how large an effect the achieved n could detect and how large an n the achieved effect would need. Third, it introduces, in the same corpus, a second authority-diffusion measurement modeled directly on Medappa et al.'s construct -- a static, whole-pre-history ratio of accounts ever holding write access, as distinct from this line of work's own pre-departure *timing*-based measure -- to test directly whether the two studies' opposite-signed findings reflect a real disagreement or a difference in what is being measured.

Scaling the search stage turns out to be the easy part, and running the resulting battery honestly turns out to require disclosing why it does not run on the full scaled corpus. The 254-repository build completed, with its funnel fully logged, after the experiment and evaluation stages had already executed against earlier intermediate snapshots of the same pipeline -- a timing race of the same family as the one the prior iteration disclosed in its evaluation stage, now affecting the experiment stage as well and reaching the evaluation stage a second time in a different form. The experiment stage ran against a 34 founder-candidate-repository snapshot (yielding 19 strict-rule and 22 relaxed-rule founder-only events), and the independent evaluation harness's cached input predates even that, matching the prior iteration's 16/20-event numbers exactly. We verified this from file modification timestamps rather than inference: the final dataset artifact is timestamped 21:06:46 UTC, the experiment's output 19:54:52, and the evaluation's cached experiment summary 19:48:53 -- three snapshots, each earlier than the next stage that consumed it, all on the same pipeline run. We report the results actually produced by each of those three snapshots rather than describe a scaled analysis that did not, in fact, happen.

Why does this matter beyond a bookkeeping correction? Because it changes what the paper can honestly claim. The scaling work this iteration set out to do is real and reusable -- the funnel-transparent 254-repository corpus exists on disk and is a strictly larger, equally fame-independent successor to the 69-repository one -- but the statistical battery this paper reports is not run on it, and saying otherwise would misrepresent the paper's own evidence. What the paper can claim, and does, is sharper than before along three axes that do not require the full scaled n: a formal, simulation-based diagnosis of exactly how underpowered the current sample is and exactly how much more data closing that gap would take; a more robust placebo check; and a first look at whether the founder-diffusion and write-access-ratio literatures are actually in tension or are measuring different things in the same data.

**What this paper is, concretely.** A larger, funnel-transparent corpus build that the downstream pipeline stages did not yet consume, reported as what it is rather than as a completed larger-n analysis; a formal power/minimum-detectable-effect audit that replaces "underpowered" with a number (n≈120 needed, 7.5x achieved) and a mechanism (quasi-complete separation at n=16 with four covariates); a Firth-regression placebo check whose confidence interval is well-behaved and includes zero; a first same-corpus test of whether pre-departure diffusion timing and Medappa et al.'s static write-access ratio point the same direction (they do not, in this data, though neither reaches significance); and a second disclosed pipeline-timing defect, reported with the timestamp evidence that establishes it.

[FIGURE:fig1]

**Summary of Contributions**

- A scaled, funnel-transparent, fame-independent corpus build (1,170 sampled, 254 processed repositories across the same six-language by three-star-stratum grid, up from 270/69) with per-cell filtering counts reported as first-class output rather than a summary total (Section 4).
- A formal Monte Carlo power and minimum-detectable-effect audit of the founder-share and diffused-owner-count coefficients: no finite MDE exists within a beta grid of 0.25-10 at the achieved n=16 (power stays at or below 5.7%, diagnosed as quasi-complete separation rather than a merely large true effect), and 80% power at the observed effect size requires an estimated 120 events for founder-share (7.5x achieved) and 60 for diffused-owner-count (3.75x achieved) (Section 5).
- A Firth bias-reduced penalized-logistic placebo regression replacing the prior iteration's unstable placebo fit, whose 95% Wald confidence interval on the placebo-window founder-share coefficient (-8.02, 6.72) cleanly includes zero (Section 5).
- A first same-corpus test of Medappa et al.'s static write-access-ratio construct alongside this line of work's pre-departure timing measure (n=13): the static ratio's coefficient (-3.27) replicates Medappa et al.'s diffusion-reduces-survival sign, while the timing measure retains the opposite, protective sign in every regression reported across both iterations of this project -- a dissociation, not (yet) a significant one, reported with its variance-inflation-factor check (VIF 1.0, no multicollinearity) ruling out the trivial explanation that the two measures are just collinear proxies for the same thing (Section 5).
- Disclosure, with file-timestamp evidence, of a second pipeline-timing defect distinct from the prior iteration's: the experiment and evaluation stages each analyzed an earlier intermediate snapshot of the corpus than the one the dataset-construction stage ultimately produced, so this paper's statistical results are reported at n=14-19 (experiment) and n=16-20 (evaluation), not at the scaled corpus's 254-repository size (Section 4, Section 6).

# Related Work

**Truck Factor and Degree of Authorship.** The Truck Factor -- the minimal number of developers whose combined departure would incapacitate a project -- was formalized computationally by Avelino et al. via a greedy algorithm over per-file Degree-of-Authorship (DOA) scores [2]. DOA originates with Fritz et al., who model developer expertise on a file as a function of file creation, subsequent edits, and edits by others [7]; Avelino et al.'s authorship-only variant is reused verbatim across both iterations of this project, so any new result here is attributable to the new corpus, power analysis, and reconciliation test rather than a re-tuned expertise model. Ferreira et al. compare three Truck-Factor estimation algorithms and find Avelino et al.'s the most defensible on a manually labeled sample [3].

**Abandonment and survival.** Avelino et al.'s study remains this paper's direct empirical basis [1]: mining 1,932 popular GitHub repositories, they define TFDD, score 18-month post-TFDD survival, and report 128 of 315 (40.6%) TFDDs survive, with surviving and non-surviving projects statistically indistinguishable in size at the snapshot itself (Cohen's d = 0.13-0.26). This project's methodological departure, unchanged from the prior iteration, is to run the identical DOA/Truck-Factor machinery one window earlier and treat the pre-departure trend, rather than the snapshot, as the candidate signal.

**Diffusion of write access and core-team loss.** Medappa et al. analyze a matched sample of 5,762 GitHub projects and find that a higher proportion of contributors holding write access -- a static, whole-project-history measure of diffusion -- increases novelty but reduces survival [9], the opposite sign from this project's hypothesis about pre-departure diffusion *timing*. Section 5 reports the first attempt in this project to test both constructs in the same corpus rather than only note the tension in prose. Nourry et al. re-examine the TFDD construct at over 36,000 projects and report only 27% of abandoned projects attract a new Truck-Factor developer afterward [10], a base rate this project's 14.3-45.0% strict/relaxed survival range (across the two iterations' differing snapshots) brackets loosely. Jabrayilzade et al. survey 269 engineers and find informal "hard to replace" judgments often diverge from commit-based Truck-Factor estimates [11], a reminder that DOA-based identification is a version-control proxy, not a measurement of organizational knowledge.

**Why projects fail, self-reported, and dependency abandonment.** Coelho and Valente survey maintainers of 104 failed GitHub projects and report failed projects adopt fewer maintenance-practice signals (contributing guidelines 16% vs. 72%, CI 27% vs. 68%) than surviving ones [4], a plausible downstream correlate of diffusion measured directly here. Miller et al. study how downstream consumers detect and cope with an unmaintained dependency [5], complementary to this paper's producer-side question.

**Contributor-diversity metrics and succession outside software.** CHAOSS's Contributor Absence Factor names a longitudinal measurement option without formalizing or validating one against outcomes [12], which this paper's diffusion measurement operationalizes and tests. Jergensen, Sarma, and Wagstrom's "onion" model of periphery-to-core migration [13] and Steinmacher et al.'s newcomer-barrier review [14] both study the inward trajectory this paper's outward, founder-departing trajectory mirrors. Ahn's study of 64 matched Korean founder-led firms finds succession characteristics, including how authority was transferred, associated with post-succession survival independent of firm size [8], structurally paralleling the diffused-versus-concentrated distinction tested here.

**Mining-methodology controls.** Because this study mines GitHub commit history, it inherits the hazards Kalliamvakou et al. document under "the perils of mining GitHub" [6], most relevantly bulk-imported histories whose first commit touches an implausibly large file fraction in an implausibly short window; this study applies the same greater-than-80%-of-files-in-week-one heuristic, and the scaled corpus's per-cell funnel (Section 4) reports exactly how many candidates this filter removes at each language-by-stratum cell.

# Method

The core pipeline is unchanged from the prior iteration: the same reimplemented DOA/Truck-Factor/TFDD machinery [1, 2], the same pre-departure authority-diffusion measurement (founder commit-share and count of distinct non-founder DOA owners over a 180-365-day pre-departure window), and the same statistical test battery (matched-pairs bootstrap, Benjamini-Hochberg-corrected logistic regression, placebo/window-relocation regression, Mann-Whitney comparison). This section summarizes that machinery briefly and describes the two substantive additions: a scaled corpus-construction step (Section 4) and a Medappa-style reconciliation measurement (below).

**Alias resolution, DOA, and TFDD detection.** Unchanged from the prior iteration: commit authors are collapsed via normalized email and GitHub-login matching; cumulative-window DOA uses the Fritz et al. weights as reused by Avelino et al. (FA=3.293, DL=1.098, AC=-1.017) [7, 1]; the yearly Truck-Factor set is the greedy minimal set of primary-DOA owners whose removal leaves more than half of a project's files without a primary owner; a TFDD is recorded the first time every developer in the current Truck-Factor set has been silent for 365 days. Founder-only TFDDs are isolated under strict and relaxed founder-identification rules, with bulk-import artifacts (first commit touching more than 80% of files in week one) excluded per [6].

**Reconciliation measurement (new this iteration).** For each founder-only TFDD event, two additional quantities are computed alongside the existing pre-departure founder-share and diffused-owner-count measures. The `medappa_ratio` is a static, whole-pre-history analogue of Medappa et al.'s construct: the count of distinct accounts ever holding primary DOA ownership on any file, divided by the count of all distinct developers active before the TFDD -- not founder-specific, and not restricted to the pre-departure window. The `timing_term` is the fraction of that same diffusion that occurred specifically within the pre-departure window rather than earlier in the project's history, isolating whether diffusion's apparent effect (in either direction) depends on when it happens. A joint logistic model regresses survival on `medappa_ratio`, `timing_term`, their interaction, founder-share, and the snapshot covariates; a variance-inflation-factor check between `medappa_ratio` and `founder_share` rules out the two constructs being collinear proxies for each other before interpreting any sign difference between them.

**Statistical tests.** Unchanged in form from the prior iteration -- matched-pairs bootstrap, BH-corrected logistic regression (strict and relaxed founder-identification rules, plus a snapshot-only baseline), placebo/window-relocation regression, and Mann-Whitney comparison -- with one addition: where the standard maximum-likelihood logistic fit fails with a singular information matrix (the signature of quasi-complete separation at small n), a Firth bias-reduced penalized logistic regression [15] is fit instead, since it remains finite exactly where ordinary MLE and its Wald standard errors diverge together. All bootstrap resampling uses 5,000 draws with a fixed random seed (20260821).

**Power audit (new this iteration).** A Monte Carlo simulation generates 200 synthetic datasets per grid point (25 grid points x 2 covariates of interest), at the observed covariate mean and standard deviation, with the true effect on the covariate of interest swept across a grid and nuisance covariates fixed at a modest true effect (0.3); a logistic model is refit on each simulated dataset and power is the fraction rejecting at alpha=0.025 (Benjamini-Hochberg-equivalent for two primary tests). Two complementary sweeps are run: minimum detectable effect at the achieved n (varying true effect, fixing n), and required n for 80% power at the observed effect (varying n, fixing the true effect at its actually observed coefficient value).

# Experimental Setup

**Scaled corpus construction.** The corpus uses the identical stratified sampling frame as the prior iteration -- six languages (Python, JavaScript, Go, Java, Ruby, C++) by three star-count strata (50-500, 500-5,000, 5,000-100,000) -- widened at the search stage to approximately 65 candidates per language-by-stratum cell, 1,170 sampled repositories total, versus 270 previously. Each candidate is cloned and its full commit history extracted via `git log --numstat`. Filtering proceeds through the same four stages as before -- sufficient history (at least 1,095 days), exclusion of mining artifacts, exclusion of repositories lacking a single dominant early founder -- and every stage's exclusion count is logged per language-by-stratum cell rather than only as an aggregate. The resulting funnel: 1,170 sampled, 143 excluded for insufficient history, 112 excluded as mining artifacts, 118 excluded for lacking a dominant founder, 254 final processed repositories -- a 3.7x increase in processed corpus size over the prior iteration's 69, with a comparable overall pass rate (21.7% versus 25.6% previously).

**Table 1.** Search-stage and processed-corpus scale, this iteration versus the prior iteration.

| Iteration | Sampled | Insuff. history | Mining artifact | No dominant founder |
|---|---|---|---|---|
| Prior (69 processed) | 270 | -- | -- | -- |
| This iteration (254 processed) | 1,170 | 143 | 112 | 118 |

**The three-snapshot disclosure.** This 254-repository corpus is the one the dataset-construction stage produced, but it is not the one the experiment and evaluation stages analyzed. File modification timestamps establish the sequence directly: the final dataset artifact is dated 2026-08-21 21:06:46 UTC; the experiment stage's output (containing 34 founder-candidate repositories, 19 strict-rule and 22 relaxed-rule founder-only events) is dated 19:54:52; and the evaluation stage's cached copy of the experiment's summary statistics is dated 19:48:53 and numerically matches the prior iteration's 69-repository, 16-event corpus exactly. Each of these three timestamps precedes the next stage's consumption of it, meaning the experiment ran on an intermediate build well short of both the final 254-repository corpus and even the prior iteration's 69-repository one, and the evaluation stage's cache was captured before the experiment stage had itself finished. We report every result below tagged with which of these three snapshots produced it, rather than presenting a single n as if the pipeline had run end-to-end on the final corpus.

**Baselines.** As in the prior iteration, results are compared against Avelino et al.'s published statistics [1] (18-month survival 40.6%, snapshot Cohen's d = 0.13-0.26) and against a within-study snapshot-only baseline regression (developers, stars, forks at TFDD) computed on each snapshot's own founder-only subset.

# Results

## The experiment-stage snapshot (34 repositories, n=19 strict / 22 relaxed): quasi-complete separation reappears at the larger-but-still-small n

The experiment stage's 34-founder-candidate-repository snapshot yields 19 strict-rule and 22 relaxed-rule founder-only TFDD events. Strict-rule survival, after excluding 5 right-censored events, is 14.3% (2 of 14, SE 0.097); relaxed-rule survival, after excluding 6 censored events, is 25.0% (4 of 16, SE 0.112) -- both lower than the prior iteration's 31.3-45.0% and than Avelino et al.'s 40.6% reference, though on a smaller uncensored analysis sample (n=14-16) than either. The strict-rule diffusion regression fails outright with a singular information matrix at n=14, the signature of quasi-complete separation the power audit below diagnoses formally; the snapshot-only baseline regression converges at the same n (pseudo-R² = 0.257, log-stars coefficient 1.39, uncorrected p=0.256, not significant after correction). The relaxed-rule diffusion regression, at n=16, does converge: founder-share coefficient -7.46 (uncorrected p=0.525, BH p=0.63), diffused-owner-count coefficient +0.054 (uncorrected p=0.618), pseudo-R² = 0.508. The founder-share sign remains hypothesis-consistent -- higher founder concentration associated with lower survival odds -- across both this snapshot's relaxed-rule fit and the prior iteration's strict- and relaxed-rule fits, a sign that has now held in every regression run across two iterations of this project even though none has reached significance.

**Table 2.** Diffusion-hypothesis regressions across both iterations and snapshots. BH = Benjamini-Hochberg corrected.

| Snapshot | Rule | n | Founder-share coef. | p (BH) |
|---|---|---|---|---|
| Prior iteration (69 repos) | Strict | 16 | -5.558 | 0.600 |
| Prior iteration (69 repos) | Relaxed | 20 | -27.9 | 0.27 |
| This iteration, experiment (34 repos) | Strict | 14 | singular matrix | -- |
| This iteration, experiment (34 repos) | Relaxed | 16 | -7.464 | 0.629 |

The matched-pairs comparison, matching high- versus low-diffusion projects on standardized size and language, finds 4 eligible pairs at this snapshot (versus zero previously) but an undefined risk ratio, since the pairs available do not span both survival outcomes. A model-free Mann-Whitney comparison of founder share and diffused-owner count between survivors and non-survivors returns U=8.0, p=0.513 and U=5.0, p=0.229 respectively -- neither significant, consistent with the regression results.

## The reconciliation test: timing and static ratio point opposite directions in the same corpus

Restricting to the 13 founder-only events with both a valid pre-departure timing measurement and a valid whole-history write-access ratio, a joint logistic model including both `medappa_ratio` and `timing_term` alongside founder-share and snapshot covariates also fails with a singular matrix at this sample size. Falling back to the pre-specified univariate and single-covariate fallback analyses: the static `medappa_ratio`'s Cohen's d between survivors and non-survivors is -0.466 (Mann-Whitney p=0.553) and its coefficient in a single-covariate regression (`medappa_ratio` plus snapshot covariates, n=13) is -3.27 (uncorrected p=0.541, pseudo-R² = 0.306) -- negative, meaning higher static write-access diffusion is associated with lower survival, the same sign Medappa et al. report [9]. The `timing_term`'s Cohen's d is -0.657 (p=0.311), also negative in the raw comparison, but every founder-share regression reported in this paper and the prior iteration -- the measure this project's hypothesis is actually built on -- has a negative coefficient in the *opposite* substantive direction from `medappa_ratio`: founder-share is a concentration measure (higher = more concentrated authority = the pattern Medappa's low-diffusion ratio would also flag as low-diffusion), so a negative founder-share coefficient and a negative `medappa_ratio` coefficient are not, on inspection, actually pointing the same way -- founder-share's negative sign says concentration hurts survival (diffusion helps), while `medappa_ratio`'s negative sign says diffusion hurts survival (concentration helps), the direct disagreement with Medappa et al. that this iteration set out to interrogate. A variance-inflation-factor check between `medappa_ratio` and `founder_share` returns VIF=1.0002 for both, ruling out collinearity as the explanation: the two measures are not simply redundant proxies for the same underlying quantity, so the sign difference reflects something the corpus is capturing about pre-departure timing specifically, or (equally plausibly at n=13) statistical noise this sample cannot distinguish from a real dissociation.

## The power audit: quasi-complete separation, not merely a large effect, and a concrete n target

The Monte Carlo power audit, run on the evaluation stage's cached 16-event snapshot, finds that statistical power for detecting the founder-share effect does not rise monotonically with true effect size as it would under a well-behaved test: across a grid of true effect sizes from 0.25 to 10, power stays at or below 5.7% at every point, with no finite minimum detectable effect within the tested grid. This is not a claim that the true effect is unbounded; it is a diagnosis that as the simulated true effect grows, outcomes become near-perfectly separable by the covariates, the maximum-likelihood estimate and its Wald standard error diverge together, and the significance test the regression battery relies on stops rejecting even at large effects -- exactly the quasi-complete-separation failure mode the strict-rule regression at n=14 hit directly (Section 5.1) rather than only in simulation. The complementary sweep, fixing the true effect at the actually observed founder-share coefficient (-5.56) and varying n, is better-behaved: power rises from near 0 at n=16-40 to 31.1% at n=60, 57.3% at n=80, and crosses 80% between n=80 and n=120 (89.0% at n=120), yielding an estimated requirement of approximately 120 founder-only events for 80% power at the observed effect -- 7.5x the achieved n=16. The diffused-owner-count covariate's analogous requirement is smaller, approximately 60 events (3.75x achieved), consistent with its somewhat larger standardized effect size.

[FIGURE:fig2]

## The placebo check: a well-behaved confidence interval that includes zero

The prior iteration's placebo-window regression (a relocated, incorrect pre-departure window in place of the true one) produced a large, unstable coefficient and a near-1.0 p-value at n=15, a result that could only be read as suggestive given the fit's own instability. This iteration's independent evaluation harness refits the same placebo specification with a Firth bias-reduced penalized logistic regression, which remains finite where ordinary maximum likelihood does not: the placebo-window founder-share coefficient is -0.652 (SE 3.76, p=0.862), and its 95% Wald confidence interval, (-8.02, 6.72), cleanly includes zero. This is a materially firmer placebo result than the prior iteration's: rather than an unstable large coefficient whose near-1.0 p-value is hard to interpret on its own, the placebo effect now has a bounded, well-behaved interval centered near zero, consistent with the true pre-departure window carrying signal that a relocated window does not. The evaluation's stratified robustness audit, run on the same cached 16-20-event snapshot, finds most language and popularity-stratum cells too small to report a statistic (5 of 6 languages have fewer than 3 events or a single outcome class); the two cells with sufficient n (Go, n=3 events but 2 outcome classes; the 100-1k star stratum, n=11) show founder-share point-biserial correlations with survival of -0.022 (p=0.986) and -0.086 (p=0.802) respectively, both null and both far too small-n to interpret as more than a null-result placeholder pending the scaled corpus's actual analysis.

[FIGURE:fig3]

# Discussion

**What this iteration demonstrates, and what it does not yet.** The corpus-construction problem the prior iteration solved stays solved and is now solved at greater scale: the same fame-independent sampling frame, widened at the search stage, produces a 254-repository processed corpus with a fully disclosed per-cell funnel. What this iteration does *not* demonstrate is a founder-diffusion-predicts-survival test run at that scale, because the experiment and evaluation stages consumed earlier, smaller snapshots of the same pipeline run, established by file timestamps rather than assumption (Section 4). This is worth stating plainly rather than letting the larger corpus-construction number imply a larger analysis sample: the statistical results in Section 5 are run at n=13-19, not n=254, and reporting them as if the scaling had reached the analysis stage would misrepresent this paper's own evidence.

**What the power audit changes.** Prior to this iteration, "underpowered" was a qualitative judgment backed by a single number (the prior iteration's own power analysis specified roughly 40 events as a target, derived differently). The Monte Carlo audit here replaces that with a mechanism -- quasi-complete separation at n=16 with four covariates, which the strict-rule regression at n=14 independently corroborates by failing with the exact same signature (a singular information matrix) rather than merely a non-significant p-value -- and a concrete target: approximately 120 founder-only events for 80% power at the observed effect size, 7.5x the achieved n. This number is itself provisional (it assumes the observed coefficient is close to the true effect, which a non-significant n=16 estimate cannot guarantee), but it is a falsifiable target in a way "collect more data" is not, and the 254-repository corpus this iteration built is large enough, if the pipeline-timing defect is fixed and the corpus is run through the full DOA/TFDD pipeline, to plausibly approach it: 254 processed repositories at a comparable founder-only-TFDD yield rate to the 69-repository corpus's 16-20 events (23-29%) would be expected to produce on the order of 55-75 events, short of 120 but a substantial step, and worth reporting as the still-open next scaling target rather than a solved problem.

**What the reconciliation test suggests, cautiously.** The static `medappa_ratio` measure replicates Medappa et al.'s sign (diffusion reduces survival) while the timing-based founder-share measure retains the opposite sign in every regression across both iterations, and the two are not simply collinear (VIF ≈ 1.0). Read generously, this is consistent with the reconciling hypothesis this iteration set out to test: that diffusion's effect on survival depends on *when* it happens, protective when concentrated shortly before a founder's departure (a succession-planning signal) and harmful when it is a permanent structural feature of the project (a coordination-cost signal, Medappa et al.'s framing). Read skeptically, at n=13 with no covariate reaching significance and a joint model that itself fails to converge, this dissociation could equally be noise, and the paper does not have the power to distinguish the two readings. We report it as a first same-corpus observation worth testing at the scale the power audit specifies, not as a resolved reconciliation.

**The pipeline-timing defect, and why it recurs.** This is the second disclosed timing race in two iterations, and the recurrence is itself informative: the prior iteration's fix addressed a race between the experiment and evaluation stages for a *single* corpus build, but did not address the more general problem that a dataset-construction stage taking longer than the stages downstream of it will always risk being read by those stages before it finishes, regardless of which specific pair of stages races. The concrete fix, as before, is a completion signal the downstream stages wait on rather than a fixed schedule they assume; until that is in place, any future iteration that scales the dataset-construction stage should expect the same defect unless it explicitly checks, as this paper did, that the timestamp of the artifact each downstream stage consumed is not earlier than the timestamp of the artifact that stage was supposed to consume.

**Limitations.** Beyond the snapshot-timing gap already discussed at length, four further limitations bound how these results should be read. First, the experiment-stage snapshot's 34-repository founder-candidate pool is itself an intermediate artifact of unclear provenance relative to both the prior iteration's 69-repository corpus and this iteration's final 254-repository one, so its lower survival rate (14.3% strict) should not be read as a new estimate of the population rate. Second, the reconciliation test's n=13 is too small for its dissociation to be more than suggestive, and the joint model's failure to converge means the interaction term between timing and static diffusion -- the term that would most directly test the reconciling hypothesis -- was never actually estimated. Third, the power audit's n-required-for-80%-power figure assumes the observed coefficient approximates the true effect; if the true effect is smaller, more than 120 events would be needed, and the audit's own MDE-side sweep shows this assumption cannot currently be checked. Fourth, the scaled 254-repository corpus's own founder-only-TFDD yield has not been measured at all, since the pipeline defect means it was never run through the DOA/TFDD stage; the 55-75-event estimate above is a projection from the prior corpus's yield rate, not a measurement.

# Conclusion

This iteration set out to scale the founder-diffusion-predicts-survival test past the power ceiling the prior iteration identified, and partially succeeded: the fame-independent sampling frame now produces a 254-repository processed corpus, 3.7x the prior iteration's, with a fully disclosed filtering funnel. It did not succeed in running the statistical battery on that larger corpus, because a pipeline-timing defect -- disclosed here with file-timestamp evidence rather than inferred -- meant the experiment and evaluation stages each analyzed an earlier, smaller snapshot. Within that constraint, this iteration produced three results the prior one could not: a formal Monte Carlo power audit that replaces "underpowered" with a mechanism (quasi-complete separation at n=16) and a target (approximately 120 events, 7.5x achieved, for 80% power at the observed effect); a Firth-regression placebo check whose confidence interval is well-behaved and cleanly includes zero; and a first same-corpus test suggesting -- at n=13, not yet significant, but not explained away by collinearity -- that pre-departure diffusion timing and Medappa et al.'s static write-access ratio may point in genuinely opposite directions rather than merely disagreeing across studies with different corpora. The next step is now specific in a way it was not before: fix the completion-signal race so the DOA/TFDD pipeline actually runs on the 254-repository corpus already built, which should close a substantial fraction, though probably not all, of the gap to the 120-event target this audit specifies, and re-run the reconciliation test's joint model at whatever n that produces.
</paper>

<supplementary_materials>
The authors' code, data, and experimental artifacts. You may read these to verify
claims made in the paper — check if the code matches the described methodology,
if the results are reproducible, and if the data supports the conclusions.

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

--- Item 4 ---
id: art_kuFKmgecMVuK
type: dataset
title: Founder-Departure GitHub Commit Corpus
summary: >-
  Scaled the prior iteration's fame-independent, stratified GitHub sampling design (6 languages: Python, JavaScript, Go, Java,
  Ruby, C++ x 3 star strata: 50-500, 500-5,000, 5,000-100,000 = 18 cells) from ~270 candidates up to 1,170 candidates via
  the GitHub Search API (GH_TOKEN-authenticated, sort=stars per cell), then ran the same validated pipeline unchanged: a cheap
  created_at pre-filter for >=1,095 days of history, `git clone --bare` + `git log --numstat` (avoids API rate limits, 500MB
  per-repo size cap, incremental cleanup), the Kalliamvakou et al. bulk-import-artifact test (exclude if >80% of all-time-touched
  files are touched within the first 7 days), and the single-dominant-founder test (>=70% of commits from one author in the
  first 6 months / 50 commits, whichever is smaller). Funnel: 1,170 sampled -> 143 excluded_insufficient_history -> 112 excluded_mining_artifact
  -> 118 excluded_no_dominant_founder -> 254 final_processed (exceeds the 200-300 target), with full per-cell (language x
  star-stratum) counts in metadata.funnel.by_cell so both language- and stratum-level attrition are auditable. Beyond the
  prior iteration, each retained repo's commit rows now carry two new fields needed to reconcile Medappa et al.'s static write-access-ratio
  construct against this hypothesis's dynamic pre-departure diffusion construct from the SAME corpus: contributor_tenure_days
  (each contributor's first-to-last authored-commit span, the standard OSS-survival-literature proxy for write-access duration,
  since GitHub exposes no historical collaborator/push-access API for arbitrary repos) and diffusion_window_tag, which locates
  each non-founder's first-commit timing relative to an approximate founder TFDD point (a 365-day-silence rule applied to
  the dominant founder's commit dates, coarsened from Avelino et al.'s yearly Truck-Factor/DOA silence test since full DOA/TF
  computation is out of scope for a dataset artifact) into pre_tfdd_6_12mo / pre_tfdd_far / before_pre_tfdd_window / after_tfdd
  / n/a (founder still active). The delivered full_data_out.json follows the exp_sel_data_out schema: one dataset group 'github_founder_departure_corpus'
  with 50,695 examples, one example per (commit, file) row (repos with >200 rows are chronological-stride-capped to 200 rows
  to bound corpus size at 87MB, under the 100MB limit). `output` is the is_founder_commit label (0/1); `input` is a JSON string
  of all other per-row fields (repo identity/stars/forks/license/language, commit sha/timestamp/index, n_commits_total, tenure,
  TFDD, diffusion-window tag, file path/ext, lines added/removed) with author identity (alias key, email, name) withheld to
  prevent label leakage for downstream DOA/classification use. metadata_fold tags each example with its language|star-stratum
  cell. No DOA/TF computation, survival-outcome labeling, or statistical testing was performed here (out of scope for a dataset
  artifact) -- the TFDD point is only an approximate tagging aid so the downstream experiment can window the raw commit log
  without a second crawl. The raw per-repo git-log text (temp/numstat_raw, 684MB) and the unstrided full commit-row jsonl
  (temp/datasets/github_founder_corpus_rows.jsonl, 3.9GB) are excluded from the published repo as scratch intermediates; full_data_out.json
  is the complete, self-contained deliverable.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 5 ---
id: art_An3IzNVz6VIl
type: experiment
title: Founder Diffusion Timing vs. Project Survival
summary: >-
  Re-runs the validated DOA/Truck-Factor/TFDD/diffusion/survival pipeline from iter1 on the same 34 founder-candidate-repo
  corpus (via the mined full_data_out.json, 70,260 commit/file rows across 121 repos), using the byte-faithful Avelino et
  al. 2016 ICPC DOA formula, greedy Truck-Factor selection, and the validated 1-year abandoner threshold to detect founder-only
  Truck-Factor Developer Departure (TFDD) events. It computes the pre-departure diffusion score (founder commit share and
  diffused-owner count in the 6-12mo pre-departure window), classifies 18-month post-TFDD survival via the Avelino Active/Inactive
  graded model collapsed to binary survived/not-survived, and runs the full statistical battery: a BH-corrected logistic regression
  with Cohen's d and bootstrap 95% CIs on snapshot covariates, matched-pairs analysis, Mann-Whitney tests, and a placebo/shuffle
  check (1000 random-window reruns) building an empirical null distribution for the diffusion coefficient. It adds the direction's
  headline new test: a Medappa-et-al.-style reconciliation model with a static whole-history write-access ratio (medappa_ratio),
  a timing_term capturing how concentrated diffusion is near departure vs. spread through history, and their interaction,
  jointly regressed against survival with a VIF collinearity check between medappa_ratio and founder_commit_share_in_window.
  Achieved n_strict=19 and n_relaxed=22 founder-only TFDD events (against iter1's 16/20 and the underpowered 40-event target),
  and the shortfall is reported explicitly rather than overclaimed, since the 34-repo candidate pool structurally caps strict
  events below 40. All outputs (corpus summary, primary regression, matched pairs, Mann-Whitney, placebo check, and the medappa/timing
  reconciliation coefficients and interpretation) are written to method_out.json validated against the exp_gen_sol_out schema,
  with a per-event raw feature/outcome table for downstream paper writing, plus a repo_processing_diagnostics.csv audit trail
  in results/.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 6 ---
id: art_qP98tth_1H79
type: evaluation
title: Power Audit of Founder-Departure Survival Test
summary: >-
  This evaluation re-audits the founder-authority-diffusion survival experiment (art_4CZ-9Ou1G5ty, 69 repos processed, 16
  strict founder-only TFDD events, 20 relaxed TF<=2 events) with a race-condition guard that verifies full_method_out.json
  and the experiment's results/method_summary.json are complete (row-count vs metadata cross-check, required-key check) before
  computing any statistic, failing loudly on truncation. It produces eval.py and a schema-valid eval_out.json (exp_eval_sol_out
  format) with six analysis blocks stored under metadata and summarized in metrics_agg. (1) pipeline_validity: strict (n=16,
  rate=0.3125) and relaxed (n=20, rate=0.45) unconditioned survival rates with Wilson 95% CIs, each tested against Avelino
  et al.'s published 41%/128-of-315 reference via exact binomial test and a two-proportion z-test; both p>0.05 (strict p=0.613,
  relaxed p=0.821), so the re-implemented DOA/TF/TFDD pipeline is validated as unbiased relative to the published baseline.
  (2) primary_regression: independently refits the BH-corrected logistic models for our_method (founder_share, n_diffused_owners,
  log_stars, log_devs_at_tfdd) and the snapshot-only baseline on the strict-16 sample, confirming the refit reproduces the
  experiment's original coefficients essentially exactly (founder_share=-5.56, n_diffused_owners=-0.174, neither surviving
  BH correction, q=0.60), and cross-checks direction/magnitude against the relaxed-20 fit reused from the experiment's own
  code path. (3) placebo_test: recomputes the within-repo placebo-window regression using a hand-implemented Firth (1993)
  bias-reduced logistic regression to replace the original's uninterpretable near-infinite coefficient (-164.5, p=1.0, a quasi-separation
  artifact) with a finite, stable estimate (Firth coef=-0.652, Wald CI includes 0), and runs a Wald-type contrast against
  the real pre-departure coefficient -- verdict SPECIFICITY_CONFIRMED. (4) stratified_robustness: survival rate and (where
  n>=3 per cell) point-biserial correlation of founder_share with survival, broken out by language and by 3 star tiers, with
  any cell below the n>=3 threshold explicitly marked insufficient_n rather than computing a spurious statistic. (5) calibration:
  stratified bootstrap (1000 resamples, both classes preserved per resample) 95% CIs on AUC and Brier score for our_method
  (AUC=0.782) and baseline (AUC=0.800) fitted probabilities, plus calibration-in-the-large (mean predicted vs observed survival
  rate). (6) power_sensitivity_analysis, the artifact's core new contribution: a Monte Carlo simulation (up to 5000 synthetic
  datasets per grid search, logistic refit each time, BH-equivalent alpha=0.025 for m=2 primary covariates) that searches
  for the minimum detectable effect at 80% power at the achieved n, and separately solves for the n required to reach 80%
  power at the OBSERVED effect size. Result: no finite MDE exists within the tested effect grid at n=16 (power stays under
  ~5-6% even at the largest tested effect, the signature of quasi-complete separation with 4 covariates at this n) -- this
  is reported as a sharper diagnosis than a numeric MDE ('the achieved n is too small for this test statistic to be well-behaved
  at any effect size'), and the more trustworthy number is the n-required-for-power in the other direction: 120 events needed
  for founder_share and 60 for n_diffused_owners to reach 80% power at their observed coefficients, versus 16-20 achieved
  and versus the original ~40-event power-analysis target. Downstream GEN_PAPER_TEXT should present this as: the pipeline
  is validated against Avelino et al., the placebo test now supports (rather than being ambiguous about) pre-departure specificity
  of the diffusion signal, and the corpus needs roughly 60-120 founder-only TFDD events (not the originally assumed ~40) to
  have 80% power to detect the observed effect sizes, giving the next iteration's corpus-scaling target a precise, effect-size-grounded
  number instead of a qualitative '40-50% of target' claim.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
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

### [2] HUMAN-USER prompt · 2026-08-21 21:27:31 UTC

```
What determines whether an open-source project survives its founder stepping away?
```
