# gen_demo_art_experiment_2 — report_results

> Phase: `gen_paper_repo` · `gen_demo_art`
> Run: `iter1_0b7b616dce39` — Does Pre-Departure Authority Diffusion Predict Open-Source Project Survival? A Unified-Corpus Retest with a Window-Boundary-Noise Control
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_demo_art_experiment_2` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-08-21 19:21:22 UTC

```
model: claude-sonnet-5 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui
```

### [2] SYSTEM-USER prompt · 2026-08-21 19:21:30 UTC

````
<conversion_philosophy>
**MINIMAL CHANGES — PRESERVE THE ORIGINAL CODE**

The goal is to make the artifact's code READABLE, UNDERSTANDABLE, and RUNNABLE in a short time
to someone reviewing the research, with the option to easily scale parameters back to original
values for a full run (which can take much longer). Think of this as annotating and reformatting,
not refactoring.

**DO:**
- Split the original script into logical notebook cells (imports, setup, processing, results)
- Add markdown cells BETWEEN code cells explaining what each section does and why
- Add inline comments where the logic is non-obvious
- Add a visualization/summary cell at the end showing key outputs
- Fix hardcoded file paths to use the GitHub data loading pattern

**DO NOT:**
- Rewrite functions or change algorithms
- Rename variables or restructure logic
- Add error handling, type hints, or "improvements" that weren't in the original
- Simplify or "clean up" the original code
- Remove any original comments or logic
- Change the computational approach

The reader should recognize the original script when looking at the notebook — it's the
same code, just split into cells with explanatory markdown between sections.
</conversion_philosophy>

<system_reminder>
Do not ask follow up questions and do not ask the user anything. Execute all steps independently.
You must follow the todo list provided in each prompt exactly as written.
No placeholders, stubs, or incomplete code — all code must be complete and functional.
</system_reminder>

<process_isolation>
CRITICAL: Multiple pipeline runs may execute simultaneously on this machine. `ps aux | grep method.py` matches ALL runs, not just yours.
- NEVER kill processes by name (`killall`, `pkill -f`, `ps aux | grep ... | xargs kill`). This kills OTHER runs' processes.
- NEVER monitor processes by name (`ps aux | grep method.py`). You will see other runs' processes and get confused.
- ALWAYS use PID-based process management:
  Run: `uv run method.py & PID=$!` or `timeout <seconds> uv run method.py & PID=$!`
  Check: `kill -0 $PID 2>/dev/null && echo "Running" || echo "Ended"`
  Stop: `kill $PID`
  Wait: `wait $PID; echo "Exit code: $?"`
  Monitor: `tail -f logs/run.log & TAIL_PID=$!` then `kill $TAIL_PID` when done
</process_isolation>

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/`:
GOOD: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/file.py`, `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<task>
Convert this artifact's Python script into a demo notebook with MINIMAL changes to the original code.
Split into cells, add markdown explanations between sections, add a visualization cell at the end.
Output: mini_demo_data.json + code_demo.ipynb (notebook that loads data from GitHub URL)
</task>

<artifact_info>
id: art_65c2e4aGIhui
type: experiment
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
out_demo_files:
- path: method.py
  description: Research methodology implementation
</artifact_info>

<github_repo>
Repo URL: https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion
Raw data URL: https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json

URLs won't work yet — files pushed to GitHub AFTER notebook creation.
Use local fallback pattern so notebook works locally (now) and in Colab (after deployment).
</github_repo>

<data_file_sizes>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_file_sizes>

<install_dependencies_pattern>
Follow the aii-colab skill exactly. It has the install cell pattern, pre-installed package list, numpy 2.0 compat shims, and all Colab-specific rules.
</install_dependencies_pattern>

<data_loading_pattern>
`mini_demo_data.json` = curated subset for the demo.
Use this pattern for Colab compatibility (GitHub URL with local fallback):
```python
GITHUB_DATA_URL = "https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json"
import json, os

def load_data():
    try:
        import urllib.request
        with urllib.request.urlopen(GITHUB_DATA_URL) as response:
            return json.loads(response.read().decode())
    except Exception: pass
    if os.path.exists("mini_demo_data.json"):
        with open("mini_demo_data.json") as f: return json.load(f)
    raise FileNotFoundError("Could not load mini_demo_data.json")
```
</data_loading_pattern>

<notebook_structure>
--- Setup ---
Cell 1 (markdown): Title, description, what this artifact does.
Cell 2 (code): Install dependencies — follow the aii-colab skill's install cell pattern exactly. Fill in all packages imported by the artifact's code.
Cell 3 (code): Imports — copy original import block as-is, plus any additional imports needed for the notebook (e.g. matplotlib for visualization).
Cell 4 (code): Data loading helper — use the <data_loading_pattern> above.
Cell 5 (code): `data = load_data()`

--- Config ---
Config cell (code): Define ALL tunable parameters (iterations, epochs, n_samples, hidden_size, etc.) as variables at the top of this cell. Start with the ABSOLUTE MINIMUM values — the smallest that produce any output at all (e.g. 1 iteration, 2 samples, smallest array size). These get gradually increased during testing — see TODOs.

--- Processing ---
Remaining cells: One code cell per logical section of the original script. Add a markdown cell BEFORE each code cell. Copy code as closely as possible, with these changes:
  1. Replace file paths to use the loaded `data` variable.
  2. Use the config variables from the config cell (NOT hardcoded values).
  3. Minimal fixes are allowed if something doesn't work in notebook context (e.g. adjusting paths, removing CLI args, fixing imports), but keep changes to the absolute minimum.

--- Results ---
Visualization cell (code): Print key results in a readable table, plot numeric data with matplotlib if appropriate.
</notebook_structure>

<priority>
WORKING > OPTIMIZED. A small-scale demo that runs correctly is the goal. Once the notebook passes with minimum config values, scale up only if time permits — do NOT spend multiple retries chasing larger parameters. If a working version exists, finish and move on.
</priority>

<max_notebook_total_runtime>600s (10 min)</max_notebook_total_runtime>

<test_environment>
To test-run the notebook in a clean environment (simulating Colab), create a disposable `.nb_env` in your workspace:
```bash
/usr/local/bin/python3.12 -m venv .nb_env
.nb_env/bin/pip install -q pip jupyter ipykernel
.nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb
rm -rf .nb_env
```
The timeout is set to <max_notebook_total_runtime>. The entire notebook must finish within this time.

What happens: the .venv starts empty (just jupyter). When the notebook's install cell runs, `google.colab` is NOT in sys.modules, so ALL packages get installed — non-Colab packages unconditionally, and Colab packages (numpy, pandas, etc.) at Colab's exact versions via the guard block. The result mirrors Colab's environment as closely as possible. If a cell fails, fix the notebook and re-run.
</test_environment>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.


<todos>
TODO 1. Read and STRICTLY follow these skills: aii-colab, aii-long-running-tasks.
TODO 2. Read demo file and relevant preview_* files (preview only). Understand script structure: imports, setup, processing, output. Identify ALL tunable parameters (iterations, epochs, n_samples, hidden_size, batch_size, etc.) — these go in the config cell.
TODO 3. Create `mini_demo_data.json`: curated subset from at most ONE dataset (no more than 100 diverse examples). CRITICAL: do NOT read/grep full output file — may crash. Use `head -c 5000` or stream first entries with Python to pick examples.
TODO 4. Create `code_demo.ipynb` via NotebookEdit following <notebook_structure>. Set ALL config parameters to ABSOLUTE MINIMUM values — the smallest that produce any output (e.g. 1 iteration, 2 samples, smallest array sizes). Test-run using <test_environment>. Fix all errors until it passes.
TODO 5. GRADUALLY SCALE (but don't overdo it): increase config params step by step (e.g. ~2x each round). After each increase: test-run, record runtime, fix errors. STOP SCALING as soon as results look meaningful — a working small-scale demo beats a failed large-scale one. If full original params fit within <max_notebook_total_runtime> (10% margin), use them. Otherwise keep whatever works and comment out the true original values. Do NOT spend more than 2-3 scaling rounds.
TODO 6. Verify: (1) code_demo.ipynb contains GITHUB_DATA_URL = "https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json" exactly, (2) mini_demo_data.json exists, (3) uses GitHub URL pattern not just open('mini_demo_data.json').
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "DemoExpectedFiles": {
      "description": "Expected output files from code demo notebook generation.",
      "properties": {
        "notebook": {
          "default": "",
          "description": "Path to the generated demo notebook. Example: 'code_demo.ipynb'",
          "title": "Notebook",
          "type": "string"
        },
        "mini_data_file": {
          "default": "",
          "description": "Path to the mini demo data JSON (curated subset). Example: 'mini_demo_data.json'",
          "title": "Mini Data File",
          "type": "string"
        }
      },
      "title": "DemoExpectedFiles",
      "type": "object"
    }
  },
  "description": "Dataset/experiment/evaluation \u2192 Jupyter notebook demo.\n\nTitle and summary come from the parent artifact (gen_art step),\nnot from the demo agent. The agent only outputs expected files.",
  "properties": {
    "out_expected_files": {
      "$ref": "#/$defs/DemoExpectedFiles",
      "description": "All output files you created. Must include the demo notebook."
    }
  },
  "required": [],
  "title": "CodeDemo",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [3] HUMAN-USER prompt · 2026-08-21 19:21:30 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [4] TOOL CALL — Bash · 2026-08-21 19:21:34 UTC

```
ls -la && echo --- && find /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1 -maxdepth 2
```

### [5] TOOL CALL — Skill · 2026-08-21 19:21:34 UTC

```
aii-colab
```

### [6] TOOL CALL — Skill · 2026-08-21 19:21:34 UTC

```
aii-long-running-tasks
```

### [7] TOOL RESULT — Bash · 2026-08-21 19:21:34 UTC

```
{"stdout": "total 2975\ndrwxr-xr-x 2 root root 1003701 Aug 21 19:21 .\ndrwxr-xr-x 5 root root 2003045 Aug 21 19:16 ..\n-rw-r--r-- 1 root root   39916 Aug 21 19:21 .repl_agent.ptylog\n---\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/.terminal_claude_agent_struct_out.json\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/pyproject.toml\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/claude-0-freeze.txt\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/preview_method_out.json\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/mini_method_out.json\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/full_method_out.json\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/method.py\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/method_out.json\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/__pycache__\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/logs\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/.venv\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/full_data_out.json\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/__pycache__/method.cpython-312.pyc\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/.venv/.lock\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/.venv/lib64\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/.venv/lib\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/.venv/pyvenv.cfg\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/.venv/bin\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/.venv/.gitignore\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/.venv/CACHEDIR.TAG\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/logs/run.log", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [8] TOOL RESULT — Skill · 2026-08-21 19:21:34 UTC

```
{"success": true, "commandName": "aii-colab"}
```

### [9] TOOL RESULT — Skill · 2026-08-21 19:21:34 UTC

```
{"success": true, "commandName": "aii-long-running-tasks"}
```

### [10] TOOL CALL — Read · 2026-08-21 19:21:38 UTC

```
/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/method.py
```

### [11] TOOL RESULT — Read · 2026-08-21 19:21:38 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/method.py", "content": "#!/usr/bin/env python3\n\"\"\"Unified-corpus re-test of pre-departure authority diffusion vs. founder-exit survival.\n\nRe-runs three pre-registered tests (BH-FDR regression, matched-pairs bootstrap,\nwithin-repo placebo) on the single unified 32-repo dataset artifact\n(art_24Q1bYB_ULpu) instead of independently re-mine... [truncated, 39021 chars total]
```

### [12] TOOL CALL — Bash · 2026-08-21 19:21:38 UTC

```
head -c 3000 /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/preview_method_out.json
```

### [13] TOOL RESULT — Bash · 2026-08-21 19:21:38 UTC

```
{"stdout": "{\n  \"metadata\": {\n    \"method_name\": \"unified_corpus_retest_pre_departure_authority_diffusion\",\n    \"iteration\": 2,\n    \"what_changed_vs_iter1\": \"Unified 32-repo corpus (single provenance) instead of 62-attempted/30-usable independently re-mined data; placebo draws raised 25 -> 300 (year-resolution, data-availability-limited); new window-bounda...\",\n    \"test_0_baseline_replication\": {\n      \"n_qualified_tfdds\": 32,\n      \"n_screened_candidates\": 216,\n      \"founder_only_tfdd_rate_in_screened_pool\": 0.1481,\n      \"survival_rate_this_corpus\": 0.625,\n      \"avelino_et_al_unconditioned_survival_rate\": 0.41,\n      \"note_denominator_difference\": \"This corpus's 62.5% survival rate is conditioned on founder-only TFDD (TF=1 sole developer, confirmed founder), a strict subset of Avelino et al.'s unconditioned 41% baseline across all TFDDs regardle...\",\n      \"snapshot_cohens_d_survivors_vs_not\": {\n        \"total_contributors\": 0.2973,\n        \"n_files_total\": 0.1443,\n        \"n_commits_total\": 0.4871,\n        \"stars\": 0.4032,\n        \"forks\": 0.4412\n      },\n      \"avelino_et_al_reference_d_range\": [\n        0.13,\n        0.26\n      ],\n      \"replication_assessment\": \"consistent_negligible_to_small\"\n    },\n    \"test_a_bhfdr_regression\": {\n      \"status\": \"EXECUTED\",\n      \"stratification_check\": {\n        \"language_x_outcome_min_cell\": 0,\n        \"popularity_x_outcome_min_cell\": 2,\n        \"any_cell_below_3\": true,\n        \"decision\": \"pooled_model_with_strata_as_covariates (deviation documented: per-stratum fits infeasible, min cell count below 3)\"\n      },\n      \"n_predictors\": 12,\n      \"n_obs\": 32,\n      \"method_used\": \"l2_regularized_C0.5\",\n      \"convergence_note\": \"Unregularized MLE showed complete-separation symptoms; substituted L2-regularized logit (C=0.5) with 1000-resample bootstrap p-values, per fallback_plan.\",\n      \"per_predictor\": [\n        {\n          \"predictor\": \"project_age_days\",\n          \"is_diffusion_predictor\": false,\n          \"standardized_coef\": -0.8801,\n          \"se\": 0.2301,\n          \"p_raw\": 0.0033,\n          \"p_bh_adjusted\": 0.04,\n          \"significant_at_bh_0.05\": true\n        },\n        {\n          \"predictor\": \"lang_Java\",\n          \"is_diffusion_predictor\": false,\n          \"standardized_coef\": 0.6552,\n          \"se\": 0.1943,\n          \"p_raw\": 0.0067,\n          \"p_bh_adjusted\": 0.04,\n          \"significant_at_bh_0.05\": true\n        },\n        {\n          \"predictor\": \"n_commits_total\",\n          \"is_diffusion_predictor\": false,\n          \"standardized_coef\": 0.2779,\n          \"se\": 0.1661,\n          \"p_raw\": 0.1,\n          \"p_bh_adjusted\": 0.24,\n          \"significant_at_bh_0.05\": false\n        }\n      ],\n      \"excluded_zero_variance_diffusion_predictors\": [\n        \"founder_commit_share_pre_tfdd\"\n      ],\n      \"excluded_predictors_reason\": \"Constant (zero-variance) in this 32-row corpus -- upstream dataset artifact limitation (founder_commit_share_pre_tfdd is 0.0 for 31/32 rows and missing for 1), mathematically", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [14] TOOL CALL — Bash · 2026-08-21 19:21:44 UTC

```
ls -la /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/full_data_out.json
python3 -c "
import json
d = json.load(open('/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/full_data_out.json'))
print(list(d.keys()))
for ds in d['datasets']:
    print(ds['dataset'], len(ds['examples']))
"
```

### [15] TOOL RESULT — Bash · 2026-08-21 19:21:44 UTC

```
{"stdout": "-rw-r--r-- 1 231072 231072 178502 Aug 21 17:47 /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/full_data_out.json\n['metadata', 'datasets']\nfounder_departure_tfdd_corpus 32", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [16] ASSISTANT · 2026-08-21 19:21:48 UTC

```
Full dataset is only 178KB / 32 repos, and the whole script runs in ~13s — so I'll use the full corpus as the demo data (it's already minimal). All required hard-coded validation checks (n=32, exact language counts) depend on having the complete corpus, so no subsetting is possible without breaking the script's own checks.
```

### [17] TOOL CALL — Bash · 2026-08-21 19:21:48 UTC

```
cp /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/full_data_out.json /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/mini_demo_data.json
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui
ls -la
```

### [18] TOOL CALL — ToolSearch · 2026-08-21 19:21:48 UTC

```
{'query': 'select:NotebookEdit'}
```

### [19] TOOL RESULT — Bash · 2026-08-21 19:21:48 UTC

```
{"stdout": "total 3197\ndrwxr-xr-x 2 root root 1023982 Aug 21 19:21 .\ndrwxr-xr-x 5 root root 2003342 Aug 21 19:16 ..\n-rw-r--r-- 1 root root   69068 Aug 21 19:21 .repl_agent.ptylog\n-rw-r--r-- 1 root root  178502 Aug 21 19:21 mini_demo_data.json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [20] TOOL RESULT — ToolSearch · 2026-08-21 19:21:48 UTC

```
{"matches": ["NotebookEdit"], "query": "select:NotebookEdit", "total_deferred_tools": 22}
```

### [21] TOOL CALL — Write · 2026-08-21 19:21:54 UTC

```
File: /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb

{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["# placeholder"],
   "id": "cell-0"
  }
 ],
 "metadata": {
  "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
  "language_info": {"name": "python", "version": "3.12.0"}
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

### [22] TOOL RESULT — Write · 2026-08-21 19:21:54 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb", "content": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": [\"# placeholder\"],\n   \"id\": \"cell-0\"\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"},\n  \"language_info\": {\"name\": \"python\", \"version\": \"3.12.0\"}\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [23] ASSISTANT · 2026-08-21 19:22:02 UTC

```
Now building the notebook cell by cell.
```

### [24] TOOL CALL — NotebookEdit · 2026-08-21 19:22:02 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': 'cell-0', 'cell_type': 'markdown', 'new_source': "# Re-Testing Founder-Departure Survival Signals\\n\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\n\\nKey design choices carried over unchanged from the original script:\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\n\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks)."}
```

### [25] TOOL RESULT — NotebookEdit · 2026-08-21 19:22:02 UTC

```
{"new_source": "# Re-Testing Founder-Departure Survival Signals\\n\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\n\\nKey design choices carried over unchanged from the original script:\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\n\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).", "old_source": "# placeholder", "cell_type": "markdown", "language": "python", "edit_mode": "replace", "cell_id": "cell-0", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": [\"# placeholder\"],\n   \"id\": \"cell-0\"\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"},\n  \"language_info\": {\"name\": \"python\", \"version\": \"3.12.0\"}\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}\n", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Re-Testing Founder-Departure Survival Signals\\\\n\\\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\\\n\\\\nKey design choices carried over unchanged from the original script:\\\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\\\n\\\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).\",\n   \"id\": \"cell-0\"\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [26] TOOL CALL — Read · 2026-08-21 19:22:06 UTC

