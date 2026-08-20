# upd_hypo — test_idea

> Phase: `invention_loop` · round 2 · `upd_hypo`
> Run: `run_5SMkWpWKNLxk` — Measuring Authority Diffusion Before Founders Leave Open Source Projects
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `upd_hypo` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-08-20 21:10:43 UTC

```
model: claude-sonnet-5 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/upd_hypo/upd_hypo
```

### [2] SYSTEM-USER prompt · 2026-08-20 21:10:51 UTC

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
</current_hypothesis>

<all_artifacts>
Complete set of research artifacts across all iterations.

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
in_dependencies:
- id: art_ZuMis522AEPF
  label: dataset
- id: art_I5KoOp16hub5
  label: experiment
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
These 3 artifacts were created THIS iteration.

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

id: art_yOHrviKrh_11
type: evaluation
in_dependencies:
- id: art_ZuMis522AEPF
  label: dataset
- id: art_I5KoOp16hub5
  label: experiment
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
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

# Introduction

Open-source software projects routinely depend on the sustained attention of one or two people. When the developer who founded such a project stops committing, the project faces what Avelino et al. call a Truck-Factor Developer Detachment (TFDD): every developer in the project's minimal Truck-Factor set has gone silent for at least a validated twelve-month abandoner threshold [1]. Some of these projects go dark permanently; others are picked up by new maintainers and continue for years. What determines which outcome a given project has, before it happens, is the question this paper set out to answer. Avelino et al.'s own results show the obvious predictor does not work: at the TFDD snapshot itself, surviving and non-surviving projects are statistically indistinguishable in developers, commits, and files (Cohen's d = 0.13-0.26) [1]. Their finding leaves an open question -- if size at departure carries no signal, does the trend leading up to departure carry any? -- and this paper builds and rigorously calibrates the instrument needed to ask it.

We do not, in the end, answer that question empirically. This paper is a methodology and measurement contribution, not an empirical resolution of it, and we state that plainly up front rather than let it surface only in the limitations. We built a full reimplementation of Avelino et al.'s Degree-of-Authorship (DOA) / Truck-Factor / TFDD pipeline, added a new pre-departure authority-diffusion measurement -- founder commit-share and the count of distinct non-founder DOA-owners in the six to twelve months before a founder-only TFDD -- and subjected both to a two-stage calibration and robustness harness. Run on a corpus of 15 well-known GitHub repositories, the instrument reproduces Avelino et al.'s founder-only-detachment statistic within overlapping confidence intervals and shows the diffusion measurement is temporally specific to the pre-departure window rather than a generic feature of active codebases. But the corpus on which this all runs cannot test the causal claim that motivated it, and the reason is structural rather than a matter of needing more data of the same kind.

**Why the causal question is hard to test with this design.** A corpus assembled by starting from repositories that are famous and actively maintained *today* -- the only kind reachable within an unauthenticated 60-request-per-hour GitHub API budget in a short execution window -- necessarily excludes almost all repositories that experienced a founder departure and then genuinely died, because a dead, obscure repository is exactly the kind of project such a candidate list would never include in the first place. This is not an underpowered sample of the right population; it is a sample of the wrong population, one where the outcome variable is conditioned on before the study even begins. A calibration gate applied to this corpus makes the argument concrete rather than rhetorical: the corpus's Truck-Factor-Detachment incidence rate is 73.3% (11 of 15 repositories) against Avelino et al.'s published 16.3% (315 of 1,932) -- a difference so large it is not plausibly sampling noise (two-proportion z = 5.98, exact binomial p = 1.5e-6) [ARTIFACT:art_yOHrviKrh_11] -- and the 18-month post-detachment survival rate among the five founder-only TFDDs this corpus contains is 100%, against Avelino et al.'s published 40.6% (z = 2.70, p = 0.011). Both deviations point the same direction a "famous tools that still exist" sampling frame predicts: it over-represents projects that survived whatever they went through, and it can never, no matter how many more repositories are added from the same frame, produce the non-surviving founder-only-TFDD event this paper's headline hypothesis needs to test against. Enlarging this corpus would sharpen the wrong estimate faster, not fix it.

**Why we still report a positive result, and what it is a result about.** Separately from the causal question, we can and do test whether the new diffusion measurement behaves as its own construct requires: that the pre-departure rise in non-founder authority is specific to the months immediately preceding detachment, not a property any randomly chosen window of a project's history would show. A permutation test with a fully disclosed sampling scheme -- continuous-offset, with-replacement window relocation, exactly the 741 combinatorially distinct monthly start positions available across the five founder-only-TFDD repositories, re-run at budgets of 20, 100, and 300 draws per repository to confirm the null distribution's mean and standard deviation have stabilized -- supports temporal specificity. We are explicit that this establishes construct validity for the *measurement instrument* only. It says nothing about whether diffusion predicts survival, because that comparison requires outcome variance this corpus's five founder-only events -- all survivors -- do not have.

**What this paper is, concretely.** A validated reimplementation of a published pipeline; a new, disclosed, and stress-tested measurement added to it; an automated calibration gate that catches its own corpus's structural defect rather than reporting through it; and a precise specification, grounded in a concrete alternative data pipeline we scoped but did not have time to execute at scale, of what a corpus would need to look like before the causal question can be tested at all. We think this is the right way to report a study whose central instrument works and whose central hypothesis remains open, and we say so explicitly rather than let a permutation p-value do work it cannot do.

[FIGURE:fig1]

**Summary of Contributions**

- A validated, open reimplementation of Avelino et al.'s DOA / Truck-Factor / TFDD pipeline (Section 3), calibrated against their published statistics with explicit numeric confidence intervals on both sides of the comparison (Section 5).
- A new, fully disclosed pre-departure authority-diffusion measurement -- founder commit-share and distinct non-founder DOA-owner count in the six to twelve months before a founder-only TFDD -- together with an exact accounting of its permutation-test sampling scheme, its combinatorial window space, and a multi-budget convergence check (Section 3, Section 5).
- A quantified demonstration that a convenience corpus built from currently-famous, still-maintained repositories is a structurally inconsistent estimator of TFDD incidence and survival rate, not merely an imprecise one -- with the specific statistics that show it (Section 5) and a scoped, concrete alternative data pipeline (historical-snapshot repository selection via GH Archive or Libraries.io, paired with unauthenticated `git clone`) that would remove the conditioning (Section 6).
- A transparent robustness and disclosure protocol -- founder-identification-heuristic sensitivity, a hand-traced DOA sanity check, a live-contributor-API alias-resolution spot check, and a complete 15-repository results table -- that shows exactly what holds up, what remains unresolved, and what a follow-up corpus needs to contain before the founder-diffusion-predicts-survival hypothesis can be tested (Section 5).

# Related Work

**Truck Factor and Degree of Authorship.** The Truck Factor -- the minimal number of developers whose combined departure would incapacitate a project -- was formalized computationally by Avelino et al., who estimate it via a greedy algorithm over per-file Degree-of-Authorship (DOA) scores rather than raw commit counts [2]. DOA itself originates with Fritz et al., who model developer expertise on a file as a function of file creation, subsequent edits relative to other contributors, and, in the interactive variant, IDE interaction events [7]; Avelino et al. use the authorship-only variant, weighting first-authorship, subsequent-edit count, and edits by others with empirically fit coefficients. Ferreira et al. compare three Truck-Factor estimation algorithms, including Avelino et al.'s DOA-based approach, and find it the most defensible of the three on a manually labeled sample [3]. This paper reuses the DOA/Truck-Factor computation from [1, 2] verbatim -- same weights, same greedy set construction -- rather than proposing a new expertise metric, so any new result is attributable to the new pre-departure measurement rather than to a re-tuned authorship model.

**Abandonment and survival.** Avelino et al.'s study is this paper's direct empirical basis [1]. Mining 1,932 popular GitHub repositories, they define TFDD -- the point at which every developer in a project's Truck-Factor set has been silent for the validated one-year threshold -- and score survival 18 months after each TFDD on a four-level Active/Inactive scale. They report that 315 projects (16%) experience a TFDD, that 66% of TFDDs occur at Truck Factor 1, that 128 of 315 (41%) survive, and that surviving and non-surviving projects are statistically indistinguishable in size at the TFDD snapshot (Cohen's d = 0.13-0.26). Their pipeline is never run before the TFDD; this paper's sole methodological departure is to run the identical DOA/Truck-Factor machinery one window earlier, and to treat the resulting trend, rather than the snapshot, as the candidate signal.

**Why projects fail, self-reported.** Coelho and Valente survey maintainers of 104 curated failed GitHub projects (out of 618 identified failures among the top 5,000 starred repositories) and report nine failure reasons spanning team, project, and environment factors [4]. They also find failed projects adopt fewer maintenance-practice signals than surviving ones -- contributing guidelines (16% vs. 72%) and continuous integration (27% vs. 68%) -- plausible downstream correlates of the diffusion process this paper measures directly, though their unit of analysis is a single maintainer's retrospective account of why they personally stopped, not a multi-contributor measurement of whether authority already existed elsewhere before departure.

