# upd_hypo — test_idea

> Phase: `invention_loop` · round 2 · `upd_hypo`
> Run: `iter2_13ec49ac7efb` — Authority Diffusion Before Founder Departure: Diagnosing Sample Starvation in OSS Survival Research
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `upd_hypo` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-08-20 21:21:04 UTC

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
  /ai-inventor/aii_data/runs/run_LYICROwXFVjo/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
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
  /ai-inventor/aii_data/runs/run_LYICROwXFVjo/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
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
  /ai-inventor/aii_data/runs/run_LYICROwXFVjo/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1
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
id: art_ajD7unO0iQl3
type: dataset
title: Founder-Departure GitHub Corpus Without Liveness Bias
summary: >-
  This artifact delivers a 67-repository GitHub commit corpus mined via the authenticated GitHub REST API (GH_TOKEN, 5000
  req/hr), sampled purely on historical repository creation/push-date windows (2011-2015, GitHub Search API created:/pushed:
  qualifiers across 8 languages) with NO filter on present-day archived, starred, or maintained status. This deliberately
  avoids the survivorship bias of sampling from 'currently famous' repo lists: of the 450 candidates screened, 383 were rejected
  (mostly too few commits or too-short history) and 67 were accepted, of which 48 (72%) have had no commit in >=2 years as
  of build time (a non-surviving proxy) and 7 are archived by GitHub itself. code/build_dataset.py contains the full mining
  pipeline (search, per-repo /commits and /stats/contributors pulls, founder-detectability screen requiring a single author
  to account for >=60% of a repo's early commits) with a resumable checkpoint at temp/checkpoint/checkpoint.json. Its raw
  output, temp/datasets/full_founder_departure_corpus.json, carries the complete exp_sel_data_out-companion schema per repo
  (repo_metadata, founder_signal, commits[], contributor_stats_weekly, plus explicit sampling_frame='liveness_non_conditioned'
  and frame_construction_method fields) and an honest build_yield_report (candidates attempted/accepted/rejected with reasons,
  and counts of founder-only-TFDD candidates and non-surviving proxies). data.py standardizes this into the required exp_sel_data_out.json
  schema as the single chosen dataset, repo_level_founder_departure_survival: one example per repo, with JSON-encoded input
  features computed strictly BEFORE the founder's own last commit (avoiding outcome leakage) and a 3-way output label (survived
  / non_surviving / unknown_insufficient_post_departure_window, the last used for the 40 repos where the founder is still
  active or departed too recently to judge). Of the 27 repos with a judgeable label, 20 are non_surviving and 7 survived --
  the specific non-liveness-conditioned signal this artifact exists to supply for downstream founder-departure survival analysis.
  full_data_out.json (64KB, well under the 100MB limit) is schema-validated; mini_data_out.json and preview_data_out.json
  are the standard 3-example variants. Known limitations for downstream use: the survival label is a crude staleness proxy
  (no commit in 2 years), not a validated abandonment determination, and should be re-derived from the raw commits[] timeline
  if a stricter definition is needed; the founder-only-TFDD screen is a heuristic on REST /commits author identity (login/email/name),
  not a full DOA/Truck-Factor algorithm run, so downstream code computing TFDD should treat dominant_early_author as a candidate
  founder identity to verify, not a ground truth; and the 27-repo judgeable-label subset is small, so any statistical claims
  drawn from it should report this sample size explicitly rather than treating it as a large-sample result.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_LYICROwXFVjo/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 6 ---
id: art_zgnq2xDjA0ta
type: evaluation
in_dependencies:
- id: art_ZuMis522AEPF
  label: dataset
- id: art_I5KoOp16hub5
  label: experiment
