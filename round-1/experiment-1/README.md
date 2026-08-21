# Does authority spreading before founders leave keep projects alive?

`demo/` — Self-contained demo (Colab-ready notebook or markdown). Run without setup.  
`src/` — Full source code, data, and outputs from the experiment execution.

**Type:** experiment  
**ID:** `art_I5KoOp16hub5`

## Layman Summary

We tested whether open-source projects survive their founder's departure better when other contributors had already started taking over code ownership beforehand.

## Full Summary

Reimplemented Avelino et al.'s (ESEM 2019) Degree-of-Authorship / Truck-Factor / Truck-Factor-Detachment-Departure (TFDD) pipeline end-to-end in method.py, run against the DATASET dependency's mined GitHub commit histories (15 usable repos with full per-file commit logs, out of 3427 raw records also containing an unrelated HuggingFace commit-message corpus that the loader correctly skips via a 'no_commits' filter). For each repo the pipeline: (1) resolves author aliases via normalized email/github-login matching and logs a per-repo alias-collapse-rate QA metric; (2) computes yearly cumulative-window DOA (Degree of Authorship) per file per author using Fritz et al.'s weights (FA=3.293, DL=1.098, AC=-1.017) as used by Avelino et al.; (3) derives the yearly greedy Truck-Factor set from primary DOA ownership; (4) detects Truck-Factor-Detachment-Departure events (a TF-set fully silent for 12 months) and isolates founder-only TFDDs (TF=1 and the sole departing developer is the repo's first human committer, with bulk-import first commits filtered per the Kalliamvakou et al. 2014 'perils of mining GitHub' heuristic of >80% of files touched within the first week); (5) computes a NEW pre-departure authority-diffusion trajectory over the 6-12 months before each TFDD -- founder commit-share and count of distinct non-founder DOA file-owners -- alongside Avelino et al.'s original at-TFDD snapshot covariates (developers/commits/files at detachment); (6) classifies 18-month post-TFDD survival into Avelino's four-level active/inactive grades (thriving/maintained/dormant/dead) plus a binary survived flag; (7) runs a matched-pairs bootstrap comparison (nearest-neighbor matching on standardized log-stars/log-forks/log-contributors within language, comparing high- vs low-diffusion projects) with 10,000-resample 95% CIs; (8) fits BH-corrected logistic and ordinal (statsmodels OrderedModel) regressions of survival on diffusion predictors plus snapshot covariates, reporting standardized effect sizes comparable to Avelino et al.'s reported d=0.13 (files) / 0.25-0.26 (developers, commits); (9) runs a 500-iteration placebo/window-shuffle check that redraws the pre-departure window from elsewhere in project history and refits the regression, to test whether the true diffusion-window effect exceeds the null distribution of effects from arbitrary windows. All steps implement both the proposed authority-diffusion predictor AND Avelino et al.'s original snapshot-covariate baseline side-by-side in the same regression and matched-pairs machinery, so the two are directly comparable under identical data and identical statistical procedures -- baseline_predict and ourmethod_predict columns are both emitted per example. The run found n_repos_total=3427 raw dataset records (3409 filtered as non-repo commit-message rows lacking file-level structure; the dataset dependency's GitHub API rate limiting -- 60 unauthenticated requests/hour -- constrained the usable repo count to 15, well below the plan's 150-250 target), yielding n_founder_tfdd_events=6, which falls below the ~40 events the plan's own fallback_plan identifies as needed for a well-powered matched-pairs test; per that fallback plan this limitation is reported explicitly in the output metadata (extended_sample_used_TFle2 flag, doa_approximation_used flag, alias_qa block) rather than silently presented as adequately powered, and all regression/matched-pairs/placebo numbers in method_out.json should be read as a small-n pilot demonstrating the pipeline mechanics rather than a well-powered test of the founder-diffusion-predicts-survival hypothesis. A bug where the dataset dependency's example-wrapper format (repo records JSON-encoded inside an 'input' string field, per the exp_gen_sol_out schema) was not being unwrapped -- causing every repo to be misread as having zero commits -- was found and fixed during this run; the corrected loader now parses that wrapper and the pipeline runs end-to-end in ~90 seconds. Output method_out.json / full_method_out.json / mini_method_out.json / preview_method_out.json validate cleanly against the exp_gen_sol_out.json schema (0 errors) and are all under 9KB, far below the 100MB size limit. Downstream users (GEN_PAPER_TEXT) should present this as a methodology-validation / small-sample pilot result: the pipeline itself (DOA/TF/TFDD replication, diffusion-trajectory measurement, survival classification, matched-pairs + regression + placebo statistical machinery) is fully implemented and tested (smoke tests on synthetic hand-constructed repos, mini-run sanity checks, and the full corpus run all pass), but the headline finding is data-starved (n=6 events) due to upstream GitHub API rate limiting documented in the DATASET dependency's own metadata, not a pipeline defect.

## Output Files

- `method.py`
- `full_method_out.json`
- `mini_method_out.json`
- `preview_method_out.json`

## Demo Files

- **method.py** — Research methodology implementation

---
*Generated by AI Inventor Pipeline*
