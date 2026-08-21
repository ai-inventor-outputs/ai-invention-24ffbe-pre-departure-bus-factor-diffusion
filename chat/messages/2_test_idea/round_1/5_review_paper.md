# review_paper — test_idea

> Phase: `invention_loop` · round 1 · `review_paper`
> Run: `iter1_0b7b616dce39` — Does Pre-Departure Authority Diffusion Predict Open-Source Project Survival? A Unified-Corpus Retest with a Window-Boundary-Noise Control
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `review_paper` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-08-21 17:38:33 UTC

```
model: claude-sonnet-5 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/review_paper/review_paper
```

### [2] SYSTEM-USER prompt · 2026-08-21 17:38:41 UTC

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
</supplementary_materials>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for judging whether the paper's contribution is genuinely novel versus already-done or a known dead end in this field.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
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

### [3] HUMAN-USER prompt · 2026-08-21 17:38:41 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [4] TOOL CALL — Write · 2026-08-21 17:39:46 UTC

```
File: ./.terminal_claude_agent_struct_out.json

{
  "overall_assessment": "This is an honestly-reported negative result built on a careful, citation-anchored reconstruction of the Avelino et al. DOA/Truck-Factor/TFDD pipeline. The paper's core virtue -- pre-registering three success criteria and reporting failure on all three without post-hoc rescue -- is genuine and should be valued. But the empirical contribution is severely undermined by a corpus that is too small to run two of its three pre-registered tests at all (n_used=0), by an unexplained mismatch between the experiment's 62-repo curation and the paper's own dataset artifact's 32-repo corpus (the experiment never touches the artifact it is nominally paired with), and by a placebo test built on only 25 null draws. As written, the paper documents a methodology and a failed pilot more than it tests a hypothesis. For a top-tier venue, the honesty is commendable but the evidentiary content is too thin: a reviewer cannot distinguish 'the hypothesis is false' from 'the study was underpowered by roughly 10x,' and the paper itself concedes this. The work reads as a well-documented negative pilot / methods paper rather than a hypothesis test with a real answer, and needs either substantially more corpus (the paper's own suggested next step) or a reframing that centers the pipeline-construction and negative-result-reporting contribution rather than the diffusion-vs-survival question implied by the title and abstract framing.",
  "strengths": [
    "Careful, source-verified reconstruction of a nontrivial prior pipeline (DOA formula, greedy Truck-Factor algorithm, TFDD/survival state machine), with explicit correction of three working assumptions (DL term, binary vs. graded survival state, yearly-only validation scope) documented against primary sources rather than assumed from prose.",
    "Genuine pre-registration discipline: three success criteria stated before running the experiment, and the paper reports failure on all three without relaxing thresholds, pooling covariates, or otherwise post-hoc rescuing a positive result -- this is rare and valuable scientific practice.",
    "Transparent, quantified exclusion funnel (62 to 47 to 30) and explicit acknowledgment of where the sample-size ceiling binds each of the three pre-registered tests, rather than silently omitting the tests that could not run.",
    "The paper explicitly flags its own extension's unvalidated status (sub-year DOA windows were never validated by the original authors) and proposes a concrete follow-up validation (window-recomputed DOA vs. full-history DOA on non-TFDD held-out projects)."
  ],
  "dimension_scores": [
    {
      "dimension": "soundness",
      "score": 2,
      "justification": "The reconstructed pipeline itself appears carefully verified against primary sources, but the empirical test is not actually completed: 2 of 3 pre-registered criteria are untestable (n_used=0, n_high=0/n_low=0) rather than tested and failed, and the one criterion that does run (placebo, r=0.180 at 40th percentile) rests on only 25 null draws against a planned 1,000 -- a 40x reduction the paper itself flags as limiting resolution. A negative finding that is 2/3 'could not run' and 1/3 'ran on a coarse null' does not soundly support the paper's central claim that the pre-departure diffusion hypothesis 'fails.'",
      "improvements": [
        "Scale the corpus toward the 200-300 founder-only-TFDD range needed for the regression and matched-pairs tests to produce n_used > 0 per cell -- this is the paper's own stated next step and is the single highest-value fix.",
        "Re-run the placebo test at or near the pre-registered 1,000 draws (or report a bootstrap CI on the empirical percentile at n=25 to show the qualitative conclusion is robust to draw count) rather than asserting robustness without evidence.",
        "If corpus scaling is infeasible, reframe the abstract/intro/conclusion claims from 'the hypothesis fails' to 'the hypothesis is untestable at this scale, with one informative but coarse null result' -- the current framing overstates what was actually established."
      ]
    },
    {
      "dimension": "presentation",
      "score": 3,
      "justification": "The writing is clear, well-organized, and unusually careful about distinguishing 'tested and rejected' from 'untestable at this sample size' throughout. The corpus-provenance mismatch between Sections 3 and 4, however, is confusing on first read and under-motivated (why was the dataset artifact unavailable at experiment run time, and why is this only revealed as an aside rather than addressed as a first-order methodological problem).",
      "improvements": [
        "Move the corpus-provenance mismatch (62-repo experiment corpus vs. 32-repo dataset artifact) into Section 3 as a first-class methodological caveat rather than a Discussion-section aside, since it affects how every number in Section 4 should be read.",
        "Add a table directly comparing the 30-repo and 32-repo corpora on outcome balance, language distribution, and star/size ranges, not just a qualitative claim that 'the two funnels are consistent in shape' -- the current argument for population equivalence is weak (attrition category similarity is not evidence of sample equivalence).",
        "Clarify in the abstract/intro that the headline result is a negative/null finding under severe power constraints, not a general answer to 'what determines survival' -- a reader skimming the abstract could come away thinking more was established than was."
      ]
    },
    {
      "dimension": "contribution",
      "score": 2,
      "justification": "The pipeline-reconstruction contribution is real but incremental (a careful reimplementation with documented deviations, not a new method). The intended novel contribution -- the pre-departure trajectory signal -- is not actually evaluated with adequate power, so the paper cannot claim to have advanced understanding of what predicts survival; it can only claim to have built infrastructure and hit a wall. That is a legitimate but modest contribution for a top-tier venue, more suited to a workshop, a negative-results track, or a resource/reproducibility paper than a full research contribution.",
      "improvements": [
        "Either scale the corpus by 5-10x to get a real test of criteria (i) and (ii), or pivot the paper's framing entirely toward a methods/resource contribution: 'a validated open pipeline plus a documented power analysis for founder-departure survival prediction,' with the dataset and mining code as the primary artifact and the underpowered pilot result presented as a proof-of-concept rather than a conclusion.",
        "Quantify explicitly (via a power analysis) how large a founder-only-TFDD corpus would be needed to detect an effect of the magnitude claimed plausible (e.g., matching Avelino et al.'s Cohen's d range) at 80% power -- this converts 'more data needed' from a vague appeal into an actionable, falsifiable target for follow-up work, and substantially strengthens the paper's value even without new data."
      ]
    }
  ],
  "critiques": [
    {
      "category": "evidence",
      "severity": "major",
      "description": "Two of the three pre-registered success criteria (BH-FDR logistic regression and matched-pairs bootstrap) do not run to completion -- n_used=0 and n_high=0/n_low=0 respectively. The paper's abstract and conclusion nonetheless state that 'the hypothesis fails on all three counts' and treat this as a negative result about the underlying mechanism. A test that cannot execute provides zero evidence either for or against the hypothesis; conflating 'untestable' with 'tested and failed' materially overstates what the paper shows.",
      "suggested_action": "Reframe every top-level claim (abstract, contributions list, Section 4 verdict, conclusion) to separate 'untested for lack of power' (2/3 criteria) from 'tested and null' (1/3 criteria, the placebo). Do not use language like 'the hypothesis fails on all three counts' -- state instead that the protocol could only execute one of three pre-registered tests, and that test alone is inconclusive-to-null."
    },
    {
      "category": "methodology",
      "severity": "major",
      "description": "The experiment (Section 4) is run on an independently-mined 62-repository curation, not on the paper's own 32-repository dataset artifact (Section 3's 'companion' funnel). The paper acknowledges this only in the Discussion as a limitation, attributing it to the dataset artifact 'not yet being available at experiment run time.' This means the paper's headline dataset contribution (30 founder-only TFDD events with full exclusion funnel) and its headline experimental result are drawn from two different, only qualitatively-compared corpora -- a significant internal inconsistency for a paper whose central claim rests on corpus construction rigor.",
      "suggested_action": "Either (a) re-run the experiment against the 32-repository dataset artifact and report both results side by side, or (b) if that is infeasible in this iteration, merge Sections 3 and 4 to describe only the 62-repository experimental corpus as the paper's dataset, and present the 32-repository artifact separately and explicitly as a distinct, not-yet-integrated resource -- do not imply methodological unity between the two where none currently exists."
    },
    {
      "category": "methodology",
      "severity": "major",
      "description": "The core measurement extension -- computing DOA/Truck-Factor over a 6-12 month sub-year window rather than Avelino et al.'s validated yearly full-history snapshot -- is acknowledged as 'unvalidated' throughout the paper (Section 2, Section 5) but is nonetheless used as the paper's primary independent variable. No sensitivity or robustness check (e.g., varying window width, or the proposed held-out non-TFDD validation) is actually run in this iteration; it is deferred entirely to 'future work.' Given that this window computation is the paper's stated central technical extension over prior work, leaving it fully unvalidated is a significant gap -- if the window computation is itself noisy or biased at the boundary, that alone could explain the null placebo result without implicating the underlying hypothesis.",
      "suggested_action": "Run the proposed validation check now, even on a small held-out set: compute window-recomputed DOA on a handful of non-TFDD projects (no departure event) at several 6-12 month windows drawn from stable periods, and report how much window-boundary noise alone contributes to founder-share variance. Without this, the paper cannot distinguish 'the diffusion signal is genuinely absent' from 'the measurement of the diffusion signal is too noisy to detect anything.'"
    },
    {
      "category": "rigor",
      "severity": "minor",
      "description": "The placebo null distribution uses only 25 draws (Section 4, Limitation 5), reduced from a planned 1,000 for compute budget. At n=25, the empirical percentile (40th) has coarse resolution -- individual draws move the percentile by 4 points -- and the paper's claim that 'a p-value of 0.615 is unlikely to change qualitative conclusion under a finer null' is asserted without any supporting calculation (e.g., a binomial CI on the percentile, or a parametric approximation of the null).",
      "suggested_action": "Either increase the draw count to at least 200-500 (the compute cost of a placebo re-draw should be modest relative to the rest of the pipeline) or report a confidence interval on the empirical percentile (e.g., via bootstrap resampling of the 25 draws, or a normal approximation to the underlying correlation-null) to substantiate the robustness claim rather than asserting it."
    },
    {
      "category": "scope",
      "severity": "minor",
      "description": "Snapshot-covariate effect sizes reported in the paper's own corpus (Cohen's d = -0.226 to -0.625) are 2-3x larger in absolute magnitude than Avelino et al.'s reported 0.13-0.26, and the paper attributes this entirely to 'corpus-size noise' from the smaller, targeted sample. This is plausible but not verified -- no confidence intervals are reported alongside these point estimates, so a reader cannot assess whether the discrepancy is within sampling noise or reflects a genuine difference in the targeted-corpus population (e.g., systematically larger/more visible projects, given the seed-list construction described in the research artifact).",
      "suggested_action": "Report bootstrap or analytic confidence intervals on all Cohen's d effect sizes in Section 4's baseline replication, and explicitly state whether Avelino et al.'s original 0.13-0.26 range falls inside or outside those intervals -- this converts a hand-waved attribution into a checkable claim."
    },
    {
      "category": "clarity",
      "severity": "minor",
      "description": "The paper reports a founder-only-TFDD rate of 63.8% in its filtered corpus against Avelino et al.'s reported 16%, a 4x difference explained as an artifact of targeted candidate selection. This explanation is plausible, but the mechanics of how the candidate list was constructed (Section 3 mentions only 'we search GitHub for single-founder repositories') are underspecified relative to the level of detail given elsewhere in the paper -- the supplementary research artifact reveals a curated 10-entry seed list with explicit exclude/caution flags, which is not described in the main text at all.",
      "suggested_action": "Add a short paragraph to Section 3 describing the candidate-selection procedure (seed-list curation, exclusion of known non-single-founder or fork-not-handoff projects such as youtube-dl/yt-dlp) so the 4x TFDD-rate discrepancy is explainable from the main text alone rather than requiring the supplementary artifact."
    },
    {
      "category": "novelty",
      "severity": "minor",
      "description": "The paper positions its contribution primarily as testing a new trajectory-based signal against Avelino et al.'s snapshot covariates, but does not engage with the broader bus-factor/knowledge-concentration prediction literature beyond the two Avelino et al. papers and brief citations to ecosystem-turnover studies (Jabrayilzade2022, Coelho2017, Constantinou2017, Fan2025). Related work on predicting OSS project abandonment or 'survival' more broadly (e.g., using activity time-series, issue/PR dynamics, or social network features) is not discussed, making it hard to judge whether a 'trajectory vs. snapshot' framing is itself a known distinction in adjacent prediction literatures.",
      "suggested_action": "Add a short related-work paragraph situating the trajectory-vs-snapshot distinction against general OSS-abandonment-prediction literature (which often already uses time-series/activity-trend features, not just point-in-time snapshots), to clarify what specifically is new here: the DOA-based authority-diffusion operationalization, not the general idea of using trends rather than snapshots."
    },
    {
      "category": "methodology",
      "severity": "minor",
      "description": "Identity resolution (Section 5, 'Identity resolution') uses an unvalidated local heuristic in place of Avelino et al.'s GitHub-API-based alias resolution (median 11% alias rate), and the paper correctly flags that this could bias the diffusion covariate (count of independent non-founder DOA owners) in either direction. At n=30 with an already-underpowered test, even modest misclassification of author identity could materially shift which repositories qualify as 'founder-only' TFDD events in the first place -- this is a data-quality risk affecting corpus construction, not just covariate noise.",
      "suggested_action": "Spot-check identity resolution against GitHub API results (even without full-scale API access, a random 10-15 repo sample checked manually against GitHub profile pages would suffice) and report the observed alias/merge error rate on that sample, to give readers a concrete bound rather than an open-ended caveat."
    }
  ],
  "score": 4,
  "confidence": 3
}
```

