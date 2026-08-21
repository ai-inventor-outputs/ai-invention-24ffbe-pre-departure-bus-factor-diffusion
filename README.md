# Authority Diffusion Before Founder Departure: Diagnosing Sample Starvation in OSS Survival Research

<div align="center">

<a href="https://cdn.jsdelivr.net/gh/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion@fork/run_LYICROwXFVjo/workflow.svg">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="workflow-dark.svg">
  <img alt="Artifact workflow — how every artifact in this repo was built" src="workflow.svg">
</picture>
</a>

<sub>🖱️ <b><a href="https://cdn.jsdelivr.net/gh/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion@fork/run_LYICROwXFVjo/workflow.svg">Open the interactive diagram</a></b> — every card links to its artifact folder.</sub>

</div>

> **TL;DR** — Diagnoses why a popularity-sampled 3,427-repository GitHub corpus yielded only 6 founder-only TFDD events (insufficient for the planned authority-diffusion-vs-survival tests), formally shows via two-proportion tests against Avelino et al.'s published population that the corpus is survivorship-conditioned (TFDD incidence 73.3% vs 16.3%, p=3.8e-9; founder-only survival 100% vs 40.6%, p=0.0075), finds the pipeline's placebo check was structurally incapable of detecting an effect due to an undocumented 20-draw cap, and releases a 67-repository liveness-non-conditioned corpus (72% non-surviving by proxy) as the fix.

<details>
<summary>Full hypothesis</summary>

