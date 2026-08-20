# Closing the Rigor Gaps in the Diffusion Pipeline

`demo/` — Self-contained demo (Colab-ready notebook or markdown). Run without setup.  
`src/` — Full source code, data, and outputs from the experiment execution.

**Type:** evaluation  
**ID:** `art_yOHrviKrh_11`

## Layman Summary

Re-checks a small open-source study by disclosing its randomization method, adding proper confidence intervals, spot-checking data against live GitHub, listing every repo, and honestly stating what remains unproven.

## Full Summary

This evaluation artifact closes five reviewer-named rigor gaps in the prior founder-departure authority-diffusion pipeline (EXPERIMENT art_I5KoOp16hub5, DATASET art_ZuMis522AEPF) by re-analyzing their outputs in a new eval.py, without collecting new repos or new methods. (A) Discloses the placebo/window-shuffle permutation scheme exactly from method.py's source: continuous with-replacement sampling of window start offsets, per-repo shipped cap of 20 draws (not 500/60/40 as summarized), no cross-stratum seed dependence; reports the combinatorial feasible-window space per founder-TFDD repo (741 total feasible start-month positions across 5 founder-only-TFDD events found on re-run, vs 6 claimed in the EXPERIMENT summary); re-runs the placebo test at budgets 20/100/300 draws per repo (up to 300 achieved in ~113s wall-clock for the largest budget, well under a 20-minute cap), reporting a convergence table of null-distribution mean/SD and the theoretical minimum two-sided p-value (1/(k+1)) at each budget; and proves no true-effect placebo p-value is computable at any budget because method.run_regressions requires n>=10 while n_founder_tfdd_events=5, so the disclosure gap is closed but the underlying power gap is not. (B) Computes Wilson 95% CIs for Avelino et al.'s reported 66% TF=1 rate (n=315, CI [0.606, 0.710]) and this study's own all-TFDD-denominator TF=1 rate (CI [0.354, 0.848]), finding the intervals overlap, with an explicit caution that this study's wide small-n interval makes 'overlap' weak evidence rather than validation. (C) Spot-checks alias-resolution against live GitHub contributor data for 3 of 15 repos (20% of corpus, amoffat/sh, arrow-py/arrow, Kludex/starlette), finding no confirmed bot-as-authority-holder or over-merging, one plausible under-merged same-human pair (would slightly deflate diffusion score, not flip classification), and one unresolved bot-inflation risk (dependabot[bot] at 159 contributions on Kludex/starlette) that a contributor-list-only check cannot rule out without file-level DOA attribution. (D) Emits an exact 15-row repository table (verified live count matches the dataset's claimed 15) with repo name, language, stars, forks, history span, TFDD/TF=1/survival status, and diffusion metrics, cross-checked directly against the two source JSON files with missing-field flags where applicable. (E) Quantifies this corpus's TFDD incidence (73.3% at n=15) and survival rate (100% among detected TFDDs) against Avelino et al.'s published 16.3% incidence and 40.6% survival via exact binomial and normal-approximation two-proportion tests, both showing large, statistically significant deviations in the direction consistent with survivorship bias; and documents a formal 'Residual Limitation' section explaining why a survivor-conditioned sampling frame is an inconsistent (not merely imprecise) estimator, quoting the DATASET artifact's own 60-req/hour GitHub API rate-limit constraint (15 of ~104 candidate repos completed), and giving a concrete falsifiable prediction for a future GITHUB_TOKEN-enabled run, explicitly not claiming the second-frame comparison was run. All five parts write into eval_out.json under clearly named top-level keys (permutation_disclosure, tf1_ci_comparison, alias_spotcheck, repo_table, survivorship_bias_quantification) plus a top-level overall_verdict summarizing which gaps are fully closed with data (A's disclosure, B, D, E's quantification) versus structurally open (A's power problem, E's second-frame comparison, C's full-corpus coverage). eval_out.json validates cleanly against the exp_eval_sol_out schema (0 errors, 0 warnings after adding numeric eval_* fields to every example); full/mini/preview variants (46KB/35KB/19KB) are all far under the 100MB size limit. pyproject.toml pins numpy==2.5.2, pandas==3.0.5, scipy==1.18.0, scikit-learn==1.9.0, statsmodels==0.14.6, loguru==0.7.3, psutil==7.2.2, matching the installed .venv exactly. Downstream GEN_PAPER_TEXT should present this as closing the disclosure/comparison/reproducibility gaps with concrete numbers while explicitly retaining two structurally open limitations (small-n placebo power, single-frame survivorship-bias evidence) as honest scope boundaries rather than resolved claims.

## Dependencies

- `art_ZuMis522AEPF` — dataset
- `art_I5KoOp16hub5` — experiment

## Output Files

- `eval.py`
- `full_eval_out.json`
- `mini_eval_out.json`
- `preview_eval_out.json`

## Demo Files

- **eval.py** — Evaluation script with metrics computation

---
*Generated by AI Inventor Pipeline*
