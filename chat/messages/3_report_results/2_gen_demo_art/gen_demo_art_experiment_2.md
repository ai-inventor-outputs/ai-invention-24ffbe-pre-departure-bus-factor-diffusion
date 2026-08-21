# gen_demo_art_experiment_2 — report_results

> Phase: `gen_paper_repo` · `gen_demo_art`
> Run: `iter1_0b7b616dce39` — Scaling the Corpus, Auditing the Power, and Reconciling the Sign: What Happens When a Founder-Diffusion Survival Test Is Finally Interrogated Rather Than Just Run
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_demo_art_experiment_2` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-08-21 21:35:07 UTC

```
model: claude-sonnet-5 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl
```

### [2] SYSTEM-USER prompt · 2026-08-21 21:35:15 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/`:
GOOD: `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/file.py`, `/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/results/out.json`
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
id: art_An3IzNVz6VIl
type: experiment
title: Founder Diffusion Timing vs. Project Survival
summary: >-
  Re-runs the validated DOA/Truck-Factor/TFDD/diffusion/survival pipeline from iter1 on the same 34 founder-candidate-repo
  corpus (via the mined full_data_out.json, 70,260 commit/file rows across 121 repos), using the byte-faithful Avelino et
  al. 2016 ICPC DOA formula, greedy Truck-Factor selection, and the validated 1-year abandoner threshold to detect founder-only
  Truck-Factor Developer Departure (TFDD) events. It computes the pre-departure diffusion score (founder commit share and
  diffused-owner count in the 6-12mo pre-departure window), classifies 18-month post-TFDD survival via the Avelino Active/Inactive
  graded model collapsed to binary survived/not-survived, and runs the full statistical battery: a BH-corrected logistic regression
  with Cohen's d and bootstrap 95% CIs on snapshot covariates, matched-pairs analysis, Mann-Whitney tests, and a placebo/shuffle
  check (1000 random-window reruns) building an empirical null distribution for the diffusion coefficient. It adds the direction's
  headline new test: a Medappa-et-al.-style reconciliation model with a static whole-history write-access ratio (medappa_ratio),
  a timing_term capturing how concentrated diffusion is near departure vs. spread through history, and their interaction,
  jointly regressed against survival with a VIF collinearity check between medappa_ratio and founder_commit_share_in_window.
  Achieved n_strict=19 and n_relaxed=22 founder-only TFDD events (against iter1's 16/20 and the underpowered 40-event target),
  and the shortfall is reported explicitly rather than overclaimed, since the 34-repo candidate pool structurally caps strict
  events below 40. All outputs (corpus summary, primary regression, matched pairs, Mann-Whitney, placebo check, and the medappa/timing
  reconciliation coefficients and interpretation) are written to method_out.json validated against the exp_gen_sol_out schema,
  with a per-event raw feature/outcome table for downstream paper writing, plus a repo_processing_diagnostics.csv audit trail
  in results/.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
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

### [3] HUMAN-USER prompt · 2026-08-21 21:35:15 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [4] TOOL CALL — Skill · 2026-08-21 21:35:17 UTC

```
aii-colab
```

### [5] TOOL RESULT — Skill · 2026-08-21 21:35:17 UTC

```
{"success": true, "commandName": "aii-colab"}
```

### [6] TOOL CALL — Skill · 2026-08-21 21:35:17 UTC

```
aii-long-running-tasks
```

### [7] TOOL RESULT — Skill · 2026-08-21 21:35:17 UTC

```
{"success": true, "commandName": "aii-long-running-tasks"}
```

### [8] TOOL CALL — Bash · 2026-08-21 21:35:21 UTC

```
cd /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/gen_art/gen_art_experiment_1 && ls -la && wc -l method.py
```

### [9] TOOL RESULT — Bash · 2026-08-21 21:35:21 UTC

```
{"stdout": "total 8980\ndrwxr-xr-x 5 root root 2026439 Aug 21 19:58 .\ndrwxr-xr-x 5 root root 3000519 Aug 21 19:45 ..\n-rw-r--r-- 1 root root    2594 Aug 21 19:58 .terminal_claude_agent_struct_out.json\ndrwxr-xr-x 4 root root 2026413 Aug 21 19:50 .venv\nlrwxrwxrwx 1 root root     112 Aug 21 19:47 full_data_out.json -> /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out.json\n-rw-r--r-- 1 root root   31140 Aug 21 19:58 full_method_out.json\ndrwxr-xr-x 2 root root 1011691 Aug 21 19:53 logs\n-rw-r--r-- 1 root root   47960 Aug 21 19:55 method.py\n-rw-r--r-- 1 root root   31140 Aug 21 19:54 method_out.json\nlrwxrwxrwx 1 root root     112 Aug 21 19:47 mini_data_out.json -> /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/mini_data_out.json\n-rw-r--r-- 1 root root    5996 Aug 21 19:58 mini_method_out.json\nlrwxrwxrwx 1 root root     115 Aug 21 19:47 preview_data_out.json -> /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/preview_data_out.json\n-rw-r--r-- 1 root root    4738 Aug 21 19:58 preview_method_out.json\n-rw-r--r-- 1 root root     456 Aug 21 19:47 pyproject.toml\ndrwxr-xr-x 2 root root 1002436 Aug 21 19:54 results\n1006 method.py", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [10] TOOL CALL — Read · 2026-08-21 21:35:23 UTC

```
/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/method.py
```

### [11] TOOL RESULT — Read · 2026-08-21 21:35:24 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [12] ASSISTANT · 2026-08-21 21:35:29 UTC

```
Now let me look at the preview/mini data to understand structure.
```

### [13] TOOL CALL — Bash · 2026-08-21 21:35:29 UTC

```
cd /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/gen_art/gen_art_experiment_1 && head -c 3000 preview_data_out.json && echo "---" && python3 -c "
import json
d = json.load(open('mini_data_out.json'))
print(list(d.keys()))
print(d['datasets'][0].keys())
print(len(d['datasets'][0]['examples']))
print(json.dumps(d['datasets'][0]['examples'][0], indent=2)[:2000])
"
```

### [14] TOOL RESULT — Bash · 2026-08-21 21:35:31 UTC

```
{"stdout": "{\n  \"metadata\": {\n    \"source\": \"Local git clone (git log --numstat) over GitHub repos sampled via the GitHub REST search/repositories API across JavaScript/Python/Java/Go and 3 popularity strata (100-1k, 1k-10k, 10k+ stars); repo-le...\",\n    \"description\": \"Per-(commit,file) rows for GitHub repos passing founder-only-start filters (>=100 commits, no history-loss/squash artifact, a single author holding >=70% share of commits in the first ~50-commit / 6-m...\",\n    \"n_examples\": 70260,\n    \"n_repos\": 34\n  },\n  \"datasets\": [\n    {\n      \"dataset\": \"github_founder_departure_corpus\",\n      \"examples\": [\n        {\n          \"input\": \"{\\\"commit_index\\\": 0, \\\"n_commits_total\\\": 3796, \\\"days_since_repo_created\\\": -2233, \\\"file_path\\\": \\\"Building.txt\\\", \\\"file_ext\\\": \\\"txt\\\", \\\"lines_added\\\": 1, \\\"lines_removed\\\": 0, \\\"is_creation\\\": true, \\\"repo_stars\\\": ...\",\n          \"output\": \"founder\",\n          \"metadata_repo_id\": 46464011,\n          \"metadata_full_name\": \"ClouGence/hasor\",\n          \"metadata_license\": \"Apache-2.0\",\n          \"metadata_repo_created_at\": \"2015-11-19T03:10:00Z\",\n          \"metadata_commit_sha\": \"fc58d3c2f477cef90b7d172823a56a75a2495bdf\",\n          \"metadata_commit_timestamp\": \"2009-10-08T07:54:21+00:00\",\n          \"metadata_author_alias_key\": \"email:zyc@hasor.net\",\n          \"metadata_author_email\": \"zyc@hasor.net\",\n          \"metadata_author_name\": \"zyc\",\n          \"metadata_dominant_founder_share_first_window\": 1.0,\n          \"metadata_alias_ambiguous_repo\": false,\n          \"metadata_task_type\": \"classification\",\n          \"metadata_n_classes\": 2\n        },\n        {\n          \"input\": \"{\\\"commit_index\\\": 2, \\\"n_commits_total\\\": 3796, \\\"days_since_repo_created\\\": -2233, \\\"file_path\\\": \\\"Release branches/more_1.x/src/src/org/more/core/asm/MethodWriter.java\\\", \\\"file_ext\\\": \\\"java\\\", \\\"lines_added\\\": ...\",\n          \"output\": \"founder\",\n          \"metadata_repo_id\": 46464011,\n          \"metadata_full_name\": \"ClouGence/hasor\",\n          \"metadata_license\": \"Apache-2.0\",\n          \"metadata_repo_created_at\": \"2015-11-19T03:10:00Z\",\n          \"metadata_commit_sha\": \"dcaf92602ccef9ba976180c51bbb8d6e96e2112a\",\n          \"metadata_commit_timestamp\": \"2009-10-08T08:33:24+00:00\",\n          \"metadata_author_alias_key\": \"email:zyc@hasor.net\",\n          \"metadata_author_email\": \"zyc@hasor.net\",\n          \"metadata_author_name\": \"zyc\",\n          \"metadata_dominant_founder_share_first_window\": 1.0,\n          \"metadata_alias_ambiguous_repo\": false,\n          \"metadata_task_type\": \"classification\",\n          \"metadata_n_classes\": 2\n        },\n        {\n          \"input\": \"{\\\"commit_index\\\": 2, \\\"n_commits_total\\\": 3796, \\\"days_since_repo_created\\\": -2233, \\\"file_path\\\": \\\"Release branches/more_1.x/src/src/org/more/core/serialization/ArrayType.java\\\", \\\"file_ext\\\": \\\"java\\\", \\\"lines_a...\",\n          \"output\": \"founder\",\n          \"metadata_repo_id\": 46464011,\n          \"metadata_full_name\": \"ClouGence/hasor\",\n          \"metadata_license\": \"Apache----\n['metadata', 'datasets']\ndict_keys(['dataset', 'examples'])\n3\n{\n  \"input\": \"{\\\"commit_index\\\": 0, \\\"n_commits_total\\\": 3796, \\\"days_since_repo_created\\\": -2233, \\\"file_path\\\": \\\"Building.txt\\\", \\\"file_ext\\\": \\\"txt\\\", \\\"lines_added\\\": 1, \\\"lines_removed\\\": 0, \\\"is_creation\\\": true, \\\"repo_stars\\\": 997, \\\"repo_forks\\\": 268, \\\"repo_primary_language\\\": \\\"Java\\\"}\",\n  \"output\": \"founder\",\n  \"metadata_repo_id\": 46464011,\n  \"metadata_full_name\": \"ClouGence/hasor\",\n  \"metadata_license\": \"Apache-2.0\",\n  \"metadata_repo_created_at\": \"2015-11-19T03:10:00Z\",\n  \"metadata_commit_sha\": \"fc58d3c2f477cef90b7d172823a56a75a2495bdf\",\n  \"metadata_commit_timestamp\": \"2009-10-08T07:54:21+00:00\",\n  \"metadata_author_alias_key\": \"email:zyc@hasor.net\",\n  \"metadata_author_email\": \"zyc@hasor.net\",\n  \"metadata_author_name\": \"zyc\",\n  \"metadata_dominant_founder_share_first_window\": 1.0,\n  \"metadata_alias_ambiguous_repo\": false,\n  \"metadata_task_type\": \"classification\",\n  \"metadata_n_classes\": 2\n}", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [15] TOOL CALL — Bash · 2026-08-21 21:35:35 UTC

```
cd /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/gen_art/gen_art_experiment_1 && python3 -c "
import json
d = json.load(open('full_method_out.json'))
ex = d['datasets'][0]['examples']
print(len(ex))
for e in ex[:5]:
    print(e['metadata_repo'], e['metadata_founder'], e['metadata_tfdd_date'])
"
```

### [16] TOOL RESULT — Bash · 2026-08-21 21:35:35 UTC

```
{"stdout": "19\nJustinSDK/JavaSE6Tutorial email:caterpillar@openhome.cc 2018-12-22T05:57:22+00:00\nKrupen/AutoplayVideos email:11bit009@nirmauni.ac.in 2018-11-13T08:19:30+00:00\nPhilJay/MPAndroidChart email:phil.jahoda@gmail.com 2022-06-21T13:16:32+00:00\nTencent/Shadow email:shifujun@foxmail.com 2025-12-25T09:00:53+00:00\nTestFX/TestFX email:hastebrot@gmail.com 2017-03-29T20:43:24+00:00", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [17] TOOL CALL — Bash · 2026-08-21 21:35:39 UTC

```
cd /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/gen_art/gen_art_experiment_1 && python3 -c "
import json
from collections import Counter
d = json.load(open('full_data_out.json'))
ex = d['datasets'][0]['examples']
print(len(ex))
c = Counter(e['metadata_full_name'] for e in ex)
for name in ['JustinSDK/JavaSE6Tutorial','Krupen/AutoplayVideos','PhilJay/MPAndroidChart','TestFX/TestFX']:
    print(name, c[name])
"
```

### [18] TOOL RESULT — Bash · 2026-08-21 21:35:41 UTC

```
{"stdout": "70260\nJustinSDK/JavaSE6Tutorial 864\nKrupen/AutoplayVideos 349\nPhilJay/MPAndroidChart 3038\nTestFX/TestFX 2996", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [19] ASSISTANT · 2026-08-21 21:35:45 UTC

```
Good — JustinSDK/JavaSE6Tutorial (864 rows) and Krupen/AutoplayVideos (349 rows) are small and both produce TFDD events. Let's build the mini dataset from these two plus maybe one non-event repo for diversity.
```

### [20] TOOL CALL — Bash · 2026-08-21 21:35:45 UTC

```
mkdir -p /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl
cd /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/3_invention_loop/iter_2/gen_art/gen_art_experiment_1 && python3 -c "
import json
d = json.load(open('full_data_out.json'))
ex = d['datasets'][0]['examples']
keep = {'JustinSDK/JavaSE6Tutorial','Krupen/AutoplayVideos'}
sub = [e for e in ex if e['metadata_full_name'] in keep]
print(len(sub))
out = {'metadata': d['metadata'], 'datasets':[{'dataset': d['datasets'][0]['dataset'], 'examples': sub}]}
outpath='/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/mini_demo_data.json'
json.dump(out, open(outpath,'w'))
import os
print(os.path.getsize(outpath)/1024,'KB')
"
```

### [21] TOOL RESULT — Bash · 2026-08-21 21:35:47 UTC

```
{"stdout": "1213\n1114.548828125 KB", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [22] ASSISTANT · 2026-08-21 21:35:49 UTC

```
1.1MB is fine for a mini dataset. Now let's build the notebook.
```

### [23] TOOL CALL — ToolSearch · 2026-08-21 21:35:49 UTC

```
{'query': 'NotebookEdit', 'max_results': 3}
```

### [24] TOOL RESULT — ToolSearch · 2026-08-21 21:35:49 UTC

```
{"matches": ["NotebookEdit"], "query": "NotebookEdit", "total_deferred_tools": 22}
```

### [25] TOOL CALL — Write · 2026-08-21 21:35:54 UTC

```
File: /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb

{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["# placeholder"]
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

### [26] TOOL RESULT — Write · 2026-08-21 21:35:54 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb", "content": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": [\"# placeholder\"]\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"},\n  \"language_info\": {\"name\": \"python\", \"version\": \"3.12.0\"}\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [27] TOOL CALL — Read · 2026-08-21 21:35:56 UTC

```
/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb
```

### [28] TOOL RESULT — Read · 2026-08-21 21:35:56 UTC

```
{"type": "notebook", "file": {"filePath": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb", "cells": [{"cellType": "markdown", "source": "# placeholder", "cell_id": "cell-0"}]}}
```

### [29] ASSISTANT · 2026-08-21 21:36:06 UTC

```
Now let's build out the notebook cell by cell.
```

### [30] TOOL CALL — NotebookEdit · 2026-08-21 21:36:06 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': 'cell-0', 'cell_type': 'markdown', 'new_source': '# Founder Diffusion Timing vs. Project Survival\\n\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file\'s primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\n\\nIt also runs the iteration\'s new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\n\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end."]'}
```

### [31] TOOL RESULT — NotebookEdit · 2026-08-21 21:36:06 UTC

```
{"new_source": "# Founder Diffusion Timing vs. Project Survival\\n\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\n\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\n\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\"]", "old_source": "# placeholder", "cell_type": "markdown", "language": "python", "edit_mode": "replace", "cell_id": "cell-0", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": [\"# placeholder\"]\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"},\n  \"language_info\": {\"name\": \"python\", \"version\": \"3.12.0\"}\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}\n", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\\\"]\"\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [32] TOOL CALL — NotebookEdit · 2026-08-21 21:36:12 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': 'cell-0', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': "import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# statsmodels -- NOT pre-installed on Colab, always install\\n_pip('statsmodels==0.14.6')\\n\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')"}
```

### [33] TOOL RESULT — NotebookEdit · 2026-08-21 21:36:12 UTC

```
{"new_source": "import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# statsmodels -- NOT pre-installed on Colab, always install\\n_pip('statsmodels==0.14.6')\\n\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "b0d42898", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\\\"]\"\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\\\"]\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [34] TOOL CALL — Read · 2026-08-21 21:36:16 UTC

```
/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb
```

### [35] TOOL RESULT — Read · 2026-08-21 21:36:16 UTC

```
{"type": "notebook", "file": {"filePath": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb", "cells": [{"cellType": "markdown", "source": "# Founder Diffusion Timing vs. Project Survival\\n\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\n\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\n\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\"]", "cell_id": "cell-0"}, {"cellType": "code", "source": "import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# statsmodels -- NOT pre-installed on Colab, always install\\n_pip('statsmodels==0.14.6')\\n\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')", "cell_id": "b0d42898", "language": "python"}]}}
```

### [36] ASSISTANT · 2026-08-21 21:36:20 UTC

```
Let's fix the install cell to also cover loguru (non-colab always) and skip psutil/multiprocessing complexity in the notebook (single-process, minimal edit).
```

### [37] TOOL CALL — NotebookEdit · 2026-08-21 21:36:20 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': 'b0d42898', 'new_source': "import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\n_pip('statsmodels==0.14.6')\\n_pip('loguru==0.7.2')\\n\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')"}
```

### [38] TOOL RESULT — NotebookEdit · 2026-08-21 21:36:20 UTC

```
{"new_source": "import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\n_pip('statsmodels==0.14.6')\\n_pip('loguru==0.7.2')\\n\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')", "old_source": "import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# statsmodels -- NOT pre-installed on Colab, always install\\n_pip('statsmodels==0.14.6')\\n\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')", "cell_type": "code", "language": "python", "edit_mode": "replace", "cell_id": "b0d42898", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\\\"]\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\\\"]\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n_pip('loguru==0.7.2')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [39] ASSISTANT · 2026-08-21 21:36:26 UTC

```
Now imports cell.
```

### [40] TOOL CALL — NotebookEdit · 2026-08-21 21:36:26 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': 'b0d42898', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': 'from __future__ import annotations\\n\\nimport gc\\nimport json\\nimport math\\nimport random\\nimport sys\\nimport time\\nfrom collections import Counter, defaultdict\\nfrom dataclasses import asdict, dataclass\\nfrom datetime import datetime, timedelta, timezone\\nfrom pathlib import Path\\nfrom typing import Optional\\n\\nimport numpy as np\\nimport pandas as pd\\nimport statsmodels.api as sm\\nfrom loguru import logger\\nfrom scipy import stats\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\n\\n# added for the notebook\'s results visualization cell\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\"INFO\\", format=\\"{time:HH:mm:ss}|{level:<7}|{message}\\")\\n\\nRNG_SEED = 20260821\\nrandom.seed(RNG_SEED)\\nnp.random.seed(RNG_SEED)'}
```

### [41] TOOL RESULT — NotebookEdit · 2026-08-21 21:36:26 UTC

```
{"new_source": "from __future__ import annotations\\n\\nimport gc\\nimport json\\nimport math\\nimport random\\nimport sys\\nimport time\\nfrom collections import Counter, defaultdict\\nfrom dataclasses import asdict, dataclass\\nfrom datetime import datetime, timedelta, timezone\\nfrom pathlib import Path\\nfrom typing import Optional\\n\\nimport numpy as np\\nimport pandas as pd\\nimport statsmodels.api as sm\\nfrom loguru import logger\\nfrom scipy import stats\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\n\\n# added for the notebook's results visualization cell\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\\n\\nRNG_SEED = 20260821\\nrandom.seed(RNG_SEED)\\nnp.random.seed(RNG_SEED)", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "96e95ae7", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\\\"]\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n_pip('loguru==0.7.2')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\\\"]\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n_pip('loguru==0.7.2')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"96e95ae7\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\\\n\\\\n# added for the notebook's results visualization cell\\\\nimport matplotlib.pyplot as plt\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [42] ASSISTANT · 2026-08-21 21:36:32 UTC

```
Now data loading markdown + cells.
```

### [43] TOOL CALL — NotebookEdit · 2026-08-21 21:36:32 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '96e95ae7', 'edit_mode': 'insert', 'cell_type': 'markdown', 'new_source': '## Load the demo data\\n\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now)."]'}
```

### [44] TOOL RESULT — NotebookEdit · 2026-08-21 21:36:32 UTC

```
{"new_source": "## Load the demo data\\n\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now).\"]", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "bb7b7f61", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\\\"]\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n_pip('loguru==0.7.2')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"96e95ae7\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\\\n\\\\n# added for the notebook's results visualization cell\\\\nimport matplotlib.pyplot as plt\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\\\"]\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n_pip('loguru==0.7.2')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"96e95ae7\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\\\n\\\\n# added for the notebook's results visualization cell\\\\nimport matplotlib.pyplot as plt\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"bb7b7f61\",\n   \"source\": \"## Load the demo data\\\\n\\\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\\\n\\\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now).\\\"]\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [45] TOOL CALL — NotebookEdit · 2026-08-21 21:36:36 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': 'bb7b7f61', 'new_source': '## Load the demo data\\n\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now).'}
```

### [46] TOOL RESULT — NotebookEdit · 2026-08-21 21:36:36 UTC

```
{"new_source": "## Load the demo data\\n\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now).", "old_source": "## Load the demo data\\n\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now).\"]", "cell_type": "code", "language": "python", "edit_mode": "replace", "cell_id": "bb7b7f61", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\\\"]\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n_pip('loguru==0.7.2')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"96e95ae7\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\\\n\\\\n# added for the notebook's results visualization cell\\\\nimport matplotlib.pyplot as plt\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"bb7b7f61\",\n   \"source\": \"## Load the demo data\\\\n\\\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\\\n\\\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now).\\\"]\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\\\"]\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n_pip('loguru==0.7.2')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"96e95ae7\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\\\n\\\\n# added for the notebook's results visualization cell\\\\nimport matplotlib.pyplot as plt\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"bb7b7f61\",\n   \"source\": \"## Load the demo data\\\\n\\\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\\\n\\\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now).\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [47] ASSISTANT · 2026-08-21 21:36:38 UTC

```
Also need to check the earlier cell for the same stray trailing bracket issue.
```

### [48] TOOL CALL — Read · 2026-08-21 21:36:38 UTC

```
/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb
```

### [49] TOOL RESULT — Read · 2026-08-21 21:36:38 UTC

```
{"type": "notebook", "file": {"filePath": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb", "cells": [{"cellType": "markdown", "source": "# Founder Diffusion Timing vs. Project Survival\\n\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\n\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\n\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\"]", "cell_id": "cell-0"}, {"cellType": "code", "source": "import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\n_pip('statsmodels==0.14.6')\\n_pip('loguru==0.7.2')\\n\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')", "cell_id": "b0d42898", "language": "python"}, {"cellType": "code", "source": "from __future__ import annotations\\n\\nimport gc\\nimport json\\nimport math\\nimport random\\nimport sys\\nimport time\\nfrom collections import Counter, defaultdict\\nfrom dataclasses import asdict, dataclass\\nfrom datetime import datetime, timedelta, timezone\\nfrom pathlib import Path\\nfrom typing import Optional\\n\\nimport numpy as np\\nimport pandas as pd\\nimport statsmodels.api as sm\\nfrom loguru import logger\\nfrom scipy import stats\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\n\\n# added for the notebook's results visualization cell\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\\n\\nRNG_SEED = 20260821\\nrandom.seed(RNG_SEED)\\nnp.random.seed(RNG_SEED)", "cell_id": "96e95ae7", "language": "python"}, {"cellType": "markdown", "source": "## Load the demo data\\n\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now).", "cell_id": "bb7b7f61"}]}}
```

### [50] ASSISTANT · 2026-08-21 21:36:48 UTC

```
Cell-0 still has trailing `"]`. Let me fix it.
```

### [51] TOOL CALL — NotebookEdit · 2026-08-21 21:36:48 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': 'cell-0', 'new_source': "# Founder Diffusion Timing vs. Project Survival\\n\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\n\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\n\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end."}
```

### [52] TOOL RESULT — NotebookEdit · 2026-08-21 21:36:48 UTC

```
{"new_source": "# Founder Diffusion Timing vs. Project Survival\\n\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\n\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\n\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.", "old_source": "# Founder Diffusion Timing vs. Project Survival\\n\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\n\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\n\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\"]", "cell_type": "code", "language": "python", "edit_mode": "replace", "cell_id": "cell-0", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\\\"]\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n_pip('loguru==0.7.2')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"96e95ae7\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\\\n\\\\n# added for the notebook's results visualization cell\\\\nimport matplotlib.pyplot as plt\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"bb7b7f61\",\n   \"source\": \"## Load the demo data\\\\n\\\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\\\n\\\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now).\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n_pip('loguru==0.7.2')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"96e95ae7\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\\\n\\\\n# added for the notebook's results visualization cell\\\\nimport matplotlib.pyplot as plt\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"bb7b7f61\",\n   \"source\": \"## Load the demo data\\\\n\\\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\\\n\\\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now).\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [53] ASSISTANT · 2026-08-21 21:36:54 UTC

```
Now data loading code cells.
```

### [54] TOOL CALL — NotebookEdit · 2026-08-21 21:36:54 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': 'bb7b7f61', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': 'GITHUB_DATA_URL = \\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\"mini_demo_data.json\\"):\\n        with open(\\"mini_demo_data.json\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\"Could not load mini_demo_data.json\\")'}
```

### [55] TOOL RESULT — NotebookEdit · 2026-08-21 21:36:54 UTC

```
{"new_source": "GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "07e078ee", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n_pip('loguru==0.7.2')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"96e95ae7\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\\\n\\\\n# added for the notebook's results visualization cell\\\\nimport matplotlib.pyplot as plt\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"bb7b7f61\",\n   \"source\": \"## Load the demo data\\\\n\\\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\\\n\\\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now).\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n_pip('loguru==0.7.2')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"96e95ae7\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\\\n\\\\n# added for the notebook's results visualization cell\\\\nimport matplotlib.pyplot as plt\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"bb7b7f61\",\n   \"source\": \"## Load the demo data\\\\n\\\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\\\n\\\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"07e078ee\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [56] TOOL CALL — NotebookEdit · 2026-08-21 21:36:58 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '07e078ee', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': 'data = load_data()\\nprint(data[\\"metadata\\"])\\nprint(\\"n_examples in demo:\\", len(data[\\"datasets\\"][0][\\"examples\\"]))'}
```

### [57] TOOL RESULT — NotebookEdit · 2026-08-21 21:36:58 UTC

```
{"new_source": "data = load_data()\\nprint(data[\\\"metadata\\\"])\\nprint(\\\"n_examples in demo:\\\", len(data[\\\"datasets\\\"][0][\\\"examples\\\"]))", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "12ed4615", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n_pip('loguru==0.7.2')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"96e95ae7\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\\\n\\\\n# added for the notebook's results visualization cell\\\\nimport matplotlib.pyplot as plt\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"bb7b7f61\",\n   \"source\": \"## Load the demo data\\\\n\\\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\\\n\\\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"07e078ee\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n_pip('loguru==0.7.2')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"96e95ae7\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\\\n\\\\n# added for the notebook's results visualization cell\\\\nimport matplotlib.pyplot as plt\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"bb7b7f61\",\n   \"source\": \"## Load the demo data\\\\n\\\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\\\n\\\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"07e078ee\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"12ed4615\",\n   \"source\": \"data = load_data()\\\\nprint(data[\\\\\\\"metadata\\\\\\\"])\\\\nprint(\\\\\\\"n_examples in demo:\\\\\\\", len(data[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [58] ASSISTANT · 2026-08-21 21:37:02 UTC

```
Now the config cell.
```

### [59] TOOL CALL — NotebookEdit · 2026-08-21 21:37:02 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '12ed4615', 'edit_mode': 'insert', 'cell_type': 'markdown', 'new_source': '## Config\\n\\nAll tunable parameters from the original `method.py`, collected here. `N_BOOT` (bootstrap resamples) and the placebo-check resample count are the two knobs that dominate runtime, so they are set to small-but-nonzero values for this demo (the original values, used for the full 34-repo run, are commented alongside). Everything else (thresholds, window sizes) is reused **unchanged** from the validated iter1 pipeline, per the docstring\'s \\"do not re-tune\\" note.'}
```

### [60] TOOL RESULT — NotebookEdit · 2026-08-21 21:37:02 UTC

```
{"new_source": "## Config\\n\\nAll tunable parameters from the original `method.py`, collected here. `N_BOOT` (bootstrap resamples) and the placebo-check resample count are the two knobs that dominate runtime, so they are set to small-but-nonzero values for this demo (the original values, used for the full 34-repo run, are commented alongside). Everything else (thresholds, window sizes) is reused **unchanged** from the validated iter1 pipeline, per the docstring's \\\"do not re-tune\\\" note.", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "4b221478", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n_pip('loguru==0.7.2')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"96e95ae7\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\\\n\\\\n# added for the notebook's results visualization cell\\\\nimport matplotlib.pyplot as plt\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"bb7b7f61\",\n   \"source\": \"## Load the demo data\\\\n\\\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\\\n\\\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"07e078ee\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"12ed4615\",\n   \"source\": \"data = load_data()\\\\nprint(data[\\\\\\\"metadata\\\\\\\"])\\\\nprint(\\\\\\\"n_examples in demo:\\\\\\\", len(data[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n_pip('loguru==0.7.2')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"96e95ae7\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\\\n\\\\n# added for the notebook's results visualization cell\\\\nimport matplotlib.pyplot as plt\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"bb7b7f61\",\n   \"source\": \"## Load the demo data\\\\n\\\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\\\n\\\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"07e078ee\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"12ed4615\",\n   \"source\": \"data = load_data()\\\\nprint(data[\\\\\\\"metadata\\\\\\\"])\\\\nprint(\\\\\\\"n_examples in demo:\\\\\\\", len(data[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"4b221478\",\n   \"source\": \"## Config\\\\n\\\\nAll tunable parameters from the original `method.py`, collected here. `N_BOOT` (bootstrap resamples) and the placebo-check resample count are the two knobs that dominate runtime, so they are set to small-but-nonzero values for this demo (the original values, used for the full 34-repo run, are commented alongside). Everything else (thresholds, window sizes) is reused **unchanged** from the validated iter1 pipeline, per the docstring's \\\\\\\"do not re-tune\\\\\\\" note.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [61] TOOL CALL — NotebookEdit · 2026-08-21 21:37:08 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '4b221478', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': '# --- constants reused verbatim from iter1 (do not re-tune) ---\\nSILENCE_THRESHOLD_DAYS = 365\\nTF_COVERAGE_THRESHOLD = 0.5\\nPOST_TFDD_WINDOW_DAYS = 548  # 18 months\\nPRE_WINDOW_FAR_DAYS = 365  # 12 months before TFDD\\nPRE_WINDOW_NEAR_DAYS = 180  # 6 months before TFDD\\nSNAPSHOT_EVERY_DAYS = 90\\nSTRICT_FOUNDER_SHARE = 0.70  # re-verification threshold for founder-only strict criterion\\nRELAXED_FOUNDER_SHARE = 0.50\\nTARGET_N_STRICT = 40  # iter1 power-analysis target; 34-repo pool structurally caps below this\\n\\nAVELINO_REFERENCE_SURVIVAL_RATE = 0.41\\n\\n# --- runtime-dominating knobs: minimized for this small demo ---\\nN_BOOT = 200  # original: 5000 (bootstrap CI resamples for matched-pairs / mean-diff CIs)\\nN_PLACEBO_BOOT = 50  # original: 1000 (placebo-window empirical-null resamples)'}
```

### [62] TOOL RESULT — NotebookEdit · 2026-08-21 21:37:08 UTC

```
{"new_source": "# --- constants reused verbatim from iter1 (do not re-tune) ---\\nSILENCE_THRESHOLD_DAYS = 365\\nTF_COVERAGE_THRESHOLD = 0.5\\nPOST_TFDD_WINDOW_DAYS = 548  # 18 months\\nPRE_WINDOW_FAR_DAYS = 365  # 12 months before TFDD\\nPRE_WINDOW_NEAR_DAYS = 180  # 6 months before TFDD\\nSNAPSHOT_EVERY_DAYS = 90\\nSTRICT_FOUNDER_SHARE = 0.70  # re-verification threshold for founder-only strict criterion\\nRELAXED_FOUNDER_SHARE = 0.50\\nTARGET_N_STRICT = 40  # iter1 power-analysis target; 34-repo pool structurally caps below this\\n\\nAVELINO_REFERENCE_SURVIVAL_RATE = 0.41\\n\\n# --- runtime-dominating knobs: minimized for this small demo ---\\nN_BOOT = 200  # original: 5000 (bootstrap CI resamples for matched-pairs / mean-diff CIs)\\nN_PLACEBO_BOOT = 50  # original: 1000 (placebo-window empirical-null resamples)", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "3e8cb93d", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n_pip('loguru==0.7.2')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"96e95ae7\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\\\n\\\\n# added for the notebook's results visualization cell\\\\nimport matplotlib.pyplot as plt\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"bb7b7f61\",\n   \"source\": \"## Load the demo data\\\\n\\\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\\\n\\\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"07e078ee\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"12ed4615\",\n   \"source\": \"data = load_data()\\\\nprint(data[\\\\\\\"metadata\\\\\\\"])\\\\nprint(\\\\\\\"n_examples in demo:\\\\\\\", len(data[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"4b221478\",\n   \"source\": \"## Config\\\\n\\\\nAll tunable parameters from the original `method.py`, collected here. `N_BOOT` (bootstrap resamples) and the placebo-check resample count are the two knobs that dominate runtime, so they are set to small-but-nonzero values for this demo (the original values, used for the full 34-repo run, are commented alongside). Everything else (thresholds, window sizes) is reused **unchanged** from the validated iter1 pipeline, per the docstring's \\\\\\\"do not re-tune\\\\\\\" note.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n_pip('loguru==0.7.2')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"96e95ae7\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\\\n\\\\n# added for the notebook's results visualization cell\\\\nimport matplotlib.pyplot as plt\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"bb7b7f61\",\n   \"source\": \"## Load the demo data\\\\n\\\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\\\n\\\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"07e078ee\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"12ed4615\",\n   \"source\": \"data = load_data()\\\\nprint(data[\\\\\\\"metadata\\\\\\\"])\\\\nprint(\\\\\\\"n_examples in demo:\\\\\\\", len(data[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"4b221478\",\n   \"source\": \"## Config\\\\n\\\\nAll tunable parameters from the original `method.py`, collected here. `N_BOOT` (bootstrap resamples) and the placebo-check resample count are the two knobs that dominate runtime, so they are set to small-but-nonzero values for this demo (the original values, used for the full 34-repo run, are commented alongside). Everything else (thresholds, window sizes) is reused **unchanged** from the validated iter1 pipeline, per the docstring's \\\\\\\"do not re-tune\\\\\\\" note.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"3e8cb93d\",\n   \"source\": \"# --- constants reused verbatim from iter1 (do not re-tune) ---\\\\nSILENCE_THRESHOLD_DAYS = 365\\\\nTF_COVERAGE_THRESHOLD = 0.5\\\\nPOST_TFDD_WINDOW_DAYS = 548  # 18 months\\\\nPRE_WINDOW_FAR_DAYS = 365  # 12 months before TFDD\\\\nPRE_WINDOW_NEAR_DAYS = 180  # 6 months before TFDD\\\\nSNAPSHOT_EVERY_DAYS = 90\\\\nSTRICT_FOUNDER_SHARE = 0.70  # re-verification threshold for founder-only strict criterion\\\\nRELAXED_FOUNDER_SHARE = 0.50\\\\nTARGET_N_STRICT = 40  # iter1 power-analysis target; 34-repo pool structurally caps below this\\\\n\\\\nAVELINO_REFERENCE_SURVIVAL_RATE = 0.41\\\\n\\\\n# --- runtime-dominating knobs: minimized for this small demo ---\\\\nN_BOOT = 200  # original: 5000 (bootstrap CI resamples for matched-pairs / mean-diff CIs)\\\\nN_PLACEBO_BOOT = 50  # original: 1000 (placebo-window empirical-null resamples)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [63] TOOL CALL — NotebookEdit · 2026-08-21 21:37:18 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '3e8cb93d', 'edit_mode': 'insert', 'cell_type': 'markdown', 'new_source': '## Step 0: reconstruct per-repo commit streams\\n\\nThe mined `full_data_out.json` (here, its `mini_demo_data.json` subset) stores one row per `(commit, file)` pair. This step groups rows back into per-repo, per-commit lists sorted by date — the same shape `git log --numstat` would have produced if the pipeline had cloned these repos live, but read from the already-mined dataset instead.'}
```

### [64] TOOL RESULT — NotebookEdit · 2026-08-21 21:37:18 UTC

```
{"new_source": "## Step 0: reconstruct per-repo commit streams\\n\\nThe mined `full_data_out.json` (here, its `mini_demo_data.json` subset) stores one row per `(commit, file)` pair. This step groups rows back into per-repo, per-commit lists sorted by date — the same shape `git log --numstat` would have produced if the pipeline had cloned these repos live, but read from the already-mined dataset instead.", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "9da1f4fc", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n_pip('loguru==0.7.2')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"96e95ae7\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\\\n\\\\n# added for the notebook's results visualization cell\\\\nimport matplotlib.pyplot as plt\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"bb7b7f61\",\n   \"source\": \"## Load the demo data\\\\n\\\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\\\n\\\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"07e078ee\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"12ed4615\",\n   \"source\": \"data = load_data()\\\\nprint(data[\\\\\\\"metadata\\\\\\\"])\\\\nprint(\\\\\\\"n_examples in demo:\\\\\\\", len(data[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"4b221478\",\n   \"source\": \"## Config\\\\n\\\\nAll tunable parameters from the original `method.py`, collected here. `N_BOOT` (bootstrap resamples) and the placebo-check resample count are the two knobs that dominate runtime, so they are set to small-but-nonzero values for this demo (the original values, used for the full 34-repo run, are commented alongside). Everything else (thresholds, window sizes) is reused **unchanged** from the validated iter1 pipeline, per the docstring's \\\\\\\"do not re-tune\\\\\\\" note.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"3e8cb93d\",\n   \"source\": \"# --- constants reused verbatim from iter1 (do not re-tune) ---\\\\nSILENCE_THRESHOLD_DAYS = 365\\\\nTF_COVERAGE_THRESHOLD = 0.5\\\\nPOST_TFDD_WINDOW_DAYS = 548  # 18 months\\\\nPRE_WINDOW_FAR_DAYS = 365  # 12 months before TFDD\\\\nPRE_WINDOW_NEAR_DAYS = 180  # 6 months before TFDD\\\\nSNAPSHOT_EVERY_DAYS = 90\\\\nSTRICT_FOUNDER_SHARE = 0.70  # re-verification threshold for founder-only strict criterion\\\\nRELAXED_FOUNDER_SHARE = 0.50\\\\nTARGET_N_STRICT = 40  # iter1 power-analysis target; 34-repo pool structurally caps below this\\\\n\\\\nAVELINO_REFERENCE_SURVIVAL_RATE = 0.41\\\\n\\\\n# --- runtime-dominating knobs: minimized for this small demo ---\\\\nN_BOOT = 200  # original: 5000 (bootstrap CI resamples for matched-pairs / mean-diff CIs)\\\\nN_PLACEBO_BOOT = 50  # original: 1000 (placebo-window empirical-null resamples)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n_pip('loguru==0.7.2')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"96e95ae7\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\\\n\\\\n# added for the notebook's results visualization cell\\\\nimport matplotlib.pyplot as plt\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"bb7b7f61\",\n   \"source\": \"## Load the demo data\\\\n\\\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\\\n\\\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"07e078ee\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"12ed4615\",\n   \"source\": \"data = load_data()\\\\nprint(data[\\\\\\\"metadata\\\\\\\"])\\\\nprint(\\\\\\\"n_examples in demo:\\\\\\\", len(data[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"4b221478\",\n   \"source\": \"## Config\\\\n\\\\nAll tunable parameters from the original `method.py`, collected here. `N_BOOT` (bootstrap resamples) and the placebo-check resample count are the two knobs that dominate runtime, so they are set to small-but-nonzero values for this demo (the original values, used for the full 34-repo run, are commented alongside). Everything else (thresholds, window sizes) is reused **unchanged** from the validated iter1 pipeline, per the docstring's \\\\\\\"do not re-tune\\\\\\\" note.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"3e8cb93d\",\n   \"source\": \"# --- constants reused verbatim from iter1 (do not re-tune) ---\\\\nSILENCE_THRESHOLD_DAYS = 365\\\\nTF_COVERAGE_THRESHOLD = 0.5\\\\nPOST_TFDD_WINDOW_DAYS = 548  # 18 months\\\\nPRE_WINDOW_FAR_DAYS = 365  # 12 months before TFDD\\\\nPRE_WINDOW_NEAR_DAYS = 180  # 6 months before TFDD\\\\nSNAPSHOT_EVERY_DAYS = 90\\\\nSTRICT_FOUNDER_SHARE = 0.70  # re-verification threshold for founder-only strict criterion\\\\nRELAXED_FOUNDER_SHARE = 0.50\\\\nTARGET_N_STRICT = 40  # iter1 power-analysis target; 34-repo pool structurally caps below this\\\\n\\\\nAVELINO_REFERENCE_SURVIVAL_RATE = 0.41\\\\n\\\\n# --- runtime-dominating knobs: minimized for this small demo ---\\\\nN_BOOT = 200  # original: 5000 (bootstrap CI resamples for matched-pairs / mean-diff CIs)\\\\nN_PLACEBO_BOOT = 50  # original: 1000 (placebo-window empirical-null resamples)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"9da1f4fc\",\n   \"source\": \"## Step 0: reconstruct per-repo commit streams\\\\n\\\\nThe mined `full_data_out.json` (here, its `mini_demo_data.json` subset) stores one row per `(commit, file)` pair. This step groups rows back into per-repo, per-commit lists sorted by date — the same shape `git log --numstat` would have produced if the pipeline had cloned these repos live, but read from the already-mined dataset instead.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [65] TOOL CALL — NotebookEdit · 2026-08-21 21:37:26 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '9da1f4fc', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': 'def load_repo_commit_streams(raw: dict) -> dict[str, dict]:\\n    examples = raw[\\"datasets\\"][0][\\"examples\\"]\\n    logger.info(f\\"[step0] loaded {len(examples)} (commit,file) rows\\")\\n\\n    repos: dict[str, dict] = {}\\n    for row in examples:\\n        rid = str(row[\\"metadata_repo_id\\"])\\n        rep = repos.setdefault(\\n            rid,\\n            {\\n                \\"full_name\\": row[\\"metadata_full_name\\"],\\n                \\"license_key\\": row.get(\\"metadata_license\\") or \\"none\\",\\n                \\"created_at\\": datetime.fromisoformat(row[\\"metadata_repo_created_at\\"].replace(\\"Z\\", \\"+00:00\\")),\\n                \\"stars\\": None,\\n                \\"forks\\": None,\\n                \\"language\\": None,\\n                \\"commits_by_sha\\": {},\\n                \\"dominant_founder_first_window_share\\": row.get(\\"metadata_dominant_founder_share_first_window\\"),\\n                \\"alias_ambiguous\\": row.get(\\"metadata_alias_ambiguous_repo\\"),\\n            },\\n        )\\n        try:\\n            inp = json.loads(row[\\"input\\"])\\n        except (json.JSONDecodeError, TypeError):\\n            inp = {}\\n        if rep[\\"stars\\"] is None:\\n            rep[\\"stars\\"] = inp.get(\\"repo_stars\\", 0)\\n            rep[\\"forks\\"] = inp.get(\\"repo_forks\\", 0)\\n            rep[\\"language\\"] = inp.get(\\"repo_primary_language\\", \\"unknown\\")\\n        sha = row[\\"metadata_commit_sha\\"]\\n        c = rep[\\"commits_by_sha\\"].get(sha)\\n        if c is None:\\n            try:\\n                dt = datetime.fromisoformat(row[\\"metadata_commit_timestamp\\"])\\n            except ValueError:\\n                continue\\n            c = {\\"hash\\": sha, \\"author_email\\": row[\\"metadata_author_alias_key\\"], \\"date\\": dt, \\"files\\": []}\\n            rep[\\"commits_by_sha\\"][sha] = c\\n        added = inp.get(\\"lines_added\\", 0) or 0\\n        removed = inp.get(\\"lines_removed\\", 0) or 0\\n        c[\\"files\\"].append((inp.get(\\"file_path\\", \\"?\\"), added, removed))\\n\\n    for rep in repos.values():\\n        commits = sorted(rep[\\"commits_by_sha\\"].values(), key=lambda c: c[\\"date\\"])\\n        rep[\\"commits\\"] = commits\\n        del rep[\\"commits_by_sha\\"]\\n    logger.info(f\\"[step0] grouped into {len(repos)} repos\\")\\n    return repos\\n\\n\\nrepos = load_repo_commit_streams(data)\\nn_repo_candidates = len(repos)\\nfor rid, rep in repos.items():\\n    print(rep[\\"full_name\\"], \\"-\\", len(rep[\\"commits\\"]), \\"commits\\")'}
```

### [66] TOOL RESULT — NotebookEdit · 2026-08-21 21:37:26 UTC

```
{"new_source": "def load_repo_commit_streams(raw: dict) -> dict[str, dict]:\\n    examples = raw[\\\"datasets\\\"][0][\\\"examples\\\"]\\n    logger.info(f\\\"[step0] loaded {len(examples)} (commit,file) rows\\\")\\n\\n    repos: dict[str, dict] = {}\\n    for row in examples:\\n        rid = str(row[\\\"metadata_repo_id\\\"])\\n        rep = repos.setdefault(\\n            rid,\\n            {\\n                \\\"full_name\\\": row[\\\"metadata_full_name\\\"],\\n                \\\"license_key\\\": row.get(\\\"metadata_license\\\") or \\\"none\\\",\\n                \\\"created_at\\\": datetime.fromisoformat(row[\\\"metadata_repo_created_at\\\"].replace(\\\"Z\\\", \\\"+00:00\\\")),\\n                \\\"stars\\\": None,\\n                \\\"forks\\\": None,\\n                \\\"language\\\": None,\\n                \\\"commits_by_sha\\\": {},\\n                \\\"dominant_founder_first_window_share\\\": row.get(\\\"metadata_dominant_founder_share_first_window\\\"),\\n                \\\"alias_ambiguous\\\": row.get(\\\"metadata_alias_ambiguous_repo\\\"),\\n            },\\n        )\\n        try:\\n            inp = json.loads(row[\\\"input\\\"])\\n        except (json.JSONDecodeError, TypeError):\\n            inp = {}\\n        if rep[\\\"stars\\\"] is None:\\n            rep[\\\"stars\\\"] = inp.get(\\\"repo_stars\\\", 0)\\n            rep[\\\"forks\\\"] = inp.get(\\\"repo_forks\\\", 0)\\n            rep[\\\"language\\\"] = inp.get(\\\"repo_primary_language\\\", \\\"unknown\\\")\\n        sha = row[\\\"metadata_commit_sha\\\"]\\n        c = rep[\\\"commits_by_sha\\\"].get(sha)\\n        if c is None:\\n            try:\\n                dt = datetime.fromisoformat(row[\\\"metadata_commit_timestamp\\\"])\\n            except ValueError:\\n                continue\\n            c = {\\\"hash\\\": sha, \\\"author_email\\\": row[\\\"metadata_author_alias_key\\\"], \\\"date\\\": dt, \\\"files\\\": []}\\n            rep[\\\"commits_by_sha\\\"][sha] = c\\n        added = inp.get(\\\"lines_added\\\", 0) or 0\\n        removed = inp.get(\\\"lines_removed\\\", 0) or 0\\n        c[\\\"files\\\"].append((inp.get(\\\"file_path\\\", \\\"?\\\"), added, removed))\\n\\n    for rep in repos.values():\\n        commits = sorted(rep[\\\"commits_by_sha\\\"].values(), key=lambda c: c[\\\"date\\\"])\\n        rep[\\\"commits\\\"] = commits\\n        del rep[\\\"commits_by_sha\\\"]\\n    logger.info(f\\\"[step0] grouped into {len(repos)} repos\\\")\\n    return repos\\n\\n\\nrepos = load_repo_commit_streams(data)\\nn_repo_candidates = len(repos)\\nfor rid, rep in repos.items():\\n    print(rep[\\\"full_name\\\"], \\\"-\\\", len(rep[\\\"commits\\\"]), \\\"commits\\\")", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "17e949b6", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n_pip('loguru==0.7.2')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"96e95ae7\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\\\n\\\\n# added for the notebook's results visualization cell\\\\nimport matplotlib.pyplot as plt\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"bb7b7f61\",\n   \"source\": \"## Load the demo data\\\\n\\\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\\\n\\\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"07e078ee\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"12ed4615\",\n   \"source\": \"data = load_data()\\\\nprint(data[\\\\\\\"metadata\\\\\\\"])\\\\nprint(\\\\\\\"n_examples in demo:\\\\\\\", len(data[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"4b221478\",\n   \"source\": \"## Config\\\\n\\\\nAll tunable parameters from the original `method.py`, collected here. `N_BOOT` (bootstrap resamples) and the placebo-check resample count are the two knobs that dominate runtime, so they are set to small-but-nonzero values for this demo (the original values, used for the full 34-repo run, are commented alongside). Everything else (thresholds, window sizes) is reused **unchanged** from the validated iter1 pipeline, per the docstring's \\\\\\\"do not re-tune\\\\\\\" note.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"3e8cb93d\",\n   \"source\": \"# --- constants reused verbatim from iter1 (do not re-tune) ---\\\\nSILENCE_THRESHOLD_DAYS = 365\\\\nTF_COVERAGE_THRESHOLD = 0.5\\\\nPOST_TFDD_WINDOW_DAYS = 548  # 18 months\\\\nPRE_WINDOW_FAR_DAYS = 365  # 12 months before TFDD\\\\nPRE_WINDOW_NEAR_DAYS = 180  # 6 months before TFDD\\\\nSNAPSHOT_EVERY_DAYS = 90\\\\nSTRICT_FOUNDER_SHARE = 0.70  # re-verification threshold for founder-only strict criterion\\\\nRELAXED_FOUNDER_SHARE = 0.50\\\\nTARGET_N_STRICT = 40  # iter1 power-analysis target; 34-repo pool structurally caps below this\\\\n\\\\nAVELINO_REFERENCE_SURVIVAL_RATE = 0.41\\\\n\\\\n# --- runtime-dominating knobs: minimized for this small demo ---\\\\nN_BOOT = 200  # original: 5000 (bootstrap CI resamples for matched-pairs / mean-diff CIs)\\\\nN_PLACEBO_BOOT = 50  # original: 1000 (placebo-window empirical-null resamples)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"9da1f4fc\",\n   \"source\": \"## Step 0: reconstruct per-repo commit streams\\\\n\\\\nThe mined `full_data_out.json` (here, its `mini_demo_data.json` subset) stores one row per `(commit, file)` pair. This step groups rows back into per-repo, per-commit lists sorted by date — the same shape `git log --numstat` would have produced if the pipeline had cloned these repos live, but read from the already-mined dataset instead.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder Diffusion Timing vs. Project Survival\\\\n\\\\nThis notebook demonstrates the founder-only **Truck-Factor Developer Departure (TFDD)** pipeline: it reconstructs per-repo commit history from mined `(commit, file)` rows, computes the **Degree-of-Authorship (DOA)** formula of Fritz et al. 2010 / Avelino et al. ICPC2016 to find each file's primary owner, detects the moment a repo drops to a single-developer Truck Factor and that developer then goes silent for 365+ days (a TFDD event), measures the **pre-departure authority-diffusion trajectory** (founder commit share and number of diffused owners in the 6-12 month window before departure), and classifies whether the project **survives** the following 18 months (recovers a non-founder Truck-Factor owner).\\\\n\\\\nIt also runs the iteration's new **Medappa-et-al.-style reconciliation model**: a static whole-history write-access ratio (`medappa_ratio`) plus a `timing_term` capturing how concentrated diffusion onset is near departure vs. spread through history, testing whether it is the *timing* of diffusion — not its mere presence — that predicts survival.\\\\n\\\\nThis demo runs the full pipeline on a small subset of repos (2 repos, ~1200 commit/file rows) from the original 34-repo founder-candidate corpus, small enough to finish in well under a minute while producing real founder-TFDD events end to end.\"\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b0d42898\",\n   \"source\": \"import subprocess, sys\\\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\\\n\\\\n# statsmodels, loguru -- NOT pre-installed on Colab, always install\\\\n_pip('statsmodels==0.14.6')\\\\n_pip('loguru==0.7.2')\\\\n\\\\n# numpy, pandas, scipy -- pre-installed on Colab, install locally only (Colab's exact versions)\\\\nif 'google.colab' not in sys.modules:\\\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'scipy==1.16.3')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"96e95ae7\",\n   \"source\": \"from __future__ import annotations\\\\n\\\\nimport gc\\\\nimport json\\\\nimport math\\\\nimport random\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter, defaultdict\\\\nfrom dataclasses import asdict, dataclass\\\\nfrom datetime import datetime, timedelta, timezone\\\\nfrom pathlib import Path\\\\nfrom typing import Optional\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nimport statsmodels.api as sm\\\\nfrom loguru import logger\\\\nfrom scipy import stats\\\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\\\n\\\\n# added for the notebook's results visualization cell\\\\nimport matplotlib.pyplot as plt\\\\n\\\\nlogger.remove()\\\\nlogger.add(sys.stdout, level=\\\\\\\"INFO\\\\\\\", format=\\\\\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\\\\\")\\\\n\\\\nRNG_SEED = 20260821\\\\nrandom.seed(RNG_SEED)\\\\nnp.random.seed(RNG_SEED)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"bb7b7f61\",\n   \"source\": \"## Load the demo data\\\\n\\\\n`mini_demo_data.json` is a curated subset of the original mined `full_data_out.json`: the full per-`(commit, file)` row corpus for **two** of the 34 founder-candidate repos (`JustinSDK/JavaSE6Tutorial` and `Krupen/AutoplayVideos`, ~1200 rows total) — both of which are known to produce a genuine founder-only TFDD event under the original pipeline, so this small demo still exercises the full detection + survival + reconciliation logic end to end.\\\\n\\\\nThe loader tries the GitHub raw URL first (works once this artifact is pushed / on Colab), then falls back to the local file (works right now).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"07e078ee\",\n   \"source\": \"GITHUB_DATA_URL = \\\\\\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/experiment-1/demo/mini_demo_data.json\\\\\\\"\\\\nimport json, os\\\\n\\\\ndef load_data():\\\\n    try:\\\\n        import urllib.request\\\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\\\n            return json.loads(response.read().decode())\\\\n    except Exception: pass\\\\n    if os.path.exists(\\\\\\\"mini_demo_data.json\\\\\\\"):\\\\n        with open(\\\\\\\"mini_demo_data.json\\\\\\\") as f: return json.load(f)\\\\n    raise FileNotFoundError(\\\\\\\"Could not load mini_demo_data.json\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"12ed4615\",\n   \"source\": \"data = load_data()\\\\nprint(data[\\\\\\\"metadata\\\\\\\"])\\\\nprint(\\\\\\\"n_examples in demo:\\\\\\\", len(data[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]))\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"4b221478\",\n   \"source\": \"## Config\\\\n\\\\nAll tunable parameters from the original `method.py`, collected here. `N_BOOT` (bootstrap resamples) and the placebo-check resample count are the two knobs that dominate runtime, so they are set to small-but-nonzero values for this demo (the original values, used for the full 34-repo run, are commented alongside). Everything else (thresholds, window sizes) is reused **unchanged** from the validated iter1 pipeline, per the docstring's \\\\\\\"do not re-tune\\\\\\\" note.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"3e8cb93d\",\n   \"source\": \"# --- constants reused verbatim from iter1 (do not re-tune) ---\\\\nSILENCE_THRESHOLD_DAYS = 365\\\\nTF_COVERAGE_THRESHOLD = 0.5\\\\nPOST_TFDD_WINDOW_DAYS = 548  # 18 months\\\\nPRE_WINDOW_FAR_DAYS = 365  # 12 months before TFDD\\\\nPRE_WINDOW_NEAR_DAYS = 180  # 6 months before TFDD\\\\nSNAPSHOT_EVERY_DAYS = 90\\\\nSTRICT_FOUNDER_SHARE = 0.70  # re-verification threshold for founder-only strict criterion\\\\nRELAXED_FOUNDER_SHARE = 0.50\\\\nTARGET_N_STRICT = 40  # iter1 power-analysis target; 34-repo pool structurally caps below this\\\\n\\\\nAVELINO_REFERENCE_SURVIVAL_RATE = 0.41\\\\n\\\\n# --- runtime-dominating knobs: minimized for this small demo ---\\\\nN_BOOT = 200  # original: 5000 (bootstrap CI resamples for matched-pairs / mean-diff CIs)\\\\nN_PLACEBO_BOOT = 50  # original: 1000 (placebo-window empirical-null resamples)\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"9da1f4fc\",\n   \"source\": \"## Step 0: reconstruct per-repo commit streams\\\\n\\\\nThe mined `full_data_out.json` (here, its `mini_demo_data.json` subset) stores one row per `(commit, file)` pair. This step groups rows back into per-repo, per-commit lists sorted by date — the same shape `git log --numstat` would have produced if the pipeline had cloned these repos live, but read from the already-mined dataset instead.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"17e949b6\",\n   \"source\": \"def load_repo_commit_streams(raw: dict) -> dict[str, dict]:\\\\n    examples = raw[\\\\\\\"datasets\\\\\\\"][0][\\\\\\\"examples\\\\\\\"]\\\\n    logger.info(f\\\\\\\"[step0] loaded {len(examples)} (commit,file) rows\\\\\\\")\\\\n\\\\n    repos: dict[str, dict] = {}\\\\n    for row in examples:\\\\n        rid = str(row[\\\\\\\"metadata_repo_id\\\\\\\"])\\\\n        rep = repos.setdefault(\\\\n            rid,\\\\n            {\\\\n                \\\\\\\"full_name\\\\\\\": row[\\\\\\\"metadata_full_name\\\\\\\"],\\\\n                \\\\\\\"license_key\\\\\\\": row.get(\\\\\\\"metadata_license\\\\\\\") or \\\\\\\"none\\\\\\\",\\\\n                \\\\\\\"created_at\\\\\\\": datetime.fromisoformat(row[\\\\\\\"metadata_repo_created_at\\\\\\\"].replace(\\\\\\\"Z\\\\\\\", \\\\\\\"+00:00\\\\\\\")),\\\\n                \\\\\\\"stars\\\\\\\": None,\\\\n                \\\\\\\"forks\\\\\\\": None,\\\\n                \\\\\\\"language\\\\\\\": None,\\\\n                \\\\\\\"commits_by_sha\\\\\\\": {},\\\\n                \\\\\\\"dominant_founder_first_window_share\\\\\\\": row.get(\\\\\\\"metadata_dominant_founder_share_first_window\\\\\\\"),\\\\n                \\\\\\\"alias_ambiguous\\\\\\\": row.get(\\\\\\\"metadata_alias_ambiguous_repo\\\\\\\"),\\\\n            },\\\\n        )\\\\n        try:\\\\n            inp = json.loads(row[\\\\\\\"input\\\\\\\"])\\\\n        except (json.JSONDecodeError, TypeError):\\\\n            inp = {}\\\\n        if rep[\\\\\\\"stars\\\\\\\"] is None:\\\\n            rep[\\\\\\\"stars\\\\\\\"] = inp.get(\\\\\\\"repo_stars\\\\\\\", 0)\\\\n            rep[\\\\\\\"forks\\\\\\\"] = inp.get(\\\\\\\"repo_forks\\\\\\\", 0)\\\\n            rep[\\\\\\\"language\\\\\\\"] = inp.get(\\\\\\\"repo_primary_language\\\\\\\", \\\\\\\"unknown\\\\\\\")\\\\n        sha = row[\\\\\\\"metadata_commit_sha\\\\\\\"]\\\\n        c = rep[\\\\\\\"commits_by_sha\\\\\\\"].get(sha)\\\\n        if c is None:\\\\n            try:\\\\n                dt = datetime.fromisoformat(row[\\\\\\\"metadata_commit_timestamp\\\\\\\"])\\\\n            except ValueError:\\\\n                continue\\\\n            c = {\\\\\\\"hash\\\\\\\": sha, \\\\\\\"author_email\\\\\\\": row[\\\\\\\"metadata_author_alias_key\\\\\\\"], \\\\\\\"date\\\\\\\": dt, \\\\\\\"files\\\\\\\": []}\\\\n            rep[\\\\\\\"commits_by_sha\\\\\\\"][sha] = c\\\\n        added = inp.get(\\\\\\\"lines_added\\\\\\\", 0) or 0\\\\n        removed = inp.get(\\\\\\\"lines_removed\\\\\\\", 0) or 0\\\\n        c[\\\\\\\"files\\\\\\\"].append((inp.get(\\\\\\\"file_path\\\\\\\", \\\\\\\"?\\\\\\\"), added, removed))\\\\n\\\\n    for rep in repos.values():\\\\n        commits = sorted(rep[\\\\\\\"commits_by_sha\\\\\\\"].values(), key=lambda c: c[\\\\\\\"date\\\\\\\"])\\\\n        rep[\\\\\\\"commits\\\\\\\"] = commits\\\\n        del rep[\\\\\\\"commits_by_sha\\\\\\\"]\\\\n    logger.info(f\\\\\\\"[step0] grouped into {len(repos)} repos\\\\\\\")\\\\n    return repos\\\\n\\\\n\\\\nrepos = load_repo_commit_streams(data)\\\\nn_repo_candidates = len(repos)\\\\nfor rid, rep in repos.items():\\\\n    print(rep[\\\\\\\"full_name\\\\\\\"], \\\\\\\"-\\\\\\\", len(rep[\\\\\\\"commits\\\\\\\"]), \\\\\\\"commits\\\\\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [67] ASSISTANT · 2026-08-21 21:37:34 UTC

```
Now DOA/Truck-Factor cells.
```

### [68] TOOL CALL — NotebookEdit · 2026-08-21 21:37:34 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '17e949b6', 'edit_mode': 'insert', 'cell_type': 'markdown', 'new_source': '## Degree-of-Authorship (DOA) and Truck-Factor\\n\\nReused verbatim from iter1: the Fritz et al. 2010 DOA formula as validated by Avelino et al. (ICPC 2016 / ESEM 2019), `DOA(dev, file, t) = 3.293 + 1.098*FA - 0.164*sqrt(AC) + 0.230*ln(1+DL)` where `FA` = first-author flag, `AC` = number of commits by that dev to that file, `DL` = deleted lines. The primary owner of a file is whoever has the highest DOA at a given cutoff date. The Truck Factor set is the smallest set of top owners whose files collectively cover >=50% of the repo."]'}
```

### [69] TOOL RESULT — NotebookEdit · 2026-08-21 21:37:34 UTC

```
{"new_source": "## Degree-of-Authorship (DOA) and Truck-Factor\\n\\nReused verbatim from iter1: the Fritz et al. 2010 DOA formula as validated by Avelino et al. (ICPC 2016 / ESEM 2019), `DOA(dev, file, t) = 3.293 + 1.098*FA - 0.164*sqrt(AC) + 0.230*ln(1+DL)` where `FA` = first-author flag, `AC` = number of commits by that dev to that file, `DL` = deleted lines. The primary owner of a file is whoever has the highest DOA at a given cutoff date. The Truck Factor set is th... [truncated, 23226 chars total]
```

### [70] TOOL CALL — NotebookEdit · 2026-08-21 21:37:38 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '0525f05c', 'new_source': '## Degree-of-Authorship (DOA) and Truck-Factor\\n\\nReused verbatim from iter1: the Fritz et al. 2010 DOA formula as validated by Avelino et al. (ICPC 2016 / ESEM 2019), `DOA(dev, file, t) = 3.293 + 1.098*FA - 0.164*sqrt(AC) + 0.230*ln(1+DL)` where `FA` = first-author flag, `AC` = number of commits by that dev to that file, `DL` = deleted lines. The primary owner of a file is whoever has the highest DOA at a given cutoff date. The Truck Factor set is the smallest set of top owners whose files collectively cover >=50% of the repo.'}
```

### [71] TOOL RESULT — NotebookEdit · 2026-08-21 21:37:40 UTC

```
{"new_source": "## Degree-of-Authorship (DOA) and Truck-Factor\\n\\nReused verbatim from iter1: the Fritz et al. 2010 DOA formula as validated by Avelino et al. (ICPC 2016 / ESEM 2019), `DOA(dev, file, t) = 3.293 + 1.098*FA - 0.164*sqrt(AC) + 0.230*ln(1+DL)` where `FA` = first-author flag, `AC` = number of commits by that dev to that file, `DL` = deleted lines. The primary owner of a file is whoever has the highest DOA at a given cutoff date. The Truck Factor set is th... [truncated, 24428 chars total]
```

### [72] TOOL CALL — NotebookEdit · 2026-08-21 21:37:46 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '0525f05c', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': 'def doa_snapshot(commits: list[dict], cutoff: datetime) -> dict[tuple[str, str], float]:\\n    file_dev_stats: dict[str, dict[str, dict]] = defaultdict(dict)\\n    file_first_author: dict[str, str] = {}\\n    for c in commits:\\n        if c[\\"date\\"] > cutoff:\\n            break\\n        for path, added, deleted in c[\\"files\\"]:\\n            if path not in file_first_author:\\n                file_first_author[path] = c[\\"author_email\\"]\\n            dev_stats = file_dev_stats[path]\\n            s = dev_stats.setdefault(c[\\"author_email\\"], {\\"ac\\": 0, \\"dl\\": 0})\\n            s[\\"ac\\"] += 1\\n            s[\\"dl\\"] += deleted\\n    doa: dict[tuple[str, str], float] = {}\\n    for path, devs in file_dev_stats.items():\\n        first_author = file_first_author[path]\\n        for dev, s in devs.items():\\n            fa = 1 if dev == first_author else 0\\n            doa[(dev, path)] = 3.293 + 1.098 * fa - 0.164 * math.sqrt(s[\\"ac\\"]) + 0.230 * math.log(1 + s[\\"dl\\"])\\n    return doa\\n\\n\\ndef file_owners(doa: dict[tuple[str, str], float]) -> dict[str, tuple[str, float]]:\\n    owner: dict[str, tuple[str, float]] = {}\\n    for (dev, path), score in doa.items():\\n        if path not in owner or score > owner[path][1]:\\n            owner[path] = (dev, score)\\n    return owner\\n\\n\\ndef truck_factor_set(doa: dict[tuple[str, str], float]) -> list[str]:\\n    owner = file_owners(doa)\\n    total_files = len(owner)\\n    if total_files == 0:\\n        return []\\n    owned_counts = Counter(dev for dev, _ in owner.values())\\n    tf_set: list[str] = []\\n    covered = 0\\n    for dev, n in owned_counts.most_common():\\n        tf_set.append(dev)\\n        covered += n\\n        if covered >= TF_COVERAGE_THRESHOLD * total_files:\\n            break\\n    return tf_set'}
```

### [73] TOOL RESULT — NotebookEdit · 2026-08-21 21:37:48 UTC

```
{"new_source": "def doa_snapshot(commits: list[dict], cutoff: datetime) -> dict[tuple[str, str], float]:\\n    file_dev_stats: dict[str, dict[str, dict]] = defaultdict(dict)\\n    file_first_author: dict[str, str] = {}\\n    for c in commits:\\n        if c[\\\"date\\\"] > cutoff:\\n            break\\n        for path, added, deleted in c[\\\"files\\\"]:\\n            if path not in file_first_author:\\n                file_first_author[path] = c[\\\"author_email\\\"]... [truncated, 27348 chars total]
```

### [74] ASSISTANT · 2026-08-21 21:37:54 UTC

```
Now TFDDEvent + detection functions.
```

### [75] TOOL CALL — NotebookEdit · 2026-08-21 21:37:54 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '1260744c', 'edit_mode': 'insert', 'cell_type': 'markdown', 'new_source': "## TFDD event detection\\n\\n`TFDDEvent` records one founder-only Truck-Factor Developer Departure: the moment a repo's Truck Factor drops to a single developer who then goes silent for `SILENCE_THRESHOLD_DAYS` (365 days). `detect_founder_tfdd` scans snapshots every `SNAPSHOT_EVERY_DAYS` (90 days) for the **strict** criterion (Truck Factor == 1); `detect_relaxed_tfdd` is a looser variant allowing a Truck Factor of 1 or 2."}
```

### [76] TOOL RESULT — NotebookEdit · 2026-08-21 21:37:54 UTC

```
{"new_source": "## TFDD event detection\\n\\n`TFDDEvent` records one founder-only Truck-Factor Developer Departure: the moment a repo's Truck Factor drops to a single developer who then goes silent for `SILENCE_THRESHOLD_DAYS` (365 days). `detect_founder_tfdd` scans snapshots every `SNAPSHOT_EVERY_DAYS` (90 days) for the **strict** criterion (Truck Factor == 1); `detect_relaxed_tfdd` is a looser variant allowing a Truck Factor of 1 or 2.", "cell_type": "markdown", "lan... [truncated, 28646 chars total]
```

### [77] TOOL CALL — NotebookEdit · 2026-08-21 21:38:04 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '1e07eb7c', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': '@dataclass\\nclass TFDDEvent:\\n    repo: str\\n    founder: str\\n    tfdd_date: datetime\\n    repo_created_at: datetime\\n    stars: int\\n    forks: int\\n    language: str\\n    license_key: str\\n    n_commits_total: int\\n    tf_set_size_at_relaxed: int = 1\\n    devs_at_tfdd: int = 0\\n    commits_at_tfdd: int = 0\\n    files_at_tfdd: int = 0\\n    founder_share: float = float(\\"nan\\")\\n    n_diffused_owners: int = 0\\n    placebo_founder_share: float = float(\\"nan\\")\\n    placebo_n_diffused_owners: int = 0\\n    survived: Optional[bool] = None\\n    grade: str = \\"\\"\\n    censored: bool = False\\n    devs_seen_up_to_tfdd: int = 0\\n    # NEW (this iteration): reconciliation-test measurements\\n    medappa_ratio: float = float(\\"nan\\")\\n    timing_term: float = float(\\"nan\\")\\n\\n\\ndef detect_founder_tfdd(commits: list[dict], snapshot_every_days: int = SNAPSHOT_EVERY_DAYS) -> Optional[tuple[datetime, str]]:\\n    if len(commits) < 20:\\n        return None\\n    start = commits[0][\\"date\\"]\\n    end = commits[-1][\\"date\\"]\\n    last_active: dict[str, datetime] = {}\\n    for c in commits:\\n        e = c[\\"author_email\\"]\\n        if e not in last_active or c[\\"date\\"] > last_active[e]:\\n            last_active[e] = c[\\"date\\"]\\n    cursor = start + timedelta(days=180)\\n    while cursor <= end:\\n        doa = doa_snapshot(commits, cursor)\\n        tf_set = truck_factor_set(doa)\\n        if len(tf_set) == 1:\\n            founder = tf_set[0]\\n            silence = (cursor - last_active.get(founder, start)).days\\n            if silence >= SILENCE_THRESHOLD_DAYS:\\n                tfdd_date = last_active[founder] + timedelta(days=SILENCE_THRESHOLD_DAYS)\\n                return min(tfdd_date, cursor), founder\\n        cursor += timedelta(days=snapshot_every_days)\\n    return None\\n\\n\\ndef detect_relaxed_tfdd(commits: list[dict], snapshot_every_days: int = SNAPSHOT_EVERY_DAYS) -> Optional[tuple[datetime, list[str]]]:\\n    if len(commits) < 20:\\n        return None\\n    start = commits[0][\\"date\\"]\\n    end = commits[-1][\\"date\\"]\\n    last_active: dict[str, datetime] = {}\\n    for c in commits:\\n        e = c[\\"author_email\\"]\\n        if e not in last_active or c[\\"date\\"] > last_active[e]:\\n            last_active[e] = c[\\"date\\"]\\n    cursor = start + timedelta(days=180)\\n    while cursor <= end:\\n        doa = doa_snapshot(commits, cursor)\\n        tf_set = truck_factor_set(doa)\\n        if 1 <= len(tf_set) <= 2 and all(\\n            (cursor - last_active.get(d, start)).days >= SILENCE_THRESHOLD_DAYS for d in tf_set\\n        ):\\n            tfdd_date = max(last_active[d] for d in tf_set) + timedelta(days=SILENCE_THRESHOLD_DAYS)\\n            return min(tfdd_date, cursor), tf_set\\n        cursor += timedelta(days=snapshot_every_days)\\n    return None'}
```

### [78] TOOL RESULT — NotebookEdit · 2026-08-21 21:38:04 UTC

```
{"new_source": "@dataclass\\nclass TFDDEvent:\\n    repo: str\\n    founder: str\\n    tfdd_date: datetime\\n    repo_created_at: datetime\\n    stars: int\\n    forks: int\\n    language: str\\n    license_key: str\\n    n_commits_total: int\\n    tf_set_size_at_relaxed: int = 1\\n    devs_at_tfdd: int = 0\\n    commits_at_tfdd: int = 0\\n    files_at_tfdd: int = 0\\n    founder_share: float = float(\\\"nan\\\")\\n    n_diffused_owners: int = 0\\n    placebo_founder_s... [truncated, 35000 chars total]
```

### [79] ASSISTANT · 2026-08-21 21:38:10 UTC

```
Now window_metrics, placebo, classify_grade, label_survival, medappa/timing.
```

### [80] TOOL CALL — NotebookEdit · 2026-08-21 21:38:10 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': 'f302e402', 'edit_mode': 'insert', 'cell_type': 'markdown', 'new_source': "## Pre-departure diffusion window, placebo windows, and post-departure survival grading\\n\\n`window_metrics` measures `founder_share` (fraction of commits by the founder) and `n_diffused_owners` (distinct non-founder file owners) inside a given window. `sample_placebo_window` picks a random 180-day window elsewhere in the repo's history, for the placebo/shuffle null-distribution check later. `classify_grade`/`label_survival` determine the 18-month post-TFDD outcome (survived = recovers a non-founder Truck-Factor owner)."}
```

### [81] TOOL RESULT — NotebookEdit · 2026-08-21 21:38:10 UTC

```
{"new_source": "## Pre-departure diffusion window, placebo windows, and post-departure survival grading\\n\\n`window_metrics` measures `founder_share` (fraction of commits by the founder) and `n_diffused_owners` (distinct non-founder file owners) inside a given window. `sample_placebo_window` picks a random 180-day window elsewhere in the repo's history, for the placebo/shuffle null-distribution check later. `classify_grade`/`label_survival` determine the 18-month post... [truncated, 36598 chars total]
```

### [82] TOOL CALL — NotebookEdit · 2026-08-21 21:38:20 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': 'ebbc258c', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': 'def window_metrics(commits: list[dict], window_start: datetime, window_end: datetime, founder: str) -> tuple[float, int]:\\n    window_commits = [c for c in commits if window_start <= c[\\"date\\"] < window_end]\\n    if not window_commits:\\n        return float(\\"nan\\"), 0\\n    founder_commits = sum(1 for c in window_commits if c[\\"author_email\\"] == founder)\\n    founder_share = founder_commits / len(window_commits)\\n    doa_end = doa_snapshot(commits, window_end)\\n    owner = file_owners(doa_end)\\n    non_founder_owners = {o[0] for o in owner.values() if o[0] != founder}\\n    return founder_share, len(non_founder_owners)\\n\\n\\ndef sample_placebo_window(commits: list[dict], exclude_start: datetime, exclude_end: datetime) -> Optional[tuple[datetime, datetime]]:\\n    start = commits[0][\\"date\\"]\\n    end = commits[-1][\\"date\\"]\\n    total_span_days = (end - start).days\\n    if total_span_days < 800:\\n        return None\\n    for _ in range(20):\\n        offset = random.uniform(0, total_span_days - 180)\\n        w_start = start + timedelta(days=offset)\\n        w_end = w_start + timedelta(days=180)\\n        if w_end < exclude_start - timedelta(days=365) or w_start > exclude_end + timedelta(days=365):\\n            return w_start, w_end\\n    return None\\n\\n\\ndef classify_grade(post_commits: list[dict], recovered_tf: list[str], founder: str) -> str:\\n    if not post_commits:\\n        return \\"dead\\"\\n    n_devs = len({c[\\"author_email\\"] for c in post_commits})\\n    n_commits = len(post_commits)\\n    non_founder_tf = [d for d in recovered_tf if d != founder]\\n    if non_founder_tf and n_commits >= 20 and n_devs >= 2:\\n        return \\"thriving\\"\\n    if n_commits >= 5:\\n        return \\"maintained\\"\\n    if n_commits >= 1:\\n        return \\"dormant\\"\\n    return \\"dead\\"\\n\\n\\ndef label_survival(commits: list[dict], event: TFDDEvent, last_commit_date: datetime) -> None:\\n    window_end = event.tfdd_date + timedelta(days=POST_TFDD_WINDOW_DAYS)\\n    if last_commit_date < window_end:\\n        event.censored = True\\n    post = [c for c in commits if event.tfdd_date <= c[\\"date\\"] < window_end]\\n    doa_post = doa_snapshot(commits, window_end)\\n    recovered_tf = truck_factor_set(doa_post)\\n    event.survived = bool(recovered_tf) and any(d != event.founder for d in recovered_tf)\\n    event.grade = classify_grade(post, recovered_tf, event.founder)'}
```

### [83] TOOL RESULT — NotebookEdit · 2026-08-21 21:38:20 UTC

```
{"new_source": "def window_metrics(commits: list[dict], window_start: datetime, window_end: datetime, founder: str) -> tuple[float, int]:\\n    window_commits = [c for c in commits if window_start <= c[\\\"date\\\"] < window_end]\\n    if not window_commits:\\n        return float(\\\"nan\\\"), 0\\n    founder_commits = sum(1 for c in window_commits if c[\\\"author_email\\\"] == founder)\\n    founder_share = founder_commits / len(window_commits)\\n    doa_end = doa_sn... [truncated, 42010 chars total]
```

### [84] ASSISTANT · 2026-08-21 21:38:26 UTC

```
Now medappa/timing.
```

### [85] TOOL CALL — NotebookEdit · 2026-08-21 21:38:26 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '1d1383d1', 'edit_mode': 'insert', 'cell_type': 'markdown', 'new_source': "## NEW (this iteration): Medappa-style reconciliation measurements\\n\\n`medappa_ratio` is a static, whole-pre-history write-access ratio (analog of Medappa et al.'s construct): the fraction of pre-TFDD developers who ever reached primary DOA ownership of at least one file. `timing_term` measures, among non-founder devs who own files AT the TFDD date, what fraction of their ownership *onset* dates fall inside the 6-12mo pre-departure window vs. earlier — testing whether diffusion is concentrated near departure or was already present in the repo's history."}
```

### [86] TOOL RESULT — NotebookEdit · 2026-08-21 21:38:26 UTC

```
{"new_source": "## NEW (this iteration): Medappa-style reconciliation measurements\\n\\n`medappa_ratio` is a static, whole-pre-history write-access ratio (analog of Medappa et al.'s construct): the fraction of pre-TFDD developers who ever reached primary DOA ownership of at least one file. `timing_term` measures, among non-founder devs who own files AT the TFDD date, what fraction of their ownership *onset* dates fall inside the 6-12mo pre-departure window vs. earlier ... [truncated, 43610 chars total]
```

### [87] TOOL CALL — NotebookEdit · 2026-08-21 21:38:32 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '47a19995', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': 'def compute_medappa_and_timing(\\n    commits: list[dict], founder: str, tfdd_date: datetime, window_start: datetime, window_end: datetime\\n) -> tuple[float, float]:\\n    devs_before = {c[\\"author_email\\"] for c in commits if c[\\"date\\"] <= tfdd_date}\\n    doa_tfdd = doa_snapshot(commits, tfdd_date)\\n    owners_tfdd = file_owners(doa_tfdd)\\n    ever_owners = {o[0] for o in owners_tfdd.values()}\\n    medappa_ratio = len(ever_owners) / len(devs_before) if devs_before else float(\\"nan\\")\\n\\n    non_founder_owners_at_tfdd = {o[0] for o in owners_tfdd.values() if o[0] != founder}\\n    if not non_founder_owners_at_tfdd:\\n        return medappa_ratio, float(\\"nan\\")\\n\\n    start = commits[0][\\"date\\"]\\n    onset_date: dict[str, datetime] = {}\\n    cursor = start + timedelta(days=180)\\n    remaining = set(non_founder_owners_at_tfdd)\\n    while cursor <= tfdd_date and remaining:\\n        doa = doa_snapshot(commits, cursor)\\n        owners = file_owners(doa)\\n        present = {o[0] for o in owners.values()}\\n        newly_onset = remaining & present\\n        for dev in newly_onset:\\n            onset_date[dev] = cursor\\n        remaining -= newly_onset\\n        cursor += timedelta(days=SNAPSHOT_EVERY_DAYS)\\n    for dev in remaining:  # never caught by a coarse snapshot before TFDD -> onset at TFDD itself\\n        onset_date[dev] = tfdd_date\\n\\n    n_total = len(onset_date)\\n    n_in_window = sum(1 for d in onset_date.values() if window_start <= d < window_end)\\n    timing_term = n_in_window / n_total if n_total else float(\\"nan\\")\\n    return medappa_ratio, timing_term'}
```

### [88] TOOL RESULT — NotebookEdit · 2026-08-21 21:38:34 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [89] ASSISTANT · 2026-08-21 21:38:38 UTC

```
Now stats helpers.
```

### [90] TOOL CALL — NotebookEdit · 2026-08-21 21:38:38 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '95942d62', 'edit_mode': 'insert', 'cell_type': 'markdown', 'new_source': "## Statistics helpers\\n\\nMatched-pairs construction (low- vs. high-diffusion repos matched on language/stars/forks/devs, with a relaxed same-stratum fallback), bootstrap survival-rate-ratio CIs, Benjamini-Hochberg FDR correction, Cohen's d, and bootstrap mean-difference CIs — all reused verbatim from iter1."}
```

### [91] TOOL RESULT — NotebookEdit · 2026-08-21 21:38:38 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [92] TOOL CALL — NotebookEdit · 2026-08-21 21:38:56 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': 'e6aaf04f', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': 'def build_matched_pairs(df: pd.DataFrame, low_thresh: float = 0.50, hi_thresh: float = 0.80, n_diffused_min: int = 2):\\n    lo = df[(df.founder_share < low_thresh) & (df.n_diffused_owners >= n_diffused_min)].copy()\\n    hi = df[df.founder_share >= hi_thresh].copy()\\n    pairs = []\\n    used_hi = set()\\n    for _, lrow in lo.iterrows():\\n        best_idx, best_dist = None, float(\\"inf\\")\\n        for hidx, hrow in hi.iterrows():\\n            if hidx in used_hi or hrow.language != lrow.language:\\n                continue\\n            dist = (\\n                (math.log1p(hrow.stars) - math.log1p(lrow.stars)) ** 2\\n                + (math.log1p(hrow.forks) - math.log1p(lrow.forks)) ** 2\\n                + (math.log1p(hrow.devs_at_tfdd) - math.log1p(lrow.devs_at_tfdd)) ** 2\\n            )\\n            if dist < best_dist:\\n                best_dist, best_idx = dist, hidx\\n        if best_idx is not None and best_dist < 4.0:\\n            used_hi.add(best_idx)\\n            pairs.append((lrow, hi.loc[best_idx]))\\n    return pairs\\n\\n\\ndef build_matched_pairs_relaxed(df: pd.DataFrame, low_thresh: float = 0.50, hi_thresh: float = 0.80, n_diffused_min: int = 2):\\n    \\"\\"\\"fallback_plan item (4): same-stratum-only matching, drop the exact language\\n    requirement (kept as a regression covariate elsewhere instead).\\"\\"\\"\\n    lo = df[(df.founder_share < low_thresh) & (df.n_diffused_owners >= n_diffused_min)].copy()\\n    hi = df[df.founder_share >= hi_thresh].copy()\\n\\n    def star_stratum(s: float) -> int:\\n        return 0 if s < 1000 else (1 if s < 10000 else 2)\\n\\n    pairs = []\\n    used_hi = set()\\n    for _, lrow in lo.iterrows():\\n        best_idx, best_dist = None, float(\\"inf\\")\\n        for hidx, hrow in hi.iterrows():\\n            if hidx in used_hi or star_stratum(hrow.stars) != star_stratum(lrow.stars):\\n                continue\\n            dist = (math.log1p(hrow.devs_at_tfdd) - math.log1p(lrow.devs_at_tfdd)) ** 2\\n            if dist < best_dist:\\n                best_dist, best_idx = dist, hidx\\n        if best_idx is not None:\\n            used_hi.add(best_idx)\\n            pairs.append((lrow, hi.loc[best_idx]))\\n    return pairs\\n\\n\\ndef bootstrap_survival_rate_ratio(pairs: list[tuple[pd.Series, pd.Series]], n_boot: int = N_BOOT) -> tuple[float, tuple[float, float], Optional[str]]:\\n    if not pairs:\\n        return float(\\"nan\\"), (float(\\"nan\\"), float(\\"nan\\")), \\"no matched pairs\\"\\n    lo_surv = np.array([1.0 if p[0].survived else 0.0 for p in pairs])\\n    hi_surv = np.array([1.0 if p[1].survived else 0.0 for p in pairs])\\n    n = len(pairs)\\n    ratios = []\\n    for _ in range(n_boot):\\n        idx = np.random.randint(0, n, size=n)\\n        lo_rate = lo_surv[idx].mean()\\n        hi_rate = hi_surv[idx].mean()\\n        if hi_rate == 0:\\n            continue\\n        ratios.append((lo_rate + 1e-6) / (hi_rate + 1e-6))\\n    if not ratios:\\n        degeneracy_note = (\\n            f\\"ALL {n_boot} bootstrap resamples had zero survivors in the high-diffusion group \\"\\n            f\\"(hi_surv.mean()={hi_surv.mean():.3f} across the {n} matched pairs) -- the risk-ratio is \\"\\n            \\"degenerate at this n, not computable, and NOT silently reported as a point estimate.\\"\\n        )\\n        return float(\\"nan\\"), (float(\\"nan\\"), float(\\"nan\\")), degeneracy_note\\n    ratios = np.array(ratios)\\n    point = (lo_surv.mean() + 1e-6) / (hi_surv.mean() + 1e-6)\\n    ci = (float(np.percentile(ratios, 2.5)), float(np.percentile(ratios, 97.5)))\\n    return float(point), ci, None\\n\\n\\ndef benjamini_hochberg(pvals: dict[str, float]) -> dict[str, float]:\\n    items = sorted(pvals.items(), key=lambda kv: kv[1])\\n    m = len(items)\\n    adj = {}\\n    prev = 1.0\\n    for rank, (k, p) in enumerate(reversed(items), start=1):\\n        r = m - rank + 1\\n        val = min(prev, p * m / r)\\n        adj[k] = val\\n        prev = val\\n    return adj\\n\\n\\ndef cohens_d(a: np.ndarray, b: np.ndarray) -> float:\\n    a, b = a[~np.isnan(a)], b[~np.isnan(b)]\\n    if len(a) < 2 or len(b) < 2:\\n        return float(\\"nan\\")\\n    pooled_sd = math.sqrt(((len(a) - 1) * a.var(ddof=1) + (len(b) - 1) * b.var(ddof=1)) / (len(a) + len(b) - 2))\\n    if pooled_sd == 0:\\n        return float(\\"nan\\")\\n    return float((a.mean() - b.mean()) / pooled_sd)\\n\\n\\ndef bootstrap_ci_mean_diff(a: np.ndarray, b: np.ndarray, n_boot: int = N_BOOT) -> tuple[float, float]:\\n    a, b = a[~np.isnan(a)], b[~np.isnan(b)]\\n    if len(a) < 2 or len(b) < 2:\\n        return float(\\"nan\\"), float(\\"nan\\")\\n    diffs = np.empty(n_boot)\\n    for i in range(n_boot):\\n        ai = a[np.random.randint(0, len(a), len(a))]\\n        bi = b[np.random.randint(0, len(b), len(b))]\\n        diffs[i] = ai.mean() - bi.mean()\\n    return float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5))'}
```

### [93] TOOL RESULT — NotebookEdit · 2026-08-21 21:38:56 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [94] ASSISTANT · 2026-08-21 21:39:02 UTC

```
Now process_repo and fit_logit/compute_vif functions, then main pipeline execution (sequential, no multiprocessing).
```

### [95] TOOL CALL — NotebookEdit · 2026-08-21 21:39:02 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '92c94db8', 'edit_mode': 'insert', 'cell_type': 'markdown', 'new_source': '## Per-repo processing\\n\\n`process_repo` runs the full strict + relaxed TFDD detection and event-construction pipeline for one repo. The original script parallelizes this across repos with a `ProcessPoolExecutor`; for this small demo (2 repos) we run it as a plain sequential loop below to keep the notebook simple — the per-repo logic itself is unchanged.'}
```

### [96] TOOL RESULT — NotebookEdit · 2026-08-21 21:39:02 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [97] TOOL CALL — NotebookEdit · 2026-08-21 21:39:22 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '0fef9573', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': 'def process_repo(repo_id: str, rep: dict) -> tuple[Optional[TFDDEvent], Optional[TFDDEvent], dict]:\\n    full_name = rep[\\"full_name\\"]\\n    commits = rep[\\"commits\\"]\\n    diag = {\\"repo\\": full_name, \\"stars\\": rep[\\"stars\\"], \\"language\\": rep[\\"language\\"]}\\n    if len(commits) < 20:\\n        diag[\\"status\\"] = \\"too_few_commits\\"\\n        return None, None, diag\\n    n_devs_total = len({c[\\"author_email\\"] for c in commits})\\n    if n_devs_total < 2:\\n        diag[\\"status\\"] = \\"single_dev_never_had_team\\"\\n        return None, None, diag\\n    last_commit_date = commits[-1][\\"date\\"]\\n\\n    strict = detect_founder_tfdd(commits)\\n    relaxed = detect_relaxed_tfdd(commits)\\n    created_at = rep[\\"created_at\\"]\\n    license_key = rep[\\"license_key\\"]\\n\\n    def make_event(tfdd_date: datetime, founder: str) -> Optional[TFDDEvent]:\\n        window_start = tfdd_date - timedelta(days=PRE_WINDOW_FAR_DAYS)\\n        window_end = tfdd_date - timedelta(days=PRE_WINDOW_NEAR_DAYS)\\n        if window_start < commits[0][\\"date\\"]:\\n            return None\\n        founder_share, n_diffused = window_metrics(commits, window_start, window_end, founder)\\n        if math.isnan(founder_share):\\n            return None\\n        doa_tfdd = doa_snapshot(commits, tfdd_date)\\n        owners_tfdd = file_owners(doa_tfdd)\\n        devs_before = {c[\\"author_email\\"] for c in commits if c[\\"date\\"] <= tfdd_date}\\n        commits_before = [c for c in commits if c[\\"date\\"] <= tfdd_date]\\n        ev = TFDDEvent(\\n            repo=full_name,\\n            founder=founder,\\n            tfdd_date=tfdd_date,\\n            repo_created_at=created_at,\\n            stars=rep[\\"stars\\"] or 0,\\n            forks=rep[\\"forks\\"] or 0,\\n            language=rep[\\"language\\"] or \\"unknown\\",\\n            license_key=license_key,\\n            n_commits_total=len(commits),\\n            devs_at_tfdd=len(devs_before),\\n            commits_at_tfdd=len(commits_before),\\n            files_at_tfdd=len(owners_tfdd),\\n            founder_share=founder_share,\\n            n_diffused_owners=n_diffused,\\n            devs_seen_up_to_tfdd=len(devs_before),\\n        )\\n        placebo_window = sample_placebo_window(commits, window_start, window_end)\\n        if placebo_window:\\n            p_share, p_diff = window_metrics(commits, placebo_window[0], placebo_window[1], founder)\\n            ev.placebo_founder_share = p_share\\n            ev.placebo_n_diffused_owners = p_diff\\n        label_survival(commits, ev, last_commit_date)\\n        ev.medappa_ratio, ev.timing_term = compute_medappa_and_timing(commits, founder, tfdd_date, window_start, window_end)\\n        return ev\\n\\n    strict_event = make_event(strict[0], strict[1]) if strict else None\\n    relaxed_event = None\\n    if relaxed:\\n        r_date, r_set = relaxed\\n        counts = Counter(c[\\"author_email\\"] for c in commits if c[\\"author_email\\"] in r_set)\\n        dominant = counts.most_common(1)[0][0] if counts else r_set[0]\\n        relaxed_event = make_event(r_date, dominant)\\n        if relaxed_event is not None:\\n            relaxed_event.tf_set_size_at_relaxed = len(r_set)\\n\\n    diag[\\"status\\"] = \\"ok\\"\\n    diag[\\"n_commits\\"] = len(commits)\\n    diag[\\"n_devs\\"] = n_devs_total\\n    diag[\\"strict_tfdd_found\\"] = strict_event is not None\\n    diag[\\"relaxed_tfdd_found\\"] = relaxed_event is not None\\n    diag[\\"dominant_founder_first_window_share\\"] = rep.get(\\"dominant_founder_first_window_share\\")\\n    return strict_event, relaxed_event, diag\\n\\n\\ndef fit_logit(df_in: pd.DataFrame, cols: list[str], label: str) -> dict:\\n    if df_in.empty or df_in[\\"survived\\"].nunique() < 2 or len(df_in) < len(cols) + 3:\\n        return {\\"status\\": \\"insufficient_data\\", \\"n\\": int(len(df_in)), \\"n_classes\\": int(df_in[\\"survived\\"].nunique()) if not df_in.empty else 0}\\n    X = df_in[cols].astype(float)\\n    y = df_in[\\"survived\\"].astype(int)\\n    X_const = sm.add_constant(X, has_constant=\\"add\\")\\n    try:\\n        model = sm.Logit(y, X_const).fit(disp=0, maxiter=200)\\n    except Exception as e:\\n        logger.warning(f\\"[{label}] logit failed ({e}); dropping lowest-priority covariates in order\\")\\n        drop_order = [\\"license_key\\", \\"contributor_count\\", \\"medappa_ratio:timing_term\\", \\"timing_term\\"]\\n        parsimonious = [c for c in cols if c not in drop_order]\\n        if not parsimonious or set(parsimonious) == set(cols):\\n            return {\\"status\\": f\\"failed:{e}\\", \\"n\\": int(len(df_in))}\\n        return fit_logit(df_in, parsimonious, label + \\"_parsimonious\\")\\n    std_X = (X - X.mean()) / X.std(ddof=0).replace(0, 1)\\n    std_X_const = sm.add_constant(std_X, has_constant=\\"add\\")\\n    try:\\n        std_model = sm.Logit(y, std_X_const).fit(disp=0, maxiter=200)\\n        std_effects = std_model.params.drop(\\"const\\").to_dict()\\n    except Exception:\\n        std_effects = {}\\n    return {\\n        \\"status\\": \\"ok\\",\\n        \\"n\\": int(len(df_in)),\\n        \\"covariates\\": cols,\\n        \\"coefs\\": model.params.to_dict(),\\n        \\"pvalues\\": model.pvalues.to_dict(),\\n        \\"pvalues_bh\\": benjamini_hochberg(model.pvalues.drop(\\"const\\").to_dict()),\\n        \\"standardized_effect_sizes\\": std_effects,\\n        \\"pseudo_r2\\": float(model.prsquared),\\n        \\"converged\\": bool(model.mle_retvals.get(\\"converged\\", True)),\\n    }\\n\\n\\ndef compute_vif(df_in: pd.DataFrame, cols: list[str]) -> dict:\\n    if df_in.empty or len(df_in) < len(cols) + 2:\\n        return {\\"status\\": \\"insufficient_data\\"}\\n    X = sm.add_constant(df_in[cols].astype(float), has_constant=\\"add\\")\\n    vifs = {}\\n    for i, c in enumerate(X.columns):\\n        if c == \\"const\\":\\n            continue\\n        try:\\n            vifs[c] = float(variance_inflation_factor(X.values, i))\\n        except (ZeroDivisionError, np.linalg.LinAlgError, ValueError):\\n            vifs[c] = float(\\"nan\\")\\n    return vifs'}
```

### [98] TOOL RESULT — NotebookEdit · 2026-08-21 21:39:22 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [99] ASSISTANT · 2026-08-21 21:39:26 UTC

```
Now the main pipeline execution cell (sequential loop over repos).
```

### [100] TOOL CALL — NotebookEdit · 2026-08-21 21:39:26 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '20bbf15e', 'edit_mode': 'insert', 'cell_type': 'markdown', 'new_source': '## Run the pipeline over all demo repos'}
```

### [101] TOOL RESULT — NotebookEdit · 2026-08-21 21:39:26 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [102] TOOL CALL — NotebookEdit · 2026-08-21 21:39:32 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '1cd388cf', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': 't0 = time.time()\\nlogger.info(f\\"=== STEP 1-3: DOA/TF/TFDD pipeline, {n_repo_candidates} repos (sequential in this demo) ===\\")\\nstrict_events: list[dict] = []\\nrelaxed_events: list[dict] = []\\ndiagnostics: list[dict] = []\\nfor i, (repo_id, rep) in enumerate(repos.items(), start=1):\\n    try:\\n        s_ev, r_ev, diag = process_repo(repo_id, rep)\\n    except Exception as e:\\n        logger.error(f\\"[process_repo] {rep.get(\'full_name\')} failed: {e}\\")\\n        s_ev, r_ev, diag = None, None, {\\"repo\\": rep.get(\\"full_name\\"), \\"status\\": f\\"exception:{e}\\"}\\n    diagnostics.append(diag)\\n    if s_ev is not None:\\n        strict_events.append(asdict(s_ev))\\n    if r_ev is not None:\\n        relaxed_events.append(asdict(r_ev))\\n    logger.info(f\\"[step1-3] ({i}/{len(repos)}) {rep[\'full_name\']}: {diag.get(\'status\')}\\")\\n\\nlogger.info(f\\"=== Finished: {len(repos)} repos, {len(strict_events)} strict events, {len(relaxed_events)} relaxed events, {time.time()-t0:.1f}s ===\\")\\ndiag_df = pd.DataFrame(diagnostics)\\ndiag_df'}
```

### [103] TOOL RESULT — NotebookEdit · 2026-08-21 21:39:32 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [104] ASSISTANT · 2026-08-21 21:39:38 UTC

```
Now the results-computation cell (rate summaries, dataframes, regressions, matched pairs, mann-whitney, placebo, reconciliation).
```

### [105] TOOL CALL — NotebookEdit · 2026-08-21 21:39:38 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': 'c8f26f35', 'edit_mode': 'insert', 'cell_type': 'markdown', 'new_source': '## Survival rates and analysis dataframes\\n\\nParse the raw event dicts back into `TFDDEvent` objects, compute unconditioned survival rates for the strict and relaxed criteria, and build the pandas analysis dataframes (log-transformed snapshot covariates, dropping censored events).'}
```

### [106] TOOL RESULT — NotebookEdit · 2026-08-21 21:39:40 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [107] TOOL CALL — NotebookEdit · 2026-08-21 21:39:48 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '4729b415', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': 'n_strict, n_relaxed = len(strict_events), len(relaxed_events)\\n\\ndef parse_events(raw_events: list[dict]) -> list[TFDDEvent]:\\n    out = []\\n    for d in raw_events:\\n        d = dict(d)\\n        d[\\"tfdd_date\\"] = pd.to_datetime(d[\\"tfdd_date\\"], utc=True).to_pydatetime()\\n        d[\\"repo_created_at\\"] = pd.to_datetime(d[\\"repo_created_at\\"], utc=True).to_pydatetime()\\n        out.append(TFDDEvent(**d))\\n    return out\\n\\nstrict_ev_objs = parse_events(strict_events)\\nrelaxed_ev_objs = parse_events(relaxed_events)\\n\\ndef rate_summary(events: list[TFDDEvent]) -> dict:\\n    uncensored = [e for e in events if not e.censored]\\n    if not uncensored:\\n        return {\\"n_events\\": len(events), \\"n_uncensored\\": 0, \\"survival_rate\\": None, \\"n_censored_excluded\\": len(events)}\\n    surv = np.array([1.0 if e.survived else 0.0 for e in uncensored])\\n    return {\\n        \\"n_events\\": len(events),\\n        \\"n_uncensored\\": len(uncensored),\\n        \\"n_censored_excluded\\": len(events) - len(uncensored),\\n        \\"survival_rate\\": float(surv.mean()),\\n        \\"survival_rate_se\\": float(surv.std(ddof=1) / math.sqrt(len(surv))) if len(surv) > 1 else None,\\n    }\\n\\nstrict_rate = rate_summary(strict_ev_objs)\\nrelaxed_rate = rate_summary(relaxed_ev_objs)\\nlogger.info(f\\"[step6] strict founder-only TFDD survival: {strict_rate}\\")\\nlogger.info(f\\"[step6] relaxed TF<=2 TFDD survival: {relaxed_rate}\\")\\n\\ndef events_to_df(events: list[TFDDEvent]) -> pd.DataFrame:\\n    rows = [asdict(e) for e in events if not e.censored]\\n    if not rows:\\n        return pd.DataFrame()\\n    df = pd.DataFrame(rows)\\n    df[\\"log_stars\\"] = np.log1p(df[\\"stars\\"])\\n    df[\\"log_forks\\"] = np.log1p(df[\\"forks\\"])\\n    df[\\"log_devs_at_tfdd\\"] = np.log1p(df[\\"devs_at_tfdd\\"])\\n    df = df.dropna(subset=[\\"founder_share\\", \\"n_diffused_owners\\", \\"log_stars\\", \\"log_forks\\", \\"devs_at_tfdd\\"])\\n    return df\\n\\ndf = events_to_df(strict_ev_objs)\\ndf_relaxed = events_to_df(relaxed_ev_objs)\\nprint(\\"strict analysis rows:\\", len(df), \\"| relaxed analysis rows:\\", len(df_relaxed))\\ndf'}
```

### [108] TOOL RESULT — NotebookEdit · 2026-08-21 21:39:49 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [109] ASSISTANT · 2026-08-21 21:39:54 UTC

```
Now the primary battery cell (regression, matched pairs, mann-whitney, placebo check, reconciliation joint model).
```

### [110] TOOL CALL — NotebookEdit · 2026-08-21 21:39:54 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': 'f057f481', 'edit_mode': 'insert', 'cell_type': 'markdown', 'new_source': "## Primary statistical battery\\n\\nBH-corrected logistic regression of survival on `our_method` (diffusion trajectory + snapshot covariates) vs. a `baseline` (snapshot covariates only), Cohen's d / bootstrap CIs on individual covariates, matched-pairs risk-ratio analysis, and Mann-Whitney tests. With only a handful of demo events these tests will mostly report `insufficient_data` — exactly as the original script does when it lacks statistical power — rather than silently fabricating a result."}
```

### [111] TOOL RESULT — NotebookEdit · 2026-08-21 21:39:55 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [112] TOOL CALL — NotebookEdit · 2026-08-21 21:40:08 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '514f6c62', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': 'results: dict = {\\n    \\"n_repos_input\\": n_repo_candidates,\\n    \\"n_founder_candidates\\": n_repo_candidates,\\n    \\"n_strict_tfdd\\": n_strict,\\n    \\"n_relaxed_tfdd\\": n_relaxed,\\n    \\"target_n\\": TARGET_N_STRICT,\\n    \\"strict_unconditioned_survival\\": strict_rate,\\n    \\"relaxed_unconditioned_survival\\": relaxed_rate,\\n    \\"avelino_et_al_reference_survival_rate\\": AVELINO_REFERENCE_SURVIVAL_RATE,\\n    \\"n_analysis_rows_strict\\": int(len(df)),\\n    \\"n_analysis_rows_relaxed\\": int(len(df_relaxed)),\\n}\\n\\n# ---- primary battery ----\\nour_cols = [\\"founder_share\\", \\"n_diffused_owners\\", \\"log_stars\\", \\"log_forks\\", \\"log_devs_at_tfdd\\"]\\nbaseline_cols = [\\"log_stars\\", \\"log_forks\\", \\"log_devs_at_tfdd\\"]\\nresults[\\"primary_regression\\"] = {\\n    \\"our_method\\": fit_logit(df, our_cols, \\"our_method\\"),\\n    \\"baseline_snapshot_only\\": fit_logit(df, baseline_cols, \\"baseline\\"),\\n}\\nif not df.empty and df[\\"survived\\"].nunique() == 2:\\n    surv_mask = df[\\"survived\\"].astype(bool)\\n    cov_effects = {}\\n    for col in [\\"devs_at_tfdd\\", \\"commits_at_tfdd\\", \\"files_at_tfdd\\", \\"founder_share\\", \\"n_diffused_owners\\"]:\\n        a = df.loc[surv_mask, col].to_numpy(dtype=float)\\n        b = df.loc[~surv_mask, col].to_numpy(dtype=float)\\n        cov_effects[col] = {\\"cohens_d\\": cohens_d(a, b), \\"bootstrap_ci95_mean_diff\\": list(bootstrap_ci_mean_diff(a, b, n_boot=N_BOOT))}\\n    results[\\"primary_regression\\"][\\"snapshot_covariate_effect_sizes\\"] = cov_effects\\nelse:\\n    results[\\"primary_regression\\"][\\"snapshot_covariate_effect_sizes\\"] = {\\"status\\": \\"insufficient_class_variation\\"}\\n\\nmatched_pairs_result = {\\"n_pairs\\": 0}\\nif len(df) >= 6:\\n    pairs = build_matched_pairs(df)\\n    if pairs:\\n        risk_ratio, ci95, degeneracy_note = bootstrap_survival_rate_ratio(pairs, n_boot=N_BOOT)\\n        matched_pairs_result = {\\n            \\"n_pairs\\": len(pairs),\\n            \\"matching\\": \\"strict (exact language + star/fork/devs distance)\\",\\n            \\"risk_ratio_low_vs_high_diffusion\\": risk_ratio,\\n            \\"risk_ratio_ci95\\": list(ci95),\\n            \\"note\\": degeneracy_note or \\"risk_ratio = P(survival|low diffusion) / P(survival|high diffusion); >1 => concentrated founder survives MORE\\",\\n        }\\n    else:\\n        relaxed_pairs = build_matched_pairs_relaxed(df)\\n        if relaxed_pairs:\\n            risk_ratio, ci95, degeneracy_note = bootstrap_survival_rate_ratio(relaxed_pairs, n_boot=N_BOOT)\\n            matched_pairs_result = {\\n                \\"n_pairs\\": len(relaxed_pairs),\\n                \\"matching\\": \\"RELAXED (fallback_plan item 4): same star-stratum only, language dropped as exact match\\",\\n                \\"risk_ratio_low_vs_high_diffusion\\": risk_ratio,\\n                \\"risk_ratio_ci95\\": list(ci95),\\n                \\"note\\": degeneracy_note,\\n            }\\n        else:\\n            matched_pairs_result[\\"note\\"] = \\"ZERO eligible pairs even under relaxed same-stratum matching -- reporting explicitly rather than omitting\\"\\nelse:\\n    matched_pairs_result[\\"note\\"] = \\"insufficient events for matched-pairs analysis (need >=6)\\"\\nresults[\\"matched_pairs\\"] = matched_pairs_result\\n\\nif not df.empty and df[\\"survived\\"].nunique() == 2:\\n    surv_mask = df[\\"survived\\"].astype(bool)\\n    mw = {}\\n    for col in [\\"founder_share\\", \\"n_diffused_owners\\"]:\\n        res = stats.mannwhitneyu(df.loc[surv_mask, col], df.loc[~surv_mask, col], alternative=\\"two-sided\\")\\n        mw[col] = {\\"u_stat\\": float(res.statistic), \\"p\\": float(res.pvalue)}\\n    results[\\"mann_whitney\\"] = mw\\nelse:\\n    results[\\"mann_whitney\\"] = {\\"status\\": \\"insufficient_class_variation\\"}\\n\\nresults[\\"primary_regression\\"]'}
```

### [113] TOOL RESULT — NotebookEdit · 2026-08-21 21:40:08 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [114] ASSISTANT · 2026-08-21 21:40:14 UTC

```
Now placebo check and reconciliation cells.
```

### [115] TOOL CALL — NotebookEdit · 2026-08-21 21:40:14 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '44792ab9', 'edit_mode': 'insert', 'cell_type': 'markdown', 'new_source': "## Placebo / shuffle check\\n\\nRe-fits the regression using the randomly-placed placebo windows instead of the true pre-departure window, then bootstraps (`N_PLACEBO_BOOT` resamples here, 1000 in the original full run) an empirical null distribution for the founder_share coefficient — the true window's coefficient is compared against this null to get an empirical p-value."}
```

### [116] TOOL RESULT — NotebookEdit · 2026-08-21 21:40:17 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [117] TOOL CALL — NotebookEdit · 2026-08-21 21:40:24 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '6eb97a3d', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': 'placebo_df = df.dropna(subset=[\\"placebo_founder_share\\", \\"placebo_n_diffused_owners\\"]).copy()\\nplacebo_cols = [\\"placebo_founder_share\\", \\"placebo_n_diffused_owners\\", \\"log_stars\\", \\"log_forks\\", \\"log_devs_at_tfdd\\"]\\nplacebo_reg = fit_logit(placebo_df, placebo_cols, \\"placebo\\") if len(placebo_df) >= 8 else {\\"status\\": \\"insufficient_data\\", \\"n\\": int(len(placebo_df))}\\ntrue_coef = results[\\"primary_regression\\"][\\"our_method\\"].get(\\"coefs\\", {}).get(\\"founder_share\\") if results[\\"primary_regression\\"][\\"our_method\\"].get(\\"status\\") == \\"ok\\" else None\\nnull_coefs = []\\nif len(placebo_df) >= 8:\\n    for _ in range(N_PLACEBO_BOOT):\\n        boot_idx = np.random.randint(0, len(placebo_df), len(placebo_df))\\n        boot_df = placebo_df.iloc[boot_idx]\\n        r = fit_logit(boot_df, placebo_cols, \\"placebo_boot\\")\\n        if r.get(\\"status\\") == \\"ok\\":\\n            null_coefs.append(r[\\"coefs\\"].get(\\"placebo_founder_share\\", np.nan))\\nnull_coefs = np.array([c for c in null_coefs if not np.isnan(c)])\\nempirical_p = None\\nif true_coef is not None and len(null_coefs) > 10:\\n    empirical_p = float((np.abs(null_coefs) >= abs(true_coef)).mean())\\nresults[\\"placebo_check\\"] = {\\n    \\"n_events_with_placebo_window\\": int(len(placebo_df)),\\n    \\"regression_placebo_window\\": placebo_reg,\\n    \\"true_window_founder_share_coef\\": true_coef,\\n    \\"null_distribution_summary\\": {\\n        \\"n\\": int(len(null_coefs)),\\n        \\"mean\\": float(null_coefs.mean()) if len(null_coefs) else None,\\n        \\"std\\": float(null_coefs.std()) if len(null_coefs) else None,\\n    },\\n    \\"empirical_p\\": empirical_p,\\n}\\n\\nif len(df_relaxed) >= 6 and df_relaxed[\\"survived\\"].nunique() == 2:\\n    results[\\"relaxed_sensitivity_regression\\"] = fit_logit(df_relaxed, our_cols, \\"relaxed_our_method\\")\\nelse:\\n    results[\\"relaxed_sensitivity_regression\\"] = {\\"status\\": \\"insufficient_data\\", \\"n\\": int(len(df_relaxed))}\\n\\nresults[\\"placebo_check\\"]'}
```

### [118] TOOL RESULT — NotebookEdit · 2026-08-21 21:40:25 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [119] ASSISTANT · 2026-08-21 21:40:31 UTC

```
Now the reconciliation model cell.
```

### [120] TOOL CALL — NotebookEdit · 2026-08-21 21:40:31 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': 'bb3bc2a1', 'edit_mode': 'insert', 'cell_type': 'markdown', 'new_source': "## Medappa reconciliation joint model\\n\\nThe new test for this iteration: does `timing_term` moderate or flip the sign of `medappa_ratio`'s association with survival? Reports univariate associations, a VIF collinearity check between `medappa_ratio` and `founder_share`, and the joint logistic model with the `medappa_ratio x timing_term` interaction."}
```

### [121] TOOL RESULT — NotebookEdit · 2026-08-21 21:40:31 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [122] TOOL CALL — NotebookEdit · 2026-08-21 21:40:45 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '326cfeed', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': 'recon_df = df.dropna(subset=[\\"medappa_ratio\\", \\"timing_term\\"]).copy()\\nrecon_df[\\"medappa_x_timing\\"] = recon_df[\\"medappa_ratio\\"] * recon_df[\\"timing_term\\"]\\nreconciliation: dict = {\\"n_events\\": int(len(recon_df))}\\n\\nif len(recon_df) >= 6 and recon_df[\\"survived\\"].nunique() == 2:\\n    univariate = {}\\n    surv_mask = recon_df[\\"survived\\"].astype(bool)\\n    for col in [\\"medappa_ratio\\", \\"timing_term\\", \\"founder_share\\"]:\\n        a = recon_df.loc[surv_mask, col].to_numpy(dtype=float)\\n        b = recon_df.loc[~surv_mask, col].to_numpy(dtype=float)\\n        res = stats.mannwhitneyu(a, b, alternative=\\"two-sided\\") if len(a) >= 1 and len(b) >= 1 else None\\n        univariate[col] = {\\n            \\"cohens_d\\": cohens_d(a, b),\\n            \\"mannwhitney_p\\": float(res.pvalue) if res is not None else None,\\n            \\"mean_survived\\": float(np.nanmean(a)) if len(a) else None,\\n            \\"mean_not_survived\\": float(np.nanmean(b)) if len(b) else None,\\n        }\\n    reconciliation[\\"univariate_associations\\"] = univariate\\n\\n    vif = compute_vif(recon_df, [\\"medappa_ratio\\", \\"founder_share\\"])\\n    reconciliation[\\"vif_medappa_vs_founder_share\\"] = vif\\n    high_vif = isinstance(vif, dict) and any(isinstance(v, float) and v > 10 for v in vif.values())\\n    reconciliation[\\"multicollinearity_flag\\"] = bool(high_vif)\\n\\n    base_reconcile_cols = [\\"founder_share\\", \\"medappa_ratio\\", \\"timing_term\\", \\"medappa_x_timing\\", \\"log_stars\\", \\"log_forks\\", \\"log_devs_at_tfdd\\"]\\n    joint = fit_logit(recon_df, base_reconcile_cols, \\"reconciliation_joint\\")\\n    reconciliation[\\"joint_model\\"] = joint\\n\\n    medappa_only = fit_logit(recon_df, [\\"medappa_ratio\\", \\"log_stars\\", \\"log_forks\\", \\"log_devs_at_tfdd\\"], \\"medappa_alone\\")\\n    reconciliation[\\"medappa_alone_model\\"] = medappa_only\\n    medappa_sign = None\\n    if medappa_only.get(\\"status\\") == \\"ok\\":\\n        medappa_sign = \\"negative\\" if medappa_only[\\"coefs\\"].get(\\"medappa_ratio\\", 0) < 0 else \\"positive\\"\\n    reconciliation[\\"medappa_alone_sign\\"] = medappa_sign\\n    reconciliation[\\"replicates_medappa_negative_direction\\"] = (medappa_sign == \\"negative\\")\\n\\n    interp_parts = []\\n    if high_vif:\\n        interp_parts.append(\\n            \\"VIF>10 between medappa_ratio and founder_share: the two constructs are NOT cleanly separable \\"\\n            f\\"at n={len(recon_df)}; the joint model\'s medappa/founder_share coefficients should not be \\"\\n            \\"interpreted independently. Reporting separate univariate associations as the primary evidence instead.\\"\\n        )\\n    if joint.get(\\"status\\") == \\"ok\\":\\n        interaction_coef = joint[\\"coefs\\"].get(\\"medappa_x_timing\\")\\n        timing_coef = joint[\\"coefs\\"].get(\\"timing_term\\")\\n        interp_parts.append(\\n            f\\"Joint model converged (n={joint[\'n\']}); medappa_ratio coef={joint[\'coefs\'].get(\'medappa_ratio\'):.3f}, \\"\\n            f\\"timing_term coef={timing_coef:.3f}, interaction coef={interaction_coef:.3f}. \\"\\n            + (\\"Timing/interaction term MODERATES or FLIPS the medappa_ratio-alone sign, consistent with the \\"\\n               \\"timing-not-presence reconciliation hypothesis.\\"\\n               if (medappa_sign == \\"negative\\" and interaction_coef is not None and (interaction_coef > 0) != (joint[\\"coefs\\"].get(\\"medappa_ratio\\", 0) > 0))\\n               else \\"Timing/interaction term does NOT clearly flip the medappa_ratio-alone sign at this n; \\"\\n                    \\"underpowered to distinguish timing-driven from presence-driven mechanisms.\\")\\n        )\\n    else:\\n        interp_parts.append(f\\"Joint model did not converge cleanly ({joint.get(\'status\')}); falling back to separate univariate associations per fallback_plan item (5).\\")\\n    reconciliation[\\"interpretation\\"] = \\" \\".join(interp_parts)\\nelse:\\n    reconciliation[\\"status\\"] = \\"insufficient_data_or_class_variation\\"\\n    reconciliation[\\"note\\"] = f\\"n={len(recon_df)} events with complete medappa_ratio/timing_term measurements; need >=6 with both survival classes present\\"\\nresults[\\"reconciliation\\"] = reconciliation\\nresults[\\"runtime_seconds\\"] = time.time() - t0\\nreconciliation'}
```

### [123] TOOL RESULT — NotebookEdit · 2026-08-21 21:40:45 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [124] ASSISTANT · 2026-08-21 21:40:51 UTC

```
Now the final results/visualization cell.
```

### [125] TOOL CALL — NotebookEdit · 2026-08-21 21:40:51 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '8a6164d1', 'edit_mode': 'insert', 'cell_type': 'markdown', 'new_source': '## Results summary\\n\\nA readable summary table of the per-event raw features/outcome, plus a bar chart of pre-departure founder commit share for each detected strict TFDD event, colored by whether the project survived the following 18 months.'}
```

### [126] TOOL RESULT — NotebookEdit · 2026-08-21 21:40:51 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [127] TOOL CALL — NotebookEdit · 2026-08-21 21:41:01 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/code_demo.ipynb', 'cell_id': '028ce6ea', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': 'print(f\\"n_repos_input={n_repo_candidates}  n_strict_tfdd={n_strict}  n_relaxed_tfdd={n_relaxed}  target_n={TARGET_N_STRICT}\\")\\nprint(f\\"strict_unconditioned_survival={strict_rate}\\")\\nprint(f\\"avelino_et_al_reference_survival_rate={AVELINO_REFERENCE_SURVIVAL_RATE}\\")\\nprint(f\\"runtime_seconds={results[\'runtime_seconds\']:.2f}\\")\\n\\nsummary_cols = [\\"repo\\", \\"founder\\", \\"founder_share\\", \\"n_diffused_owners\\", \\"medappa_ratio\\", \\"timing_term\\", \\"stars\\", \\"devs_at_tfdd\\", \\"survived\\", \\"grade\\", \\"censored\\"]\\nif not df.empty:\\n    display_df = df[summary_cols].copy()\\n    print(display_df.to_string(index=False))\\nelse:\\n    display_df = pd.DataFrame(columns=summary_cols)\\n    print(\\"No uncensored strict TFDD events in this demo subset.\\")\\n\\nfig, ax = plt.subplots(figsize=(7, 4))\\nif not display_df.empty:\\n    colors = [\\"#2a9d8f\\" if s else \\"#e76f51\\" for s in display_df[\\"survived\\"]]\\n    labels = [f\\"{r.split(\'/\')[-1]}\\\\n{d.date()}\\" for r, d in zip(display_df[\\"repo\\"], df[\\"tfdd_date\\"])]\\n    ax.bar(range(len(display_df)), display_df[\\"founder_share\\"], color=colors)\\n    ax.set_xticks(range(len(display_df)))\\n    ax.set_xticklabels(labels, rotation=0, fontsize=8)\\n    ax.axhline(AVELINO_REFERENCE_SURVIVAL_RATE, color=\\"gray\\", linestyle=\\"--\\", linewidth=1, label=f\\"Avelino et al. reference survival rate ({AVELINO_REFERENCE_SURVIVAL_RATE})\\")\\n    ax.set_ylabel(\\"pre-departure founder_share (12-6mo window)\\")\\n    ax.set_title(\\"Founder commit share before TFDD, by event outcome\\")\\n    ax.legend(handles=[\\n        plt.Rectangle((0, 0), 1, 1, color=\\"#2a9d8f\\", label=\\"survived\\"),\\n        plt.Rectangle((0, 0), 1, 1, color=\\"#e76f51\\", label=\\"did not survive\\"),\\n    ], fontsize=8)\\nelse:\\n    ax.text(0.5, 0.5, \\"no strict TFDD events detected in this demo subset\\", ha=\\"center\\", va=\\"center\\")\\nplt.tight_layout()\\nplt.show()'}
```

### [128] TOOL RESULT — NotebookEdit · 2026-08-21 21:41:01 UTC

```
[event truncated: exceeded SSE frame limit]
```

### [129] ASSISTANT · 2026-08-21 21:41:05 UTC

```
Notebook is fully built. Now let's test-run it in a clean environment.
```

### [130] TOOL CALL — Bash · 2026-08-21 21:41:05 UTC

```
/usr/local/bin/python3.12 -m venv .nb_env 2>&1 | tail -5 && .nb_env/bin/pip install -q pip jupyter ipykernel 2>&1 | tail -20
```

### [131] TOOL RESULT — Bash · 2026-08-21 21:44:05 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "by4qx7ruy", "timedOutAfterMs": 180000}
```

### [132] ASSISTANT · 2026-08-21 21:44:07 UTC

```
Waiting on the venv setup in background; I'll check back shortly.
```

### [133] TOOL CALL — ToolSearch · 2026-08-21 21:44:07 UTC

```
{'query': 'Monitor', 'max_results': 1}
```

### [134] TOOL RESULT — ToolSearch · 2026-08-21 21:44:07 UTC

```
{"matches": ["Monitor"], "query": "Monitor", "total_deferred_tools": 22}
```

### [135] TOOL CALL — Monitor · 2026-08-21 21:44:09 UTC

```
{'description': 'wait for pip venv setup to finish', 'command': 'until kill -0 $(pgrep -f "pip install -q pip jupyter" | head -1) 2>/dev/null; then :; done 2>/dev/null; while pgrep -f "pip install -q pip jupyter" > /dev/null; do sleep 2; done; echo DONE', 'timeout_ms': 180000, 'persistent': False}
```

### [136] TOOL RESULT — Monitor · 2026-08-21 21:44:09 UTC

```
{"taskId": "bmm7n490z", "timeoutMs": 180000, "persistent": false}
```

### [137] ASSISTANT · 2026-08-21 21:44:11 UTC

```
My monitor script had a bug. Let me just poll the background task directly instead.
```

### [138] TOOL CALL — Bash · 2026-08-21 21:44:11 UTC

```
ls -la /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/.nb_env/bin/ 2>&1 | head -20
```

### [139] TOOL RESULT — Bash · 2026-08-21 21:44:11 UTC

```
{"stdout": "total 2956\ndrwxr-xr-x 2 root root 1001630 Aug 21 21:43 .\ndrwxr-xr-x 7 root root 2004081 Aug 21 21:42 ..\n-rw-r--r-- 1 root root    9033 Aug 21 21:41 Activate.ps1\n-rw-r--r-- 1 root root    2382 Aug 21 21:41 activate\n-rw-r--r-- 1 root root    1030 Aug 21 21:41 activate.csh\n-rw-r--r-- 1 root root    2305 Aug 21 21:41 activate.fish\n-rwxr-xr-x 1 root root     381 Aug 21 21:41 pip\n-rwxr-xr-x 1 root root     381 Aug 21 21:41 pip3\n-rwxr-xr-x 1 root root     381 Aug 21 21:41 pip3.12\nlrwxrwxrwx 1 root root      10 Aug 21 21:41 python -> python3.12\nlrwxrwxrwx 1 root root      10 Aug 21 21:41 python3 -> python3.12\nlrwxrwxrwx 1 root root      25 Aug 21 21:41 python3.12 -> /usr/local/bin/python3.12\n-rwxr-xr-x 1 root root     378 Aug 21 21:43 send2trash\n-rwxr-xr-x 1 root root     376 Aug 21 21:42 wsdump", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [140] ASSISTANT · 2026-08-21 21:44:15 UTC

```
jupyter install still in progress. Let me monitor properly with a correct loop.
```

### [141] TOOL CALL — Monitor · 2026-08-21 21:44:15 UTC

```
{'description': 'wait for jupyter install to finish in .nb_env', 'command': 'cd /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl; while [ ! -f .nb_env/bin/jupyter ]; do sleep 3; done; echo JUPYTER_READY', 'timeout_ms': 300000, 'persistent': False}
```

### [142] TOOL RESULT — Monitor · 2026-08-21 21:44:15 UTC

```
{"taskId": "br7wfm10w", "timeoutMs": 300000, "persistent": false}
```

### [143] ASSISTANT · 2026-08-21 21:44:17 UTC

```
I'll wait for the notification that jupyter is ready.
```

### [144] TOOL CALL — AskUserQuestion · 2026-08-21 21:44:17 UTC

```
{'questions': []}
```

### [145] TOOL RESULT — AskUserQuestion [ERROR] · 2026-08-21 21:44:17 UTC

```
InputValidationError: [
  {
    "origin": "array",
    "code": "too_small",
    "minimum": 1,
    "inclusive": true,
    "path": [
      "questions"
    ],
    "message": "Too small: expected array to have >=1 items"
  }
]
```

### [146] TOOL CALL — Bash · 2026-08-21 21:44:19 UTC

```
sleep 1; echo waiting
```

### [147] TOOL RESULT — Bash · 2026-08-21 21:44:19 UTC

```
{"stdout": "waiting", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [148] TOOL CALL — Bash · 2026-08-21 21:44:23 UTC

```
sleep 1
```

### [149] TOOL RESULT — Bash · 2026-08-21 21:44:23 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [150] ASSISTANT · 2026-08-21 21:44:25 UTC

```
Waiting for the jupyter install to finish in the test venv.
```

### [151] TOOL CALL — Bash · 2026-08-21 21:44:25 UTC

```
sleep 60
```

### [152] TOOL RESULT — Bash [ERROR] · 2026-08-21 21:44:25 UTC

```
Error: Blocked: standalone sleep 60. To wait for a condition, use Monitor with an until-loop (e.g. `until <check>; do sleep 2; done`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block.
```

### [153] ASSISTANT · 2026-08-21 21:44:27 UTC

```
Right, I'll just wait for the Monitor notification without polling.
```

### [154] TOOL CALL — TaskCreate · 2026-08-21 21:44:27 UTC

```
{'tasks': '[{"content":"Test-run notebook in clean .nb_env, fix errors","status":"in_progress","activeForm":"Testing notebook in clean environment"}]'}
```

### [155] TOOL RESULT — TaskCreate [ERROR] · 2026-08-21 21:44:27 UTC

```
InputValidationError: [
  {
    "expected": "string",
    "code": "invalid_type",
    "path": [
      "subject"
    ],
    "message": "Invalid input: expected string, received undefined"
  },
  {
    "expected": "string",
    "code": "invalid_type",
    "path": [
      "description"
    ],
    "message": "Invalid input: expected string, received undefined"
  },
  {
    "code": "unrecognized_keys",
    "keys": [
      "tasks"
    ],
    "path": [],
    "message": "Unrecognized key: \"tasks\""
  }
]
```

### [156] ASSISTANT · 2026-08-21 21:44:27 UTC

```
Skipping task tracking overhead, will just wait for the monitor notification.
```

### [157] SYSTEM-USER prompt · 2026-08-21 21:44:29 UTC

```
<validation-feedback>
Attempt 1 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [158] TOOL CALL — Bash · 2026-08-21 21:44:35 UTC

```
cd /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl
ls .nb_env/bin/jupyter 2>&1
ls -la mini_demo_data.json code_demo.ipynb 2>&1
```

### [159] TOOL RESULT — Bash · 2026-08-21 21:44:37 UTC

```
{"stdout": "ls: cannot access '.nb_env/bin/jupyter': No such file or directory\n-rw-r--r-- 1 root root   53318 Aug 21 21:40 code_demo.ipynb\n-rw-r--r-- 1 root root 1141298 Aug 21 21:35 mini_demo_data.json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [160] TOOL CALL — Bash · 2026-08-21 21:44:39 UTC

```
cd /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl
ls -la .nb_env/bin/ 2>&1 | head -30
echo "---"
ps aux | grep -i pip | grep -v grep
```

### [161] TOOL RESULT — Bash · 2026-08-21 21:44:39 UTC

```
{"stdout": "total 2956\ndrwxr-xr-x 2 root root 1001630 Aug 21 21:43 .\ndrwxr-xr-x 7 root root 2004475 Aug 21 21:42 ..\n-rw-r--r-- 1 root root    9033 Aug 21 21:41 Activate.ps1\n-rw-r--r-- 1 root root    2382 Aug 21 21:41 activate\n-rw-r--r-- 1 root root    1030 Aug 21 21:41 activate.csh\n-rw-r--r-- 1 root root    2305 Aug 21 21:41 activate.fish\n-rwxr-xr-x 1 root root     381 Aug 21 21:41 pip\n-rwxr-xr-x 1 root root     381 Aug 21 21:41 pip3\n-rwxr-xr-x 1 root root     381 Aug 21 21:41 pip3.12\nlrwxrwxrwx 1 root root      10 Aug 21 21:41 python -> python3.12\nlrwxrwxrwx 1 root root      10 Aug 21 21:41 python3 -> python3.12\nlrwxrwxrwx 1 root root      25 Aug 21 21:41 python3.12 -> /usr/local/bin/python3.12\n-rwxr-xr-x 1 root root     378 Aug 21 21:43 send2trash\n-rwxr-xr-x 1 root root     376 Aug 21 21:42 wsdump\n---\nroot         240  0.0  0.0   4492  1536 ?        Ss   21:41   0:00 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1787348120628-0t0f4o.sh 2>/dev/null || true && shopt -u extglob 2>/dev/null || true && { \\builtin unalias -- 'unsetenv'; \\builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval '/usr/local/bin/python3.12 -m venv .nb_env 2>&1 | tail -5 && .nb_env/bin/pip install -q pip jupyter ipykernel 2>&1 | tail -20' < /dev/null && pwd -P >| /tmp/claude-b32e-cwd\nroot         249  5.9  0.0  99212 94840 ?        S    21:41   0:09 /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/.nb_env/bin/python3.12 .nb_env/bin/pip install -q pip jupyter ipykernel", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [162] ASSISTANT · 2026-08-21 21:44:43 UTC

```
It's still installing. Let me write a preliminary output JSON now (files exist) and continue testing in background.
```

### [163] TOOL CALL — Write · 2026-08-21 21:44:43 UTC

```
File: /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/.terminal_claude_agent_struct_out.json

{
  "out_expected_files": {
    "notebook": "code_demo.ipynb",
    "mini_data_file": "mini_demo_data.json"
  }
}
```

### [164] TOOL RESULT — Write · 2026-08-21 21:44:43 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl/.terminal_claude_agent_struct_out.json", "content": "{\n  \"out_expected_files\": {\n    \"notebook\": \"code_demo.ipynb\",\n    \"mini_data_file\": \"mini_demo_data.json\"\n  }\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [165] ASSISTANT · 2026-08-21 21:44:47 UTC

```
Now let's continue waiting for the pip install, then execute the notebook test.
```

### [166] TOOL CALL — Monitor · 2026-08-21 21:44:47 UTC

```
{'description': 'wait for jupyter install to finish in .nb_env', 'command': 'cd /ai-inventor/aii_data/runs/run_r-byUQiUWdrF/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_An3IzNVz6VIl; while [ ! -f .nb_env/bin/jupyter ]; do sleep 3; done; echo JUPYTER_READY', 'timeout_ms': 300000, 'persistent': False}
```

### [167] TOOL RESULT — Monitor · 2026-08-21 21:44:47 UTC

```
{"taskId": "bdx8nkno0", "timeoutMs": 300000, "persistent": false}
```

### [168] ASSISTANT · 2026-08-21 21:44:47 UTC

```
I'll wait for this notification before proceeding.
```
