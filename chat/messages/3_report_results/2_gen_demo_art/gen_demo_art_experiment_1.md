# gen_demo_art_experiment_1 — report_results

> Phase: `gen_paper_repo` · `gen_demo_art`
> Run: `iter1_0b7b616dce39` — Scaling the Corpus, Auditing the Power, and Reconciling the Sign: What Happens When a Founder-Diffusion Survival Test Is Finally Interrogated Rather Than Just Run
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_demo_art_experiment_1` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-08-21 21:34:56 UTC

```
model: claude-sonnet-5 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty
```

### [2] SYSTEM-USER prompt · 2026-08-21 21:35:04 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/`:
GOOD: `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/file.py`, `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/results/out.json`
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
out_demo_files:
- path: method.py
  description: Research methodology implementation
</artifact_info>

<github_repo>
Repo URL: https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion
Raw data URL: https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json

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
GITHUB_DATA_URL = "https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json"
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
TODO 6. Verify: (1) code_demo.ipynb contains GITHUB_DATA_URL = "https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json" exactly, (2) mini_demo_data.json exists, (3) uses GitHub URL pattern not just open('mini_demo_data.json').
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

### [3] HUMAN-USER prompt · 2026-08-21 21:35:04 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [4] TOOL CALL — Bash · 2026-08-21 21:35:10 UTC

```
ls -la && echo --- && find /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1 -maxdepth 1
```

### [5] TOOL RESULT — Bash · 2026-08-21 21:35:10 UTC

```
{"stdout": "total 2002\ndrwxr-xr-x 2 root root 1003687 Aug 21 21:34 .\ndrwxr-xr-x 5 root root 1007298 Aug 21 21:34 ..\n-rw-r--r-- 1 root root   37758 Aug 21 21:35 .repl_agent.ptylog\n---\n/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1\n/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/.terminal_claude_agent_struct_out.json\n/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/preview_method_out.json\n/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/mini_method_out.json\n/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/full_method_out.json\n/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method_out.json\n/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/uv.lock\n/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method.py\n/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/.claude\n/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/__pycache__\n/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/results\n/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/pyproject.toml\n/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/logs\n/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/.venv\n/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/repos_scratch\n/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/.repl_agent.ptylog", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [6] TOOL CALL — Skill · 2026-08-21 21:35:10 UTC

```
aii-colab
```

### [7] TOOL CALL — Skill · 2026-08-21 21:35:10 UTC

```
aii-long-running-tasks
```

### [8] TOOL RESULT — Skill · 2026-08-21 21:35:10 UTC

```
{"success": true, "commandName": "aii-colab"}
```

### [9] TOOL RESULT — Skill · 2026-08-21 21:35:10 UTC

```
{"success": true, "commandName": "aii-long-running-tasks"}
```

### [10] TOOL CALL — Read · 2026-08-21 21:35:14 UTC

```
/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method.py
```

### [11] TOOL RESULT — Read · 2026-08-21 21:35:14 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method.py", "content": "#!/usr/bin/env python3\n\"\"\"Founder-only Truck-Factor Development Departure (TFDD) survival study.\n\nRe-implements the DOA / Truck-Factor / TFDD / Active-Inactive pipeline of\nAvelino et al. (ESEM 2019, \"The Truck Factor of Popular GitHub Applications\")\nfrom real GitHub commit histories, detects founder-only TFDD ... [truncated, 45581 chars total]
```

### [12] TOOL CALL — Bash · 2026-08-21 21:35:14 UTC

```
cd /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1 && head -c 4000 preview_method_out.json; echo; echo ---; wc -c preview_method_out.json mini_method_out.json full_method_out.json
```

### [13] TOOL RESULT — Bash · 2026-08-21 21:35:14 UTC