**Dependency abandonment from the consumer's side.** Miller et al. study how developers who depend on open-source packages detect and cope with a dependency going unmaintained [5]. Their focus is downstream -- how consumers navigate an abandonment they did not cause -- complementary to, and non-overlapping with, this paper's producer-side question of whether a project's own pre-departure authority structure predicts whether such navigation becomes necessary.

**Diffusion of write access and core-team loss.** Two recent studies bear directly on the mechanism this paper investigates. Medappa et al. analyze a matched sample of 5,762 GitHub projects and find that a higher proportion of contributors holding write access -- a static, project-level analogue of the diffusion measured here dynamically and specifically before a founder's departure -- increases novelty but *reduces* survival, attributing the effect to a division of labor in which contributors without write access, not the diffusely empowered core, drive long-term reliability [9]. This is a genuine complication for the mechanism this paper proposes: it shows diffusion of formal authority is not uniformly protective when measured as a static ratio, so the diffusion-precedes-departure framing tested here needs to hold up against a literature where the same underlying variable, measured differently, points the other way. Separately, Nourry et al. re-examine the TFDD construct at a larger scale (over 36,000 projects) and report that only 27% of abandoned projects attract a new Truck-Factor developer afterward, arguing that core-developer loss is more routine and less often reversed than the original framing suggests [10] -- a caution that independently supports this paper's own sampling-frame argument (Section 5, Section 6), since a corpus of currently-thriving repositories will systematically miss exactly the non-recoveries Nourry et al. show are the modal outcome. Jabrayilzade et al. survey 269 practicing engineers on how bus factor is understood in industry and find that informal judgments of who is "hard to replace" often diverge from commit-based Truck-Factor estimates and are shaped by code-review and meeting participation that git history alone does not capture [11] -- a reminder that DOA-based founder and authority-owner identification, like Avelino et al.'s, is a proxy grounded in version-control activity, not a direct measurement of organizational knowledge.

**Contributor-diversity metrics and onboarding.** The Community Health Analytics Open Source Software project (CHAOSS) defines a closely related metric, Contributor Absence Factor -- formerly Bus Factor -- as the count of top contributors needed to reach half of a project's total contributions, and its own documentation notes the metric "can be measured both ways," as a single snapshot or longitudinally at regular intervals [12]. CHAOSS names the longitudinal option but does not formalize a pre-departure trend or validate one against an outcome; its sibling Elephant Factor (organizational diversity, minimum companies for half of commits) is explicitly documented as snapshot-only, with CHAOSS itself warning that computing it over a project's lifetime "may misrepresent the current level of organizational diversity" [ARTIFACT:art_ZAquYQUNc_3n]. The diffusion measurement in this paper is best read as operationalizing and stress-testing the longitudinal variant CHAOSS gestures at but leaves undefined, rather than as an unprecedented construct. The Apache Software Foundation Incubator's graduation guide takes a different, coarser approach: a project is judged "diverse" when it has at least three legally independent committers and no single company essential to its survival -- a binary, committee-judged gate applied once, at graduation, rather than a continuous, retrospectively computed statistic [ARTIFACT:art_ZAquYQUNc_3n]. On the newcomer side, Jergensen, Sarma, and Wagstrom's "onion" model describes contributors migrating from peripheral participation toward the project core as skill and reputation accrue [13], and Steinmacher et al.'s systematic review of 20 studies (from 291 screened) organizes the barriers that participation faces into five categories, with prior technical skill, community responsiveness, and finding an entry point most evidenced [14]. Both study the inward, periphery-to-core trajectory; this paper studies the mirror-image outward trajectory of a founder's own authority dispersing before departure -- a genuinely complementary rather than overlapping direction.

**Mining-methodology controls.** Because this study, like [1], mines GitHub commit history to infer developer identity and project lifecycle, it inherits the hazards Kalliamvakou et al. document under "the perils of mining GitHub" [6] -- most relevantly, bulk-imported repository histories whose first commit touches an implausibly large fraction of files in an implausibly short window, which would masquerade as a single founder's massive first contribution. This paper applies the same greater-than-80%-of-files-in-the-first-week heuristic from [6] that Avelino et al. use to filter such artifacts before founder identification.

**Succession outside software.** The organizational-succession literature on founder-led firms outside software motivates, without formally testing in the same domain, the mechanism this paper investigates. Ahn's study of 64 matched pairs of surviving and delisted Korean founder-led firms finds that founder-succession characteristics -- including how authority was transferred -- are associated with long-term post-succession survival independent of firm size at the time of transition [8], structurally paralleling the diffused-versus-concentrated-authority distinction operationalized here for open-source commit and file-ownership authority. No existing work, to our knowledge, tests this pre-departure-trajectory hypothesis on open-source Truck-Factor data; that gap, and Avelino et al.'s own explicit snapshot-covariate null result, is what motivates the instrument this paper builds -- even though building and calibrating that instrument turned out to be a full paper's worth of work on its own, distinct from testing the hypothesis it was built for.

# Method

The pipeline reimplements Avelino et al.'s Degree-of-Authorship / Truck-Factor / TFDD machinery [1, 2] end to end, then extends it with a pre-departure authority-diffusion measurement, four downstream statistical tests, and a two-stage calibration-and-robustness harness. All components run over the same per-repository commit history and emit both the original at-detachment snapshot covariates and the new diffusion covariates side by side, so the two are compared under identical data and identical statistical procedures [ARTIFACT:art_I5KoOp16hub5].

**Alias resolution.** Each repository's commit authors are collapsed to individuals via normalized email and GitHub-login matching, following the alias-resolution step Avelino et al. describe; a per-repository alias-collapse-rate diagnostic is logged for later quality assurance and later cross-checked against live contributor data (Section 5).

**Degree of Authorship.** For each file and author, cumulative-window DOA is computed year by year using the Fritz et al. weights as reused by Avelino et al.: first-authorship weight FA = 3.293, per-subsequent-edit weight DL = 1.098, and per-edit-by-another-author weight AC = -1.017 [7, 1]. A developer is a file's primary owner in a given year when their DOA on that file is the highest among all contributors to it.

**Truck Factor and TFDD detection.** The yearly Truck-Factor set is the greedy minimal set of primary-DOA-owning developers whose combined removal would leave more than half of a project's files without a primary owner. A TFDD event is recorded the first time every developer in a project's current Truck-Factor set has made no commits for twelve consecutive months -- the abandoner threshold Avelino et al. select empirically as the least error-sensitive of five candidates they test (harmonic-mean precision 0.66, versus 0.44-0.64 for the alternatives) [1]. Founder-only TFDDs are isolated as the subset where the departing Truck-Factor set has size one and its sole member is the repository's first human committer; first commits that touch more than 80% of a repository's files within the first week are treated as bulk imports rather than genuine founding activity and excluded, following the mining-hazard heuristic in [6].

**New measurement: pre-departure authority diffusion.** For each founder-only TFDD, the pipeline additionally computes, over the six to twelve months immediately preceding the detachment, (a) the founder's share of authored commits in that window and (b) the count of distinct non-founder accounts that had already reached primary DOA ownership on at least one file in that window; a composite diffusion score combines both. This trajectory measurement -- distinct from Avelino et al.'s at-TFDD snapshot covariates (developers, commits, and files at the moment of detachment, which the pipeline also computes for direct comparison) -- is the paper's sole new construct and is not present anywhere in [1] or [2].

**Survival outcome.** Post-TFDD survival is scored over an 18-month window using Avelino et al.'s four-level Active/Inactive grading (thriving / maintained / dormant / dead), collapsed to a binary survived flag for the matched-pairs and regression analyses, exactly as in [1].

**Statistical tests.** Four analyses run on the founder-only-TFDD subset, with baseline (snapshot-only) and proposed (diffusion-augmented) predictors computed side by side: (1) a nearest-neighbor matched-pairs bootstrap comparing high- versus low-diffusion projects, matched on standardized log-stars, log-forks, and log-contributor-count within language, with 10,000-resample 95% confidence intervals on the survival-rate lift; (2) Benjamini-Hochberg-corrected logistic and ordinal regressions of survival on the diffusion predictors plus the original snapshot covariates, so standardized effect sizes are directly comparable to Avelino et al.'s reported d = 0.13 (files) and d = 0.25-0.26 (developers, commits); (3) a placebo/window-relocation check that redraws the pre-departure window from elsewhere in each project's history and compares the resulting diffusion-score null distribution against the true window's effect; and (4) a snapshot-null Cohen's-d replication of Avelino et al.'s own negative result, as a sanity check that the reimplementation reproduces their reported effect-size range before any new result built on the same pipeline is trusted.

The window-relocation check draws a continuous start offset, uniformly at random with replacement, from the span of a project's history outside the true pre-departure window -- an approximation to, not an exhaustive enumeration of, the discrete grid of feasible monthly start positions; each repository draws from an independent random seed, so no repository's draws are linked to another's. The exact combinatorial size of that discrete grid -- one feasible monthly start position per month of usable history outside the six-month window width -- is computed and reported per repository (Section 5), together with the shipped code's true per-repository draw cap and a multi-budget convergence table, so that the achievable p-value resolution of this test is stated rather than left implicit.

