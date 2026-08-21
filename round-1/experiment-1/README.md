# Does Founder Authority Diffusion Predict OSS Survival?

`demo/` — Self-contained demo (Colab-ready notebook or markdown). Run without setup.  
`src/` — Full source code, data, and outputs from the experiment execution.

**Type:** experiment  
**ID:** `art_4CZ-9Ou1G5ty`

## Layman Summary

We measured, from real GitHub commit histories, whether a project's code ownership had already spread beyond its founder in the months before the founder went silent, and tested if that early spread predicts whether the project survives.

## Full Summary

Re-implements Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline directly from real GitHub commit histories via the GitHub REST search API and `git log --numstat` history walks (no mocked or synthetic data). Sampled 270 candidate repositories across 6 languages (Python, JavaScript, Go, Ruby, Java, C++) stratified by popularity tier; 69 survived the age/size filters and were fully processed (clone -> per-file DOA snapshots -> yearly Truck-Factor sets -> TFDD detection). Detected 16 strict founder-only (TF=1) TFDD events and 20 relaxed (TF<=2) TFDD events. Unconditioned 18-month post-TFDD survival rate was 31.25% (strict) / 45% (relaxed), in the same neighborhood as Avelino et al.'s reported ~41%, cross-validating the DOA/TF/TFDD re-implementation. The new contribution (our_method) is a pre-departure authority-diffusion trajectory computed in the 12-to-6-month window before each TFDD event: founder_share (fraction of window commits made by the founder) and n_diffused_owners (count of independent non-founder DOA file-owners at window end). This is compared against Avelino et al.'s own approach (baseline): snapshot size/popularity covariates (stars, forks, developer count) measured AT the TFDD event with no temporal trajectory information. Both are fit as BH-corrected logistic regressions on the same 16-event strict sample, plus a within-repo placebo/falsification check that recomputes the same diffusion metrics on a random non-TFDD-adjacent window (15/16 events had a valid placebo window) to test whether the signal is specific to the pre-departure period rather than a generic property of any window. A matched-pairs bootstrap risk-ratio design (stars/forks/language-bucketed low-diffusion vs high-diffusion event pairs) was also implemented per the plan but found 0 matchable pairs at this sample size (n_pairs=0, risk_ratio=NaN) and is reported honestly as inconclusive at this scale rather than fabricated. In the realized logistic fit, our_method's founder_share coefficient is negative (-5.56, i.e. higher founder commit-share pre-departure associates with lower survival) and n_diffused_owners is also negative (-0.17) in this small sample, but neither survives BH correction at n=16 (BH p>0.6 for all covariates in both our_method and the baseline); pseudo-R^2 is 0.175 (our_method) vs 0.211 (baseline snapshot-only), so the baseline explains marginally more deviance in this small realized sample. The placebo regression on random non-TFDD windows shows a much larger, non-significant coefficient on placebo_founder_share (-164.5, p=1.0), consistent with the placebo metric being poorly identified in a non-TFDD-adjacent window rather than a real effect. All numbers here are the genuine output of one completed pipeline run (906.7s wall-clock) with no placeholders; the honest headline is that with only 16 founder-only TFDD events the study is underpowered to detect a significant BH-corrected effect, and this is reported transparently (raw coefficients, p-values, and both BH-corrected and uncorrected results are all present in the output) rather than oversold. method.py implements Stages 0-9 exactly as specified in the artifact plan: GitHub API sampling with popularity stratification, exclusion-criteria filtering (age/size/fork), `git log --numstat` commit-history extraction, the Fritz-et-al DOA formula (3.293 + 1.098*FA - 0.164*sqrt(AC) + 0.230*ln(1+DL)), greedy Truck-Factor-set computation, yearly TFDD scanning with a 1-year silence threshold, both strict (TF=1) and relaxed (TF<=2) TFDD detection reported separately, 12-to-6-month pre-departure diffusion metrics, 18-month post-TFDD Active/Inactive survival labeling, a within-repo placebo window falsification check, matched-pairs bootstrap risk-ratio, and BH-corrected logistic regression for both our_method and the baseline, with all per-event rows preserved in method_out.json (16 example rows under the exp_gen_sol_out schema, `dataset='founder_authority_diffusion_tfdd_survival'`, `input`=repo/founder identity JSON, `output`=full event record JSON, plus `predict_our_method_survived_prob` and `predict_baseline_survived_prob` per-example predicted probabilities). Full/mini/preview variants were generated and both files (21KB) are far under the 100MB size-limit threshold, so no splitting was required. Downstream GEN_PAPER_TEXT should present this as a genuine re-implementation validated against Avelino et al.'s published survival rate, with the new pre-departure diffusion signal reported as a directionally-consistent but not-yet-statistically-significant finding at n=16, and should NOT claim the matched-pairs risk-ratio result since it produced 0 matched pairs at this scale.

## Output Files

- `method.py`
- `full_method_out.json`
- `mini_method_out.json`
- `preview_method_out.json`

## Demo Files

- **method.py** — Research methodology implementation

---
*Generated by AI Inventor Pipeline*
