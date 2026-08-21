# upd_hypo — test_idea

> Phase: `invention_loop` · round 2 · `upd_hypo`
> Run: `iter1_0b7b616dce39` — Scaling the Corpus, Auditing the Power, and Reconciling the Sign: What Happens When a Founder-Diffusion Survival Test Is Finally Interrogated Rather Than Just Run
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `upd_hypo` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-08-21 21:28:58 UTC

```
model: claude-sonnet-5 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/upd_hypo/upd_hypo
```

### [2] SYSTEM-USER prompt · 2026-08-21 21:29:08 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis reviser (Step 3.6: UPD_HYPO in the invention loop)

You received the current hypothesis, all artifacts, and the paper draft.
Revise the hypothesis based on what the evidence supports.

Honest revision → focused research. Inflated confidence → wasted iteration.
</your_role>
</ai_inventor_context>

You are revising a research hypothesis based on empirical evidence gathered
during an iterative invention loop. Your role is internal reflection — honest
assessment of what the evidence supports.

SCOPE: Your ONLY output is the revised hypothesis text. You do NOT run code,
produce artifacts, fix bugs, or otherwise act on the evidence yourself — the
next iteration of the invention loop will spawn fresh artifacts based on your
revised hypothesis. Reflect on the evidence and rewrite the hypothesis;
nothing else.

PRINCIPLES:
- Ground every revision in specific artifacts and results
- Treat negative and null results as valuable contributions. If the original
  approach failed, the null result IS often the contribution — frame it as
  such (e.g. "X does not improve Y under conditions Z"). Only pivot to a
  different positive claim when the evidence actually supports one; never
  fabricate a positive narrative to mask a failed approach.
- Increase specificity as evidence accumulates
- Don't inflate confidence without strong evidence
- Preserve the core AII prompt unless evidence clearly contradicts it
- Revise hypothesis text only — never attempt to address feedback by running
  code, proposing fixes, or producing artifacts; the next loop iteration
  handles all artifact generation

<current_hypothesis>
The hypothesis as it stands. Revise it based on the evidence below.

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
</current_hypothesis>

<all_artifacts>
Complete set of research artifacts across all iterations.

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
in_dependencies:
- id: art_ZbwYXh1VlhVp
  label: prior corpus
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
in_dependencies:
- id: art_4CZ-9Ou1G5ty
  label: prior pipeline
- id: art_ZbwYXh1VlhVp
  label: prior corpus
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
</all_artifacts>

<new_artifacts_this_iteration>
These 3 artifacts were created THIS iteration.

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

id: art_An3IzNVz6VIl
type: experiment
in_dependencies:
- id: art_ZbwYXh1VlhVp
  label: prior corpus
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

id: art_qP98tth_1H79
type: evaluation
in_dependencies:
- id: art_4CZ-9Ou1G5ty
  label: prior pipeline
- id: art_ZbwYXh1VlhVp
  label: prior corpus
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
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

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
</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (methodology) This is the second consecutive iteration in which a pipeline-timing race has prevented the statistical battery from running on the intended, freshly-built corpus. The prior iteration disclosed one such race between the experiment and evaluation stages; this iteration discloses a second, now also implicating the dataset-construction stage, and proposes the identical fix (a completion signal) that was apparently not implemented after the first disclosure. The Discussion section itself concedes the general problem was never fixed, only the specific instance. Submitting a paper whose central defect is 'we found the same class of bug again because we didn't fix the general case last time' is a stronger signal that the underlying engineering practice is unreliable than that this particular result is publishable.
  Action: Before resubmission, implement the completion-signal fix described in Discussion (downstream stages block on an explicit artifact-ready marker rather than a fixed schedule) and re-run the pipeline end-to-end on the 254-repository corpus. If time truly does not permit this, the paper should not claim a 'second disclosed pipeline-timing defect' as a contribution (bullet 5 of Summary of Contributions) -- reframe it as an unresolved risk carried over from the prior iteration and explain concretely why the fix proposed after the first occurrence was not implemented before this run started.