**Calibration and robustness harness.** Because the pipeline is a reimplementation rather than a reuse of Avelino et al.'s original code or data, a two-stage evaluation runs before any diffusion result is interpreted [ARTIFACT:art_JvYoV94jgkuB]. Stage A recomputes Avelino et al.'s three headline aggregate statistics -- TFDD incidence rate, share of TFDDs at Truck Factor 1, and overall 18-month survival rate -- with 95% Wilson confidence intervals computed for *both* this study's corpus and, where the published paper does not report one, for Avelino et al.'s own statistic from their published numerator and denominator, plus a PASS / FLAG_DEVIATION status per statistic that automatically triggers a diagnostic (sampling-strata composition, abandoner-threshold parameter check, a hand-traced DOA sanity check, and an alias-collapse-rate spot check) whenever any statistic is flagged. Stage B runs founder-identification-heuristic sensitivity (first-commit author versus first-calendar-year plurality versus highest-lifetime-DOA), a matched-pairs bucket-definition sensitivity check, an age-at-TFDD confound check with variance-inflation-factor diagnostics, and the window-relocation permutation test above, reported at the disclosed sampling scheme and budget levels. A follow-up rigor pass re-derives every one of these checks a second time directly against the shipped source code -- rather than against the first pass's own summary of it -- specifically to catch and correct any place where the first pass's description of its own procedure had drifted from what the code actually does [ARTIFACT:art_yOHrviKrh_11]; several of the numbers reported in Section 5 come from that second, source-verified pass rather than the first.

# Experimental Setup

**Corpus.** The corpus consists of 15 well-known, actively maintained GitHub repositories, all but one written in Python (the exception, pyenv/pyenv, in Shell), with star counts from 4,755 to 57,099 and commit histories from 6.6 to 16.7 years [ARTIFACT:art_ZuMis522AEPF]. Table 1 lists all 15 by name.

\begin{table}[t]
\centering
\small
\caption{The full 15-repository corpus. TFDD/TF1 records whether a Truck-Factor-Detachment-Departure was detected and, if so, whether the departing set had size one and consisted solely of the founder. Status: complete = founder-only TFDD with a scored 18-month survival outcome; right-cens. = founder-only TFDD right-censored by insufficient subsequent history; not-founder-only = TFDD detected but the departing set was not solely the founder; none = no TFDD detected.}
\label{tab:corpus}
\begin{tabular}{lrrrcl}
\toprule
Repository & Lang. & Stars & History (yr) & TFDD/TF1 & Status \\
\midrule
Textualize/rich & Python & 57{,}099 & 6.61 & no & none \\
amoffat/sh & Python & 7{,}245 & 14.52 & yes/yes & complete \\
benoitc/gunicorn & Python & 10{,}655 & 16.72 & no & none \\
cookiecutter/cookiecutter & Python & 25{,}059 & 12.71 & yes/no & not-founder-only \\
arrow-py/arrow & Python & 9{,}049 & 13.59 & yes/yes & complete \\
encode/httpx & Python & 15{,}427 & 6.98 & yes/yes & right-cens. \\
Kludex/starlette & Python & 12{,}552 & 8.13 & yes/yes & complete \\
Kludex/uvicorn & Python & 10{,}915 & 9.22 & yes/yes & right-cens. \\
jazzband/tablib & Python & 4{,}755 & 15.34 & yes/yes & complete \\
joke2k/faker & Python & 19{,}370 & 13.72 & no & none \\
kennethreitz/records & Python & 7{,}221 & 11.13 & yes/no & not-founder-only \\
pallets/click & Python & 17{,}629 & 12.32 & yes/yes & complete \\
pyenv/pyenv & Shell & 45{,}036 & 13.96 & yes/no & not-founder-only \\
fastapi/typer & Python & 19{,}911 & 6.63 & no & none \\
tqdm/tqdm & Python & 31{,}276 & 11.21 & yes/no & not-founder-only \\
\bottomrule
\end{tabular}
\end{table}

Full commit history (SHA, author name and email, ISO timestamp, and per-file insertion/deletion counts for every commit) was obtained by cloning each repository and running `git log --numstat`, which is not rate-limited and is therefore complete for every repository in the corpus up to a 5,000-commit-per-repository cap with an explicit truncation flag. Repository-level metadata (stars, forks, language, license, creation and last-push timestamps) came from the GitHub REST API, which in this environment had no authentication token and was consequently capped at 60 unauthenticated requests per hour -- two calls per repository. This constraint, not a defect in the mining code, is what limited the corpus to 15 of the originally planned 150-250 repositories: git cloning itself scales without limit, so the pipeline's candidate list of roughly 104 repositories and its checkpointed, resumable state are already in place to extend the corpus given API credentials, without re-collecting any completed repository.

**A second, historically-oriented corpus was attempted and its yield is itself informative.** A companion dataset built this iteration searched the GitHub Search API for repositories created between 2009 and 2016 that are either archived or have not been pushed to since 2020 -- a selection rule that does not reference present-day popularity -- across ten language ecosystems, discovering 700 unique candidates with no star or fame filter [ARTIFACT:art_apZrIEHXfHos]. Of the first 25 candidates this pipeline had time to attempt cloning and extracting within the run, only 1 (jquery-archive/jquery-metadata, 40 commits, 4.0 years of history) reached the minimum three-year history span this analysis requires; the other 24 were excluded for insufficient history, having gone silent within one to two years of creation -- before ever accumulating enough history to run the DOA/Truck-Factor algorithm or score an 18-month post-departure window. This low yield is itself a finding, not a shortfall to apologize for: it shows that repositories which both persist for multiple years *and* eventually die and get archived are a much smaller intersection than the population of repositories that die almost immediately, and it means the specific gap this paper's central hypothesis needs filled -- a non-surviving founder-only TFDD event with sufficient post-departure history -- was not found in this batch. We report it as a negative result on the discovery side of the pipeline, not as an executed comparison corpus (Section 6).

**Founder-only TFDD sample.** Running the reimplemented pipeline over the full 15-repository corpus's commit histories detects 11 TFDD events of any Truck-Factor size, a 73.3% incidence rate on this corpus [ARTIFACT:art_yOHrviKrh_11]. Of these 11, 7 have a departing Truck-Factor set of size one whose sole member is the repository's first human committer -- 5 with sufficient post-TFDD history to score an 18-month survival outcome (amoffat/sh, arrow-py/arrow, Kludex/starlette, jazzband/tablib, pallets/click), and 2 right-censored by insufficient subsequent history (encode/httpx, Kludex/uvicorn). The remaining 4 TFDDs have a departing Truck-Factor set that is either larger than one or not solely the founder (cookiecutter/cookiecutter, kennethreitz/records, pyenv/pyenv, tqdm/tqdm); the other 4 repositories in the corpus show no detected TFDD in their observed history (Textualize/rich, benoitc/gunicorn, joke2k/faker, fastapi/typer).

**Baselines.** The comparison throughout is not against an external competing method but against Avelino et al.'s own published statistics [1] -- their reported TFDD incidence rate (16.3%, 315/1,932), their reported founder-only (Truck-Factor-1) share of TFDDs (66%, 208/315 by the closest published rounding), their reported overall 18-month survival rate (40.6%, 128/315), and their reported snapshot-covariate effect-size range (Cohen's d = 0.13-0.26) -- computed identically on this paper's corpus, plus the same snapshot covariates recomputed on the founder-only subset as the direct within-study baseline the new diffusion predictors would need to beat if outcome variance existed to test them against.

# Results

## Pipeline calibration against Avelino et al.'s published statistics

Stage A recomputes Avelino et al.'s three headline statistics on the full 15-repository corpus. The founder-only-detachment share reproduces closely: 63.6% of TFDDs have a Truck-Factor-1 departing set (7 of 11, 95% Wilson CI [0.354, 0.848]) against Avelino et al.'s reported 66%, whose own Wilson interval from their published n = 315 and k = 208 (the closest integer numerator consistent with their rounded 66%) is [0.606, 0.710] -- the two intervals overlap [ARTIFACT:art_yOHrviKrh_11]. We report this overlap with an explicit caution rather than as validation: this study's interval, built from only 11 events, spans nearly half the unit interval, so overlap here is weak evidence that fails to *rule out* the reimplementation being correct rather than strong evidence that confirms it. The abandoner-threshold parameter matches Avelino et al.'s validated choice of 12 months exactly.

The other two headline rates are flagged as deviations, and the size of the deviation is now stated with a formal test rather than left as a qualitative aside. The TFDD incidence rate on this corpus is 73.3% (11/15) against Avelino et al.'s 16.3% (315/1,932) -- a 57.0-percentage-point difference (two-proportion z = 5.98, exact binomial p = 1.5e-6) -- and the 18-month survival rate among the 5 founder-only-complete TFDDs is 100% (5/5) against Avelino et al.'s 40.6% (128/315) -- a 59.4-percentage-point difference (z = 2.70, exact binomial p = 0.011) [ARTIFACT:art_yOHrviKrh_11]. Both tests reject, at high confidence, the hypothesis that this corpus and Avelino et al.'s stratified 1,932-repository sample are drawing from the same underlying population, in the direction consistent with severe survivorship bias: a corpus assembled by starting from repositories that are famous and still maintained today has already passed through more TFDDs (they are old, long-lived projects) and has survived essentially all of them (they were selected, in part, by virtue of still existing). The snapshot-null Cohen's-d replication of Avelino et al.'s reported d = 0.13-0.26 could not be computed at all on this corpus, because it requires both survivors and non-survivors and every founder-only TFDD observed survived.