A calibrated reimplementation of Avelino et al.'s (ESEM 2019) DOA/Truck-Factor/TFDD pipeline, extended with a NEW pre-departure authority-diffusion measurement (founder commit-share and count of distinct non-founder DOA file-owners in the 6-12 months before a founder-only Truck-Factor Detachment), can (a) reproduce Avelino et al.'s published headline statistics closely enough to trust the reimplementation, and (b) show this new diffusion measurement is temporally specific to the pre-departure window rather than a generic property of active projects. On the original 15-repository popularity-sampled corpus (mined from a 3,427-ROW raw candidate pool of which 3,409 rows were unrelated HuggingFace commit-message records correctly excluded by a no-commits filter, NOT 3,409 failed GitHub repositories -- a scale claim this revision corrects), the calibration gate demonstrates the corpus is NOT a valid sampling frame for testing the causal diffusion-predicts-survival claim: any-TFDD incidence (73.3% vs Avelino et al.'s 16.3%, z=5.89, p=3.8e-9) and founder-only-TFDD 18-month survival (100% vs their 40.6%, z=2.67, p=0.0075) both deviate sharply in the direction of severe survivorship bias, because starting from tools known today to still exist necessarily conditions on the outcome being predicted. This is a sampling-frame defect, not merely a power shortfall. A newly surfaced reliability issue must now be carried alongside that finding: an independent re-run of the identical Section-3 pipeline on the identical 15-repo corpus produced 5 founder-only-TFDD events rather than 6, a genuine reproducibility discrepancy (likely nondeterminism in alias resolution or founder-identification tie-breaking) that has not yet been root-caused, so every downstream statistic drawn from this corpus must state explicitly whether it rests on n=5 or n=6. A second corpus (67 repositories, GitHub Search API `created:`/`pushed:` date-window sampling with NO present-day-liveness filter) has been built specifically to remove the popularity conditioning, but it REMAINS UNVALIDATED as a fix at this iteration: it has not yet been run through the Section-3 DOA/TFDD pipeline, only 27 of its 67 repositories carry a judgeable survival label (20 non-surviving / 7 surviving; the other 40 are 'insufficient post-departure window'), and its founder screen is a coarser REST-API commit-share heuristic (dominant author >=60% of early commits), not the DOA-based founder-only-TFDD definition the paper's own pipeline uses -- so it is not yet established that this corpus will even yield enough founder-only TFDD events to fix the n=5-6 starvation problem, let alone produce incidence/survival rates closer to Avelino et al.'s population figures. The original causal hypothesis (that founder-only-TFDD projects with diffused pre-departure authority survive at a higher rate than matched projects with concentrated authority) THEREFORE REMAINS OPEN. The single highest-value action for the next iteration is to run the existing Section-3 pipeline end-to-end on this existing 67-repository corpus and report the resulting founder-only-TFDD count and incidence/survival rates against the explicit falsifiable prediction (a non-conditioned frame should move incidence toward ~16.3% and survival toward ~40.6%, not reproduce 73.3%/100%) -- this is a concrete, already-buildable next step, not a hypothetical one, since both the pipeline and the candidate corpus already exist as artifacts. Until that run happens, this paper's contribution remains the validated measurement instrument, the calibration/robustness harness (including the newly documented placebo-check hard-cap artifact: a previously undocumented 20-draws-per-repository cap that makes the pipeline's apparent placebo-check stability across simulation budgets structurally uninformative rather than confirmatory, since the resolvable-effect floor at n=5-6 exceeds any plausible true effect regardless of requested budget), and a precise specification -- now partially executed but not yet closed -- of what a valid test of the causal claim requires.

</details>

[![Download PDF](https://img.shields.io/badge/Download-PDF-red)](https://cdn.jsdelivr.net/gh/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion@fork/run_LYICROwXFVjo/paper.pdf) [![LaTeX Source](https://img.shields.io/badge/LaTeX-Source-orange)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/fork/run_LYICROwXFVjo/paper_latex)

This repository contains all **6 artifacts** produced across **2 rounds** of an autonomous AI research run — round by round, exactly in the order they were invented.

## Round 1

| Artifact | Type | Demo | Source | Builds on |
|----------|------|------|--------|-----------|
| **[GitHub Founder-Departure Commit Corpus](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/fork/run_LYICROwXFVjo/round-1/dataset-1)** | [![dataset](https://img.shields.io/badge/dataset-f59e0b)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/fork/run_LYICROwXFVjo/round-1/dataset-1) | — | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/fork/run_LYICROwXFVjo/round-1/dataset-1/src) | — |
| **[Does authority spreading before founders leave keep projects…](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/fork/run_LYICROwXFVjo/round-1/experiment-1)** | [![experiment](https://img.shields.io/badge/experiment-8b5cf6)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/fork/run_LYICROwXFVjo/round-1/experiment-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/blob/fork/run_LYICROwXFVjo/round-1/experiment-1/demo/method_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/fork/run_LYICROwXFVjo/round-1/experiment-1/src) | — |
| **[Calibrating and Stress-Testing the Founder-Departure Diffusi…](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/fork/run_LYICROwXFVjo/round-1/evaluation-1)** | [![evaluation](https://img.shields.io/badge/evaluation-10b981)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/fork/run_LYICROwXFVjo/round-1/evaluation-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/blob/fork/run_LYICROwXFVjo/round-1/evaluation-1/demo/eval_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/fork/run_LYICROwXFVjo/round-1/evaluation-1/src) | — |

## Round 2

| Artifact | Type | Demo | Source | Builds on |
|----------|------|------|--------|-----------|
| **[OSS Community-Health Positioning and Bias-Free Data Sources](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/fork/run_LYICROwXFVjo/round-2/research-1)** | [![research](https://img.shields.io/badge/research-3b82f6)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/fork/run_LYICROwXFVjo/round-2/research-1) | [![View Research](https://img.shields.io/badge/View-Research-green)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/blob/fork/run_LYICROwXFVjo/round-2/research-1/demo/research_demo.md) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/fork/run_LYICROwXFVjo/round-2/research-1/src) | — |
| **[Founder-Departure GitHub Corpus Without Liveness Bias](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/fork/run_LYICROwXFVjo/round-2/dataset-1)** | [![dataset](https://img.shields.io/badge/dataset-f59e0b)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/fork/run_LYICROwXFVjo/round-2/dataset-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/blob/fork/run_LYICROwXFVjo/round-2/dataset-1/demo/data_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/fork/run_LYICROwXFVjo/round-2/dataset-1/src) | — |
| **[Closing the Rigor Gaps in the Diffusion Pipeline](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/fork/run_LYICROwXFVjo/round-2/evaluation-1)** | [![evaluation](https://img.shields.io/badge/evaluation-10b981)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/fork/run_LYICROwXFVjo/round-2/evaluation-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/blob/fork/run_LYICROwXFVjo/round-2/evaluation-1/demo/eval_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/fork/run_LYICROwXFVjo/round-2/evaluation-1/src) | <sub><i>uses:</i><br/>[dataset‑1&nbsp;(R1)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/fork/run_LYICROwXFVjo/round-1/dataset-1)<br/><i>extends:</i><br/>[experiment‑1&nbsp;(R1)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/fork/run_LYICROwXFVjo/round-1/experiment-1)</sub> |

## Repository Structure

Artifacts are grouped by the round of invention that produced them. Each
artifact has its own folder with source code and a self-contained demo:

```
.
├── round-1/                         # One folder per round of invention
│   ├── experiment-1/
│   │   ├── README.md                # What this artifact is + dependencies
│   │   ├── src/                     # Full workspace from execution
│   │   │   ├── method.py            # Main implementation
│   │   │   ├── method_out.json      # Full output data
│   │   │   └── ...                  # All execution artifacts
│   │   └── demo/                    # Self-contained demo
│   │       └── method_code_demo.ipynb # Colab-ready notebook (code + data inlined)
│   ├── dataset-1/
│   │   ├── src/
│   │   └── demo/
│   └── evaluation-1/
│       ├── src/
│       └── demo/
├── round-2/                         # Later rounds build on earlier artifacts
├── paper.pdf                        # Research paper
├── paper_latex/                     # LaTeX source files
├── chat/                            # Every prompt, response and tool call, per module
├── workflow.svg                     # Artifact dependency diagram (this page's header)
└── README.md
```

## Running Notebooks

### Option 1: Google Colab (Recommended)

Click the "Open in Colab" badges above to run notebooks directly in your browser.
No installation required!

### Option 2: Local Jupyter

```bash
# Clone the repo
git clone https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion
cd ai-invention-24ffbe-pre-departure-bus-factor-diffusion

# Install dependencies
pip install jupyter

# Run any artifact's demo notebook
jupyter notebook <artifact_folder>/demo/
```

## Source Code

The original source files are in each artifact's `src/` folder.
These files may have external dependencies - use the demo notebooks for a self-contained experience.

---
*Generated by AI Inventor Pipeline - Automated Research Generation*
