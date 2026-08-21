# upd_hypo — test_idea

> Phase: `invention_loop` · round 2 · `upd_hypo`
> Run: `iter1_0b7b616dce39` — Does Pre-Departure Authority Diffusion Predict Open-Source Project Survival? A Unified-Corpus Retest with a Window-Boundary-Noise Control
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `upd_hypo` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 19:07:50 UTC

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
title: 'Pre-Departure Authority Diffusion: An Underpowered Test'
hypothesis: >-
  An open-source project's survival after its founder stops committing (a founder-only Truck Factor Developer Detachment,
  or TFDD, in Avelino et al.'s ESEM 2019 terminology) is hypothesized to depend more on how diffused DOA-based commit/file
  authority already was among non-founder contributors in the 6-12 months BEFORE departure than on the project's popularity
  or size at the moment of departure -- which Avelino et al. already show is statistically indistinguishable between survivors
  and non-survivors at the TFDD snapshot (d=0.13-0.26). This iteration's evidence neither confirms nor refutes that claim:
  of three pre-registered tests, only one -- a within-repo random-window placebo control -- actually ran to completion, at
  n=30 founder-only TFDD events. It found the true pre-departure window's founder-share/survival correlation (r=0.180) statistically
  indistinguishable from an arbitrary window drawn from the same repositories' own histories (40th percentile of a 25-draw
  null, empirical p=0.615), a genuine but weakly-resolved null on that one specific test. The other two pre-registered tests
  (BH-FDR logistic regression; matched-pairs bootstrap) could not be run at all -- they returned zero usable observations
  per stratification cell -- so they provide no evidence either way, and must not be read as failed tests. The hypothesis
  is therefore narrowed and reframed: (1) the central claim is now explicitly conditional on closing three concrete gaps before
  any future test can be informative -- (a) a corpus of founder-only TFDD events an order of magnitude larger than the current
  30-62 repositories, since founder-only-TFDD scarcity, not the underlying mechanism, was the dominant source of attrition
  in both mining passes; (b) a validated sub-year DOA/TF window computation, since Avelino et al.'s DOA/TF pipeline was only
  ever validated at yearly full-history snapshots and the pre-departure window recomputation used here is an unvalidated methodological
  extension whose own boundary noise has not been separated from genuine authority-diffusion signal; (c) a single unified
  experimental corpus, since this iteration's dataset artifact (32 repos) and experiment artifact (62 repos, 30 usable) were
  mined independently and never reconciled into one analysis; (2) until those gaps are closed, the hypothesis should be evaluated
  as a scope-boundary/feasibility question -- can a pre-departure authority-diffusion signal be measured with enough precision
  and corpus size to be tested at all -- rather than as a claim already tested against Avelino et al.'s snapshot baseline.
  The core mechanism (trajectory of authority concentration predicts survival better than a point-in-time snapshot) is preserved
  unchanged from the prior iteration; what has changed is an honest downgrade of what current evidence shows about it, from
  'three-way tested' to 'one-third tested (null, low-resolution), two-thirds untestable at this scale.'
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
  Same trajectory-vs-snapshot claim kept; scope narrowed to reflect only 1/3 tests ran (null), 2/3 untestable at n=30
_confidence_delta: decreased
_key_changes:
- >-
  Corrected overclaiming: no longer states 'hypothesis fails on all three counts' -- only the placebo test (1 of 3) actually
  ran, producing a weak/low-resolution null; the regression and matched-pairs tests returned zero usable observations and
  provide no evidence either way
- >-
  Added an explicit precondition list (larger founder-only-TFDD corpus, validated sub-year DOA window, unified single experimental
  corpus) that must be satisfied before the three-criterion test can be considered informative
- >-
  Flagged the sub-year DOA/TF window computation as an unvalidated methodological extension whose own measurement noise has
  not been distinguished from genuine diffusion signal, per reviewer's MAJOR critique
- >-
  Flagged the corpus provenance mismatch between the 32-repo dataset artifact and the 62-repo (30-usable) experiment corpus
  as unresolved, per reviewer's MAJOR critique
- >-
  Reframed the research question from 'does pre-departure diffusion predict survival' (tested-and-answered framing) to 'can
  this signal be measured and tested at sufficient power and precision' (feasibility framing), reflecting that most of the
  evidence gathered this iteration is about measurement feasibility, not the underlying mechanism
- >-
  Preserved the core mechanism and all definitions (TFDD, DOA, authority diffusion, matched-pairs design) unchanged from the
  prior hypothesis, since no evidence contradicts the mechanism itself -- only the ability to test it at current scale
relation_type: evolution
</current_hypothesis>

<all_artifacts>
Complete set of research artifacts across all iterations.

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
in_dependencies:
- id: art_0qwvnbyIv0EL
  label: methodology
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
in_dependencies:
- id: art_24Q1bYB_ULpu
  label: dataset
- id: art_0qwvnbyIv0EL
  label: methodology
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
in_dependencies:
- id: art_eXxdnfS0o6aV
  label: baseline
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
</all_artifacts>

<new_artifacts_this_iteration>
These 3 artifacts were created THIS iteration.

id: art_70BX2SQt9m6k
type: dataset
in_dependencies:
- id: art_0qwvnbyIv0EL
  label: methodology
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

id: art_65c2e4aGIhui
type: experiment
in_dependencies:
- id: art_24Q1bYB_ULpu
  label: dataset
- id: art_0qwvnbyIv0EL
  label: methodology
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

id: art_IN6RRoJnrq1j
type: evaluation
in_dependencies:
- id: art_eXxdnfS0o6aV
  label: baseline
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
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

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