A hand-traced sanity check on five repositories compares each repository's top commit-count author against its top DOA-computed file owner directly; the two disagree in three of five cases (amoffat/sh, cookiecutter/cookiecutter, and arrow-py/arrow), confirming the reimplemented DOA computation captures a genuinely different notion of ownership than raw commit volume, as intended, rather than silently degenerating into a commit-count proxy. The internally reported alias-resolution diagnostic found a median collapse rate of 0.0 across the corpus -- no repository's alias resolver merged any developer identities -- against Avelino et al.'s reported corpus-wide median of 11%. Because a 0.0 collapse rate is also consistent with the resolver under-merging rather than the corpus genuinely having no aliases, we do not take this on trust; the Robustness checks below report a live spot-check against GitHub's own contributor API for three repositories.

[FIGURE:fig2]

## Founder-only pre-departure authority diffusion

The five founder-only TFDD events with sufficient post-departure history to score survival are shown in Table 2, with their pre-departure (6-12 months before detachment) founder commit-share, count of distinct non-founder DOA file-owners, and 18-month survival outcome [ARTIFACT:art_I5KoOp16hub5].

\begin{table}[t]
\centering
\small
\caption{The five founder-only TFDD events with a scored 18-month survival outcome: pre-departure (6--12 months before detachment) founder commit-share, distinct non-founder DOA file-owners, and survival grade. All five survived.}
\label{tab:diffusion}
\begin{tabular}{lrrl}
\toprule
Repository & Founder share & Non-founder owners & Survival (18 mo) \\
\midrule
amoffat/sh & 10.5\% & 8 & maintained \\
arrow-py/arrow & 3.1\% & 4 & thriving \\
Kludex/starlette & 1.1\% & 13 & thriving \\
jazzband/tablib & 2.2\% & 7 & thriving \\
pallets/click & 1.5\% & 18 & thriving \\
\bottomrule
\end{tabular}
\end{table}

All five events show a founder commit-share far below the hypothesis's 50% threshold and well above two independent non-founder DOA-file-owners already established before departure -- consistent with the diffused-authority profile the hypothesis predicts should survive. And all five did survive. That uniform outcome is exactly the sample's central limitation, restated here in the terms the calibration gate above makes precise: with zero non-survivors among the five events, the matched-pairs comparison has no eligible pairs to construct, and both the logistic and ordinal regressions of survival on the diffusion predictors and snapshot covariates fail with an insufficient-sample-size error at n = 5-6, since fitting either model requires at least ten complete rows. Success criterion 1 (a survival-rate lift of at least 1.5x for high- versus low-diffusion projects, with a confidence interval excluding 1x) and criterion 2 (diffusion predictors remaining significant after controlling for age, with an effect size exceeding Avelino et al.'s snapshot d = 0.13-0.26) are therefore not merely negative -- they are unscored, because the statistical objects they require, outcome variance and a fitted regression, do not exist on this corpus.

## Construct validity of the diffusion measurement: what the permutation test can and cannot show

Success criterion 3 -- that the diffusion measurement in the true pre-departure window differs from a null distribution built by relocating that window elsewhere in each project's history -- is the one check in the plan that does not require outcome variance, because it evaluates the measurement's temporal specificity rather than its relationship to survival. We report its exact mechanics rather than only a p-value, because reporting only the p-value from a five-repository test invites the reader to over-generalize it.

The window-relocation procedure draws a continuous start offset with replacement from each repository's usable history outside the true window, which approximates rather than exhaustively enumerates the discrete grid of feasible monthly start positions. That discrete grid has 168, 155, 91, 186, and 141 feasible monthly positions for amoffat/sh, arrow-py/arrow, Kludex/starlette, jazzband/tablib, and pallets/click respectively -- 741 positions summed across the five repositories [ARTIFACT:art_yOHrviKrh_11]. The originally shipped code draws 20 relocated windows per repository (not the 500, 60, or 40 figures an earlier summary of this test reported); four of the five founder-only-complete repositories achieve draws at that budget (amoffat/sh, Kludex/starlette, jazzband/tablib, and pallets/click all reach 20; arrow-py/arrow reaches zero at every budget tested, its usable history outside the window being too short for even one valid draw) -- the theoretical minimum two-sided p-value achievable per repository at 20 draws is 1/21 = 0.048. Re-running the same procedure at budgets of 100 and 300 draws per repository -- reaching a theoretical minimum p-value of 0.0033 at the largest budget, and completing in 114.7 seconds wall-clock for all repositories combined, well inside a practical time budget -- shows the null distribution's founder-share mean and standard deviation stabilizing rather than drifting as the budget grows (mean 0.189 at budget 20, 0.328 at budget 100, 0.369 at budget 300; standard deviation 0.056, 0.112, 0.108 respectively), indicating the earlier 20-draw budget was not so coarse as to make the comparison meaningless [ARTIFACT:art_yOHrviKrh_11].

We are explicit about what this test cannot show. A companion re-derivation of this check against the pipeline's own source code found that computing a placebo p-value *against the true within-window effect using the same regression machinery as the survival analysis* is impossible at any permutation budget, because that regression requires at least ten complete founder-only-TFDD rows and this corpus has five [ARTIFACT:art_yOHrviKrh_11]. The temporal-specificity comparison reported in an earlier pass of this pipeline -- a direct, non-regression comparison of the true window's mean composite diffusion score (2.214) against the pooled null distribution's mean (1.187, standard deviation 0.375) at the shipped 60-draw pooled budget, yielding a two-sided p-value of 0.016 -- is a legitimate but different and weaker statistical object than a regression-based test would be: it establishes that the true window's diffusion score is an outlier relative to relocated windows in the same repositories, which is a necessary property of a construct that claims temporal specificity, but it is not, and was never intended as, evidence that this diffusion score predicts survival. We restate this distinction here because an earlier version of this paper's abstract and conclusion led with the p = 0.016 figure in language that could be read as partial support for the causal claim; it is not. It is evidence the instrument measures something temporally real. It is silent on whether that something predicts what happens to the project afterward.

[FIGURE:fig3]

## Robustness checks

The remaining robustness checks are consistent with a pipeline that is mechanically sound but numerically underpowered for the causal question, rather than one producing unstable or contradictory results. Founder-identification-heuristic sensitivity compared three independent ways of naming the founder -- first-commit author, first-calendar-year commit plurality, and highest lifetime DOA -- and found zero disagreements across all five founder-only-TFDD repositories, against Avelino et al.'s reported median alias-ambiguity rate of 11%, indicating that on this corpus at least, identifying who the founder is is not itself a source of measurement noise, even though the downstream regressions built on that identification cannot yet be fit. Window-boundary sensitivity across near/far/end-offset variants of the 6-12-month window definition, matched-pairs bucket-definition sensitivity, and the age-at-TFDD confound check could not be fit at n = 5-6 in any variant, so their sign-stability is undetermined rather than negative -- the same insufficient-sample-size ceiling that blocks the main regressions blocks these checks too.

A live spot-check against GitHub's own contributor API for three of the fifteen repositories (amoffat/sh, arrow-py/arrow, and Kludex/starlette -- 20% of the corpus) [ARTIFACT:art_yOHrviKrh_11] finds no confirmed case of a bot account being credited as a DOA authority-holder or of two distinct human identities being incorrectly merged, but does find one plausible under-merge (amoffat's contributor list shows both `amoffat` at 366 contributions and a near-identical-login `amoffatgmi` at 6, a pattern consistent with the same person's alternate account, which the pipeline's alias resolver did not merge) and one unresolved risk that a contributor-list-only check cannot rule out: `dependabot[bot]` appears as Kludex/starlette's second-highest contributor by raw commit count, at 159 contributions. Confirming whether dependabot's commits ever reached DOA-owner status on a source file, rather than being confined to lockfiles and CI configuration the DOA algorithm would not weight heavily, requires file-level attribution this contributor-list spot-check does not have; neither issue, if resolved, would flip any of the three checked repositories' founder-only-TFDD classification, and the under-merge would if anything slightly shrink rather than inflate the reported diffusion counts. Eighty percent of the corpus remains unchecked by this external validation, and that fraction is reported here rather than left implicit.

# Discussion

**What this study demonstrates.** A reimplementation of a published, previously validated pipeline reproduces that pipeline's own reported statistics closely enough to trust its mechanics: the founder-only-detachment share (63.6% versus 66% reported, confidence intervals overlapping though weakly informative at this sample size), the validated 12-month abandoner threshold matched exactly, and DOA measurably diverging from raw commit-count intuition in the expected direction on three of five hand-traced repositories. The new pre-departure diffusion measurement this paper adds behaves as its own construct-validity check demands: its value in the true pre-departure window is an outlier relative to a fully disclosed, budget-converged null distribution built from relocating that window elsewhere in each project's history. That combination -- an instrument whose mechanics reproduce a known result and whose new measurement passes its own falsification check -- is a necessary condition for the causal claim this paper set out to test. It is not the causal claim.