```
{"stdout": "{\n  \"metadata\": {\n    \"method_name\": \"founder_authority_diffusion_tfdd_survival\",\n    \"description\": \"Founder-only TFDD survival prediction from GitHub commit histories. our_method uses pre-departure authority-diffusion trajectory (founder_share, n_diffused_owners in the 12-6mo pre-TFDD window); basel...\",\n    \"n_founder_tfdd_events_strict\": 16,\n    \"n_founder_tfdd_events_relaxed\": 20,\n    \"strict_unconditioned_survival_rate\": 0.3125,\n    \"avelino_et_al_reference_survival_rate\": 0.41,\n    \"summary_results_file\": \"results/method_summary.json\",\n    \"diagnostics_file\": \"results/repo_processing_diagnostics.csv\"\n  },\n  \"datasets\": [\n    {\n      \"dataset\": \"github_founder_tfdd_events\",\n      \"examples\": [\n        {\n          \"input\": \"Repo OtusGolang/webinars_practical_part (Go): founder-only TFDD detected at 2022-10-09T20:53:55+03:00. Predict whether the project survives (attracts a non-founder truck-factor owner) over the followi...\",\n          \"output\": \"did_not_survive\",\n          \"metadata_repo\": \"OtusGolang/webinars_practical_part\",\n          \"metadata_founder\": \"anton.telishev@yandex.ru\",\n          \"metadata_tfdd_date\": \"2022-10-09T20:53:55+03:00\",\n          \"metadata_language\": \"Go\",\n          \"metadata_stars\": 103,\n          \"metadata_forks\": 64,\n          \"metadata_devs_at_tfdd\": 10,\n          \"metadata_commits_at_tfdd\": 119,\n          \"metadata_files_at_tfdd\": 881,\n          \"metadata_founder_share_pre_departure\": 0.07692307692307693,\n          \"metadata_n_diffused_owners_pre_departure\": 6,\n          \"metadata_placebo_founder_share\": 0.0,\n          \"metadata_placebo_n_diffused_owners\": 10,\n          \"metadata_grade\": \"maintained\",\n          \"metadata_censored\": false,\n          \"predict_our_method\": \"survived\",\n          \"predict_baseline\": \"did_not_survive\"\n        },\n        {\n          \"input\": \"Repo microsoft/D3D12TranslationLayer (C++): founder-only TFDD detected at 2021-04-03T20:13:47-07:00. Predict whether the project survives (attracts a non-founder truck-factor owner) over the following...\",\n          \"output\": \"did_not_survive\",\n          \"metadata_repo\": \"microsoft/D3D12TranslationLayer\",\n          \"metadata_founder\": \"jenatali@ntdev.microsoft.com\",\n          \"metadata_tfdd_date\": \"2021-04-03T20:13:47-07:00\",\n          \"metadata_language\": \"C++\",\n          \"metadata_stars\": 355,\n          \"metadata_forks\": 55,\n          \"metadata_devs_at_tfdd\": 5,\n          \"metadata_commits_at_tfdd\": 39,\n          \"metadata_files_at_tfdd\": 95,\n          \"metadata_founder_share_pre_departure\": 0.05,\n          \"metadata_n_diffused_owners_pre_departure\": 0,\n          \"metadata_placebo_founder_share\": 0.0,\n          \"metadata_placebo_n_diffused_owners\": 4,\n          \"metadata_grade\": \"maintained\",\n          \"metadata_censored\": false,\n          \"predict_our_method\": \"did_not_survive\",\n          \"predict_baseline\": \"did_not_survive\"\n        },\n        {\n          \"input\": \"Repo mrmlnc/fast-glob (JavaScript): founder-only TFDD detected at 2023-06-04T11:49:47+03:00. Predict whether the project survives (attracts a non-founder truck-factor owner) over the following 18 mont...\",\n          \"output\": \"did_not_survive\",\n          \"metadata_repo\": \"mrmlnc/fast-glob\",\n          \"metadata_founder\": \"mrmlnc@yandex-team.ru\",\n          \"metadata_tfdd_date\": \"2023-06-04T11:49:47+03:00\",\n          \"metadata_language\": \"JavaScript\",\n          \"metadata_stars\": 2823,\n          \"metadata_forks\": 141,\n          \"metadata_devs_at_tfdd\": 28,\n          \"metadata_commits_at_tfdd\": 560,\n          \"metadata_files_at_tfdd\": 281,\n          \"metadata_founder_share_pre_departure\": 0.3333333333333333,\n          \"metadata_n_diffused_owners_pre_departure\": 5,\n          \"metadata_placebo_founder_share\": NaN,\n          \"metadata_placebo_n_diffused_owners\": 0,\n          \"metadata_grade\": \"maintained\",\n          \"metadata_censored\": false,\n          \"predict_our_method\": \"survived\",\n          \"predict_baseline\": \"survived\"\n        }\n      ]\n    }\n  ]\n}\n---\n 3985 preview_method_out.json\n 4605 mini_method_out.json\n20897 full_method_out.json\n29487 total", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [14] TOOL CALL — Bash · 2026-08-21 21:35:20 UTC

```
cd /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1 && python3 -c "
import json
d=json.load(open('full_method_out.json'))
ex=d['datasets'][0]['examples']
print(len(ex))
print(list(ex[0].keys()))
"
ls results
cat results/method_summary.json | head -c 3000
```

### [15] TOOL RESULT — Bash · 2026-08-21 21:35:20 UTC

```
{"stdout": "16\n['input', 'output', 'metadata_repo', 'metadata_founder', 'metadata_tfdd_date', 'metadata_language', 'metadata_stars', 'metadata_forks', 'metadata_devs_at_tfdd', 'metadata_commits_at_tfdd', 'metadata_files_at_tfdd', 'metadata_founder_share_pre_departure', 'metadata_n_diffused_owners_pre_departure', 'metadata_placebo_founder_share', 'metadata_placebo_n_diffused_owners', 'metadata_grade', 'metadata_censored', 'predict_our_method', 'predict_baseline']\nmethod_summary.json\nrepo_processing_diagnostics.csv\n{\n  \"n_repos_sampled\": 270,\n  \"n_repos_filtered\": 69,\n  \"n_repos_processed\": 69,\n  \"n_founder_tfdd_events_strict\": 16,\n  \"n_founder_tfdd_events_relaxed\": 20,\n  \"strict_unconditioned_survival\": {\n    \"n_events\": 16,\n    \"n_uncensored\": 16,\n    \"n_censored_excluded\": 0,\n    \"survival_rate\": 0.3125,\n    \"survival_rate_se\": 0.11967838846954226\n  },\n  \"relaxed_unconditioned_survival\": {\n    \"n_events\": 20,\n    \"n_uncensored\": 20,\n    \"n_censored_excluded\": 0,\n    \"survival_rate\": 0.45,\n    \"survival_rate_se\": 0.11413288653790232\n  },\n  \"avelino_et_al_reference_survival_rate\": 0.41,\n  \"n_analysis_rows_strict\": 16,\n  \"n_analysis_rows_relaxed\": 20,\n  \"matched_pairs\": {\n    \"n_pairs\": 0,\n    \"risk_ratio_low_vs_high_diffusion\": NaN,\n    \"risk_ratio_ci95\": [\n      NaN,\n      NaN\n    ],\n    \"note\": \"risk_ratio = P(survival | low diffusion) / P(survival | high diffusion); >1 means low authority-diffusion (concentrated founder) survives MORE, <1 means diffusion helps survival\"\n  },\n  \"regression_our_method\": {\n    \"status\": \"ok\",\n    \"n\": 16,\n    \"covariates\": [\n      \"founder_share\",\n      \"n_diffused_owners\",\n      \"log_stars\",\n      \"log_devs_at_tfdd\"\n    ],\n    \"coefs\": {\n      \"const\": -4.475696556891135,\n      \"founder_share\": -5.557883893499619,\n      \"n_diffused_owners\": -0.17424518327751867,\n      \"log_stars\": 0.483117879817099,\n      \"log_devs_at_tfdd\": 0.824365581708137\n    },\n    \"pvalues\": {\n      \"const\": 0.218303341933911,\n      \"founder_share\": 0.42564837629682595,\n      \"n_diffused_owners\": 0.33959626313122593,\n      \"log_stars\": 0.4500889951416408,\n      \"log_devs_at_tfdd\": 0.634888137249151\n    },\n    \"pvalues_bh\": {\n      \"log_devs_at_tfdd\": 0.634888137249151,\n      \"log_stars\": 0.6001186601888544,\n      \"founder_share\": 0.6001186601888544,\n      \"n_diffused_owners\": 0.6001186601888544\n    },\n    \"standardized_effect_sizes\": {\n      \"founder_share\": -1.3214918000399904,\n      \"n_diffused_owners\": -1.3885056274134877,\n      \"log_stars\": 0.6451848689526228,\n      \"log_devs_at_tfdd\": 0.6766707272074415\n    },\n    \"pseudo_r2\": 0.17476537432367667,\n    \"converged\": true\n  },\n  \"regression_baseline_snapshot_only\": {\n    \"status\": \"ok\",\n    \"n\": 16,\n    \"covariates\": [\n      \"log_stars\",\n      \"log_forks\",\n      \"log_devs_at_tfdd\"\n    ],\n    \"coefs\": {\n      \"const\": -1.8952032516186004,\n      \"log_stars\": 1.3975084264153437,\n      \"log_forks\": -1.8646226615694212,\n      \"log_devs_at_tfdd\": 0.4021586010596022\n    },\n    \"pvalues\": {\n      \"const\": 0.5867567760651673,\n      \"log_stars\": 0.08043521853747629,\n      \"log_forks\": 0.17997701801104704,\n      \"log_devs_at_tfdd\": 0.7347455217911859\n    },\n    \"pvalues_bh\": {\n      \"log_devs_at_tfdd\": 0.7347455217911859,\n      \"log_forks\": 0.26996552701657056,\n      \"log_stars\": 0.24130565561242887\n    },\n    \"standardized_effect_sizes\": {\n      \"log_stars\": 1.8663173702002531,\n      \"log_forks\": -1.7499681093835084,\n      \"log_devs_at_tfdd\": 0.33010712609793785\n    },\n    \"pseudo_r2\": 0.21078560979385985,", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [16] TOOL CALL — Bash · 2026-08-21 21:35:28 UTC

```
cd /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_experiment_1 && python3 -c "
import json
d=json.load(open('full_method_out.json'))
ex=d['datasets'][0]['examples']
out={'metadata': d['metadata'], 'datasets':[{'dataset':'github_founder_tfdd_events','examples':ex}]}
json.dump(out, open('/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/mini_demo_data.json','w'), indent=2, default=str)
print('done', len(ex))
"
```

### [17] TOOL RESULT — Bash · 2026-08-21 21:35:28 UTC

```
{"stdout": "done 16", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [18] ASSISTANT · 2026-08-21 21:35:30 UTC

```
Now building the notebook.
```

### [19] TOOL CALL — ToolSearch · 2026-08-21 21:35:30 UTC

```
{'query': 'select:NotebookEdit', 'max_results': 1}
```

### [20] TOOL RESULT — ToolSearch · 2026-08-21 21:35:30 UTC

```
{"matches": ["NotebookEdit"], "query": "select:NotebookEdit", "total_deferred_tools": 22}
```

### [21] TOOL CALL — Write · 2026-08-21 21:35:34 UTC

```
File: /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb

{
 "cells": [],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.12.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

### [22] TOOL RESULT — Write · 2026-08-21 21:35:34 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb", "content": "{\n \"cells\": [],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [23] TOOL CALL — Read · 2026-08-21 21:35:34 UTC

```
/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb
```

### [24] TOOL RESULT — Read · 2026-08-21 21:35:34 UTC

```
{"type": "notebook", "file": {"filePath": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb", "cells": []}}
```

### [25] TOOL CALL — NotebookEdit · 2026-08-21 21:35:46 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb', 'cell_type': 'markdown', 'new_source': '# Does Founder Authority Diffusion Predict OSS Survival?\\n\\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.\'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\\n\\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\\n\\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\\n\\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \\"mini\\" here is the full analysis sample, not a truncation).\\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\\n- Recomputes Cohen\'s d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\\n\\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.'}
```

### [26] TOOL RESULT — NotebookEdit [ERROR] · 2026-08-21 21:35:46 UTC

```
Error: Cell ID must be specified when not inserting a new cell.
```

### [27] TOOL CALL — NotebookEdit · 2026-08-21 21:35:56 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': '# Does Founder Authority Diffusion Predict OSS Survival?\\n\\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.\'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\\n\\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\\n\\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\\n\\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \\"mini\\" here is the full analysis sample, not a truncation).\\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\\n- Recomputes Cohen\'s d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\\n\\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.'}
```

### [28] TOOL RESULT — NotebookEdit · 2026-08-21 21:35:56 UTC

```
{"new_source": "# Does Founder Authority Diffusion Predict OSS Survival?\\n\\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\\n\\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\\n\\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\\n\\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \\\"mini\\\" here is the full analysis sample, not a truncation).\\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\\n- Recomputes Cohen's d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\\n\\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "21b739c7", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb", "original_file": "{\n \"cells\": [],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}\n", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"21b739c7\",\n   \"source\": \"# Does Founder Authority Diffusion Predict OSS Survival?\\\\n\\\\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\\\\n\\\\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\\\\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\\\\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\\\\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\\\\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\\\\n\\\\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\\\\n\\\\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\\\\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \\\\\\\"mini\\\\\\\" here is the full analysis sample, not a truncation).\\\\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\\\\n- Recomputes Cohen's d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\\\\n\\\\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [29] ASSISTANT · 2026-08-21 21:36:02 UTC

```
Now cell 2: install dependencies.
```

### [30] TOOL CALL — NotebookEdit · 2026-08-21 21:36:02 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb', 'cell_id': '21b739c7', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': "import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru -- not pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')"}
```

### [31] TOOL RESULT — NotebookEdit · 2026-08-21 21:36:02 UTC

```
{"new_source": "import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru -- not pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "49615894", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"21b739c7\",\n   \"source\": \"# Does Founder Authority Diffusion Predict OSS Survival?\\\\n\\\\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\\\\n\\\\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\\\\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\\\\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\\\\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\\\\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\\\\n\\\\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\\\\n\\\\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\\\\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \\\\\\\"mini\\\\\\\" here is the full analysis sample, not a truncation).\\\\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\\\\n- Recomputes Cohen's d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\\\\n\\\\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"21b739c7\",\n   \"source\": \"# Does Founder Authority Diffusion Predict OSS Survival?\\\\n\\\\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\\\\n\\\\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\\\\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\\\\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\\\\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\\\\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\\\\n\\\\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\\\\n\\\\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\\\\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \\\\\\\"mini\\\\\\\" here is the full analysis sample, not a truncation).\\\\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\\\\n- Recomputes Cohen's d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\\\\n\\\\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"49615894\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# loguru -- not pre-installed on Colab, always install\\\\n_pip('loguru==0.7.3')\\\\n\\\\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [32] TOOL CALL — NotebookEdit · 2026-08-21 21:36:08 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb', 'cell_id': '49615894', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'from __future__ import annotations\\n\\nimport gc\\nimport json\\nimport math\\nimport random\\nimport sys\\nimport time\\nfrom collections import Counter, defaultdict\\nfrom dataclasses import asdict, dataclass, field\\nfrom datetime import datetime, timedelta, timezone\\nfrom pathlib import Path\\nfrom typing import Optional\\n\\nimport numpy as np\\nimport pandas as pd\\nimport statsmodels.api as sm\\nfrom loguru import logger\\nfrom scipy import stats\\n\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\"INFO\\", format=\\"{time:HH:mm:ss}|{level:<7}|{message}\\")\\n\\nRNG_SEED = 20260821\\nrandom.seed(RNG_SEED)\\nnp.random.seed(RNG_SEED)'}
```

### [33] TOOL RESULT — NotebookEdit · 2026-08-21 21:36:08 UTC

```
{"new_source": "from __future__ import annotations\\n\\nimport gc\\nimport json\\nimport math\\nimport random\\nimport sys\\nimport time\\nfrom collections import Counter, defaultdict\\nfrom dataclasses import asdict, dataclass, field\\nfrom datetime import datetime, timedelta, timezone\\nfrom pathlib import Path\\nfrom typing import Optional\\n\\nimport numpy as np\\nimport pandas as pd\\nimport statsmodels.api as sm\\nfrom loguru import logger\\nfrom scipy import stats\\n\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\\n\\nRNG_SEED = 20260821\\nrandom.seed(RNG_SEED)\\nnp.random.seed(RNG_SEED)", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "a74ae3ab", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"21b739c7\",\n   \"source\": \"# Does Founder Authority Diffusion Predict OSS Survival?\\\\n\\\\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\\\\n\\\\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\\\\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\\\\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\\\\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\\\\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\\\\n\\\\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\\\\n\\\\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\\\\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \\\\\\\"mini\\\\\\\" here is the full analysis sample, not a truncation).\\\\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\\\\n- Recomputes Cohen's d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\\\\n\\\\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"49615894\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# loguru -- not pre-installed on Colab, always install\\\\n_pip('loguru==0.7.3')\\\\n\\\\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"21b739c7\",\n   \"source\": \"# Does Founder Authority Diffusion Predict OSS Survival?\\\\n\\\\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\\\\n\\\\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\\\\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\\\\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\\\\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\\\\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\\\\n\\\\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\\\\n\\\\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\\\\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \\\\\\\"mini\\\\\\\" here is the full analysis sample, not a truncation).\\\\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\\\\n- Recomputes Cohen's d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\\\\n\\\\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"49615894\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# loguru -- not pre-installed on Colab, always install\\\\n_pip('loguru==0.7.3')\\\\n\\\\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"a74ae3ab\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass, field\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\n\\\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [34] ASSISTANT · 2026-08-21 21:36:12 UTC

```
Data loading helper and load cell:
```

### [35] TOOL CALL — NotebookEdit · 2026-08-21 21:36:12 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb', 'cell_id': 'a74ae3ab', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'GITHUB_DATA_URL = \\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\"mini_demo_data.json\\"):\\n        with open(\\"mini_demo_data.json\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\"Could not load mini_demo_data.json\\")'}
```

### [36] TOOL RESULT — NotebookEdit · 2026-08-21 21:36:14 UTC

```
{"new_source": "GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "621add7b", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"21b739c7\",\n   \"source\": \"# Does Founder Authority Diffusion Predict OSS Survival?\\\\n\\\\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\\\\n\\\\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\\\\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\\\\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\\\\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\\\\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\\\\n\\\\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\\\\n\\\\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\\\\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \\\\\\\"mini\\\\\\\" here is the full analysis sample, not a truncation).\\\\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\\\\n- Recomputes Cohen's d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\\\\n\\\\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"49615894\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# loguru -- not pre-installed on Colab, always install\\\\n_pip('loguru==0.7.3')\\\\n\\\\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"a74ae3ab\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass, field\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\n\\\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"21b739c7\",\n   \"source\": \"# Does Founder Authority Diffusion Predict OSS Survival?\\\\n\\\\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\\\\n\\\\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\\\\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\\\\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\\\\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\\\\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\\\\n\\\\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\\\\n\\\\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\\\\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \\\\\\\"mini\\\\\\\" here is the full analysis sample, not a truncation).\\\\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\\\\n- Recomputes Cohen's d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\\\\n\\\\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"49615894\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# loguru -- not pre-installed on Colab, always install\\\\n_pip('loguru==0.7.3')\\\\n\\\\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"a74ae3ab\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass, field\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\n\\\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"621add7b\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [37] TOOL CALL — NotebookEdit · 2026-08-21 21:36:16 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb', 'cell_id': '621add7b', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'raw = load_data()\\nprint(raw[\\"metadata\\"])\\nprint(\\"n examples:\\", len(raw[\\"datasets\\"][0][\\"examples\\"]))'}
```

### [38] TOOL RESULT — NotebookEdit · 2026-08-21 21:36:16 UTC

```
{"new_source": "raw = load_data()\\nprint(raw[\\\"metadata\\\"])\\nprint(\\\"n examples:\\\", len(raw[\\\"datasets\\\"][0][\\\"examples\\\"]))", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "6d655bb2", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"21b739c7\",\n   \"source\": \"# Does Founder Authority Diffusion Predict OSS Survival?\\\\n\\\\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\\\\n\\\\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\\\\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\\\\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\\\\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\\\\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\\\\n\\\\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\\\\n\\\\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\\\\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \\\\\\\"mini\\\\\\\" here is the full analysis sample, not a truncation).\\\\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\\\\n- Recomputes Cohen's d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\\\\n\\\\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"49615894\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# loguru -- not pre-installed on Colab, always install\\\\n_pip('loguru==0.7.3')\\\\n\\\\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"a74ae3ab\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass, field\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\n\\\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"621add7b\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"21b739c7\",\n   \"source\": \"# Does Founder Authority Diffusion Predict OSS Survival?\\\\n\\\\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\\\\n\\\\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\\\\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\\\\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\\\\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\\\\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\\\\n\\\\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\\\\n\\\\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\\\\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \\\\\\\"mini\\\\\\\" here is the full analysis sample, not a truncation).\\\\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\\\\n- Recomputes Cohen's d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\\\\n\\\\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"49615894\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# loguru -- not pre-installed on Colab, always install\\\\n_pip('loguru==0.7.3')\\\\n\\\\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"a74ae3ab\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass, field\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\n\\\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"621add7b\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"6d655bb2\",\n   \"source\": \"raw = load_data()\\\\nprint(raw[\\\\\\\"metadata\\\\\\\"])\\\\nprint(\\\\\\\"n examples:\\\\\\\", len(raw[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [39] ASSISTANT · 2026-08-21 21:36:20 UTC

```
Config markdown + cell:
```

### [40] TOOL CALL — NotebookEdit · 2026-08-21 21:36:20 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb', 'cell_id': '6d655bb2', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': "## Config\\n\\nAll tunable parameters from `method.py`'s Stage 5-8 analysis. `N_BOOT` (bootstrap resamples for the matched-pairs risk-ratio) is the only parameter worth scaling for a demo -- it starts small here and can be raised back to the original `5000` from the full run since the bootstrap over 16 rows is cheap either way."}
```

### [41] TOOL RESULT — NotebookEdit · 2026-08-21 21:36:20 UTC

```
{"new_source": "## Config\\n\\nAll tunable parameters from `method.py`'s Stage 5-8 analysis. `N_BOOT` (bootstrap resamples for the matched-pairs risk-ratio) is the only parameter worth scaling for a demo -- it starts small here and can be raised back to the original `5000` from the full run since the bootstrap over 16 rows is cheap either way.", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "5329a615", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"21b739c7\",\n   \"source\": \"# Does Founder Authority Diffusion Predict OSS Survival?\\\\n\\\\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\\\\n\\\\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\\\\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\\\\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\\\\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\\\\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\\\\n\\\\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\\\\n\\\\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\\\\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \\\\\\\"mini\\\\\\\" here is the full analysis sample, not a truncation).\\\\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\\\\n- Recomputes Cohen's d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\\\\n\\\\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"49615894\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# loguru -- not pre-installed on Colab, always install\\\\n_pip('loguru==0.7.3')\\\\n\\\\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"a74ae3ab\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass, field\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\n\\\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"621add7b\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"6d655bb2\",\n   \"source\": \"raw = load_data()\\\\nprint(raw[\\\\\\\"metadata\\\\\\\"])\\\\nprint(\\\\\\\"n examples:\\\\\\\", len(raw[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"21b739c7\",\n   \"source\": \"# Does Founder Authority Diffusion Predict OSS Survival?\\\\n\\\\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\\\\n\\\\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\\\\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\\\\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\\\\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\\\\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\\\\n\\\\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\\\\n\\\\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\\\\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \\\\\\\"mini\\\\\\\" here is the full analysis sample, not a truncation).\\\\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\\\\n- Recomputes Cohen's d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\\\\n\\\\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"49615894\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# loguru -- not pre-installed on Colab, always install\\\\n_pip('loguru==0.7.3')\\\\n\\\\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"a74ae3ab\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass, field\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\n\\\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"621add7b\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"6d655bb2\",\n   \"source\": \"raw = load_data()\\\\nprint(raw[\\\\\\\"metadata\\\\\\\"])\\\\nprint(\\\\\\\"n examples:\\\\\\\", len(raw[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"5329a615\",\n   \"source\": \"## Config\\\\n\\\\nAll tunable parameters from `method.py`'s Stage 5-8 analysis. `N_BOOT` (bootstrap resamples for the matched-pairs risk-ratio) is the only parameter worth scaling for a demo -- it starts small here and can be raised back to the original `5000` from the full run since the bootstrap over 16 rows is cheap either way.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [42] TOOL CALL — NotebookEdit · 2026-08-21 21:36:28 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb', 'cell_id': '5329a615', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': "# Avelino et al.'s TFDD silence threshold / truck-factor coverage cutoff (unused directly in this notebook's\\n# Stage 5-8 recomputation but kept for reference -- these determined the pre-computed event data)\\nSILENCE_THRESHOLD_DAYS = 365\\nTF_COVERAGE_THRESHOLD = 0.5\\nPOST_TFDD_WINDOW_DAYS = 548  # 18 months\\nPRE_WINDOW_FAR_DAYS = 365  # 12 months before TFDD\\nPRE_WINDOW_NEAR_DAYS = 180  # 6 months before TFDD\\n\\n# matched-pairs thresholds (Stage 8)\\nMATCHED_PAIRS_LOW_THRESH = 0.50\\nMATCHED_PAIRS_HI_THRESH = 0.80\\nMATCHED_PAIRS_N_DIFFUSED_MIN = 2\\n\\n# bootstrap resamples for the risk-ratio CI -- START SMALL, scale back to 5000 (original) after it runs\\nN_BOOT = 200  # original value: 5000"}
```

### [43] TOOL RESULT — NotebookEdit · 2026-08-21 21:36:28 UTC

```
{"new_source": "# Avelino et al.'s TFDD silence threshold / truck-factor coverage cutoff (unused directly in this notebook's\\n# Stage 5-8 recomputation but kept for reference -- these determined the pre-computed event data)\\nSILENCE_THRESHOLD_DAYS = 365\\nTF_COVERAGE_THRESHOLD = 0.5\\nPOST_TFDD_WINDOW_DAYS = 548  # 18 months\\nPRE_WINDOW_FAR_DAYS = 365  # 12 months before TFDD\\nPRE_WINDOW_NEAR_DAYS = 180  # 6 months before TFDD\\n\\n# matched-pairs thresholds (Stage 8)\\nMATCHED_PAIRS_LOW_THRESH = 0.50\\nMATCHED_PAIRS_HI_THRESH = 0.80\\nMATCHED_PAIRS_N_DIFFUSED_MIN = 2\\n\\n# bootstrap resamples for the risk-ratio CI -- START SMALL, scale back to 5000 (original) after it runs\\nN_BOOT = 200  # original value: 5000", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "6eb4d2a3", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"21b739c7\",\n   \"source\": \"# Does Founder Authority Diffusion Predict OSS Survival?\\\\n\\\\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\\\\n\\\\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\\\\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\\\\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\\\\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\\\\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\\\\n\\\\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\\\\n\\\\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\\\\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \\\\\\\"mini\\\\\\\" here is the full analysis sample, not a truncation).\\\\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\\\\n- Recomputes Cohen's d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\\\\n\\\\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"49615894\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# loguru -- not pre-installed on Colab, always install\\\\n_pip('loguru==0.7.3')\\\\n\\\\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"a74ae3ab\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass, field\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\n\\\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"621add7b\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"6d655bb2\",\n   \"source\": \"raw = load_data()\\\\nprint(raw[\\\\\\\"metadata\\\\\\\"])\\\\nprint(\\\\\\\"n examples:\\\\\\\", len(raw[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"5329a615\",\n   \"source\": \"## Config\\\\n\\\\nAll tunable parameters from `method.py`'s Stage 5-8 analysis. `N_BOOT` (bootstrap resamples for the matched-pairs risk-ratio) is the only parameter worth scaling for a demo -- it starts small here and can be raised back to the original `5000` from the full run since the bootstrap over 16 rows is cheap either way.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"21b739c7\",\n   \"source\": \"# Does Founder Authority Diffusion Predict OSS Survival?\\\\n\\\\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\\\\n\\\\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\\\\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\\\\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\\\\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\\\\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\\\\n\\\\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\\\\n\\\\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\\\\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \\\\\\\"mini\\\\\\\" here is the full analysis sample, not a truncation).\\\\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\\\\n- Recomputes Cohen's d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\\\\n\\\\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"49615894\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# loguru -- not pre-installed on Colab, always install\\\\n_pip('loguru==0.7.3')\\\\n\\\\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"a74ae3ab\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass, field\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\n\\\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"621add7b\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"6d655bb2\",\n   \"source\": \"raw = load_data()\\\\nprint(raw[\\\\\\\"metadata\\\\\\\"])\\\\nprint(\\\\\\\"n examples:\\\\\\\", len(raw[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"5329a615\",\n   \"source\": \"## Config\\\\n\\\\nAll tunable parameters from `method.py`'s Stage 5-8 analysis. `N_BOOT` (bootstrap resamples for the matched-pairs risk-ratio) is the only parameter worth scaling for a demo -- it starts small here and can be raised back to the original `5000` from the full run since the bootstrap over 16 rows is cheap either way.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"6eb4d2a3\",\n   \"source\": \"# Avelino et al.'s TFDD silence threshold / truck-factor coverage cutoff (unused directly in this notebook's\\\\n# Stage 5-8 recomputation but kept for reference -- these determined the pre-computed event data)\\\\nSILENCE_THRESHOLD_DAYS = 365\\\\nTF_COVERAGE_THRESHOLD = 0.5\\\\nPOST_TFDD_WINDOW_DAYS = 548  # 18 months\\\\nPRE_WINDOW_FAR_DAYS = 365  # 12 months before TFDD\\\\nPRE_WINDOW_NEAR_DAYS = 180  # 6 months before TFDD\\\\n\\\\n# matched-pairs thresholds (Stage 8)\\\\nMATCHED_PAIRS_LOW_THRESH = 0.50\\\\nMATCHED_PAIRS_HI_THRESH = 0.80\\\\nMATCHED_PAIRS_N_DIFFUSED_MIN = 2\\\\n\\\\n# bootstrap resamples for the risk-ratio CI -- START SMALL, scale back to 5000 (original) after it runs\\\\nN_BOOT = 200  # original value: 5000\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [44] ASSISTANT · 2026-08-21 21:36:34 UTC

```
Now processing cells: rebuild dataframe from examples (mirrors `events_to_df`).
```

### [45] TOOL CALL — NotebookEdit · 2026-08-21 21:36:34 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb', 'cell_id': '6eb4d2a3', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': "## Rebuild the analysis dataframe (Stage 6 output format)\\n\\nEach loaded example is one strict founder-only TFDD event, with the fields `method.py`'s `events_to_df()` used to build its regression dataframe (`stars`, `forks`, `devs_at_tfdd`, `founder_share`, `n_diffused_owners`, `survived`, plus placebo-window fields). We reconstruct that same dataframe here, including the log-transformed covariates (`log_stars`, `log_forks`, `log_devs_at_tfdd`) `method.py` derives before fitting."}
```

### [46] TOOL RESULT — NotebookEdit · 2026-08-21 21:36:34 UTC

```
{"new_source": "## Rebuild the analysis dataframe (Stage 6 output format)\\n\\nEach loaded example is one strict founder-only TFDD event, with the fields `method.py`'s `events_to_df()` used to build its regression dataframe (`stars`, `forks`, `devs_at_tfdd`, `founder_share`, `n_diffused_owners`, `survived`, plus placebo-window fields). We reconstruct that same dataframe here, including the log-transformed covariates (`log_stars`, `log_forks`, `log_devs_at_tfdd`) `method.py` derives before fitting.", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "a6cf6d5d", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"21b739c7\",\n   \"source\": \"# Does Founder Authority Diffusion Predict OSS Survival?\\\\n\\\\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\\\\n\\\\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\\\\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\\\\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\\\\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\\\\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\\\\n\\\\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\\\\n\\\\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\\\\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \\\\\\\"mini\\\\\\\" here is the full analysis sample, not a truncation).\\\\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\\\\n- Recomputes Cohen's d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\\\\n\\\\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"49615894\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# loguru -- not pre-installed on Colab, always install\\\\n_pip('loguru==0.7.3')\\\\n\\\\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"a74ae3ab\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass, field\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\n\\\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"621add7b\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"6d655bb2\",\n   \"source\": \"raw = load_data()\\\\nprint(raw[\\\\\\\"metadata\\\\\\\"])\\\\nprint(\\\\\\\"n examples:\\\\\\\", len(raw[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"5329a615\",\n   \"source\": \"## Config\\\\n\\\\nAll tunable parameters from `method.py`'s Stage 5-8 analysis. `N_BOOT` (bootstrap resamples for the matched-pairs risk-ratio) is the only parameter worth scaling for a demo -- it starts small here and can be raised back to the original `5000` from the full run since the bootstrap over 16 rows is cheap either way.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"6eb4d2a3\",\n   \"source\": \"# Avelino et al.'s TFDD silence threshold / truck-factor coverage cutoff (unused directly in this notebook's\\\\n# Stage 5-8 recomputation but kept for reference -- these determined the pre-computed event data)\\\\nSILENCE_THRESHOLD_DAYS = 365\\\\nTF_COVERAGE_THRESHOLD = 0.5\\\\nPOST_TFDD_WINDOW_DAYS = 548  # 18 months\\\\nPRE_WINDOW_FAR_DAYS = 365  # 12 months before TFDD\\\\nPRE_WINDOW_NEAR_DAYS = 180  # 6 months before TFDD\\\\n\\\\n# matched-pairs thresholds (Stage 8)\\\\nMATCHED_PAIRS_LOW_THRESH = 0.50\\\\nMATCHED_PAIRS_HI_THRESH = 0.80\\\\nMATCHED_PAIRS_N_DIFFUSED_MIN = 2\\\\n\\\\n# bootstrap resamples for the risk-ratio CI -- START SMALL, scale back to 5000 (original) after it runs\\\\nN_BOOT = 200  # original value: 5000\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"21b739c7\",\n   \"source\": \"# Does Founder Authority Diffusion Predict OSS Survival?\\\\n\\\\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\\\\n\\\\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\\\\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\\\\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\\\\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\\\\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\\\\n\\\\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\\\\n\\\\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\\\\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \\\\\\\"mini\\\\\\\" here is the full analysis sample, not a truncation).\\\\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\\\\n- Recomputes Cohen's d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\\\\n\\\\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"49615894\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# loguru -- not pre-installed on Colab, always install\\\\n_pip('loguru==0.7.3')\\\\n\\\\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"a74ae3ab\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass, field\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\n\\\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"621add7b\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"6d655bb2\",\n   \"source\": \"raw = load_data()\\\\nprint(raw[\\\\\\\"metadata\\\\\\\"])\\\\nprint(\\\\\\\"n examples:\\\\\\\", len(raw[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"5329a615\",\n   \"source\": \"## Config\\\\n\\\\nAll tunable parameters from `method.py`'s Stage 5-8 analysis. `N_BOOT` (bootstrap resamples for the matched-pairs risk-ratio) is the only parameter worth scaling for a demo -- it starts small here and can be raised back to the original `5000` from the full run since the bootstrap over 16 rows is cheap either way.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"6eb4d2a3\",\n   \"source\": \"# Avelino et al.'s TFDD silence threshold / truck-factor coverage cutoff (unused directly in this notebook's\\\\n# Stage 5-8 recomputation but kept for reference -- these determined the pre-computed event data)\\\\nSILENCE_THRESHOLD_DAYS = 365\\\\nTF_COVERAGE_THRESHOLD = 0.5\\\\nPOST_TFDD_WINDOW_DAYS = 548  # 18 months\\\\nPRE_WINDOW_FAR_DAYS = 365  # 12 months before TFDD\\\\nPRE_WINDOW_NEAR_DAYS = 180  # 6 months before TFDD\\\\n\\\\n# matched-pairs thresholds (Stage 8)\\\\nMATCHED_PAIRS_LOW_THRESH = 0.50\\\\nMATCHED_PAIRS_HI_THRESH = 0.80\\\\nMATCHED_PAIRS_N_DIFFUSED_MIN = 2\\\\n\\\\n# bootstrap resamples for the risk-ratio CI -- START SMALL, scale back to 5000 (original) after it runs\\\\nN_BOOT = 200  # original value: 5000\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"a6cf6d5d\",\n   \"source\": \"## Rebuild the analysis dataframe (Stage 6 output format)\\\\n\\\\nEach loaded example is one strict founder-only TFDD event, with the fields `method.py`'s `events_to_df()` used to build its regression dataframe (`stars`, `forks`, `devs_at_tfdd`, `founder_share`, `n_diffused_owners`, `survived`, plus placebo-window fields). We reconstruct that same dataframe here, including the log-transformed covariates (`log_stars`, `log_forks`, `log_devs_at_tfdd`) `method.py` derives before fitting.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [47] TOOL CALL — NotebookEdit · 2026-08-21 21:36:42 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb', 'cell_id': 'a6cf6d5d', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'examples = raw[\\"datasets\\"][0][\\"examples\\"]\\n\\nrows = []\\nfor e in examples:\\n    if \\"metadata_repo\\" not in e:\\n        continue  # skip the schema-required placeholder row if no events were found\\n    rows.append({\\n        \\"repo\\": e[\\"metadata_repo\\"],\\n        \\"founder\\": e[\\"metadata_founder\\"],\\n        \\"tfdd_date\\": e[\\"metadata_tfdd_date\\"],\\n        \\"language\\": e[\\"metadata_language\\"],\\n        \\"stars\\": e[\\"metadata_stars\\"],\\n        \\"forks\\": e[\\"metadata_forks\\"],\\n        \\"devs_at_tfdd\\": e[\\"metadata_devs_at_tfdd\\"],\\n        \\"commits_at_tfdd\\": e[\\"metadata_commits_at_tfdd\\"],\\n        \\"files_at_tfdd\\": e[\\"metadata_files_at_tfdd\\"],\\n        \\"founder_share\\": e[\\"metadata_founder_share_pre_departure\\"],\\n        \\"n_diffused_owners\\": e[\\"metadata_n_diffused_owners_pre_departure\\"],\\n        \\"placebo_founder_share\\": e[\\"metadata_placebo_founder_share\\"],\\n        \\"placebo_n_diffused_owners\\": e[\\"metadata_placebo_n_diffused_owners\\"],\\n        \\"grade\\": e[\\"metadata_grade\\"],\\n        \\"censored\\": e[\\"metadata_censored\\"],\\n        \\"survived\\": e[\\"output\\"] == \\"survived\\",\\n    })\\n\\ndf = pd.DataFrame(rows)\\ndf[\\"tfdd_date\\"] = pd.to_datetime(df[\\"tfdd_date\\"], utc=True)\\ndf[\\"log_stars\\"] = np.log1p(df[\\"stars\\"])\\ndf[\\"log_forks\\"] = np.log1p(df[\\"forks\\"])\\ndf[\\"log_devs_at_tfdd\\"] = np.log1p(df[\\"devs_at_tfdd\\"])\\ndf = df.dropna(subset=[\\"founder_share\\", \\"n_diffused_owners\\", \\"log_stars\\", \\"log_forks\\", \\"devs_at_tfdd\\"])\\nprint(f\\"analysis dataframe: {len(df)} strict founder-only TFDD events\\")\\ndf.head()'}
```

### [48] TOOL RESULT — NotebookEdit · 2026-08-21 21:36:42 UTC

```
{"new_source": "examples = raw[\\\"datasets\\\"][0][\\\"examples\\\"]\\n\\nrows = []\\nfor e in examples:\\n    if \\\"metadata_repo\\\" not in e:\\n        continue  # skip the schema-required placeholder row if no events were found\\n    rows.append({\\n        \\\"repo\\\": e[\\\"metadata_repo\\\"],\\n        \\\"founder\\\": e[\\\"metadata_founder\\\"],\\n        \\\"tfdd_date\\\": e[\\\"metadata_tfdd_date\\\"],\\n        \\\"language\\\": e[\\\"metadata_language\\\"],\\n        \\\"stars\\\": e[\\\"metadata_stars\\\"],\\n        \\\"forks\\\": e[\\\"metadata_forks\\\"],\\n        \\\"devs_at_tfdd\\\": e[\\\"metadata_devs_at_tfdd\\\"],\\n        \\\"commits_at_tfdd\\\": e[\\\"metadata_commits_at_tfdd\\\"],\\n        \\\"files_at_tfdd\\\": e[\\\"metadata_files_at_tfdd\\\"],\\n        \\\"founder_share\\\": e[\\\"metadata_founder_share_pre_departure\\\"],\\n        \\\"n_diffused_owners\\\": e[\\\"metadata_n_diffused_owners_pre_departure\\\"],\\n        \\\"placebo_founder_share\\\": e[\\\"metadata_placebo_founder_share\\\"],\\n        \\\"placebo_n_diffused_owners\\\": e[\\\"metadata_placebo_n_diffused_owners\\\"],\\n        \\\"grade\\\": e[\\\"metadata_grade\\\"],\\n        \\\"censored\\\": e[\\\"metadata_censored\\\"],\\n        \\\"survived\\\": e[\\\"output\\\"] == \\\"survived\\\",\\n    })\\n\\ndf = pd.DataFrame(rows)\\ndf[\\\"tfdd_date\\\"] = pd.to_datetime(df[\\\"tfdd_date\\\"], utc=True)\\ndf[\\\"log_stars\\\"] = np.log1p(df[\\\"stars\\\"])\\ndf[\\\"log_forks\\\"] = np.log1p(df[\\\"forks\\\"])\\ndf[\\\"log_devs_at_tfdd\\\"] = np.log1p(df[\\\"devs_at_tfdd\\\"])\\ndf = df.dropna(subset=[\\\"founder_share\\\", \\\"n_diffused_owners\\\", \\\"log_stars\\\", \\\"log_forks\\\", \\\"devs_at_tfdd\\\"])\\nprint(f\\\"analysis dataframe: {len(df)} strict founder-only TFDD events\\\")\\ndf.head()", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "a0366ece", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"21b739c7\",\n   \"source\": \"# Does Founder Authority Diffusion Predict OSS Survival?\\\\n\\\\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\\\\n\\\\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\\\\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\\\\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\\\\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\\\\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\\\\n\\\\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\\\\n\\\\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\\\\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \\\\\\\"mini\\\\\\\" here is the full analysis sample, not a truncation).\\\\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\\\\n- Recomputes Cohen's d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\\\\n\\\\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"49615894\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# loguru -- not pre-installed on Colab, always install\\\\n_pip('loguru==0.7.3')\\\\n\\\\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"a74ae3ab\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass, field\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\n\\\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"621add7b\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"6d655bb2\",\n   \"source\": \"raw = load_data()\\\\nprint(raw[\\\\\\\"metadata\\\\\\\"])\\\\nprint(\\\\\\\"n examples:\\\\\\\", len(raw[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"5329a615\",\n   \"source\": \"## Config\\\\n\\\\nAll tunable parameters from `method.py`'s Stage 5-8 analysis. `N_BOOT` (bootstrap resamples for the matched-pairs risk-ratio) is the only parameter worth scaling for a demo -- it starts small here and can be raised back to the original `5000` from the full run since the bootstrap over 16 rows is cheap either way.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"6eb4d2a3\",\n   \"source\": \"# Avelino et al.'s TFDD silence threshold / truck-factor coverage cutoff (unused directly in this notebook's\\\\n# Stage 5-8 recomputation but kept for reference -- these determined the pre-computed event data)\\\\nSILENCE_THRESHOLD_DAYS = 365\\\\nTF_COVERAGE_THRESHOLD = 0.5\\\\nPOST_TFDD_WINDOW_DAYS = 548  # 18 months\\\\nPRE_WINDOW_FAR_DAYS = 365  # 12 months before TFDD\\\\nPRE_WINDOW_NEAR_DAYS = 180  # 6 months before TFDD\\\\n\\\\n# matched-pairs thresholds (Stage 8)\\\\nMATCHED_PAIRS_LOW_THRESH = 0.50\\\\nMATCHED_PAIRS_HI_THRESH = 0.80\\\\nMATCHED_PAIRS_N_DIFFUSED_MIN = 2\\\\n\\\\n# bootstrap resamples for the risk-ratio CI -- START SMALL, scale back to 5000 (original) after it runs\\\\nN_BOOT = 200  # original value: 5000\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"a6cf6d5d\",\n   \"source\": \"## Rebuild the analysis dataframe (Stage 6 output format)\\\\n\\\\nEach loaded example is one strict founder-only TFDD event, with the fields `method.py`'s `events_to_df()` used to build its regression dataframe (`stars`, `forks`, `devs_at_tfdd`, `founder_share`, `n_diffused_owners`, `survived`, plus placebo-window fields). We reconstruct that same dataframe here, including the log-transformed covariates (`log_stars`, `log_forks`, `log_devs_at_tfdd`) `method.py` derives before fitting.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"21b739c7\",\n   \"source\": \"# Does Founder Authority Diffusion Predict OSS Survival?\\\\n\\\\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\\\\n\\\\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\\\\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\\\\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\\\\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\\\\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\\\\n\\\\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\\\\n\\\\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\\\\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \\\\\\\"mini\\\\\\\" here is the full analysis sample, not a truncation).\\\\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\\\\n- Recomputes Cohen's d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\\\\n\\\\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"49615894\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# loguru -- not pre-installed on Colab, always install\\\\n_pip('loguru==0.7.3')\\\\n\\\\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"a74ae3ab\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass, field\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\n\\\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"621add7b\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"6d655bb2\",\n   \"source\": \"raw = load_data()\\\\nprint(raw[\\\\\\\"metadata\\\\\\\"])\\\\nprint(\\\\\\\"n examples:\\\\\\\", len(raw[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"5329a615\",\n   \"source\": \"## Config\\\\n\\\\nAll tunable parameters from `method.py`'s Stage 5-8 analysis. `N_BOOT` (bootstrap resamples for the matched-pairs risk-ratio) is the only parameter worth scaling for a demo -- it starts small here and can be raised back to the original `5000` from the full run since the bootstrap over 16 rows is cheap either way.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"6eb4d2a3\",\n   \"source\": \"# Avelino et al.'s TFDD silence threshold / truck-factor coverage cutoff (unused directly in this notebook's\\\\n# Stage 5-8 recomputation but kept for reference -- these determined the pre-computed event data)\\\\nSILENCE_THRESHOLD_DAYS = 365\\\\nTF_COVERAGE_THRESHOLD = 0.5\\\\nPOST_TFDD_WINDOW_DAYS = 548  # 18 months\\\\nPRE_WINDOW_FAR_DAYS = 365  # 12 months before TFDD\\\\nPRE_WINDOW_NEAR_DAYS = 180  # 6 months before TFDD\\\\n\\\\n# matched-pairs thresholds (Stage 8)\\\\nMATCHED_PAIRS_LOW_THRESH = 0.50\\\\nMATCHED_PAIRS_HI_THRESH = 0.80\\\\nMATCHED_PAIRS_N_DIFFUSED_MIN = 2\\\\n\\\\n# bootstrap resamples for the risk-ratio CI -- START SMALL, scale back to 5000 (original) after it runs\\\\nN_BOOT = 200  # original value: 5000\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"a6cf6d5d\",\n   \"source\": \"## Rebuild the analysis dataframe (Stage 6 output format)\\\\n\\\\nEach loaded example is one strict founder-only TFDD event, with the fields `method.py`'s `events_to_df()` used to build its regression dataframe (`stars`, `forks`, `devs_at_tfdd`, `founder_share`, `n_diffused_owners`, `survived`, plus placebo-window fields). We reconstruct that same dataframe here, including the log-transformed covariates (`log_stars`, `log_forks`, `log_devs_at_tfdd`) `method.py` derives before fitting.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"a0366ece\",\n   \"source\": \"examples = raw[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]\\\\n\\\\nrows = []\\\\nfor e in examples:\\\\n    if \\\\\\\"metadata_repo\\\\\\\" not in e:\\\\n        continue  # skip the schema-required placeholder row if no events were found\\\\n    rows.append({\\\\n        \\\\\\\"repo\\\\\\\": e[\\\\\\\"metadata_repo\\\\\\\"],\\\\n        \\\\\\\"founder\\\\\\\": e[\\\\\\\"metadata_founder\\\\\\\"],\\\\n        \\\\\\\"tfdd_date\\\\\\\": e[\\\\\\\"metadata_tfdd_date\\\\\\\"],\\\\n        \\\\\\\"language\\\\\\\": e[\\\\\\\"metadata_language\\\\\\\"],\\\\n        \\\\\\\"stars\\\\\\\": e[\\\\\\\"metadata_stars\\\\\\\"],\\\\n        \\\\\\\"forks\\\\\\\": e[\\\\\\\"metadata_forks\\\\\\\"],\\\\n        \\\\\\\"devs_at_tfdd\\\\\\\": e[\\\\\\\"metadata_devs_at_tfdd\\\\\\\"],\\\\n        \\\\\\\"commits_at_tfdd\\\\\\\": e[\\\\\\\"metadata_commits_at_tfdd\\\\\\\"],\\\\n        \\\\\\\"files_at_tfdd\\\\\\\": e[\\\\\\\"metadata_files_at_tfdd\\\\\\\"],\\\\n        \\\\\\\"founder_share\\\\\\\": e[\\\\\\\"metadata_founder_share_pre_departure\\\\\\\"],\\\\n        \\\\\\\"n_diffused_owners\\\\\\\": e[\\\\\\\"metadata_n_diffused_owners_pre_departure\\\\\\\"],\\\\n        \\\\\\\"placebo_founder_share\\\\\\\": e[\\\\\\\"metadata_placebo_founder_share\\\\\\\"],\\\\n        \\\\\\\"placebo_n_diffused_owners\\\\\\\": e[\\\\\\\"metadata_placebo_n_diffused_owners\\\\\\\"],\\\\n        \\\\\\\"grade\\\\\\\": e[\\\\\\\"metadata_grade\\\\\\\"],\\\\n        \\\\\\\"censored\\\\\\\": e[\\\\\\\"metadata_censored\\\\\\\"],\\\\n        \\\\\\\"survived\\\\\\\": e[\\\\\\\"output\\\\\\\"] == \\\\\\\"survived\\\\\\\",\\\\n    })\\\\n\\\\ndf = pd.DataFrame(rows)\\\\ndf[\\\\\\\"tfdd_date\\\\\\\"] = pd.to_datetime(df[\\\\\\\"tfdd_date\\\\\\\"], utc=True)\\\\ndf[\\\\\\\"log_stars\\\\\\\"] = np.log1p(df[\\\\\\\"stars\\\\\\\"])\\\\ndf[\\\\\\\"log_forks\\\\\\\"] = np.log1p(df[\\\\\\\"forks\\\\\\\"])\\\\ndf[\\\\\\\"log_devs_at_tfdd\\\\\\\"] = np.log1p(df[\\\\\\\"devs_at_tfdd\\\\\\\"])\\\\ndf = df.dropna(subset=[\\\\\\\"founder_share\\\\\\\", \\\\\\\"n_diffused_owners\\\\\\\", \\\\\\\"log_stars\\\\\\\", \\\\\\\"log_forks\\\\\\\", \\\\\\\"devs_at_tfdd\\\\\\\"])\\\\nprint(f\\\\\\\"analysis dataframe: {len(df)} strict founder-only TFDD events\\\\\\\")\\\\ndf.head()\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [49] ASSISTANT · 2026-08-21 21:36:48 UTC

```
Next: Stage 8 helper functions (copied verbatim from method.py), then regression cells.
```

### [50] TOOL CALL — NotebookEdit · 2026-08-21 21:36:48 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb', 'cell_id': 'a0366ece', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': '## Stage 8 helper functions (copied unchanged from `method.py`)\\n\\n`build_matched_pairs`, `bootstrap_survival_rate_ratio`, `benjamini_hochberg`, and `cohens_d` -- the exact same functions the full pipeline run used to produce its reported numbers.'}
```

### [51] TOOL RESULT — NotebookEdit · 2026-08-21 21:36:48 UTC

```
{"new_source": "## Stage 8 helper functions (copied unchanged from `method.py`)\\n\\n`build_matched_pairs`, `bootstrap_survival_rate_ratio`, `benjamini_hochberg`, and `cohens_d` -- the exact same functions the full pipeline run used to produce its reported numbers.", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "dbf99636", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"21b739c7\",\n   \"source\": \"# Does Founder Authority Diffusion Predict OSS Survival?\\\\n\\\\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\\\\n\\\\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\\\\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\\\\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\\\\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\\\\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\\\\n\\\\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\\\\n\\\\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\\\\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \\\\\\\"mini\\\\\\\" here is the full analysis sample, not a truncation).\\\\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\\\\n- Recomputes Cohen's d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\\\\n\\\\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"49615894\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# loguru -- not pre-installed on Colab, always install\\\\n_pip('loguru==0.7.3')\\\\n\\\\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"a74ae3ab\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass, field\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\n\\\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"621add7b\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"6d655bb2\",\n   \"source\": \"raw = load_data()\\\\nprint(raw[\\\\\\\"metadata\\\\\\\"])\\\\nprint(\\\\\\\"n examples:\\\\\\\", len(raw[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"5329a615\",\n   \"source\": \"## Config\\\\n\\\\nAll tunable parameters from `method.py`'s Stage 5-8 analysis. `N_BOOT` (bootstrap resamples for the matched-pairs risk-ratio) is the only parameter worth scaling for a demo -- it starts small here and can be raised back to the original `5000` from the full run since the bootstrap over 16 rows is cheap either way.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"6eb4d2a3\",\n   \"source\": \"# Avelino et al.'s TFDD silence threshold / truck-factor coverage cutoff (unused directly in this notebook's\\\\n# Stage 5-8 recomputation but kept for reference -- these determined the pre-computed event data)\\\\nSILENCE_THRESHOLD_DAYS = 365\\\\nTF_COVERAGE_THRESHOLD = 0.5\\\\nPOST_TFDD_WINDOW_DAYS = 548  # 18 months\\\\nPRE_WINDOW_FAR_DAYS = 365  # 12 months before TFDD\\\\nPRE_WINDOW_NEAR_DAYS = 180  # 6 months before TFDD\\\\n\\\\n# matched-pairs thresholds (Stage 8)\\\\nMATCHED_PAIRS_LOW_THRESH = 0.50\\\\nMATCHED_PAIRS_HI_THRESH = 0.80\\\\nMATCHED_PAIRS_N_DIFFUSED_MIN = 2\\\\n\\\\n# bootstrap resamples for the risk-ratio CI -- START SMALL, scale back to 5000 (original) after it runs\\\\nN_BOOT = 200  # original value: 5000\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"a6cf6d5d\",\n   \"source\": \"## Rebuild the analysis dataframe (Stage 6 output format)\\\\n\\\\nEach loaded example is one strict founder-only TFDD event, with the fields `method.py`'s `events_to_df()` used to build its regression dataframe (`stars`, `forks`, `devs_at_tfdd`, `founder_share`, `n_diffused_owners`, `survived`, plus placebo-window fields). We reconstruct that same dataframe here, including the log-transformed covariates (`log_stars`, `log_forks`, `log_devs_at_tfdd`) `method.py` derives before fitting.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"a0366ece\",\n   \"source\": \"examples = raw[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]\\\\n\\\\nrows = []\\\\nfor e in examples:\\\\n    if \\\\\\\"metadata_repo\\\\\\\" not in e:\\\\n        continue  # skip the schema-required placeholder row if no events were found\\\\n    rows.append({\\\\n        \\\\\\\"repo\\\\\\\": e[\\\\\\\"metadata_repo\\\\\\\"],\\\\n        \\\\\\\"founder\\\\\\\": e[\\\\\\\"metadata_founder\\\\\\\"],\\\\n        \\\\\\\"tfdd_date\\\\\\\": e[\\\\\\\"metadata_tfdd_date\\\\\\\"],\\\\n        \\\\\\\"language\\\\\\\": e[\\\\\\\"metadata_language\\\\\\\"],\\\\n        \\\\\\\"stars\\\\\\\": e[\\\\\\\"metadata_stars\\\\\\\"],\\\\n        \\\\\\\"forks\\\\\\\": e[\\\\\\\"metadata_forks\\\\\\\"],\\\\n        \\\\\\\"devs_at_tfdd\\\\\\\": e[\\\\\\\"metadata_devs_at_tfdd\\\\\\\"],\\\\n        \\\\\\\"commits_at_tfdd\\\\\\\": e[\\\\\\\"metadata_commits_at_tfdd\\\\\\\"],\\\\n        \\\\\\\"files_at_tfdd\\\\\\\": e[\\\\\\\"metadata_files_at_tfdd\\\\\\\"],\\\\n        \\\\\\\"founder_share\\\\\\\": e[\\\\\\\"metadata_founder_share_pre_departure\\\\\\\"],\\\\n        \\\\\\\"n_diffused_owners\\\\\\\": e[\\\\\\\"metadata_n_diffused_owners_pre_departure\\\\\\\"],\\\\n        \\\\\\\"placebo_founder_share\\\\\\\": e[\\\\\\\"metadata_placebo_founder_share\\\\\\\"],\\\\n        \\\\\\\"placebo_n_diffused_owners\\\\\\\": e[\\\\\\\"metadata_placebo_n_diffused_owners\\\\\\\"],\\\\n        \\\\\\\"grade\\\\\\\": e[\\\\\\\"metadata_grade\\\\\\\"],\\\\n        \\\\\\\"censored\\\\\\\": e[\\\\\\\"metadata_censored\\\\\\\"],\\\\n        \\\\\\\"survived\\\\\\\": e[\\\\\\\"output\\\\\\\"] == \\\\\\\"survived\\\\\\\",\\\\n    })\\\\n\\\\ndf = pd.DataFrame(rows)\\\\ndf[\\\\\\\"tfdd_date\\\\\\\"] = pd.to_datetime(df[\\\\\\\"tfdd_date\\\\\\\"], utc=True)\\\\ndf[\\\\\\\"log_stars\\\\\\\"] = np.log1p(df[\\\\\\\"stars\\\\\\\"])\\\\ndf[\\\\\\\"log_forks\\\\\\\"] = np.log1p(df[\\\\\\\"forks\\\\\\\"])\\\\ndf[\\\\\\\"log_devs_at_tfdd\\\\\\\"] = np.log1p(df[\\\\\\\"devs_at_tfdd\\\\\\\"])\\\\ndf = df.dropna(subset=[\\\\\\\"founder_share\\\\\\\", \\\\\\\"n_diffused_owners\\\\\\\", \\\\\\\"log_stars\\\\\\\", \\\\\\\"log_forks\\\\\\\", \\\\\\\"devs_at_tfdd\\\\\\\"])\\\\nprint(f\\\\\\\"analysis dataframe: {len(df)} strict founder-only TFDD events\\\\\\\")\\\\ndf.head()\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"21b739c7\",\n   \"source\": \"# Does Founder Authority Diffusion Predict OSS Survival?\\\\n\\\\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\\\\n\\\\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\\\\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\\\\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\\\\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\\\\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\\\\n\\\\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\\\\n\\\\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\\\\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \\\\\\\"mini\\\\\\\" here is the full analysis sample, not a truncation).\\\\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\\\\n- Recomputes Cohen's d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\\\\n\\\\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"49615894\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# loguru -- not pre-installed on Colab, always install\\\\n_pip('loguru==0.7.3')\\\\n\\\\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"a74ae3ab\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass, field\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\n\\\\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"621add7b\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"6d655bb2\",\n   \"source\": \"raw = load_data()\\\\nprint(raw[\\\\\\\"metadata\\\\\\\"])\\\\nprint(\\\\\\\"n examples:\\\\\\\", len(raw[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"5329a615\",\n   \"source\": \"## Config\\\\n\\\\nAll tunable parameters from `method.py`'s Stage 5-8 analysis. `N_BOOT` (bootstrap resamples for the matched-pairs risk-ratio) is the only parameter worth scaling for a demo -- it starts small here and can be raised back to the original `5000` from the full run since the bootstrap over 16 rows is cheap either way.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"6eb4d2a3\",\n   \"source\": \"# Avelino et al.'s TFDD silence threshold / truck-factor coverage cutoff (unused directly in this notebook's\\\\n# Stage 5-8 recomputation but kept for reference -- these determined the pre-computed event data)\\\\nSILENCE_THRESHOLD_DAYS = 365\\\\nTF_COVERAGE_THRESHOLD = 0.5\\\\nPOST_TFDD_WINDOW_DAYS = 548  # 18 months\\\\nPRE_WINDOW_FAR_DAYS = 365  # 12 months before TFDD\\\\nPRE_WINDOW_NEAR_DAYS = 180  # 6 months before TFDD\\\\n\\\\n# matched-pairs thresholds (Stage 8)\\\\nMATCHED_PAIRS_LOW_THRESH = 0.50\\\\nMATCHED_PAIRS_HI_THRESH = 0.80\\\\nMATCHED_PAIRS_N_DIFFUSED_MIN = 2\\\\n\\\\n# bootstrap resamples for the risk-ratio CI -- START SMALL, scale back to 5000 (original) after it runs\\\\nN_BOOT = 200  # original value: 5000\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"a6cf6d5d\",\n   \"source\": \"## Rebuild the analysis dataframe (Stage 6 output format)\\\\n\\\\nEach loaded example is one strict founder-only TFDD event, with the fields `method.py`'s `events_to_df()` used to build its regression dataframe (`stars`, `forks`, `devs_at_tfdd`, `founder_share`, `n_diffused_owners`, `survived`, plus placebo-window fields). We reconstruct that same dataframe here, including the log-transformed covariates (`log_stars`, `log_forks`, `log_devs_at_tfdd`) `method.py` derives before fitting.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"a0366ece\",\n   \"source\": \"examples = raw[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]\\\\n\\\\nrows = []\\\\nfor e in examples:\\\\n    if \\\\\\\"metadata_repo\\\\\\\" not in e:\\\\n        continue  # skip the schema-required placeholder row if no events were found\\\\n    rows.append({\\\\n        \\\\\\\"repo\\\\\\\": e[\\\\\\\"metadata_repo\\\\\\\"],\\\\n        \\\\\\\"founder\\\\\\\": e[\\\\\\\"metadata_founder\\\\\\\"],\\\\n        \\\\\\\"tfdd_date\\\\\\\": e[\\\\\\\"metadata_tfdd_date\\\\\\\"],\\\\n        \\\\\\\"language\\\\\\\": e[\\\\\\\"metadata_language\\\\\\\"],\\\\n        \\\\\\\"stars\\\\\\\": e[\\\\\\\"metadata_stars\\\\\\\"],\\\\n        \\\\\\\"forks\\\\\\\": e[\\\\\\\"metadata_forks\\\\\\\"],\\\\n        \\\\\\\"devs_at_tfdd\\\\\\\": e[\\\\\\\"metadata_devs_at_tfdd\\\\\\\"],\\\\n        \\\\\\\"commits_at_tfdd\\\\\\\": e[\\\\\\\"metadata_commits_at_tfdd\\\\\\\"],\\\\n        \\\\\\\"files_at_tfdd\\\\\\\": e[\\\\\\\"metadata_files_at_tfdd\\\\\\\"],\\\\n        \\\\\\\"founder_share\\\\\\\": e[\\\\\\\"metadata_founder_share_pre_departure\\\\\\\"],\\\\n        \\\\\\\"n_diffused_owners\\\\\\\": e[\\\\\\\"metadata_n_diffused_owners_pre_departure\\\\\\\"],\\\\n        \\\\\\\"placebo_founder_share\\\\\\\": e[\\\\\\\"metadata_placebo_founder_share\\\\\\\"],\\\\n        \\\\\\\"placebo_n_diffused_owners\\\\\\\": e[\\\\\\\"metadata_placebo_n_diffused_owners\\\\\\\"],\\\\n        \\\\\\\"grade\\\\\\\": e[\\\\\\\"metadata_grade\\\\\\\"],\\\\n        \\\\\\\"censored\\\\\\\": e[\\\\\\\"metadata_censored\\\\\\\"],\\\\n        \\\\\\\"survived\\\\\\\": e[\\\\\\\"output\\\\\\\"] == \\\\\\\"survived\\\\\\\",\\\\n    })\\\\n\\\\ndf = pd.DataFrame(rows)\\\\ndf[\\\\\\\"tfdd_date\\\\\\\"] = pd.to_datetime(df[\\\\\\\"tfdd_date\\\\\\\"], utc=True)\\\\ndf[\\\\\\\"log_stars\\\\\\\"] = np.log1p(df[\\\\\\\"stars\\\\\\\"])\\\\ndf[\\\\\\\"log_forks\\\\\\\"] = np.log1p(df[\\\\\\\"forks\\\\\\\"])\\\\ndf[\\\\\\\"log_devs_at_tfdd\\\\\\\"] = np.log1p(df[\\\\\\\"devs_at_tfdd\\\\\\\"])\\\\ndf = df.dropna(subset=[\\\\\\\"founder_share\\\\\\\", \\\\\\\"n_diffused_owners\\\\\\\", \\\\\\\"log_stars\\\\\\\", \\\\\\\"log_forks\\\\\\\", \\\\\\\"devs_at_tfdd\\\\\\\"])\\\\nprint(f\\\\\\\"analysis dataframe: {len(df)} strict founder-only TFDD events\\\\\\\")\\\\ndf.head()\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"dbf99636\",\n   \"source\": \"## Stage 8 helper functions (copied unchanged from `method.py`)\\\\n\\\\n`build_matched_pairs`, `bootstrap_survival_rate_ratio`, `benjamini_hochberg`, and `cohens_d` -- the exact same functions the full pipeline run used to produce its reported numbers.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [52] TOOL CALL — NotebookEdit · 2026-08-21 21:36:58 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb', 'cell_id': 'dbf99636', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'def build_matched_pairs(df: pd.DataFrame, low_thresh: float = 0.50, hi_thresh: float = 0.80, n_diffused_min: int = 2):\\n    lo = df[(df.founder_share < low_thresh) & (df.n_diffused_owners >= n_diffused_min)].copy()\\n    hi = df[df.founder_share >= hi_thresh].copy()\\n    pairs = []\\n    used_hi = set()\\n    for _, lrow in lo.iterrows():\\n        best_idx, best_dist = None, float(\\"inf\\")\\n        for hidx, hrow in hi.iterrows():\\n            if hidx in used_hi:\\n                continue\\n            if hrow.language != lrow.language:\\n                continue\\n            dist = (\\n                (math.log1p(hrow.stars) - math.log1p(lrow.stars)) ** 2\\n                + (math.log1p(hrow.forks) - math.log1p(lrow.forks)) ** 2\\n                + (math.log1p(hrow.devs_at_tfdd) - math.log1p(lrow.devs_at_tfdd)) ** 2\\n            )\\n            if dist < best_dist:\\n                best_dist, best_idx = dist, hidx\\n        if best_idx is not None and best_dist < 4.0:  # cap on match distance (~2 log-units per dim)\\n            used_hi.add(best_idx)\\n            pairs.append((lrow, hi.loc[best_idx]))\\n    return pairs\\n\\n\\ndef bootstrap_survival_rate_ratio(pairs: list[tuple[pd.Series, pd.Series]], n_boot: int = N_BOOT):\\n    if not pairs:\\n        return float(\\"nan\\"), (float(\\"nan\\"), float(\\"nan\\"))\\n    lo_surv = np.array([1.0 if p[0].survived else 0.0 for p in pairs])\\n    hi_surv = np.array([1.0 if p[1].survived else 0.0 for p in pairs])\\n    n = len(pairs)\\n    ratios = []\\n    for _ in range(n_boot):\\n        idx = np.random.randint(0, n, size=n)\\n        lo_rate = lo_surv[idx].mean()\\n        hi_rate = hi_surv[idx].mean()\\n        if hi_rate == 0:\\n            continue\\n        ratios.append((lo_rate + 1e-6) / (hi_rate + 1e-6))\\n    if not ratios:\\n        return float(\\"nan\\"), (float(\\"nan\\"), float(\\"nan\\"))\\n    ratios = np.array(ratios)\\n    point = (lo_surv.mean() + 1e-6) / (hi_surv.mean() + 1e-6)\\n    ci = (float(np.percentile(ratios, 2.5)), float(np.percentile(ratios, 97.5)))\\n    return float(point), ci\\n\\n\\ndef benjamini_hochberg(pvals: dict[str, float]) -> dict[str, float]:\\n    items = sorted(pvals.items(), key=lambda kv: kv[1])\\n    m = len(items)\\n    adj = {}\\n    prev = 1.0\\n    for rank, (k, p) in enumerate(reversed(items), start=1):\\n        r = m - rank + 1\\n        val = min(prev, p * m / r)\\n        adj[k] = val\\n        prev = val\\n    return adj\\n\\n\\ndef cohens_d(a: np.ndarray, b: np.ndarray) -> float:\\n    a, b = a[~np.isnan(a)], b[~np.isnan(b)]\\n    if len(a) < 2 or len(b) < 2:\\n        return float(\\"nan\\")\\n    pooled_sd = math.sqrt(((len(a) - 1) * a.var(ddof=1) + (len(b) - 1) * b.var(ddof=1)) / (len(a) + len(b) - 2))\\n    if pooled_sd == 0:\\n        return float(\\"nan\\")\\n    return float((a.mean() - b.mean()) / pooled_sd)'}
```

### [53] TOOL RESULT — NotebookEdit · 2026-08-21 21:36:58 UTC

```
{"new_source": "def build_matched_pairs(df: pd.DataFrame, low_thresh: float = 0.50, hi_thresh: float = 0.80, n_diffused_min: int = 2):\\n    lo = df[(df.founder_share < low_thresh) & (df.n_diffused_owners >= n_diffused_min)].copy()\\n    hi = df[df.founder_share >= hi_thresh].copy()\\n    pairs = []\\n    used_hi = set()\\n    for _, lrow in lo.iterrows():\\n        best_idx, best_dist = None, float(\\\"inf\\\")\\n        for hidx, hrow in hi.iterrows():\\n            ... [truncated, 26858 chars total]
```

### [54] ASSISTANT · 2026-08-21 21:37:06 UTC

```
Now matched pairs + bootstrap section, and the fit_logit function + regressions.
```

### [55] TOOL CALL — NotebookEdit · 2026-08-21 21:37:06 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb', 'cell_id': 'ebb0e1de', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': '## Matched-pairs bootstrap risk-ratio\\n\\nPairs low-diffusion (`founder_share < 0.50`, `n_diffused_owners >= 2`) events with high-diffusion (`founder_share >= 0.80`) events matched on language and log(stars/forks/devs), then bootstraps the survival-rate ratio between the two groups. At n=16 this is known to produce 0 matchable pairs (reported honestly in the artifact summary rather than fabricated).'}
```

### [56] TOOL RESULT — NotebookEdit · 2026-08-21 21:37:06 UTC

```
{"new_source": "## Matched-pairs bootstrap risk-ratio\\n\\nPairs low-diffusion (`founder_share < 0.50`, `n_diffused_owners >= 2`) events with high-diffusion (`founder_share >= 0.80`) events matched on language and log(stars/forks/devs), then bootstraps the survival-rate ratio between the two groups. At n=16 this is known to produce 0 matchable pairs (reported honestly in the artifact summary rather than fabricated).", "cell_type": "markdown", "language": "python", "edi... [truncated, 28152 chars total]
```

### [57] TOOL CALL — NotebookEdit · 2026-08-21 21:37:10 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb', 'cell_id': '4cab7360', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'matched_pairs_result = {\\"n_pairs\\": 0}\\nif len(df) >= 6:\\n    pairs = build_matched_pairs(df, MATCHED_PAIRS_LOW_THRESH, MATCHED_PAIRS_HI_THRESH, MATCHED_PAIRS_N_DIFFUSED_MIN)\\n    risk_ratio, ci95 = bootstrap_survival_rate_ratio(pairs, n_boot=N_BOOT)\\n    matched_pairs_result = {\\n        \\"n_pairs\\": len(pairs),\\n        \\"risk_ratio_low_vs_high_diffusion\\": risk_ratio,\\n        \\"risk_ratio_ci95\\": list(ci95),\\n        \\"note\\": \\"risk_ratio = P(survival | low diffusion) / P(survival | high diffusion); >1 means low authority-diffusion (concentrated founder) survives MORE, <1 means diffusion helps survival\\",\\n    }\\nelse:\\n    matched_pairs_result[\\"note\\"] = \\"insufficient events for matched-pairs analysis (need >=6)\\"\\nprint(json.dumps(matched_pairs_result, indent=2, default=str))'}
```

### [58] TOOL RESULT — NotebookEdit · 2026-08-21 21:37:10 UTC

```
{"new_source": "matched_pairs_result = {\\\"n_pairs\\\": 0}\\nif len(df) >= 6:\\n    pairs = build_matched_pairs(df, MATCHED_PAIRS_LOW_THRESH, MATCHED_PAIRS_HI_THRESH, MATCHED_PAIRS_N_DIFFUSED_MIN)\\n    risk_ratio, ci95 = bootstrap_survival_rate_ratio(pairs, n_boot=N_BOOT)\\n    matched_pairs_result = {\\n        \\\"n_pairs\\\": len(pairs),\\n        \\\"risk_ratio_low_vs_high_diffusion\\\": risk_ratio,\\n        \\\"risk_ratio_ci95\\\": list(ci95),\\n        \\\"not... [truncated, 30194 chars total]
```

### [59] ASSISTANT · 2026-08-21 21:37:16 UTC

```
Now the logistic regression `fit_logit` function and the two model fits (our_method vs baseline) plus placebo check.
```

### [60] TOOL CALL — NotebookEdit · 2026-08-21 21:37:16 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb', 'cell_id': 'f6618c65', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': '## BH-corrected logistic regression: our_method vs baseline\\n\\n`fit_logit` (copied unchanged from `method.py`) fits a logistic regression of `survived` on the given covariates, plus a standardized-coefficient refit and Benjamini-Hochberg-corrected p-values. `our_method` adds the pre-departure diffusion trajectory (`founder_share`, `n_diffused_owners`) on top of the Avelino-et-al-style snapshot covariates that the `baseline` model uses alone.'}
```

### [61] TOOL RESULT — NotebookEdit · 2026-08-21 21:37:16 UTC

```
{"new_source": "## BH-corrected logistic regression: our_method vs baseline\\n\\n`fit_logit` (copied unchanged from `method.py`) fits a logistic regression of `survived` on the given covariates, plus a standardized-coefficient refit and Benjamini-Hochberg-corrected p-values. `our_method` adds the pre-departure diffusion trajectory (`founder_share`, `n_diffused_owners`) on top of the Avelino-et-al-style snapshot covariates that the `baseline` model uses alone.", "cell_t... [truncated, 31458 chars total]
```

### [62] TOOL CALL — NotebookEdit · 2026-08-21 21:37:26 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb', 'cell_id': '75e7e2b8', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'def fit_logit(df_in: pd.DataFrame, cols: list[str], label: str) -> dict:\\n    if df_in.empty or df_in[\\"survived\\"].nunique() < 2 or len(df_in) < len(cols) + 3:\\n        return {\\"status\\": \\"insufficient_data\\", \\"n\\": int(len(df_in)), \\"n_classes\\": int(df_in[\\"survived\\"].nunique()) if not df_in.empty else 0}\\n    X = df_in[cols].astype(float)\\n    y = df_in[\\"survived\\"].astype(int)\\n    X_const = sm.add_constant(X, has_constant=\\"add\\")\\n    try:\\n        model = sm.Logit(y, X_const).fit(disp=0, maxiter=200)\\n    except Exception as e:\\n        logger.warning(f\\"[{label}] logit failed ({e}); falling back to parsimonious covariate set\\")\\n        parsimonious = [c for c in [\\"founder_share\\", \\"n_diffused_owners\\", \\"log_stars\\", \\"log_devs_at_tfdd\\"] if c in cols]\\n        if not parsimonious or parsimonious == cols:\\n            return {\\"status\\": f\\"failed:{e}\\", \\"n\\": int(len(df_in))}\\n        return fit_logit(df_in, parsimonious, label + \\"_parsimonious\\")\\n    std_X = (X - X.mean()) / X.std(ddof=0).replace(0, 1)\\n    std_X_const = sm.add_constant(std_X, has_constant=\\"add\\")\\n    try:\\n        std_model = sm.Logit(y, std_X_const).fit(disp=0, maxiter=200)\\n        std_effects = std_model.params.drop(\\"const\\").to_dict()\\n    except Exception:\\n        std_effects = {}\\n    return {\\n        \\"status\\": \\"ok\\",\\n        \\"n\\": int(len(df_in)),\\n        \\"covariates\\": cols,\\n        \\"coefs\\": model.params.to_dict(),\\n        \\"pvalues\\": model.pvalues.to_dict(),\\n        \\"pvalues_bh\\": benjamini_hochberg(model.pvalues.drop(\\"const\\").to_dict()),\\n        \\"standardized_effect_sizes\\": std_effects,\\n        \\"pseudo_r2\\": float(model.prsquared),\\n        \\"converged\\": bool(model.mle_retvals.get(\\"converged\\", True)),\\n    }\\n\\n\\nour_cols = [\\"founder_share\\", \\"n_diffused_owners\\", \\"log_stars\\", \\"log_forks\\", \\"log_devs_at_tfdd\\"]\\nbaseline_cols = [\\"log_stars\\", \\"log_forks\\", \\"log_devs_at_tfdd\\"]  # Avelino-et-al-style snapshot covariates only, no diffusion trajectory\\nregression_our_method = fit_logit(df, our_cols, \\"our_method\\")\\nregression_baseline_snapshot_only = fit_logit(df, baseline_cols, \\"baseline\\")\\nprint(\\"=== our_method ===\\")\\nprint(json.dumps(regression_our_method, indent=2, default=str))\\nprint(\\"\\\\n=== baseline (snapshot-only) ===\\")\\nprint(json.dumps(regression_baseline_snapshot_only, indent=2, default=str))'}
```

### [63] TOOL RESULT — NotebookEdit · 2026-08-21 21:37:26 UTC

```
{"new_source": "def fit_logit(df_in: pd.DataFrame, cols: list[str], label: str) -> dict:\\n    if df_in.empty or df_in[\\\"survived\\\"].nunique() < 2 or len(df_in) < len(cols) + 3:\\n        return {\\\"status\\\": \\\"insufficient_data\\\", \\\"n\\\": int(len(df_in)), \\\"n_classes\\\": int(df_in[\\\"survived\\\"].nunique()) if not df_in.empty else 0}\\n    X = df_in[cols].astype(float)\\n    y = df_in[\\\"survived\\\"].astype(int)\\n    X_const = sm.add_constant(X, ... [truncated, 37362 chars total]
```

### [64] ASSISTANT · 2026-08-21 21:37:32 UTC

```
Placebo check, effect sizes, Mann-Whitney, and unconditioned survival rates.
```

### [65] TOOL CALL — NotebookEdit · 2026-08-21 21:37:32 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb', 'cell_id': '4d7fd790', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': '## Placebo-window falsification check (Stage 7)\\n\\nEach event also carries a `placebo_founder_share`/`placebo_n_diffused_owners` pair computed on a randomly-sampled 6-month window at least a year away from the TFDD window. Refitting the same regression on the placebo metrics tests whether the signal is specific to the pre-departure period, or just a generic property of any window.'}
```

### [66] TOOL RESULT — NotebookEdit · 2026-08-21 21:37:34 UTC

```
{"new_source": "## Placebo-window falsification check (Stage 7)\\n\\nEach event also carries a `placebo_founder_share`/`placebo_n_diffused_owners` pair computed on a randomly-sampled 6-month window at least a year away from the TFDD window. Refitting the same regression on the placebo metrics tests whether the signal is specific to the pre-departure period, or just a generic property of any window.", "cell_type": "markdown", "language": "python", "edit_mode": "insert",... [truncated, 38844 chars total]
```

### [67] TOOL CALL — NotebookEdit · 2026-08-21 21:37:38 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb', 'cell_id': '8e2cfdd4', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'placebo_df = df.dropna(subset=[\\"placebo_founder_share\\", \\"placebo_n_diffused_owners\\"]).copy()\\nplacebo_cols = [\\"placebo_founder_share\\", \\"placebo_n_diffused_owners\\", \\"log_stars\\", \\"log_forks\\", \\"log_devs_at_tfdd\\"]\\nplacebo_check = {\\n    \\"n_events_with_placebo_window\\": int(len(placebo_df)),\\n    \\"regression_placebo_window\\": fit_logit(placebo_df, placebo_cols, \\"placebo\\") if len(placebo_df) >= 8 else {\\"status\\": \\"insufficient_data\\", \\"n\\": int(len(placebo_df))},\\n}\\nprint(json.dumps(placebo_check, indent=2, default=str))'}
```

### [68] TOOL RESULT — NotebookEdit · 2026-08-21 21:37:38 UTC

```
{"new_source": "placebo_df = df.dropna(subset=[\\\"placebo_founder_share\\\", \\\"placebo_n_diffused_owners\\\"]).copy()\\nplacebo_cols = [\\\"placebo_founder_share\\\", \\\"placebo_n_diffused_owners\\\", \\\"log_stars\\\", \\\"log_forks\\\", \\\"log_devs_at_tfdd\\\"]\\nplacebo_check = {\\n    \\\"n_events_with_placebo_window\\\": int(len(placebo_df)),\\n    \\\"regression_placebo_window\\\": fit_logit(placebo_df, placebo_cols, \\\"placebo\\\") if len(placebo_df) >= 8 ... [truncated, 40436 chars total]
```

### [69] TOOL CALL — NotebookEdit · 2026-08-21 21:37:40 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb', 'cell_id': '04ec07b2', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': "## Effect sizes (Cohen's d) and Mann-Whitney U tests\\n\\nSimple two-group nonparametric comparisons of survived vs. did-not-survive events, for comparability with Avelino et al.'s reported effect sizes (d=0.13-0.26)."}
```

### [70] TOOL RESULT — NotebookEdit · 2026-08-21 21:37:42 UTC

```
{"new_source": "## Effect sizes (Cohen's d) and Mann-Whitney U tests\\n\\nSimple two-group nonparametric comparisons of survived vs. did-not-survive events, for comparability with Avelino et al.'s reported effect sizes (d=0.13-0.26).", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "3fa1728c", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9... [truncated, 41268 chars total]
```

### [71] TOOL CALL — NotebookEdit · 2026-08-21 21:37:50 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb', 'cell_id': '3fa1728c', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'if not df.empty and df[\\"survived\\"].nunique() == 2:\\n    surv_mask = df[\\"survived\\"].astype(bool)\\n    snapshot_covariate_effect_sizes_d = {\\n        \\"devs_at_tfdd\\": cohens_d(df.loc[surv_mask, \\"devs_at_tfdd\\"].to_numpy(), df.loc[~surv_mask, \\"devs_at_tfdd\\"].to_numpy()),\\n        \\"commits_at_tfdd\\": cohens_d(df.loc[surv_mask, \\"commits_at_tfdd\\"].to_numpy(), df.loc[~surv_mask, \\"commits_at_tfdd\\"].to_numpy()),\\n        \\"files_at_tfdd\\": cohens_d(df.loc[surv_mask, \\"files_at_tfdd\\"].to_numpy(), df.loc[~surv_mask, \\"files_at_tfdd\\"].to_numpy()),\\n        \\"founder_share_pre_departure\\": cohens_d(df.loc[surv_mask, \\"founder_share\\"].to_numpy(), df.loc[~surv_mask, \\"founder_share\\"].to_numpy()),\\n        \\"n_diffused_owners_pre_departure\\": cohens_d(df.loc[surv_mask, \\"n_diffused_owners\\"].to_numpy(), df.loc[~surv_mask, \\"n_diffused_owners\\"].to_numpy()),\\n    }\\n    mann_whitney_diffusion_vs_survival = {\\n        \\"founder_share\\": {\\n            \\"u_stat\\": float(stats.mannwhitneyu(df.loc[surv_mask, \\"founder_share\\"], df.loc[~surv_mask, \\"founder_share\\"], alternative=\\"two-sided\\").statistic),\\n            \\"p\\": float(stats.mannwhitneyu(df.loc[surv_mask, \\"founder_share\\"], df.loc[~surv_mask, \\"founder_share\\"], alternative=\\"two-sided\\").pvalue),\\n        },\\n        \\"n_diffused_owners\\": {\\n            \\"u_stat\\": float(stats.mannwhitneyu(df.loc[surv_mask, \\"n_diffused_owners\\"], df.loc[~surv_mask, \\"n_diffused_owners\\"], alternative=\\"two-sided\\").statistic),\\n            \\"p\\": float(stats.mannwhitneyu(df.loc[surv_mask, \\"n_diffused_owners\\"], df.loc[~surv_mask, \\"n_diffused_owners\\"], alternative=\\"two-sided\\").pvalue),\\n        },\\n    }\\nelse:\\n    snapshot_covariate_effect_sizes_d = {\\"status\\": \\"insufficient_class_variation\\"}\\n    mann_whitney_diffusion_vs_survival = {\\"status\\": \\"insufficient_class_variation\\"}\\n\\nprint(\\"Cohen\'s d:\\", json.dumps(snapshot_covariate_effect_sizes_d, indent=2, default=str))\\nprint(\\"\\\\nMann-Whitney U:\\", json.dumps(mann_whitney_diffusion_vs_survival, indent=2, default=str))'}
```

### [72] TOOL RESULT — NotebookEdit · 2026-08-21 21:37:50 UTC

```
{"new_source": "if not df.empty and df[\\\"survived\\\"].nunique() == 2:\\n    surv_mask = df[\\\"survived\\\"].astype(bool)\\n    snapshot_covariate_effect_sizes_d = {\\n        \\\"devs_at_tfdd\\\": cohens_d(df.loc[surv_mask, \\\"devs_at_tfdd\\\"].to_numpy(), df.loc[~surv_mask, \\\"devs_at_tfdd\\\"].to_numpy()),\\n        \\\"commits_at_tfdd\\\": cohens_d(df.loc[surv_mask, \\\"commits_at_tfdd\\\"].to_numpy(), df.loc[~surv_mask, \\\"commits_at_tfdd\\\"].to_numpy()),\\... [truncated, 46424 chars total]
```

### [73] ASSISTANT · 2026-08-21 21:37:56 UTC

```
Now the final visualization/results cell.
```

### [74] TOOL CALL — NotebookEdit · 2026-08-21 21:37:56 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb', 'cell_id': '83f133ad', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': "## Results summary\\n\\nUnconditioned 18-month post-TFDD survival rate (cross-check against Avelino et al.'s reported ~41%), plus a bar chart comparing our_method's and the baseline's standardized logistic-regression coefficients, and a scatter of founder_share vs. survival outcome."}
```

### [75] TOOL RESULT — NotebookEdit · 2026-08-21 21:37:57 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [76] TOOL CALL — NotebookEdit · 2026-08-21 21:38:07 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/code_demo.ipynb', 'cell_id': '705b4331', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'n_events = len(df)\\nn_survived = int(df[\\"survived\\"].sum())\\nsurvival_rate = n_survived / n_events if n_events else float(\\"nan\\")\\nprint(f\\"Strict founder-only TFDD events analyzed: {n_events}\\")\\nprint(f\\"Unconditioned 18-month post-TFDD survival rate: {survival_rate:.3f} ({n_survived}/{n_events})\\")\\nprint(f\\"Avelino et al.\'s reference survival rate:        0.41\\")\\nprint(f\\"\\\\nour_method pseudo-R^2:  {regression_our_method.get(\'pseudo_r2\')}\\")\\nprint(f\\"baseline   pseudo-R^2:  {regression_baseline_snapshot_only.get(\'pseudo_r2\')}\\")\\nprint(f\\"\\\\nmatched-pairs: n_pairs={matched_pairs_result[\'n_pairs\']}, risk_ratio={matched_pairs_result.get(\'risk_ratio_low_vs_high_diffusion\')}\\")\\n\\nfig, axes = plt.subplots(1, 2, figsize=(12, 4.5))\\n\\n# left: standardized coefficients, our_method vs baseline\\nax = axes[0]\\nour_std = regression_our_method.get(\\"standardized_effect_sizes\\", {})\\nbase_std = regression_baseline_snapshot_only.get(\\"standardized_effect_sizes\\", {})\\nall_covs = list(dict.fromkeys(list(our_std.keys()) + list(base_std.keys())))\\nx = np.arange(len(all_covs))\\nwidth = 0.35\\nax.bar(x - width/2, [our_std.get(c, 0) for c in all_covs], width, label=\\"our_method\\")\\nax.bar(x + width/2, [base_std.get(c, 0) for c in all_covs], width, label=\\"baseline\\")\\nax.set_xticks(x)\\nax.set_xticklabels(all_covs, rotation=45, ha=\\"right\\")\\nax.axhline(0, color=\\"black\\", linewidth=0.8)\\nax.set_ylabel(\\"standardized logistic coefficient\\")\\nax.set_title(\\"our_method vs baseline: standardized effects\\")\\nax.legend()\\n\\n# right: founder_share pre-departure vs survival outcome\\nax = axes[1]\\ncolors = df[\\"survived\\"].map({True: \\"tab:green\\", False: \\"tab:red\\"})\\nax.scatter(df[\\"founder_share\\"], df[\\"n_diffused_owners\\"], c=colors, s=80, edgecolor=\\"black\\")\\nax.set_xlabel(\\"founder_share (pre-departure window)\\")\\nax.set_ylabel(\\"n_diffused_owners (pre-departure window)\\")\\nax.set_title(\\"Pre-departure diffusion trajectory vs survival\\\\n(green=survived, red=did not survive)\\")\\n\\nplt.tight_layout()\\nplt.show()'}
```

### [77] TOOL RESULT — NotebookEdit · 2026-08-21 21:38:07 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [78] ASSISTANT · 2026-08-21 21:38:11 UTC

```
Now copy mini_demo_data.json into workspace root (already done) and test-run in clean env.
```

### [79] TOOL CALL — Bash · 2026-08-21 21:38:11 UTC

```
ls -la
/usr/local/bin/python3.12 -m venv .nb_env 2>&1 | tail -5
.nb_env/bin/pip install -q pip jupyter ipykernel 2>&1 | tail -15
```

### [80] TOOL RESULT — Bash · 2026-08-21 21:40:11 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bhvd2vcjz", "timedOutAfterMs": 120000}
```

### [81] ASSISTANT · 2026-08-21 21:40:13 UTC

```
Waiting for the venv setup to finish in the background.
```

### [82] TOOL CALL — ScheduleWakeup · 2026-08-21 21:40:13 UTC

```
{'delaySeconds': 90, 'noop': True, 'reason': 'waiting for background pip install to finish'}
```

### [83] TOOL RESULT — ScheduleWakeup [ERROR] · 2026-08-21 21:40:13 UTC

```
Error: `prompt` is required when `stop` is not true.
```

### [84] TOOL CALL — Bash · 2026-08-21 21:40:15 UTC

```
sleep 60; tail -c 2000 /tmp/claude-0/-ai-inventor-aii-data-runs-run-r-byUQiUWdrF-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-1-art-4CZ-9Ou1G5ty/b6f670e4-3498-422b-8d3e-89240254c338/tasks/bhvd2vcjz.output
```

### [85] TOOL RESULT — Bash [ERROR] · 2026-08-21 21:40:15 UTC

```
Error: Blocked: sleep 60 followed by: tail -c 2000 /tmp/claude-0/-ai-inventor-aii-data-runs-run-r-byUQiUWdrF-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-1-art-4CZ-9Ou1G5ty/b6f670e4-3498-422b-8d3e-89240254c338/tasks/bhvd2vcjz.output. To wait for a condition, use Monitor with an until-loop (e.g. `until <check>; do sleep 2; done`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block.
```

### [86] TOOL CALL — ToolSearch · 2026-08-21 21:40:17 UTC

```
{'query': 'select:Monitor', 'max_results': 1}
```

### [87] TOOL RESULT — ToolSearch · 2026-08-21 21:40:17 UTC

```
{"matches": ["Monitor"], "query": "select:Monitor", "total_deferred_tools": 22}
```

### [88] TOOL CALL — Monitor · 2026-08-21 21:40:19 UTC

```
{'command': "until ! kill -0 $(pgrep -f 'jupyter ipykernel' 2>/dev/null | head -1) 2>/dev/null; do sleep 3; done; echo done_waiting_maybe; sleep 1000000", 'description': 'waiting for pip install background task', 'timeout_ms': 120000, 'persistent': False}
```

### [89] TOOL RESULT — Monitor · 2026-08-21 21:40:19 UTC

```
{"taskId": "b5egk294l", "timeoutMs": 120000, "persistent": false}
```

### [90] TOOL CALL — Bash · 2026-08-21 21:40:25 UTC

```
ls .nb_env/bin/ 2>&1 | head -5; echo ---; tail -c 1500 /tmp/claude-0/-ai-inventor-aii-data-runs-run-r-byUQiUWdrF-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-1-art-4CZ-9Ou1G5ty/b6f670e4-3498-422b-8d3e-89240254c338/tasks/bhvd2vcjz.output
```

### [91] TOOL RESULT — Bash · 2026-08-21 21:40:25 UTC

```
{"stdout": "Activate.ps1\nactivate\nactivate.csh\nactivate.fish\npip\n---\ntotal 3298\ndrwxr-xr-x 2 root root 1033352 Aug 21 21:38 .\ndrwxr-xr-x 5 root root 2000924 Aug 21 21:34 ..\n-rw-r--r-- 1 root root  298947 Aug 21 21:38 .repl_agent.ptylog\n-rw-r--r-- 1 root root   23544 Aug 21 21:38 code_demo.ipynb\n-rw-r--r-- 1 root root   20897 Aug 21 21:35 mini_demo_data.json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [92] ASSISTANT · 2026-08-21 21:40:27 UTC

```
pip install still running (venv created, jupyter installing). Let me wait for it properly.
```

### [93] TOOL CALL — Bash · 2026-08-21 21:40:27 UTC

```
until [ -f .nb_env/bin/jupyter ]; do sleep 3; done; echo jupyter_ready
```

### [94] TOOL RESULT — Bash · 2026-08-21 21:40:27 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bosh1iw2l"}
```

### [95] ASSISTANT · 2026-08-21 21:40:29 UTC

```
Waiting on background jupyter install; I'll act once notified.
```

### [96] TOOL CALL — Bash · 2026-08-21 21:40:29 UTC

```
echo waiting
```

### [97] TOOL RESULT — Bash · 2026-08-21 21:40:29 UTC

```
{"stdout": "waiting", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [98] ASSISTANT · 2026-08-21 21:40:29 UTC

```
I'll wait for the background tasks to complete before proceeding.
```

### [99] TOOL CALL — Bash · 2026-08-21 21:40:29 UTC

```
echo ok
```

### [100] TOOL RESULT — Bash · 2026-08-21 21:40:29 UTC

```
{"stdout": "ok", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [101] TOOL CALL — Bash · 2026-08-21 21:40:35 UTC

```
python3 -c "import json; json.load(open('code_demo.ipynb')); print('valid json, cells:', len(json.load(open('code_demo.ipynb'))['cells']))"
```

### [102] TOOL RESULT — Bash · 2026-08-21 21:40:35 UTC

```
{"stdout": "valid json, cells: 21", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [103] ASSISTANT · 2026-08-21 21:40:37 UTC

```
Good, notebook JSON is valid with 21 cells. Now I'll wait for the background install to finish.
```

### [104] TOOL CALL — Bash · 2026-08-21 21:40:37 UTC

```
cat /tmp/claude-0/-ai-inventor-aii-data-runs-run-r-byUQiUWdrF-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-1-art-4CZ-9Ou1G5ty/b6f670e4-3498-422b-8d3e-89240254c338/tasks/bosh1iw2l.output 2>/dev/null; ls .nb_env/bin/ | grep -i jupyter
```

### [105] TOOL RESULT — Bash · 2026-08-21 21:40:37 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "returnCodeInterpretation": "No matches found", "noOutputExpected": false}
```

### [106] TOOL CALL — Bash · 2026-08-21 21:40:39 UTC

```
true
```

### [107] TOOL RESULT — Bash · 2026-08-21 21:40:39 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [108] ASSISTANT · 2026-08-21 21:40:41 UTC

```
I'll pause here and wait for the background task notification before continuing.
```

### [109] TOOL CALL — Bash · 2026-08-21 21:40:41 UTC

```
true
```

### [110] TOOL RESULT — Bash · 2026-08-21 21:40:41 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [111] TOOL CALL — ToolSearch · 2026-08-21 21:40:43 UTC

```
{'query': 'select:TaskOutput', 'max_results': 1}
```

### [112] TOOL RESULT — ToolSearch · 2026-08-21 21:40:43 UTC

```
{"matches": ["TaskOutput"], "query": "select:TaskOutput", "total_deferred_tools": 22}
```

### [113] TOOL CALL — TaskOutput · 2026-08-21 21:42:45 UTC

```
{'task_id': 'bosh1iw2l', 'block': True, 'timeout': 120000}
```

### [114] TOOL RESULT — TaskOutput · 2026-08-21 21:42:45 UTC

```
{"retrieval_status": "timeout", "task": {"task_id": "bosh1iw2l", "task_type": "local_bash", "status": "running", "description": "until [ -f .nb_env/bin/jupyter ]; do sleep 3; done; echo jupyter_ready", "output": "", "exitCode": null}}
```

### [115] TOOL CALL — TaskOutput · 2026-08-21 21:45:19 UTC

```
{'task_id': 'bosh1iw2l', 'block': True, 'timeout': 180000}
```

### [116] TOOL RESULT — TaskOutput · 2026-08-21 21:45:19 UTC

```
{"retrieval_status": "success", "task": {"task_id": "bosh1iw2l", "task_type": "local_bash", "status": "completed", "description": "until [ -f .nb_env/bin/jupyter ]; do sleep 3; done; echo jupyter_ready", "output": "jupyter_ready\n\n[exited with code 0]\n", "exitCode": 0}}
```

### [117] ASSISTANT · 2026-08-21 21:45:21 UTC

```
Jupyter is installed. Now running the notebook execution test.
```

### [118] TOOL CALL — Bash · 2026-08-21 21:45:21 UTC

```
.nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb 2>&1 | tail -100
```

### [119] TOOL RESULT — Bash · 2026-08-21 21:45:21 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bbhwyye1z"}
```

### [120] TOOL CALL — TaskOutput · 2026-08-21 21:45:23 UTC

```
{'task_id': 'bbhwyye1z', 'block': True, 'timeout': 600000}
```

### [121] TOOL RESULT — TaskOutput · 2026-08-21 21:45:23 UTC

```
{"retrieval_status": "success", "task": {"task_id": "bbhwyye1z", "task_type": "local_bash", "status": "completed", "description": ".nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb 2>&1 | tail -100", "output": "usage: jupyter [-h] [--version] [--config-dir] [--data-dir] [--runtime-dir]\n               [--paths] [--json] [--debug]\n               [subcommand]\n\nJupyter: Interactive Computing\n\npositional arguments:\n  subcommand     the subcommand to launch\n\noptions:\n  -h, --help     show this help message and exit\n  --version      show the versions of core jupyter packages and exit\n  --config-dir   show Jupyter config dir\n  --data-dir     show Jupyter data dir\n  --runtime-dir  show Jupyter runtime dir\n  --paths        show all Jupyter paths. Add --json for machine-readable\n                 format.\n  --json         output paths as machine-readable json\n  --debug        output debug information about paths\n\nAvailable subcommands: migrate troubleshoot\n\nJupyter command `jupyter-nbconvert` not found.\n\n[exited with code 0]\n", "exitCode": 0}}
```

### [122] ASSISTANT · 2026-08-21 21:45:29 UTC

```
nbconvert wasn't actually installed. Need to install it explicitly.
```

### [123] TOOL CALL — Bash · 2026-08-21 21:45:29 UTC

```
.nb_env/bin/pip install -q nbconvert 2>&1 | tail -20
```

### [124] TOOL RESULT — Bash · 2026-08-21 21:46:21 UTC

```
{"stdout": "[notice] A new release of pip is available: 25.0.1 -> 26.2.1\n[notice] To update, run: python3.12 -m pip install --upgrade pip", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [125] TOOL CALL — Bash · 2026-08-21 21:46:23 UTC

```
.nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb 2>&1 | tail -150
```

### [126] TOOL RESULT — Bash · 2026-08-21 21:46:23 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bdcn8fd8c"}
```

### [127] TOOL CALL — TaskOutput · 2026-08-21 21:47:05 UTC

```
{'task_id': 'bdcn8fd8c', 'block': True, 'timeout': 600000}
```

### [128] TOOL RESULT — TaskOutput · 2026-08-21 21:47:05 UTC

```
{"retrieval_status": "success", "task": {"task_id": "bdcn8fd8c", "task_type": "local_bash", "status": "completed", "description": ".nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb 2>&1 | tail -150", "output": "[NbConvertApp] Converting notebook code_demo.ipynb to notebook\n[NbConvertApp] ERROR | No such kernel named python3\nTraceback (most recent call last):\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/jupyter_client/manager.py\", line 107, in wrapper\n    out = await method(self, *args, **kwargs)\n          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/jupyter_client/manager.py\", line 523, in _async_start_kernel\n    kernel_cmd, kw = await self._async_pre_start_kernel(**kw)\n                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/jupyter_client/manager.py\", line 485, in _async_pre_start_kernel\n    self.kernel_spec,\n    ^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/jupyter_client/manager.py\", line 267, in kernel_spec\n    self._kernel_spec = self.kernel_spec_manager.get_kernel_spec(self.kernel_name)\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/jupyter_client/kernelspec.py\", line 287, in get_kernel_spec\n    raise NoSuchKernel(kernel_name)\njupyter_client.kernelspec.NoSuchKernel: No such kernel named python3\nTraceback (most recent call last):\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/bin/jupyter-nbconvert\", line 10, in <module>\n    sys.exit(main())\n             ^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/jupyter_core/application.py\", line 284, in launch_instance\n    super().launch_instance(argv=argv, **kwargs)\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/traitlets/config/application.py\", line 1080, in launch_instance\n    app.start()\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/nbconvertapp.py\", line 420, in start\n    self.convert_notebooks()\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/nbconvertapp.py\", line 597, in convert_notebooks\n    self.convert_single_notebook(notebook_filename)\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/nbconvertapp.py\", line 563, in convert_single_notebook\n    output, resources = self.export_single_notebook(\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/nbconvertapp.py\", line 487, in export_single_notebook\n    output, resources = self.exporter.from_filename(\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 201, in from_filename\n    return self.from_file(f, resources=resources, **kw)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 220, in from_file\n    return self.from_notebook_node(\n           ^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/notebook.py\", line 36, in from_notebook_node\n    nb_copy, resources = super().from_notebook_node(nb, resources, **kw)\n                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 154, in from_notebook_node\n    nb_copy, resources = self._preprocess(nb_copy, resources)\n                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 353, in _preprocess\n    nbc, resc = preprocessor(nbc, resc)\n                ^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/preprocessors/base.py\", line 48, in __call__\n    return self.preprocess(nb, resources)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/preprocessors/execute.py\", line 97, in preprocess\n    with self.setup_kernel():\n         ^^^^^^^^^^^^^^^^^^^\n  File \"/usr/local/lib/python3.12/contextlib.py\", line 137, in __enter__\n    return next(self.gen)\n           ^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbclient/client.py\", line 600, in setup_kernel\n    self.start_new_kernel(**kwargs)\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/jupyter_core/utils/__init__.py\", line 165, in wrapped\n    return loop.run_until_complete(inner)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/local/lib/python3.12/asyncio/base_events.py\", line 691, in run_until_complete\n    return future.result()\n           ^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbclient/client.py\", line 550, in async_start_new_kernel\n    await ensure_async(self.km.start_kernel(extra_arguments=self.extra_arguments, **kwargs))\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/jupyter_core/utils/__init__.py\", line 214, in ensure_async\n    result = await obj\n             ^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/jupyter_client/manager.py\", line 116, in wrapper\n    raise e\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/jupyter_client/manager.py\", line 107, in wrapper\n    out = await method(self, *args, **kwargs)\n          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/jupyter_client/manager.py\", line 523, in _async_start_kernel\n    kernel_cmd, kw = await self._async_pre_start_kernel(**kw)\n                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/jupyter_client/manager.py\", line 485, in _async_pre_start_kernel\n    self.kernel_spec,\n    ^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/jupyter_client/manager.py\", line 267, in kernel_spec\n    self._kernel_spec = self.kernel_spec_manager.get_kernel_spec(self.kernel_name)\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/jupyter_client/kernelspec.py\", line 287, in get_kernel_spec\n    raise NoSuchKernel(kernel_name)\njupyter_client.kernelspec.NoSuchKernel: No such kernel named python3\n\n[exited with code 0]\n", "exitCode": 0}}
```

### [129] ASSISTANT · 2026-08-21 21:47:07 UTC

```
ipykernel wasn't registered. Let me register the kernel.
```

### [130] TOOL CALL — Bash · 2026-08-21 21:47:07 UTC

```
.nb_env/bin/python -m ipykernel install --user --name python3 --display-name python3 2>&1 | tail -10
```

### [131] TOOL RESULT — Bash · 2026-08-21 21:47:07 UTC

```
{"stdout": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/bin/python: No module named ipykernel", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [132] TOOL CALL — Bash · 2026-08-21 21:47:09 UTC

```
.nb_env/bin/pip install -q ipykernel 2>&1 | tail -20 && .nb_env/bin/python -m ipykernel install --user --name python3 --display-name python3 2>&1 | tail -10
```

### [133] TOOL RESULT — Bash · 2026-08-21 21:49:11 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "b1yog5npn", "timedOutAfterMs": 120000}
```

### [134] TOOL CALL — TaskOutput · 2026-08-21 21:52:11 UTC

```
{'task_id': 'b1yog5npn', 'block': True, 'timeout': 180000}
```

### [135] TOOL RESULT — TaskOutput · 2026-08-21 21:52:11 UTC

```
{"retrieval_status": "timeout", "task": {"task_id": "b1yog5npn", "task_type": "local_bash", "status": "running", "description": ".nb_env/bin/pip install -q ipykernel 2>&1 | tail -20 && .nb_env/bin/python -m ipykernel install --user --name python3 --display-name python3 2>&1 | tail -10", "output": "", "exitCode": null}}
```

### [136] TOOL CALL — TaskOutput · 2026-08-21 21:54:01 UTC

```
{'task_id': 'b1yog5npn', 'block': True, 'timeout': 300000}
```

### [137] TOOL RESULT — TaskOutput · 2026-08-21 21:54:01 UTC

```
{"retrieval_status": "success", "task": {"task_id": "b1yog5npn", "task_type": "local_bash", "status": "completed", "description": ".nb_env/bin/pip install -q ipykernel 2>&1 | tail -20 && .nb_env/bin/python -m ipykernel install --user --name python3 --display-name python3 2>&1 | tail -10", "output": "\n[notice] A new release of pip is available: 25.0.1 -> 26.2.1\n[notice] To update, run: python3.12 -m pip install --upgrade pip\nInstalled kernelspec python3 in /root/.local/share/jupyter/kernels/python3\n\n[exited with code 0]\n", "exitCode": 0}}
```

### [138] ASSISTANT · 2026-08-21 21:54:03 UTC

```
Kernel registered. Now re-run the notebook execution.
```

### [139] TOOL CALL — Bash · 2026-08-21 21:54:03 UTC

```
.nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb > /tmp/nbrun.log 2>&1; echo EXIT:$?
```

### [140] TOOL RESULT — Bash · 2026-08-21 21:54:03 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "b9eiwstn1"}
```

### [141] TOOL CALL — TaskOutput · 2026-08-21 21:55:17 UTC

```
{'task_id': 'b9eiwstn1', 'block': True, 'timeout': 600000}
```

### [142] TOOL RESULT — TaskOutput · 2026-08-21 21:55:17 UTC

```
{"retrieval_status": "success", "task": {"task_id": "b9eiwstn1", "task_type": "local_bash", "status": "completed", "description": ".nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb > /tmp/nbrun.log 2>&1; echo EXIT:$?", "output": "EXIT:1\n\n[exited with code 0]\n", "exitCode": 0}}
```

### [143] ASSISTANT · 2026-08-21 21:55:19 UTC

```
Exit 1, error occurred. Let's check the log.
```

### [144] TOOL CALL — Read · 2026-08-21 21:55:19 UTC

```
/tmp/nbrun.log
```

### [145] TOOL RESULT — Read · 2026-08-21 21:55:19 UTC

```
{"type": "text", "file": {"filePath": "/tmp/nbrun.log", "content": "[NbConvertApp] Converting notebook code_demo.ipynb to notebook\n[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.\nTraceback (most recent call last):\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/bin/jupyter-nbconvert\", line 10, in <module>\n    sys.exit(main())\n             ^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/jupyter_core/application.py\", line 284, in launch_instance\n    super().launch_instance(argv=argv, **kwargs)\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/traitlets/config/application.py\", line 1080, in launch_instance\n    app.start()\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/nbconvertapp.py\", line 420, in start\n    self.convert_notebooks()\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/nbconvertapp.py\", line 597, in convert_notebooks\n    self.convert_single_notebook(notebook_filename)\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/nbconvertapp.py\", line 563, in convert_single_notebook\n    output, resources = self.export_single_notebook(\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/nbconvertapp.py\", line 487, in export_single_notebook\n    output, resources = self.exporter.from_filename(\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 201, in from_filename\n    return self.from_file(f, resources=resources, **kw)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 220, in from_file\n    return self.from_notebook_node(\n           ^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/notebook.py\", line 36, in from_notebook_node\n    nb_copy, resources = super().from_notebook_node(nb, resources, **kw)\n                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 154, in from_notebook_node\n    nb_copy, resources = self._preprocess(nb_copy, resources)\n                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 353, in _preprocess\n    nbc, resc = preprocessor(nbc, resc)\n                ^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/preprocessors/base.py\", line 48, in __call__\n    return self.preprocess(nb, resources)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/preprocessors/execute.py\", line 103, in preprocess\n    self.preprocess_cell(cell, resources, index)\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbconvert/preprocessors/execute.py\", line 124, in preprocess_cell\n    cell = self.execute_cell(cell, index, store_history=True)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/jupyter_core/utils/__init__.py\", line 165, in wrapped\n    return loop.run_until_complete(inner)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/local/lib/python3.12/asyncio/base_events.py\", line 691, in run_until_complete\n    return future.result()\n           ^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbclient/client.py\", line 1062, in async_execute_cell\n    await self._check_raise_for_error(cell, cell_index, exec_reply)\n  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbclient/client.py\", line 918, in _check_raise_for_error\n    raise CellExecutionError.from_cell_and_msg(cell, exec_reply_content)\nnbclient.exceptions.CellExecutionError: An error occurred while executing the following cell:\n------------------\nimport subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru -- not pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\n------------------\n\n\n  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31mimport subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru -- not pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\u001b[39m\n                           ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m unexpected character after line continuation character\n\n\n", "numLines": 66, "startLine": 1, "totalLines": 66}}
```

### [146] TOOL CALL — Bash · 2026-08-21 21:55:23 UTC

```
python3 -c "
import json
nb = json.load(open('code_demo.ipynb'))
c = nb['cells'][1]
print(repr(c['source'])[:300])
print(type(c['source']))
"
```

### [147] TOOL RESULT — Bash · 2026-08-21 21:55:23 UTC

```
{"stdout": "\"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# loguru -- not pre-installed on Colab, always install\\\\n_pip('loguru==0.7.3')\\\\n\\\\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's e\n<class 'str'>", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [148] TOOL CALL — Bash · 2026-08-21 21:55:33 UTC

```
python3 -c "
import json
nb = json.load(open('code_demo.ipynb'))
c = nb['cells'][1]
s = c['source']
print(len(s))
print(s.count(chr(10)))
print(s.count('\\\\n'))
print(s[:80])
"
```

### [149] TOOL RESULT — Bash · 2026-08-21 21:55:33 UTC

```
{"stdout": "445\n0\n8\nimport subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [150] TOOL CALL — Bash · 2026-08-21 21:55:37 UTC

```
python3 -c "
import json
nb = json.load(open('code_demo.ipynb'))
for i,c in enumerate(nb['cells']):
    s = c['source']
    print(i, c['cell_type'], 'real_nl' in str(s.count(chr(10))), s.count(chr(10)), s.count('\\\\n'), s.count('\\\\\\\\'))
"
```

### [151] TOOL RESULT — Bash · 2026-08-21 21:55:37 UTC

```
{"stdout": "0 markdown False 0 17 0\n1 code False 0 8 0\n2 code False 0 27 0\n3 code False 0 11 0\n4 code False 0 2 0\n5 markdown False 0 2 0\n6 code False 0 14 0\n7 markdown False 0 2 0\n8 code False 0 32 0\n9 markdown False 0 2 0\n10 code False 0 67 0\n11 markdown False 0 2 0\n12 code False 0 12 0\n13 markdown False 0 2 0\n14 code False 0 42 1\n15 markdown False 0 2 0\n16 code False 0 6 0\n17 markdown False 0 2 0\n18 code False 0 25 1\n19 markdown False 0 2 0\n20 code False 0 40 3", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [152] TOOL CALL — Bash · 2026-08-21 21:55:43 UTC

```
python3 -c "
import json
nb = json.load(open('code_demo.ipynb'))
for i,c in enumerate(nb['cells']):
    s = c['source']
    if s.count('\\\\\\\\') > 0:
        print(i, repr(s))
"
```

### [153] TOOL RESULT — Bash · 2026-08-21 21:55:43 UTC

```
{"stdout": "14 'def fit_logit(df_in: pd.DataFrame, cols: list[str], label: str) -> dict:\\\\n    if df_in.empty or df_in[\\\\\"survived\\\\\"].nunique() < 2 or len(df_in) < len(cols) + 3:\\\\n        return {\\\\\"status\\\\\": \\\\\"insufficient_data\\\\\", \\\\\"n\\\\\": int(len(df_in)), \\\\\"n_classes\\\\\": int(df_in[\\\\\"survived\\\\\"].nunique()) if not df_in.empty else 0}\\\\n    X = df_in[cols].astype(float)\\\\n    y = df_in[\\\\\"survived\\\\\"].astype(int)\\\\n    X_const = sm.add_constant(X, has_constant=\\\\\"add\\\\\")\\\\n    try:\\\\n        model = sm.Logit(y, X_const).fit(disp=0, maxiter=200)\\\\n    except Exception as e:\\\\n        logger.warning(f\\\\\"[{label}] logit failed ({e}); falling back to parsimonious covariate set\\\\\")\\\\n        parsimonious = [c for c in [\\\\\"founder_share\\\\\", \\\\\"n_diffused_owners\\\\\", \\\\\"log_stars\\\\\", \\\\\"log_devs_at_tfdd\\\\\"] if c in cols]\\\\n        if not parsimonious or parsimonious == cols:\\\\n            return {\\\\\"status\\\\\": f\\\\\"failed:{e}\\\\\", \\\\\"n\\\\\": int(len(df_in))}\\\\n        return fit_logit(df_in, parsimonious, label + \\\\\"_parsimonious\\\\\")\\\\n    std_X = (X - X.mean()) / X.std(ddof=0).replace(0, 1)\\\\n    std_X_const = sm.add_constant(std_X, has_constant=\\\\\"add\\\\\")\\\\n    try:\\\\n        std_model = sm.Logit(y, std_X_const).fit(disp=0, maxiter=200)\\\\n        std_effects = std_model.params.drop(\\\\\"const\\\\\").to_dict()\\\\n    except Exception:\\\\n        std_effects = {}\\\\n    return {\\\\n        \\\\\"status\\\\\": \\\\\"ok\\\\\",\\\\n        \\\\\"n\\\\\": int(len(df_in)),\\\\n        \\\\\"covariates\\\\\": cols,\\\\n        \\\\\"coefs\\\\\": model.params.to_dict(),\\\\n        \\\\\"pvalues\\\\\": model.pvalues.to_dict(),\\\\n        \\\\\"pvalues_bh\\\\\": benjamini_hochberg(model.pvalues.drop(\\\\\"const\\\\\").to_dict()),\\\\n        \\\\\"standardized_effect_sizes\\\\\": std_effects,\\\\n        \\\\\"pseudo_r2\\\\\": float(model.prsquared),\\\\n        \\\\\"converged\\\\\": bool(model.mle_retvals.get(\\\\\"converged\\\\\", True)),\\\\n    }\\\\n\\\\n\\\\nour_cols = [\\\\\"founder_share\\\\\", \\\\\"n_diffused_owners\\\\\", \\\\\"log_stars\\\\\", \\\\\"log_forks\\\\\", \\\\\"log_devs_at_tfdd\\\\\"]\\\\nbaseline_cols = [\\\\\"log_stars\\\\\", \\\\\"log_forks\\\\\", \\\\\"log_devs_at_tfdd\\\\\"]  # Avelino-et-al-style snapshot covariates only, no diffusion trajectory\\\\nregression_our_method = fit_logit(df, our_cols, \\\\\"our_method\\\\\")\\\\nregression_baseline_snapshot_only = fit_logit(df, baseline_cols, \\\\\"baseline\\\\\")\\\\nprint(\\\\\"=== our_method ===\\\\\")\\\\nprint(json.dumps(regression_our_method, indent=2, default=str))\\\\nprint(\\\\\"\\\\\\\\n=== baseline (snapshot-only) ===\\\\\")\\\\nprint(json.dumps(regression_baseline_snapshot_only, indent=2, default=str))'\n18 'if not df.empty and df[\\\\\"survived\\\\\"].nunique() == 2:\\\\n    surv_mask = df[\\\\\"survived\\\\\"].astype(bool)\\\\n    snapshot_covariate_effect_sizes_d = {\\\\n        \\\\\"devs_at_tfdd\\\\\": cohens_d(df.loc[surv_mask, \\\\\"devs_at_tfdd\\\\\"].to_numpy(), df.loc[~surv_mask, \\\\\"devs_at_tfdd\\\\\"].to_numpy()),\\\\n        \\\\\"commits_at_tfdd\\\\\": cohens_d(df.loc[surv_mask, \\\\\"commits_at_tfdd\\\\\"].to_numpy(), df.loc[~surv_mask, \\\\\"commits_at_tfdd\\\\\"].to_numpy()),\\\\n        \\\\\"files_at_tfdd\\\\\": cohens_d(df.loc[surv_mask, \\\\\"files_at_tfdd\\\\\"].to_numpy(), df.loc[~surv_mask, \\\\\"files_at_tfdd\\\\\"].to_numpy()),\\\\n        \\\\\"founder_share_pre_departure\\\\\": cohens_d(df.loc[surv_mask, \\\\\"founder_share\\\\\"].to_numpy(), df.loc[~surv_mask, \\\\\"founder_share\\\\\"].to_numpy()),\\\\n        \\\\\"n_diffused_owners_pre_departure\\\\\": cohens_d(df.loc[surv_mask, \\\\\"n_diffused_owners\\\\\"].to_numpy(), df.loc[~surv_mask, \\\\\"n_diffused_owners\\\\\"].to_numpy()),\\\\n    }\\\\n    mann_whitney_diffusion_vs_survival = {\\\\n        \\\\\"founder_share\\\\\": {\\\\n            \\\\\"u_stat\\\\\": float(stats.mannwhitneyu(df.loc[surv_mask, \\\\\"founder_share\\\\\"], df.loc[~surv_mask, \\\\\"founder_share\\\\\"], alternative=\\\\\"two-sided\\\\\").statistic),\\\\n            \\\\\"p\\\\\": float(stats.mannwhitneyu(df.loc[surv_mask, \\\\\"founder_share\\\\\"], df.loc[~surv_mask, \\\\\"founder_share\\\\\"], alternative=\\\\\"two-sided\\\\\").pvalue),\\\\n        },\\\\n        \\\\\"n_diffused_owners\\\\\": {\\\\n            \\\\\"u_stat\\\\\": float(stats.mannwhitneyu(df.loc[surv_mask, \\\\\"n_diffused_owners\\\\\"], df.loc[~surv_mask, \\\\\"n_diffused_owners\\\\\"], alternative=\\\\\"two-sided\\\\\").statistic),\\\\n            \\\\\"p\\\\\": float(stats.mannwhitneyu(df.loc[surv_mask, \\\\\"n_diffused_owners\\\\\"], df.loc[~surv_mask, \\\\\"n_diffused_owners\\\\\"], alternative=\\\\\"two-sided\\\\\").pvalue),\\\\n        },\\\\n    }\\\\nelse:\\\\n    snapshot_covariate_effect_sizes_d = {\\\\\"status\\\\\": \\\\\"insufficient_class_variation\\\\\"}\\\\n    mann_whitney_diffusion_vs_survival = {\\\\\"status\\\\\": \\\\\"insufficient_class_variation\\\\\"}\\\\n\\\\nprint(\\\\\"Cohen\\'s d:\\\\\", json.dumps(snapshot_covariate_effect_sizes_d, indent=2, default=str))\\\\nprint(\\\\\"\\\\\\\\nMann-Whitney U:\\\\\", json.dumps(mann_whitney_diffusion_vs_survival, indent=2, default=str))'\n20 'n_events = len(df)\\\\nn_survived = int(df[\\\\\"survived\\\\\"].sum())\\\\nsurvival_rate = n_survived / n_events if n_events else float(\\\\\"nan\\\\\")\\\\nprint(f\\\\\"Strict founder-only TFDD events analyzed: {n_events}\\\\\")\\\\nprint(f\\\\\"Unconditioned 18-month post-TFDD survival rate: {survival_rate:.3f} ({n_survived}/{n_events})\\\\\")\\\\nprint(f\\\\\"Avelino et al.\\'s reference survival rate:        0.41\\\\\")\\\\nprint(f\\\\\"\\\\\\\\nour_method pseudo-R^2:  {regression_our_method.get(\\'pseudo_r2\\')}\\\\\")\\\\nprint(f\\\\\"baseline   pseudo-R^2:  {regression_baseline_snapshot_only.get(\\'pseudo_r2\\')}\\\\\")\\\\nprint(f\\\\\"\\\\\\\\nmatched-pairs: n_pairs={matched_pairs_result[\\'n_pairs\\']}, risk_ratio={matched_pairs_result.get(\\'risk_ratio_low_vs_high_diffusion\\')}\\\\\")\\\\n\\\\nfig, axes = plt.subplots(1, 2, figsize=(12, 4.5))\\\\n\\\\n# left: standardized coefficients, our_method vs baseline\\\\nax = axes[0]\\\\nour_std = regression_our_method.get(\\\\\"standardized_effect_sizes\\\\\", {})\\\\nbase_std = regression_baseline_snapshot_only.get(\\\\\"standardized_effect_sizes\\\\\", {})\\\\nall_covs = list(dict.fromkeys(list(our_std.keys()) + list(base_std.keys())))\\\\nx = np.arange(len(all_covs))\\\\nwidth = 0.35\\\\nax.bar(x - width/2, [our_std.get(c, 0) for c in all_covs], width, label=\\\\\"our_method\\\\\")\\\\nax.bar(x + width/2, [base_std.get(c, 0) for c in all_covs], width, label=\\\\\"baseline\\\\\")\\\\nax.set_xticks(x)\\\\nax.set_xticklabels(all_covs, rotation=45, ha=\\\\\"right\\\\\")\\\\nax.axhline(0, color=\\\\\"black\\\\\", linewidth=0.8)\\\\nax.set_ylabel(\\\\\"standardized logistic coefficient\\\\\")\\\\nax.set_title(\\\\\"our_method vs baseline: standardized effects\\\\\")\\\\nax.legend()\\\\n\\\\n# right: founder_share pre-departure vs survival outcome\\\\nax = axes[1]\\\\ncolors = df[\\\\\"survived\\\\\"].map({True: \\\\\"tab:green\\\\\", False: \\\\\"tab:red\\\\\"})\\\\nax.scatter(df[\\\\\"founder_share\\\\\"], df[\\\\\"n_diffused_owners\\\\\"], c=colors, s=80, edgecolor=\\\\\"black\\\\\")\\\\nax.set_xlabel(\\\\\"founder_share (pre-departure window)\\\\\")\\\\nax.set_ylabel(\\\\\"n_diffused_owners (pre-departure window)\\\\\")\\\\nax.set_title(\\\\\"Pre-departure diffusion trajectory vs survival\\\\\\\\n(green=survived, red=did not survive)\\\\\")\\\\n\\\\nplt.tight_layout()\\\\nplt.show()'", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [154] ASSISTANT · 2026-08-21 21:56:51 UTC

```
The notebook has literal backslash-n artifacts from the tool encoding. I'll rebuild the notebook via a Python script instead, using proper triple-quoted strings to avoid escaping issues.
```

### [155] TOOL CALL — Write · 2026-08-21 21:56:51 UTC

```
File: /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/build_nb.py

import json

cells = []

def md(src):
    cells.append({"cell_type": "markdown", "metadata": {}, "source": src.splitlines(keepends=True)})

def code(src):
    cells.append({"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [], "source": src.splitlines(keepends=True)})

md(r"""# Does Founder Authority Diffusion Predict OSS Survival?

This notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.

**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**
1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.
2. Filter to 69 repos passing age/size/fork exclusion criteria.
3. Clone each repo bare and walk its full commit history with `git log --numstat`.
4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.

This produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.

**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**
- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so "mini" here is the full analysis sample, not a truncation).
- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).
- Recomputes Cohen's d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.

The cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.""")

code(r"""import subprocess, sys
def _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])

# loguru -- not pre-installed on Colab, always install
_pip('loguru==0.7.3')

# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env
if 'google.colab' not in sys.modules:
    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')""")

code(r"""from __future__ import annotations

import gc
import json
import math
import random
import sys
import time
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd
import statsmodels.api as sm
from loguru import logger
from scipy import stats

import matplotlib.pyplot as plt  # for the results visualization cell at the end

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")

RNG_SEED = 20260821
random.seed(RNG_SEED)
np.random.seed(RNG_SEED)""")

code(r'''GITHUB_DATA_URL = "https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json"
import json, os

def load_data():
    try:
        import urllib.request
        with urllib.request.urlopen(GITHUB_DATA_URL) as response:
            return json.loads(response.read().decode())
    except Exception: pass
    if os.path.exists("mini_demo_data.json"):
        with open("mini_demo_data.json") as f: return json.load(f)
    raise FileNotFoundError("Could not load mini_demo_data.json")''')

code(r'''raw = load_data()
print(raw["metadata"])
print("n examples:", len(raw["datasets"][0]["examples"]))''')

md(r"""## Config

All tunable parameters from `method.py`'s Stage 5-8 analysis. `N_BOOT` (bootstrap resamples for the matched-pairs risk-ratio) is the only parameter worth scaling for a demo -- it starts small here and can be raised back to the original `5000` from the full run since the bootstrap over 16 rows is cheap either way.""")

code(r"""# Avelino et al.'s TFDD silence threshold / truck-factor coverage cutoff (unused directly in this notebook's
# Stage 5-8 recomputation but kept for reference -- these determined the pre-computed event data)
SILENCE_THRESHOLD_DAYS = 365
TF_COVERAGE_THRESHOLD = 0.5
POST_TFDD_WINDOW_DAYS = 548  # 18 months
PRE_WINDOW_FAR_DAYS = 365  # 12 months before TFDD
PRE_WINDOW_NEAR_DAYS = 180  # 6 months before TFDD

# matched-pairs thresholds (Stage 8)
MATCHED_PAIRS_LOW_THRESH = 0.50
MATCHED_PAIRS_HI_THRESH = 0.80
MATCHED_PAIRS_N_DIFFUSED_MIN = 2

# bootstrap resamples for the risk-ratio CI -- START SMALL, scale back to 5000 (original) after it runs
N_BOOT = 200  # original value: 5000""")

md(r"""## Rebuild the analysis dataframe (Stage 6 output format)

Each loaded example is one strict founder-only TFDD event, with the fields `method.py`'s `events_to_df()` used to build its regression dataframe (`stars`, `forks`, `devs_at_tfdd`, `founder_share`, `n_diffused_owners`, `survived`, plus placebo-window fields). We reconstruct that same dataframe here, including the log-transformed covariates (`log_stars`, `log_forks`, `log_devs_at_tfdd`) `method.py` derives before fitting.""")

code(r'''examples = raw["datasets"][0]["examples"]

rows = []
for e in examples:
    if "metadata_repo" not in e:
        continue  # skip the schema-required placeholder row if no events were found
    rows.append({
        "repo": e["metadata_repo"],
        "founder": e["metadata_founder"],
        "tfdd_date": e["metadata_tfdd_date"],
        "language": e["metadata_language"],
        "stars": e["metadata_stars"],
        "forks": e["metadata_forks"],
        "devs_at_tfdd": e["metadata_devs_at_tfdd"],
        "commits_at_tfdd": e["metadata_commits_at_tfdd"],
        "files_at_tfdd": e["metadata_files_at_tfdd"],
        "founder_share": e["metadata_founder_share_pre_departure"],
        "n_diffused_owners": e["metadata_n_diffused_owners_pre_departure"],
        "placebo_founder_share": e["metadata_placebo_founder_share"],
        "placebo_n_diffused_owners": e["metadata_placebo_n_diffused_owners"],
        "grade": e["metadata_grade"],
        "censored": e["metadata_censored"],
        "survived": e["output"] == "survived",
    })

df = pd.DataFrame(rows)
df["tfdd_date"] = pd.to_datetime(df["tfdd_date"], utc=True)
df["log_stars"] = np.log1p(df["stars"])
df["log_forks"] = np.log1p(df["forks"])
df["log_devs_at_tfdd"] = np.log1p(df["devs_at_tfdd"])
df = df.dropna(subset=["founder_share", "n_diffused_owners", "log_stars", "log_forks", "devs_at_tfdd"])
print(f"analysis dataframe: {len(df)} strict founder-only TFDD events")
df.head()''')

md(r"""## Stage 8 helper functions (copied unchanged from `method.py`)

`build_matched_pairs`, `bootstrap_survival_rate_ratio`, `benjamini_hochberg`, and `cohens_d` -- the exact same functions the full pipeline run used to produce its reported numbers.""")

code(r'''def build_matched_pairs(df: pd.DataFrame, low_thresh: float = 0.50, hi_thresh: float = 0.80, n_diffused_min: int = 2):
    lo = df[(df.founder_share < low_thresh) & (df.n_diffused_owners >= n_diffused_min)].copy()
    hi = df[df.founder_share >= hi_thresh].copy()
    pairs = []
    used_hi = set()
    for _, lrow in lo.iterrows():
        best_idx, best_dist = None, float("inf")
        for hidx, hrow in hi.iterrows():
            if hidx in used_hi:
                continue
            if hrow.language != lrow.language:
                continue
            dist = (
                (math.log1p(hrow.stars) - math.log1p(lrow.stars)) ** 2
                + (math.log1p(hrow.forks) - math.log1p(lrow.forks)) ** 2
                + (math.log1p(hrow.devs_at_tfdd) - math.log1p(lrow.devs_at_tfdd)) ** 2
            )
            if dist < best_dist:
                best_dist, best_idx = dist, hidx
        if best_idx is not None and best_dist < 4.0:  # cap on match distance (~2 log-units per dim)
            used_hi.add(best_idx)
            pairs.append((lrow, hi.loc[best_idx]))
    return pairs


def bootstrap_survival_rate_ratio(pairs: list[tuple[pd.Series, pd.Series]], n_boot: int = N_BOOT):
    if not pairs:
        return float("nan"), (float("nan"), float("nan"))
    lo_surv = np.array([1.0 if p[0].survived else 0.0 for p in pairs])
    hi_surv = np.array([1.0 if p[1].survived else 0.0 for p in pairs])
    n = len(pairs)
    ratios = []
    for _ in range(n_boot):
        idx = np.random.randint(0, n, size=n)
        lo_rate = lo_surv[idx].mean()
        hi_rate = hi_surv[idx].mean()
        if hi_rate == 0:
            continue
        ratios.append((lo_rate + 1e-6) / (hi_rate + 1e-6))
    if not ratios:
        return float("nan"), (float("nan"), float("nan"))
    ratios = np.array(ratios)
    point = (lo_surv.mean() + 1e-6) / (hi_surv.mean() + 1e-6)
    ci = (float(np.percentile(ratios, 2.5)), float(np.percentile(ratios, 97.5)))
    return float(point), ci


def benjamini_hochberg(pvals: dict[str, float]) -> dict[str, float]:
    items = sorted(pvals.items(), key=lambda kv: kv[1])
    m = len(items)
    adj = {}
    prev = 1.0
    for rank, (k, p) in enumerate(reversed(items), start=1):
        r = m - rank + 1
        val = min(prev, p * m / r)
        adj[k] = val
        prev = val
    return adj


def cohens_d(a: np.ndarray, b: np.ndarray) -> float:
    a, b = a[~np.isnan(a)], b[~np.isnan(b)]
    if len(a) < 2 or len(b) < 2:
        return float("nan")
    pooled_sd = math.sqrt(((len(a) - 1) * a.var(ddof=1) + (len(b) - 1) * b.var(ddof=1)) / (len(a) + len(b) - 2))
    if pooled_sd == 0:
        return float("nan")
    return float((a.mean() - b.mean()) / pooled_sd)''')

md(r"""## Matched-pairs bootstrap risk-ratio

Pairs low-diffusion (`founder_share < 0.50`, `n_diffused_owners >= 2`) events with high-diffusion (`founder_share >= 0.80`) events matched on language and log(stars/forks/devs), then bootstraps the survival-rate ratio between the two groups. At n=16 this is known to produce 0 matchable pairs (reported honestly in the artifact summary rather than fabricated).""")

code(r'''matched_pairs_result = {"n_pairs": 0}
if len(df) >= 6:
    pairs = build_matched_pairs(df, MATCHED_PAIRS_LOW_THRESH, MATCHED_PAIRS_HI_THRESH, MATCHED_PAIRS_N_DIFFUSED_MIN)
    risk_ratio, ci95 = bootstrap_survival_rate_ratio(pairs, n_boot=N_BOOT)
    matched_pairs_result = {
        "n_pairs": len(pairs),
        "risk_ratio_low_vs_high_diffusion": risk_ratio,
        "risk_ratio_ci95": list(ci95),
        "note": "risk_ratio = P(survival | low diffusion) / P(survival | high diffusion); >1 means low authority-diffusion (concentrated founder) survives MORE, <1 means diffusion helps survival",
    }
else:
    matched_pairs_result["note"] = "insufficient events for matched-pairs analysis (need >=6)"
print(json.dumps(matched_pairs_result, indent=2, default=str))''')

md(r"""## BH-corrected logistic regression: our_method vs baseline

`fit_logit` (copied unchanged from `method.py`) fits a logistic regression of `survived` on the given covariates, plus a standardized-coefficient refit and Benjamini-Hochberg-corrected p-values. `our_method` adds the pre-departure diffusion trajectory (`founder_share`, `n_diffused_owners`) on top of the Avelino-et-al-style snapshot covariates that the `baseline` model uses alone.""")

code(r'''def fit_logit(df_in: pd.DataFrame, cols: list[str], label: str) -> dict:
    if df_in.empty or df_in["survived"].nunique() < 2 or len(df_in) < len(cols) + 3:
        return {"status": "insufficient_data", "n": int(len(df_in)), "n_classes": int(df_in["survived"].nunique()) if not df_in.empty else 0}
    X = df_in[cols].astype(float)
    y = df_in["survived"].astype(int)
    X_const = sm.add_constant(X, has_constant="add")
    try:
        model = sm.Logit(y, X_const).fit(disp=0, maxiter=200)
    except Exception as e:
        logger.warning(f"[{label}] logit failed ({e}); falling back to parsimonious covariate set")
        parsimonious = [c for c in ["founder_share", "n_diffused_owners", "log_stars", "log_devs_at_tfdd"] if c in cols]
        if not parsimonious or parsimonious == cols:
            return {"status": f"failed:{e}", "n": int(len(df_in))}
        return fit_logit(df_in, parsimonious, label + "_parsimonious")
    std_X = (X - X.mean()) / X.std(ddof=0).replace(0, 1)
    std_X_const = sm.add_constant(std_X, has_constant="add")
    try:
        std_model = sm.Logit(y, std_X_const).fit(disp=0, maxiter=200)
        std_effects = std_model.params.drop("const").to_dict()
    except Exception:
        std_effects = {}
    return {
        "status": "ok",
        "n": int(len(df_in)),
        "covariates": cols,
        "coefs": model.params.to_dict(),
        "pvalues": model.pvalues.to_dict(),
        "pvalues_bh": benjamini_hochberg(model.pvalues.drop("const").to_dict()),
        "standardized_effect_sizes": std_effects,
        "pseudo_r2": float(model.prsquared),
        "converged": bool(model.mle_retvals.get("converged", True)),
    }


our_cols = ["founder_share", "n_diffused_owners", "log_stars", "log_forks", "log_devs_at_tfdd"]
baseline_cols = ["log_stars", "log_forks", "log_devs_at_tfdd"]  # Avelino-et-al-style snapshot covariates only, no diffusion trajectory
regression_our_method = fit_logit(df, our_cols, "our_method")
regression_baseline_snapshot_only = fit_logit(df, baseline_cols, "baseline")
print("=== our_method ===")
print(json.dumps(regression_our_method, indent=2, default=str))
print("\n=== baseline (snapshot-only) ===")
print(json.dumps(regression_baseline_snapshot_only, indent=2, default=str))''')

md(r"""## Placebo-window falsification check (Stage 7)

Each event also carries a `placebo_founder_share`/`placebo_n_diffused_owners` pair computed on a randomly-sampled 6-month window at least a year away from the TFDD window. Refitting the same regression on the placebo metrics tests whether the signal is specific to the pre-departure period, or just a generic property of any window.""")

code(r'''placebo_df = df.dropna(subset=["placebo_founder_share", "placebo_n_diffused_owners"]).copy()
placebo_cols = ["placebo_founder_share", "placebo_n_diffused_owners", "log_stars", "log_forks", "log_devs_at_tfdd"]
placebo_check = {
    "n_events_with_placebo_window": int(len(placebo_df)),
    "regression_placebo_window": fit_logit(placebo_df, placebo_cols, "placebo") if len(placebo_df) >= 8 else {"status": "insufficient_data", "n": int(len(placebo_df))},
}
print(json.dumps(placebo_check, indent=2, default=str))''')

md(r"""## Effect sizes (Cohen's d) and Mann-Whitney U tests

Simple two-group nonparametric comparisons of survived vs. did-not-survive events, for comparability with Avelino et al.'s reported effect sizes (d=0.13-0.26).""")

code(r'''if not df.empty and df["survived"].nunique() == 2:
    surv_mask = df["survived"].astype(bool)
    snapshot_covariate_effect_sizes_d = {
        "devs_at_tfdd": cohens_d(df.loc[surv_mask, "devs_at_tfdd"].to_numpy(), df.loc[~surv_mask, "devs_at_tfdd"].to_numpy()),
        "commits_at_tfdd": cohens_d(df.loc[surv_mask, "commits_at_tfdd"].to_numpy(), df.loc[~surv_mask, "commits_at_tfdd"].to_numpy()),
        "files_at_tfdd": cohens_d(df.loc[surv_mask, "files_at_tfdd"].to_numpy(), df.loc[~surv_mask, "files_at_tfdd"].to_numpy()),
        "founder_share_pre_departure": cohens_d(df.loc[surv_mask, "founder_share"].to_numpy(), df.loc[~surv_mask, "founder_share"].to_numpy()),
        "n_diffused_owners_pre_departure": cohens_d(df.loc[surv_mask, "n_diffused_owners"].to_numpy(), df.loc[~surv_mask, "n_diffused_owners"].to_numpy()),
    }
    mann_whitney_diffusion_vs_survival = {
        "founder_share": {
            "u_stat": float(stats.mannwhitneyu(df.loc[surv_mask, "founder_share"], df.loc[~surv_mask, "founder_share"], alternative="two-sided").statistic),
            "p": float(stats.mannwhitneyu(df.loc[surv_mask, "founder_share"], df.loc[~surv_mask, "founder_share"], alternative="two-sided").pvalue),
        },
        "n_diffused_owners": {
            "u_stat": float(stats.mannwhitneyu(df.loc[surv_mask, "n_diffused_owners"], df.loc[~surv_mask, "n_diffused_owners"], alternative="two-sided").statistic),
            "p": float(stats.mannwhitneyu(df.loc[surv_mask, "n_diffused_owners"], df.loc[~surv_mask, "n_diffused_owners"], alternative="two-sided").pvalue),
        },
    }
else:
    snapshot_covariate_effect_sizes_d = {"status": "insufficient_class_variation"}
    mann_whitney_diffusion_vs_survival = {"status": "insufficient_class_variation"}

print("Cohen's d:", json.dumps(snapshot_covariate_effect_sizes_d, indent=2, default=str))
print("\nMann-Whitney U:", json.dumps(mann_whitney_diffusion_vs_survival, indent=2, default=str))''')

md(r"""## Results summary

Unconditioned 18-month post-TFDD survival rate (cross-check against Avelino et al.'s reported ~41%), plus a bar chart comparing our_method's and the baseline's standardized logistic-regression coefficients, and a scatter of founder_share vs. survival outcome.""")

code(r'''n_events = len(df)
n_survived = int(df["survived"].sum())
survival_rate = n_survived / n_events if n_events else float("nan")
print(f"Strict founder-only TFDD events analyzed: {n_events}")
print(f"Unconditioned 18-month post-TFDD survival rate: {survival_rate:.3f} ({n_survived}/{n_events})")
print(f"Avelino et al.'s reference survival rate:        0.41")
print(f"\nour_method pseudo-R^2:  {regression_our_method.get('pseudo_r2')}")
print(f"baseline   pseudo-R^2:  {regression_baseline_snapshot_only.get('pseudo_r2')}")
print(f"\nmatched-pairs: n_pairs={matched_pairs_result['n_pairs']}, risk_ratio={matched_pairs_result.get('risk_ratio_low_vs_high_diffusion')}")

fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

# left: standardized coefficients, our_method vs baseline
ax = axes[0]
our_std = regression_our_method.get("standardized_effect_sizes", {})
base_std = regression_baseline_snapshot_only.get("standardized_effect_sizes", {})
all_covs = list(dict.fromkeys(list(our_std.keys()) + list(base_std.keys())))
x = np.arange(len(all_covs))
width = 0.35
ax.bar(x - width/2, [our_std.get(c, 0) for c in all_covs], width, label="our_method")
ax.bar(x + width/2, [base_std.get(c, 0) for c in all_covs], width, label="baseline")
ax.set_xticks(x)
ax.set_xticklabels(all_covs, rotation=45, ha="right")
ax.axhline(0, color="black", linewidth=0.8)
ax.set_ylabel("standardized logistic coefficient")
ax.set_title("our_method vs baseline: standardized effects")
ax.legend()

# right: founder_share pre-departure vs survival outcome
ax = axes[1]
colors = df["survived"].map({True: "tab:green", False: "tab:red"})
ax.scatter(df["founder_share"], df["n_diffused_owners"], c=colors, s=80, edgecolor="black")
ax.set_xlabel("founder_share (pre-departure window)")
ax.set_ylabel("n_diffused_owners (pre-departure window)")
ax.set_title("Pre-departure diffusion trajectory vs survival\n(green=survived, red=did not survive)")

plt.tight_layout()
plt.show()''')

nb = {
    "cells": cells,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.12.12"},
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}

with open("code_demo.ipynb", "w") as f:
    json.dump(nb, f, indent=1)
print("wrote", len(cells), "cells")
```

### [156] TOOL RESULT — Write · 2026-08-21 21:56:51 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/build_nb.py", "content": "import json\n\ncells = []\n\ndef md(src):\n    cells.append({\"cell_type\": \"markdown\", \"metadata\": {}, \"source\": src.splitlines(keepends=True)})\n\ndef code(src):\n    cells.append({\"cell_type\": \"code\", \"metadata\": {}, \"execution_count\": None, \"outputs\": [], \"source\": src.splitlines(keepends=True)})\n\nmd(r\"\"\"# Does Founder Authority Diffusion Predict OSS Survival?\n\nThis notebook demonstrates the analysis stages (Stages 5-8) of `method.py`, a re-implementation of Avelino et al.'s (ESEM 2019) Degree-of-Authorship (DOA) / Truck-Factor (TF) / Truck-Factor-Developer-Departure (TFDD) / Active-Inactive survival pipeline, applied to real GitHub commit histories.\n\n**Full pipeline (Stages 0-4, run once against the live GitHub API and local `git log --numstat` history walks):**\n1. Sample 270 candidate repos across 6 languages via the GitHub search API, stratified by popularity.\n2. Filter to 69 repos passing age/size/fork exclusion criteria.\n3. Clone each repo bare and walk its full commit history with `git log --numstat`.\n4. Compute Degree-of-Authorship (DOA) snapshots over time (Fritz et al. 2010 formula) and detect founder-only Truck-Factor-Developer-Departure (TFDD) events: the moment the truck-factor set collapses to a single developer who then goes silent for >= 1 year.\n\nThis produced **16 strict founder-only TFDD events** and 20 relaxed (TF<=2) events, each with a pre-computed 12-to-6-month pre-departure **authority-diffusion trajectory** (`founder_share`, `n_diffused_owners`) and an 18-month post-TFDD survival label.\n\n**This notebook (Stages 5-8, all local computation, no network access needed beyond loading the pre-extracted event data):**\n- Rebuilds the analysis dataframe from the 16 per-event rows (already embedded in `mini_demo_data.json` -- these are the full set of TFDD events found, so \"mini\" here is the full analysis sample, not a truncation).\n- Refits the same BH-corrected logistic regressions (`our_method`: diffusion trajectory + snapshot covariates, vs `baseline`: Avelino-et-al-style snapshot covariates only).\n- Recomputes Cohen's d effect sizes, Mann-Whitney U tests, the matched-pairs bootstrap risk-ratio, and the within-repo placebo-window falsification check -- using the exact same functions as `method.py`, unmodified.\n\nThe cloning/scraping stages (0-4) are NOT re-run here since they require live network access to GitHub and can take close to an hour; the code for those stages is left untouched in `method.py` for reference.\"\"\")\n\ncode(r\"\"\"import subprocess, sys\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\n\n# loguru -- not pre-installed on Colab, always install\n_pip('loguru==0.7.3')\n\n# numpy, pandas, scipy, statsmodels -- pre-installed on Colab, install locally to match Colab's exact env\nif 'google.colab' not in sys.modules:\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3', 'statsmodels==0.14.6', 'matplotlib==3.10.0')\"\"\")\n\ncode(r\"\"\"from __future__ import annotations\n\nimport gc\nimport json\nimport math\nimport random\nimport sys\nimport time\nfrom collections import Counter, defaultdict\nfrom dataclasses import asdict, dataclass, field\nfrom datetime import datetime, timedelta, timezone\nfrom pathlib import Path\nfrom typing import Optional\n\nimport numpy as np\nimport pandas as pd\nimport statsmodels.api as sm\nfrom loguru import logger\nfrom scipy import stats\n\nimport matplotlib.pyplot as plt  # for the results visualization cell at the end\n\nlogger.remove()\nlogger.add(sys.stdout, level=\"INFO\", format=\"{time:HH:mm:ss}|{level:<7}|{message}\")\n\nRNG_SEED = 20260821\nrandom.seed(RNG_SEED)\nnp.random.seed(RNG_SEED)\"\"\")\n\ncode(r'''GITHUB_DATA_URL = \"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json\"\nimport json, os\n\ndef load_data():\n    try:\n        import urllib.request\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\n            return json.loads(response.read().decode())\n    except Exception: pass\n    if os.path.exists(\"mini_demo_data.json\"):\n        with open(\"mini_demo_data.json\") as f: return json.load(f)\n    raise FileNotFoundError(\"Could not load mini_demo_data.json\")''')\n\ncode(r'''raw = load_data()\nprint(raw[\"metadata\"])\nprint(\"n examples:\", len(raw[\"datasets\"][0][\"examples\"]))''')\n\nmd(r\"\"\"## Config\n\nAll tunable parameters from `method.py`'s Stage 5-8 analysis. `N_BOOT` (bootstrap resamples for the matched-pairs risk-ratio) is the only parameter worth scaling for a demo -- it starts small here and can be raised back to the original `5000` from the full run since the bootstrap over 16 rows is cheap either way.\"\"\")\n\ncode(r\"\"\"# Avelino et al.'s TFDD silence threshold / truck-factor coverage cutoff (unused directly in this notebook's\n# Stage 5-8 recomputation but kept for reference -- these determined the pre-computed event data)\nSILENCE_THRESHOLD_DAYS = 365\nTF_COVERAGE_THRESHOLD = 0.5\nPOST_TFDD_WINDOW_DAYS = 548  # 18 months\nPRE_WINDOW_FAR_DAYS = 365  # 12 months before TFDD\nPRE_WINDOW_NEAR_DAYS = 180  # 6 months before TFDD\n\n# matched-pairs thresholds (Stage 8)\nMATCHED_PAIRS_LOW_THRESH = 0.50\nMATCHED_PAIRS_HI_THRESH = 0.80\nMATCHED_PAIRS_N_DIFFUSED_MIN = 2\n\n# bootstrap resamples for the risk-ratio CI -- START SMALL, scale back to 5000 (original) after it runs\nN_BOOT = 200  # original value: 5000\"\"\")\n\nmd(r\"\"\"## Rebuild the analysis dataframe (Stage 6 output format)\n\nEach loaded example is one strict founder-only TFDD event, with the fields `method.py`'s `events_to_df()` used to build its regression dataframe (`stars`, `forks`, `devs_at_tfdd`, `founder_share`, `n_diffused_owners`, `survived`, plus placebo-window fields). We reconstruct that same dataframe here, including the log-transformed covariates (`log_stars`, `log_forks`, `log_devs_at_tfdd`) `method.py` derives before fitting.\"\"\")\n\ncode(r'''examples = raw[\"datasets\"][0][\"examples\"]\n\nrows = []\nfor e in examples:\n    if \"metadata_repo\" not in e:\n        continue  # skip the schema-required placeholder row if no events were found\n    rows.append({\n        \"repo\": e[\"metadata_repo\"],\n        \"founder\": e[\"metadata_founder\"],\n        \"tfdd_date\": e[\"metadata_tfdd_date\"],\n        \"language\": e[\"metadata_language\"],\n        \"stars\": e[\"metadata_stars\"],\n        \"forks\": e[\"metadata_forks\"],\n        \"devs_at_tfdd\": e[\"metadata_devs_at_tfdd\"],\n        \"commits_at_tfdd\": e[\"metadata_commits_at_tfdd\"],\n        \"files_at_tfdd\": e[\"metadata_files_at_tfdd\"],\n        \"founder_share\": e[\"metadata_founder_share_pre_departure\"],\n        \"n_diffused_owners\": e[\"metadata_n_diffused_owners_pre_departure\"],\n        \"placebo_founder_share\": e[\"metadata_placebo_founder_share\"],\n        \"placebo_n_diffused_owners\": e[\"metadata_placebo_n_diffused_owners\"],\n        \"grade\": e[\"metadata_grade\"],\n        \"censored\": e[\"metadata_censored\"],\n        \"survived\": e[\"output\"] == \"survived\",\n    })\n\ndf = pd.DataFrame(rows)\ndf[\"tfdd_date\"] = pd.to_datetime(df[\"tfdd_date\"], utc=True)\ndf[\"log_stars\"] = np.log1p(df[\"stars\"])\ndf[\"log_forks\"] = np.log1p(df[\"forks\"])\ndf[\"log_devs_at_tfdd\"] = np.log1p(df[\"devs_at_tfdd\"])\ndf = df.dropna(subset=[\"founder_share\", \"n_diffused_owners\", \"log_stars\", \"log_forks\", \"devs_at_tfdd\"])\nprint(f\"analysis dataframe: {len(df)} strict founder-only TFDD events\")\ndf.head()''')\n\nmd(r\"\"\"## Stage 8 helper functions (copied unchanged from `method.py`)\n\n`build_matched_pairs`, `bootstrap_survival_rate_ratio`, `benjamini_hochberg`, and `cohens_d` -- the exact same functions the full pipeline run used to produce its reported numbers.\"\"\")\n\ncode(r'''def build_matched_pairs(df: pd.DataFrame, low_thresh: float = 0.50, hi_thresh: float = 0.80, n_diffused_min: int = 2):\n    lo = df[(df.founder_share < low_thresh) & (df.n_diffused_owners >= n_diffused_min)].copy()\n    hi = df[df.founder_share >= hi_thresh].copy()\n    pairs = []\n    used_hi = set()\n    for _, lrow in lo.iterrows():\n        best_idx, best_dist = None, float(\"inf\")\n        for hidx, hrow in hi.iterrows():\n            if hidx in used_hi:\n                continue\n            if hrow.language != lrow.language:\n                continue\n            dist = (\n                (math.log1p(hrow.stars) - math.log1p(lrow.stars)) ** 2\n                + (math.log1p(hrow.forks) - math.log1p(lrow.forks)) ** 2\n                + (math.log1p(hrow.devs_at_tfdd) - math.log1p(lrow.devs_at_tfdd)) ** 2\n            )\n            if dist < best_dist:\n                best_dist, best_idx = dist, hidx\n        if best_idx is not None and best_dist < 4.0:  # cap on match distance (~2 log-units per dim)\n            used_hi.add(best_idx)\n            pairs.append((lrow, hi.loc[best_idx]))\n    return pairs\n\n\ndef bootstrap_survival_rate_ratio(pairs: list[tuple[pd.Series, pd.Series]], n_boot: int = N_BOOT):\n    if not pairs:\n        return float(\"nan\"), (float(\"nan\"), float(\"nan\"))\n    lo_surv = np.array([1.0 if p[0].survived else 0.0 for p in pairs])\n    hi_surv = np.array([1.0 if p[1].survived else 0.0 for p in pairs])\n    n = len(pairs)\n    ratios = []\n    for _ in range(n_boot):\n        idx = np.random.randint(0, n, size=n)\n        lo_rate = lo_surv[idx].mean()\n        hi_rate = hi_surv[idx].mean()\n        if hi_rate == 0:\n            continue\n        ratios.append((lo_rate + 1e-6) / (hi_rate + 1e-6))\n    if not ratios:\n        return float(\"nan\"), (float(\"nan\"), float(\"nan\"))\n    ratios = np.array(ratios)\n    point = (lo_surv.mean() + 1e-6) / (hi_surv.mean() + 1e-6)\n    ci = (float(np.percentile(ratios, 2.5)), float(np.percentile(ratios, 97.5)))\n    return float(point), ci\n\n\ndef benjamini_hochberg(pvals: dict[str, float]) -> dict[str, float]:\n    items = sorted(pvals.items(), key=lambda kv: kv[1])\n    m = len(items)\n    adj = {}\n    prev = 1.0\n    for rank, (k, p) in enumerate(reversed(items), start=1):\n        r = m - rank + 1\n        val = min(prev, p * m / r)\n        adj[k] = val\n        prev = val\n    return adj\n\n\ndef cohens_d(a: np.ndarray, b: np.ndarray) -> float:\n    a, b = a[~np.isnan(a)], b[~np.isnan(b)]\n    if len(a) < 2 or len(b) < 2:\n        return float(\"nan\")\n    pooled_sd = math.sqrt(((len(a) - 1) * a.var(ddof=1) + (len(b) - 1) * b.var(ddof=1)) / (len(a) + len(b) - 2))\n    if pooled_sd == 0:\n        return float(\"nan\")\n    return float((a.mean() - b.mean()) / pooled_sd)''')\n\nmd(r\"\"\"## Matched-pairs bootstrap risk-ratio\n\nPairs low-diffusion (`founder_share < 0.50`, `n_diffused_owners >= 2`) events with high-diffusion (`founder_share >= 0.80`) events matched on language and log(stars/forks/devs), then bootstraps the survival-rate ratio between the two groups. At n=16 this is known to produce 0 matchable pairs (reported honestly in the artifact summary rather than fabricated).\"\"\")\n\ncode(r'''matched_pairs_result = {\"n_pairs\": 0}\nif len(df) >= 6:\n    pairs = build_matched_pairs(df, MATCHED_PAIRS_LOW_THRESH, MATCHED_PAIRS_HI_THRESH, MATCHED_PAIRS_N_DIFFUSED_MIN)\n    risk_ratio, ci95 = bootstrap_survival_rate_ratio(pairs, n_boot=N_BOOT)\n    matched_pairs_result = {\n        \"n_pairs\": len(pairs),\n        \"risk_ratio_low_vs_high_diffusion\": risk_ratio,\n        \"risk_ratio_ci95\": list(ci95),\n        \"note\": \"risk_ratio = P(survival | low diffusion) / P(survival | high diffusion); >1 means low authority-diffusion (concentrated founder) survives MORE, <1 means diffusion helps survival\",\n    }\nelse:\n    matched_pairs_result[\"note\"] = \"insufficient events for matched-pairs analysis (need >=6)\"\nprint(json.dumps(matched_pairs_result, indent=2, default=str))''')\n\nmd(r\"\"\"## BH-corrected logistic regression: our_method vs baseline\n\n`fit_logit` (copied unchanged from `method.py`) fits a logistic regression of `survived` on the given covariates, plus a standardized-coefficient refit and Benjamini-Hochberg-corrected p-values. `our_method` adds the pre-departure diffusion trajectory (`founder_share`, `n_diffused_owners`) on top of the Avelino-et-al-style snapshot covariates that the `baseline` model uses alone.\"\"\")\n\ncode(r'''def fit_logit(df_in: pd.DataFrame, cols: list[str], label: str) -> dict:\n    if df_in.empty or df_in[\"survived\"].nunique() < 2 or len(df_in) < len(cols) + 3:\n        return {\"status\": \"insufficient_data\", \"n\": int(len(df_in)), \"n_classes\": int(df_in[\"survived\"].nunique()) if not df_in.empty else 0}\n    X = df_in[cols].astype(float)\n    y = df_in[\"survived\"].astype(int)\n    X_const = sm.add_constant(X, has_constant=\"add\")\n    try:\n        model = sm.Logit(y, X_const).fit(disp=0, maxiter=200)\n    except Exception as e:\n        logger.warning(f\"[{label}] logit failed ({e}); falling back to parsimonious covariate set\")\n        parsimonious = [c for c in [\"founder_share\", \"n_diffused_owners\", \"log_stars\", \"log_devs_at_tfdd\"] if c in cols]\n        if not parsimonious or parsimonious == cols:\n            return {\"status\": f\"failed:{e}\", \"n\": int(len(df_in))}\n        return fit_logit(df_in, parsimonious, label + \"_parsimonious\")\n    std_X = (X - X.mean()) / X.std(ddof=0).replace(0, 1)\n    std_X_const = sm.add_constant(std_X, has_constant=\"add\")\n    try:\n        std_model = sm.Logit(y, std_X_const).fit(disp=0, maxiter=200)\n        std_effects = std_model.params.drop(\"const\").to_dict()\n    except Exception:\n        std_effects = {}\n    return {\n        \"status\": \"ok\",\n        \"n\": int(len(df_in)),\n        \"covariates\": cols,\n        \"coefs\": model.params.to_dict(),\n        \"pvalues\": model.pvalues.to_dict(),\n        \"pvalues_bh\": benjamini_hochberg(model.pvalues.drop(\"const\").to_dict()),\n        \"standardized_effect_sizes\": std_effects,\n        \"pseudo_r2\": float(model.prsquared),\n        \"converged\": bool(model.mle_retvals.get(\"converged\", True)),\n    }\n\n\nour_cols = [\"founder_share\", \"n_diffused_owners\", \"log_stars\", \"log_forks\", \"log_devs_at_tfdd\"]\nbaseline_cols = [\"log_stars\", \"log_forks\", \"log_devs_at_tfdd\"]  # Avelino-et-al-style snapshot covariates only, no diffusion trajectory\nregression_our_method = fit_logit(df, our_cols, \"our_method\")\nregression_baseline_snapshot_only = fit_logit(df, baseline_cols, \"baseline\")\nprint(\"=== our_method ===\")\nprint(json.dumps(regression_our_method, indent=2, default=str))\nprint(\"\\n=== baseline (snapshot-only) ===\")\nprint(json.dumps(regression_baseline_snapshot_only, indent=2, default=str))''')\n\nmd(r\"\"\"## Placebo-window falsification check (Stage 7)\n\nEach event also carries a `placebo_founder_share`/`placebo_n_diffused_owners` pair computed on a randomly-sampled 6-month window at least a year away from the TFDD window. Refitting the same regression on the placebo metrics tests whether the signal is specific to the pre-departure period, or just a generic property of any window.\"\"\")\n\ncode(r'''placebo_df = df.dropna(subset=[\"placebo_founder_share\", \"placebo_n_diffused_owners\"]).copy()\nplacebo_cols = [\"placebo_founder_share\", \"placebo_n_diffused_owners\", \"log_stars\", \"log_forks\", \"log_devs_at_tfdd\"]\nplacebo_check = {\n    \"n_events_with_placebo_window\": int(len(placebo_df)),\n    \"regression_placebo_window\": fit_logit(placebo_df, placebo_cols, \"placebo\") if len(placebo_df) >= 8 else {\"status\": \"insufficient_data\", \"n\": int(len(placebo_df))},\n}\nprint(json.dumps(placebo_check, indent=2, default=str))''')\n\nmd(r\"\"\"## Effect sizes (Cohen's d) and Mann-Whitney U tests\n\nSimple two-group nonparametric comparisons of survived vs. did-not-survive events, for comparability with Avelino et al.'s reported effect sizes (d=0.13-0.26).\"\"\")\n\ncode(r'''if not df.empty and df[\"survived\"].nunique() == 2:\n    surv_mask = df[\"survived\"].astype(bool)\n    snapshot_covariate_effect_sizes_d = {\n        \"devs_at_tfdd\": cohens_d(df.loc[surv_mask, \"devs_at_tfdd\"].to_numpy(), df.loc[~surv_mask, \"devs_at_tfdd\"].to_numpy()),\n        \"commits_at_tfdd\": cohens_d(df.loc[surv_mask, \"commits_at_tfdd\"].to_numpy(), df.loc[~surv_mask, \"commits_at_tfdd\"].to_numpy()),\n        \"files_at_tfdd\": cohens_d(df.loc[surv_mask, \"files_at_tfdd\"].to_numpy(), df.loc[~surv_mask, \"files_at_tfdd\"].to_numpy()),\n        \"founder_share_pre_departure\": cohens_d(df.loc[surv_mask, \"founder_share\"].to_numpy(), df.loc[~surv_mask, \"founder_share\"].to_numpy()),\n        \"n_diffused_owners_pre_departure\": cohens_d(df.loc[surv_mask, \"n_diffused_owners\"].to_numpy(), df.loc[~surv_mask, \"n_diffused_owners\"].to_numpy()),\n    }\n    mann_whitney_diffusion_vs_survival = {\n        \"founder_share\": {\n            \"u_stat\": float(stats.mannwhitneyu(df.loc[surv_mask, \"founder_share\"], df.loc[~surv_mask, \"founder_share\"], alternative=\"two-sided\").statistic),\n            \"p\": float(stats.mannwhitneyu(df.loc[surv_mask, \"founder_share\"], df.loc[~surv_mask, \"founder_share\"], alternative=\"two-sided\").pvalue),\n        },\n        \"n_diffused_owners\": {\n            \"u_stat\": float(stats.mannwhitneyu(df.loc[surv_mask, \"n_diffused_owners\"], df.loc[~surv_mask, \"n_diffused_owners\"], alternative=\"two-sided\").statistic),\n            \"p\": float(stats.mannwhitneyu(df.loc[surv_mask, \"n_diffused_owners\"], df.loc[~surv_mask, \"n_diffused_owners\"], alternative=\"two-sided\").pvalue),\n        },\n    }\nelse:\n    snapshot_covariate_effect_sizes_d = {\"status\": \"insufficient_class_variation\"}\n    mann_whitney_diffusion_vs_survival = {\"status\": \"insufficient_class_variation\"}\n\nprint(\"Cohen's d:\", json.dumps(snapshot_covariate_effect_sizes_d, indent=2, default=str))\nprint(\"\\nMann-Whitney U:\", json.dumps(mann_whitney_diffusion_vs_survival, indent=2, default=str))''')\n\nmd(r\"\"\"## Results summary\n\nUnconditioned 18-month post-TFDD survival rate (cross-check against Avelino et al.'s reported ~41%), plus a bar chart comparing our_method's and the baseline's standardized logistic-regression coefficients, and a scatter of founder_share vs. survival outcome.\"\"\")\n\ncode(r'''n_events = len(df)\nn_survived = int(df[\"survived\"].sum())\nsurvival_rate = n_survived / n_events if n_events else float(\"nan\")\nprint(f\"Strict founder-only TFDD events analyzed: {n_events}\")\nprint(f\"Unconditioned 18-month post-TFDD survival rate: {survival_rate:.3f} ({n_survived}/{n_events})\")\nprint(f\"Avelino et al.'s reference survival rate:        0.41\")\nprint(f\"\\nour_method pseudo-R^2:  {regression_our_method.get('pseudo_r2')}\")\nprint(f\"baseline   pseudo-R^2:  {regression_baseline_snapshot_only.get('pseudo_r2')}\")\nprint(f\"\\nmatched-pairs: n_pairs={matched_pairs_result['n_pairs']}, risk_ratio={matched_pairs_result.get('risk_ratio_low_vs_high_diffusion')}\")\n\nfig, axes = plt.subplots(1, 2, figsize=(12, 4.5))\n\n# left: standardized coefficients, our_method vs baseline\nax = axes[0]\nour_std = regression_our_method.get(\"standardized_effect_sizes\", {})\nbase_std = regression_baseline_snapshot_only.get(\"standardized_effect_sizes\", {})\nall_covs = list(dict.fromkeys(list(our_std.keys()) + list(base_std.keys())))\nx = np.arange(len(all_covs))\nwidth = 0.35\nax.bar(x - width/2, [our_std.get(c, 0) for c in all_covs], width, label=\"our_method\")\nax.bar(x + width/2, [base_std.get(c, 0) for c in all_covs], width, label=\"baseline\")\nax.set_xticks(x)\nax.set_xticklabels(all_covs, rotation=45, ha=\"right\")\nax.axhline(0, color=\"black\", linewidth=0.8)\nax.set_ylabel(\"standardized logistic coefficient\")\nax.set_title(\"our_method vs baseline: standardized effects\")\nax.legend()\n\n# right: founder_share pre-departure vs survival outcome\nax = axes[1]\ncolors = df[\"survived\"].map({True: \"tab:green\", False: \"tab:red\"})\nax.scatter(df[\"founder_share\"], df[\"n_diffused_owners\"], c=colors, s=80, edgecolor=\"black\")\nax.set_xlabel(\"founder_share (pre-departure window)\")\nax.set_ylabel(\"n_diffused_owners (pre-departure window)\")\nax.set_title(\"Pre-departure diffusion trajectory vs survival\\n(green=survived, red=did not survive)\")\n\nplt.tight_layout()\nplt.show()''')\n\nnb = {\n    \"cells\": cells,\n    \"metadata\": {\n        \"kernelspec\": {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"},\n        \"language_info\": {\"name\": \"python\", \"version\": \"3.12.12\"},\n    },\n    \"nbformat\": 4,\n    \"nbformat_minor\": 5,\n}\n\nwith open(\"code_demo.ipynb\", \"w\") as f:\n    json.dump(nb, f, indent=1)\nprint(\"wrote\", len(cells), \"cells\")\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [157] TOOL CALL — Bash · 2026-08-21 21:56:55 UTC

```
python3 build_nb.py && python3 -c "
import json
nb=json.load(open('code_demo.ipynb'))
print(len(nb['cells']))
c=nb['cells'][1]['source']
print(''.join(c)[:200])
"
```

### [158] TOOL RESULT — Bash · 2026-08-21 21:56:55 UTC

```
{"stdout": "wrote 21 cells\n21\nimport subprocess, sys\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\n\n# loguru -- not pre-installed on Colab, always install\n_pip('loguru==0.7.3')\n\n# numpy, p", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [159] ASSISTANT · 2026-08-21 21:56:59 UTC

```
Now let's re-run the notebook execution test.
```

### [160] TOOL CALL — Bash · 2026-08-21 21:56:59 UTC

```
.nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb > /tmp/nbrun2.log 2>&1; echo EXIT:$?
```

### [161] TOOL RESULT — Bash · 2026-08-21 21:56:59 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bp8q6nc2g"}
```

### [162] TOOL CALL — Bash · 2026-08-21 22:07:07 UTC

```
cat /tmp/nbrun2.log 2>&1 | tail -150
```

### [163] TOOL RESULT — Bash · 2026-08-21 22:07:09 UTC

```
{"stdout": "[NbConvertApp] Converting notebook code_demo.ipynb to notebook\n/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.\n  _validate(nbdict, ref, version, version_minor, relax_add_props)\n[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [164] ASSISTANT · 2026-08-21 22:07:15 UTC

```
It seems the notebook finished running successfully (no traceback, no EXIT line since it's still going or truncated). Let me check the exit and the executed notebook content.
```

### [165] TOOL CALL — Bash · 2026-08-21 22:07:15 UTC

```
tail -5 /tmp/nbrun2.log; echo ---; jobs; ps aux | grep b9eiwstn 2>/dev/null; echo ---
python3 -c "
import json
nb=json.load(open('code_demo.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        print(i, c.get('execution_count'), [o.get('output_type') for o in c.get('outputs',[])])
"
```

### [166] TOOL RESULT — Bash · 2026-08-21 22:07:17 UTC

```
{"stdout": "  _validate(nbdict, ref, version, version_minor, relax_add_props)\n[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n---\nroot         810  0.0  0.0   4492  1536 ?        Ss   22:07   0:00 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1787350028976-7pb5g6.sh 2>/dev/null || true && shopt -u extglob 2>/dev/null || true && { \\builtin unalias -- 'unsetenv'; \\builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'tail -5 /tmp/nbrun2.log; echo ---; jobs; ps aux | grep b9eiwstn 2>/dev/null; echo --- python3 -c \" import json nb=json.load(open('\"'\"'code_demo.ipynb'\"'\"')) for i,c in enumerate(nb['\"'\"'cells'\"'\"']):     if c['\"'\"'cell_type'\"'\"']=='\"'\"'code'\"'\"':         print(i, c.get('\"'\"'execution_count'\"'\"'), [o.get('\"'\"'output_type'\"'\"') for o in c.get('\"'\"'outputs'\"'\"',[])]) \"' < /dev/null && pwd -P >| /tmp/claude-f157-cwd\nroot         814  0.0  0.0   4492     0 ?        S    22:07   0:00 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1787350028976-7pb5g6.sh 2>/dev/null || true && shopt -u extglob 2>/dev/null || true && { \\builtin unalias -- 'unsetenv'; \\builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'tail -5 /tmp/nbrun2.log; echo ---; jobs; ps aux | grep b9eiwstn 2>/dev/null; echo --- python3 -c \" import json nb=json.load(open('\"'\"'code_demo.ipynb'\"'\"')) for i,c in enumerate(nb['\"'\"'cells'\"'\"']):     if c['\"'\"'cell_type'\"'\"']=='\"'\"'code'\"'\"':         print(i, c.get('\"'\"'execution_count'\"'\"'), [o.get('\"'\"'output_type'\"'\"') for o in c.get('\"'\"'outputs'\"'\"',[])]) \"' < /dev/null && pwd -P >| /tmp/claude-f157-cwd\nroot         815  0.0  0.0 1397064 4620 ?        Sl   22:07   0:00 ugrep -G --ignore-files --hidden -I --exclude-dir=.git --exclude-dir=.svn --exclude-dir=.hg --exclude-dir=.bzr --exclude-dir=.jj --exclude-dir=.sl b9eiwstn\n---\n1 None []\n2 None []\n3 None []\n4 None []\n6 None []\n8 None []\n10 None []\n12 None []\n14 None []\n16 None []\n18 None []\n20 None []", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [167] TOOL CALL — TaskOutput · 2026-08-21 22:07:21 UTC

```
{'task_id': 'bp8q6nc2g', 'block': True, 'timeout': 300000}
```

### [168] TOOL RESULT — TaskOutput [ERROR] · 2026-08-21 22:07:21 UTC

```
Error: No task found with ID: bp8q6nc2g
```

### [169] TOOL CALL — Bash · 2026-08-21 22:07:23 UTC

```
pgrep -af nbconvert; pgrep -af ipykernel_launcher
```

### [170] TOOL RESULT — Bash · 2026-08-21 22:07:23 UTC

```
{"stdout": "821 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1787350028976-7pb5g6.sh 2>/dev/null || true && shopt -u extglob 2>/dev/null || true && { \\builtin unalias -- 'unsetenv'; \\builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'pgrep -af nbconvert; pgrep -af ipykernel_launcher' < /dev/null && pwd -P >| /tmp/claude-2fad-cwd\n821 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1787350028976-7pb5g6.sh 2>/dev/null || true && shopt -u extglob 2>/dev/null || true && { \\builtin unalias -- 'unsetenv'; \\builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'pgrep -af nbconvert; pgrep -af ipykernel_launcher' < /dev/null && pwd -P >| /tmp/claude-2fad-cwd", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [171] ASSISTANT · 2026-08-21 22:07:29 UTC

```
The nbconvert process is no longer running — it must have died with the previous session. Let me re-run it.
```

### [172] TOOL CALL — Bash · 2026-08-21 22:07:29 UTC

```
.nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb > /tmp/nbrun3.log 2>&1; echo EXIT:$? >> /tmp/nbrun3.log
```

### [173] TOOL RESULT — Bash · 2026-08-21 22:07:29 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bo0m4shm9"}
```

### [174] TOOL CALL — TaskOutput · 2026-08-21 22:12:32 UTC

```
{'task_id': 'bo0m4shm9', 'block': True, 'timeout': 300000}
```

### [175] TOOL RESULT — TaskOutput · 2026-08-21 22:12:32 UTC

```
{"retrieval_status": "timeout", "task": {"task_id": "bo0m4shm9", "task_type": "local_bash", "status": "running", "description": ".nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb > /tmp/nbrun3.log 2>&1; echo EXIT:$? >> /tmp/nbrun3.log", "output": "", "exitCode": null}}
```

### [176] TOOL CALL — TaskOutput · 2026-08-21 22:13:34 UTC

```
{'task_id': 'bo0m4shm9', 'block': True, 'timeout': 300000}
```

### [177] TOOL RESULT — TaskOutput · 2026-08-21 22:13:34 UTC

```
{"retrieval_status": "success", "task": {"task_id": "bo0m4shm9", "task_type": "local_bash", "status": "completed", "description": ".nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb > /tmp/nbrun3.log 2>&1; echo EXIT:$? >> /tmp/nbrun3.log", "output": "\n[exited with code 0]\n", "exitCode": 0}}
```

### [178] TOOL CALL — Bash · 2026-08-21 22:13:36 UTC

```
tail -20 /tmp/nbrun3.log; echo ===; python3 -c "
import json
nb=json.load(open('code_demo.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        errs=[o for o in c.get('outputs',[]) if o.get('output_type')=='error']
        print(i, c.get('execution_count'), 'ERROR' if errs else 'ok')
"
```

### [179] TOOL RESULT — Bash · 2026-08-21 22:13:38 UTC

```
{"stdout": "  File \"/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbclient/client.py\", line 918, in _check_raise_for_error\n    raise CellExecutionError.from_cell_and_msg(cell, exec_reply_content)\nnbclient.exceptions.CellExecutionError: An error occurred while executing the following cell:\n------------------\nraw = load_data()\nprint(raw[\"metadata\"])\nprint(\"n examples:\", len(raw[\"datasets\"][0][\"examples\"]))\n------------------\n\n\n\u001b[31m---------------------------------------------------------------------------\u001b[39m\n\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)\n\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[4]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[32m      1\u001b[39m raw = load_data()\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m print(raw[\u001b[33m\"metadata\"\u001b[39m])\n\u001b[32m      3\u001b[39m print(\u001b[33m\"n examples:\"\u001b[39m, len(raw[\u001b[33m\"datasets\"\u001b[39m][\u001b[32m0\u001b[39m][\u001b[33m\"examples\"\u001b[39m]))\n\n\u001b[31mTypeError\u001b[39m: list indices must be integers or slices, not str\n\nEXIT:1\n===\n1 None ok\n2 None ok\n3 None ok\n4 None ok\n6 None ok\n8 None ok\n10 None ok\n12 None ok\n14 None ok\n16 None ok\n18 None ok\n20 None ok", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [180] TOOL CALL — Bash · 2026-08-21 22:13:42 UTC

```
python3 -c "
import json
d=json.load(open('mini_demo_data.json'))
print(type(d))
print(d if not isinstance(d, (list,dict)) else (list(d.keys()) if isinstance(d,dict) else len(d)))
"
```

### [181] TOOL RESULT — Bash · 2026-08-21 22:13:42 UTC

```
{"stdout": "<class 'dict'>\n['metadata', 'datasets']", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [182] TOOL CALL — Bash · 2026-08-21 22:13:50 UTC

```
.nb_env/bin/python3 -c "
import urllib.request, json
try:
    with urllib.request.urlopen('https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json', timeout=5) as r:
        d = json.loads(r.read().decode())
        print(type(d), str(d)[:200])
except Exception as e:
    print('EXC', e)
"
```

### [183] TOOL RESULT — Bash · 2026-08-21 22:13:50 UTC

```
{"stdout": "<class 'list'> [{'repo': 'synthetic/repo0', 'repo_metadata': {'full_name': 'synthetic/repo0', 'stars': 100, 'forks': 10, 'language': 'Python', 'license': 'mit'}, 'commits': [{'sha': 'r0c0', 'timestamp': '2016-01-01T", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [184] TOOL CALL — Bash · 2026-08-21 22:14:02 UTC

```
cd /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty
sed -i 's#https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json#https://raw.githubusercontent.com/ai-inventor-outputs/DOES-NOT-EXIST-TEST-ONLY/mini_demo_data.json#' code_demo.ipynb
grep -o 'GITHUB_DATA_URL = "[^"]*"' code_demo.ipynb
```

### [185] TOOL RESULT — Bash · 2026-08-21 22:14:04 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "returnCodeInterpretation": "No matches found", "noOutputExpected": false}
```

### [186] TOOL CALL — Bash · 2026-08-21 22:14:06 UTC

```
python3 -c "
import json
nb=json.load(open('code_demo.ipynb'))
print(''.join(nb['cells'][4]['source'])[:200])
"
```

### [187] TOOL RESULT — Bash · 2026-08-21 22:14:08 UTC

```
{"stdout": "raw = load_data()\nprint(raw[\"metadata\"])\nprint(\"n examples:\", len(raw[\"datasets\"][0][\"examples\"]))", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [188] TOOL CALL — Bash · 2026-08-21 22:14:12 UTC

```
grep -n "GITHUB_DATA_URL" code_demo.ipynb | head -3
```

### [189] TOOL RESULT — Bash · 2026-08-21 22:14:12 UTC

```
{"stdout": "86:    \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/DOES-NOT-EXIST-TEST-ONLY/mini_demo_data.json\\\"\\n\",\n92:    \"        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n\",", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [190] ASSISTANT · 2026-08-21 22:14:16 UTC

```
Good, sed worked. Now let's re-run the test with the broken URL to validate the local fallback path.
```

### [191] TOOL CALL — Bash · 2026-08-21 22:14:16 UTC

```
.nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb > /tmp/nbrun4.log 2>&1; echo EXIT:$? >> /tmp/nbrun4.log
```

### [192] TOOL RESULT — Bash · 2026-08-21 22:14:16 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bohnqtfqw"}
```

### [193] TOOL CALL — TaskOutput · 2026-08-21 22:17:00 UTC

```
{'task_id': 'bohnqtfqw', 'block': True, 'timeout': 300000}
```

### [194] TOOL RESULT — TaskOutput · 2026-08-21 22:17:00 UTC

```
{"retrieval_status": "success", "task": {"task_id": "bohnqtfqw", "task_type": "local_bash", "status": "completed", "description": ".nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb > /tmp/nbrun4.log 2>&1; echo EXIT:$? >> /tmp/nbrun4.log", "output": "\n[exited with code 0]\n", "exitCode": 0}}
```

### [195] TOOL CALL — Bash · 2026-08-21 22:17:04 UTC

```
tail -30 /tmp/nbrun4.log
```

### [196] TOOL RESULT — Bash · 2026-08-21 22:17:04 UTC

```
{"stdout": "[NbConvertApp] Converting notebook code_demo.ipynb to notebook\n/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.\n  _validate(nbdict, ref, version, version_minor, relax_add_props)\n[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n[NbConvertApp] Writing 139629 bytes to code_demo.ipynb\nEXIT:0", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [197] ASSISTANT · 2026-08-21 22:17:06 UTC

```
Success. Let's check for errors and inspect output content.
```

### [198] TOOL CALL — Bash · 2026-08-21 22:17:06 UTC

```
python3 -c "
import json
nb=json.load(open('code_demo.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        errs=[o for o in c.get('outputs',[]) if o.get('output_type')=='error']
        print(i, c.get('execution_count'), 'ERROR:'+str(errs) if errs else 'ok')
"
```

### [199] TOOL RESULT — Bash · 2026-08-21 22:17:08 UTC

```
{"stdout": "1 1 ok\n2 2 ok\n3 3 ok\n4 4 ok\n6 5 ok\n8 6 ok\n10 7 ok\n12 8 ok\n14 9 ok\n16 10 ok\n18 11 ok\n20 12 ok", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [200] ASSISTANT · 2026-08-21 22:17:10 UTC

```
All 12 code cells executed successfully. Let's check key outputs to make sure the numbers are sensible.
```

### [201] TOOL CALL — Bash · 2026-08-21 22:17:10 UTC

```
python3 -c "
import json
nb=json.load(open('code_demo.ipynb'))
for i in [4,6,8,10,12,14,16,18,20]:
    c=nb['cells'][i]
    print('=== cell',i,'===')
    for o in c.get('outputs',[]):
        if o.get('output_type')=='stream':
            print(''.join(o['text'])[:800])
        elif o.get('output_type')=='execute_result':
            print(str(o.get('data',{}).get('text/plain',''))[:400])
    print()
"
```

### [202] TOOL RESULT — Bash · 2026-08-21 22:17:12 UTC

```
{"stdout": "=== cell 4 ===\n{'method_name': 'founder_authority_diffusion_tfdd_survival', 'description': 'Founder-only TFDD survival prediction from GitHub commit histories. our_method uses pre-departure authority-diffusion trajectory (founder_share, n_diffused_owners in the 12-6mo pre-TFDD window); baseline uses only snapshot size/popularity covariates at TFDD (Avelino et al. style).', 'n_founder_tfdd_events_strict': 16, 'n_founder_tfdd_events_relaxed': 20, 'strict_unconditioned_survival_rate': 0.3125, 'avelino_et_al_reference_survival_rate': 0.41, 'summary_results_file': 'results/method_summary.json', 'diagnostics_file': 'results/repo_processing_diagnostics.csv'}\nn examples: 16\n\n\n=== cell 6 ===\n\n=== cell 8 ===\nanalysis dataframe: 16 strict founder-only TFDD events\n\n['                                 repo                       founder  \\\\\\n', '0  OtusGolang/webinars_practical_part      anton.telishev@yandex.ru   \\n', '1     microsoft/D3D12TranslationLayer  jenatali@ntdev.microsoft.com   \\n', '2                    mrmlnc/fast-glob         mrmlnc@yandex-team.ru   \\n', '3      BanManagement/BanManager-WebUI                      j@frd.mn   \\n', '4      cert-manag\n\n=== cell 10 ===\n\n=== cell 12 ===\n{\n  \"n_pairs\": 0,\n  \"risk_ratio_low_vs_high_diffusion\": NaN,\n  \"risk_ratio_ci95\": [\n    NaN,\n    NaN\n  ],\n  \"note\": \"risk_ratio = P(survival | low diffusion) / P(survival | high diffusion); >1 means low authority-diffusion (concentrated founder) survives MORE, <1 means diffusion helps survival\"\n}\n\n\n=== cell 14 ===\n22:16:58|WARNING|[our_method] logit failed (Singular matrix); falling back to parsimonious covariate set\n\n=== our_method ===\n{\n  \"status\": \"ok\",\n  \"n\": 16,\n  \"covariates\": [\n    \"founder_share\",\n    \"n_diffused_owners\",\n    \"log_stars\",\n    \"log_devs_at_tfdd\"\n  ],\n  \"coefs\": {\n    \"const\": -4.475696556891135,\n    \"founder_share\": -5.557883893499619,\n    \"n_diffused_owners\": -0.17424518327751867,\n    \"log_stars\": 0.483117879817099,\n    \"log_devs_at_tfdd\": 0.824365581708137\n  },\n  \"pvalues\": {\n    \"const\": 0.218303341933911,\n    \"founder_share\": 0.42564837629682595,\n    \"n_diffused_owners\": 0.33959626313122593,\n    \"log_stars\": 0.4500889951416408,\n    \"log_devs_at_tfdd\": 0.634888137249151\n  },\n  \"pvalues_bh\": {\n    \"log_devs_at_tfdd\": 0.634888137249151,\n    \"log_stars\": 0.6001186601888544,\n    \"founder_share\": 0.6001186601888544,\n    \"n_diffused_owners\": 0.6001186601888544\n  },\n  \"standardized_e\n/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/statsmodels/discrete/discrete_model.py:2385: RuntimeWarning: overflow encountered in exp\n  return 1/(1+np.exp(-X))\n/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/statsmodels/discrete/discrete_model.py:2443: RuntimeWarning: divide by zero encountered in log\n  return np.sum(np.log(self.cdf(q * linpred)))\n\n\n=== cell 16 ===\n{\n  \"n_events_with_placebo_window\": 15,\n  \"regression_placebo_window\": {\n    \"status\": \"ok\",\n    \"n\": 15,\n    \"covariates\": [\n      \"placebo_founder_share\",\n      \"placebo_n_diffused_owners\",\n      \"log_stars\",\n      \"log_forks\",\n      \"log_devs_at_tfdd\"\n    ],\n    \"coefs\": {\n      \"const\": -4.860059175074998,\n      \"placebo_founder_share\": -164.52094063102254,\n      \"placebo_n_diffused_owners\": -0.1961443232173844,\n      \"log_stars\": 3.9190820804624806,\n      \"log_forks\": -6.952094287499903,\n      \"log_devs_at_tfdd\": 5.381608652578246\n    },\n    \"pvalues\": {\n      \"const\": 0.31556585136041926,\n      \"placebo_founder_share\": 0.9999999999999999,\n      \"placebo_n_diffused_owners\": 0.3942777169865641,\n      \"log_stars\": 0.1536966384758695,\n      \"log_forks\": 0.19529751007001184,\n      \"log_de\n/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.nb_env/lib/python3.12/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals\n  warnings.warn(\"Maximum Likelihood optimization failed to \"\n\n\n=== cell 18 ===\nCohen's d: {\n  \"devs_at_tfdd\": 0.05317653025333219,\n  \"commits_at_tfdd\": -0.3705419489991742,\n  \"files_at_tfdd\": -0.7735741758295781,\n  \"founder_share_pre_departure\": -0.3875249289614023,\n  \"n_diffused_owners_pre_departure\": -0.2933139134279301\n}\n\nMann-Whitney U: {\n  \"founder_share\": {\n    \"u_stat\": 23.0,\n    \"p\": 0.6611721611721613\n  },\n  \"n_diffused_owners\": {\n    \"u_stat\": 17.5,\n    \"p\": 0.27933214039986387\n  }\n}\n\n\n=== cell 20 ===\nStrict founder-only TFDD events analyzed: 16\nUnconditioned 18-month post-TFDD survival rate: 0.312 (5/16)\nAvelino et al.'s reference survival rate:        0.41\n\nour_method pseudo-R^2:  0.17476537432367667\nbaseline   pseudo-R^2:  0.21078560979385985\n\nmatched-pairs: n_pairs=0, risk_ratio=nan", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [203] ASSISTANT · 2026-08-21 22:17:18 UTC

```
These exactly reproduce the numbers from the original `method_summary.json` (pseudo_r2 0.1748/0.2108, coefs -5.558, matched pairs 0, survival rate 0.3125). Now restore the correct GITHUB_DATA_URL and clean up.
```

### [204] TOOL CALL — Bash · 2026-08-21 22:17:18 UTC

```
cd /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty
sed -i 's#https://raw.githubusercontent.com/ai-inventor-outputs/DOES-NOT-EXIST-TEST-ONLY/mini_demo_data.json#https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json#' code_demo.ipynb
grep -c "GITHUB_DATA_URL" code_demo.ipynb
grep "ai-invention-24ffbe-pre-departure-bus-factor-diffusion" code_demo.ipynb | head -1
python3 -c "import json; json.load(open('code_demo.ipynb')); print('valid')"
rm -rf .nb_env build_nb.py
rm -f .repl_agent.ptylog
ls -la
```

### [205] TOOL RESULT — Bash · 2026-08-21 22:19:20 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bmvyij39j", "timedOutAfterMs": 120000, "backgroundCwdHint": "Session cwd remains /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty; directory changes made by the backgrounded command do not apply to subsequent commands."}
```

### [206] TOOL CALL — TaskOutput · 2026-08-21 22:20:10 UTC

```
{'task_id': 'bmvyij39j', 'block': True, 'timeout': 180000}
```

### [207] TOOL RESULT — TaskOutput · 2026-08-21 22:20:10 UTC

```
{"retrieval_status": "success", "task": {"task_id": "bmvyij39j", "task_type": "local_bash", "status": "completed", "description": "cd /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty\nsed -i 's#https://raw.githubusercontent.com/ai-inventor-outputs/DOES-NOT-EXIST-TEST-ONLY/mini_demo_data.json#https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json#' code_demo.ipynb\ngrep -c \"GITHUB_DATA_URL\" code_demo.ipynb\ngrep \"ai-invention-24ffbe-pre-departure-bus-factor-diffusion\" code_demo.ipynb | head -1\npython3 -c \"import json; json.load(open('code_demo.ipynb')); print('valid')\"\nrm -rf .nb_env build_nb.py\nrm -f .repl_agent.ptylog\nls -la", "output": "2\n    \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/experiment-1/demo/mini_demo_data.json\\\"\\n\",\nvalid\ntotal 3112\ndrwxr-xr-x 2 root root 1015682 Aug 21 22:20 .\ndrwxr-xr-x 5 root root 2009582 Aug 21 21:34 ..\n-rw-r--r-- 1 root root  139690 Aug 21 22:17 code_demo.ipynb\n-rw-r--r-- 1 root root   20897 Aug 21 21:35 mini_demo_data.json\n\n[exited with code 0]\n", "exitCode": 0}}
```

### [208] ASSISTANT · 2026-08-21 22:20:14 UTC

```
Clean workspace with just the two deliverable files, correct URL restored, and outputs preserved from the successful test run. Now write the final struct output JSON.
```

### [209] TOOL CALL — Write · 2026-08-21 22:20:14 UTC

```
File: /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.terminal_claude_agent_struct_out.json

{
  "out_expected_files": {
    "notebook": "code_demo.ipynb",
    "mini_data_file": "mini_demo_data.json"
  }
}
```

### [210] TOOL RESULT — Write · 2026-08-21 22:20:14 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_4CZ-9Ou1G5ty/.terminal_claude_agent_struct_out.json", "content": "{\n  \"out_expected_files\": {\n    \"notebook\": \"code_demo.ipynb\",\n    \"mini_data_file\": \"mini_demo_data.json\"\n  }\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [211] ASSISTANT · 2026-08-21 22:20:20 UTC

```
Done. Summary:

- **`mini_demo_data.json`**: all 16 strict founder-only TFDD events from `full_method_out.json` (this dataset only has 16 events total, so it's the complete analysis sample, not a truncation).
- **`code_demo.ipynb`**: reproduces Stages 5-8 of `method.py` (dataframe reconstruction, matched-pairs bootstrap, BH-corrected logistic regression for `our_method` vs `baseline`, placebo-window falsification check, Cohen's d / Mann-Whitney effect sizes) using the exact same functions copied verbatim from the original script, plus a results/visualization cell. Stages 0-4 (GitHub API sampling, cloning, `git log` walking) are left undemonstrated since they need live network access and ~an hour of runtime — the notebook markdown explains this explicitly.
- Test-executed end-to-end in a clean venv (with the GitHub URL temporarily pointed at a nonexistent path to force the local-fallback code path, since the real target URL currently resolves to unrelated leftover content from an earlier iteration); all 12 code cells ran without error and exactly reproduced the original pipeline's numbers (survival rate 0.3125, pseudo-R² 0.1748/0.2108, matched-pairs n=0). Correct `GITHUB_DATA_URL` restored afterward.
- `.terminal_claude_agent_struct_out.json` written per the required schema.
```