</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (methodology) The paper's description of the window-boundary-noise control (Section 3: '13 held-out repositories with no TFDD event in their observed history'; Section 4: '13 held-out, non-departure repositories') appears to contradict the underlying experiment artifact (art_65c2e4aGIhui), which states the control 'substitut[es] TFDD-corpus repos' own multi-year-before-departure periods for the unavailable non-TFDD candidate pool' -- i.e., it reuses stable periods from the same 32 repositories already used in the main analysis, rather than drawing on an independent set of repositories that never had a TFDD event. If the artifact's description is accurate, the noise floor is not an independent external benchmark; it is computed from the same corpus whose placebo result it is being used to judge, which weakens (though does not necessarily invalidate) the claim that it isolates 'measurement noise' cleanly separable from the phenomenon under study. This is the paper's single most important new analysis for this iteration's headline conclusion, so the discrepancy needs to be resolved, not left implicit.
  Action: Check the actual method.py / method_out.json from the experiment artifact to determine which set of repositories the noise-floor control actually drew on, and correct either the paper's text (if it misdescribes the artifact) or flag this as a genuine independent-sample construction if the paper's account is in fact correct and the artifact summary is stale. If the control does reuse the analysis corpus's own stable periods, add an explicit limitation stating that the noise floor is not fully independent of the placebo sample and discuss how that affects the strength of the 'noise, not signal' conclusion.
- [MAJOR] (rigor) The quantitative claim that the true window's placebo effect 'sits at roughly 1.4 standard deviations of the boundary-noise floor from zero, short of the 2-standard-deviation threshold' compares two statistics on apparently incommensurate scales: the boundary-noise floor is reported as a variance/SD of a raw covariate (mean 11.74, SD 3.43, in units of the diffusion covariate itself), while the placebo statistic being judged is a correlation coefficient (r = -0.246) drawn from a null distribution with its own, much smaller SD (0.176) on the correlation scale. The text asserts these are combined ('measured in placebo-null units') but never shows the conversion. As written, a reader cannot verify or reproduce the '1.4 SD' figure, which is the number the paper's entire third success criterion turns on.
  Action: Provide the explicit calculation (formula or worked numeric example) that converts the raw-covariate boundary-noise floor into the same scale as the placebo-null correlation statistic, or re-derive the comparison entirely on one consistent scale (e.g., by running the boundary-noise control using the identical correlation statistic and window procedure used for the placebo test, rather than a differently-scaled variance measure). Until this is shown, treat the '1.4 SD' / '2-SD threshold' framing as unverified.
- [MINOR] (scope) The paper's headline hypothesis is framed around declining founder commit share, but that covariate is zero-variance in 31 of 32 repositories and cannot be tested at all; the paper substitutes a DOA-owner-count proxy throughout. This is disclosed as a limitation, which is good practice, but the framing in the abstract and introduction ('whether authority is already diffusing away from the founder') still reads as if the founder-share mechanism itself was tested, when in fact only a correlated proxy was.
  Action: Soften the abstract/introduction framing to state upfront that the tested diffusion covariate is a proxy (count of new non-founder DOA owners), not founder commit share directly, so a reader does not have to reach the limitations section to learn the paper's headline mechanism was not directly testable in this corpus.
- [MINOR] (novelty) The prior review's suggestion to situate the trajectory-vs-snapshot framing against the broader OSS-abandonment-prediction literature (time-series/activity-trend features, issue/PR dynamics, social-network signals) has not been addressed in this revision; the related work remains confined to the two Avelino et al. papers and brief single-sentence citations to ecosystem-turnover studies.
  Action: Add a short related-work paragraph (even 3-4 sentences) distinguishing this paper's DOA-based authority-diffusion operationalization from general trend/time-series abandonment predictors already common in the OSS-survival literature, to make clear what is specific to this contribution versus what is a known idea applied with a new operationalization.
- [MINOR] (evidence) Section 5's bootstrap confidence intervals and identity-resolution audit are computed on the prior iteration's 30-repository sample rather than the current iteration's unified 32-repository corpus (disclosed as Limitation 3), meaning every CI and error-rate figure quoted in the paper's discussion of data quality does not describe the corpus the paper's own headline regression and placebo results were computed on. This is honestly flagged, but it means two of the paper's supporting rigor claims (Section 5) do not actually bound the risk in the analysis corpus used in Section 4.
  Action: Re-run the bootstrap CI and identity-resolution audit directly against the unified 32-repository corpus (the paper itself identifies this as the most direct fix); at minimum, if compute/scope prevents this now, state explicitly in the abstract/introduction (not only the limitations section) that Section 5's rigor checks apply to a different, though comparably-sized, sample than the main results.
- [MINOR] (clarity) The paper reports 'BH-FDR-adjusted p-value is 0.84' for the diffusion covariate but does not state the number of hypotheses the BH-FDR correction was applied over (implied to be ~12 predictors from the regression, but this is not stated at the point the p-value is given), making it hard for a reader to sanity-check the adjustment.
  Action: State the number of tests corrected for (e.g., '12 predictors, BH-FDR corrected') directly alongside the reported adjusted p-value in Section 4, rather than requiring the reader to infer it from the earlier mention of '12 predictors' in the regression paragraph.
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

### [2] HUMAN-USER prompt · 2026-08-21 19:07:50 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SYSTEM-USER prompt · 2026-08-21 19:09:06 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Same mechanism kept; downgraded to near-negative given 2/3 clean-fail tests, placebo status now UNRESOLVED not confirmed-noise per reviewer' is too long (at most 120 characters, got 139)
Every required field must be present and every field type must match the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```