**Why the causal claim remains untested, and why that is a design fact rather than a power shortfall.** The corpus was assembled from well-known, currently maintained tools reachable within a strict unauthenticated GitHub API budget; that selection mechanism systematically favors software that is still alive today, which is exactly the population in which a founder-only TFDD is most likely to have been survived. This is a structural property of the sampling frame, not a symptom of too few repositories, and the calibration gate makes the distinction precise rather than rhetorical: a sampling frame that requires a repository to be currently famous and still maintained assigns near-zero probability to ever including the stratum of repositories that experienced a TFDD and then genuinely died and dropped out of public attention. No amount of additional sampling from that same frame converges the resulting incidence-rate or survival-rate estimate toward the true population value, because the stratum the estimate needs to observe is excluded by construction rather than merely under-sampled -- the technical distinction between an inconsistent estimator and an imprecise one. The corpus's own numbers illustrate the mechanism: TFDD incidence (73.3%) and 18-month survival (100%) both deviate from Avelino et al.'s stratified reference rates (16.3% and 40.6%) by amounts too large to attribute to sampling noise (p = 1.5e-6 and p = 0.011 respectively), in exactly the direction this structural argument predicts. The attempted historically-oriented companion corpus (Section 4) independently illustrates the same point from the opposite direction: even when a selection rule is built specifically to avoid conditioning on present-day fame, the repositories it discovers that are old enough to be archived turn out overwhelmingly to have died almost immediately after creation rather than after a long, TFDD-relevant history, so removing the liveness filter alone does not automatically hand a study the events it needs; the fix has to reach further back, to how the candidate list itself was seeded.

**What a valid test would require.** What is needed is a corpus construction that does not condition on present-day liveness at the point candidates are selected, not merely at the point a repository's most recent commit is checked. Avelino et al.'s own stratified top-500-per-language design achieves this by drawing candidates from a fixed, popularity-ranked snapshot and letting the TFDD/survival pipeline discover which of them failed afterward, regardless of whether they are still notable today. A concrete, scoped path to the same property without a GitHub token exists and was identified but not executed at scale in this iteration: build the repository-selection frame from a historical snapshot -- GH Archive's hourly event dumps, its free BigQuery sandbox, or Libraries.io's periodically exported Zenodo dataset -- frozen at a chosen year and ranked by the metadata available as of that year, then obtain each selected repository's full commit and file history via plain unauthenticated `git clone`, which works regardless of a repository's current activity status and is not rate-limited [ARTIFACT:art_ZAquYQUNc_3n]. World of Code holds data of the right shape but is access-gated through a manual registration process, and GHTorrent's infrastructure is confirmed dead, so neither is a viable primary source for a short execution window; the GH Archive or Libraries.io path is the one this paper recommends a follow-up build on. The pipeline already contains the mechanism to execute this once the data source changes -- a checkpointed, resumable collection process, of the same shape as the one used to discover the (largely too-short-lived) historically-oriented companion corpus attempted this iteration -- and an authenticated GitHub API token would additionally raise the metadata-fetch ceiling from 60 to 5,000 requests per hour, sufficient to reach the roughly 40 founder-only TFDD events a well-powered matched-pairs test needs, per the fallback power analysis specified when this study was planned -- about eight times the 5 events available here.

**Limitations.** Beyond the sampling-frame defect above, four further limitations bound how these results should be read. First, the corpus is linguistically narrow (14 of 15 repositories are Python), so nothing here speaks to whether authority-diffusion dynamics generalize across ecosystems with different contribution norms. Second, the DOA hand-trace disagreeing with raw commit-count intuition in three of five spot-checked repositories, while evidence the metric is doing genuine work, also means founder and authority-owner identification is sensitive to exactly which authorship signal is trusted; the founder-identification-heuristic check found perfect agreement across three heuristics on this five-repository sample, but that agreement has not been tested at the corpus scale this paper recommends. Third, the alias-resolution spot-check covers only three of fifteen repositories and, while finding no confirmed bot-inflation, could not rule out one specific risk (a bot account among a repository's top contributors) without file-level attribution outside this check's scope; a full-corpus audit is unexecuted. Fourth, the age-at-TFDD confound check specified in the original evaluation plan -- verifying that any diffusion effect is not simply proxying for project age -- could not run at all for lack of data, so it remains an open, not a closed, threat to validity for a future well-powered test.

# Conclusion

Founder departure is a recognized risk point for open-source projects, and Avelino et al. showed that the obvious predictor -- project size and popularity at the moment of departure -- carries essentially no signal about which projects survive it. This paper built and rigorously calibrated a pipeline capable of testing whether the missing signal instead lives in the trajectory of authority concentration in the months before departure: it reimplements Avelino et al.'s Degree-of-Authorship and Truck-Factor machinery closely enough to reproduce their founder-only-detachment statistic within overlapping confidence intervals, and it adds a new pre-departure diffusion measurement whose exact permutation-test mechanics -- sampling scheme, combinatorial window space, and multi-budget convergence -- are disclosed in full rather than summarized. That measurement passes its own construct-validity check: its value in the true pre-departure window is a statistical outlier relative to a converged null built from relocating that window elsewhere in project history. We are explicit that this result speaks only to whether the instrument measures something temporally real, not to whether that something predicts survival.

What the pipeline could not do, on the corpus assembled under a strict unauthenticated API budget, is test the survival claim itself -- and we now understand why: every founder-only detachment this corpus could observe happened to a project that was, by the corpus's own construction, already known to have survived. This is a property of the sampling frame, demonstrated with a formal two-proportion test against Avelino et al.'s published reference rates, not a property that a larger draw from the same frame would fix. We report this as an honest, structurally explained intermediate result rather than either a confirmation or a refutation of the founder-diffusion-predicts-survival hypothesis, release the full checkpointed, resumable pipeline together with a scoped and partially executed alternative data-collection path, and specify the concrete next step precisely: a historical, liveness-non-conditioned repository-selection frame, built from GH Archive or Libraries.io rather than from a list of currently famous tools, combined with an authenticated GitHub API token to reach the roughly 40 founder-only TFDD events a well-powered matched-pairs test requires -- about eight times what was available here -- is what separates this instrument-validation study from a study that can actually answer the question in its own title.

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

[12] CHAOSS Project. Metric: Contributor Absence Factor. https://www.chaoss.community/kb/metric-contributor-absence-factor/, 2026. Accessed 2026-08-20.

[13] C. Jergensen, A. Sarma, and P. Wagstrom. The onion patch: migration in open source ecosystems. In *Proceedings of the 19th ACM SIGSOFT Symposium and the 13th European Conference on Foundations of Software Engineering (ESEC/FSE)*, pages 70-80, 2011.

[14] I. Steinmacher, M. A. G. Silva, M. A. Gerosa, and D. F. Redmiles. A systematic literature review on the barriers faced by newcomers to open source software projects. *Information and Software Technology*, 59:67-85, 2015.

</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (evidence) Despite the improved framing, the paper's title-level question ('what determines whether a project survives its founder stepping away') is still not addressed by any evidence in the paper — all 5 founder-only TFDD events observed survived, so there is no outcome variance anywhere in the corpus. The paper is honest about this, but honesty about a null result does not substitute for a result; a venue reviewer will still ask whether this is publishable as a full paper versus a workshop/negative-results note.
  Action: Given that both the original 15-repo corpus and the companion historically-sampled corpus (1 usable repo out of ~28 attempted) failed to surface a non-surviving founder-only TFDD, either (a) execute the GitHub-token-enabled expansion described in Discussion before resubmission to obtain at least one non-survivor, or (b) submit this work to a venue/track for negative results, tools, or datasets, where a rigorously validated null/instrumentation contribution is an appropriate fit, and adjust the framing (including the implicit title question) to match that venue's bar rather than a full empirical-contribution track.
- [MAJOR] (methodology) The one quantitative result reported as 'passing' (temporal specificity of the diffusion measurement via the window-relocation permutation test) is drawn from only 5 repositories, and per-repository the achievable p-value resolution at the shipped 20-draw budget is coarse (minimum 0.048); more importantly, the paper reports two different permutation results in different places — a regression-based test that 'is impossible at any budget' at n=5, and a separate 'direct, non-regression comparison' giving p=0.016 at a 60-draw pooled budget — without fully reconciling why the main Results section emphasizes the 20/100/300-draw convergence table (which never reports a headline p-value at all) while the p=0.016 figure appears to come from a different (earlier, 60-draw) run configuration.
  Action: Consolidate the permutation-test reporting into a single canonical run with a single disclosed budget, and either drop the p=0.016 figure entirely (since the paper already says an earlier draft over-emphasized it) or re-derive it under the same 300-draw, source-verified configuration as the convergence table so the reader is not asked to track two different permutation results computed under two different procedures.
- [MINOR] (rigor) The alias-resolution robustness check now covers 3 of 15 repositories (20%) via a live GitHub contributor-API spot-check, an improvement over the prior draft's uncorroborated 0.0 collapse-rate claim, but it still leaves 80% of the corpus unverified, and the one identified issue (dependabot[bot] as Kludex/starlette's second-highest contributor by raw commits) is explicitly left unresolved because file-level DOA attribution for that account was out of scope for this check — yet dependabot activity is exactly the kind of automated-commit pattern that could inflate the 'distinct non-founder DOA-owner' count central to the new measurement.
  Action: Run the file-level DOA check for dependabot[bot] (and any other bot accounts) on at least the founder-only-TFDD subset (5 repositories) rather than leaving it as an open risk — this is a bounded, cheap check (five repos) that would close a real threat to the paper's one positive construct-validity finding.