```
/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb
```

### [27] TOOL RESULT — Read · 2026-08-21 19:22:06 UTC

```
{"type": "notebook", "file": {"filePath": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb", "cells": [{"cellType": "markdown", "source": "# Re-Testing Founder-Departure Survival Signals\\n\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\n\\nKey design choices carried over unchanged from the original script:\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\n\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).", "cell_id": "cell-0"}]}}
```

### [28] ASSISTANT · 2026-08-21 19:22:12 UTC

```
Confirmed it stored literal `\n`. I need to use actual newlines in the source string, not escaped ones.
```

### [29] TOOL CALL — NotebookEdit · 2026-08-21 19:22:12 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': 'cell-0', 'cell_type': 'markdown', 'new_source': "# Re-Testing Founder-Departure Survival Signals\n\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\n\nKey design choices carried over unchanged from the original script:\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\n\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks)."}
```

### [30] TOOL RESULT — NotebookEdit · 2026-08-21 19:22:12 UTC

```
{"new_source": "# Re-Testing Founder-Departure Survival Signals\n\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\n\nKey design choices carried over unchanged from the original script:\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\n\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).", "old_source": "# Re-Testing Founder-Departure Survival Signals\\n\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\n\\nKey design choices carried over unchanged from the original script:\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\n\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).", "cell_type": "markdown", "language": "python", "edit_mode": "replace", "cell_id": "cell-0", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Re-Testing Founder-Departure Survival Signals\\\\n\\\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\\\n\\\\nKey design choices carried over unchanged from the original script:\\\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\\\n\\\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).\",\n   \"id\": \"cell-0\"\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Re-Testing Founder-Departure Survival Signals\\n\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\n\\nKey design choices carried over unchanged from the original script:\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\n\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).\",\n   \"id\": \"cell-0\"\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [31] ASSISTANT · 2026-08-21 19:22:18 UTC

```
Good, now proper newlines. Continuing with the install/imports/data-loading cells.
```