title: Closing the Rigor Gaps in the Diffusion Pipeline
summary: >-
  This evaluation re-analyzes the DATASET (art_ZuMis522AEPF) and EXPERIMENT (art_I5KoOp16hub5) artifacts across five reviewer-named
  rigor gaps. The declared iter_1 dependency workspace paths did not exist in this run's live data tree; the identical dependency
  outputs (verified matching n_repos=15, n_repos_total=3427) were located and used from this run's own prior-round paper-repo
  deployment snapshot instead of being fabricated. eval.py imports the EXPERIMENT's own method.py and genuinely re-executes
  process_repo/run_regressions/placebo_check against the real 15-repo corpus, rather than re-deriving numbers from summary
  text. Part A discloses the placebo/window-shuffle scheme by reading the actual generation code (continuous with-replacement
  draws, distinct per-repo seeds) and uncovers a previously undocumented hardcoded 20-draws-per-repo cap that makes the EXPERIMENT
  summary's cited '500 iterations' never actually binding; a live re-run at budgets 10/60/2000 shows the placebo check is
  blocked at every budget because the true regression effect is unavailable at n=5-6 founder-only-TFDD events, not because
  the effect is robust. Part B computes Wilson 95% CIs for both Avelino et al.'s published 66% TF=1 rate (n=315, quoted live
  from arXiv:1906.08058) and this study's own TF=1 fraction, with an explicit numeric overlap determination and an explicit
  caution against over-reading overlap given this study's tiny denominator (n=11); it also surfaces a genuine reproducibility
  discrepancy (5 vs. the archived 6 founder-only TFDD events on an identical re-run). Part C live-fetches GitHub contributor
  graphs for 3 of the 15 real corpus repos (arrow-py/arrow, Kludex/starlette, pallets/click -- corrected after discovering
  the DATASET summary's example repo names do not match the actual corpus) and cross-references bot accounts against the pipeline's
  own resolved author IDs. Part D emits a full, exact 15-row per-repo table cross-checked against both source JSON files.
  Part E computes this corpus's TFDD incidence and founder-only survival rates and formally tests them against Avelino et
  al.'s published rates via two-proportion z-tests and exact binomial tests, then documents a structural residual-limitation
  argument (with a concrete falsifiable prediction) for why no second, non-conditioned corpus exists to close the survivorship-bias
  comparison fully. All five parts write into eval_out.json (schema-conformant metrics_agg + datasets/examples, each example's
  metadata_full_result carrying the rich per-part detail), validated against the exp_eval_sol_out schema (PASSED). Downstream
  users (GEN_PAPER_TEXT) should present parts A, B, D, and E's quantification half as fully closed with genuine re-computation,
  and part C plus E's second-frame comparison as explicitly, honestly scoped as partial (3-of-15 spot-check) or structurally
  open (no expanded corpus available) rather than resolved.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_LYICROwXFVjo/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
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

id: art_ajD7unO0iQl3
type: dataset
title: Founder-Departure GitHub Corpus Without Liveness Bias
summary: >-
  This artifact delivers a 67-repository GitHub commit corpus mined via the authenticated GitHub REST API (GH_TOKEN, 5000
  req/hr), sampled purely on historical repository creation/push-date windows (2011-2015, GitHub Search API created:/pushed:
  qualifiers across 8 languages) with NO filter on present-day archived, starred, or maintained status. This deliberately
  avoids the survivorship bias of sampling from 'currently famous' repo lists: of the 450 candidates screened, 383 were rejected
  (mostly too few commits or too-short history) and 67 were accepted, of which 48 (72%) have had no commit in >=2 years as
  of build time (a non-surviving proxy) and 7 are archived by GitHub itself. code/build_dataset.py contains the full mining
  pipeline (search, per-repo /commits and /stats/contributors pulls, founder-detectability screen requiring a single author
  to account for >=60% of a repo's early commits) with a resumable checkpoint at temp/checkpoint/checkpoint.json. Its raw
  output, temp/datasets/full_founder_departure_corpus.json, carries the complete exp_sel_data_out-companion schema per repo
  (repo_metadata, founder_signal, commits[], contributor_stats_weekly, plus explicit sampling_frame='liveness_non_conditioned'
  and frame_construction_method fields) and an honest build_yield_report (candidates attempted/accepted/rejected with reasons,
  and counts of founder-only-TFDD candidates and non-surviving proxies). data.py standardizes this into the required exp_sel_data_out.json
  schema as the single chosen dataset, repo_level_founder_departure_survival: one example per repo, with JSON-encoded input
  features computed strictly BEFORE the founder's own last commit (avoiding outcome leakage) and a 3-way output label (survived
  / non_surviving / unknown_insufficient_post_departure_window, the last used for the 40 repos where the founder is still
  active or departed too recently to judge). Of the 27 repos with a judgeable label, 20 are non_surviving and 7 survived --
  the specific non-liveness-conditioned signal this artifact exists to supply for downstream founder-departure survival analysis.
  full_data_out.json (64KB, well under the 100MB limit) is schema-validated; mini_data_out.json and preview_data_out.json
  are the standard 3-example variants. Known limitations for downstream use: the survival label is a crude staleness proxy
  (no commit in 2 years), not a validated abandonment determination, and should be re-derived from the raw commits[] timeline
  if a stricter definition is needed; the founder-only-TFDD screen is a heuristic on REST /commits author identity (login/email/name),
  not a full DOA/Truck-Factor algorithm run, so downstream code computing TFDD should treat dominant_early_author as a candidate
  founder identity to verify, not a ground truth; and the 27-repo judgeable-label subset is small, so any statistical claims
  drawn from it should report this sample size explicitly rather than treating it as a large-sample result.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_LYICROwXFVjo/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

id: art_zgnq2xDjA0ta
type: evaluation
in_dependencies:
- id: art_ZuMis522AEPF
  label: dataset
- id: art_I5KoOp16hub5
  label: experiment
title: Closing the Rigor Gaps in the Diffusion Pipeline
summary: >-
  This evaluation re-analyzes the DATASET (art_ZuMis522AEPF) and EXPERIMENT (art_I5KoOp16hub5) artifacts across five reviewer-named
  rigor gaps. The declared iter_1 dependency workspace paths did not exist in this run's live data tree; the identical dependency
  outputs (verified matching n_repos=15, n_repos_total=3427) were located and used from this run's own prior-round paper-repo
  deployment snapshot instead of being fabricated. eval.py imports the EXPERIMENT's own method.py and genuinely re-executes
  process_repo/run_regressions/placebo_check against the real 15-repo corpus, rather than re-deriving numbers from summary
  text. Part A discloses the placebo/window-shuffle scheme by reading the actual generation code (continuous with-replacement
  draws, distinct per-repo seeds) and uncovers a previously undocumented hardcoded 20-draws-per-repo cap that makes the EXPERIMENT
  summary's cited '500 iterations' never actually binding; a live re-run at budgets 10/60/2000 shows the placebo check is
  blocked at every budget because the true regression effect is unavailable at n=5-6 founder-only-TFDD events, not because
  the effect is robust. Part B computes Wilson 95% CIs for both Avelino et al.'s published 66% TF=1 rate (n=315, quoted live
  from arXiv:1906.08058) and this study's own TF=1 fraction, with an explicit numeric overlap determination and an explicit
  caution against over-reading overlap given this study's tiny denominator (n=11); it also surfaces a genuine reproducibility
  discrepancy (5 vs. the archived 6 founder-only TFDD events on an identical re-run). Part C live-fetches GitHub contributor
  graphs for 3 of the 15 real corpus repos (arrow-py/arrow, Kludex/starlette, pallets/click -- corrected after discovering
  the DATASET summary's example repo names do not match the actual corpus) and cross-references bot accounts against the pipeline's
  own resolved author IDs. Part D emits a full, exact 15-row per-repo table cross-checked against both source JSON files.
  Part E computes this corpus's TFDD incidence and founder-only survival rates and formally tests them against Avelino et
  al.'s published rates via two-proportion z-tests and exact binomial tests, then documents a structural residual-limitation
  argument (with a concrete falsifiable prediction) for why no second, non-conditioned corpus exists to close the survivorship-bias
  comparison fully. All five parts write into eval_out.json (schema-conformant metrics_agg + datasets/examples, each example's
  metadata_full_result carrying the rich per-part detail), validated against the exp_eval_sol_out schema (PASSED). Downstream
  users (GEN_PAPER_TEXT) should present parts A, B, D, and E's quantification half as fully closed with genuine re-computation,
  and part C plus E's second-frame comparison as explicitly, honestly scoped as partial (3-of-15 spot-check) or structurally
  open (no expanded corpus available) rather than resolved.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_LYICROwXFVjo/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

# 1. Introduction

## 1.1 The problem

An open-source project's founder eventually stops committing. Some projects keep going; others go quiet within a year. The literature has metrics for measuring how concentrated a project's ownership is at a single point in time, but not for measuring how that concentration was *changing* in the months before the founder left — whether responsibility had already spread to other contributors, or whether the founder was still the sole owner of every file up to their last commit. We call this pre-departure trend *authority diffusion*, and we test whether it predicts survival beyond the snapshot statistics (team size, commit volume, file count) that existing metrics already capture.

## 1.2 Why it matters

Community-health tooling already tries to answer a version of this question after the fact: CHAOSS's Contributor Absence Factor counts how many top contributors are needed to reach 50% of a project's commits, and its Elephant Factor does the analogous count over organizations, but CHAOSS's own knowledge base documents both as computable only as a snapshot or as repeated snapshots, never as a fitted trajectory leading into a departure [1, 2]. The Apache Software Foundation operationalizes "diversity" for graduation as a binary committee judgment — at least three legally independent committers, no single essential company — rather than a continuous, predictive statistic [4]. A validated pre-departure trajectory signal would let maintainers, funders, and package-registry risk tooling flag an at-risk project *before* the founder's last commit, rather than after the project has already gone quiet long enough to trip a Contributor Absence Factor snapshot.

## 1.3 Why it is hard

Testing this hypothesis needs three things simultaneously: (a) a reliable, automatic detector for the event itself — a founder truly stepping away, not merely going quiet for a sprint — (b) commit-level history reaching back far enough before that event to fit a pre-departure trend, and (c) a sample of repositories that is not itself pre-filtered on the outcome being measured. We show in Section 4 that ordinary GitHub sampling strategies violate (c) by construction: search and trending endpoints surface repositories that are popular and active *today*, which already conditions the sample on having survived long enough to accumulate that popularity. A repository whose founder left and which then died six months later is, almost by definition, one that never accumulated the stars needed to be discovered by a present-day search query.

## 1.4 Why existing approaches fall short

Avelino et al.'s (ESEM 2019) [19] Truck-Factor / Degree-of-Authorship (DOA) pipeline is the closest prior instrument: it detects Truck-Factor-Detachment-Departure (TFDD) events from commit history and reports population-level TFDD incidence and post-TFDD survival rates from a large GitHub sample. It was not designed to fit a *pre-departure* trajectory, and — more importantly for the present study — it was built on exactly the kind of popularity-conditioned frame described above. We reused its DOA/TFDD machinery in full (Section 3) rather than re-deriving it, but applied it to our own sampling frame; the corpus we built for that first pass turned out to inherit the same liveness conditioning, which is the central negative finding of this paper.

## 1.5 What we did and what we found

We built the Avelino-style DOA/TFDD pipeline (Section 3), ran it on a 3,427-repository GitHub corpus, and found that only 6 repositories produced a usable founder-only TFDD event (Section 4.1) — an error breakdown dominated by 3,409 repositories with no minable commit history at all. Every downstream statistical test we had planned (matched-pairs survival comparison, BH-corrected logistic/ordinal regression, window-shuffle placebo check) consequently reported `insufficient_n` rather than a substantive result. Rather than treat this null as evidence about the hypothesis, we ran a dedicated rigor-gap evaluation (Section 4.2) that shows the corpus itself is biased toward survival — its TFDD incidence and founder-only survival rate are both statistically distinguishable from Avelino et al.'s own published population figures — and that the placebo check's apparent robustness across simulation budgets is a structural artifact of an undocumented per-repository draw cap, not evidence that six events are enough. We then built a second corpus (Section 5) that removes the liveness conditioning by sampling on historical creation/push-date windows only, and report its composition as the resource this hypothesis needs to be tested properly. **This paper's contribution is therefore diagnostic and infrastructural, not a confirmed or refuted authority-diffusion effect**: we did not obtain enough founder-only TFDD events in either corpus to run the planned regression, and we report that limitation explicitly rather than a spurious point estimate from n=6.

### Summary of Contributions

- A working reimplementation of Avelino et al.'s DOA/Truck-Factor/TFDD pipeline extended with a pre-departure authority-diffusion covariate, applied at 3,427-repository scale (Section 3).
- A rigor-gap evaluation that formally quantifies the survivorship bias in a popularity-sampled TFDD corpus against Avelino et al.'s own published population statistics, and that exposes an undocumented hard cap that makes the pipeline's placebo check vacuous rather than confirmatory (Section 4).
- A positioning of the pre-departure authority-diffusion construct against the nearest existing OSS community-health metrics and onboarding literature, establishing that none of them measure a pre-departure trend (Section 2).
- A second, 67-repository corpus sampled without any liveness or popularity filter, in which 72% of repositories are non-surviving by a two-year-inactivity proxy, released as the resource needed to run this hypothesis test with an adequately powered, unbiased sample (Section 5).

[FIGURE:fig1]

# 2. Related Work

**Snapshot diversity metrics.** CHAOSS's Contributor Absence Factor (formerly Bus Factor) sorts contributors by contribution volume and counts how many are needed to reach 50% of total contributions; CHAOSS's own documentation states this can be measured as a single snapshot or repeated at intervals, but no CHAOSS metric fits or validates a continuous pre-departure *trend* [1]. The sibling Elephant Factor, the organizational analogue, is explicitly documented as snapshot-only and as misrepresenting project history if computed cumulatively [2]. Neither metric is designed to answer "was authority already diffusing before this specific person left," which is the question this paper's construct targets.

**Governance-gate diversity.** The Apache Incubator's graduation guide requires at least three legally independent committers and no single dominating company as a binary, committee-judged gate for exiting incubation [4]; the Apache Project Maturity Model's retrievable CD-series criteria turned out on inspection to cover code governance (distribution, reproducible builds, provenance) rather than community diversity, and a true diversity-specific code series was not located [5]. Both instruments answer a governance-compliance question at a point in time, not a predictive one.

**Newcomer trajectories.** The onion model of OSS socialization describes contributors migrating *inward*, from peripheral participation (mailing lists, bug reports) toward the code-owning core, as skill and reputation accrue [6], and a systematic review of newcomer barriers organizes the obstacles to that inward migration into five categories, most centrally prior technical skill and community responsiveness [7]. Both study the mirror-image trajectory to the one this paper is interested in: contributors moving *toward* ownership, rather than a founder's ownership moving *away* from them before departure.

**Population-scale TFDD baselines.** Avelino et al. (ESEM 2019) [19] is the direct methodological ancestor of the pipeline used here (Section 3): its DOA weighting and Truck-Factor-Detachment-Departure detection are reused verbatim, and its published population-level TFDD incidence (16.3%) and founder-only-TFDD survival rate (40.6%) are the external baseline this paper's rigor-gap evaluation tests our own corpora against (Section 4.2).

**Data-source landscape.** GH Archive exposes GitHub's public event stream (15+ event types) with no token required, but its `PushEvent` payload carries only commit SHA/author/message pointers — never file lists or diffs [8, 9, 10] — so it can supply a repository-selection frame but not the commit-level content this study needs. World of Code holds full commit/blob/file/author cross-referencing at the right granularity [11, 12] but is gated behind an SSH-registration approval process [13], and its self-serve Zenodo derivative covers only bot commits [14]. GHTorrent, an earlier commit-mining service, is confirmed dead: its domain now redirects to an unrelated site and its BigQuery mirror has been stale since 2019 [15, 16, 17]. Libraries.io's Zenodo dump is live and gives repository-selection metadata at scale but carries no commit-level history [18]. We concluded that a repository-selection frame independent of present-day liveness (built from historical creation/push-date search, Section 5) combined with a direct, unauthenticated `git clone` of each selected repository's full history is the only path that is simultaneously live, token-cheap, and free of the liveness conditioning this paper's Section 4 diagnoses.

# 3. Method: DOA/TFDD Pipeline and the Authority-Diffusion Covariate

We reimplement Avelino et al.'s Degree-of-Authorship (DOA) weighting over per-file commit history to identify, for each repository, the point at which a single "founder" author accounts for the plurality of authorship (a Truck-Factor-Detachment-Departure, TFDD, event: the date the founder's authorship share falls below the threshold that would make their departure survivable without loss of institutional knowledge). A TFDD event is classed *founder-only* when the departing author is the repository's original committer, distinguishing genuine founder succession from a later core contributor's departure.