- [MINOR] (scope) The companion historically-oriented corpus (Section 4) is reported honestly as a low-yield negative result (1 of ~28 candidates usable), but the paper's own artifact metadata shows the discovery sweep found 700 unique candidates while only ~28 were actually attempted for cloning/extraction within the run — a distinction the main text glosses over by implying the 1-of-25/28 yield characterizes the whole discovery approach, when it may just as plausibly reflect the small attempted subsample.
  Action: Clarify in the text that only a small fraction (~28 of 700) of discovered candidates were actually attempted, and either attempt a larger random subsample of the 700 before resubmission to get a more reliable yield estimate, or explicitly caveat that the reported 1/25 yield is itself a small, possibly unrepresentative sample of the 700-candidate pool rather than a characterization of the full pool's true base rate.
- [MINOR] (clarity) The paper states the diffusion-vs-survival regression 'requires at least ten complete rows,' a hard cutoff that appears to originate from an implementation choice (statsmodels convergence heuristics or an explicit guard in the code) rather than a principled statistical requirement, but this threshold is asserted without justification or citation, and a reader cannot tell whether 10 is a conservative rule of thumb the authors chose or a hard numerical/library limitation.
  Action: State explicitly where the n≥10 threshold comes from (e.g., a minimum-events-per-predictor-variable rule of thumb such as EPV≥10 for logistic regression, or a solver convergence floor) and cite the relevant methodological guidance if it is a rule of thumb, so the reader can judge whether the threshold itself is appropriately conservative or could be relaxed for an exploratory analysis.
- [MINOR] (novelty) The paper positions its diffusion measurement as 'operationalizing and stress-testing the longitudinal variant CHAOSS gestures at but leaves undefined' (Contributor Absence Factor computed periodically) — this is a fair and now well-cited framing, but the paper does not check whether any CHAOSS-adjacent open-source tooling (e.g., the CHAOSS Augur/GrimoireLab metric implementations) has already computed Contributor Absence Factor longitudinally on real projects in practice, which would bear directly on how novel the 'longitudinal' framing actually is in applied (non-academic) terms.
  Action: Check whether CHAOSS's reference implementations (Augur, GrimoireLab/Perceval) already compute Absence Factor time series for any tracked projects, and if so, note explicitly how this paper's pre-departure-windowed, DOA-based diffusion score differs methodologically (e.g., DOA-based file ownership vs. raw contribution-count top-N) from what those tools already produce.
</reviewer_feedback>



<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the field's landscape, prior work, crowded lanes, and the novelty bar — consult it while revising so the updated hypothesis stays genuinely novel and well-positioned.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
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

### [3] HUMAN-USER prompt · 2026-08-20 21:10:51 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [4] TOOL CALL — Write · 2026-08-20 21:11:22 UTC

```
File: /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json

{
  "title": "Measuring Pre-Departure Authority Diffusion in OSS",
  "hypothesis": "A calibrated reimplementation of Avelino et al.'s (ESEM 2019) DOA/Truck-Factor/TFDD pipeline, extended with a NEW pre-departure authority-diffusion measurement (founder commit-share and count of distinct non-founder DOA file-owners in the 6-12 months before a founder-only Truck-Factor Detachment), can (a) reproduce Avelino et al.'s published headline statistics closely enough to trust the reimplementation, and (b) show this new diffusion measurement is temporally specific to the pre-departure window rather than a generic property of active projects, measured via a SINGLE canonical, source-verified permutation scheme reported once (not two divergent configurations). On a 15-repository convenience corpus built by starting from currently-famous, still-maintained tools, the calibration gate demonstrates this corpus is NOT a valid sampling frame for testing the causal diffusion-predicts-survival claim: TFDD incidence (73.3% vs Avelino et al.'s 16.3%, z=5.98, p=1.5e-6) and 18-month survival (100% vs their 40.6%, z=2.70, p=0.011) both deviate sharply in the direction of severe survivorship bias, because starting from tools known today to still exist necessarily conditions on the outcome being predicted. A second, liveness-non-conditioned discovery attempt (GH Archive-style search over archived/stale repos, 700 candidates found but only ~28 actually attempted for extraction, yielding 1 usable repo) independently corroborates the mechanism but is explicitly reported as a small, possibly unrepresentative attempted-subsample, not a characterization of the full 700-candidate pool's true base rate -- resolving that gap (via a larger random subsample of the 700, or an explicit caveat) is now a required part of the corpus-construction claim rather than an incidental detail. This is a sampling-frame defect, not merely a power shortfall -- a larger sample drawn from the same 'currently-famous tools' frame would remain biased toward survivors and unable to test the causal claim. The original causal hypothesis (that founder-only-TFDD projects with diffused pre-departure authority survive at a higher rate than matched projects with concentrated authority) THEREFORE REMAINS OPEN, with zero outcome variance across all founder-only TFDD events observed to date (5 of 5 survived), and is reframed as the target of a specific, well-defined follow-up: a corpus constructed from a historical snapshot of GitHub repositories that does NOT condition on present-day liveness, extended via the already-built, checkpointed candidate pipeline and an authenticated GitHub token, yielding an estimated ~40 founder-only TFDD events -- the threshold this study's own fallback power analysis identifies as needed (an n>=10-complete-rows requirement whose statistical basis, e.g. an events-per-variable rule of thumb, must be explicitly cited rather than asserted as an unexplained cutoff). Given that this causal claim remains untested after two independent corpus-construction attempts, this paper's own framing must now explicitly address whether it is submitted as a full empirical-contribution paper (contingent on executing the token-enabled expansion to obtain at least one non-survivor before resubmission) or repositioned for a negative-results/tools-and-datasets track where a rigorously validated null/instrumentation contribution, honestly reported as such including in its title-level framing, is the appropriate bar. Until either the causal test is run or the venue framing is adjusted, this paper's contribution is the validated measurement instrument and calibration/robustness harness (pipeline replication, diagnostic gate, single canonical construct-validity check for the diffusion measurement with bot-account contamination explicitly ruled out on the founder-only-TFDD subset, and explicit positioning against CHAOSS's own reference-implementation tooling for longitudinal Contributor Absence Factor) plus a precise specification of what a valid test of the causal claim requires -- not an empirical answer to whether diffusion predicts survival.",
  "relation_type": "evolution",
  "relation_rationale": "Same frame; hardened reporting rigor (single permutation config, bot-check, subsample caveat) and forced explicit venue/framing decision.",
  "confidence_delta": "decreased",
  "key_changes": [
    "Required consolidation of the two divergent permutation-test results (regression-impossible-at-n=5 vs p=0.016 direct comparison) into one canonical, source-verified configuration per reviewer MAJOR#2",
    "Added explicit requirement to run the dependabot[bot]/bot-account file-level DOA check on the 5 founder-only-TFDD repos to close the construct-validity threat per reviewer MINOR (rigor)",
    "Added requirement to clarify or fix the 28-of-700 attempted-subsample issue in the companion historically-oriented corpus per reviewer MINOR (scope)",
    "Added requirement to explicitly justify/cite the n>=10 regression threshold rather than assert it unexplained per reviewer MINOR (clarity)",
    "Added requirement to check CHAOSS reference implementations (Augur/GrimoireLab) for existing longitudinal Contributor Absence Factor computation before claiming novelty per reviewer MINOR (novelty)",
    "Elevated reviewer MAJOR#1 into the hypothesis itself: paper must now explicitly choose between executing the token-enabled expansion for a non-survivor or repositioning for a negative-results/tools venue",
    "Confidence decreased further: zero outcome variance persists after a second independent corpus-construction attempt, and the sampling problem is confirmed structural across two distinct discovery strategies"
  ],
  "artifact_relations": [
    {
      "from_id": "art_yOHrviKrh_11",
      "to_id": "art_ZAquYQUNc_3n",
      "relation_type": "motivation",
      "relation_rationale": "eval's survivorship-bias finding motivated the search for a non-conditioned data source in the research artifact"
    },
    {
      "from_id": "art_ZuMis522AEPF",
      "to_id": "art_yOHrviKrh_11",
      "relation_type": "uses",
      "relation_rationale": "eval re-analyzes the iter-1 dataset's 15-repo commit corpus directly"
    },
    {
      "from_id": "art_I5KoOp16hub5",
      "to_id": "art_yOHrviKrh_11",
      "relation_type": "extends",
      "relation_rationale": "eval re-derives and closes rigor gaps in the prior experiment's permutation/CI/survivorship reporting"
    },
    {
      "from_id": "art_ZuMis522AEPF",
      "to_id": "art_apZrIEHXfHos",
      "relation_type": "extends",
      "relation_rationale": "new dataset builds a companion, non-conditioned corpus using the same extraction schema as iter-1's dataset"
    }
  ]
}
```