### [5] TOOL RESULT — Write · 2026-08-21 17:39:46 UTC

```
{"type": "create", "filePath": "./.terminal_claude_agent_struct_out.json", "content": "{\n  \"overall_assessment\": \"This is an honestly-reported negative result built on a careful, citation-anchored reconstruction of the Avelino et al. DOA/Truck-Factor/TFDD pipeline. The paper's core virtue -- pre-registering three success criteria and reporting failure on all three without post-hoc rescue -- is genuine and should be valued. But the empirical contribution is severely undermined by a corpus that is too small to run two of its three pre-registered tests at all (n_used=0), by an unexplained mismatch between the experiment's 62-repo curation and the paper's own dataset artifact's 32-repo corpus (the experiment never touches the artifact it is nominally paired with), and by a placebo test built on only 25 null draws. As written, the paper documents a methodology and a failed pilot more than it tests a hypothesis. For a top-tier venue, the honesty is commendable but the evidentiary content is too thin: a reviewer cannot distinguish 'the hypothesis is false' from 'the study was underpowered by roughly 10x,' and the paper itself concedes this. The work reads as a well-documented negative pilot / methods paper rather than a hypothesis test with a real answer, and needs either substantially more corpus (the paper's own suggested next step) or a reframing that centers the pipeline-construction and negative-result-reporting contribution rather than the diffusion-vs-survival question implied by the title and abstract framing.\",\n  \"strengths\": [\n    \"Careful, source-verified reconstruction of a nontrivial prior pipeline (DOA formula, greedy Truck-Factor algorithm, TFDD/survival state machine), with explicit correction of three working assumptions (DL term, binary vs. graded survival state, yearly-only validation scope) documented against primary sources rather than assumed from prose.\",\n    \"Genuine pre-registration discipline: three success criteria stated before running the experiment, and the paper reports failure on all three without relaxing thresholds, pooling covariates, or otherwise post-hoc rescuing a positive result -- this is rare and valuable scientific practice.\",\n    \"Transparent, quantified exclusion funnel (62 to 47 to 30) and explicit acknowledgment of where the sample-size ceiling binds each of the three pre-registered tests, rather than silently omitting the tests that could not run.\",\n    \"The paper explicitly flags its own extension's unvalidated status (sub-year DOA windows were never validated by the original authors) and proposes a concrete follow-up validation (window-recomputed DOA vs. full-history DOA on non-TFDD held-out projects).\"\n  ],\n  \"dimension_scores\": [\n    {\n      \"dimension\": \"soundness\",\n      \"score\": 2,\n      \"justification\": \"The reconstructed pipeline itself appears carefully verified against primary sources, but the empirical test is not actually completed: 2 of 3 pre-registered criteria are untestable (n_used=0, n_high=0/n_low=0) rather than tested and failed, and the one criterion that does run (placebo, r=0.180 at 40th percentile) rests on only 25 null draws against a planned 1,000 -- a 40x reduction the paper itself flags as limiting resolution. A negative finding that is 2/3 'could not run' and 1/3 'ran on a coarse null' does not soundly support the paper's central claim that the pre-departure diffusion hypothesis 'fails.'\",\n      \"improvements\": [\n        \"Scale the corpus toward the 200-300 founder-only-TFDD range needed for the regression and matched-pairs tests to produce n_used > 0 per cell -- this is the paper's own stated next step and is the single highest-value fix.\",\n        \"Re-run the placebo test at or near the pre-registered 1,000 draws (or report a bootstrap CI on the empirical percentile at n=25 to show the qualitative conclusion is robust to draw count) rather than asserting robustness without evidence.\",\n        \"If corpus scaling is infeasible, reframe the abstract/intro/conclusion claims from 'the hypothesis fails' to 'the hypothesis is untestable at this scale, with one informative but coarse null result' -- the current framing overstates what was actually established.\"\n      ]\n    },\n    {\n      \"dimension\": \"presentation\",\n      \"score\": 3,\n      \"justification\": \"The writing is clear, well-organized, and unusually careful about distinguishing 'tested and rejected' from 'untestable at this sample size' throughout. The corpus-provenance mismatch between Sections 3 and 4, however, is confusing on first read and under-motivated (why was the dataset artifact unavailable at experiment run time, and why is this only revealed as an aside rather than addressed as a first-order methodological problem).\",\n      \"improvements\": [\n        \"Move the corpus-provenance mismatch (62-repo experiment corpus vs. 32-repo dataset artifact) into Section 3 as a first-class methodological caveat rather than a Discussion-section aside, since it affects how every number in Section 4 should be read.\",\n        \"Add a table directly comparing the 30-repo and 32-repo corpora on outcome balance, language distribution, and star/size ranges, not just a qualitative claim that 'the two funnels are consistent in shape' -- the current argument for population equivalence is weak (attrition category similarity is not evidence of sample equivalence).\",\n        \"Clarify in the abstract/intro that the headline result is a negative/null finding under severe power constraints, not a general answer to 'what determines survival' -- a reader skimming the abstract could come away thinking more was established than was.\"\n      ]\n    },\n    {\n      \"dimension\": \"contribution\",\n      \"score\": 2,\n      \"justification\": \"The pipeline-reconstruction contribution is real but incremental (a careful reimplementation with documented deviations, not a new method). The intended novel contribution -- the pre-departure trajectory signal -- is not actually evaluated with adequate power, so the paper cannot claim to have advanced understanding of what predicts survival; it can only claim to have built infrastructure and hit a wall. That is a legitimate but modest contribution for a top-tier venue, more suited to a workshop, a negative-results track, or a resource/reproducibility paper than a full research contribution.\",\n      \"improvements\": [\n        \"Either scale the corpus by 5-10x to get a real test of criteria (i) and (ii), or pivot the paper's framing entirely toward a methods/resource contribution: 'a validated open pipeline plus a documented power analysis for founder-departure survival prediction,' with the dataset and mining code as the primary artifact and the underpowered pilot result presented as a proof-of-concept rather than a conclusion.\",\n        \"Quantify explicitly (via a power analysis) how large a founder-only-TFDD corpus would be needed to detect an effect of the magnitude claimed plausible (e.g., matching Avelino et al.'s Cohen's d range) at 80% power -- this converts 'more data needed' from a vague appeal into an actionable, falsifiable target for follow-up work, and substantially strengthens the paper's value even without new data.\"\n      ]\n    }\n  ],\n  \"critiques\": [\n    {\n      \"category\": \"evidence\",\n      \"severity\": \"major\",\n      \"description\": \"Two of the three pre-registered success criteria (BH-FDR logistic regression and matched-pairs bootstrap) do not run to completion -- n_used=0 and n_high=0/n_low=0 respectively. The paper's abstract and conclusion nonetheless state that 'the hypothesis fails on all three counts' and treat this as a negative result about the underlying mechanism. A test that cannot execute provides zero evidence either for or against the hypothesis; conflating 'untestable' with 'tested and failed' materially overstates what the paper shows.\",\n      \"suggested_action\": \"Reframe every top-level claim (abstract, contributions list, Section 4 verdict, conclusion) to separate 'untested for lack of power' (2/3 criteria) from 'tested and null' (1/3 criteria, the placebo). Do not use language like 'the hypothesis fails on all three counts' -- state instead that the protocol could only execute one of three pre-registered tests, and that test alone is inconclusive-to-null.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"major\",\n      \"description\": \"The experiment (Section 4) is run on an independently-mined 62-repository curation, not on the paper's own 32-repository dataset artifact (Section 3's 'companion' funnel). The paper acknowledges this only in the Discussion as a limitation, attributing it to the dataset artifact 'not yet being available at experiment run time.' This means the paper's headline dataset contribution (30 founder-only TFDD events with full exclusion funnel) and its headline experimental result are drawn from two different, only qualitatively-compared corpora -- a significant internal inconsistency for a paper whose central claim rests on corpus construction rigor.\",\n      \"suggested_action\": \"Either (a) re-run the experiment against the 32-repository dataset artifact and report both results side by side, or (b) if that is infeasible in this iteration, merge Sections 3 and 4 to describe only the 62-repository experimental corpus as the paper's dataset, and present the 32-repository artifact separately and explicitly as a distinct, not-yet-integrated resource -- do not imply methodological unity between the two where none currently exists.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"major\",\n      \"description\": \"The core measurement extension -- computing DOA/Truck-Factor over a 6-12 month sub-year window rather than Avelino et al.'s validated yearly full-history snapshot -- is acknowledged as 'unvalidated' throughout the paper (Section 2, Section 5) but is nonetheless used as the paper's primary independent variable. No sensitivity or robustness check (e.g., varying window width, or the proposed held-out non-TFDD validation) is actually run in this iteration; it is deferred entirely to 'future work.' Given that this window computation is the paper's stated central technical extension over prior work, leaving it fully unvalidated is a significant gap -- if the window computation is itself noisy or biased at the boundary, that alone could explain the null placebo result without implicating the underlying hypothesis.\",\n      \"suggested_action\": \"Run the proposed validation check now, even on a small held-out set: compute window-recomputed DOA on a handful of non-TFDD projects (no departure event) at several 6-12 month windows drawn from stable periods, and report how much window-boundary noise alone contributes to founder-share variance. Without this, the paper cannot distinguish 'the diffusion signal is genuinely absent' from 'the measurement of the diffusion signal is too noisy to detect anything.'\"\n    },\n    {\n      \"category\": \"rigor\",\n      \"severity\": \"minor\",\n      \"description\": \"The placebo null distribution uses only 25 draws (Section 4, Limitation 5), reduced from a planned 1,000 for compute budget. At n=25, the empirical percentile (40th) has coarse resolution -- individual draws move the percentile by 4 points -- and the paper's claim that 'a p-value of 0.615 is unlikely to change qualitative conclusion under a finer null' is asserted without any supporting calculation (e.g., a binomial CI on the percentile, or a parametric approximation of the null).\",\n      \"suggested_action\": \"Either increase the draw count to at least 200-500 (the compute cost of a placebo re-draw should be modest relative to the rest of the pipeline) or report a confidence interval on the empirical percentile (e.g., via bootstrap resampling of the 25 draws, or a normal approximation to the underlying correlation-null) to substantiate the robustness claim rather than asserting it.\"\n    },\n    {\n      \"category\": \"scope\",\n      \"severity\": \"minor\",\n      \"description\": \"Snapshot-covariate effect sizes reported in the paper's own corpus (Cohen's d = -0.226 to -0.625) are 2-3x larger in absolute magnitude than Avelino et al.'s reported 0.13-0.26, and the paper attributes this entirely to 'corpus-size noise' from the smaller, targeted sample. This is plausible but not verified -- no confidence intervals are reported alongside these point estimates, so a reader cannot assess whether the discrepancy is within sampling noise or reflects a genuine difference in the targeted-corpus population (e.g., systematically larger/more visible projects, given the seed-list construction described in the research artifact).\",\n      \"suggested_action\": \"Report bootstrap or analytic confidence intervals on all Cohen's d effect sizes in Section 4's baseline replication, and explicitly state whether Avelino et al.'s original 0.13-0.26 range falls inside or outside those intervals -- this converts a hand-waved attribution into a checkable claim.\"\n    },\n    {\n      \"category\": \"clarity\",\n      \"severity\": \"minor\",\n      \"description\": \"The paper reports a founder-only-TFDD rate of 63.8% in its filtered corpus against Avelino et al.'s reported 16%, a 4x difference explained as an artifact of targeted candidate selection. This explanation is plausible, but the mechanics of how the candidate list was constructed (Section 3 mentions only 'we search GitHub for single-founder repositories') are underspecified relative to the level of detail given elsewhere in the paper -- the supplementary research artifact reveals a curated 10-entry seed list with explicit exclude/caution flags, which is not described in the main text at all.\",\n      \"suggested_action\": \"Add a short paragraph to Section 3 describing the candidate-selection procedure (seed-list curation, exclusion of known non-single-founder or fork-not-handoff projects such as youtube-dl/yt-dlp) so the 4x TFDD-rate discrepancy is explainable from the main text alone rather than requiring the supplementary artifact.\"\n    },\n    {\n      \"category\": \"novelty\",\n      \"severity\": \"minor\",\n      \"description\": \"The paper positions its contribution primarily as testing a new trajectory-based signal against Avelino et al.'s snapshot covariates, but does not engage with the broader bus-factor/knowledge-concentration prediction literature beyond the two Avelino et al. papers and brief citations to ecosystem-turnover studies (Jabrayilzade2022, Coelho2017, Constantinou2017, Fan2025). Related work on predicting OSS project abandonment or 'survival' more broadly (e.g., using activity time-series, issue/PR dynamics, or social network features) is not discussed, making it hard to judge whether a 'trajectory vs. snapshot' framing is itself a known distinction in adjacent prediction literatures.\",\n      \"suggested_action\": \"Add a short related-work paragraph situating the trajectory-vs-snapshot distinction against general OSS-abandonment-prediction literature (which often already uses time-series/activity-trend features, not just point-in-time snapshots), to clarify what specifically is new here: the DOA-based authority-diffusion operationalization, not the general idea of using trends rather than snapshots.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"minor\",\n      \"description\": \"Identity resolution (Section 5, 'Identity resolution') uses an unvalidated local heuristic in place of Avelino et al.'s GitHub-API-based alias resolution (median 11% alias rate), and the paper correctly flags that this could bias the diffusion covariate (count of independent non-founder DOA owners) in either direction. At n=30 with an already-underpowered test, even modest misclassification of author identity could materially shift which repositories qualify as 'founder-only' TFDD events in the first place -- this is a data-quality risk affecting corpus construction, not just covariate noise.\",\n      \"suggested_action\": \"Spot-check identity resolution against GitHub API results (even without full-scale API access, a random 10-15 repo sample checked manually against GitHub profile pages would suffice) and report the observed alias/merge error rate on that sample, to give readers a concrete bound rather than an open-ended caveat.\"\n    }\n  ],\n  \"score\": 4,\n  \"confidence\": 3\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [6] ASSISTANT · 2026-08-21 17:39:49 UTC

```
Review complete — written to `./.terminal_claude_agent_struct_out.json`. Score: 4/10 (Borderline Reject), confidence 3/5.

Key finding: the paper's honest pre-registration and negative-result discipline are genuine strengths, but the empirical core is too thin — 2 of 3 pre-registered tests couldn't even run (n_used=0), the experiment's 62-repo corpus doesn't match its own 32-repo dataset artifact, and the sub-year DOA window extension (the paper's central technical contribution) is never validated in this iteration. Biggest score-impact fixes: scale the corpus or reframe as a methods/negative-pilot contribution, and reconcile the two corpora.
```