For every founder-only TFDD event, we compute two families of covariates purely from commits dated **before** the event, to avoid any post-departure leakage:

- **At-TFDD snapshot covariates** (Avelino et al.'s original feature set): number of active developers, total commits, and total files at the moment of TFDD.
- **Pre-departure authority-diffusion covariates** (this paper's addition): the founder's commit-share in the 6-12 month window immediately before TFDD, and the count of distinct non-founder contributors who already held DOA-recognized file ownership in that same window (`n_diffuse_owners_pre`). A single scalar `diffusion_score` combines the two.

The outcome is 18-month post-TFDD survival, labeled from subsequent commit activity (`survived_binary`), with three planned analyses: (1) a nearest-neighbor matched-pairs comparison of high- versus low-diffusion repositories controlling for the snapshot covariates, (2) BH-corrected logistic regression (binary survival) and ordinal regression (a graded survival label) with diffusion score as the covariate of interest, and (3) a window-shuffle placebo check that repeatedly reassigns which pre-TFDD window is treated as "pre-departure" to establish whether the observed diffusion-survival association could arise by chance.

# 4. Results

## 4.1 Sample starvation at 3,427 repositories

Running the pipeline on a 3,427-repository corpus sampled by current GitHub popularity/activity produced only 6 founder-only TFDD events. The error breakdown for the remaining 3,421 repositories was: 3,409 had no minable commit history at all under the mining budget used, 4 had a TFDD event that was not founder-only, and 2 were right-censored (no 18-month post-TFDD window had yet elapsed). At n=6, every planned statistical test failed outright: the matched-pairs comparison found zero eligible pairs even under relaxed matching, and both the logistic and ordinal regressions reported `insufficient_n`.

[FIGURE:fig2]

## 4.2 The null is a sampling artifact, not evidence of no effect

A dedicated rigor-gap evaluation re-examined the 6-event corpus against Avelino et al.'s own published population statistics using Wilson 95% confidence intervals and two-proportion z-tests. Two results indicate the corpus is not a fair sample of the population Avelino et al. characterized:

- **TFDD incidence.** 73.3% of this corpus's repositories (11 of 15 candidates carried through to the full table) exhibit any TFDD event, versus 16.3% in Avelino et al.'s published population — a two-proportion z=5.89, p=3.8e-9.
- **Founder-only-TFDD survival.** 100% (5 of 5) of this corpus's founder-only-TFDD repositories survived 18 months post-departure, versus 40.6% in Avelino et al.'s population (Wilson 95% CI [0.606, 0.710] for their 66% TF=1 baseline versus this corpus's 45.5% TF=1 fraction, CI [0.213, 0.720]) — z=2.67, p=0.0075.

Both deviations point the same direction: a corpus selected for present-day popularity over-represents repositories that already survived whatever ownership transition they went through, which is exactly the confound the pre-departure authority-diffusion hypothesis needs an unbiased corpus to rule out.

[FIGURE:fig3]

Separately, the evaluation audited the placebo check's own implementation and found a previously undocumented **20-draw-per-repository hard cap** — the code path never reaches the "500 iterations" figure the original summary cited, because it caps each repository's contribution to the placebo distribution at 20 draws regardless of the requested budget. Re-running the placebo check at three budgets (10, 60, and 2,000 requested draws) produced an identical qualitative conclusion at all three, which is not evidence of robustness: at the 20-draw hard cap, the theoretical floor on the smallest detectable effect is 4.8%, and at the (never-reached) 500-draw figure the floor would be 0.2% — meaning the check is structurally incapable of resolving an effect at n=6 regardless of how large the requested budget is set. The evaluation additionally spot-checked 3 of the corpus's 15 repositories against their raw source records and found all three aliases consistent (no full-corpus audit was run; 80% of the corpus remains unchecked by this pass).

## 4.3 What we did not test

No expanded or non-liveness-conditioned corpus existed among this round's dependencies to run head-to-head against the population baseline, so the claim that the null in Section 4.1 is a design flaw rather than a genuine power problem rests on the structural argument and evidence in Section 4.2, not on a second frame producing more TFDD events. Section 5 supplies that second frame as this paper's concrete, falsifiable next step: if the pre-departure authority-diffusion hypothesis holds, a non-liveness-conditioned corpus should yield both a TFDD incidence closer to Avelino et al.'s 16.3% population figure and a founder-only survival rate closer to their 40.6%, rather than reproducing this section's 73.3%/100% figures.

# 5. A Liveness-Non-Conditioned Corpus

To remove the conditioning identified in Section 4.2, we built a second 67-repository corpus using GitHub's Search API `created:`/`pushed:` date qualifiers to sample purely on **historical** creation and push-date windows (2011-2015) across eight languages, applying **no filter on present-day archived, starred, or maintained status**. Of 450 candidates screened, 383 (85%) were rejected — mostly for too few commits or too short a history to fit a pre-departure trajectory — leaving 67 accepted repositories. Of those, 48 (72%) have had no commit in at least two years as of build time (our non-surviving proxy) and 7 are archived by GitHub itself, meaning non-surviving projects are represented in this corpus for the first time at a scale the original 3,427-repository frame never produced (Section 4.1: only 2 right-censored, 0 confirmed non-surviving, among 6 founder-only TFDD events).

[FIGURE:fig4]

Each repository's record standardizes to one example carrying only pre-departure-observable input features (computed strictly before the founder's last commit, to avoid the leakage the original pipeline already guards against in Section 3) and one of three survival labels: `survived`, `non_surviving`, or `unknown_insufficient_post_departure_window` for repositories without enough elapsed history to call a label at all. This corpus is released as the direct input to Section 3's pipeline for the next round of this study; running it end to end and reporting the resulting TFDD incidence and founder-only survival rate against Avelino et al.'s population baseline is the falsifiable prediction stated in Section 4.3.

# 6. Discussion

**The headline finding of this paper is methodological.** A popularity-sampled GitHub corpus produced too few founder-only TFDD events to test the pre-departure authority-diffusion hypothesis (n=6), and the rigor-gap evaluation in Section 4.2 shows this was not bad luck: the corpus's TFDD incidence and founder-only survival rate both differ from Avelino et al.'s population figures in the direction consistent with survivorship conditioning, and the placebo check that appeared to certify the pipeline's null result was, on inspection, structurally incapable of detecting an effect at any of the budgets it was run at. We consider this worth reporting on its own terms rather than smoothing over: an automated pipeline that runs to completion and reports a stable null across three simulation budgets looks, from the outside, like a well-powered negative result. Section 4.2 shows it is not, and the distinction matters for anyone building on TFDD-style pipelines with any GitHub sample drawn by present-day popularity, stars, or trending status.

**Limitations.** The spot-check audit of the original corpus's alias resolution covered only 3 of 15 repositories (80% unchecked). The new liveness-non-conditioned corpus (Section 5) has not yet been run through the DOA/TFDD pipeline of Section 3, so we cannot yet report whether it in fact yields more founder-only TFDD events or a less skewed incidence/survival rate than the original frame — that comparison is the explicit next step, not a result claimed here. The non-surviving proxy (no commit in >=2 years) is a coarse label; a repository can be dormant and later revived, and the corpus's `unknown_insufficient_post_departure_window` label exists precisely to avoid forcing a survival call where the post-departure window is too short. Finally, both corpora are drawn from GitHub only; repositories hosted elsewhere or migrated away from GitHub after founder departure are systematically invisible to any GitHub-only sampling frame, including ours.

# 7. Conclusion

We set out to test whether authority diffusing away from a project's founder before their departure predicts survival beyond existing snapshot diversity metrics, and found instead that the obvious way to build a GitHub corpus for this question — sampling by current popularity — silently conditions the sample on survival, starving the founder-only-TFDD event count down to 6 and rendering every planned statistical test uninformative. We quantified that conditioning against Avelino et al.'s own published population baseline (TFDD incidence 73.3% vs. 16.3%, z=5.89, p=3.8e-9; founder-only survival 100% vs. 40.6%, z=2.67, p=0.0075) and showed the pipeline's placebo check could not have detected an effect at n=6 regardless of its requested simulation budget, due to an undocumented 20-draw-per-repository cap. We release a 67-repository corpus sampled without any liveness conditioning, 72% of which are non-surviving by a two-year-inactivity proxy, as the concrete resource needed to run this hypothesis test properly.

Future work: (1) run the Section 3 pipeline against the Section 5 corpus and report whether its TFDD incidence and founder-only survival rate move toward Avelino et al.'s population figures, as predicted in Section 4.3; (2) complete the full-corpus alias audit begun in Section 4.2, extending the 3-of-15 spot-check to all repositories in both corpora; (3) locate or derive the Apache Project Maturity Model's community-diversity-specific criteria codes, left unresolved in Section 2, to add a second governance-gate baseline alongside Avelino et al.'s population statistics.

# References

[1] CHAOSS. "Metric: Contributor Absence Factor." https://www.chaoss.community/kb/metric-contributor-absence-factor/
[2] CHAOSS. "Metric: Elephant Factor." https://www.chaoss.community/kb/metric-elephant-factor/
[3] CHAOSS. "Metric: Newcomer Experience." https://www.chaoss.community/kb/metric-newcomer-experience/
[4] Apache Incubator. "Guide to Successful Graduation." https://incubator.apache.org/guides/graduation.html
[5] Apache Software Foundation. "Apache Project Maturity Model." https://community.apache.org/apache-way/apache-project-maturity-model.html
[6] Jergensen, C., Sarma, A., & Wagstrom, P. "The Onion Patch: Migration in Open Source Ecosystems." OpenSym 2011. https://dl.acm.org/doi/10.1145/2025113.2025127
[7] Steinmacher, I., et al. "A systematic literature review on the barriers faced by newcomers to open source software projects." Information and Software Technology, 2015. https://www.sciencedirect.com/science/article/abs/pii/S0950584914002390
[8] GH Archive. https://www.gharchive.org/
[9] GitHub Docs. "REST API endpoints for events." https://docs.github.com/en/rest/activity/events
[10] GH Archive payload field documentation. https://www.gharchive.org/
[11] World of Code. https://worldofcode.org/docs/
[12] "Scaling Author Identity Disambiguation to the World of Code: A Methodology." arXiv:2607.06920. https://arxiv.org/abs/2607.06920
[13] woc-hack/tutorial. https://github.com/woc-hack/tutorial
[14] "A mapping between Bot Commit, Projects, Files, and Blobs." Zenodo. https://zenodo.org/records/3699665
[15] ghtorrent/ghtorrent.org. https://github.com/ghtorrent/ghtorrent.org
[16] GHTorrent downloads page (dead domain). https://ghtorrent.org/downloads.html
[17] Hoffa, F. "Analyzing GitHub with BigQuery and other tools." https://github.com/fhoffa/analyzing_github
[18] Libraries.io Open Source Repository and Dependency Metadata. Zenodo. https://zenodo.org/records/3626071
[19] Avelino, G., Constantinou, E., Valente, M. T., & Serebrenik, A. "On the abandonment and survival of open source projects: An empirical investigation." ESEM 2019.

</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (clarity) The paper repeatedly describes its primary corpus as '3,427-repository corpus' (Sections 1.5, Contributions, 4.1, Conclusion) and states '3,409 repositories with no minable commit history at all.' Per the underlying experiment artifact (art_I5KoOp16hub5), this figure is actually 3,427 raw dataset records, of which 3,409 are rows from an unrelated HuggingFace commit-message dataset (kamalkishor1991/commit-messages-dataset) that was explicitly rejected as a data source in the dataset artifact's own build log for lacking repo-level lifecycle structure — they were never GitHub repositories that failed mining, they are individual commit records from a different task entirely, correctly filtered out by a 'no_commits' loader check. Describing this as '3,427 repositories' materially overstates the scale of the mining attempt and could mislead a reader (or a downstream researcher trying to replicate the pipeline) into thinking 3,409 real repositories were attempted and failed to yield history.
  Action: Rewrite every instance of '3,427-repository corpus' to something like '15 mined GitHub repositories (filtered from a 3,427-row raw pool that included 3,409 unrelated HuggingFace commit-message records, correctly excluded by the loader's no_commits check).' State the true attempted-repository count (15, per the dataset artifact) as the headline sample size throughout, since that is the number the TFDD pipeline actually operated on.
- [MAJOR] (evidence) The paper's central methodological fix — Section 5's liveness-non-conditioned 67-repository corpus — has never been run through the Section 3 DOA/TFDD pipeline. The paper's falsifiable prediction (Section 4.3: the new corpus 'should yield both a TFDD incidence closer to... 16.3%... and a founder-only survival rate closer to... 40.6%') is therefore entirely untested at submission time. The dataset artifact (art_ajD7unO0iQl3) also reveals that only 27 of the 67 repositories have a judgeable survival label at all (40 are 'unknown_insufficient_post_departure_window'), and its founder screen is a REST-API commit-share heuristic (>=60% of early commits), not the DOA-based founder-only-TFDD definition used in Section 3 — so it is not yet established that this corpus will even produce enough founder-only TFDD events to fix the sample-starvation problem diagnosed in Section 4.1. The paper currently reads as though the fix is validated when it is only proposed.
  Action: Either (a) run the Section 3 pipeline end-to-end on the Section 5 corpus before resubmission and report the resulting TFDD incidence/survival numbers against the falsifiable prediction — this is the single highest-value experiment left to run and would let the paper finally engage its title question — or (b) if that is infeasible this round, add an explicit caveat in Section 5 stating that the corpus's founder screen is a coarser heuristic than Section 3's DOA-based definition, and that only 27/67 repositories carry a judgeable label, so the corpus's ability to resolve the starvation problem remains unverified, not merely 'the next step.'
- [MINOR] (rigor) The evaluation artifact (art_zgnq2xDjA0ta) documents 'a genuine reproducibility discrepancy (5 vs. 6 founder-only TFDD events on an identical re-run)' of the Section 3 pipeline against the same 15-repository corpus. This is exactly the kind of finding the paper's own rigor-focused framing should surface, but it is not mentioned anywhere in the paper text — Section 4.1 reports 6 events, Section 4.2's Wilson CIs are computed over 5 (per the survival bullet: '100% (5 of 5)'), and the discrepancy between the two is never flagged or explained to the reader.
  Action: Add a sentence in Section 4.2 or the Limitations paragraph disclosing that an independent re-run of the Section 3 pipeline on the identical corpus produced 5 rather than 6 founder-only TFDD events, name the likely source if known (e.g., nondeterminism in alias resolution or tie-breaking in the founder-identification heuristic), and clarify which count (5 or 6) each downstream statistic in the paper actually uses.
- [MINOR] (clarity) Section 4.2's TFDD-incidence bullet ('73.3%... 11 of 15 candidates') and its own parenthetical Wilson-CI aside ('this corpus's 45.5% TF=1 fraction, CI [0.213, 0.720]') present two different proportions — any-TFDD-event rate versus TF=1-given-TFDD rate — inside one bullet point without labeling which is which, making the paragraph difficult to audit against the underlying evaluation artifact's Part B/Part E outputs.
  Action: Split into two explicitly labeled statistics with their own headers or clause markers, e.g., 'TFDD incidence: 73.3% (11/15) vs. Avelino's 16.3%...' and separately 'Conditional on TFDD, share at TF=1: 45.5% [CI] vs. Avelino's 66% [CI]...', each with its own comparison and p-value, so the two do not read as a single inconsistent number.