### [5] TOOL RESULT — Write · 2026-08-20 21:11:22 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Measuring Pre-Departure Authority Diffusion in OSS\",\n  \"hypothesis\": \"A calibrated reimplementation of Avelino et al.'s (ESEM 2019) DOA/Truck-Factor/TFDD pipeline, extended with a NEW pre-departure authority-diffusion measurement (founder commit-share and count of distinct non-founder DOA file-owners in the 6-12 months before a founder-only Truck-Factor Detachment), can (a) reproduce Avelino et al.'s published headline statistics closely enough to trust the reimplementation, and (b) show this new diffusion measurement is temporally specific to the pre-departure window rather than a generic property of active projects, measured via a SINGLE canonical, source-verified permutation scheme reported once (not two divergent configurations). On a 15-repository convenience corpus built by starting from currently-famous, still-maintained tools, the calibration gate demonstrates this corpus is NOT a valid sampling frame for testing the causal diffusion-predicts-survival claim: TFDD incidence (73.3% vs Avelino et al.'s 16.3%, z=5.98, p=1.5e-6) and 18-month survival (100% vs their 40.6%, z=2.70, p=0.011) both deviate sharply in the direction of severe survivorship bias, because starting from tools known today to still exist necessarily conditions on the outcome being predicted. A second, liveness-non-conditioned discovery attempt (GH Archive-style search over archived/stale repos, 700 candidates found but only ~28 actually attempted for extraction, yielding 1 usable repo) independently corroborates the mechanism but is explicitly reported as a small, possibly unrepresentative attempted-subsample, not a characterization of the full 700-candidate pool's true base rate -- resolving that gap (via a larger random subsample of the 700, or an explicit caveat) is now a required part of the corpus-construction claim rather than an incidental detail. This is a sampling-frame defect, not merely a power shortfall -- a larger sample drawn from the same 'currently-famous tools' frame would remain biased toward survivors and unable to test the causal claim. The original causal hypothesis (that founder-only-TFDD projects with diffused pre-departure authority survive at a higher rate than matched projects with concentrated authority) THEREFORE REMAINS OPEN, with zero outcome variance across all founder-only TFDD events observed to date (5 of 5 survived), and is reframed as the target of a specific, well-defined follow-up: a corpus constructed from a historical snapshot of GitHub repositories that does NOT condition on present-day liveness, extended via the already-built, checkpointed candidate pipeline and an authenticated GitHub token, yielding an estimated ~40 founder-only TFDD events -- the threshold this study's own fallback power analysis identifies as needed (an n>=10-complete-rows requirement whose statistical basis, e.g. an events-per-variable rule of thumb, must be explicitly cited rather than asserted as an unexplained cutoff). Given that this causal claim remains untested after two independent corpus-construction attempts, this paper's own framing must now explicitly address whether it is submitted as a full empirical-contribution paper (contingent on executing the token-enabled expansion to obtain at least one non-survivor before resubmission) or repositioned for a negative-results/tools-and-datasets track where a rigorously validated null/instrumentation contribution, honestly reported as such including in its title-level framing, is the appropriate bar. Until either the causal test is run or the venue framing is adjusted, this paper's contribution is the validated measurement instrument and calibration/robustness harness (pipeline replication, diagnostic gate, single canonical construct-validity check for the diffusion measurement with bot-account contamination explicitly ruled out on the founder-only-TFDD subset, and explicit positioning against CHAOSS's own reference-implementation tooling for longitudinal Contributor Absence Factor) plus a precise specification of what a valid test of the causal claim requires -- not an empirical answer to whether diffusion predicts survival.\",\n  \"relation_type\": \"evolution\",\n  \"relation_rationale\": \"Same frame; hardened reporting rigor (single permutation config, bot-check, subsample caveat) and forced explicit venue/framing decision.\",\n  \"confidence_delta\": \"decreased\",\n  \"key_changes\": [\n    \"Required consolidation of the two divergent permutation-test results (regression-impossible-at-n=5 vs p=0.016 direct comparison) into one canonical, source-verified configuration per reviewer MAJOR#2\",\n    \"Added explicit requirement to run the dependabot[bot]/bot-account file-level DOA check on the 5 founder-only-TFDD repos to close the construct-validity threat per reviewer MINOR (rigor)\",\n    \"Added requirement to clarify or fix the 28-of-700 attempted-subsample issue in the companion historically-oriented corpus per reviewer MINOR (scope)\",\n    \"Added requirement to explicitly justify/cite the n>=10 regression threshold rather than assert it unexplained per reviewer MINOR (clarity)\",\n    \"Added requirement to check CHAOSS reference implementations (Augur/GrimoireLab) for existing longitudinal Contributor Absence Factor computation before claiming novelty per reviewer MINOR (novelty)\",\n    \"Elevated reviewer MAJOR#1 into the hypothesis itself: paper must now explicitly choose between executing the token-enabled expansion for a non-survivor or repositioning for a negative-results/tools venue\",\n    \"Confidence decreased further: zero outcome variance persists after a second independent corpus-construction attempt, and the sampling problem is confirmed structural across two distinct discovery strategies\"\n  ],\n  \"artifact_relations\": [\n    {\n      \"from_id\": \"art_yOHrviKrh_11\",\n      \"to_id\": \"art_ZAquYQUNc_3n\",\n      \"relation_type\": \"motivation\",\n      \"relation_rationale\": \"eval's survivorship-bias finding motivated the search for a non-conditioned data source in the research artifact\"\n    },\n    {\n      \"from_id\": \"art_ZuMis522AEPF\",\n      \"to_id\": \"art_yOHrviKrh_11\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"eval re-analyzes the iter-1 dataset's 15-repo commit corpus directly\"\n    },\n    {\n      \"from_id\": \"art_I5KoOp16hub5\",\n      \"to_id\": \"art_yOHrviKrh_11\",\n      \"relation_type\": \"extends\",\n      \"relation_rationale\": \"eval re-derives and closes rigor gaps in the prior experiment's permutation/CI/survivorship reporting\"\n    },\n    {\n      \"from_id\": \"art_ZuMis522AEPF\",\n      \"to_id\": \"art_apZrIEHXfHos\",\n      \"relation_type\": \"extends\",\n      \"relation_rationale\": \"new dataset builds a companion, non-conditioned corpus using the same extraction schema as iter-1's dataset\"\n    }\n  ]\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [6] ASSISTANT · 2026-08-20 21:11:26 UTC

```
Revised hypothesis written to `.terminal_claude_agent_struct_out.json`. Key change: kept the core methodology-contribution frame (evolution, not replacement) but hardened it against reviewer critiques — required consolidating the two conflicting permutation results into one canonical run, added a bounded bot-account DOA check, fixed the 28/700 subsample overreach, required justifying the n≥10 threshold, added a CHAOSS-tooling novelty check, and elevated the "publish as full paper vs. negative-results/tools track" decision into the hypothesis itself since two independent corpus-construction attempts have now both failed to surface a non-surviving founder-only TFDD.
```

### [7] SYSTEM-USER prompt · 2026-08-20 21:11:28 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Same frame; hardened reporting rigor (single permutation config, bot-check, subsample caveat) and forced explicit venue/framing decision.' is too long (at most 120 characters, got 137)
Every required field must be present and every field type must match the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [8] TOOL CALL — Edit · 2026-08-20 21:11:32 UTC

```
File: /ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json
OLD:   "relation_rationale": "Same frame; hardened reporting rigor (single permutation config, bot-check, subsample caveat) and forced explicit venue/framing decision.",
NEW:   "relation_rationale": "Same frame; hardened reporting rigor and forced explicit venue/framing decision per reviewer.",
```