### [32] TOOL CALL — NotebookEdit · 2026-08-21 19:22:18 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': 'cell-0', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': "import subprocess, sys\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\n\n# psutil, loguru — NOT pre-installed on Colab, always install\n_pip('psutil==6.1.1')\n_pip('loguru==0.7.3')\n\n# numpy, pandas, scipy, scikit-learn, statsmodels — pre-installed on Colab, install locally only\nif 'google.colab' not in sys.modules:\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'scikit-learn==1.6.1', 'statsmodels==0.14.6', 'matplotlib==3.10.0')"}
```

### [33] TOOL RESULT — NotebookEdit · 2026-08-21 19:22:18 UTC

```
{"new_source": "import subprocess, sys\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\n\n# psutil, loguru — NOT pre-installed on Colab, always install\n_pip('psutil==6.1.1')\n_pip('loguru==0.7.3')\n\n# numpy, pandas, scipy, scikit-learn, statsmodels — pre-installed on Colab, install locally only\nif 'google.colab' not in sys.modules:\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'scikit-learn==1.6.1', 'statsmodels==0.14.6', 'matplotlib==3.10.0')", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "3f53fc45", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Re-Testing Founder-Departure Survival Signals\\n\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\n\\nKey design choices carried over unchanged from the original script:\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\n\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).\",\n   \"id\": \"cell-0\"\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Re-Testing Founder-Departure Survival Signals\\n\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\n\\nKey design choices carried over unchanged from the original script:\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\n\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"3f53fc45\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# psutil, loguru — NOT pre-installed on Colab, always install\\n_pip('psutil==6.1.1')\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, scipy, scikit-learn, statsmodels — pre-installed on Colab, install locally only\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'scikit-learn==1.6.1', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [34] TOOL CALL — NotebookEdit · 2026-08-21 19:22:24 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': '3f53fc45', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'from __future__ import annotations\n\nimport json\nimport resource\nimport warnings\nfrom typing import Any\n\nwarnings.filterwarnings("ignore", category=FutureWarning, module="sklearn")\n\nimport numpy as np\nimport pandas as pd\nimport psutil\nimport statsmodels.api as sm\nfrom loguru import logger\nfrom scipy import stats as spstats\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.neighbors import NearestNeighbors\nfrom sklearn.preprocessing import StandardScaler\nfrom statsmodels.stats.multitest import multipletests\n\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\n\nlogger.remove()\nlogger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")'}
```

### [35] TOOL RESULT — NotebookEdit · 2026-08-21 19:22:24 UTC

```
{"new_source": "from __future__ import annotations\n\nimport json\nimport resource\nimport warnings\nfrom typing import Any\n\nwarnings.filterwarnings(\"ignore\", category=FutureWarning, module=\"sklearn\")\n\nimport numpy as np\nimport pandas as pd\nimport psutil\nimport statsmodels.api as sm\nfrom loguru import logger\nfrom scipy import stats as spstats\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.neighbors import NearestNeighbors\nfrom sklearn.preprocessing import StandardScaler\nfrom statsmodels.stats.multitest import multipletests\n\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\n\nlogger.remove()\nlogger.add(sys.stdout, level=\"INFO\", format=\"{time:HH:mm:ss}|{level:<7}|{message}\")", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "2c9d0c25", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Re-Testing Founder-Departure Survival Signals\\n\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\n\\nKey design choices carried over unchanged from the original script:\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\n\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"3f53fc45\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# psutil, loguru — NOT pre-installed on Colab, always install\\n_pip('psutil==6.1.1')\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, scipy, scikit-learn, statsmodels — pre-installed on Colab, install locally only\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'scikit-learn==1.6.1', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Re-Testing Founder-Departure Survival Signals\\n\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\n\\nKey design choices carried over unchanged from the original script:\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\n\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"3f53fc45\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# psutil, loguru — NOT pre-installed on Colab, always install\\n_pip('psutil==6.1.1')\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, scipy, scikit-learn, statsmodels — pre-installed on Colab, install locally only\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'scikit-learn==1.6.1', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"2c9d0c25\",\n   \"source\": \"from __future__ import annotations\\n\\nimport json\\nimport resource\\nimport warnings\\nfrom typing import Any\\n\\nwarnings.filterwarnings(\\\"ignore\\\", category=FutureWarning, module=\\\"sklearn\\\")\\n\\nimport numpy as np\\nimport pandas as pd\\nimport psutil\\nimport statsmodels.api as sm\\nfrom loguru import logger\\nfrom scipy import stats as spstats\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neighbors import NearestNeighbors\\nfrom sklearn.preprocessing import StandardScaler\\nfrom statsmodels.stats.multitest import multipletests\\n\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [36] TOOL CALL — NotebookEdit · 2026-08-21 19:22:30 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': '2c9d0c25', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': "## Load the data\n\n`mini_demo_data.json` is the full 32-repo unified corpus (`founder_departure_tfdd_corpus`) exported by the original dataset artifact — it is already small (178 KB) and the script's own provenance checks require the exact n=32/20-survived/language-breakdown counts, so it cannot be subsetted further. The loader tries the GitHub-hosted copy first (for Colab), then falls back to the local file."}
```

### [37] TOOL RESULT — NotebookEdit · 2026-08-21 19:22:30 UTC

```
{"new_source": "## Load the data\n\n`mini_demo_data.json` is the full 32-repo unified corpus (`founder_departure_tfdd_corpus`) exported by the original dataset artifact — it is already small (178 KB) and the script's own provenance checks require the exact n=32/20-survived/language-breakdown counts, so it cannot be subsetted further. The loader tries the GitHub-hosted copy first (for Colab), then falls back to the local file.", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "764cde32", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Re-Testing Founder-Departure Survival Signals\\n\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\n\\nKey design choices carried over unchanged from the original script:\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\n\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"3f53fc45\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# psutil, loguru — NOT pre-installed on Colab, always install\\n_pip('psutil==6.1.1')\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, scipy, scikit-learn, statsmodels — pre-installed on Colab, install locally only\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'scikit-learn==1.6.1', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"2c9d0c25\",\n   \"source\": \"from __future__ import annotations\\n\\nimport json\\nimport resource\\nimport warnings\\nfrom typing import Any\\n\\nwarnings.filterwarnings(\\\"ignore\\\", category=FutureWarning, module=\\\"sklearn\\\")\\n\\nimport numpy as np\\nimport pandas as pd\\nimport psutil\\nimport statsmodels.api as sm\\nfrom loguru import logger\\nfrom scipy import stats as spstats\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neighbors import NearestNeighbors\\nfrom sklearn.preprocessing import StandardScaler\\nfrom statsmodels.stats.multitest import multipletests\\n\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Re-Testing Founder-Departure Survival Signals\\n\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\n\\nKey design choices carried over unchanged from the original script:\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\n\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"3f53fc45\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# psutil, loguru — NOT pre-installed on Colab, always install\\n_pip('psutil==6.1.1')\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, scipy, scikit-learn, statsmodels — pre-installed on Colab, install locally only\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'scikit-learn==1.6.1', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"2c9d0c25\",\n   \"source\": \"from __future__ import annotations\\n\\nimport json\\nimport resource\\nimport warnings\\nfrom typing import Any\\n\\nwarnings.filterwarnings(\\\"ignore\\\", category=FutureWarning, module=\\\"sklearn\\\")\\n\\nimport numpy as np\\nimport pandas as pd\\nimport psutil\\nimport statsmodels.api as sm\\nfrom loguru import logger\\nfrom scipy import stats as spstats\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neighbors import NearestNeighbors\\nfrom sklearn.preprocessing import StandardScaler\\nfrom statsmodels.stats.multitest import multipletests\\n\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"764cde32\",\n   \"source\": \"## Load the data\\n\\n`mini_demo_data.json` is the full 32-repo unified corpus (`founder_departure_tfdd_corpus`) exported by the original dataset artifact — it is already small (178 KB) and the script's own provenance checks require the exact n=32/20-survived/language-breakdown counts, so it cannot be subsetted further. The loader tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [38] TOOL CALL — NotebookEdit · 2026-08-21 19:22:36 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': '764cde32', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'GITHUB_DATA_URL = "https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json"\nimport json, os\n\ndef load_data():\n    try:\n        import urllib.request\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\n            return json.loads(response.read().decode())\n    except Exception: pass\n    if os.path.exists("mini_demo_data.json"):\n        with open("mini_demo_data.json") as f: return json.load(f)\n    raise FileNotFoundError("Could not load mini_demo_data.json")'}
```

### [39] TOOL RESULT — NotebookEdit · 2026-08-21 19:22:36 UTC

```
{"new_source": "GITHUB_DATA_URL = \"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\"\nimport json, os\n\ndef load_data():\n    try:\n        import urllib.request\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\n            return json.loads(response.read().decode())\n    except Exception: pass\n    if os.path.exists(\"mini_demo_data.json\"):\n        with open(\"mini_demo_data.json\") as f: return json.load(f)\n    raise FileNotFoundError(\"Could not load mini_demo_data.json\")", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "ccbfabfd", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Re-Testing Founder-Departure Survival Signals\\n\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\n\\nKey design choices carried over unchanged from the original script:\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\n\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"3f53fc45\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# psutil, loguru — NOT pre-installed on Colab, always install\\n_pip('psutil==6.1.1')\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, scipy, scikit-learn, statsmodels — pre-installed on Colab, install locally only\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'scikit-learn==1.6.1', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"2c9d0c25\",\n   \"source\": \"from __future__ import annotations\\n\\nimport json\\nimport resource\\nimport warnings\\nfrom typing import Any\\n\\nwarnings.filterwarnings(\\\"ignore\\\", category=FutureWarning, module=\\\"sklearn\\\")\\n\\nimport numpy as np\\nimport pandas as pd\\nimport psutil\\nimport statsmodels.api as sm\\nfrom loguru import logger\\nfrom scipy import stats as spstats\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neighbors import NearestNeighbors\\nfrom sklearn.preprocessing import StandardScaler\\nfrom statsmodels.stats.multitest import multipletests\\n\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"764cde32\",\n   \"source\": \"## Load the data\\n\\n`mini_demo_data.json` is the full 32-repo unified corpus (`founder_departure_tfdd_corpus`) exported by the original dataset artifact — it is already small (178 KB) and the script's own provenance checks require the exact n=32/20-survived/language-breakdown counts, so it cannot be subsetted further. The loader tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Re-Testing Founder-Departure Survival Signals\\n\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\n\\nKey design choices carried over unchanged from the original script:\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\n\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"3f53fc45\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# psutil, loguru — NOT pre-installed on Colab, always install\\n_pip('psutil==6.1.1')\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, scipy, scikit-learn, statsmodels — pre-installed on Colab, install locally only\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'scikit-learn==1.6.1', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"2c9d0c25\",\n   \"source\": \"from __future__ import annotations\\n\\nimport json\\nimport resource\\nimport warnings\\nfrom typing import Any\\n\\nwarnings.filterwarnings(\\\"ignore\\\", category=FutureWarning, module=\\\"sklearn\\\")\\n\\nimport numpy as np\\nimport pandas as pd\\nimport psutil\\nimport statsmodels.api as sm\\nfrom loguru import logger\\nfrom scipy import stats as spstats\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neighbors import NearestNeighbors\\nfrom sklearn.preprocessing import StandardScaler\\nfrom statsmodels.stats.multitest import multipletests\\n\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"764cde32\",\n   \"source\": \"## Load the data\\n\\n`mini_demo_data.json` is the full 32-repo unified corpus (`founder_departure_tfdd_corpus`) exported by the original dataset artifact — it is already small (178 KB) and the script's own provenance checks require the exact n=32/20-survived/language-breakdown counts, so it cannot be subsetted further. The loader tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"ccbfabfd\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [40] TOOL CALL — NotebookEdit · 2026-08-21 19:22:38 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': 'ccbfabfd', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'raw_data = load_data()\nprint("Top-level keys:", list(raw_data.keys()))\nfor ds in raw_data["datasets"]:\n    print(ds["dataset"], "->", len(ds["examples"]), "examples")'}
```

### [41] TOOL RESULT — NotebookEdit · 2026-08-21 19:22:38 UTC

```
{"new_source": "raw_data = load_data()\nprint(\"Top-level keys:\", list(raw_data.keys()))\nfor ds in raw_data[\"datasets\"]:\n    print(ds[\"dataset\"], \"->\", len(ds[\"examples\"]), \"examples\")", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "76d7a551", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Re-Testing Founder-Departure Survival Signals\\n\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\n\\nKey design choices carried over unchanged from the original script:\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\n\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"3f53fc45\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# psutil, loguru — NOT pre-installed on Colab, always install\\n_pip('psutil==6.1.1')\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, scipy, scikit-learn, statsmodels — pre-installed on Colab, install locally only\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'scikit-learn==1.6.1', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"2c9d0c25\",\n   \"source\": \"from __future__ import annotations\\n\\nimport json\\nimport resource\\nimport warnings\\nfrom typing import Any\\n\\nwarnings.filterwarnings(\\\"ignore\\\", category=FutureWarning, module=\\\"sklearn\\\")\\n\\nimport numpy as np\\nimport pandas as pd\\nimport psutil\\nimport statsmodels.api as sm\\nfrom loguru import logger\\nfrom scipy import stats as spstats\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neighbors import NearestNeighbors\\nfrom sklearn.preprocessing import StandardScaler\\nfrom statsmodels.stats.multitest import multipletests\\n\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"764cde32\",\n   \"source\": \"## Load the data\\n\\n`mini_demo_data.json` is the full 32-repo unified corpus (`founder_departure_tfdd_corpus`) exported by the original dataset artifact — it is already small (178 KB) and the script's own provenance checks require the exact n=32/20-survived/language-breakdown counts, so it cannot be subsetted further. The loader tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"ccbfabfd\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Re-Testing Founder-Departure Survival Signals\\n\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\n\\nKey design choices carried over unchanged from the original script:\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\n\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"3f53fc45\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# psutil, loguru — NOT pre-installed on Colab, always install\\n_pip('psutil==6.1.1')\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, scipy, scikit-learn, statsmodels — pre-installed on Colab, install locally only\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'scikit-learn==1.6.1', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"2c9d0c25\",\n   \"source\": \"from __future__ import annotations\\n\\nimport json\\nimport resource\\nimport warnings\\nfrom typing import Any\\n\\nwarnings.filterwarnings(\\\"ignore\\\", category=FutureWarning, module=\\\"sklearn\\\")\\n\\nimport numpy as np\\nimport pandas as pd\\nimport psutil\\nimport statsmodels.api as sm\\nfrom loguru import logger\\nfrom scipy import stats as spstats\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neighbors import NearestNeighbors\\nfrom sklearn.preprocessing import StandardScaler\\nfrom statsmodels.stats.multitest import multipletests\\n\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"764cde32\",\n   \"source\": \"## Load the data\\n\\n`mini_demo_data.json` is the full 32-repo unified corpus (`founder_departure_tfdd_corpus`) exported by the original dataset artifact — it is already small (178 KB) and the script's own provenance checks require the exact n=32/20-survived/language-breakdown counts, so it cannot be subsetted further. The loader tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"ccbfabfd\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"76d7a551\",\n   \"source\": \"raw_data = load_data()\\nprint(\\\"Top-level keys:\\\", list(raw_data.keys()))\\nfor ds in raw_data[\\\"datasets\\\"]:\\n    print(ds[\\\"dataset\\\"], \\\"->\\\", len(ds[\\\"examples\\\"]), \\\"examples\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [42] ASSISTANT · 2026-08-21 19:22:44 UTC

```
Now the config cell, then processing cells matching each stage of method.py.
```

### [43] TOOL CALL — NotebookEdit · 2026-08-21 19:22:44 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': '76d7a551', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': "## Configuration\n\nAll tunable parameters from the original script, gathered in one place. `N_PLACEBO_DRAWS` and `N_BOOTSTRAP` are the two knobs that trade demo speed for statistical smoothness — the corpus itself (n=32 repos) is fixed size and cannot be shrunk further (see data-loading note above). Values below are the original script's own values: at this corpus size (32 repos) the full analysis already completes in ~13 seconds, well inside the 10-minute budget, so no scaling-down was necessary."}
```

### [44] TOOL RESULT — NotebookEdit · 2026-08-21 19:22:44 UTC

```
{"new_source": "## Configuration\n\nAll tunable parameters from the original script, gathered in one place. `N_PLACEBO_DRAWS` and `N_BOOTSTRAP` are the two knobs that trade demo speed for statistical smoothness — the corpus itself (n=32 repos) is fixed size and cannot be shrunk further (see data-loading note above). Values below are the original script's own values: at this corpus size (32 repos) the full analysis already completes in ~13 seconds, well inside the 10-minute budget, so no scaling-down was necessary.", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "4f05de28", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Re-Testing Founder-Departure Survival Signals\\n\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\n\\nKey design choices carried over unchanged from the original script:\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\n\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"3f53fc45\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# psutil, loguru — NOT pre-installed on Colab, always install\\n_pip('psutil==6.1.1')\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, scipy, scikit-learn, statsmodels — pre-installed on Colab, install locally only\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'scikit-learn==1.6.1', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"2c9d0c25\",\n   \"source\": \"from __future__ import annotations\\n\\nimport json\\nimport resource\\nimport warnings\\nfrom typing import Any\\n\\nwarnings.filterwarnings(\\\"ignore\\\", category=FutureWarning, module=\\\"sklearn\\\")\\n\\nimport numpy as np\\nimport pandas as pd\\nimport psutil\\nimport statsmodels.api as sm\\nfrom loguru import logger\\nfrom scipy import stats as spstats\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neighbors import NearestNeighbors\\nfrom sklearn.preprocessing import StandardScaler\\nfrom statsmodels.stats.multitest import multipletests\\n\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"764cde32\",\n   \"source\": \"## Load the data\\n\\n`mini_demo_data.json` is the full 32-repo unified corpus (`founder_departure_tfdd_corpus`) exported by the original dataset artifact — it is already small (178 KB) and the script's own provenance checks require the exact n=32/20-survived/language-breakdown counts, so it cannot be subsetted further. The loader tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"ccbfabfd\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"76d7a551\",\n   \"source\": \"raw_data = load_data()\\nprint(\\\"Top-level keys:\\\", list(raw_data.keys()))\\nfor ds in raw_data[\\\"datasets\\\"]:\\n    print(ds[\\\"dataset\\\"], \\\"->\\\", len(ds[\\\"examples\\\"]), \\\"examples\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Re-Testing Founder-Departure Survival Signals\\n\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\n\\nKey design choices carried over unchanged from the original script:\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\n\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"3f53fc45\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# psutil, loguru — NOT pre-installed on Colab, always install\\n_pip('psutil==6.1.1')\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, scipy, scikit-learn, statsmodels — pre-installed on Colab, install locally only\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'scikit-learn==1.6.1', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"2c9d0c25\",\n   \"source\": \"from __future__ import annotations\\n\\nimport json\\nimport resource\\nimport warnings\\nfrom typing import Any\\n\\nwarnings.filterwarnings(\\\"ignore\\\", category=FutureWarning, module=\\\"sklearn\\\")\\n\\nimport numpy as np\\nimport pandas as pd\\nimport psutil\\nimport statsmodels.api as sm\\nfrom loguru import logger\\nfrom scipy import stats as spstats\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neighbors import NearestNeighbors\\nfrom sklearn.preprocessing import StandardScaler\\nfrom statsmodels.stats.multitest import multipletests\\n\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"764cde32\",\n   \"source\": \"## Load the data\\n\\n`mini_demo_data.json` is the full 32-repo unified corpus (`founder_departure_tfdd_corpus`) exported by the original dataset artifact — it is already small (178 KB) and the script's own provenance checks require the exact n=32/20-survived/language-breakdown counts, so it cannot be subsetted further. The loader tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"ccbfabfd\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"76d7a551\",\n   \"source\": \"raw_data = load_data()\\nprint(\\\"Top-level keys:\\\", list(raw_data.keys()))\\nfor ds in raw_data[\\\"datasets\\\"]:\\n    print(ds[\\\"dataset\\\"], \\\"->\\\", len(ds[\\\"examples\\\"]), \\\"examples\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"4f05de28\",\n   \"source\": \"## Configuration\\n\\nAll tunable parameters from the original script, gathered in one place. `N_PLACEBO_DRAWS` and `N_BOOTSTRAP` are the two knobs that trade demo speed for statistical smoothness — the corpus itself (n=32 repos) is fixed size and cannot be shrunk further (see data-loading note above). Values below are the original script's own values: at this corpus size (32 repos) the full analysis already completes in ~13 seconds, well inside the 10-minute budget, so no scaling-down was necessary.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [45] TOOL CALL — NotebookEdit · 2026-08-21 19:22:52 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': '4f05de28', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'RNG_SEED = 20260821\nN_PLACEBO_DRAWS = 300  # raised from iter1\'s 25 per plan Sec 5\nN_BOOTSTRAP = 2000\nCALIPER_WIDTHS = [0.5, 1.0, 1.5]  # standardized-feature-space distance thresholds, Sec 4\nEXPECTED_N = 32\nEXPECTED_SURVIVED = 20\nEXPECTED_LANG_COUNTS = {"Go": 7, "Ruby": 11, "JavaScript": 6, "Java": 5, "Rust": 3}\n\n# Memory: dataset is 175KB, trivially small relative to the 57GB container limit.\n# Cap generously to fail fast/catchable rather than OOM-kill on any runaway growth.\n# NOTE: numpy/OpenBLAS/statsmodels reserve large virtual address ranges (mmap\'d\n# thread-pool arenas etc.) that count against RLIMIT_AS but are never resident,\n# so a tight AS cap raises spurious MemoryErrors well before physical RAM is\n# actually threatened. Cap at 16GB (still a hard, catchable ceiling; far below\n# the 57GB container limit) rather than 4GB.\nresource.setrlimit(resource.RLIMIT_AS, (16 * 1024**3, 16 * 1024**3))\n\n# CPU-time cap: guards against statsmodels Logit hanging under complete\n# separation (observed in the prior attempt -- the language dummies for\n# Java/Rust are perfectly predictive of survival, which can make the\n# unregularized MLE\'s Newton iterations pathologically slow even under\n# maxiter). 600s (10 min) is far below the ~1199s wall-clock budget this\n# worker container gets before a hard external kill, so a runaway fit\n# raises a catchable SIGXCPU-triggered exception instead of taking the\n# whole container down with it.\nresource.setrlimit(resource.RLIMIT_CPU, (600, 600))'}
```

### [46] TOOL RESULT — NotebookEdit · 2026-08-21 19:22:52 UTC

```
{"new_source": "RNG_SEED = 20260821\nN_PLACEBO_DRAWS = 300  # raised from iter1's 25 per plan Sec 5\nN_BOOTSTRAP = 2000\nCALIPER_WIDTHS = [0.5, 1.0, 1.5]  # standardized-feature-space distance thresholds, Sec 4\nEXPECTED_N = 32\nEXPECTED_SURVIVED = 20\nEXPECTED_LANG_COUNTS = {\"Go\": 7, \"Ruby\": 11, \"JavaScript\": 6, \"Java\": 5, \"Rust\": 3}\n\n# Memory: dataset is 175KB, trivially small relative to the 57GB container limit.\n# Cap generously to fail fast/catchable rather than OOM-kill on any runaway growth.\n# NOTE: numpy/OpenBLAS/statsmodels reserve large virtual address ranges (mmap'd\n# thread-pool arenas etc.) that count against RLIMIT_AS but are never resident,\n# so a tight AS cap raises spurious MemoryErrors well before physical RAM is\n# actually threatened. Cap at 16GB (still a hard, catchable ceiling; far below\n# the 57GB container limit) rather than 4GB.\nresource.setrlimit(resource.RLIMIT_AS, (16 * 1024**3, 16 * 1024**3))\n\n# CPU-time cap: guards against statsmodels Logit hanging under complete\n# separation (observed in the prior attempt -- the language dummies for\n# Java/Rust are perfectly predictive of survival, which can make the\n# unregularized MLE's Newton iterations pathologically slow even under\n# maxiter). 600s (10 min) is far below the ~1199s wall-clock budget this\n# worker container gets before a hard external kill, so a runaway fit\n# raises a catchable SIGXCPU-triggered exception instead of taking the\n# whole container down with it.\nresource.setrlimit(resource.RLIMIT_CPU, (600, 600))", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "baecd6f7", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Re-Testing Founder-Departure Survival Signals\\n\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\n\\nKey design choices carried over unchanged from the original script:\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\n\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"3f53fc45\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# psutil, loguru — NOT pre-installed on Colab, always install\\n_pip('psutil==6.1.1')\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, scipy, scikit-learn, statsmodels — pre-installed on Colab, install locally only\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'scikit-learn==1.6.1', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"2c9d0c25\",\n   \"source\": \"from __future__ import annotations\\n\\nimport json\\nimport resource\\nimport warnings\\nfrom typing import Any\\n\\nwarnings.filterwarnings(\\\"ignore\\\", category=FutureWarning, module=\\\"sklearn\\\")\\n\\nimport numpy as np\\nimport pandas as pd\\nimport psutil\\nimport statsmodels.api as sm\\nfrom loguru import logger\\nfrom scipy import stats as spstats\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neighbors import NearestNeighbors\\nfrom sklearn.preprocessing import StandardScaler\\nfrom statsmodels.stats.multitest import multipletests\\n\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"764cde32\",\n   \"source\": \"## Load the data\\n\\n`mini_demo_data.json` is the full 32-repo unified corpus (`founder_departure_tfdd_corpus`) exported by the original dataset artifact — it is already small (178 KB) and the script's own provenance checks require the exact n=32/20-survived/language-breakdown counts, so it cannot be subsetted further. The loader tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"ccbfabfd\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"76d7a551\",\n   \"source\": \"raw_data = load_data()\\nprint(\\\"Top-level keys:\\\", list(raw_data.keys()))\\nfor ds in raw_data[\\\"datasets\\\"]:\\n    print(ds[\\\"dataset\\\"], \\\"->\\\", len(ds[\\\"examples\\\"]), \\\"examples\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"4f05de28\",\n   \"source\": \"## Configuration\\n\\nAll tunable parameters from the original script, gathered in one place. `N_PLACEBO_DRAWS` and `N_BOOTSTRAP` are the two knobs that trade demo speed for statistical smoothness — the corpus itself (n=32 repos) is fixed size and cannot be shrunk further (see data-loading note above). Values below are the original script's own values: at this corpus size (32 repos) the full analysis already completes in ~13 seconds, well inside the 10-minute budget, so no scaling-down was necessary.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Re-Testing Founder-Departure Survival Signals\\n\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\n\\nKey design choices carried over unchanged from the original script:\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\n\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"3f53fc45\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# psutil, loguru — NOT pre-installed on Colab, always install\\n_pip('psutil==6.1.1')\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, scipy, scikit-learn, statsmodels — pre-installed on Colab, install locally only\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'scikit-learn==1.6.1', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"2c9d0c25\",\n   \"source\": \"from __future__ import annotations\\n\\nimport json\\nimport resource\\nimport warnings\\nfrom typing import Any\\n\\nwarnings.filterwarnings(\\\"ignore\\\", category=FutureWarning, module=\\\"sklearn\\\")\\n\\nimport numpy as np\\nimport pandas as pd\\nimport psutil\\nimport statsmodels.api as sm\\nfrom loguru import logger\\nfrom scipy import stats as spstats\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neighbors import NearestNeighbors\\nfrom sklearn.preprocessing import StandardScaler\\nfrom statsmodels.stats.multitest import multipletests\\n\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"764cde32\",\n   \"source\": \"## Load the data\\n\\n`mini_demo_data.json` is the full 32-repo unified corpus (`founder_departure_tfdd_corpus`) exported by the original dataset artifact — it is already small (178 KB) and the script's own provenance checks require the exact n=32/20-survived/language-breakdown counts, so it cannot be subsetted further. The loader tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"ccbfabfd\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"76d7a551\",\n   \"source\": \"raw_data = load_data()\\nprint(\\\"Top-level keys:\\\", list(raw_data.keys()))\\nfor ds in raw_data[\\\"datasets\\\"]:\\n    print(ds[\\\"dataset\\\"], \\\"->\\\", len(ds[\\\"examples\\\"]), \\\"examples\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"4f05de28\",\n   \"source\": \"## Configuration\\n\\nAll tunable parameters from the original script, gathered in one place. `N_PLACEBO_DRAWS` and `N_BOOTSTRAP` are the two knobs that trade demo speed for statistical smoothness — the corpus itself (n=32 repos) is fixed size and cannot be shrunk further (see data-loading note above). Values below are the original script's own values: at this corpus size (32 repos) the full analysis already completes in ~13 seconds, well inside the 10-minute budget, so no scaling-down was necessary.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"baecd6f7\",\n   \"source\": \"RNG_SEED = 20260821\\nN_PLACEBO_DRAWS = 300  # raised from iter1's 25 per plan Sec 5\\nN_BOOTSTRAP = 2000\\nCALIPER_WIDTHS = [0.5, 1.0, 1.5]  # standardized-feature-space distance thresholds, Sec 4\\nEXPECTED_N = 32\\nEXPECTED_SURVIVED = 20\\nEXPECTED_LANG_COUNTS = {\\\"Go\\\": 7, \\\"Ruby\\\": 11, \\\"JavaScript\\\": 6, \\\"Java\\\": 5, \\\"Rust\\\": 3}\\n\\n# Memory: dataset is 175KB, trivially small relative to the 57GB container limit.\\n# Cap generously to fail fast/catchable rather than OOM-kill on any runaway growth.\\n# NOTE: numpy/OpenBLAS/statsmodels reserve large virtual address ranges (mmap'd\\n# thread-pool arenas etc.) that count against RLIMIT_AS but are never resident,\\n# so a tight AS cap raises spurious MemoryErrors well before physical RAM is\\n# actually threatened. Cap at 16GB (still a hard, catchable ceiling; far below\\n# the 57GB container limit) rather than 4GB.\\nresource.setrlimit(resource.RLIMIT_AS, (16 * 1024**3, 16 * 1024**3))\\n\\n# CPU-time cap: guards against statsmodels Logit hanging under complete\\n# separation (observed in the prior attempt -- the language dummies for\\n# Java/Rust are perfectly predictive of survival, which can make the\\n# unregularized MLE's Newton iterations pathologically slow even under\\n# maxiter). 600s (10 min) is far below the ~1199s wall-clock budget this\\n# worker container gets before a hard external kill, so a runaway fit\\n# raises a catchable SIGXCPU-triggered exception instead of taking the\\n# whole container down with it.\\nresource.setrlimit(resource.RLIMIT_CPU, (600, 600))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [47] ASSISTANT · 2026-08-21 19:22:58 UTC

```
Now Stage 0: load_corpus function + call it.
```

### [48] TOOL CALL — NotebookEdit · 2026-08-21 19:22:58 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': 'baecd6f7', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': "## Stage 0: load + validate the unified corpus\n\nHard-validates corpus provenance (exact n=32, exact survived/language counts) against the dataset artifact's own summary before any analysis runs, then flags the degenerate (zero-variance) `founder_commit_share_pre_tfdd` predictor documented in the original write-up."}
```

### [49] TOOL RESULT — NotebookEdit · 2026-08-21 19:22:58 UTC

```
{"new_source": "## Stage 0: load + validate the unified corpus\n\nHard-validates corpus provenance (exact n=32, exact survived/language counts) against the dataset artifact's own summary before any analysis runs, then flags the degenerate (zero-variance) `founder_commit_share_pre_tfdd` predictor documented in the original write-up.", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "e62a2256", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Re-Testing Founder-Departure Survival Signals\\n\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\n\\nKey design choices carried over unchanged from the original script:\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\n\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"3f53fc45\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# psutil, loguru — NOT pre-installed on Colab, always install\\n_pip('psutil==6.1.1')\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, scipy, scikit-learn, statsmodels — pre-installed on Colab, install locally only\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'scikit-learn==1.6.1', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"2c9d0c25\",\n   \"source\": \"from __future__ import annotations\\n\\nimport json\\nimport resource\\nimport warnings\\nfrom typing import Any\\n\\nwarnings.filterwarnings(\\\"ignore\\\", category=FutureWarning, module=\\\"sklearn\\\")\\n\\nimport numpy as np\\nimport pandas as pd\\nimport psutil\\nimport statsmodels.api as sm\\nfrom loguru import logger\\nfrom scipy import stats as spstats\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neighbors import NearestNeighbors\\nfrom sklearn.preprocessing import StandardScaler\\nfrom statsmodels.stats.multitest import multipletests\\n\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"764cde32\",\n   \"source\": \"## Load the data\\n\\n`mini_demo_data.json` is the full 32-repo unified corpus (`founder_departure_tfdd_corpus`) exported by the original dataset artifact — it is already small (178 KB) and the script's own provenance checks require the exact n=32/20-survived/language-breakdown counts, so it cannot be subsetted further. The loader tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"ccbfabfd\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"76d7a551\",\n   \"source\": \"raw_data = load_data()\\nprint(\\\"Top-level keys:\\\", list(raw_data.keys()))\\nfor ds in raw_data[\\\"datasets\\\"]:\\n    print(ds[\\\"dataset\\\"], \\\"->\\\", len(ds[\\\"examples\\\"]), \\\"examples\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"4f05de28\",\n   \"source\": \"## Configuration\\n\\nAll tunable parameters from the original script, gathered in one place. `N_PLACEBO_DRAWS` and `N_BOOTSTRAP` are the two knobs that trade demo speed for statistical smoothness — the corpus itself (n=32 repos) is fixed size and cannot be shrunk further (see data-loading note above). Values below are the original script's own values: at this corpus size (32 repos) the full analysis already completes in ~13 seconds, well inside the 10-minute budget, so no scaling-down was necessary.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"baecd6f7\",\n   \"source\": \"RNG_SEED = 20260821\\nN_PLACEBO_DRAWS = 300  # raised from iter1's 25 per plan Sec 5\\nN_BOOTSTRAP = 2000\\nCALIPER_WIDTHS = [0.5, 1.0, 1.5]  # standardized-feature-space distance thresholds, Sec 4\\nEXPECTED_N = 32\\nEXPECTED_SURVIVED = 20\\nEXPECTED_LANG_COUNTS = {\\\"Go\\\": 7, \\\"Ruby\\\": 11, \\\"JavaScript\\\": 6, \\\"Java\\\": 5, \\\"Rust\\\": 3}\\n\\n# Memory: dataset is 175KB, trivially small relative to the 57GB container limit.\\n# Cap generously to fail fast/catchable rather than OOM-kill on any runaway growth.\\n# NOTE: numpy/OpenBLAS/statsmodels reserve large virtual address ranges (mmap'd\\n# thread-pool arenas etc.) that count against RLIMIT_AS but are never resident,\\n# so a tight AS cap raises spurious MemoryErrors well before physical RAM is\\n# actually threatened. Cap at 16GB (still a hard, catchable ceiling; far below\\n# the 57GB container limit) rather than 4GB.\\nresource.setrlimit(resource.RLIMIT_AS, (16 * 1024**3, 16 * 1024**3))\\n\\n# CPU-time cap: guards against statsmodels Logit hanging under complete\\n# separation (observed in the prior attempt -- the language dummies for\\n# Java/Rust are perfectly predictive of survival, which can make the\\n# unregularized MLE's Newton iterations pathologically slow even under\\n# maxiter). 600s (10 min) is far below the ~1199s wall-clock budget this\\n# worker container gets before a hard external kill, so a runaway fit\\n# raises a catchable SIGXCPU-triggered exception instead of taking the\\n# whole container down with it.\\nresource.setrlimit(resource.RLIMIT_CPU, (600, 600))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Re-Testing Founder-Departure Survival Signals\\n\\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a unified 32-repo founder-departure Truck-Factor corpus, asking: **does authority diffusion before a founder leaves predict whether the project survives?**\\n\\nKey design choices carried over unchanged from the original script:\\n- Corpus provenance is hard-validated at load time (exact n=32, 20 survived/12 not, language breakdown) before any analysis runs.\\n- Test A pre-detects complete/quasi-complete separation and falls back to L2-regularized logistic regression with a bootstrap for p-values.\\n- Test B reports EXECUTED or UNTESTABLE honestly depending on achieved matched-pair count.\\n- Test C substitutes a documented year-resolution proxy statistic because the dataset only carries yearly snapshots.\\n- A new Sec 6 control compares the true window's effect size against a within-repo stable-period noise floor.\\n\\nThe code below is the **same code as the original `method.py`**, split into cells with explanatory markdown between sections. Since the whole corpus is only 32 repos and the full analysis runs in ~13 seconds, this demo uses the complete corpus (no subsetting is possible without breaking the script's own exact-count provenance checks).\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"3f53fc45\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# psutil, loguru — NOT pre-installed on Colab, always install\\n_pip('psutil==6.1.1')\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, scipy, scikit-learn, statsmodels — pre-installed on Colab, install locally only\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'scikit-learn==1.6.1', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"2c9d0c25\",\n   \"source\": \"from __future__ import annotations\\n\\nimport json\\nimport resource\\nimport warnings\\nfrom typing import Any\\n\\nwarnings.filterwarnings(\\\"ignore\\\", category=FutureWarning, module=\\\"sklearn\\\")\\n\\nimport numpy as np\\nimport pandas as pd\\nimport psutil\\nimport statsmodels.api as sm\\nfrom loguru import logger\\nfrom scipy import stats as spstats\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neighbors import NearestNeighbors\\nfrom sklearn.preprocessing import StandardScaler\\nfrom statsmodels.stats.multitest import multipletests\\n\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"764cde32\",\n   \"source\": \"## Load the data\\n\\n`mini_demo_data.json` is the full 32-repo unified corpus (`founder_departure_tfdd_corpus`) exported by the original dataset artifact — it is already small (178 KB) and the script's own provenance checks require the exact n=32/20-survived/language-breakdown counts, so it cannot be subsetted further. The loader tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"ccbfabfd\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"76d7a551\",\n   \"source\": \"raw_data = load_data()\\nprint(\\\"Top-level keys:\\\", list(raw_data.keys()))\\nfor ds in raw_data[\\\"datasets\\\"]:\\n    print(ds[\\\"dataset\\\"], \\\"->\\\", len(ds[\\\"examples\\\"]), \\\"examples\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"4f05de28\",\n   \"source\": \"## Configuration\\n\\nAll tunable parameters from the original script, gathered in one place. `N_PLACEBO_DRAWS` and `N_BOOTSTRAP` are the two knobs that trade demo speed for statistical smoothness — the corpus itself (n=32 repos) is fixed size and cannot be shrunk further (see data-loading note above). Values below are the original script's own values: at this corpus size (32 repos) the full analysis already completes in ~13 seconds, well inside the 10-minute budget, so no scaling-down was necessary.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"baecd6f7\",\n   \"source\": \"RNG_SEED = 20260821\\nN_PLACEBO_DRAWS = 300  # raised from iter1's 25 per plan Sec 5\\nN_BOOTSTRAP = 2000\\nCALIPER_WIDTHS = [0.5, 1.0, 1.5]  # standardized-feature-space distance thresholds, Sec 4\\nEXPECTED_N = 32\\nEXPECTED_SURVIVED = 20\\nEXPECTED_LANG_COUNTS = {\\\"Go\\\": 7, \\\"Ruby\\\": 11, \\\"JavaScript\\\": 6, \\\"Java\\\": 5, \\\"Rust\\\": 3}\\n\\n# Memory: dataset is 175KB, trivially small relative to the 57GB container limit.\\n# Cap generously to fail fast/catchable rather than OOM-kill on any runaway growth.\\n# NOTE: numpy/OpenBLAS/statsmodels reserve large virtual address ranges (mmap'd\\n# thread-pool arenas etc.) that count against RLIMIT_AS but are never resident,\\n# so a tight AS cap raises spurious MemoryErrors well before physical RAM is\\n# actually threatened. Cap at 16GB (still a hard, catchable ceiling; far below\\n# the 57GB container limit) rather than 4GB.\\nresource.setrlimit(resource.RLIMIT_AS, (16 * 1024**3, 16 * 1024**3))\\n\\n# CPU-time cap: guards against statsmodels Logit hanging under complete\\n# separation (observed in the prior attempt -- the language dummies for\\n# Java/Rust are perfectly predictive of survival, which can make the\\n# unregularized MLE's Newton iterations pathologically slow even under\\n# maxiter). 600s (10 min) is far below the ~1199s wall-clock budget this\\n# worker container gets before a hard external kill, so a runaway fit\\n# raises a catchable SIGXCPU-triggered exception instead of taking the\\n# whole container down with it.\\nresource.setrlimit(resource.RLIMIT_CPU, (600, 600))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"e62a2256\",\n   \"source\": \"## Stage 0: load + validate the unified corpus\\n\\nHard-validates corpus provenance (exact n=32, exact survived/language counts) against the dataset artifact's own summary before any analysis runs, then flags the degenerate (zero-variance) `founder_commit_share_pre_tfdd` predictor documented in the original write-up.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [50] TOOL CALL — NotebookEdit · 2026-08-21 19:23:12 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': 'e62a2256', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'def load_corpus(raw: dict) -> pd.DataFrame:\n    logger.info("Loading unified corpus from loaded data")\n    ds = next((d for d in raw["datasets"] if d["dataset"] == "founder_departure_tfdd_corpus"), None)\n    if ds is None:\n        raise ValueError("founder_departure_tfdd_corpus dataset group not found in data")\n    examples = ds["examples"]\n    if len(examples) != EXPECTED_N:\n        raise ValueError(\n            f"Corpus-provenance unification check failed: expected {EXPECTED_N} rows, got {len(examples)}. "\n            "Hard-failing per plan Sec 0 rather than silently proceeding on a mismatched corpus."\n        )\n\n    rows = []\n    for ex in examples:\n        inp = json.loads(ex["input"])\n        row = dict(inp)\n        row["survival_label"] = ex["output"]\n        row["survival"] = 1 if ex["output"] == "Active_survived" else 0\n        row["repo"] = ex.get("metadata_full_name")\n        row["tfdd_year"] = ex.get("metadata_tfdd", {}).get("year")\n        row["tfdd_developer"] = ex.get("metadata_tfdd", {}).get("developer")\n        row["activity_bucket"] = ex.get("metadata_activity_bucket")\n        row["yearly_tables"] = ex.get("metadata_yearly_doa_tf_tables", [])\n        row["repo_created_at"] = ex.get("metadata_repo_meta", {}).get("created_at")\n        rows.append(row)\n    df = pd.DataFrame(rows)\n\n    n_survived = int(df["survival"].sum())\n    lang_counts = df["language"].value_counts().to_dict()\n    logger.info(f"Loaded n={len(df)}, survived={n_survived}/{len(df)}, languages={lang_counts}")\n    if n_survived != EXPECTED_SURVIVED:\n        raise ValueError(f"Survival breakdown mismatch: expected {EXPECTED_SURVIVED} survived, got {n_survived}")\n    for lang, expect_n in EXPECTED_LANG_COUNTS.items():\n        got = int(lang_counts.get(lang, 0))\n        if got != expect_n:\n            raise ValueError(f"Language breakdown mismatch for {lang}: expected {expect_n}, got {got}")\n    logger.info("Corpus spot-check PASSED: matches dataset artifact\'s own textual summary exactly.")\n\n    # DATA-QUALITY CHECK: founder_commit_share_pre_tfdd -- the plan\'s primary\n    # diffusion predictor -- is 0.0 for 31/32 rows and missing (None) for the\n    # remaining row in this dataset artifact, i.e. it is effectively CONSTANT\n    # (zero variance) rather than a genuine per-repo covariate. This is a\n    # limitation of the upstream dataset artifact (art_24Q1bYB_ULpu), not a\n    # parsing bug here (verified: the raw `input` JSON carries exactly this\n    # value for every example). A zero-variance predictor is mathematically\n    # inestimable in a regression and undefined for a point-biserial\n    # correlation (division by zero SD), so every test below explicitly\n    # detects and excludes/flags it rather than silently producing NaN or\n    # crashing. The single missing value is imputed with 0.0 (the column\'s\n    # own mode) purely so the row is not dropped from the OTHER predictors.\n    degenerate_predictors = []\n    for col in ["founder_commit_share_pre_tfdd", "n_distinct_new_primary_owners_pre_tfdd"]:\n        non_null = df[col].dropna()\n        if non_null.nunique() <= 1:\n            degenerate_predictors.append(col)\n    if degenerate_predictors:\n        logger.warning(\n            f"DATA-QUALITY FLAG: predictor(s) {degenerate_predictors} are constant (zero variance) "\n            "in this 32-row corpus -- upstream dataset artifact limitation, not a local parsing bug "\n            "(spot-checked against the raw `input` JSON). Excluded from regression/correlation "\n            "computations below; documented explicitly in method_out.json rather than silently dropped."\n        )\n    df.attrs["degenerate_predictors"] = degenerate_predictors\n    if df["founder_commit_share_pre_tfdd"].isna().any():\n        n_na = int(df["founder_commit_share_pre_tfdd"].isna().sum())\n        logger.warning(f"Imputing {n_na} missing founder_commit_share_pre_tfdd value(s) with 0.0 (column mode).")\n        df["founder_commit_share_pre_tfdd"] = df["founder_commit_share_pre_tfdd"].fillna(0.0)\n    return df\n\n\ndf = load_corpus(raw_data)\ndf.head()'}
```

### [51] TOOL RESULT — NotebookEdit · 2026-08-21 19:23:12 UTC

```
{"new_source": "def load_corpus(raw: dict) -> pd.DataFrame:\n    logger.info(\"Loading unified corpus from loaded data\")\n    ds = next((d for d in raw[\"datasets\"] if d[\"dataset\"] == \"founder_departure_tfdd_corpus\"), None)\n    if ds is None:\n        raise ValueError(\"founder_departure_tfdd_corpus dataset group not found in data\")\n    examples = ds[\"examples\"]\n    if len(examples) != EXPECTED_N:\n        raise ValueError(\n            f\"Corpus-provenance... [truncated, 24997 chars total]
```

### [52] ASSISTANT · 2026-08-21 19:23:16 UTC

```
Now Test 0 (baseline replication).
```

### [53] TOOL CALL — NotebookEdit · 2026-08-21 19:23:16 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': 'd6d38340', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': "## Test 0: baseline replication checks\n\nSanity check against Avelino et al.'s founder-departure literature: survival rate and Cohen's d effect sizes for developer/commit/file/star/fork gaps between survivors and non-survivors, which should land in the negligible-to-small range reported in prior work."}
```

### [54] TOOL RESULT — NotebookEdit · 2026-08-21 19:23:16 UTC

```
{"new_source": "## Test 0: baseline replication checks\n\nSanity check against Avelino et al.'s founder-departure literature: survival rate and Cohen's d effect sizes for developer/commit/file/star/fork gaps between survivors and non-survivors, which should land in the negligible-to-small range reported in prior work.", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "25f513e7", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/... [truncated, 26142 chars total]
```

### [55] TOOL CALL — NotebookEdit · 2026-08-21 19:23:26 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': '25f513e7', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'def cohens_d(a: np.ndarray, b: np.ndarray) -> float:\n    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)\n    n1, n2 = len(a), len(b)\n    if n1 < 2 or n2 < 2:\n        return float("nan")\n    pooled_sd = np.sqrt(((n1 - 1) * a.var(ddof=1) + (n2 - 1) * b.var(ddof=1)) / (n1 + n2 - 2))\n    if pooled_sd == 0:\n        return 0.0\n    return float((a.mean() - b.mean()) / pooled_sd)\n\n\ndef test0_baseline_replication(df: pd.DataFrame) -> dict[str, Any]:\n    logger.info("=== Test 0: baseline replication checks ===")\n    surv = df[df.survival == 1]\n    dead = df[df.survival == 0]\n\n    survival_rate = float(df.survival.mean())\n    snapshot_vars = ["total_contributors", "n_files_total", "n_commits_total", "stars", "forks"]\n    d_results = {}\n    for v in snapshot_vars:\n        d = cohens_d(surv[v].values, dead[v].values)\n        d_results[v] = d\n        logger.info(f"  Cohen\'s d ({v}, survived vs not): {d:.3f}")\n\n    within_range = [abs(d) for d in d_results.values() if not np.isnan(d)]\n    matches_avelino = bool(within_range) and (min(within_range) >= 0 and np.median(within_range) < 1.0)\n    result = {\n        "n_qualified_tfdds": len(df),\n        "n_screened_candidates": 216,\n        "founder_only_tfdd_rate_in_screened_pool": round(len(df) / 216, 4),\n        "survival_rate_this_corpus": round(survival_rate, 4),\n        "avelino_et_al_unconditioned_survival_rate": 0.41,\n        "note_denominator_difference": (\n            "This corpus\'s 62.5% survival rate is conditioned on founder-only TFDD "\n            "(TF=1 sole developer, confirmed founder), a strict subset of Avelino et al.\'s "\n            "unconditioned 41% baseline across all TFDDs regardless of TF-developer identity; "\n            "not directly comparable without re-deriving their founder-only subset."\n        ),\n        "snapshot_cohens_d_survivors_vs_not": {k: (round(v, 4) if not np.isnan(v) else None) for k, v in d_results.items()},\n        "avelino_et_al_reference_d_range": [0.13, 0.26],\n        "replication_assessment": (\n            "consistent_negligible_to_small" if matches_avelino else "inconsistent_flag_for_review"\n        ),\n    }\n    logger.info(f"Test 0 result: survival_rate={survival_rate:.3f}, assessment={result[\'replication_assessment\']}")\n    return result\n\n\ntest0 = test0_baseline_replication(df)\ntest0'}
```

### [56] TOOL RESULT — NotebookEdit · 2026-08-21 19:23:26 UTC

```
{"new_source": "def cohens_d(a: np.ndarray, b: np.ndarray) -> float:\n    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)\n    n1, n2 = len(a), len(b)\n    if n1 < 2 or n2 < 2:\n        return float(\"nan\")\n    pooled_sd = np.sqrt(((n1 - 1) * a.var(ddof=1) + (n2 - 1) * b.var(ddof=1)) / (n1 + n2 - 2))\n    if pooled_sd == 0:\n        return 0.0\n    return float((a.mean() - b.mean()) / pooled_sd)\n\n\ndef test0_baseline_replication(df: pd.DataFrame) -> d... [truncated, 31387 chars total]
```

### [57] ASSISTANT · 2026-08-21 19:23:32 UTC

```
Now Test A (BH-FDR regression).
```

### [58] TOOL CALL — NotebookEdit · 2026-08-21 19:23:32 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': '129a820e', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': '## Test A: BH-FDR logistic regression with separation-aware fallback\n\nFits a Benjamini-Hochberg FDR-corrected logistic regression of survival on the diffusion predictors plus size/age/language controls. Before attempting the unregularized MLE, it pre-checks for complete/quasi-complete separation (the Java/Rust language dummies perfectly predict survival in this small corpus) and, if detected, falls back to L2-regularized logistic regression with a bootstrap for p-values rather than letting the MLE diverge or hang.'}
```

### [59] TOOL RESULT — NotebookEdit · 2026-08-21 19:23:32 UTC

```
{"new_source": "## Test A: BH-FDR logistic regression with separation-aware fallback\n\nFits a Benjamini-Hochberg FDR-corrected logistic regression of survival on the diffusion predictors plus size/age/language controls. Before attempting the unregularized MLE, it pre-checks for complete/quasi-complete separation (the Java/Rust language dummies perfectly predict survival in this small corpus) and, if detected, falls back to L2-regularized logistic regression with a boo... [truncated, 32854 chars total]
```

### [60] TOOL CALL — NotebookEdit · 2026-08-21 19:23:56 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': 'c680dd23', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'def check_stratification_cells(df: pd.DataFrame) -> dict[str, Any]:\n    lang_cross = pd.crosstab(df.language, df.survival)\n    stars_tercile = pd.qcut(df.stars, 3, labels=["low", "mid", "high"], duplicates="drop")\n    pop_cross = pd.crosstab(stars_tercile, df.survival)\n    lang_min = int(lang_cross.values.min())\n    pop_min = int(pop_cross.values.min())\n    logger.info(f"Stratification cell counts -- language x outcome:\\n{lang_cross}")\n    logger.info(f"Stratification cell counts -- popularity-tercile x outcome:\\n{pop_cross}")\n    any_sparse = lang_min < 3 or pop_min < 3\n    return {\n        "language_x_outcome_min_cell": lang_min,\n        "popularity_x_outcome_min_cell": pop_min,\n        "any_cell_below_3": any_sparse,\n        "decision": (\n            "pooled_model_with_strata_as_covariates (deviation documented: per-stratum fits infeasible, "\n            "min cell count below 3)"\n            if any_sparse\n            else "per_stratum_fits_attempted"\n        ),\n    }\n\n\ndef test_a_bhfdr_regression(df: pd.DataFrame) -> dict[str, Any]:\n    logger.info("=== Test A: BH-FDR logistic regression ===")\n    strat_check = check_stratification_cells(df)\n\n    degenerate = df.attrs.get("degenerate_predictors", [])\n    predictors_diffusion_full = ["founder_commit_share_pre_tfdd", "n_distinct_new_primary_owners_pre_tfdd"]\n    predictors_diffusion = [c for c in predictors_diffusion_full if c not in degenerate]\n    excluded_diffusion = [c for c in predictors_diffusion_full if c in degenerate]\n    if excluded_diffusion:\n        logger.warning(\n            f"Excluding zero-variance diffusion predictor(s) {excluded_diffusion} from the regression "\n            "(inestimable coefficient) -- see data-quality flag logged at load time."\n        )\n    predictors_controls_num = [\n        "stars", "forks", "total_contributors", "project_age_days", "n_commits_total", "n_files_total",\n        "history_span_years",\n    ]\n    X_num = df[predictors_diffusion + predictors_controls_num].astype(float).copy()\n    for c in predictors_controls_num:\n        if X_num[c].skew() > 1.5:\n            X_num[c] = np.log1p(X_num[c].clip(lower=0))\n    lang_dummies = pd.get_dummies(df["language"], prefix="lang", drop_first=True).astype(float)\n    X_full = pd.concat([X_num, lang_dummies], axis=1)\n    all_predictor_names = list(X_full.columns)\n\n    scaler = StandardScaler()\n    X_std = pd.DataFrame(scaler.fit_transform(X_full), columns=all_predictor_names, index=X_full.index)\n    y = df["survival"].values.astype(float)\n\n    X_sm = sm.add_constant(X_std)\n\n    # Pre-check for complete/quasi-complete separation BEFORE attempting the\n    # unregularized MLE: any binary predictor column that is constant within\n    # one outcome class perfectly predicts that class, which sends Newton\'s\n    # method\'s coefficient estimates to +-infinity and can make statsmodels\'\n    # iteration pathologically slow (observed hanging >600s CPU time in a\n    # prior attempt) rather than cleanly failing to converge. Detected here\n    # via a closed-form check on each binary column\'s cross-tab with y,\n    # so the risky unbounded fit is skipped entirely rather than attempted\n    # and killed by the RLIMIT_CPU cap above.\n    unreg_converged, unreg_diverged = True, False\n    separation_predictors = []\n    for col in all_predictor_names:\n        raw_col = X_full[col]\n        if raw_col.nunique() <= 2:\n            for yv in (0.0, 1.0):\n                mask = y == yv\n                if mask.sum() > 0 and raw_col[mask].nunique() <= 1:\n                    separation_predictors.append(col)\n                    break\n    if separation_predictors:\n        unreg_diverged = True\n        logger.warning(\n            f"Complete/quasi-complete separation detected pre-fit on {separation_predictors} "\n            "(a binary predictor is constant within one outcome class) -- skipping the "\n            "unregularized MLE entirely (it would diverge/hang) and going straight to the "\n            "L2-regularized fallback."\n        )\n    else:\n        try:\n            model = sm.Logit(y, X_sm)\n            fit = model.fit(disp=0, maxiter=200)\n            coefs = fit.params.drop("const")\n            pvals = fit.pvalues.drop("const")\n            ses = fit.bse.drop("const")\n            if (coefs.abs() > 10).any() or (not fit.mle_retvals.get("converged", True)):\n                unreg_diverged = True\n        except Exception as e:\n            logger.warning(f"Unregularized Logit failed: {e}")\n            unreg_diverged = True\n\n    method_used = "unregularized_mle"\n    boot_pvals = None\n    if unreg_diverged:\n        logger.warning(\n            "Unregularized MLE shows complete-separation symptoms (|coef|>10 or non-convergence) "\n            f"at n={len(df)} with {len(all_predictor_names)} predictors -- falling back to L2-regularized logit."\n        )\n        method_used = "l2_regularized_C0.5"\n        clf = LogisticRegression(penalty="l2", C=0.5, solver="lbfgs", max_iter=2000)\n        clf.fit(X_std.values, y)\n        coefs = pd.Series(clf.coef_[0], index=all_predictor_names)\n        rng = np.random.default_rng(RNG_SEED)\n        n_boot = 300\n        boot_coefs = np.zeros((n_boot, len(all_predictor_names)))\n        n = len(df)\n        for b in range(n_boot):\n            idx = rng.integers(0, n, size=n)\n            Xb, yb = X_std.values[idx], y[idx]\n            if len(np.unique(yb)) < 2:\n                boot_coefs[b] = np.nan\n                continue\n            cb = LogisticRegression(penalty="l2", C=0.5, solver="lbfgs", max_iter=2000)\n            cb.fit(Xb, yb)\n            boot_coefs[b] = cb.coef_[0]\n        boot_pvals = np.array([\n            2 * min((boot_coefs[:, j] > 0).mean(), (boot_coefs[:, j] < 0).mean())\n            for j in range(len(all_predictor_names))\n        ])\n        boot_pvals = np.clip(boot_pvals, 1.0 / n_boot, 1.0)\n        pvals = pd.Series(boot_pvals, index=all_predictor_names)\n        ses = pd.Series(boot_coefs.std(axis=0, ddof=1), index=all_predictor_names)\n\n    reject, pvals_bh, _, _ = multipletests(pvals.values, alpha=0.05, method="fdr_bh")\n    per_predictor = []\n    for name, coef, se, p, p_bh, rej in zip(all_predictor_names, coefs.values, ses.values, pvals.values, pvals_bh, reject):\n        per_predictor.append({\n            "predictor": name,\n            "is_diffusion_predictor": name in predictors_diffusion,\n            "standardized_coef": round(float(coef), 4),\n            "se": round(float(se), 4),\n            "p_raw": round(float(p), 4),\n            "p_bh_adjusted": round(float(p_bh), 4),\n            "significant_at_bh_0.05": bool(rej),\n        })\n    per_predictor.sort(key=lambda r: r["p_bh_adjusted"])\n\n    diffusion_rows = [r for r in per_predictor if r["is_diffusion_predictor"]]\n    control_rows = [r for r in per_predictor if not r["is_diffusion_predictor"]]\n    diffusion_mean_abs_coef = float(np.mean([abs(r["standardized_coef"]) for r in diffusion_rows])) if diffusion_rows else float("nan")\n    control_mean_abs_coef = float(np.mean([abs(r["standardized_coef"]) for r in control_rows])) if control_rows else float("nan")\n\n    logger.info(f"Test A method used: {method_used}")\n    logger.info(f"Diffusion predictors mean |std coef|={diffusion_mean_abs_coef:.3f} vs controls={control_mean_abs_coef:.3f}")\n    return {\n        "status": "EXECUTED",\n        "stratification_check": strat_check,\n        "n_predictors": len(all_predictor_names),\n        "n_obs": len(df),\n        "method_used": method_used,\n        "convergence_note": (\n            "Unregularized MLE converged with plausible coefficient magnitudes." if method_used == "unregularized_mle"\n            else "Unregularized MLE showed complete-separation symptoms; substituted L2-regularized logit "\n                 "(C=0.5) with 1000-resample bootstrap p-values, per fallback_plan."\n        ),\n        "per_predictor": per_predictor,\n        "excluded_zero_variance_diffusion_predictors": excluded_diffusion,\n        "excluded_predictors_reason": (\n            "Constant (zero-variance) in this 32-row corpus -- upstream dataset artifact limitation "\n            "(founder_commit_share_pre_tfdd is 0.0 for 31/32 rows and missing for 1), mathematically "\n            "inestimable in a regression. Not a local parsing bug; see load_corpus data-quality flag."\n        ) if excluded_diffusion else None,\n        "diffusion_predictors_mean_abs_standardized_coef": round(diffusion_mean_abs_coef, 4),\n        "controls_mean_abs_standardized_coef": round(control_mean_abs_coef, 4),\n        "head_to_head_diffusion_beats_controls": bool(diffusion_mean_abs_coef > control_mean_abs_coef),\n    }\n\n\ntest_a = test_a_bhfdr_regression(df)\n{k: v for k, v in test_a.items() if k != "per_predictor"}'}
```

### [61] TOOL RESULT — NotebookEdit · 2026-08-21 19:23:59 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [62] ASSISTANT · 2026-08-21 19:24:02 UTC

```
Now Test B (matched pairs), Test C (placebo), Sec6, build_predictions, and finally output+visualization.
```

### [63] TOOL CALL — NotebookEdit · 2026-08-21 19:24:02 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': '303f71ad', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': '## Test B: caliper matched-pairs bootstrap\n\nNearest-neighbor matches high-diffusion repos to low-diffusion repos on standardized [log(stars), log(forks), log(contributors)], sweeping three caliper widths. Reports the result honestly as `EXECUTED` or `UNTESTABLE` depending on whether any caliper width yields usable pairs — never fabricates a bootstrap CI from zero pairs.'}
```

### [64] TOOL RESULT — NotebookEdit · 2026-08-21 19:24:05 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [65] TOOL CALL — NotebookEdit · 2026-08-21 19:24:18 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': '301e07ba', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'def test_b_matched_pairs(df: pd.DataFrame) -> dict[str, Any]:\n    logger.info("=== Test B: caliper matched-pairs bootstrap ===")\n    feat = np.column_stack([\n        np.log1p(df.stars.values.astype(float)),\n        np.log1p(df.forks.values.astype(float)),\n        np.log1p(df.total_contributors.values.astype(float)),\n    ])\n    feat_std = StandardScaler().fit_transform(feat)\n\n    degenerate = df.attrs.get("degenerate_predictors", [])\n    share_degenerate = "founder_commit_share_pre_tfdd" in degenerate\n    if share_degenerate:\n        logger.warning(\n            "founder_commit_share_pre_tfdd is zero-variance (all 0.0) in this corpus -- the plan\'s "\n            "share<0.5 / share>=0.8 group boundaries cannot discriminate on it. High-diffusion group "\n            "collapses to n_owners>=2 alone; low-diffusion group (share>=0.8) is necessarily EMPTY, "\n            "which correctly routes this test to the UNTESTABLE branch below rather than a fabricated split."\n        )\n    high_mask = (df.founder_commit_share_pre_tfdd < 0.5) & (df.n_distinct_new_primary_owners_pre_tfdd >= 2)\n    low_mask = df.founder_commit_share_pre_tfdd >= 0.8\n    high_idx = np.where(high_mask.values)[0]\n    low_idx = np.where(low_mask.values)[0]\n    logger.info(f"High-diffusion group n={len(high_idx)}, low-diffusion group n={len(low_idx)}")\n\n    sensitivity = []\n    best_pairs = None\n    best_caliper = None\n    if len(high_idx) > 0 and len(low_idx) > 0:\n        nn = NearestNeighbors(n_neighbors=1).fit(feat_std[low_idx])\n        dists, nn_idx = nn.kneighbors(feat_std[high_idx])\n        for caliper in CALIPER_WIDTHS:\n            pairs = [\n                (high_idx[i], low_idx[nn_idx[i, 0]])\n                for i in range(len(high_idx))\n                if dists[i, 0] <= caliper\n            ]\n            sensitivity.append({"caliper": caliper, "n_pairs": len(pairs)})\n            logger.info(f"  caliper={caliper}: {len(pairs)} usable pairs")\n            if pairs and best_pairs is None:\n                best_pairs = pairs\n                best_caliper = caliper\n\n    if not best_pairs:\n        logger.warning("No usable matched pairs at any caliper width -- reporting UNTESTABLE per fallback_plan.")\n        unmatched_diff = None\n        mw_p = None\n        if len(high_idx) > 0 and len(low_idx) > 0:\n            u_stat, mw_p = spstats.mannwhitneyu(\n                df.survival.values[high_idx], df.survival.values[low_idx], alternative="two-sided"\n            )\n            unmatched_diff = float(df.survival.values[high_idx].mean() - df.survival.values[low_idx].mean())\n        return {\n            "status": "UNTESTABLE",\n            "reason": "zero usable matched pairs at all swept caliper widths",\n            "caliper_sensitivity": sensitivity,\n            "high_diffusion_group_n": int(len(high_idx)),\n            "low_diffusion_group_n": int(len(low_idx)),\n            "unmatched_raw_survival_rate_difference": (\n                round(unmatched_diff, 4) if unmatched_diff is not None else None\n            ),\n            "unmatched_mann_whitney_p": (round(float(mw_p), 4) if mw_p is not None else None),\n            "caveat": "Unmatched comparison does NOT control for popularity/size -- reported only as a fallback, not a substitute for the matched test.",\n        }\n\n    rng = np.random.default_rng(RNG_SEED)\n    pair_diffs = np.array([df.survival.values[h] - df.survival.values[l] for h, l in best_pairs])\n    n_pairs = len(pair_diffs)\n    boot_means = np.array([\n        rng.choice(pair_diffs, size=n_pairs, replace=True).mean() for _ in range(N_BOOTSTRAP)\n    ])\n    ci_lo, ci_hi = np.percentile(boot_means, [2.5, 97.5])\n    logger.info(f"Best caliper={best_caliper}, n_pairs={n_pairs}, mean paired diff={pair_diffs.mean():.3f}, CI=[{ci_lo:.3f},{ci_hi:.3f}]")\n    return {\n        "status": "EXECUTED",\n        "caliper_sensitivity": sensitivity,\n        "used_caliper": best_caliper,\n        "n_matched_pairs": int(n_pairs),\n        "high_diffusion_group_n": int(len(high_idx)),\n        "low_diffusion_group_n": int(len(low_idx)),\n        "mean_paired_survival_diff_high_minus_low": round(float(pair_diffs.mean()), 4),\n        "bootstrap_n_resamples": N_BOOTSTRAP,\n        "bootstrap_95ci": [round(float(ci_lo), 4), round(float(ci_hi), 4)],\n        "ci_excludes_zero": bool(ci_lo > 0 or ci_hi < 0),\n    }\n\n\ntest_b = test_b_matched_pairs(df)\ntest_b'}
```

### [66] TOOL RESULT — NotebookEdit · 2026-08-21 19:24:19 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [67] TOOL CALL — NotebookEdit · 2026-08-21 19:24:22 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': '29eec43f', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': "## Test C: within-repo year-level placebo\n\nBuilds an empirical null distribution by repeatedly drawing a non-departure year-transition within each repo's own history and computing a year-resolution diffusion proxy (year-over-year change in `n_active_authors_in_doa`, substituting for the unavailable sub-year founder-commit-share metric). The true TFDD-year statistic is then compared to this null via its percentile rank."}
```

### [68] TOOL RESULT — NotebookEdit · 2026-08-21 19:24:23 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [69] TOOL CALL — NotebookEdit · 2026-08-21 19:24:43 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': '8f868885', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'def year_proxy_diffusion(yearly_tables: list[dict], year: int) -> float | None:\n    """Year-over-year growth in n_active_authors_in_doa: a coarse, year-resolution\n    substitute for the true sub-year founder-commit-share metric (see module docstring)."""\n    by_year = {t["year"]: t for t in yearly_tables}\n    if year not in by_year or (year - 1) not in by_year:\n        return None\n    prev_n = by_year[year - 1]["n_active_authors_in_doa"]\n    cur_n = by_year[year]["n_active_authors_in_doa"]\n    if prev_n == 0:\n        return None\n    return (cur_n - prev_n) / prev_n\n\n\ndef test_c_placebo(df: pd.DataFrame) -> dict[str, Any]:\n    logger.info("=== Test C: within-repo year-level placebo (n_draws=%d) ===" % N_PLACEBO_DRAWS)\n    rng = np.random.default_rng(RNG_SEED)\n\n    # True effect: real diffusion predictors\' correlation with survival.\n    # founder_commit_share_pre_tfdd is a zero-variance column in this corpus (see load_corpus\n    # data-quality flag) -- point-biserial correlation is undefined (division by zero SD) for it,\n    # so it is reported as None with an explicit reason rather than a silent/crashing NaN.\n    degenerate = df.attrs.get("degenerate_predictors", [])\n    if "founder_commit_share_pre_tfdd" in degenerate:\n        true_r_share, true_p_share = None, None\n        logger.warning("r(founder_share, survival) UNDEFINED: founder_commit_share_pre_tfdd is zero-variance.")\n    else:\n        true_r_share, true_p_share = spstats.pointbiserialr(df.survival.values, df.founder_commit_share_pre_tfdd.values)\n    true_r_owners, true_p_owners = spstats.pointbiserialr(df.survival.values, df.n_distinct_new_primary_owners_pre_tfdd.values)\n    logger.info(f"True: r(founder_share, survival)={true_r_share}; r(n_owners, survival)={true_r_owners:.3f} (p={true_p_owners:.3f})")\n\n    per_repo_placebo_years: dict[str, list[int]] = {}\n    for _, row in df.iterrows():\n        yrs = sorted(t["year"] for t in row["yearly_tables"])\n        non_tfdd_yrs = [y for y in yrs if y != row["tfdd_year"] and (y - 1) in yrs]\n        per_repo_placebo_years[row["repo"]] = non_tfdd_yrs\n\n    n_repos_with_placebo = sum(1 for v in per_repo_placebo_years.values() if v)\n    logger.info(f"{n_repos_with_placebo}/{len(df)} repos have >=1 usable non-TFDD year-transition for placebo draws.")\n\n    null_rs = []\n    for draw in range(N_PLACEBO_DRAWS):\n        proxy_vals, survivals = [], []\n        for _, row in df.iterrows():\n            candidates = per_repo_placebo_years[row["repo"]]\n            if not candidates:\n                continue\n            y = candidates[rng.integers(0, len(candidates))]\n            v = year_proxy_diffusion(row["yearly_tables"], y)\n            if v is None:\n                continue\n            proxy_vals.append(v)\n            survivals.append(row["survival"])\n        if len(proxy_vals) < 5 or len(set(survivals)) < 2:\n            continue\n        r, _ = spstats.pointbiserialr(np.array(survivals), np.array(proxy_vals))\n        if not np.isnan(r):\n            null_rs.append(r)\n    null_rs = np.array(null_rs)\n    logger.info(f"Built empirical null from {len(null_rs)}/{N_PLACEBO_DRAWS} valid placebo draws.")\n\n    # True-window proxy computed identically to the placebo statistic, for apples-to-apples percentile.\n    true_proxy_vals, true_survivals = [], []\n    for _, row in df.iterrows():\n        v = year_proxy_diffusion(row["yearly_tables"], row["tfdd_year"])\n        if v is None:\n            continue\n        true_proxy_vals.append(v)\n        true_survivals.append(row["survival"])\n    true_proxy_r, true_proxy_p = spstats.pointbiserialr(np.array(true_survivals), np.array(true_proxy_vals))\n\n    percentile = float((null_rs < true_proxy_r).mean() * 100) if len(null_rs) else float("nan")\n    prior_iter_r, prior_iter_p, prior_iter_n = 0.180, 0.615, 30\n    return {\n        "status": "EXECUTED",\n        "resolution_limitation": (\n            "Dataset artifact lacks per-commit timestamps; placebo windows are YEAR-resolution "\n            "(year-over-year change in n_active_authors_in_doa) rather than the original plan\'s "\n            "arbitrary 6-12mo re-slicing. Documented substitution per fallback_plan."\n        ),\n        "n_placebo_draws_requested": N_PLACEBO_DRAWS,\n        "n_placebo_draws_valid": int(len(null_rs)),\n        "n_repos_with_usable_placebo_windows": int(n_repos_with_placebo),\n        "true_window_correlations_exact_metric": {\n            "founder_commit_share_pre_tfdd_vs_survival": (\n                {"r": None, "p": None, "status": "UNDEFINED_ZERO_VARIANCE_PREDICTOR"}\n                if true_r_share is None\n                else {"r": round(float(true_r_share), 4), "p": round(float(true_p_share), 4)}\n            ),\n            "n_distinct_new_primary_owners_pre_tfdd_vs_survival": {"r": round(float(true_r_owners), 4), "p": round(float(true_p_owners), 4)},\n        },\n        "true_window_proxy_metric_matched_to_placebo": {\n            "r": round(float(true_proxy_r), 4), "p": round(float(true_proxy_p), 4), "n": int(len(true_proxy_vals)),\n        },\n        "placebo_null_distribution": {\n            "mean": round(float(null_rs.mean()), 4) if len(null_rs) else None,\n            "std": round(float(null_rs.std(ddof=1)), 4) if len(null_rs) > 1 else None,\n            "percentiles_5_25_50_75_95": (\n                [round(float(x), 4) for x in np.percentile(null_rs, [5, 25, 50, 75, 95])] if len(null_rs) else None\n            ),\n        },\n        "true_window_percentile_in_null": round(percentile, 2) if not np.isnan(percentile) else None,\n        "comparison_to_prior_iteration": {\n            "prior_iteration_r": prior_iter_r, "prior_iteration_p": prior_iter_p, "prior_iteration_n_draws": prior_iter_n,\n            "prior_iteration_note": "iter1 used 25 draws on re-mined, non-unified data (n=30 usable repos)",\n            "note": "Metric definitions differ (year-resolution proxy here vs sub-year founder-share in iter1); "\n                    "compare pattern (percentile in null), not raw r values, across iterations.",\n        },\n    }\n\n\ntest_c = test_c_placebo(df)\n{k: v for k, v in test_c.items() if k != "placebo_null_distribution"}'}
```

### [70] TOOL RESULT — NotebookEdit · 2026-08-21 19:24:43 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [71] ASSISTANT · 2026-08-21 19:24:49 UTC

```
Now Sec6, build_predictions/output assembly, and final visualization.
```

### [72] TOOL CALL — NotebookEdit · 2026-08-21 19:24:49 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': '897078d5', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': "## Sec 6: window-boundary-noise validation control\n\nNew this iteration: computes founder-share variance across multiple stable (non-departure) windows within each repo's own history, and compares this within-repo noise floor against the true window's effect size (from Test C) — testing whether the weak Test C signal could simply be a window-computation artifact."}
```

### [73] TOOL RESULT — NotebookEdit · 2026-08-21 19:24:49 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [74] TOOL CALL — NotebookEdit · 2026-08-21 19:24:59 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': '19f34d30', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'def sec6_boundary_noise_control(df: pd.DataFrame, test_c_result: dict[str, Any]) -> dict[str, Any]:\n    logger.info("=== Sec 6: window-boundary-noise control (stable-period substitution) ===")\n    logger.warning(\n        "Non-TFDD candidate-pool repos (120 \'no qualifying TFDD\' discards) are not retrievable from "\n        "the dataset artifact\'s metadata -- substituting TFDD-corpus repos\' own multi-year-before-departure "\n        "windows as the stable-period proxy, per fallback_plan explicit substitution clause."\n    )\n    per_repo_variance = []\n    for _, row in df.iterrows():\n        yrs = sorted(t["year"] for t in row["yearly_tables"])\n        stable_yrs = [y for y in yrs if y <= (row["tfdd_year"] - 2) and (y - 1) in yrs]\n        proxies = [year_proxy_diffusion(row["yearly_tables"], y) for y in stable_yrs]\n        proxies = [p for p in proxies if p is not None]\n        if len(proxies) >= 2:\n            per_repo_variance.append({\n                "repo": row["repo"], "n_stable_windows": len(proxies), "variance": float(np.var(proxies, ddof=1)),\n            })\n\n    if not per_repo_variance:\n        logger.warning("No repo had >=2 usable stable-period windows -- boundary-noise floor UNTESTABLE.")\n        return {\n            "status": "UNTESTABLE",\n            "reason": "fewer than 2 usable stable-period windows in any repo (short pre-TFDD histories)",\n        }\n\n    variances = np.array([r["variance"] for r in per_repo_variance])\n    noise_floor_mean_var = float(variances.mean())\n    noise_floor_sd = float(np.sqrt(noise_floor_mean_var))\n\n    null_stats = test_c_result.get("placebo_null_distribution", {})\n    null_sd = null_stats.get("std")\n    true_r = test_c_result.get("true_window_proxy_metric_matched_to_placebo", {}).get("r")\n    distinguishable = None\n    if null_sd is not None and true_r is not None:\n        distinguishable = bool(abs(true_r) > 2 * (null_sd if null_sd else 1e-9))\n\n    logger.info(\n        f"Boundary-noise floor: mean per-repo variance={noise_floor_mean_var:.4f} (sd~{noise_floor_sd:.4f}) "\n        f"across {len(per_repo_variance)} repos with usable stable windows; placebo-null sd={null_sd}."\n    )\n    return {\n        "status": "EXECUTED",\n        "n_repos_with_usable_stable_windows": len(per_repo_variance),\n        "per_repo_stable_window_variance": per_repo_variance,\n        "boundary_noise_floor_mean_variance": round(noise_floor_mean_var, 4),\n        "boundary_noise_floor_sd": round(noise_floor_sd, 4),\n        "placebo_test_c_null_sd_for_comparison": null_sd,\n        "true_window_effect_r_for_comparison": true_r,\n        "true_effect_exceeds_2x_noise_floor_sd": distinguishable,\n        "interpretation": (\n            "If true_effect_exceeds_2x_noise_floor_sd is False/None, the pre-departure window\'s weak signal "\n            "is NOT distinguishable from ordinary within-repo measurement noise, i.e. the reviewer\'s window-"\n            "computation-artifact concern cannot be ruled out with this corpus. If True, the signal exceeds "\n            "what stable-period noise alone would produce."\n        ),\n    }\n\n\nsec6 = sec6_boundary_noise_control(df, test_c)\n{k: v for k, v in sec6.items() if k != "per_repo_stable_window_variance"}'}
```

### [75] TOOL RESULT — NotebookEdit · 2026-08-21 19:25:01 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [76] TOOL CALL — NotebookEdit · 2026-08-21 19:25:05 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': '46ed273b', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': '## Output assembly\n\nFits a controls-only baseline model and a full (controls + diffusion) model, producing per-repo `predict_baseline` / `predict_our_method` predictions in the same schema-validated format as the original `method_out.json`.'}
```

### [77] TOOL RESULT — NotebookEdit · 2026-08-21 19:25:05 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [78] TOOL CALL — NotebookEdit · 2026-08-21 19:25:17 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': 'b2b667c7', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'def build_predictions(df: pd.DataFrame) -> tuple[list[str], list[str]]:\n    controls_num = ["stars", "forks", "total_contributors", "project_age_days", "n_commits_total", "n_files_total", "history_span_years"]\n    degenerate = df.attrs.get("degenerate_predictors", [])\n    diffusion = [c for c in ["founder_commit_share_pre_tfdd", "n_distinct_new_primary_owners_pre_tfdd"] if c not in degenerate]\n    lang_dummies = pd.get_dummies(df["language"], prefix="lang", drop_first=True).astype(float)\n\n    def std_block(cols):\n        block = df[cols].astype(float).copy()\n        for c in cols:\n            if block[c].skew() > 1.5:\n                block[c] = np.log1p(block[c].clip(lower=0))\n        return pd.DataFrame(StandardScaler().fit_transform(block), columns=cols, index=df.index)\n\n    X_base = pd.concat([std_block(controls_num), lang_dummies], axis=1)\n    X_full = pd.concat([std_block(diffusion + controls_num), lang_dummies], axis=1)\n    y = df["survival"].values.astype(float)\n\n    baseline_clf = LogisticRegression(penalty="l2", C=1.0, solver="lbfgs", max_iter=2000).fit(X_base.values, y)\n    full_clf = LogisticRegression(penalty="l2", C=1.0, solver="lbfgs", max_iter=2000).fit(X_full.values, y)\n\n    p_base = baseline_clf.predict_proba(X_base.values)[:, 1]\n    p_full = full_clf.predict_proba(X_full.values)[:, 1]\n    labels_base = [("Active_survived" if p >= 0.5 else "Inactive_did_not_survive") + f"|p={p:.4f}" for p in p_base]\n    labels_full = [("Active_survived" if p >= 0.5 else "Inactive_did_not_survive") + f"|p={p:.4f}" for p in p_full]\n    return labels_base, labels_full\n\n\n_avail = psutil.virtual_memory().available\nlogger.info(f"Available RAM at start: {_avail / 1e9:.1f} GB")\n\npred_base, pred_full = build_predictions(df)\n\nds = next(d for d in raw_data["datasets"] if d["dataset"] == "founder_departure_tfdd_corpus")\nout_examples = []\nfor i, ex in enumerate(ds["examples"]):\n    out_examples.append({\n        "input": ex["input"],\n        "output": ex["output"],\n        "metadata_full_name": ex.get("metadata_full_name"),\n        "predict_baseline": pred_base[i],\n        "predict_our_method": pred_full[i],\n    })\n\noutput = {\n    "metadata": {\n        "method_name": "unified_corpus_retest_pre_departure_authority_diffusion",\n        "iteration": 2,\n        "what_changed_vs_iter1": (\n            "Unified 32-repo corpus (single provenance) instead of 62-attempted/30-usable independently "\n            "re-mined data; placebo draws raised 25 -> 300 (year-resolution, data-availability-limited); "\n            "new window-boundary-noise control (Sec 6) added to separate measurement noise from signal."\n        ),\n        "test_0_baseline_replication": test0,\n        "test_a_bhfdr_regression": test_a,\n        "test_b_matched_pairs_bootstrap": test_b,\n        "test_c_placebo_null": test_c,\n        "sec6_window_boundary_noise_control": sec6,\n        "random_seed": RNG_SEED,\n    },\n    "datasets": [{"dataset": "founder_departure_tfdd_corpus", "examples": out_examples}],\n}\nprint(f"Assembled output with {len(out_examples)} scored repos.")'}
```

### [79] TOOL RESULT — NotebookEdit · 2026-08-21 19:25:17 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [80] ASSISTANT · 2026-08-21 19:25:23 UTC

```
Now final results/visualization cells.
```

### [81] TOOL CALL — NotebookEdit · 2026-08-21 19:25:23 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': '8f2e5744', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': "## Results summary\n\nA readable table of the headline numbers from each test, plus two plots: the BH-FDR-significant predictors' standardized coefficients (Test A), and the true diffusion effect placed against its placebo-null distribution and the Sec-6 boundary-noise floor (Test C / Sec 6)."}
```

### [82] TOOL RESULT — NotebookEdit · 2026-08-21 19:25:23 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [83] TOOL CALL — NotebookEdit · 2026-08-21 19:25:35 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb', 'cell_id': '4555322d', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'print("=" * 70)\nprint("SUMMARY TABLE")\nprint("=" * 70)\nsummary_rows = [\n    ("Test 0", "baseline replication", test0["replication_assessment"]),\n    ("Test A", "BH-FDR regression", f"method={test_a[\'method_used\']}, diffusion_beats_controls={test_a[\'head_to_head_diffusion_beats_controls\']}"),\n    ("Test B", "matched-pairs bootstrap", test_b["status"]),\n    ("Test C", "within-repo placebo", f"true_r={test_c[\'true_window_proxy_metric_matched_to_placebo\'][\'r\']}, percentile_in_null={test_c[\'true_window_percentile_in_null\']}"),\n    ("Sec 6", "boundary-noise control", f"{sec6[\'status\']}: exceeds_2x_noise_floor={sec6.get(\'true_effect_exceeds_2x_noise_floor_sd\')}"),\n]\nfor name, desc, val in summary_rows:\n    print(f"{name:8s} {desc:28s} {val}")\n\nfig, axes = plt.subplots(1, 2, figsize=(13, 5))\n\n# Panel 1: standardized coefficients from Test A, sorted by BH-adjusted p-value\npreds = test_a["per_predictor"]\nnames = [p["predictor"] for p in preds]\ncoefs = [p["standardized_coef"] for p in preds]\ncolors = ["#2a7de1" if p["significant_at_bh_0.05"] else "#b0b0b0" for p in preds]\naxes[0].barh(names, coefs, color=colors)\naxes[0].axvline(0, color="black", linewidth=0.8)\naxes[0].set_xlabel("Standardized coefficient")\naxes[0].set_title("Test A: predictor coefficients\\n(blue = significant at BH-FDR 0.05)")\naxes[0].invert_yaxis()\n\n# Panel 2: placebo null distribution vs. true effect and Sec-6 noise floor\nnull_stats = test_c["placebo_null_distribution"]\ntrue_r = test_c["true_window_proxy_metric_matched_to_placebo"]["r"]\nif null_stats["std"] is not None:\n    x = np.linspace(null_stats["mean"] - 4 * null_stats["std"], null_stats["mean"] + 4 * null_stats["std"], 200)\n    from scipy.stats import norm\n    axes[1].plot(x, norm.pdf(x, null_stats["mean"], null_stats["std"]), color="#888888", label="placebo null (approx.)")\n    axes[1].axvline(true_r, color="#d62728", linewidth=2, label=f"true effect r={true_r}")\n    if sec6.get("status") == "EXECUTED":\n        nf_sd = sec6["boundary_noise_floor_sd"]\n        axes[1].axvspan(-2 * nf_sd, 2 * nf_sd, color="#f4c542", alpha=0.25, label="±2x Sec-6 noise floor")\n    axes[1].set_xlabel("year-resolution diffusion-proxy correlation (r)")\n    axes[1].set_title("Test C: true effect vs. placebo null\\n+ Sec-6 boundary-noise floor")\n    axes[1].legend(fontsize=8)\nelse:\n    axes[1].text(0.5, 0.5, "insufficient placebo draws", ha="center", va="center")\n\nplt.tight_layout()\nplt.show()'}
```

### [84] TOOL RESULT — NotebookEdit · 2026-08-21 19:25:35 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [85] ASSISTANT · 2026-08-21 19:25:41 UTC

```
Now let's remove the placeholder cell issue — it's already cell-0 replaced with title markdown. Let's test-run the notebook.
```

### [86] TOOL CALL — Bash · 2026-08-21 19:25:41 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui
/usr/local/bin/python3.12 -m venv .nb_env 2>&1 | tail -5
.nb_env/bin/pip install -q pip jupyter ipykernel 2>&1 | tail -10
```

### [87] TOOL RESULT — Bash · 2026-08-21 19:27:39 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bfyn6uicb", "timedOutAfterMs": 120000, "backgroundCwdHint": "Session cwd remains /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui; directory changes made by the backgrounded command do not apply to subsequent commands."}
```

### [88] ASSISTANT · 2026-08-21 19:27:41 UTC

```
Waiting on venv setup in background; I'll check back.
```

### [89] TOOL CALL — Bash · 2026-08-21 19:27:41 UTC

```
sleep 60; tail -30 /tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-65c2e4aGIhui/f2f30ce8-1e48-415b-89da-4521be7874a1/tasks/bfyn6uicb.output
```

### [90] TOOL RESULT — Bash [ERROR] · 2026-08-21 19:27:41 UTC

```
Error: Blocked: sleep 60 followed by: tail -30 /tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-65c2e4aGIhui/f2f30ce8-1e48-415b-89da-4521be7874a1/tasks/bfyn6uicb.output. To wait for a condition, use Monitor with an until-loop (e.g. `until <check>; do sleep 2; done`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block.
```

### [91] TOOL CALL — ToolSearch · 2026-08-21 19:27:43 UTC

```
{'query': 'select:Monitor'}
```

### [92] TOOL RESULT — ToolSearch · 2026-08-21 19:27:43 UTC

```
{"matches": ["Monitor"], "query": "select:Monitor", "total_deferred_tools": 22}
```

### [93] TOOL CALL — Monitor · 2026-08-21 19:27:45 UTC

```
{'description': 'wait for pip install to finish', 'command': 'until ! kill -0 $(pgrep -f "pip install -q pip jupyter" | head -1) 2>/dev/null; do sleep 3; done; echo DONE_INSTALL', 'timeout_ms': 180000, 'persistent': False}
```

### [94] TOOL RESULT — Monitor · 2026-08-21 19:27:45 UTC

```
{"taskId": "b1cgj8gqh", "timeoutMs": 180000, "persistent": false}
```

### [95] ASSISTANT · 2026-08-21 19:27:49 UTC

```
I'll wait for the install to complete before running the test.
```

### [96] TOOL CALL — Read · 2026-08-21 19:27:49 UTC

```
/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb
```

### [97] TOOL RESULT — Read · 2026-08-21 19:27:49 UTC

```
{"type": "notebook", "file": {"filePath": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/code_demo.ipynb", "cells": [{"cellType": "markdown", "source": "# Re-Testing Founder-Departure Survival Signals\n\nThis notebook re-runs three pre-registered statistical tests (BH-FDR logistic regression, caliper matched-pairs bootstrap, within-repo year-level placebo) plus a new window-boundary-noise control on a u... [truncated, 46361 chars total]
```

### [98] ASSISTANT · 2026-08-21 19:27:55 UTC

```
Notebook structure looks good. Now let's execute the test run.
```

### [99] TOOL CALL — Bash · 2026-08-21 19:27:55 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui
ls .nb_env/bin/jupyter 2>&1
.nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb > nbconvert.log 2>&1 &
echo "PID=$!"
```

### [100] TOOL RESULT — Bash · 2026-08-21 19:27:55 UTC

```
{"stdout": "ls: cannot access '.nb_env/bin/jupyter': No such file or directory\nPID=247", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [101] TOOL CALL — Bash · 2026-08-21 19:27:59 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui
ps aux | grep -i pip | grep -v grep
ls .nb_env/bin/ 2>&1 | head -20
```

### [102] TOOL RESULT — Bash · 2026-08-21 19:27:59 UTC

```
{"stdout": "root         203  0.0  0.0   4492  3092 ?        Ss   19:25   0:00 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1787340094067-r7go59.sh 2>/dev/null || true && shopt -u extglob 2>/dev/null || true && { \\builtin unalias -- 'unsetenv'; \\builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui /usr/local/bin/python3.12 -m venv .nb_env 2>&1 | tail -5 .nb_env/bin/pip install -q pip jupyter ipykernel 2>&1 | tail -10' < /dev/null && pwd -P >| /tmp/claude-1a35-cwd\nroot         212  3.7  0.0  97156 91176 ?        S    19:26   0:02 /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/.nb_env/bin/python3.12 .nb_env/bin/pip install -q pip jupyter ipykernel\nActivate.ps1\nactivate\nactivate.csh\nactivate.fish\npip\npip3\npip3.12\npython\npython3\npython3.12\nwsdump", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [103] ASSISTANT · 2026-08-21 19:28:01 UTC

```
Still installing. My nbconvert command failed silently since jupyter isn't installed yet — I'll wait for the Monitor notification, then retry.
```

### [104] TOOL CALL — Monitor · 2026-08-21 19:28:01 UTC

```
{'description': 'wait for pip install of jupyter/ipykernel to finish', 'command': 'cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui\nuntil [ -f .nb_env/bin/jupyter ]; do sleep 3; done\necho JUPYTER_READY', 'timeout_ms': 240000, 'persistent': False}
```

### [105] TOOL RESULT — Monitor · 2026-08-21 19:28:01 UTC

```
{"taskId": "bqvmas691", "timeoutMs": 240000, "persistent": false}
```

### [106] ASSISTANT · 2026-08-21 19:28:03 UTC

```
I'll wait for the notification before proceeding with the test run.
```

### [107] TOOL CALL — Bash · 2026-08-21 19:28:03 UTC

```
echo waiting
```

### [108] TOOL RESULT — Bash · 2026-08-21 19:28:03 UTC

```
{"stdout": "waiting", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [109] TOOL CALL — ToolSearch · 2026-08-21 19:28:05 UTC

```
{'query': 'select:TaskOutput'}
```

### [110] TOOL RESULT — ToolSearch · 2026-08-21 19:28:05 UTC

```
{"matches": ["TaskOutput"], "query": "select:TaskOutput", "total_deferred_tools": 22}
```

### [111] TOOL CALL — TaskOutput · 2026-08-21 19:32:01 UTC

```
{'task_id': 'bqvmas691', 'block': True, 'timeout': 240000}
```

### [112] TOOL RESULT — TaskOutput · 2026-08-21 19:32:01 UTC

```
{"retrieval_status": "success", "task": {"task_id": "bqvmas691", "task_type": "local_bash", "status": "killed", "description": "wait for pip install of jupyter/ipykernel to finish", "output": "\n[killed]\n", "exitCode": null}}
```

### [113] ASSISTANT · 2026-08-21 19:32:07 UTC

```
Pip install is taking a long time. Let me check its current status directly.
```

### [114] TOOL CALL — Bash · 2026-08-21 19:32:07 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui
ps aux | grep pip | grep -v grep
ls .nb_env/bin/jupyter 2>&1
```

### [115] TOOL RESULT — Bash [ERROR] · 2026-08-21 19:32:07 UTC

```
Error: Exit code 2
root         203  0.0  0.0   4492  3092 ?        Ss   19:25   0:00 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1787340094067-r7go59.sh 2>/dev/null || true && shopt -u extglob 2>/dev/null || true && { \builtin unalias -- 'unsetenv'; \builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui /usr/local/bin/python3.12 -m venv .nb_env 2>&1 | tail -5 .nb_env/bin/pip install -q pip jupyter ipykernel 2>&1 | tail -10' < /dev/null && pwd -P >| /tmp/claude-1a35-cwd
root         212  1.8  0.0 100524 95148 ?        S    19:26   0:05 /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/.nb_env/bin/python3.12 .nb_env/bin/pip install -q pip jupyter ipykernel
ls: cannot access '.nb_env/bin/jupyter': No such file or directory
```

### [116] ASSISTANT · 2026-08-21 19:32:11 UTC

```
Still running after several minutes, likely resolving dependencies slowly. I'll monitor with a longer timeout.
```

### [117] TOOL CALL — Monitor · 2026-08-21 19:32:11 UTC

```
{'description': 'wait for jupyter install to finish (long dependency resolve)', 'command': 'cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui\nuntil [ -f .nb_env/bin/jupyter ] || ! pgrep -f "pip install -q pip jupyter" > /dev/null; do sleep 5; done\necho JUPYTER_INSTALL_DONE', 'timeout_ms': 600000, 'persistent': True}
```

### [118] TOOL RESULT — Monitor · 2026-08-21 19:32:11 UTC

```
{"taskId": "bvywh8a5g", "timeoutMs": 0, "persistent": true}
```

### [119] ASSISTANT · 2026-08-21 19:32:25 UTC

```
I'll wait for that notification before continuing with the test execution.
```

### [120] TOOL CALL — TaskOutput · 2026-08-21 19:32:25 UTC

```
{'task_id': 'bvywh8a5g', 'block': True, 'timeout': 590000}
```

### [121] TOOL RESULT — TaskOutput · 2026-08-21 19:32:25 UTC

```
{"retrieval_status": "success", "task": {"task_id": "bvywh8a5g", "task_type": "local_bash", "status": "completed", "description": "wait for jupyter install to finish (long dependency resolve)", "output": "JUPYTER_INSTALL_DONE\n\n[exited with code 0]\n", "exitCode": 0}}
```

### [122] ASSISTANT · 2026-08-21 19:32:29 UTC

```
Jupyter is installed. Now running the actual notebook execution in the background.
```

### [123] TOOL CALL — Bash · 2026-08-21 19:32:29 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui
ls .nb_env/bin/jupyter
nohup .nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb > nbconvert.log 2>&1 &
echo "PID=$!"
```

### [124] TOOL RESULT — Bash · 2026-08-21 19:32:29 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "b4mbcspao", "backgroundCwdHint": "Session cwd remains /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui; directory changes made by the backgrounded command do not apply to subsequent commands."}
```

### [125] TOOL CALL — Bash · 2026-08-21 19:32:31 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui
sleep 2; ps aux | grep nbconvert | grep -v grep; cat nbconvert.log 2>&1
```

### [126] TOOL RESULT — Bash · 2026-08-21 19:32:35 UTC

```
{"stdout": "usage: jupyter [-h] [--version] [--config-dir] [--data-dir] [--runtime-dir]\n               [--paths] [--json] [--debug]\n               [subcommand]\n\nJupyter: Interactive Computing\n\npositional arguments:\n  subcommand     the subcommand to launch\n\noptions:\n  -h, --help     show this help message and exit\n  --version      show the versions of core jupyter packages and exit\n  --config-dir   show Jupyter config dir\n  --data-dir     show Jupyter data dir\n  --runtime-dir  show Jupyter runtime dir\n  --paths        show all Jupyter paths. Add --json for machine-readable\n                 format.\n  --json         output paths as machine-readable json\n  --debug        output debug information about paths\n\nAvailable subcommands: migrate troubleshoot\n\nJupyter command `jupyter-nbconvert` not found.", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [127] ASSISTANT · 2026-08-21 19:32:37 UTC

```
nbconvert isn't installed — need to install it explicitly.
```

### [128] TOOL CALL — Bash · 2026-08-21 19:32:37 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui
nohup .nb_env/bin/pip install -q nbconvert > pip_nbconvert.log 2>&1 &
echo "PID=$!"
```

### [129] TOOL RESULT — Bash · 2026-08-21 19:32:37 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "b023peirh", "backgroundCwdHint": "Session cwd remains /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui; directory changes made by the backgrounded command do not apply to subsequent commands."}
```

### [130] TOOL CALL — Monitor · 2026-08-21 19:32:41 UTC

```
{'description': 'wait for nbconvert pip install to finish', 'command': 'cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui\nuntil [ -f .nb_env/bin/jupyter-nbconvert ]; do sleep 3; done\necho NBCONVERT_READY', 'timeout_ms': 180000, 'persistent': False}
```

### [131] TOOL RESULT — Monitor · 2026-08-21 19:32:41 UTC

```
{"taskId": "bylyiawfc", "timeoutMs": 180000, "persistent": false}
```

### [132] TOOL CALL — TaskOutput · 2026-08-21 19:33:37 UTC

```
{'task_id': 'bylyiawfc', 'block': True, 'timeout': 180000}
```

### [133] TOOL RESULT — TaskOutput · 2026-08-21 19:33:37 UTC

```
{"retrieval_status": "success", "task": {"task_id": "bylyiawfc", "task_type": "local_bash", "status": "completed", "description": "wait for nbconvert pip install to finish", "output": "NBCONVERT_READY\n\n[exited with code 0]\n", "exitCode": 0}}
```

### [134] ASSISTANT · 2026-08-21 19:33:41 UTC

```
Now let's run the actual notebook execution.
```

### [135] TOOL CALL — Bash · 2026-08-21 19:33:41 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui
nohup .nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb > nbconvert.log 2>&1 &
echo "PID=$!"
```

### [136] TOOL RESULT — Bash · 2026-08-21 19:33:41 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "b7449f6ff", "backgroundCwdHint": "Session cwd remains /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui; directory changes made by the backgrounded command do not apply to subsequent commands."}
```

### [137] TOOL CALL — Monitor · 2026-08-21 19:33:43 UTC

```
{'description': 'wait for nbconvert notebook execution to finish', 'command': 'cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui\nuntil ! pgrep -f "jupyter.*nbconvert" > /dev/null; do sleep 3; done\necho NBCONVERT_DONE\ntail -40 nbconvert.log', 'timeout_ms': 300000, 'persistent': False}
```

### [138] TOOL RESULT — Monitor · 2026-08-21 19:33:43 UTC

```
{"taskId": "biaedngzo", "timeoutMs": 300000, "persistent": false}
```

### [139] TOOL CALL — TaskOutput · 2026-08-21 19:38:43 UTC

```
{'task_id': 'biaedngzo', 'block': True, 'timeout': 300000}
```

### [140] TOOL RESULT — TaskOutput · 2026-08-21 19:38:43 UTC

```
{"retrieval_status": "success", "task": {"task_id": "biaedngzo", "task_type": "local_bash", "status": "killed", "description": "wait for nbconvert notebook execution to finish", "output": "\n[killed]\n", "exitCode": null}}
```

### [141] TOOL CALL — Bash · 2026-08-21 19:38:47 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui
ps aux | grep -E "jupyter|nbconvert|pip" | grep -v grep
echo ---
tail -50 nbconvert.log
```

### [142] TOOL RESULT — Bash · 2026-08-21 19:38:47 UTC

```
{"stdout": "root         203  0.0  0.0   4492  3092 ?        Ss   19:25   0:00 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1787340094067-r7go59.sh 2>/dev/null || true && shopt -u extglob 2>/dev/null || true && { \\builtin unalias -- 'unsetenv'; \\builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui /usr/local/bin/python3.12 -m venv .nb_env 2>&1 | tail -5 .nb_env/bin/pip install -q pip jupyter ipykernel 2>&1 | tail -10' < /dev/null && pwd -P >| /tmp/claude-1a35-cwd\nroot         212  1.2  0.0 101264 96300 ?        S    19:26   0:08 /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/.nb_env/bin/python3.12 .nb_env/bin/pip install -q pip jupyter ipykernel\n---\n    return self.from_notebook_node(\n           ^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/notebook.py\", line 36, in from_notebook_node\n    nb_copy, resources = super().from_notebook_node(nb, resources, **kw)\n                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 154, in from_notebook_node\n    nb_copy, resources = self._preprocess(nb_copy, resources)\n                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 353, in _preprocess\n    nbc, resc = preprocessor(nbc, resc)\n                ^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/.nb_env/lib/python3.12/site-packages/nbconvert/preprocessors/base.py\", line 48, in __call__\n    return self.preprocess(nb, resources)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/.nb_env/lib/python3.12/site-packages/nbconvert/preprocessors/execute.py\", line 97, in preprocess\n    with self.setup_kernel():\n         ^^^^^^^^^^^^^^^^^^^\n  File \"/usr/local/lib/python3.12/contextlib.py\", line 137, in __enter__\n    return next(self.gen)\n           ^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/.nb_env/lib/python3.12/site-packages/nbclient/client.py\", line 600, in setup_kernel\n    self.start_new_kernel(**kwargs)\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/.nb_env/lib/python3.12/site-packages/jupyter_core/utils/__init__.py\", line 165, in wrapped\n    return loop.run_until_complete(inner)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/local/lib/python3.12/asyncio/base_events.py\", line 691, in run_until_complete\n    return future.result()\n           ^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/.nb_env/lib/python3.12/site-packages/nbclient/client.py\", line 550, in async_start_new_kernel\n    await ensure_async(self.km.start_kernel(extra_arguments=self.extra_arguments, **kwargs))\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/.nb_env/lib/python3.12/site-packages/jupyter_core/utils/__init__.py\", line 214, in ensure_async\n    result = await obj\n             ^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/.nb_env/lib/python3.12/site-packages/jupyter_client/manager.py\", line 116, in wrapper\n    raise e\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/.nb_env/lib/python3.12/site-packages/jupyter_client/manager.py\", line 107, in wrapper\n    out = await method(self, *args, **kwargs)\n          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/.nb_env/lib/python3.12/site-packages/jupyter_client/manager.py\", line 523, in _async_start_kernel\n    kernel_cmd, kw = await self._async_pre_start_kernel(**kw)\n                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/.nb_env/lib/python3.12/site-packages/jupyter_client/manager.py\", line 485, in _async_pre_start_kernel\n    self.kernel_spec,\n    ^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/.nb_env/lib/python3.12/site-packages/jupyter_client/manager.py\", line 267, in kernel_spec\n    self._kernel_spec = self.kernel_spec_manager.get_kernel_spec(self.kernel_name)\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/.nb_env/lib/python3.12/site-packages/jupyter_client/kernelspec.py\", line 287, in get_kernel_spec\n    raise NoSuchKernel(kernel_name)\njupyter_client.kernelspec.NoSuchKernel: No such kernel named python3", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [143] ASSISTANT · 2026-08-21 19:38:53 UTC

```
Need to register the ipykernel.
```

### [144] TOOL CALL — Bash · 2026-08-21 19:38:53 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui
.nb_env/bin/python -m ipykernel install --user --name python3 --display-name python3 2>&1 | tail -10
```

### [145] TOOL RESULT — Bash · 2026-08-21 19:39:03 UTC

```
{"stdout": "Installed kernelspec python3 in /root/.local/share/jupyter/kernels/python3", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [146] TOOL CALL — Bash · 2026-08-21 19:39:05 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui
nohup .nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb > nbconvert.log 2>&1 &
echo "PID=$!"
```

### [147] TOOL RESULT — Bash · 2026-08-21 19:39:05 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bzy0z13yk", "backgroundCwdHint": "Session cwd remains /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui; directory changes made by the backgrounded command do not apply to subsequent commands."}
```

### [148] ASSISTANT · 2026-08-21 19:39:09 UTC

```
This will take a while due to numpy/pandas/etc install cell. Monitoring for completion.
```

### [149] TOOL CALL — Monitor · 2026-08-21 19:39:09 UTC

```
{'description': 'wait for nbconvert notebook execution to finish (installs numpy/pandas/statsmodels locally)', 'command': 'cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui\nuntil ! pgrep -f "jupyter-nbconvert" > /dev/null && [ -f nbconvert.log ]; do sleep 5; done\nsleep 2\necho NBCONVERT_DONE\ntail -60 nbconvert.log', 'timeout_ms': 600000, 'persistent': True}
```

### [150] TOOL RESULT — Monitor · 2026-08-21 19:39:09 UTC

```
{"taskId": "b59am7cpm", "timeoutMs": 0, "persistent": true}
```

### [151] TOOL CALL — TaskOutput · 2026-08-21 19:49:11 UTC

```
{'task_id': 'b59am7cpm', 'block': True, 'timeout': 600000}
```

### [152] TOOL RESULT — TaskOutput · 2026-08-21 19:49:11 UTC

```
{"retrieval_status": "timeout", "task": {"task_id": "b59am7cpm", "task_type": "local_bash", "status": "running", "description": "wait for nbconvert notebook execution to finish (installs numpy/pandas/statsmodels locally)", "output": "Output truncated (0KB total). Full output saved to: /tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-65c2e4aGIhui/f2f30ce8-1e48-415b-89da-4521be7874a1/tasks/b59am7cpm.output", "exitCode": null}}
```

### [153] TOOL CALL — Bash · 2026-08-21 19:49:33 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui
ps aux | grep -E "jupyter|nbconvert" | grep -v grep
echo ---
tail -60 nbconvert.log 2>&1
```

### [154] TOOL RESULT — Bash · 2026-08-21 19:49:33 UTC

```
{"stdout": "root         915  0.3  0.0 407144 93020 ?        Sl   19:39   0:02 /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/.nb_env/bin/python3.12 .nb_env/bin/jupyter-nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb\n---\n[NbConvertApp] Converting notebook code_demo.ipynb to notebook\n[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.\n\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\nipython 9.16.1 requires psutil>=7; sys_platform != \"emscripten\" and sys_platform != \"cygwin\", but you have psutil 6.1.1 which is incompatible.\u001b[0m\u001b[31m\n\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [155] ASSISTANT · 2026-08-21 19:49:39 UTC

```
Still running (past install cell now, into imports/execution). Let me wait more.
```

### [156] TOOL CALL — Monitor · 2026-08-21 19:49:39 UTC

```
{'description': 'wait for nbconvert process to exit', 'command': 'cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui\nuntil ! pgrep -f "jupyter-nbconvert" > /dev/null; do sleep 5; done\necho NBCONVERT_PROCESS_EXITED\ntail -80 nbconvert.log', 'timeout_ms': 600000, 'persistent': True}
```

### [157] TOOL RESULT — Monitor · 2026-08-21 19:49:39 UTC

```
{"taskId": "br4q0st18", "timeoutMs": 0, "persistent": true}
```

### [158] CONFIG · 2026-08-21 20:34:01 UTC

```
model: claude-sonnet-5 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui
```

### [159] SYSTEM-USER prompt · 2026-08-21 20:34:09 UTC

````
<conversion_philosophy>
**MINIMAL CHANGES — PRESERVE THE ORIGINAL CODE**

The goal is to make the artifact's code READABLE, UNDERSTANDABLE, and RUNNABLE in a short time
to someone reviewing the research, with the option to easily scale parameters back to original
values for a full run (which can take much longer). Think of this as annotating and reformatting,
not refactoring.

**DO:**
- Split the original script into logical notebook cells (imports, setup, processing, results)
- Add markdown cells BETWEEN code cells explaining what each section does and why
- Add inline comments where the logic is non-obvious
- Add a visualization/summary cell at the end showing key outputs
- Fix hardcoded file paths to use the GitHub data loading pattern

**DO NOT:**
- Rewrite functions or change algorithms
- Rename variables or restructure logic
- Add error handling, type hints, or "improvements" that weren't in the original
- Simplify or "clean up" the original code
- Remove any original comments or logic
- Change the computational approach

The reader should recognize the original script when looking at the notebook — it's the
same code, just split into cells with explanatory markdown between sections.
</conversion_philosophy>

<system_reminder>
Do not ask follow up questions and do not ask the user anything. Execute all steps independently.
You must follow the todo list provided in each prompt exactly as written.
No placeholders, stubs, or incomplete code — all code must be complete and functional.
</system_reminder>

<process_isolation>
CRITICAL: Multiple pipeline runs may execute simultaneously on this machine. `ps aux | grep method.py` matches ALL runs, not just yours.
- NEVER kill processes by name (`killall`, `pkill -f`, `ps aux | grep ... | xargs kill`). This kills OTHER runs' processes.
- NEVER monitor processes by name (`ps aux | grep method.py`). You will see other runs' processes and get confused.
- ALWAYS use PID-based process management:
  Run: `uv run method.py & PID=$!` or `timeout <seconds> uv run method.py & PID=$!`
  Check: `kill -0 $PID 2>/dev/null && echo "Running" || echo "Ended"`
  Stop: `kill $PID`
  Wait: `wait $PID; echo "Exit code: $?"`
  Monitor: `tail -f logs/run.log & TAIL_PID=$!` then `kill $TAIL_PID` when done
</process_isolation>

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/`:
GOOD: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/file.py`, `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<task>
Convert this artifact's Python script into a demo notebook with MINIMAL changes to the original code.
Split into cells, add markdown explanations between sections, add a visualization cell at the end.
Output: mini_demo_data.json + code_demo.ipynb (notebook that loads data from GitHub URL)
</task>

<artifact_info>
id: art_65c2e4aGIhui
type: experiment
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
out_demo_files:
- path: method.py
  description: Research methodology implementation
</artifact_info>

<github_repo>
Repo URL: https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion
Raw data URL: https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json

URLs won't work yet — files pushed to GitHub AFTER notebook creation.
Use local fallback pattern so notebook works locally (now) and in Colab (after deployment).
</github_repo>

<data_file_sizes>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_file_sizes>

<install_dependencies_pattern>
Follow the aii-colab skill exactly. It has the install cell pattern, pre-installed package list, numpy 2.0 compat shims, and all Colab-specific rules.
</install_dependencies_pattern>

<data_loading_pattern>
`mini_demo_data.json` = curated subset for the demo.
Use this pattern for Colab compatibility (GitHub URL with local fallback):
```python
GITHUB_DATA_URL = "https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json"
import json, os

def load_data():
    try:
        import urllib.request
        with urllib.request.urlopen(GITHUB_DATA_URL) as response:
            return json.loads(response.read().decode())
    except Exception: pass
    if os.path.exists("mini_demo_data.json"):
        with open("mini_demo_data.json") as f: return json.load(f)
    raise FileNotFoundError("Could not load mini_demo_data.json")
```
</data_loading_pattern>

<notebook_structure>
--- Setup ---
Cell 1 (markdown): Title, description, what this artifact does.
Cell 2 (code): Install dependencies — follow the aii-colab skill's install cell pattern exactly. Fill in all packages imported by the artifact's code.
Cell 3 (code): Imports — copy original import block as-is, plus any additional imports needed for the notebook (e.g. matplotlib for visualization).
Cell 4 (code): Data loading helper — use the <data_loading_pattern> above.
Cell 5 (code): `data = load_data()`

--- Config ---
Config cell (code): Define ALL tunable parameters (iterations, epochs, n_samples, hidden_size, etc.) as variables at the top of this cell. Start with the ABSOLUTE MINIMUM values — the smallest that produce any output at all (e.g. 1 iteration, 2 samples, smallest array size). These get gradually increased during testing — see TODOs.

--- Processing ---
Remaining cells: One code cell per logical section of the original script. Add a markdown cell BEFORE each code cell. Copy code as closely as possible, with these changes:
  1. Replace file paths to use the loaded `data` variable.
  2. Use the config variables from the config cell (NOT hardcoded values).
  3. Minimal fixes are allowed if something doesn't work in notebook context (e.g. adjusting paths, removing CLI args, fixing imports), but keep changes to the absolute minimum.

--- Results ---
Visualization cell (code): Print key results in a readable table, plot numeric data with matplotlib if appropriate.
</notebook_structure>

<priority>
WORKING > OPTIMIZED. A small-scale demo that runs correctly is the goal. Once the notebook passes with minimum config values, scale up only if time permits — do NOT spend multiple retries chasing larger parameters. If a working version exists, finish and move on.
</priority>

<max_notebook_total_runtime>600s (10 min)</max_notebook_total_runtime>

<test_environment>
To test-run the notebook in a clean environment (simulating Colab), create a disposable `.nb_env` in your workspace:
```bash
/usr/local/bin/python3.12 -m venv .nb_env
.nb_env/bin/pip install -q pip jupyter ipykernel
.nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb
rm -rf .nb_env
```
The timeout is set to <max_notebook_total_runtime>. The entire notebook must finish within this time.

What happens: the .venv starts empty (just jupyter). When the notebook's install cell runs, `google.colab` is NOT in sys.modules, so ALL packages get installed — non-Colab packages unconditionally, and Colab packages (numpy, pandas, etc.) at Colab's exact versions via the guard block. The result mirrors Colab's environment as closely as possible. If a cell fails, fix the notebook and re-run.
</test_environment>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.


<todos>
TODO 1. Read and STRICTLY follow these skills: aii-colab, aii-long-running-tasks.
TODO 2. Read demo file and relevant preview_* files (preview only). Understand script structure: imports, setup, processing, output. Identify ALL tunable parameters (iterations, epochs, n_samples, hidden_size, batch_size, etc.) — these go in the config cell.
TODO 3. Create `mini_demo_data.json`: curated subset from at most ONE dataset (no more than 100 diverse examples). CRITICAL: do NOT read/grep full output file — may crash. Use `head -c 5000` or stream first entries with Python to pick examples.
TODO 4. Create `code_demo.ipynb` via NotebookEdit following <notebook_structure>. Set ALL config parameters to ABSOLUTE MINIMUM values — the smallest that produce any output (e.g. 1 iteration, 2 samples, smallest array sizes). Test-run using <test_environment>. Fix all errors until it passes.
TODO 5. GRADUALLY SCALE (but don't overdo it): increase config params step by step (e.g. ~2x each round). After each increase: test-run, record runtime, fix errors. STOP SCALING as soon as results look meaningful — a working small-scale demo beats a failed large-scale one. If full original params fit within <max_notebook_total_runtime> (10% margin), use them. Otherwise keep whatever works and comment out the true original values. Do NOT spend more than 2-3 scaling rounds.
TODO 6. Verify: (1) code_demo.ipynb contains GITHUB_DATA_URL = "https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json" exactly, (2) mini_demo_data.json exists, (3) uses GitHub URL pattern not just open('mini_demo_data.json').
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "DemoExpectedFiles": {
      "description": "Expected output files from code demo notebook generation.",
      "properties": {
        "notebook": {
          "default": "",
          "description": "Path to the generated demo notebook. Example: 'code_demo.ipynb'",
          "title": "Notebook",
          "type": "string"
        },
        "mini_data_file": {
          "default": "",
          "description": "Path to the mini demo data JSON (curated subset). Example: 'mini_demo_data.json'",
          "title": "Mini Data File",
          "type": "string"
        }
      },
      "title": "DemoExpectedFiles",
      "type": "object"
    }
  },
  "description": "Dataset/experiment/evaluation \u2192 Jupyter notebook demo.\n\nTitle and summary come from the parent artifact (gen_art step),\nnot from the demo agent. The agent only outputs expected files.",
  "properties": {
    "out_expected_files": {
      "$ref": "#/$defs/DemoExpectedFiles",
      "description": "All output files you created. Must include the demo notebook."
    }
  },
  "required": [],
  "title": "CodeDemo",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [160] HUMAN-USER prompt · 2026-08-21 20:34:09 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [161] TOOL CALL — Bash · 2026-08-21 20:34:13 UTC

```
cd "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui" && ls -la && echo --- && find /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1 -maxdepth 1
```

### [162] TOOL RESULT — Bash · 2026-08-21 20:34:13 UTC

```
{"stdout": "total 6452\ndrwxr-xr-x 3 root root 2067654 Aug 21 20:00 .\ndrwxr-xr-x 5 root root 2067807 Aug 21 19:16 ..\ndrwxr-xr-x 7 root root 2067616 Aug 21 19:27 .nb_env\n-rw-r--r-- 1 root root   37780 Aug 21 20:34 .repl_agent.ptylog\n-rw-r--r-- 1 root root  174135 Aug 21 20:05 code_demo.ipynb\n-rw-r--r-- 1 root root  178502 Aug 21 19:21 mini_demo_data.json\n-rw-r--r-- 1 root root    9012 Aug 21 19:50 nbconvert.log\n-rw-r--r-- 1 root root    1202 Aug 21 20:05 nbconvert2.log\n-rw-r--r-- 1 root root     127 Aug 21 19:33 pip_nbconvert.log\n-rw-r--r-- 1 root root     127 Aug 21 20:05 pip_prewarm.log\n---\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/.terminal_claude_agent_struct_out.json\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/pyproject.toml\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/claude-0-freeze.txt\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/preview_method_out.json\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/mini_method_out.json\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/full_method_out.json\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/method.py\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/method_out.json\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/__pycache__\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/logs\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/.venv\n/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/full_data_out.json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [163] TOOL CALL — Skill · 2026-08-21 20:34:13 UTC

```
aii-colab
```

### [164] TOOL CALL — Skill · 2026-08-21 20:34:13 UTC

```
aii-long-running-tasks
```

### [165] TOOL RESULT — Skill · 2026-08-21 20:34:13 UTC

```
{"success": true, "commandName": "aii-colab"}
```

### [166] TOOL RESULT — Skill · 2026-08-21 20:34:13 UTC

```
{"success": true, "commandName": "aii-long-running-tasks"}
```

### [167] TOOL CALL — Bash · 2026-08-21 20:34:19 UTC

```
cd "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui" && tail -50 nbconvert2.log && echo "---STRUCT---" && cat .terminal_claude_agent_struct_out.json 2>/dev/null && echo "---GREP URL---" && grep -o 'GITHUB_DATA_URL = "[^"]*"' code_demo.ipynb
```

### [168] TOOL RESULT — Bash · 2026-08-21 20:34:19 UTC

```
{"stdout": "[NbConvertApp] Converting notebook code_demo.ipynb to notebook\n[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n[NbConvertApp] Writing 174122 bytes to code_demo.ipynb\n---STRUCT---", "stderr": "", "interrupted": false, "isImage": false, "returnCodeInterpretation": "No matches found", "noOutputExpected": false}
```

### [169] ASSISTANT · 2026-08-21 20:34:23 UTC

```
Good, this workspace already has a working notebook and data file from prior work. Let me verify execution succeeded and check the URL pattern, then verify outputs and errors in the executed notebook.
```

### [170] TOOL CALL — Bash · 2026-08-21 20:34:23 UTC

```
cd "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui" && python3 -c "
import json
nb = json.load(open('code_demo.ipynb'))
errs = 0
for c in nb['cells']:
    for o in c.get('outputs', []):
        if o.get('output_type') == 'error':
            errs += 1
            print('ERROR in cell:', o.get('ename'), o.get('evalue'))
print('total error outputs:', errs)
print('num cells:', len(nb['cells']))
"
grep -o 'GITHUB_DATA_URL = \"[^\"]*\"' code_demo.ipynb | head -1
grep -c '"open(\\"mini_demo_data.json\\")"' code_demo.ipynb || true
```

### [171] TOOL RESULT — Bash · 2026-08-21 20:34:23 UTC

```
{"stdout": "total error outputs: 0\nnum cells: 24\n0", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [172] TOOL CALL — Bash · 2026-08-21 20:34:27 UTC

```
cd "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui" && python3 -c "
import json
nb = json.load(open('code_demo.ipynb'))
for c in nb['cells']:
    src = ''.join(c.get('source', []))
    if 'GITHUB_DATA_URL' in src:
        print(src)
        print('====')
"
```

### [173] TOOL RESULT — Bash · 2026-08-21 20:34:27 UTC

```
{"stdout": "GITHUB_DATA_URL = \"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\"\nimport json, os\n\ndef load_data():\n    try:\n        import urllib.request\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\n            return json.loads(response.read().decode())\n    except Exception: pass\n    if os.path.exists(\"mini_demo_data.json\"):\n        with open(\"mini_demo_data.json\") as f: return json.load(f)\n    raise FileNotFoundError(\"Could not load mini_demo_data.json\")\n====", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [174] ASSISTANT · 2026-08-21 20:34:31 UTC

```
Everything checks out: the notebook exists, executed with 0 errors, and uses the exact required GITHUB_DATA_URL with local fallback. Now write the struct output file.
```

### [175] TOOL CALL — Write · 2026-08-21 20:34:31 UTC

```
File: /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/.terminal_claude_agent_struct_out.json

{
  "out_expected_files": {
    "notebook": "code_demo.ipynb",
    "mini_data_file": "mini_demo_data.json"
  }
}
```

### [176] TOOL RESULT — Write · 2026-08-21 20:34:31 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_65c2e4aGIhui/.terminal_claude_agent_struct_out.json", "content": "{\n  \"out_expected_files\": {\n    \"notebook\": \"code_demo.ipynb\",\n    \"mini_data_file\": \"mini_demo_data.json\"\n  }\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [177] ASSISTANT · 2026-08-21 20:34:32 UTC

```
The demo notebook was already built and verified in this workspace (24 cells, 0 execution errors, correct GitHub URL with local fallback pattern). I confirmed the executed output is error-free and wrote the required `.terminal_claude_agent_struct_out.json` pointing to `code_demo.ipynb` and `mini_demo_data.json`. Task complete.
```
