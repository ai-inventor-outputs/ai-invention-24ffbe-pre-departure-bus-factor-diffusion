# Measuring Authority Diffusion Before Founders Leave Open Source Projects

<div align="center">

<a href="https://cdn.jsdelivr.net/gh/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion@main/workflow.svg">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="workflow-dark.svg">
  <img alt="Artifact workflow — how every artifact in this repo was built" src="workflow.svg">
</picture>
</a>

<sub>🖱️ <b><a href="https://cdn.jsdelivr.net/gh/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion@main/workflow.svg">Open the interactive diagram</a></b> — every card links to its artifact folder.</sub>

</div>

> **TL;DR** — We reimplement and calibrate Avelino et al.'s Truck-Factor pipeline, add a new pre-departure authority-diffusion measurement whose permutation-test construct validity we confirm, and use a formal calibration gate to show that a convenience corpus of currently-famous repositories is a structurally inconsistent (not merely underpowered) sampling frame for testing whether that diffusion predicts survival -- reframing the paper as a validated instrument plus a precise specification of the corpus a follow-up study needs.

<details>
<summary>Full hypothesis</summary>

A calibrated reimplementation of Avelino et al.'s (ESEM 2019) DOA/Truck-Factor/TFDD pipeline, extended with a NEW pre-departure authority-diffusion measurement (founder commit-share and count of distinct non-founder DOA file-owners in the 6-12 months before a founder-only Truck-Factor Detachment), can (a) reproduce Avelino et al.'s published headline statistics closely enough to trust the reimplementation, and (b) show this new diffusion measurement is temporally specific to the pre-departure window rather than a generic property of active projects, measured via a SINGLE canonical, source-verified permutation scheme reported once (not two divergent configurations). On a 15-repository convenience corpus built by starting from currently-famous, still-maintained tools, the calibration gate demonstrates this corpus is NOT a valid sampling frame for testing the causal diffusion-predicts-survival claim: TFDD incidence (73.3% vs Avelino et al.'s 16.3%, z=5.98, p=1.5e-6) and 18-month survival (100% vs their 40.6%, z=2.70, p=0.011) both deviate sharply in the direction of severe survivorship bias, because starting from tools known today to still exist necessarily conditions on the outcome being predicted. A second, liveness-non-conditioned discovery attempt (GH Archive-style search over archived/stale repos, 700 candidates found but only ~28 actually attempted for extraction, yielding 1 usable repo) independently corroborates the mechanism but is explicitly reported as a small, possibly unrepresentative attempted-subsample, not a characterization of the full 700-candidate pool's true base rate -- resolving that gap (via a larger random subsample of the 700, or an explicit caveat) is now a required part of the corpus-construction claim rather than an incidental detail. This is a sampling-frame defect, not merely a power shortfall -- a larger sample drawn from the same 'currently-famous tools' frame would remain biased toward survivors and unable to test the causal claim. The original causal hypothesis (that founder-only-TFDD projects with diffused pre-departure authority survive at a higher rate than matched projects with concentrated authority) THEREFORE REMAINS OPEN, with zero outcome variance across all founder-only TFDD events observed to date (5 of 5 survived), and is reframed as the target of a specific, well-defined follow-up: a corpus constructed from a historical snapshot of GitHub repositories that does NOT condition on present-day liveness, extended via the already-built, checkpointed candidate pipeline and an authenticated GitHub token, yielding an estimated ~40 founder-only TFDD events -- the threshold this study's own fallback power analysis identifies as needed (an n>=10-complete-rows requirement whose statistical basis, e.g. an events-per-variable rule of thumb, must be explicitly cited rather than asserted as an unexplained cutoff). Given that this causal claim remains untested after two independent corpus-construction attempts, this paper's own framing must now explicitly address whether it is submitted as a full empirical-contribution paper (contingent on executing the token-enabled expansion to obtain at least one non-survivor before resubmission) or repositioned for a negative-results/tools-and-datasets track where a rigorously validated null/instrumentation contribution, honestly reported as such including in its title-level framing, is the appropriate bar. Until either the causal test is run or the venue framing is adjusted, this paper's contribution is the validated measurement instrument and calibration/robustness harness (pipeline replication, diagnostic gate, single canonical construct-validity check for the diffusion measurement with bot-account contamination explicitly ruled out on the founder-only-TFDD subset, and explicit positioning against CHAOSS's own reference-implementation tooling for longitudinal Contributor Absence Factor) plus a precise specification of what a valid test of the causal claim requires -- not an empirical answer to whether diffusion predicts survival.

</details>

[![Download PDF](https://img.shields.io/badge/Download-PDF-red)](https://cdn.jsdelivr.net/gh/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion@main/paper.pdf) [![LaTeX Source](https://img.shields.io/badge/LaTeX-Source-orange)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/main/paper_latex)

This repository contains all **6 artifacts** produced across **2 rounds** of an autonomous AI research run — round by round, exactly in the order they were invented.

## Round 1

| Artifact | Type | Demo | Source | Builds on |
|----------|------|------|--------|-----------|
| **[GitHub Founder-Departure Commit Corpus](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/main/round-1/dataset-1)** | [![dataset](https://img.shields.io/badge/dataset-f59e0b)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/main/round-1/dataset-1) | — | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/main/round-1/dataset-1/src) | — |
| **[Does authority spreading before founders leave keep projects…](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/main/round-1/experiment-1)** | [![experiment](https://img.shields.io/badge/experiment-8b5cf6)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/main/round-1/experiment-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/blob/main/round-1/experiment-1/demo/method_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/main/round-1/experiment-1/src) | — |
| **[Calibrating and Stress-Testing the Founder-Departure Diffusi…](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/main/round-1/evaluation-1)** | [![evaluation](https://img.shields.io/badge/evaluation-10b981)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/main/round-1/evaluation-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/blob/main/round-1/evaluation-1/demo/eval_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/main/round-1/evaluation-1/src) | — |

## Round 2

| Artifact | Type | Demo | Source | Builds on |
|----------|------|------|--------|-----------|
| **[OSS Community-Health Positioning and Bias-Free Data Sources](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/main/round-2/research-1)** | [![research](https://img.shields.io/badge/research-3b82f6)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/main/round-2/research-1) | [![View Research](https://img.shields.io/badge/View-Research-green)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/blob/main/round-2/research-1/demo/research_demo.md) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/main/round-2/research-1/src) | — |
| **[Non-Survivorship-Biased Founder Departure Corpus](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/main/round-2/dataset-1)** | [![dataset](https://img.shields.io/badge/dataset-f59e0b)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/main/round-2/dataset-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/blob/main/round-2/dataset-1/demo/data_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/main/round-2/dataset-1/src) | — |
| **[Closing the Rigor Gaps in the Diffusion Pipeline](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/main/round-2/evaluation-1)** | [![evaluation](https://img.shields.io/badge/evaluation-10b981)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/main/round-2/evaluation-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/blob/main/round-2/evaluation-1/demo/eval_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/main/round-2/evaluation-1/src) | <sub><i>uses:</i><br/>[dataset‑1&nbsp;(R1)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/main/round-1/dataset-1)<br/><i>extends:</i><br/>[experiment‑1&nbsp;(R1)](https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/tree/main/round-1/experiment-1)</sub> |

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