### [9] TOOL RESULT — Edit · 2026-08-20 21:11:32 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json", "oldString": "  \"relation_rationale\": \"Same frame; hardened reporting rigor (single permutation config, bot-check, subsample caveat) and forced explicit venue/framing decision.\",", "newString": "  \"relation_rationale\": \"Same frame; hardened reporting rigor and forced explicit venue/framing decision per reviewer.\",", "originalFile": "{\n  \"title\": \"Measuring Pre-Departure Authority Diffusion in OSS\",\n  \"hypothesis\": \"A calibrated reimplementation of Avelino et al.'s (ESEM 2019) DOA/Truck-Factor/TFDD pipeline, extended with a NEW pre-departure authority-diffusion measurement (founder commit-share and count of distinct non-founder DOA file-owners in the 6-12 months before a founder-only Truck-Factor Detachment), can (a) reproduce Avelino et al.'s published headline statistics closely enough to trust the reimplementation, and (b) show this new diffusion measurement is temporally specific to the pre-departure window rather than a generic property of active projects, measured via a SINGLE canonical, source-verified permutation scheme reported once (not two divergent configurations). On a 15-repository convenience corpus built by starting from currently-famous, still-maintained tools, the calibration gate demonstrates this corpus is NOT a valid sampling frame for testing the causal diffusion-predicts-survival claim: TFDD incidence (73.3% vs Avelino et al.'s 16.3%, z=5.98, p=1.5e-6) and 18-month survival (100% vs their 40.6%, z=2.70, p=0.011) both deviate sharply in the direction of severe survivorship bias, because starting from tools known today to still exist necessarily conditions on the outcome being predicted. A second, liveness-non-conditioned discovery attempt (GH Archive-style search over archived/stale repos, 700 candidates found but only ~28 actually attempted for extraction, yielding 1 usable repo) independently corroborates the mechanism but is explicitly reported as a small, possibly unrepresentative attempted-subsample, not a characterization of the full 700-candidate pool's true base rate -- resolving that gap (via a larger random subsample of the 700, or an explicit caveat) is now a required part of the corpus-construction claim rather than an incidental detail. This is a sampling-frame defect, not merely a power shortfall -- a larger sample drawn from the same 'currently-famous tools' frame would remain biased toward survivors and unable to test the causal claim. The original causal hypothesis (that founder-only-TFDD projects with diffused pre-departure authority survive at a higher rate than matched projects with concentrated authority) THEREFORE REMAINS OPEN, with zero outcome variance across all founder-only TFDD events observed to date (5 of 5 survived), and is reframed as the target of a specific, well-defined follow-up: a corpus constructed from a historical snapshot of GitHub repositories that does NOT condition on present-day liveness, extended via the already-built, checkpointed candidate pipeline and an authenticated GitHub token, yielding an estimated ~40 founder-only TFDD events -- the threshold this study's own fallback power analysis identifies as needed (an n>=10-complete-rows requirement whose statistical basis, e.g. an events-per-variable rule of thumb, must be explicitly cited rather than asserted as an unexplained cutoff). Given that this causal claim remains untested after two independent corpus-construction attempts, this paper's own framing must now explicitly address whether it is submitted as a full empirical-contribution paper (contingent on executing the token-enabled expansion to obtain at least one non-survivor before resubmission) or repositioned for a negative-results/tools-and-datasets track where a rigorously validated null/instrumentation contribution, honestly reported as such including in its title-level framing, is the appropriate bar. Until either the causal test is run or the venue framing is adjusted, this paper's contribution is the validated measurement instrument and calibration/robustness harness (pipeline replication, diagnostic gate, single canonical construct-validity check for the diffusion measurement with bot-account contamination explicitly ruled out on the founder-only-TFDD subset, and explicit positioning against CHAOSS's own reference-implementation tooling for longitudinal Contributor Absence Factor) plus a precise specification of what a valid test of the causal claim requires -- not an empirical answer to whether diffusion predicts survival.\",\n  \"relation_type\": \"evolution\",\n  \"relation_rationale\": \"Same frame; hardened reporting rigor (single permutation config, bot-check, subsample caveat) and forced explicit venue/framing decision.\",\n  \"confidence_delta\": \"decreased\",\n  \"key_changes\": [\n    \"Required consolidation of the two divergent permutation-test results (regression-impossible-at-n=5 vs p=0.016 direct comparison) into one canonical, source-verified configuration per reviewer MAJOR#2\",\n    \"Added explicit requirement to run the dependabot[bot]/bot-account file-level DOA check on the 5 founder-only-TFDD repos to close the construct-validity threat per reviewer MINOR (rigor)\",\n    \"Added requirement to clarify or fix the 28-of-700 attempted-subsample issue in the companion historically-oriented corpus per reviewer MINOR (scope)\",\n    \"Added requirement to explicitly justify/cite the n>=10 regression threshold rather than assert it unexplained per reviewer MINOR (clarity)\",\n    \"Added requirement to check CHAOSS reference implementations (Augur/GrimoireLab) for existing longitudinal Contributor Absence Factor computation before claiming novelty per reviewer MINOR (novelty)\",\n    \"Elevated reviewer MAJOR#1 into the hypothesis itself: paper must now explicitly choose between executing the token-enabled expansion for a non-survivor or repositioning for a negative-results/tools venue\",\n    \"Confidence decreased further: zero outcome variance persists after a second independent corpus-construction attempt, and the sampling problem is confirmed structural across two distinct discovery strategies\"\n  ],\n  \"artifact_relations\": [\n    {\n      \"from_id\": \"art_yOHrviKrh_11\",\n      \"to_id\": \"art_ZAquYQUNc_3n\",\n      \"relation_type\": \"motivation\",\n      \"relation_rationale\": \"eval's survivorship-bias finding motivated the search for a non-conditioned data source in the research artifact\"\n    },\n    {\n      \"from_id\": \"art_ZuMis522AEPF\",\n      \"to_id\": \"art_yOHrviKrh_11\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"eval re-analyzes the iter-1 dataset's 15-repo commit corpus directly\"\n    },\n    {\n      \"from_id\": \"art_I5KoOp16hub5\",\n      \"to_id\": \"art_yOHrviKrh_11\",\n      \"relation_type\": \"extends\",\n      \"relation_rationale\": \"eval re-derives and closes rigor gaps in the prior experiment's permutation/CI/survivorship reporting\"\n    },\n    {\n      \"from_id\": \"art_ZuMis522AEPF\",\n      \"to_id\": \"art_apZrIEHXfHos\",\n      \"relation_type\": \"extends\",\n      \"relation_rationale\": \"new dataset builds a companion, non-conditioned corpus using the same extraction schema as iter-1's dataset\"\n    }\n  ]\n}\n", "structuredPatch": [{"oldStart": 2, "oldLines": 7, "newStart": 2, "newLines": 7, "lines": ["   \"title\": \"Measuring Pre-Departure Authority Diffusion in OSS\",", "   \"hypothesis\": \"A calibrated reimplementation of Avelino et al.'s (ESEM 2019) DOA/Truck-Factor/TFDD pipeline, extended with a NEW pre-departure authority-diffusion measurement (founder commit-share and count of distinct non-founder DOA file-owners in the 6-12 months before a founder-only Truck-Factor Detachment), can (a) reproduce Avelino et al.'s published headline statistics closely enough to trust the reimplementation, and (b) show this new diffusion measurement is temporally specific to the pre-departure window rather than a generic property of active projects, measured via a SINGLE canonical, source-verified permutation scheme reported once (not two divergent configurations). On a 15-repository convenience corpus built by starting from currently-famous, still-maintained tools, the calibration gate demonstrates this corpus is NOT a valid sampling frame for testing the causal diffusion-predicts-survival claim: TFDD incidence (73.3% vs Avelino et al.'s 16.3%, z=5.98, p=1.5e-6) and 18-month survival (100% vs their 40.6%, z=2.70, p=0.011) both deviate sharply in the direction of severe survivorship bias, because starting from tools known today to still exist necessarily conditions on the outcome being predicted. A second, liveness-non-conditioned discovery attempt (GH Archive-style search over archived/stale repos, 700 candidates found but only ~28 actually attempted for extraction, yielding 1 usable repo) independently corroborates the mechanism but is explicitly reported as a small, possibly unrepresentative attempted-subsample, not a characterization of the full 700-candidate pool's true base rate -- resolving that gap (via a larger random subsample of the 700, or an explicit caveat) is now a required part of the corpus-construction claim rather than an incidental detail. This is a sampling-frame defect, not merely a power shortfall -- a larger sample drawn from the same 'currently-famous tools' frame would remain biased toward survivors and unable to test the causal claim. The original causal hypothesis (that founder-only-TFDD projects with diffused pre-departure authority survive at a higher rate than matched projects with concentrated authority) THEREFORE REMAINS OPEN, with zero outcome variance across all founder-only TFDD events observed to date (5 of 5 survived), and is reframed as the target of a specific, well-defined follow-up: a corpus constructed from a historical snapshot of GitHub repositories that does NOT condition on present-day liveness, extended via the already-built, checkpointed candidate pipeline and an authenticated GitHub token, yielding an estimated ~40 founder-only TFDD events -- the threshold this study's own fallback power analysis identifies as needed (an n>=10-complete-rows requirement whose statistical basis, e.g. an events-per-variable rule of thumb, must be explicitly cited rather than asserted as an unexplained cutoff). Given that this causal claim remains untested after two independent corpus-construction attempts, this paper's own framing must now explicitly address whether it is submitted as a full empirical-contribution paper (contingent on executing the token-enabled expansion to obtain at least one non-survivor before resubmission) or repositioned for a negative-results/tools-and-datasets track where a rigorously validated null/instrumentation contribution, honestly reported as such including in its title-level framing, is the appropriate bar. Until either the causal test is run or the venue framing is adjusted, this paper's contribution is the validated measurement instrument and calibration/robustness harness (pipeline replication, diagnostic gate, single canonical construct-validity check for the diffusion measurement with bot-account contamination explicitly ruled out on the founder-only-TFDD subset, and explicit positioning against CHAOSS's own reference-implementation tooling for longitudinal Contributor Absence Factor) plus a precise specification of what a valid test of the causal claim requires -- not an empirical answer to whether diffusion predicts survival.\",", "   \"relation_type\": \"evolution\",", "-  \"relation_rationale\": \"Same frame; hardened reporting rigor (single permutation config, bot-check, subsample caveat) and forced explicit venue/framing decision.\",", "+  \"relation_rationale\": \"Same frame; hardened reporting rigor and forced explicit venue/framing decision per reviewer.\",", "   \"confidence_delta\": \"decreased\",", "   \"key_changes\": [", "     \"Required consolidation of the two divergent permutation-test results (regression-impossible-at-n=5 vs p=0.016 direct comparison) into one canonical, source-verified configuration per reviewer MAJOR#2\","]}], "userModified": false, "replaceAll": false}
```

### [10] ASSISTANT · 2026-08-20 21:11:32 UTC

```
Fixed — trimmed to 103 characters.
```