- [MAJOR] (evidence) The paper's headline new empirical claim -- that pre-departure diffusion timing and Medappa et al.'s static write-access ratio point in opposite directions -- is not actually estimated by the model designed to test it. The joint logistic model including medappa_ratio, timing_term, their interaction, and founder-share fails with a singular matrix at n=13, so the interaction term that would directly test the reconciling hypothesis is never fit. The reported evidence (Cohen's d and single-covariate regressions, both non-significant at n=13) is a fallback, and the paper's own Limitations section acknowledges this, but the framing in the Abstract-equivalent Contributions list and Conclusion ('a first same-corpus test...suggesting...they point in genuinely opposite directions') reads more confidently than the underlying non-converging joint model and n=13 univariate fallbacks support.
  Action: Either (a) apply the Firth bias-reduced regression already used to rescue the placebo test to the joint reconciliation model, since Firth's whole purpose is to remain finite exactly where standard MLE fails with a singular information matrix -- this is a straightforward, already-available fix given the tooling used elsewhere in the paper -- or (b) soften every claim about the medappa_ratio/timing_term dissociation throughout the paper (Contributions, Results, Discussion, Conclusion) to explicitly flag it as based on univariate fallback statistics only, not the joint model the reconciliation was designed around.
- [MINOR] (rigor) The n-required-for-80%-power figures (120 events for founder-share, 60 for diffused-owner-count) are computed by fixing the true effect at the coefficient observed in a non-significant n=16 fit. The paper's own Limitations section notes this circularity (if the true effect is smaller, more events are needed) but the number is nonetheless repeated prominently, unqualified, five separate times across Abstract-equivalent Contributions, Results, Discussion, and Conclusion, which risks the reader treating 120 as a firmer target than the audit itself supports.
  Action: State the n=120/n=60 figures with an explicit sensitivity range the first time they are introduced (e.g., 'assuming the true effect is at least as large as the n=16 point estimate; if the true effect is half that size, the required n is approximately X') rather than repeating the bare point figure unqualified in every subsequent section.
- [MINOR] (novelty) The prior review asked for an explicit comparison of this project's fame-independent, stratified sampling frame against Nourry et al.'s 36,000-project TFDD re-examination's own sampling approach, to substantiate whether the sampling-design contribution is genuinely novel in this literature. This iteration's Related Work paragraph on Nourry et al. still only compares the reported survival/re-adoption base rate, not the sampling methodology itself.
  Action: Add one sentence in Related Work stating explicitly whether Nourry et al.'s 36,000-project sample conditions on present-day popularity/fame or is otherwise constructed, and how that compares to this paper's fame-independent six-language-by-three-star-stratum frame, to substantiate the novelty claim implicit in treating fame-independence as this project's own methodological fix.
- [MINOR] (clarity) The paper is written throughout as a direct continuation of and commentary on 'the prior iteration,' with recurring phrases ('unchanged from the prior iteration', 'the prior iteration disclosed', 'the prior iteration's own power analysis specified roughly 40 events') that assume the reader has that other, unpublished draft in hand. A reader encountering only this submission cannot verify or contextualize those comparisons without the earlier paper.
  Action: Either include the prior iteration's key results as an explicit appendix/supplementary table so comparisons are self-contained, or rewrite comparative statements to state the relevant prior fact directly (e.g., 'a 40-event power target derived from a bootstrap-based method, see Appendix A' or simply the number itself) rather than referring to an external, unavailable document.
- [MINOR] (scope) The matched-pairs bootstrap analysis at the experiment-stage snapshot finds 4 eligible pairs (versus 0 previously) but reports an undefined risk ratio because the pairs do not span both survival outcomes -- functionally the same null result as the prior iteration's 0-pair outcome, just reached one step further into the pipeline. This is reported accurately but without much discussion of whether the matched-pairs design is simply unworkable at this project's achievable n and should be dropped from the battery going forward.
  Action: Add a sentence assessing whether matched-pairs bootstrap risk-ratio estimation is a viable component of this battery at any n below roughly 30-40 founder-only events (using the same Monte Carlo power-audit machinery already built for the regression), so future iterations know whether to keep reporting an always-undefined statistic.
</reviewer_feedback>



<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the field's landscape, prior work, crowded lanes, and the novelty bar — consult it while revising so the updated hypothesis stays genuinely novel and well-positioned.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<task>
IMPORTANT: Your ONLY output is the revised hypothesis text. Do NOT run code, produce artifacts,
fix bugs, or attempt to address the evidence yourself — the next iteration of the invention loop
will generate fresh artifacts based on your revised hypothesis. Reflect and rewrite; nothing else.

Do NOT generate a completely new hypothesis. Take the current hypothesis and REVISE it
to incorporate new evidence. Keep the core idea — refine, narrow, or strengthen it.

1. Does the evidence support the hypothesis? Narrow or broaden scope as needed.
2. Which claims now have strong evidence? Which are still unsupported?
3. Should the hypothesis become more specific based on what we've learned?
4. If reviewer feedback is provided, address the critiques directly.

STABILITY IS OK: If progress is good and evidence supports the current direction, keep the
hypothesis similar or identical. Only make substantive changes when evidence clearly calls for
them — e.g., contradictory results, fundamental reviewer critiques, or findings that refine scope.

You must also classify two kinds of edges in the research trace:

(A) The H↔H edge — how does this revised hypothesis relate to the previous one?
    Set `relation_type` (Moulines's structuralist typology) to one of:
    - "evolution": refining specialised claims, same conceptual frame
    - "embedding": previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian shift)
    Set `relation_rationale` to a brief justification (≤120 chars).

(B) The A↔A edges — for each artifact created THIS iteration, classify each of its
    `in_dependencies` (predecessor → dependent) using MultiCite's citation-function
    typology (Lauscher et al., NAACL 2022) — emit one entry in `artifact_relations`
    per (predecessor, dependent) pair. Predecessors are ALWAYS artifacts from EARLIER
    iterations — artifacts within one iteration run in parallel and cannot depend on
    each other, so never emit a relation between two same-iteration artifacts (it
    will be dropped):
    - "background": predecessor is treated as background context
    - "motivation": predecessor motivated this artifact's research
    - "uses": this artifact uses the predecessor's data, method, or output
    - "extends": this artifact extends the predecessor
    - "similarities": this artifact's results agree with the predecessor's
    - "differences": this artifact's results disagree with the predecessor's
    Each `relation_rationale` must be ≤120 characters.

Output the COMPLETE revised hypothesis (with the H↔H relation fields) AND the full
list of A↔A `artifact_relations` for this iteration's new artifacts.
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
    "ArtifactRelation": {
      "description": "One typed A\u2194A edge between a dependent artifact and one of its in_dependencies.\n\nMultiCite citation-function typology (Lauscher et al., NAACL 2022),\nreduced to 6 plain-English types.",
      "properties": {
        "from_id": {
          "description": "ID of the predecessor artifact (the one being depended on)",
          "title": "From Id",
          "type": "string"
        },
        "to_id": {
          "description": "ID of the dependent artifact (the new artifact this iteration)",
          "title": "To Id",
          "type": "string"
        },
        "relation_type": {
          "description": "MultiCite citation-function type for the predecessor\u2192dependent edge: 'background' \u2014 predecessor is treated as background context; 'motivation' \u2014 predecessor motivated this artifact's research; 'uses' \u2014 this artifact uses the predecessor's data, method, or output; 'extends' \u2014 this artifact extends the predecessor; 'similarities' \u2014 this artifact's results agree with the predecessor's; 'differences' \u2014 this artifact's results disagree with the predecessor's.",
          "enum": [
            "background",
            "motivation",
            "uses",
            "extends",
            "similarities",
            "differences"
          ],
          "title": "Relation Type",
          "type": "string"
        },
        "relation_rationale": {
          "description": "Brief rationale for this relation type (one short line, max 120 characters).",
          "maxLength": 120,
          "title": "Relation Rationale",
          "type": "string"
        }
      },
      "required": [
        "from_id",
        "to_id",
        "relation_type",
        "relation_rationale"
      ],
      "title": "ArtifactRelation",
      "type": "object"
    }
  },
  "description": "Revised hypothesis after reviewing iteration results.\n\nOutput matches the hypothesis dict structure so it can replace the\noriginal hypothesis in subsequent iterations.",
  "properties": {
    "title": {
      "description": "Revised hypothesis title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); may be unchanged if still accurate.",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "Revised hypothesis statement \u2014 what we now believe based on evidence",
      "title": "Hypothesis",
      "type": "string"
    },
    "relation_rationale": {
      "description": "Brief rationale for the H\u2194H revision type (one short line, max 120 characters).",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    },
    "confidence_delta": {
      "description": "How confidence changed: 'increased', 'decreased', or 'unchanged'",
      "title": "Confidence Delta",
      "type": "string"
    },
    "key_changes": {
      "description": "Bullet list of specific changes made to the hypothesis",
      "items": {
        "type": "string"
      },
      "title": "Key Changes",
      "type": "array"
    },
    "relation_type": {
      "description": "Moulines's structuralist typology of this hypothesis revision: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (incommensurable, Kuhnian revolution).",
      "enum": [
        "evolution",
        "embedding",
        "replacement"
      ],
      "title": "Relation Type",
      "type": "string"
    },
    "artifact_relations": {
      "description": "Typed A\u2194A edges for this iteration's new artifacts. Emit one entry per (predecessor \u2192 dependent) edge for every in_dependency on each artifact produced this iteration.",
      "items": {
        "$ref": "#/$defs/ArtifactRelation"
      },
      "title": "Artifact Relations",
      "type": "array"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "relation_rationale",
    "confidence_delta",
    "key_changes",
    "relation_type"
  ],
  "title": "RevisedHypothesis",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [3] HUMAN-USER prompt · 2026-08-21 21:29:08 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [4] TOOL CALL — Write · 2026-08-21 21:30:28 UTC

```
File: /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json

{
  "title": "Pre-Departure Authority Diffusion and OSS Survival",
  "hypothesis": "An open-source project's survival after its founder stops committing (a founder-only Truck Factor Developer Detachment, or TFDD, in Avelino et al.'s ESEM 2019 terminology) is hypothesized to depend less on the project's popularity or size at the moment of departure -- which Avelino et al. already show is statistically indistinguishable between survivors and non-survivors at the TFDD snapshot (d=0.13-0.26) -- and more on how diffused DOA-based commit/file authority already was among non-founder contributors in the 6-12 months BEFORE departure. Three iterations of testing establish the following, in order of evidential strength. (1) STRONGLY SUPPORTED: a fame-conditioned corpus structurally cannot test this hypothesis (it excludes non-surviving events by construction); a stratified, popularity-independent sampling frame across 6 languages and 3 star strata restores real outcome variance (14.3-45.0% survival across four different snapshots so far, bracketing Avelino et al.'s 40.6% reference), and this corpus-construction method is the load-bearing, reusable contribution -- now demonstrated a second time at greater scale (1,170 sampled -> 254 processed repositories, a fully disclosed per-cell funnel) though NOT yet run through the DOA/TFDD statistical pipeline. (2) NOT YET SUPPORTED OR REFUTED, AND NOW FORMALLY DIAGNOSED AS UNDERPOWERED RATHER THAN MERELY 'SMALL n': across four regression fits at n=13-20 spanning two iterations, the founder-share coefficient is negative (hypothesis-consistent direction) in every fit that converges, but none reaches significance and one fit outright fails with a singular information matrix. A Monte Carlo power audit run on this iteration's data shows this is not incidental: at n=16 with the current covariate set, no finite minimum detectable effect exists (power stays <=5.7% even at large simulated true effects, the signature of quasi-complete separation), and reaching 80% power at the observed effect size requires an estimated ~120 events for founder-share and ~60 for diffused-owner-count (roughly 3.75-7.5x the achieved n) -- these figures assume the n=16 point estimate approximates the true effect and should be read with that caveat, not as a firm target. The hypothesis's central causal claim remains open pending a corpus run at that scale; the 254-repository corpus already built is a plausible (though unverified, ~55-75-event-projected) step toward it. (3) PARTIALLY ADDRESSED, STILL OPEN: the working reconciliation with Medappa et al.'s opposite-signed finding (higher static write-access ratio reduces survival) was tested for the first time in the same corpus (n=13): a static whole-history write-access-ratio measure (medappa_ratio) replicates Medappa et al.'s sign, while this hypothesis's timing-specific founder-share measure retains the opposite, protective sign, and the two are not collinear (VIF~1.0) -- but the joint model with their interaction term, the model actually designed to test the reconciling claim, fails to converge at this n, so the dissociation rests on univariate fallback statistics only and must be treated as suggestive, not established, until it can be fit jointly (via a Firth-type penalized regression, mirroring the successful Firth rescue of the placebo test) at a larger n. (4) NEW METHODOLOGICAL FINDING THIS ITERATION: a second, distinct pipeline-timing race (beyond the one disclosed and only partially fixed after iteration 1) caused the experiment and evaluation stages to consume earlier, smaller intermediate snapshots of the corpus than the dataset-construction stage ultimately produced -- confirmed via file-modification timestamps, not inferred. This recurrence, on the identical class of bug, is itself informative: the fix scoped after the first disclosure (a completion signal) was not actually implemented before this run, so the general problem (any downstream stage can race ahead of a still-running upstream build stage) persists across whichever specific stage pair is involved. Implementing that completion-signal fix and re-running the full DOA/TFDD pipeline end-to-end on the already-built 254-repository corpus is now the single most concrete and highest-priority next step, since it would simultaneously test the core diffusion-predicts-survival claim at a larger, cleaner n and remove the recurring disclosure liability from the paper's central narrative.",
  "motivation": "The folk narrative around OSS abandonment treats founder departure as an exogenous shock whose outcome is explained after the fact by project popularity ('it was big enough to survive') or luck (a 'benevolent dictator' successor happened to appear). Avelino et al.'s full-text-verified ESEM 2019 results directly undercut the popularity explanation: at the TFDD snapshot itself, surviving and non-surviving projects show no meaningful difference in developers, commits, or files. That leaves a genuine open question their paper does not answer — if size doesn't predict survival at the moment of departure, what does? This hypothesis proposes that the missing signal is temporal rather than cross-sectional: it lives in the TREND of authority concentration in the run-up to departure, not in any single snapshot. Two iterations of empirical work have now shown the sign of that trend is consistently hypothesis-consistent but statistically underpowered at every achieved n, and a formal power audit has replaced a vague 'need more data' with a concrete (if provisional) scale target — sharpening, rather than resolving, the original motivation: foundations still lack an actionable, pre-departure-observable predictor, and this project's job is now specifically to reach the n at which that predictor can actually be tested rather than merely suggested.",
  "assumptions": [
    "Founder departure can be operationalized, following Avelino et al.'s validated Truck Factor Developer Detachment (TFDD) construct (ESEM 2019), as the point at which every developer in the project's Truck-Factor set has gone silent for the validated 1-year abandoner threshold, which this study reuses rather than re-deriving.",
    "Truck Factor / core-developer status can be computed per year with the Degree-of-Authorship (DOA) algorithm Avelino et al. use, operationalizing 'authority' as file-level primary ownership rather than raw commit count.",
    "Projects included have sufficient post-departure history (>=1,095 days total history in this iteration's corpus-construction filter) so an 18-month post-departure survival window can be measured without right-censoring, following Avelino et al.'s own filtering discipline against 'perils of mining GitHub' artifacts, operationalized here via Kalliamvakou et al.'s bulk-import heuristic (>80% of files touched in the first week).",
    "Survival is operationalized as a graded outcome from post-departure activity (Active/Inactive state model), not a formal abandonment declaration, since most failed projects never post one.",
    "The founder's identity and non-founder authority-holders can be disambiguated via commit-author email/login matching, acknowledging this does not catch developers with multiple distinct GitHub accounts.",
    "A downstream analysis stage's cached/consumed snapshot of an upstream corpus-construction artifact must be verified via file-timestamp cross-checks before its results are reported as reflecting the corpus's final state — a lesson now learned twice in this project and treated as a standing methodological requirement, not a one-off fix.",
    "Statistical significance claims at small n (here n=13-20) must be accompanied by a formal power/minimum-detectable-effect diagnosis (e.g. Monte Carlo simulation) rather than reported as 'underpowered' qualitatively, since ordinary non-significance and quasi-complete-separation failure are different diagnoses with different implications for how much more data is needed."
  ],
  "investigation_approach": "1. Fix the recurring pipeline-timing race by implementing an explicit completion-signal marker that downstream experiment/evaluation stages block on before consuming a corpus-construction artifact, rather than relying on a fixed schedule or assuming completion. 2. Re-run the full validated DOA/TF/TFDD/diffusion/survival pipeline end-to-end on the already-built 254-repository, fame-independent, funnel-transparent corpus, verifying via timestamp that each stage consumes the final artifact from the stage before it. 3. Refit the core diffusion-predicts-survival regression (BH-corrected logistic, matched-pairs, Mann-Whitney, placebo/window-relocation) at whatever n this produces, using Firth bias-reduced penalized logistic regression wherever standard MLE fails with a singular information matrix (as already validated for the placebo test in this iteration) so quasi-complete separation no longer blocks a fit outright. 4. Apply the same Firth-regression fix to the joint medappa_ratio/timing_term/interaction reconciliation model that failed to converge at n=13, so the reconciling hypothesis (diffusion helps when concentrated pre-departure, hurts when structurally permanent) is actually tested by its designed model rather than only by univariate fallbacks. 5. Re-run the Monte Carlo power audit on the new n to check whether the ~120/~60-event targets from this iteration's n=16 extrapolation hold, tightening or loosening the audit's own required-n estimate. 6. Report the matched-pairs bootstrap component's viability explicitly: given it has produced an undefined or unusable risk ratio at every n tested so far (0 pairs, then 4 pairs spanning only one outcome), assess via the power-audit machinery whether it is workable at any n below ~30-40 founder-only events and either keep or drop it from the battery accordingly. 7. Add the requested comparison of this project's fame-independent sampling frame against Nourry et al.'s 36,000-project TFDD sampling methodology (not just outcome base rates) to substantiate the corpus-construction novelty claim.",
  "success_criteria": "1. The pipeline-timing race is fixed with an explicit completion-signal mechanism, and the full DOA/TFDD/diffusion pipeline is verified (via timestamp cross-check) to have run end-to-end on the final, largest available corpus for that iteration -- no further silent snapshot mismatches. 2. In the regression on the resulting larger n, the authority-diffusion predictors (founder authorship-share, distinct pre-departure DOA-owner count) reach statistical significance (p<0.05, BH-corrected) after controlling for stars, forks, and contributor count, OR the power audit confirms the achieved n still falls short of its own required-n estimate, in which case the honest report is a sharper power diagnosis (e.g. an updated MDE/required-n number) rather than a claimed effect. 3. The joint medappa_ratio/timing_term/interaction reconciliation model converges (via Firth regression if needed) and its interaction/sign-difference is reported as an estimated coefficient with a confidence interval, not only as a univariate fallback comparison. 4. The placebo/shuffle check continues to show the true pre-departure window's effect is distinguishable from a relocated window's (as it did this iteration via Firth regression, CI (-8.02, 6.72) including zero for the placebo but the true-window coefficient consistently negative and larger in magnitude). 5. The matched-pairs bootstrap component is either dropped from the battery with a stated rationale (viability threshold not reached) or retained with evidence it can produce a defined, interpretable risk ratio at the achieved n.",
  "related_works": [
    "Avelino, Constantinou, Valente & Serebrenik, 'On the abandonment and survival of open source projects: An empirical investigation' (ESEM 2019, arXiv:1906.08058) — the direct empirical basis: TFDD, DOA-based Truck Factor, Active/Inactive survival model, 41% unconditioned TFDD survival, and the snapshot-covariate null (size doesn't predict survival at departure) that motivates testing a pre-departure trajectory instead.",
    "Avelino, Ferreira, Valente et al., 'A novel approach for estimating Truck Factor' (ICPC 2016) — the DOA-based TF-estimation algorithm reused verbatim across all iterations of this project; validated against a manual survey of 67 projects but only computed as a single-time-point risk score in the original.",
    "Coelho & Valente, 'Why Modern Open Source Projects Fail' (FSE 2017, arXiv:1707.02327) — single-maintainer self-reported abandonment reasons and maintenance-practice correlates (contributing guidelines, CI adoption), a different unit (individual abandonment) and mechanism from this hypothesis's multi-contributor succession question, but corroborating that pre-existing process signals associate with failure risk.",
    "Medappa, Srinivasan et al. on write-access diffusion and OSS project outcomes — a well-powered (n=5,762) finding that a higher STATIC, whole-history ratio of write-access contributors reduces survival, the opposite sign from this hypothesis's DYNAMIC, founder-specific, pre-departure-window diffusion measure. This iteration ran the first same-corpus test of both constructs (n=13, univariate only, joint model non-convergent): medappa_ratio replicates Medappa et al.'s sign while founder-share retains the opposite sign, VIF~1.0 rules out trivial collinearity, but the reconciling interaction term itself remains unestimated pending a Firth-regression refit at larger n.",
    "Nourry et al.'s ~36,000-project TFDD re-examination — reports a lower (27%) new-TF-developer-attraction rate than Avelino et al.'s 41%, a base rate this project's 14.3-45.0% strict/relaxed survival range across snapshots brackets loosely; the explicit sampling-methodology comparison (does Nourry et al. condition on present-day fame the way the pre-fix corpus in this project's first iteration did) requested by reviewer feedback remains to be added to substantiate this project's fame-independence novelty claim.",
    "Kalliamvakou et al., 'The promises and perils of mining GitHub' — the bulk-import-artifact heuristic (>80% of all-time-touched files touched in the first week) this project's corpus-construction pipeline applies at every iteration to exclude squash/import artifacts from the founder-candidate pool.",
    "Firth (1993) bias-reduced penalized logistic regression — the technique this iteration used to rescue the placebo-window regression from an uninterpretable near-infinite coefficient under quasi-complete separation, and the technique explicitly identified (per reviewer feedback) as the fix still needed for the non-converging joint reconciliation model."
  ],
  "inspiration": "The inspiration remains the analogy to organizational succession research: founder-led organizations survive exit better when authority was already delegated beforehand ('planned succession') rather than concentrated until the moment of transition ('crisis succession'). Two iterations in, a second inspiration has emerged from the project's own methodological trajectory: the discipline of formally diagnosing WHY a test is underpowered (quasi-complete separation, diagnosed via Monte Carlo simulation, rather than just reporting a non-significant p-value) turns 'we need more data' from a vague hedge into a falsifiable, effect-size-grounded target — and the discovery that the SAME class of pipeline-timing bug recurred after being 'fixed' once is itself a reminder that a specific patch is not the same as fixing the general failure mode it was an instance of.",
  "terms": [
    {"term": "Truck Factor Developer Detachment (TFDD)", "definition": "Avelino et al.'s (ESEM 2019) term for the event at which every developer in a project's current Truck-Factor set has gone silent for the validated 1-year abandoner threshold; this hypothesis's 'founder departure point' is the founder-only subset (TF=1 at detachment)."},
    {"term": "Degree of Authorship (DOA)", "definition": "The file-level expertise metric (Fritz et al., reused by Avelino et al.'s TF algorithm) combining file creation and edit share; a developer is a file's primary author, and thus a candidate Truck-Factor/authority holder, when their DOA is highest among that file's contributors."},
    {"term": "Pre-departure authority diffusion", "definition": "The degree to which DOA-based file ownership and authored-commit share had already shifted away from the founder to other contributors during the 6-12 months immediately before the founder's TFDD, measured as founder commit-share and count of distinct non-founder DOA file-owners in that window."},
    {"term": "Quasi-complete separation / minimum detectable effect (MDE)", "definition": "A small-sample logistic-regression failure mode in which outcomes become near-perfectly separable by covariates, causing MLE and its Wald standard error to diverge together; diagnosed in this project's power audit as power failing to rise even at large simulated true effect sizes, distinct from an ordinary non-significant result and requiring a specific fix (Firth regression) rather than only more conservative inference."},
    {"term": "Static write-access ratio (medappa_ratio)", "definition": "A whole-project-history, non-founder-specific measure of authority diffusion (count of distinct primary-DOA file owners divided by all distinct developers active before TFDD), constructed this iteration to test Medappa et al.'s construct directly in the same corpus as this project's timing-specific founder-share measure."},
    {"term": "Post-departure survival", "definition": "Following Avelino et al.'s Active/Inactive model: whether a project attracts a new TF developer and shows non-trivial activity persisting at least 18 months after the founder's TFDD, identified from commit silence rather than a formal abandonment declaration."}
  ],
  "summary": "Whether an open-source project survives its founder stepping away is hypothesized to depend on whether commit/file authority had already diffused away from the founder in the 6-12 months before departure, not on popularity or size at the moment of departure. Two iterations of real-data testing find the diffusion coefficient's sign consistently hypothesis-consistent but never significant, and a formal power audit now diagnoses why (quasi-complete separation at n=16-20, ~120/~60 events needed for 80% power) rather than leaving 'underpowered' vague; a first same-corpus reconciliation with Medappa et al.'s opposite-signed static-ratio finding shows a real dissociation in univariate statistics but awaits a converging joint model; and a second disclosed pipeline-timing defect, recurring after an incomplete fix, makes implementing a proper completion-signal fix and re-running the pipeline on the already-built 254-repository corpus the clear next step.",
  "_relation_rationale": "Same TFDD/DOA frame; power diagnosis formalized, reconciliation partially tested, recurring pipeline bug now first-class scope item.",
  "_confidence_delta": "unchanged",
  "_key_changes": [
    "Formalized the power-audit result (quasi-complete separation, ~120/~60-event targets with explicit caveat) as evidence item (2), replacing the prior iteration's qualitative 'ordinary underpowered first pass' framing.",
    "Added the medappa_ratio/timing_term reconciliation as evidence item (3), explicitly flagged as univariate-fallback-only pending a Firth-regression refit of the non-converging joint model, per reviewer MAJOR feedback.",
    "Added the second, recurring pipeline-timing race as evidence item (4) and elevated fixing it (completion-signal mechanism) plus re-running the pipeline on the 254-repo corpus to the single highest-priority next step, per reviewer MAJOR feedback.",
    "Added the matched-pairs bootstrap viability question (drop or retain at achievable n) to success_criteria and investigation_approach, per reviewer MINOR feedback.",
    "Added the requested Nourry et al. sampling-methodology (not just base-rate) comparison to related_works/investigation_approach, per reviewer MINOR feedback.",
    "Added the standing methodological requirement (timestamp cross-checks; formal power diagnosis, not qualitative) as new assumptions, generalizing the lesson from this iteration's recurring bug."
  ],
  "relation_type": "evolution",
  "artifact_relations": [
    {"from_id": "art_ZbwYXh1VlhVp", "to_id": "art_kuFKmgecMVuK", "relation_type": "extends", "relation_rationale": "Scales the same stratified sampling design from prior corpus (270→1,170 sampled, 69→254 processed)."},
    {"from_id": "art_ZbwYXh1VlhVp", "to_id": "art_An3IzNVz6VIl", "relation_type": "uses", "relation_rationale": "Re-runs the pipeline on the exact same 34-repo, 70,260-row corpus mined in iter1."},
    {"from_id": "art_4CZ-9Ou1G5ty", "to_id": "art_qP98tth_1H79", "relation_type": "uses", "relation_rationale": "Audits/re-derives statistics directly from iter1 experiment's method_out.json and results."},
    {"from_id": "art_ZbwYXh1VlhVp", "to_id": "art_qP98tth_1H79", "relation_type": "background", "relation_rationale": "Corpus underlying the experiment this evaluation audits, cited for provenance context."}
  ]
}
```

### [5] TOOL RESULT — Write · 2026-08-21 21:30:28 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Pre-Departure Authority Diffusion and OSS Survival\",\n  \"hypothesis\": \"An open-source project's survival after its founder stops committing (a founder-only Truck Factor Developer Detachment, or TFDD, in Avelino et al.'s ESEM 2019 terminology) is hypothesized to depend less on the project's popularity or size at the moment of departure -- which Avelino et al. already show is statistically indistinguishable between survivors and non-survivors at the TFDD snapshot (d=0.13-0.26) -- and more on how diffused DOA-based commit/file authority already was among non-founder contributors in the 6-12 months BEFORE departure. Three iterations of testing establish the following, in order of evidential strength. (1) STRONGLY SUPPORTED: a fame-conditioned corpus structurally cannot test this hypothesis (it excludes non-surviving events by construction); a stratified, popularity-independent sampling frame across 6 languages and 3 star strata restores real outcome variance (14.3-45.0% survival across four different snapshots so far, bracketing Avelino et al.'s 40.6% reference), and this corpus-construction method is the load-bearing, reusable contribution -- now demonstrated a second time at greater scale (1,170 sampled -> 254 processed repositories, a fully disclosed per-cell funnel) though NOT yet run through the DOA/TFDD statistical pipeline. (2) NOT YET SUPPORTED OR REFUTED, AND NOW FORMALLY DIAGNOSED AS UNDERPOWERED RATHER THAN MERELY 'SMALL n': across four regression fits at n=13-20 spanning two iterations, the founder-share coefficient is negative (hypothesis-consistent direction) in every fit that converges, but none reaches significance and one fit outright fails with a singular information matrix. A Monte Carlo power audit run on this iteration's data shows this is not incidental: at n=16 with the current covariate set, no finite minimum detectable effect exists (power stays <=5.7% even at large simulated true effects, the signature of quasi-complete separation), and reaching 80% power at the observed effect size requires an estimated ~120 events for founder-share and ~60 for diffused-owner-count (roughly 3.75-7.5x the achieved n) -- these figures assume the n=16 point estimate approximates the true effect and should be read with that caveat, not as a firm target. The hypothesis's central causal claim remains open pending a corpus run at that scale; the 254-repository corpus already built is a plausible (though unverified, ~55-75-event-projected) step toward it. (3) PARTIALLY ADDRESSED, STILL OPEN: the working reconciliation with Medappa et al.'s opposite-signed finding (higher static write-access ratio reduces survival) was tested for the first time in the same corpus (n=13): a static whole-history write-access-ratio measure (medappa_ratio) replicates Medappa et al.'s sign, while this hypothesis's timing-specific founder-share measure retains the opposite, protective sign, and the two are not collinear (VIF~1.0) -- but the joint model with their interaction term, the model actually designed to test the reconciling claim, fails to converge at this n, so the dissociation rests on univariate fallback statistics only and must be treated as suggestive, not established, until it can be fit jointly (via a Firth-type penalized regression, mirroring the successful Firth rescue of the placebo test) at a larger n. (4) NEW METHODOLOGICAL FINDING THIS ITERATION: a second, distinct pipeline-timing race (beyond the one disclosed and only partially fixed after iteration 1) caused the experiment and evaluation stages to consume earlier, smaller intermediate snapshots of the corpus than the dataset-construction stage ultimately produced -- confirmed via file-modification timestamps, not inferred. This recurrence, on the identical class of bug, is itself informative: the fix scoped after the first disclosure (a completion signal) was not actually implemented before this run, so the general problem (any downstream stage can race ahead of a still-running upstream build stage) persists across whichever specific stage pair is involved. Implementing that completion-signal fix and re-running the full DOA/TFDD pipeline end-to-end on the already-built 254-repository corpus is now the single most concrete and highest-priority next step, since it would simultaneously test the core diffusion-predicts-survival claim at a larger, cleaner n and remove the recurring disclosure liability from the paper's central narrative.\",\n  \"motivation\": \"The folk narrative around OSS abandonment treats founder departure as an exogenous shock whose outcome is explained after the fact by project popularity ('it was big enough to survive') or luck (a 'benevolent dictator' successor happened to appear). Avelino et al.'s full-text-verified ESEM 2019 results directly undercut the popularity explanation: at the TFDD snapshot itself, surviving and non-surviving projects show no meaningful difference in developers, commits, or files. That leaves a genuine open question their paper does not answer — if size doesn't predict survival at the moment of departure, what does? This hypothesis proposes that the missing signal is temporal rather than cross-sectional: it lives in the TREND of authority concentration in the run-up to departure, not in any single snapshot. Two iterations of empirical work have now shown the sign of that trend is consistently hypothesis-consistent but statistically underpowered at every achieved n, and a formal power audit has replaced a vague 'need more data' with a concrete (if provisional) scale target — sharpening, rather than resolving, the original motivation: foundations still lack an actionable, pre-departure-observable predictor, and this project's job is now specifically to reach the n at which that predictor can actually be tested rather than merely suggested.\",\n  \"assumptions\": [\n    \"Founder departure can be operationalized, following Avelino et al.'s validated Truck Factor Developer Detachment (TFDD) construct (ESEM 2019), as the point at which every developer in the project's Truck-Factor set has gone silent for the validated 1-year abandoner threshold, which this study reuses rather than re-deriving.\",\n    \"Truck Factor / core-developer status can be computed per year with the Degree-of-Authorship (DOA) algorithm Avelino et al. use, operationalizing 'authority' as file-level primary ownership rather than raw commit count.\",\n    \"Projects included have sufficient post-departure history (>=1,095 days total history in this iteration's corpus-construction filter) so an 18-month post-departure survival window can be measured without right-censoring, following Avelino et al.'s own filtering discipline against 'perils of mining GitHub' artifacts, operationalized here via Kalliamvakou et al.'s bulk-import heuristic (>80% of files touched in the first week).\",\n    \"Survival is operationalized as a graded outcome from post-departure activity (Active/Inactive state model), not a formal abandonment declaration, since most failed projects never post one.\",\n    \"The founder's identity and non-founder authority-holders can be disambiguated via commit-author email/login matching, acknowledging this does not catch developers with multiple distinct GitHub accounts.\",\n    \"A downstream analysis stage's cached/consumed snapshot of an upstream corpus-construction artifact must be verified via file-timestamp cross-checks before its results are reported as reflecting the corpus's final state — a lesson now learned twice in this project and treated as a standing methodological requirement, not a one-off fix.\",\n    \"Statistical significance claims at small n (here n=13-20) must be accompanied by a formal power/minimum-detectable-effect diagnosis (e.g. Monte Carlo simulation) rather than reported as 'underpowered' qualitatively, since ordinary non-significance and quasi-complete-separation failure are different diagnoses with different implications for how much more data is needed.\"\n  ],\n  \"investigation_approach\": \"1. Fix the recurring pipeline-timing race by implementing an explicit completion-signal marker that downstream experiment/evaluation stages block on before consuming a corpus-construction artifact, rather than relying on a fixed schedule or assuming completion. 2. Re-run the full validated DOA/TF/TFDD/diffusion/survival pipeline end-to-end on the already-built 254-repository, fame-independent, funnel-transparent corpus, verifying via timestamp that each stage consumes the final artifact from the stage before it. 3. Refit the core diffusion-predicts-survival regression (BH-corrected logistic, matched-pairs, Mann-Whitney, placebo/window-relocation) at whatever n this produces, using Firth bias-reduced penalized logistic regression wherever standard MLE fails with a singular information matrix (as already validated for the placebo test in this iteration) so quasi-complete separation no longer blocks a fit outright. 4. Apply the same Firth-regression fix to the joint medappa_ratio/timing_term/interaction reconciliation model that failed to converge at n=13, so the reconciling hypothesis (diffusion helps when concentrated pre-departure, hurts when structurally permanent) is actually tested by its designed model rather than only by univariate fallbacks. 5. Re-run the Monte Carlo power audit on the new n to check whether the ~120/~60-event targets from this iteration's n=16 extrapolation hold, tightening or loosening the audit's own required-n estimate. 6. Report the matched-pairs bootstrap component's viability explicitly: given it has produced an undefined or unusable risk ratio at every n tested so far (0 pairs, then 4 pairs spanning only one outcome), assess via the power-audit machinery whether it is workable at any n below ~30-40 founder-only events and either keep or drop it from the battery accordingly. 7. Add the requested comparison of this project's fame-independent sampling frame against Nourry et al.'s 36,000-project TFDD sampling methodology (not just outcome base rates) to substantiate the corpus-construction novelty claim.\",\n  \"success_criteria\": \"1. The pipeline-timing race is fixed with an explicit completion-signal mechanism, and the full DOA/TFDD/diffusion pipeline is verified (via timestamp cross-check) to have run end-to-end on the final, largest available corpus for that iteration -- no further silent snapshot mismatches. 2. In the regression on the resulting larger n, the authority-diffusion predictors (founder authorship-share, distinct pre-departure DOA-owner count) reach statistical significance (p<0.05, BH-corrected) after controlling for stars, forks, and contributor count, OR the power audit confirms the achieved n still falls short of its own required-n estimate, in which case the honest report is a sharper power diagnosis (e.g. an updated MDE/required-n number) rather than a claimed effect. 3. The joint medappa_ratio/timing_term/interaction reconciliation model converges (via Firth regression if needed) and its interaction/sign-difference is reported as an estimated coefficient with a confidence interval, not only as a univariate fallback comparison. 4. The placebo/shuffle check continues to show the true pre-departure window's effect is distinguishable from a relocated window's (as it did this iteration via Firth regression, CI (-8.02, 6.72) including zero for the placebo but the true-window coefficient consistently negative and larger in magnitude). 5. The matched-pairs bootstrap component is either dropped from the battery with a stated rationale (viability threshold not reached) or retained with evidence it can produce a defined, interpretable risk ratio at the achieved n.\",\n  \"related_works\": [\n    \"Avelino, Constantinou, Valente & Serebrenik, 'On the abandonment and survival of open source projects: An empirical investigation' (ESEM 2019, arXiv:1906.08058) — the direct empirical basis: TFDD, DOA-based Truck Factor, Active/Inactive survival model, 41% unconditioned TFDD survival, and the snapshot-covariate null (size doesn't predict survival at departure) that motivates testing a pre-departure trajectory instead.\",\n    \"Avelino, Ferreira, Valente et al., 'A novel approach for estimating Truck Factor' (ICPC 2016) — the DOA-based TF-estimation algorithm reused verbatim across all iterations of this project; validated against a manual survey of 67 projects but only computed as a single-time-point risk score in the original.\",\n    \"Coelho & Valente, 'Why Modern Open Source Projects Fail' (FSE 2017, arXiv:1707.02327) — single-maintainer self-reported abandonment reasons and maintenance-practice correlates (contributing guidelines, CI adoption), a different unit (individual abandonment) and mechanism from this hypothesis's multi-contributor succession question, but corroborating that pre-existing process signals associate with failure risk.\",\n    \"Medappa, Srinivasan et al. on write-access diffusion and OSS project outcomes — a well-powered (n=5,762) finding that a higher STATIC, whole-history ratio of write-access contributors reduces survival, the opposite sign from this hypothesis's DYNAMIC, founder-specific, pre-departure-window diffusion measure. This iteration ran the first same-corpus test of both constructs (n=13, univariate only, joint model non-convergent): medappa_ratio replicates Medappa et al.'s sign while founder-share retains the opposite sign, VIF~1.0 rules out trivial collinearity, but the reconciling interaction term itself remains unestimated pending a Firth-regression refit at larger n.\",\n    \"Nourry et al.'s ~36,000-project TFDD re-examination — reports a lower (27%) new-TF-developer-attraction rate than Avelino et al.'s 41%, a base rate this project's 14.3-45.0% strict/relaxed survival range across snapshots brackets loosely; the explicit sampling-methodology comparison (does Nourry et al. condition on present-day fame the way the pre-fix corpus in this project's first iteration did) requested by reviewer feedback remains to be added to substantiate this project's fame-independence novelty claim.\",\n    \"Kalliamvakou et al., 'The promises and perils of mining GitHub' — the bulk-import-artifact heuristic (>80% of all-time-touched files touched in the first week) this project's corpus-construction pipeline applies at every iteration to exclude squash/import artifacts from the founder-candidate pool.\",\n    \"Firth (1993) bias-reduced penalized logistic regression — the technique this iteration used to rescue the placebo-window regression from an uninterpretable near-infinite coefficient under quasi-complete separation, and the technique explicitly identified (per reviewer feedback) as the fix still needed for the non-converging joint reconciliation model.\"\n  ],\n  \"inspiration\": \"The inspiration remains the analogy to organizational succession research: founder-led organizations survive exit better when authority was already delegated beforehand ('planned succession') rather than concentrated until the moment of transition ('crisis succession'). Two iterations in, a second inspiration has emerged from the project's own methodological trajectory: the discipline of formally diagnosing WHY a test is underpowered (quasi-complete separation, diagnosed via Monte Carlo simulation, rather than just reporting a non-significant p-value) turns 'we need more data' from a vague hedge into a falsifiable, effect-size-grounded target — and the discovery that the SAME class of pipeline-timing bug recurred after being 'fixed' once is itself a reminder that a specific patch is not the same as fixing the general failure mode it was an instance of.\",\n  \"terms\": [\n    {\"term\": \"Truck Factor Developer Detachment (TFDD)\", \"definition\": \"Avelino et al.'s (ESEM 2019) term for the event at which every developer in a project's current Truck-Factor set has gone silent for the validated 1-year abandoner threshold; this hypothesis's 'founder departure point' is the founder-only subset (TF=1 at detachment).\"},\n    {\"term\": \"Degree of Authorship (DOA)\", \"definition\": \"The file-level expertise metric (Fritz et al., reused by Avelino et al.'s TF algorithm) combining file creation and edit share; a developer is a file's primary author, and thus a candidate Truck-Factor/authority holder, when their DOA is highest among that file's contributors.\"},\n    {\"term\": \"Pre-departure authority diffusion\", \"definition\": \"The degree to which DOA-based file ownership and authored-commit share had already shifted away from the founder to other contributors during the 6-12 months immediately before the founder's TFDD, measured as founder commit-share and count of distinct non-founder DOA file-owners in that window.\"},\n    {\"term\": \"Quasi-complete separation / minimum detectable effect (MDE)\", \"definition\": \"A small-sample logistic-regression failure mode in which outcomes become near-perfectly separable by covariates, causing MLE and its Wald standard error to diverge together; diagnosed in this project's power audit as power failing to rise even at large simulated true effect sizes, distinct from an ordinary non-significant result and requiring a specific fix (Firth regression) rather than only more conservative inference.\"},\n    {\"term\": \"Static write-access ratio (medappa_ratio)\", \"definition\": \"A whole-project-history, non-founder-specific measure of authority diffusion (count of distinct primary-DOA file owners divided by all distinct developers active before TFDD), constructed this iteration to test Medappa et al.'s construct directly in the same corpus as this project's timing-specific founder-share measure.\"},\n    {\"term\": \"Post-departure survival\", \"definition\": \"Following Avelino et al.'s Active/Inactive model: whether a project attracts a new TF developer and shows non-trivial activity persisting at least 18 months after the founder's TFDD, identified from commit silence rather than a formal abandonment declaration.\"}\n  ],\n  \"summary\": \"Whether an open-source project survives its founder stepping away is hypothesized to depend on whether commit/file authority had already diffused away from the founder in the 6-12 months before departure, not on popularity or size at the moment of departure. Two iterations of real-data testing find the diffusion coefficient's sign consistently hypothesis-consistent but never significant, and a formal power audit now diagnoses why (quasi-complete separation at n=16-20, ~120/~60 events needed for 80% power) rather than leaving 'underpowered' vague; a first same-corpus reconciliation with Medappa et al.'s opposite-signed static-ratio finding shows a real dissociation in univariate statistics but awaits a converging joint model; and a second disclosed pipeline-timing defect, recurring after an incomplete fix, makes implementing a proper completion-signal fix and re-running the pipeline on the already-built 254-repository corpus the clear next step.\",\n  \"_relation_rationale\": \"Same TFDD/DOA frame; power diagnosis formalized, reconciliation partially tested, recurring pipeline bug now first-class scope item.\",\n  \"_confidence_delta\": \"unchanged\",\n  \"_key_changes\": [\n    \"Formalized the power-audit result (quasi-complete separation, ~120/~60-event targets with explicit caveat) as evidence item (2), replacing the prior iteration's qualitative 'ordinary underpowered first pass' framing.\",\n    \"Added the medappa_ratio/timing_term reconciliation as evidence item (3), explicitly flagged as univariate-fallback-only pending a Firth-regression refit of the non-converging joint model, per reviewer MAJOR feedback.\",\n    \"Added the second, recurring pipeline-timing race as evidence item (4) and elevated fixing it (completion-signal mechanism) plus re-running the pipeline on the 254-repo corpus to the single highest-priority next step, per reviewer MAJOR feedback.\",\n    \"Added the matched-pairs bootstrap viability question (drop or retain at achievable n) to success_criteria and investigation_approach, per reviewer MINOR feedback.\",\n    \"Added the requested Nourry et al. sampling-methodology (not just base-rate) comparison to related_works/investigation_approach, per reviewer MINOR feedback.\",\n    \"Added the standing methodological requirement (timestamp cross-checks; formal power diagnosis, not qualitative) as new assumptions, generalizing the lesson from this iteration's recurring bug.\"\n  ],\n  \"relation_type\": \"evolution\",\n  \"artifact_relations\": [\n    {\"from_id\": \"art_ZbwYXh1VlhVp\", \"to_id\": \"art_kuFKmgecMVuK\", \"relation_type\": \"extends\", \"relation_rationale\": \"Scales the same stratified sampling design from prior corpus (270→1,170 sampled, 69→254 processed).\"},\n    {\"from_id\": \"art_ZbwYXh1VlhVp\", \"to_id\": \"art_An3IzNVz6VIl\", \"relation_type\": \"uses\", \"relation_rationale\": \"Re-runs the pipeline on the exact same 34-repo, 70,260-row corpus mined in iter1.\"},\n    {\"from_id\": \"art_4CZ-9Ou1G5ty\", \"to_id\": \"art_qP98tth_1H79\", \"relation_type\": \"uses\", \"relation_rationale\": \"Audits/re-derives statistics directly from iter1 experiment's method_out.json and results.\"},\n    {\"from_id\": \"art_ZbwYXh1VlhVp\", \"to_id\": \"art_qP98tth_1H79\", \"relation_type\": \"background\", \"relation_rationale\": \"Corpus underlying the experiment this evaluation audits, cited for provenance context.\"}\n  ]\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [6] ASSISTANT · 2026-08-21 21:30:30 UTC

```
Revised hypothesis written to `.terminal_claude_agent_struct_out.json`. Key updates: formalized the power-audit findings (quasi-complete separation, ~120/~60-event targets) as strengthened evidence item, added the medappa_ratio reconciliation as a partially-tested item pending a Firth-regression refit, elevated the recurring pipeline-timing bug to a first-class next-step, and addressed the reviewer's matched-pairs viability and Nourry et al. sampling-comparison requests. Relation type: evolution (same TFDD/DOA frame, refined specificity).
```

### [7] SYSTEM-USER prompt · 2026-08-21 21:30:32 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 3 problems — fix ALL of them at once:
  - at `<root>`: 'relation_rationale' is a required property
  - at `<root>`: 'confidence_delta' is a required property
  - at `<root>`: 'key_changes' is a required property
Every required field must be present and every field type must match the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [8] ASSISTANT · 2026-08-21 21:30:34 UTC

```
Fixing field names to match schema exactly.
```

### [9] TOOL CALL — Read · 2026-08-21 21:30:34 UTC

```
/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json
```

### [10] TOOL RESULT — Read · 2026-08-21 21:30:34 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Pre-Departure Authority Diffusion and OSS Survival\",\n  \"hypothesis\": \"An open-source project's survival after its founder stops committing (a founder-only Truck Factor Developer Detachment, or TFDD, in Avelino et al.'s ESEM 2019 terminology) is hypothesized to depend less on the project's popularity or size at the moment of departure -- which Avelino et al. already show is statistically indistinguishable between survivors and non-survivors at the TFDD snapshot (d=0.13-0.26) -- and more on how diffused DOA-based commit/file authority already was among non-founder contributors in the 6-12 months BEFORE departure. Three iterations of testing establish the following, in order of evidential strength. (1) STRONGLY SUPPORTED: a fame-conditioned corpus structurally cannot test this hypothesis (it excludes non-surviving events by construction); a stratified, popularity-independent sampling frame across 6 languages and 3 star strata restores real outcome variance (14.3-45.0% survival across four different snapshots so far, bracketing Avelino et al.'s 40.6% reference), and this corpus-construction method is the load-bearing, reusable contribution -- now demonstrated a second time at greater scale (1,170 sampled -> 254 processed repositories, a fully disclosed per-cell funnel) though NOT yet run through the DOA/TFDD statistical pipeline. (2) NOT YET SUPPORTED OR REFUTED, AND NOW FORMALLY DIAGNOSED AS UNDERPOWERED RATHER THAN MERELY 'SMALL n': across four regression fits at n=13-20 spanning two iterations, the founder-share coefficient is negative (hypothesis-consistent direction) in every fit that converges, but none reaches significance and one fit outright fails with a singular information matrix. A Monte Carlo power audit run on this iteration's data shows this is not incidental: at n=16 with the current covariate set, no finite minimum detectable effect exists (power stays <=5.7% even at large simulated true effects, the signature of quasi-complete separation), and reaching 80% power at the observed effect size requires an estimated ~120 events for founder-share and ~60 for diffused-owner-count (roughly 3.75-7.5x the achieved n) -- these figures assume the n=16 point estimate approximates the true effect and should be read with that caveat, not as a firm target. The hypothesis's central causal claim remains open pending a corpus run at that scale; the 254-repository corpus already built is a plausible (though unverified, ~55-75-event-projected) step toward it. (3) PARTIALLY ADDRESSED, STILL OPEN: the working reconciliation with Medappa et al.'s opposite-signed finding (higher static write-access ratio reduces survival) was tested for the first time in the same corpus (n=13): a static whole-history write-access-ratio measure (medappa_ratio) replicates Medappa et al.'s sign, while this hypothesis's timing-specific founder-share measure retains the opposite, protective sign, and the two are not collinear (VIF~1.0) -- but the joint model with their interaction term, the model actually designed to test the reconciling claim, fails to converge at this n, so the dissociation rests on univariate fallback statistics only and must be treated as suggestive, not established, until it can be fit jointly (via a Firth-type penalized regression, mirroring the successful Firth rescue of the placebo test) at a larger n. (4) NEW METHODOLOGICAL FINDING THIS ITERATION: a second, distinct pipeline-timing race (beyond the one disclosed and only partially fixed after iteration 1) caused the experiment and evaluation stages to consume earlier, smaller intermediate snapshots of the corpus than the dataset-construction stage ultimately produced -- confirmed via file-modification timestamps, not inferred. This recurrence, on the identical class of bug, is itself informative: the fix scoped after the first disclosure (a completion signal) was not actually implemented before this run, so the general problem (any downstream stage can race ahead of a still-running upstream build stage) persists across whichever specific stage pair is involved. Implementing that completion-signal fix and re-running the full DOA/TFDD pipeline end-to-end on the already-built 254-repository corpus is now the single most concrete and highest-priority next step, since it would simultaneously test the core diffusion-predicts-survival claim at a larger, cleaner n and remove the recurring disclosure liability from the paper's central narrative.\",\n  \"motivation\": \"The folk narrative around OSS abandonment treats founder departure as an exogenous shock whose outcome is explained after the fact by project popularity ('it was big enough to survive') or luck (a 'benevolent dictator' successor happened to appear). Avelino et al.'s full-text-verified ESEM 2019 results directly undercut the popularity explanation: at the TFDD snapshot itself, surviving and non-surviving projects show no meaningful difference in developers, commits, or files. That leaves a genuine open question their paper does not answer — if size doesn't predict survival at the moment of departure, what does? This hypothesis proposes that the missing signal is temporal rather than cross-sectional: it lives in the TREND of authority concentration in the run-up to departure, not in any single snapshot. Two iterations of empirical work have now shown the sign of that trend is consistently hypothesis-consistent but statistically underpowered at every achieved n, and a formal power audit has replaced a vague 'need more data' with a concrete (if provisional) scale target — sharpening, rather than resolving, the original motivation: foundations still lack an actionable, pre-departure-observable predictor, and this project's job is now specifically to reach the n at which that predictor can actually be tested rather than merely suggested.\",\n  \"assumptions\": [", "numLines": 5, "startLine": 1, "totalLines": 53}}
```

### [11] TOOL CALL — Edit · 2026-08-21 21:30:40 UTC

```
File: /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json
OLD:   "_relation_rationale": "Same TFDD/DOA frame; power diagnosis formalized, reconciliation partially tested, recurring pipeline bug now first-class scope item.",
  "_confidence_delta": "unchanged",
  "_key_changes": [
NEW:   "relation_rationale": "Same TFDD/DOA frame; power diagnosis formalized, reconciliation partially tested, recurring pipeline bug now first-class scope item.",
  "confidence_delta": "unchanged",
  "key_changes": [
```

### [12] TOOL RESULT — Edit · 2026-08-21 21:30:40 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json", "oldString": "  \"_relation_rationale\": \"Same TFDD/DOA frame; power diagnosis formalized, reconciliation partially tested, recurring pipeline bug now first-class scope item.\",\n  \"_confidence_delta\": \"unchanged\",\n  \"_key_changes\": [", "newString": "  \"relation_rationale\": \"Same TFDD/DOA frame; power diagnosis formalized, reconciliation partially tested, recurring pipeline bug now first-class scope item.\",\n  \"confidence_delta\": \"unchanged\",\n  \"key_changes\": [", "originalFile": null, "structuredPatch": [{"oldStart": 32, "oldLines": 9, "newStart": 32, "newLines": 9, "lines": ["     {\"term\": \"Post-departure survival\", \"definition\": \"Following Avelino et al.'s Active/Inactive model: whether a project attracts a new TF developer and shows non-trivial activity persisting at least 18 months after the founder's TFDD, identified from commit silence rather than a formal abandonment declaration.\"}", "   ],", "   \"summary\": \"Whether an open-source project survives its founder stepping away is hypothesized to depend on whether commit/file authority had already diffused away from the founder in the 6-12 months before departure, not on popularity or size at the moment of departure. Two iterations of real-data testing find the diffusion coefficient's sign consistently hypothesis-consistent but never significant, and a formal power audit now diagnoses why (quasi-complete separation at n=16-20, ~120/~60 events needed for 80% power) rather than leaving 'underpowered' vague; a first same-corpus reconciliation with Medappa et al.'s opposite-signed static-ratio finding shows a real dissociation in univariate statistics but awaits a converging joint model; and a second disclosed pipeline-timing defect, recurring after an incomplete fix, makes implementing a proper completion-signal fix and re-running the pipeline on the already-built 254-repository corpus the clear next step.\",", "-  \"_relation_rationale\": \"Same TFDD/DOA frame; power diagnosis formalized, reconciliation partially tested, recurring pipeline bug now first-class scope item.\",", "-  \"_confidence_delta\": \"unchanged\",", "-  \"_key_changes\": [", "+  \"relation_rationale\": \"Same TFDD/DOA frame; power diagnosis formalized, reconciliation partially tested, recurring pipeline bug now first-class scope item.\",", "+  \"confidence_delta\": \"unchanged\",", "+  \"key_changes\": [", "     \"Formalized the power-audit result (quasi-complete separation, ~120/~60-event targets with explicit caveat) as evidence item (2), replacing the prior iteration's qualitative 'ordinary underpowered first pass' framing.\",", "     \"Added the medappa_ratio/timing_term reconciliation as evidence item (3), explicitly flagged as univariate-fallback-only pending a Firth-regression refit of the non-converging joint model, per reviewer MAJOR feedback.\",", "     \"Added the second, recurring pipeline-timing race as evidence item (4) and elevated fixing it (completion-signal mechanism) plus re-running the pipeline on the 254-repo corpus to the single highest-priority next step, per reviewer MAJOR feedback.\","]}], "userModified": false, "replaceAll": false}
```

### [13] ASSISTANT · 2026-08-21 21:30:41 UTC

```
Fixed the field names to match the schema exactly.
```

### [14] SYSTEM-USER prompt · 2026-08-21 21:30:42 UTC

```
<validation-feedback>
Attempt 2 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Same TFDD/DOA frame; power diagnosis formalized, reconciliation partially tested, recurring pipeline bug now first-class scope item.' is too long (at most 120 characters, got 132)
Every required field must be present and every field type must match the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [15] TOOL CALL — Edit · 2026-08-21 21:30:46 UTC

```
File: /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json
OLD:   "relation_rationale": "Same TFDD/DOA frame; power diagnosis formalized, reconciliation partially tested, recurring pipeline bug now first-class scope item.",
NEW:   "relation_rationale": "Same frame; power diagnosis formalized, reconciliation partial, recurring pipeline bug now first-class.",
```

### [16] TOOL RESULT — Edit · 2026-08-21 21:30:46 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json", "oldString": "  \"relation_rationale\": \"Same TFDD/DOA frame; power diagnosis formalized, reconciliation partially tested, recurring pipeline bug now first-class scope item.\",", "newString": "  \"relation_rationale\": \"Same frame; power diagnosis formalized, reconciliation partial, recurring pipeline bug now first-class.\",", "originalFile": null, "structuredPatch": [{"oldStart": 32, "oldLines": 7, "newStart": 32, "newLines": 7, "lines": ["     {\"term\": \"Post-departure survival\", \"definition\": \"Following Avelino et al.'s Active/Inactive model: whether a project attracts a new TF developer and shows non-trivial activity persisting at least 18 months after the founder's TFDD, identified from commit silence rather than a formal abandonment declaration.\"}", "   ],", "   \"summary\": \"Whether an open-source project survives its founder stepping away is hypothesized to depend on whether commit/file authority had already diffused away from the founder in the 6-12 months before departure, not on popularity or size at the moment of departure. Two iterations of real-data testing find the diffusion coefficient's sign consistently hypothesis-consistent but never significant, and a formal power audit now diagnoses why (quasi-complete separation at n=16-20, ~120/~60 events needed for 80% power) rather than leaving 'underpowered' vague; a first same-corpus reconciliation with Medappa et al.'s opposite-signed static-ratio finding shows a real dissociation in univariate statistics but awaits a converging joint model; and a second disclosed pipeline-timing defect, recurring after an incomplete fix, makes implementing a proper completion-signal fix and re-running the pipeline on the already-built 254-repository corpus the clear next step.\",", "-  \"relation_rationale\": \"Same TFDD/DOA frame; power diagnosis formalized, reconciliation partially tested, recurring pipeline bug now first-class scope item.\",", "+  \"relation_rationale\": \"Same frame; power diagnosis formalized, reconciliation partial, recurring pipeline bug now first-class.\",", "   \"confidence_delta\": \"unchanged\",", "   \"key_changes\": [", "     \"Formalized the power-audit result (quasi-complete separation, ~120/~60-event targets with explicit caveat) as evidence item (2), replacing the prior iteration's qualitative 'ordinary underpowered first pass' framing.\","]}], "userModified": false, "replaceAll": false}
```

### [17] ASSISTANT · 2026-08-21 21:30:47 UTC

```
Shortened the rationale to fit the 120-char limit.
```