- [MINOR] (scope) Section 5 reports '48 (72%) have had no commit in at least two years' as the corpus's non-surviving signal, but the dataset artifact clarifies that only 27 of the 67 repositories actually carry a judgeable survival label (the other 40 fall into 'unknown_insufficient_post_departure_window'), with 20/27 non-surviving. The paper's 72% figure is a raw staleness proxy across all 67, not the same population as the 27-repo judgeable subset that would actually feed a founder-departure-survival analysis, and conflating the two overstates how much usable signal the new corpus currently provides.
  Action: Report both numbers explicitly and distinguish them: the raw two-year-inactivity rate across all 67 repos (72%) and the smaller judgeable-label subset actually usable for a TFDD-style survival analysis (27 repos, 20 non-surviving / 7 surviving), noting that the latter is the operative sample size for any future regression on this corpus.
- [MINOR] (novelty) The paper's diagnostic finding — that sampling GitHub repositories by present-day popularity/stars conditions the sample on survival — is a specific and well-quantified instance of a caution that is already broadly known in the mining-software-repositories and empirical-SE community (survivorship bias in convenience-sampled OSS corpora is a standard methodological caveat, e.g., raised in critiques of star-based or trending-based GitHub sampling more generally). The paper does not cite any general MSR methodology literature on this broader survivorship-bias problem, only Avelino et al.'s specific population baseline, which makes the contribution read as narrower than it could be positioned.
  Action: Add 1-2 sentences and citations situating the survivorship-bias diagnosis relative to the broader MSR literature on GitHub sampling validity (e.g., Kalliamvakou et al.'s 'perils of mining GitHub,' already cited for a different purpose in the experiment artifact, plus any dedicated work on star-based/trending-based sampling bias), to make clear the paper's contribution is a specific, quantified instance of a known class of problem rather than implying the survivorship-bias insight itself is novel.
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
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_LYICROwXFVjo/user_uploads`. Check this folder for anything relevant to your task.
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

### [2] HUMAN-USER prompt · 2026-08-20 21:21:04 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SYSTEM-USER prompt · 2026-08-20 21:21:36 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: "Same frame; corrected scale-of-attempt claim, added reproducibility gap (5 vs 6), demoted 2nd corpus from 'fix' to 'untested candidate'" is too long (at most 120 characters, got 135)
Every required field must be present and every field type must match the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```
