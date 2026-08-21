# gen_demo_art_dataset_2 — report_results

> Phase: `gen_paper_repo` · `gen_demo_art`
> Run: `iter1_0b7b616dce39` — Does Pre-Departure Authority Diffusion Predict Open-Source Project Survival? A Unified-Corpus Retest with a Window-Boundary-Noise Control
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_demo_art_dataset_2` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-08-21 19:17:05 UTC

```
model: claude-sonnet-5 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
```

### [2] SYSTEM-USER prompt · 2026-08-21 19:17:13 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/`:
GOOD: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/file.py`, `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/results/out.json`
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
id: art_70BX2SQt9m6k
type: dataset
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
out_demo_files:
- path: data.py
  description: Dataset fetching/generation script
</artifact_info>

<github_repo>
Repo URL: https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion
Raw data URL: https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json

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
GITHUB_DATA_URL = "https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json"
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
TODO 6. Verify: (1) code_demo.ipynb contains GITHUB_DATA_URL = "https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json" exactly, (2) mini_demo_data.json exists, (3) uses GitHub URL pattern not just open('mini_demo_data.json').
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

### [3] HUMAN-USER prompt · 2026-08-21 19:17:13 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [4] TOOL CALL — ToolSearch · 2026-08-21 19:17:17 UTC

```
{'query': 'select:NotebookEdit,TaskCreate,TaskUpdate', 'max_results': 5}
```

### [5] TOOL RESULT — ToolSearch · 2026-08-21 19:17:17 UTC

```
{"matches": ["NotebookEdit", "TaskCreate", "TaskUpdate"], "query": "select:NotebookEdit,TaskCreate,TaskUpdate", "total_deferred_tools": 22}
```

### [6] TOOL CALL — Bash · 2026-08-21 19:17:17 UTC

```
ls /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/
```

### [7] TOOL RESULT — Bash · 2026-08-21 19:17:17 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [8] TOOL CALL — Bash · 2026-08-21 19:17:23 UTC

```
WS=/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
mkdir -p "$WS"
ls -la "$WS"
echo "---source---"
SRC=/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
ls -la "$SRC"
```

### [9] TOOL RESULT — Bash · 2026-08-21 19:17:23 UTC

```
{"stdout": "total 2007\ndrwxr-xr-x 2 root root 1004362 Aug 21 19:17 .\ndrwxr-xr-x 5 root root 1005490 Aug 21 19:16 ..\n-rw-r--r-- 1 root root   44671 Aug 21 19:17 .repl_agent.ptylog\n---source---\ntotal 10457\ndrwxr-xr-x 6 root root 2009973 Aug 21 18:13 .\ndrwxr-xr-x 5 root root 2046301 Aug 21 17:43 ..\ndrwxr-xr-x 2 root root   11300 Aug 21 17:52 .claude\n-rw-r--r-- 1 root root 1078148 Aug 21 18:13 .repl_agent.ptylog\n-rw-r--r-- 1 root root    3755 Aug 21 18:13 .terminal_claude_agent_struct_out.json\ndrwxr-xr-x 4 root root 2009525 Aug 21 17:55 .venv\n-rw-r--r-- 1 root root    4570 Aug 21 17:46 data.py\n-rw-r--r-- 1 root root  358318 Aug 21 18:13 full_data_out.json\ndrwxr-xr-x 2 root root 1013603 Aug 21 18:08 logs\n-rw-r--r-- 1 root root   15826 Aug 21 17:46 mine_repo.py\n-rw-r--r-- 1 root root   17194 Aug 21 18:13 mini_data_out.json\n-rw-r--r-- 1 root root   54386 Aug 21 18:13 preview_data_out.json\n-rw-r--r-- 1 root root     380 Aug 21 18:12 pyproject.toml\n-rw-r--r-- 1 root root    3624 Aug 21 18:00 run_mining.py\n-rw-r--r-- 1 root root    4660 Aug 21 17:46 search_candidates.py\ndrwxr-xr-x 4 root root 2000281 Aug 21 18:00 temp\n-rw-r--r-- 1 root root   72332 Aug 21 18:12 uv.lock", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [10] TOOL CALL — Skill · 2026-08-21 19:17:25 UTC

```
aii-colab
```

### [11] TOOL RESULT — Skill · 2026-08-21 19:17:25 UTC

```
{"success": true, "commandName": "aii-colab"}
```

### [12] TOOL CALL — Read · 2026-08-21 19:17:25 UTC

```
/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/data.py
```

### [13] TOOL RESULT — Read · 2026-08-21 19:17:25 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/data.py", "content": "#!/usr/bin/env python3\n\"\"\"Assemble mined repo results into the exp_sel_data_out.json schema:\none dataset group ('founder_departure_tfdd_corpus'), one example per\nqualifying repo. `input` = JSON of pre-TFDD/TFDD-snapshot covariates\n(the predictors); `output` = survival_label (the target). All raw\nper-year DOA/TF tables, TFDD metadata, and post-TFDD monthly series are\ncarried as metadata_* fields so downstream experiment code can recompute\nor verify authority-diffusion trajectories without re-cloning repos.\n\"\"\"\nimport glob\nimport json\nimport sys\nfrom pathlib import Path\n\nfrom loguru import logger\n\nlogger.remove()\nlogger.add(sys.stdout, level=\"INFO\", format=\"{time:HH:mm:ss}|{level:<7}|{message}\")\nlogger.add(\"logs/data.log\", rotation=\"10 MB\", level=\"DEBUG\")\n\nRESULTS_GLOB = \"temp/repo_results/*.json\"\nOUT_PATH = Path(\"full_data_out.json\")\n\n\ndef build_example(r: dict) -> dict:\n    pre = r[\"pre_tfdd_window\"]\n    cov = r[\"tfdd_snapshot_covariates\"]\n    input_features = {\n        \"founder_commit_share_pre_tfdd\": pre[\"founder_commit_share\"],\n        \"n_distinct_new_primary_owners_pre_tfdd\": pre[\"n_distinct_new_primary_owners\"],\n        \"founder_early_authorship_share\": r[\"founder_early_authorship_share\"],\n        \"stars\": cov[\"stars\"],\n        \"forks\": cov[\"forks\"],\n        \"total_contributors\": cov[\"total_contributors\"],\n        \"language\": cov[\"language\"],\n        \"license\": cov[\"license\"],\n        \"project_age_days\": cov[\"project_age_days\"],\n        \"n_commits_total\": r[\"n_commits\"],\n        \"n_files_total\": r[\"n_files\"],\n        \"history_span_years\": r[\"history_span_years\"],\n    }\n    example = {\n        \"input\": json.dumps(input_features, sort_keys=True),\n        \"output\": r[\"survival_label\"],\n        \"metadata_full_name\": r[\"full_name\"],\n        \"metadata_activity_bucket\": r[\"activity_bucket\"],\n        \"metadata_founder\": r[\"founder\"],\n        \"metadata_tfdd\": r[\"tfdd\"],\n        \"metadata_pre_tfdd_window\": pre,\n        \"metadata_tfdd_snapshot_covariates\": cov,\n        \"metadata_yearly_doa_tf_tables\": r[\"yearly_tables\"],\n        \"metadata_post_tfdd_monthly_commits\": r[\"post_tfdd_monthly_commits\"],\n        \"metadata_post_tfdd_months_available\": r[\"post_tfdd_months_available\"],\n        \"metadata_years_after_tfdd\": r[\"years_after_tfdd\"],\n        \"metadata_repo_meta\": r[\"meta\"],\n        \"metadata_repo_first_commit\": r[\"repo_first_commit\"],\n        \"metadata_repo_last_commit\": r[\"repo_last_commit\"],\n        \"metadata_task_type\": \"binary_classification\",\n        \"metadata_n_classes\": 2,\n    }\n    return example\n\n\ndef main():\n    files = sorted(glob.glob(RESULTS_GLOB))\n    logger.info(f\"Found {len(files)} mined repo result files\")\n    qualified = []\n    discard_reasons = {}\n    for f in files:\n        r = json.loads(Path(f).read_text())\n        if r.get(\"status\") == \"qualified\":\n            qualified.append(r)\n        else:\n            reason = r.get(\"discard_reason\", \"unknown\")\n            discard_reasons[reason] = discard_reasons.get(reason, 0) + 1\n    logger.info(f\"Qualified repos: {len(qualified)}\")\n    logger.info(f\"Discard reasons: {json.dumps(discard_reasons, indent=2)}\")\n\n    examples = [build_example(r) for r in qualified]\n    output = {\n        \"metadata\": {\n            \"source\": \"GitHub REST search API (candidate discovery) + git log (--filter=blob:none) \"\n                       \"for full commit history mining\",\n            \"description\": \"Single-founder GitHub repos with founder-only Truck-Factor-Developer-\"\n                            \"Detachment (TFDD) events, per Avelino et al. ICPC'16 (DOA/TF algorithm) \"\n                            \"and Avelino et al. ESEM'19 (TFDD/survival definitions). Each example is \"\n                            \"one qualifying repo; input=pre-TFDD/snapshot covariates, output=survival \"\n                            \"label (Active_survived / Inactive_did_not_survive).\",\n            \"n_qualified\": len(qualified),\n            \"discard_reason_counts\": discard_reasons,\n            \"doa_formula\": \"DOA(d,f) = 3.293 + 1.098*FirstAuthor(d,f) + 0.164*Deliveries(d,f) \"\n                           \"- 0.321*ln(1+Acceptances(d,f))\",\n            \"tf_algorithm\": \"greedy removal of highest-file-count DOA-primary-author while \"\n                            \"remaining-authors' file coverage >= 0.5\",\n        },\n        \"datasets\": [\n            {\"dataset\": \"founder_departure_tfdd_corpus\", \"examples\": examples}\n        ],\n    }\n    OUT_PATH.write_text(json.dumps(output, indent=2))\n    logger.info(f\"Wrote {len(examples)} examples to {OUT_PATH}\")\n\n\nif __name__ == \"__main__\":\n    main()\n", "numLines": 106, "startLine": 1, "totalLines": 106}}
```

### [14] TOOL CALL — Bash · 2026-08-21 19:17:25 UTC

```
SRC=/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
head -c 3000 "$SRC/preview_data_out.json"
```

### [15] TOOL RESULT — Bash · 2026-08-21 19:17:25 UTC

```
{"stdout": "{\n  \"metadata\": {\n    \"source\": \"GitHub REST search API (candidate discovery) + git log (--filter=blob:none) for full commit history mining\",\n    \"description\": \"Single-founder GitHub repos with founder-only Truck-Factor-Developer-Detachment (TFDD) events, per Avelino et al. ICPC'16 (DOA/TF algorithm) and Avelino et al. ESEM'19 (TFDD/survival definitions). Eac...[truncated]\",\n    \"n_qualified\": 62,\n    \"discard_reason_counts\": {\n      \"non_software_repo_low_code_fraction\": 50,\n      \"too_few_commits\": 81,\n      \"right_censored_insufficient_post_tfdd_history\": 31,\n      \"no_qualifying_founder_only_tfdd\": 247,\n      \"mining_artifact_migration_squash\": 39,\n      \"too_large_history\": 10,\n      \"single_developer_only\": 2\n    },\n    \"doa_formula\": \"DOA(d,f) = 3.293 + 1.098*FirstAuthor(d,f) + 0.164*Deliveries(d,f) - 0.321*ln(1+Acceptances(d,f))\",\n    \"tf_algorithm\": \"greedy removal of highest-file-count DOA-primary-author while remaining-authors' file coverage >= 0.5\"\n  },\n  \"datasets\": [\n    {\n      \"dataset\": \"founder_departure_tfdd_corpus\",\n      \"examples\": [\n        {\n          \"input\": \"{\\\"forks\\\": 3444, \\\"founder_commit_share_pre_tfdd\\\": 0.0, \\\"founder_early_authorship_share\\\": 0.98, \\\"history_span_years\\\": 7.52, \\\"language\\\": \\\"Java\\\", \\\"license\\\": \\\"Apache-2.0\\\", \\\"n_commits_total\\\": 504, \\\"n_distin...[truncated]\",\n          \"output\": \"Inactive_did_not_survive\",\n          \"metadata_full_name\": \"Bigkoo/Android-PickerView\",\n          \"metadata_activity_bucket\": \"dormant\",\n          \"metadata_founder\": \"mail:sai.wu@bigkoo.com\",\n          \"metadata_tfdd\": {\n            \"year\": 2017,\n            \"date\": \"2017-12-31T00:00:00+00:00\",\n            \"developer\": \"mail:sai.wu@bigkoo.com\",\n            \"last_commit_date\": \"2016-11-30T09:06:29+00:00\",\n            \"silence_years\": 1.08\n          },\n          \"metadata_pre_tfdd_window\": {\n            \"window_start\": \"2016-12-31T00:00:00+00:00\",\n            \"window_end\": \"2017-12-31T00:00:00+00:00\",\n            \"founder_commit_share\": 0.0,\n            \"n_pre_window_commits\": 326,\n            \"n_distinct_new_primary_owners\": 9\n          },\n          \"metadata_tfdd_snapshot_covariates\": {\n            \"stars\": 13434,\n            \"forks\": 3444,\n            \"total_contributors\": 23,\n            \"language\": \"Java\",\n            \"license\": \"Apache-2.0\",\n            \"project_age_days\": 1098\n          },\n          \"metadata_yearly_doa_tf_tables\": [\n            {\n              \"year\": 2014,\n              \"truck_factor\": 1,\n              \"tf_developers\": [\n                \"mail:sai.wu@bigkoo.com\"\n              ],\n              \"n_files\": 35,\n              \"n_active_authors_in_doa\": 1\n            },\n            {\n              \"year\": 2015,\n              \"truck_factor\": 1,\n              \"tf_developers\": [\n                \"mail:sai.wu@bigkoo.com\"\n              ],\n              \"n_files\": 119,\n              \"n_active_authors_in_doa\": 1\n            },\n            {\n              \"year\": 2016,\n              \"truck_factor\": 1,", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [16] TOOL CALL — Bash · 2026-08-21 19:17:33 UTC

```
SRC=/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
ls "$SRC/temp/repo_results" | head -5
ls "$SRC/temp/repo_results" | wc -l
du -sh "$SRC/temp/repo_results"
python3 -c "
import json
f = '$SRC/temp/repo_results'
import glob
fs = sorted(glob.glob(f+'/*.json'))[:1]
print(fs)
d = json.load(open(fs[0]))
print(list(d.keys()))
print(d.get('status'))
"
```

### [17] TOOL RESULT — Bash · 2026-08-21 19:17:33 UTC

```
{"stdout": "1c7__chinese-independent-developer.json\n5etools-mirror-3__5etools-src.json\nAgentchengfeng__chengfeng-videocut-skills.json\nAlloyTeam__PhyTouch.json\nAnarios__return-youtube-dislike.json\n522\n1.4M\t/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/temp/repo_results\n['/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/temp/repo_results/1c7__chinese-independent-developer.json']\n['full_name', 'status', 'discard_reason']\ndiscarded", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [18] TOOL CALL — Bash · 2026-08-21 19:17:41 UTC

```
SRC=/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
python3 -c "
import json, glob
files = sorted(glob.glob('$SRC/temp/repo_results/*.json'))
qual = []
disc = []
for f in files:
    d = json.load(open(f))
    if d.get('status')=='qualified':
        qual.append(f)
    else:
        disc.append((f, d.get('discard_reason')))
print('qualified', len(qual))
print('discarded', len(disc))
from collections import Counter
print(Counter(r for _,r in disc))
"
```

### [19] TOOL RESULT — Bash · 2026-08-21 19:17:49 UTC

```
{"stdout": "qualified 62\ndiscarded 460\nCounter({'no_qualifying_founder_only_tfdd': 247, 'too_few_commits': 81, 'non_software_repo_low_code_fraction': 50, 'mining_artifact_migration_squash': 39, 'right_censored_insufficient_post_tfdd_history': 31, 'too_large_history': 10, 'single_developer_only': 2})", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [20] ASSISTANT · 2026-08-21 19:17:59 UTC

```
Now let me build the mini_demo_data.json: a mix of qualified repos (diverse survival labels/languages) plus a few discarded ones to show the funnel logic.
```

### [21] TOOL CALL — Bash · 2026-08-21 19:17:59 UTC

```
SRC=/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
WS=/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
python3 -c "
import json, glob, random
random.seed(42)
files = sorted(glob.glob('$SRC/temp/repo_results/*.json'))
qual = []
disc_by_reason = {}
for f in files:
    d = json.load(open(f))
    if d.get('status')=='qualified':
        qual.append(d)
    else:
        r = d.get('discard_reason','unknown')
        disc_by_reason.setdefault(r, []).append(d)

# pick diverse qualified: balance survival labels + languages
active = [d for d in qual if d['survival_label']=='Active_survived']
inactive = [d for d in qual if d['survival_label']=='Inactive_did_not_survive']
random.shuffle(active); random.shuffle(inactive)
picked_qual = active[:10] + inactive[:10]

# pick a few discarded examples, one per reason, to illustrate the funnel
picked_disc = []
for reason, items in disc_by_reason.items():
    picked_disc.append(items[0])

mini_raw = picked_qual + picked_disc
print(len(mini_raw), 'raw repo result records selected')
json.dump(mini_raw, open('$WS/mini_repo_results.json','w'), indent=2)
"
ls -la "$WS"
```

### [22] TOOL RESULT — Bash · 2026-08-21 19:18:03 UTC

```
{"stdout": "27 raw repo result records selected\ntotal 2199\ndrwxr-xr-x 2 root root 1019201 Aug 21 19:18 .\ndrwxr-xr-x 5 root root 1034443 Aug 21 19:16 ..\n-rw-r--r-- 1 root root  105646 Aug 21 19:18 .repl_agent.ptylog\n-rw-r--r-- 1 root root   90976 Aug 21 19:18 mini_repo_results.json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [23] TOOL CALL — Bash · 2026-08-21 19:18:09 UTC

```
WS=/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
mv "$WS/mini_repo_results.json" "$WS/mini_demo_data.json"
python3 -c "
import json
d = json.load(open('$WS/mini_demo_data.json'))
print(len(d))
print(json.dumps(d[0], indent=2)[:1500])
"
wc -c "$WS/mini_demo_data.json"
```

### [24] TOOL RESULT — Bash · 2026-08-21 19:18:09 UTC

```
{"stdout": "27\n{\n  \"full_name\": \"mholt/PapaParse\",\n  \"status\": \"qualified\",\n  \"discard_reason\": null,\n  \"meta\": {\n    \"stars\": 13545,\n    \"forks\": 1185,\n    \"language\": \"JavaScript\",\n    \"license\": \"MIT\",\n    \"created_at\": \"2013-10-07T20:33:21Z\",\n    \"html_url\": \"https://github.com/mholt/PapaParse\"\n  },\n  \"n_commits\": 609,\n  \"n_developers\": 160,\n  \"n_files\": 160,\n  \"repo_first_commit\": \"2013-10-07T20:33:21+00:00\",\n  \"repo_last_commit\": \"2026-08-13T12:36:21+00:00\",\n  \"history_span_years\": 12.85,\n  \"founder\": \"mail:matthew.holt+git@gmail.com\",\n  \"founder_early_authorship_share\": 0.8,\n  \"yearly_tables\": [\n    {\n      \"year\": 2013,\n      \"truck_factor\": 1,\n      \"tf_developers\": [\n        \"mail:matthew.holt+git@gmail.com\"\n      ],\n      \"n_files\": 8,\n      \"n_active_authors_in_doa\": 2\n    },\n    {\n      \"year\": 2014,\n      \"truck_factor\": 1,\n      \"tf_developers\": [\n        \"mail:matthew.holt+git@gmail.com\"\n      ],\n      \"n_files\": 28,\n      \"n_active_authors_in_doa\": 5\n    },\n    {\n      \"year\": 2015,\n      \"truck_factor\": 1,\n      \"tf_developers\": [\n        \"mail:matthew.holt+git@gmail.com\"\n      ],\n      \"n_files\": 30,\n      \"n_active_authors_in_doa\": 7\n    },\n    {\n      \"year\": 2016,\n      \"truck_factor\": 1,\n      \"tf_developers\": [\n        \"mail:matthew.holt+git@gmail.com\"\n      ],\n      \"n_files\": 30,\n      \"n_active_authors_in_doa\": 7\n    },\n    {\n      \"year\": 2017,\n      \"truck_factor\": 1,\n      \"tf_developers\": [\n        \"mail:matthew.holt+git@gmail.com\"\n      ],\n      \"n_files\": 30\n90976 /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/mini_demo_data.json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [25] ASSISTANT · 2026-08-21 19:18:11 UTC

```
Good, 90KB, reasonable size. Now let's build the notebook.
```

### [26] TOOL CALL — Bash · 2026-08-21 19:18:11 UTC

```
WS=/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
python3 -c "
import json
nb = {'cells': [], 'metadata': {'kernelspec': {'display_name':'Python 3','language':'python','name':'python3'}, 'language_info':{'name':'python','version':'3.12'}}, 'nbformat':4, 'nbformat_minor':5}
json.dump(nb, open('$WS/code_demo.ipynb','w'), indent=1)
"
```

### [27] TOOL RESULT — Bash · 2026-08-21 19:18:11 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [28] TOOL CALL — Read · 2026-08-21 19:18:13 UTC

```
/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb
```

### [29] TOOL RESULT — Read · 2026-08-21 19:18:13 UTC

```
{"type": "notebook", "file": {"filePath": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb", "cells": []}}
```

### [30] TOOL CALL — NotebookEdit · 2026-08-21 19:18:23 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb', 'cell_type': 'markdown', 'new_source': '# Founder Departure Survival Corpus\n\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\n\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project\'s sole "truck factor" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC\'16 / ESEM\'19) goes silent. For each mined repository it computes:\n\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\n- A binary survival label: whether the project was still active after the founder\'s departure (`Active_survived`) or not (`Inactive_did_not_survive`)\n\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo\'s commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.'}
```

### [31] TOOL RESULT — NotebookEdit [ERROR] · 2026-08-21 19:18:23 UTC

```
Error: Cell ID must be specified when not inserting a new cell.
```

### [32] TOOL CALL — NotebookEdit · 2026-08-21 19:18:31 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': '# Founder Departure Survival Corpus\n\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\n\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project\'s sole "truck factor" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC\'16 / ESEM\'19) goes silent. For each mined repository it computes:\n\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\n- A binary survival label: whether the project was still active after the founder\'s departure (`Active_survived`) or not (`Inactive_did_not_survive`)\n\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo\'s commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.'}
```

### [33] TOOL RESULT — NotebookEdit · 2026-08-21 19:18:31 UTC

```
{"new_source": "# Founder Departure Survival Corpus\n\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\n\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \"truck factor\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\n\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\n\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "874aa4db", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb", "original_file": "{\n \"cells\": [],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"874aa4db\",\n   \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [34] TOOL CALL — NotebookEdit · 2026-08-21 19:18:35 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb', 'cell_id': '874aa4db', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': "import subprocess, sys\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\n\n# loguru is not pre-installed on Colab\n_pip('loguru')\n\n# matplotlib is pre-installed on Colab; install locally at Colab's exact version\nif 'google.colab' not in sys.modules:\n    _pip('matplotlib==3.10.0')"}
```

### [35] TOOL RESULT — NotebookEdit · 2026-08-21 19:18:35 UTC

```
{"new_source": "import subprocess, sys\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\n\n# loguru is not pre-installed on Colab\n_pip('loguru')\n\n# matplotlib is pre-installed on Colab; install locally at Colab's exact version\nif 'google.colab' not in sys.modules:\n    _pip('matplotlib==3.10.0')", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "71633375", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"874aa4db\",\n   \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"874aa4db\",\n   \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"71633375\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru is not pre-installed on Colab\\n_pip('loguru')\\n\\n# matplotlib is pre-installed on Colab; install locally at Colab's exact version\\nif 'google.colab' not in sys.modules:\\n    _pip('matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [36] TOOL CALL — NotebookEdit · 2026-08-21 19:18:39 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb', 'cell_id': '71633375', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': '# Original imports from data.py, plus matplotlib for the results plot at the end\nimport json\nimport sys\nfrom pathlib import Path\n\nfrom loguru import logger\nimport matplotlib.pyplot as plt\n\nlogger.remove()\nlogger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")'}
```

### [37] TOOL RESULT — NotebookEdit · 2026-08-21 19:18:39 UTC

```
{"new_source": "# Original imports from data.py, plus matplotlib for the results plot at the end\nimport json\nimport sys\nfrom pathlib import Path\n\nfrom loguru import logger\nimport matplotlib.pyplot as plt\n\nlogger.remove()\nlogger.add(sys.stdout, level=\"INFO\", format=\"{time:HH:mm:ss}|{level:<7}|{message}\")", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "d6275476", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"874aa4db\",\n   \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"71633375\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru is not pre-installed on Colab\\n_pip('loguru')\\n\\n# matplotlib is pre-installed on Colab; install locally at Colab's exact version\\nif 'google.colab' not in sys.modules:\\n    _pip('matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"874aa4db\",\n   \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"71633375\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru is not pre-installed on Colab\\n_pip('loguru')\\n\\n# matplotlib is pre-installed on Colab; install locally at Colab's exact version\\nif 'google.colab' not in sys.modules:\\n    _pip('matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"d6275476\",\n   \"source\": \"# Original imports from data.py, plus matplotlib for the results plot at the end\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [38] TOOL CALL — NotebookEdit · 2026-08-21 19:18:45 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb', 'cell_id': 'd6275476', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': "## Load the mined repo results\n\n`mini_demo_data.json` is a curated subset of the raw per-repo mining output — the same shape as the `temp/repo_results/*.json` files that `data.py` normally globs from disk. It's a mix of 20 **qualified** repos (10 that survived their founder's departure, 10 that didn't) plus one example of each **discard reason** the mining funnel applies, so the filtering step below has something to filter.\n\nThe loader tries the GitHub raw URL first (works once this artifact is published) and falls back to the local file (works right now, and in this notebook's own working directory on Colab after uploading the file)."}
```

### [39] TOOL RESULT — NotebookEdit · 2026-08-21 19:18:45 UTC

```
{"new_source": "## Load the mined repo results\n\n`mini_demo_data.json` is a curated subset of the raw per-repo mining output — the same shape as the `temp/repo_results/*.json` files that `data.py` normally globs from disk. It's a mix of 20 **qualified** repos (10 that survived their founder's departure, 10 that didn't) plus one example of each **discard reason** the mining funnel applies, so the filtering step below has something to filter.\n\nThe loader tries the GitHub raw URL first (works once this artifact is published) and falls back to the local file (works right now, and in this notebook's own working directory on Colab after uploading the file).", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "f217b255", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"874aa4db\",\n   \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"71633375\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru is not pre-installed on Colab\\n_pip('loguru')\\n\\n# matplotlib is pre-installed on Colab; install locally at Colab's exact version\\nif 'google.colab' not in sys.modules:\\n    _pip('matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"d6275476\",\n   \"source\": \"# Original imports from data.py, plus matplotlib for the results plot at the end\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"874aa4db\",\n   \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"71633375\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru is not pre-installed on Colab\\n_pip('loguru')\\n\\n# matplotlib is pre-installed on Colab; install locally at Colab's exact version\\nif 'google.colab' not in sys.modules:\\n    _pip('matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"d6275476\",\n   \"source\": \"# Original imports from data.py, plus matplotlib for the results plot at the end\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"f217b255\",\n   \"source\": \"## Load the mined repo results\\n\\n`mini_demo_data.json` is a curated subset of the raw per-repo mining output — the same shape as the `temp/repo_results/*.json` files that `data.py` normally globs from disk. It's a mix of 20 **qualified** repos (10 that survived their founder's departure, 10 that didn't) plus one example of each **discard reason** the mining funnel applies, so the filtering step below has something to filter.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is published) and falls back to the local file (works right now, and in this notebook's own working directory on Colab after uploading the file).\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [40] TOOL CALL — NotebookEdit · 2026-08-21 19:18:49 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb', 'cell_id': 'f217b255', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'GITHUB_DATA_URL = "https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json"\nimport os\n\ndef load_data():\n    try:\n        import urllib.request\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\n            return json.loads(response.read().decode())\n    except Exception:\n        pass\n    if os.path.exists("mini_demo_data.json"):\n        with open("mini_demo_data.json") as f:\n            return json.load(f)\n    raise FileNotFoundError("Could not load mini_demo_data.json")'}
```

### [41] TOOL RESULT — NotebookEdit · 2026-08-21 19:18:49 UTC

```
{"new_source": "GITHUB_DATA_URL = \"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json\"\nimport os\n\ndef load_data():\n    try:\n        import urllib.request\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\n            return json.loads(response.read().decode())\n    except Exception:\n        pass\n    if os.path.exists(\"mini_demo_data.json\"):\n        with open(\"mini_demo_data.json\") as f:\n            return json.load(f)\n    raise FileNotFoundError(\"Could not load mini_demo_data.json\")", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "bd9d9fa6", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"874aa4db\",\n   \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"71633375\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru is not pre-installed on Colab\\n_pip('loguru')\\n\\n# matplotlib is pre-installed on Colab; install locally at Colab's exact version\\nif 'google.colab' not in sys.modules:\\n    _pip('matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"d6275476\",\n   \"source\": \"# Original imports from data.py, plus matplotlib for the results plot at the end\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"f217b255\",\n   \"source\": \"## Load the mined repo results\\n\\n`mini_demo_data.json` is a curated subset of the raw per-repo mining output — the same shape as the `temp/repo_results/*.json` files that `data.py` normally globs from disk. It's a mix of 20 **qualified** repos (10 that survived their founder's departure, 10 that didn't) plus one example of each **discard reason** the mining funnel applies, so the filtering step below has something to filter.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is published) and falls back to the local file (works right now, and in this notebook's own working directory on Colab after uploading the file).\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"874aa4db\",\n   \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"71633375\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru is not pre-installed on Colab\\n_pip('loguru')\\n\\n# matplotlib is pre-installed on Colab; install locally at Colab's exact version\\nif 'google.colab' not in sys.modules:\\n    _pip('matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"d6275476\",\n   \"source\": \"# Original imports from data.py, plus matplotlib for the results plot at the end\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"f217b255\",\n   \"source\": \"## Load the mined repo results\\n\\n`mini_demo_data.json` is a curated subset of the raw per-repo mining output — the same shape as the `temp/repo_results/*.json` files that `data.py` normally globs from disk. It's a mix of 20 **qualified** repos (10 that survived their founder's departure, 10 that didn't) plus one example of each **discard reason** the mining funnel applies, so the filtering step below has something to filter.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is published) and falls back to the local file (works right now, and in this notebook's own working directory on Colab after uploading the file).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"bd9d9fa6\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json\\\"\\nimport os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception:\\n        pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f:\\n            return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [42] TOOL CALL — NotebookEdit · 2026-08-21 19:18:53 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb', 'cell_id': 'bd9d9fa6', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'data = load_data()\nprint(f"Loaded {len(data)} raw repo mining results")'}
```

### [43] TOOL RESULT — NotebookEdit · 2026-08-21 19:18:53 UTC

```
{"new_source": "data = load_data()\nprint(f\"Loaded {len(data)} raw repo mining results\")", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "784b150a", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"874aa4db\",\n   \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"71633375\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru is not pre-installed on Colab\\n_pip('loguru')\\n\\n# matplotlib is pre-installed on Colab; install locally at Colab's exact version\\nif 'google.colab' not in sys.modules:\\n    _pip('matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"d6275476\",\n   \"source\": \"# Original imports from data.py, plus matplotlib for the results plot at the end\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"f217b255\",\n   \"source\": \"## Load the mined repo results\\n\\n`mini_demo_data.json` is a curated subset of the raw per-repo mining output — the same shape as the `temp/repo_results/*.json` files that `data.py` normally globs from disk. It's a mix of 20 **qualified** repos (10 that survived their founder's departure, 10 that didn't) plus one example of each **discard reason** the mining funnel applies, so the filtering step below has something to filter.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is published) and falls back to the local file (works right now, and in this notebook's own working directory on Colab after uploading the file).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"bd9d9fa6\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json\\\"\\nimport os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception:\\n        pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f:\\n            return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"874aa4db\",\n   \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"71633375\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru is not pre-installed on Colab\\n_pip('loguru')\\n\\n# matplotlib is pre-installed on Colab; install locally at Colab's exact version\\nif 'google.colab' not in sys.modules:\\n    _pip('matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"d6275476\",\n   \"source\": \"# Original imports from data.py, plus matplotlib for the results plot at the end\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"f217b255\",\n   \"source\": \"## Load the mined repo results\\n\\n`mini_demo_data.json` is a curated subset of the raw per-repo mining output — the same shape as the `temp/repo_results/*.json` files that `data.py` normally globs from disk. It's a mix of 20 **qualified** repos (10 that survived their founder's departure, 10 that didn't) plus one example of each **discard reason** the mining funnel applies, so the filtering step below has something to filter.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is published) and falls back to the local file (works right now, and in this notebook's own working directory on Colab after uploading the file).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"bd9d9fa6\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json\\\"\\nimport os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception:\\n        pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f:\\n            return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"784b150a\",\n   \"source\": \"data = load_data()\\nprint(f\\\"Loaded {len(data)} raw repo mining results\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [44] ASSISTANT · 2026-08-21 19:18:57 UTC

```
Now the config cell, then the processing cells mirroring `data.py`'s `build_example` and `main` logic.
```

### [45] TOOL CALL — NotebookEdit · 2026-08-21 19:18:57 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb', 'cell_id': '784b150a', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': '## Config\n\nThe original `data.py` has no tunable numeric parameters — it\'s a deterministic assembly/filtering step, not a model with iterations or sample sizes. The one "parameter" is which/how-many raw repo results to process; here that\'s simply all of `data` (the small curated subset loaded above). No other config is needed to reproduce the full logic end-to-end.'}
```

### [46] TOOL RESULT — NotebookEdit · 2026-08-21 19:18:57 UTC

```
{"new_source": "## Config\n\nThe original `data.py` has no tunable numeric parameters — it's a deterministic assembly/filtering step, not a model with iterations or sample sizes. The one \"parameter\" is which/how-many raw repo results to process; here that's simply all of `data` (the small curated subset loaded above). No other config is needed to reproduce the full logic end-to-end.", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "2ca19ee2", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"874aa4db\",\n   \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"71633375\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru is not pre-installed on Colab\\n_pip('loguru')\\n\\n# matplotlib is pre-installed on Colab; install locally at Colab's exact version\\nif 'google.colab' not in sys.modules:\\n    _pip('matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"d6275476\",\n   \"source\": \"# Original imports from data.py, plus matplotlib for the results plot at the end\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"f217b255\",\n   \"source\": \"## Load the mined repo results\\n\\n`mini_demo_data.json` is a curated subset of the raw per-repo mining output — the same shape as the `temp/repo_results/*.json` files that `data.py` normally globs from disk. It's a mix of 20 **qualified** repos (10 that survived their founder's departure, 10 that didn't) plus one example of each **discard reason** the mining funnel applies, so the filtering step below has something to filter.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is published) and falls back to the local file (works right now, and in this notebook's own working directory on Colab after uploading the file).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"bd9d9fa6\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json\\\"\\nimport os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception:\\n        pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f:\\n            return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"784b150a\",\n   \"source\": \"data = load_data()\\nprint(f\\\"Loaded {len(data)} raw repo mining results\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"874aa4db\",\n   \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"71633375\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru is not pre-installed on Colab\\n_pip('loguru')\\n\\n# matplotlib is pre-installed on Colab; install locally at Colab's exact version\\nif 'google.colab' not in sys.modules:\\n    _pip('matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"d6275476\",\n   \"source\": \"# Original imports from data.py, plus matplotlib for the results plot at the end\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"f217b255\",\n   \"source\": \"## Load the mined repo results\\n\\n`mini_demo_data.json` is a curated subset of the raw per-repo mining output — the same shape as the `temp/repo_results/*.json` files that `data.py` normally globs from disk. It's a mix of 20 **qualified** repos (10 that survived their founder's departure, 10 that didn't) plus one example of each **discard reason** the mining funnel applies, so the filtering step below has something to filter.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is published) and falls back to the local file (works right now, and in this notebook's own working directory on Colab after uploading the file).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"bd9d9fa6\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json\\\"\\nimport os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception:\\n        pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f:\\n            return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"784b150a\",\n   \"source\": \"data = load_data()\\nprint(f\\\"Loaded {len(data)} raw repo mining results\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"2ca19ee2\",\n   \"source\": \"## Config\\n\\nThe original `data.py` has no tunable numeric parameters — it's a deterministic assembly/filtering step, not a model with iterations or sample sizes. The one \\\"parameter\\\" is which/how-many raw repo results to process; here that's simply all of `data` (the small curated subset loaded above). No other config is needed to reproduce the full logic end-to-end.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [47] TOOL CALL — NotebookEdit · 2026-08-21 19:19:01 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb', 'cell_id': '2ca19ee2', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': '# Config — process every record in the loaded (curated) mini dataset.\n# In the full pipeline this would instead be every file matched by\n# RESULTS_GLOB = "temp/repo_results/*.json" (all 522 mined candidates).\nraw_results = data'}
```

### [48] TOOL RESULT — NotebookEdit · 2026-08-21 19:19:01 UTC

```
{"new_source": "# Config — process every record in the loaded (curated) mini dataset.\n# In the full pipeline this would instead be every file matched by\n# RESULTS_GLOB = \"temp/repo_results/*.json\" (all 522 mined candidates).\nraw_results = data", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "e0fb48e2", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"874aa4db\",\n   \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"71633375\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru is not pre-installed on Colab\\n_pip('loguru')\\n\\n# matplotlib is pre-installed on Colab; install locally at Colab's exact version\\nif 'google.colab' not in sys.modules:\\n    _pip('matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"d6275476\",\n   \"source\": \"# Original imports from data.py, plus matplotlib for the results plot at the end\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"f217b255\",\n   \"source\": \"## Load the mined repo results\\n\\n`mini_demo_data.json` is a curated subset of the raw per-repo mining output — the same shape as the `temp/repo_results/*.json` files that `data.py` normally globs from disk. It's a mix of 20 **qualified** repos (10 that survived their founder's departure, 10 that didn't) plus one example of each **discard reason** the mining funnel applies, so the filtering step below has something to filter.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is published) and falls back to the local file (works right now, and in this notebook's own working directory on Colab after uploading the file).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"bd9d9fa6\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json\\\"\\nimport os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception:\\n        pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f:\\n            return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"784b150a\",\n   \"source\": \"data = load_data()\\nprint(f\\\"Loaded {len(data)} raw repo mining results\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"2ca19ee2\",\n   \"source\": \"## Config\\n\\nThe original `data.py` has no tunable numeric parameters — it's a deterministic assembly/filtering step, not a model with iterations or sample sizes. The one \\\"parameter\\\" is which/how-many raw repo results to process; here that's simply all of `data` (the small curated subset loaded above). No other config is needed to reproduce the full logic end-to-end.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"874aa4db\",\n   \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"71633375\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru is not pre-installed on Colab\\n_pip('loguru')\\n\\n# matplotlib is pre-installed on Colab; install locally at Colab's exact version\\nif 'google.colab' not in sys.modules:\\n    _pip('matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"d6275476\",\n   \"source\": \"# Original imports from data.py, plus matplotlib for the results plot at the end\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"f217b255\",\n   \"source\": \"## Load the mined repo results\\n\\n`mini_demo_data.json` is a curated subset of the raw per-repo mining output — the same shape as the `temp/repo_results/*.json` files that `data.py` normally globs from disk. It's a mix of 20 **qualified** repos (10 that survived their founder's departure, 10 that didn't) plus one example of each **discard reason** the mining funnel applies, so the filtering step below has something to filter.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is published) and falls back to the local file (works right now, and in this notebook's own working directory on Colab after uploading the file).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"bd9d9fa6\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json\\\"\\nimport os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception:\\n        pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f:\\n            return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"784b150a\",\n   \"source\": \"data = load_data()\\nprint(f\\\"Loaded {len(data)} raw repo mining results\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"2ca19ee2\",\n   \"source\": \"## Config\\n\\nThe original `data.py` has no tunable numeric parameters — it's a deterministic assembly/filtering step, not a model with iterations or sample sizes. The one \\\"parameter\\\" is which/how-many raw repo results to process; here that's simply all of `data` (the small curated subset loaded above). No other config is needed to reproduce the full logic end-to-end.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"e0fb48e2\",\n   \"source\": \"# Config — process every record in the loaded (curated) mini dataset.\\n# In the full pipeline this would instead be every file matched by\\n# RESULTS_GLOB = \\\"temp/repo_results/*.json\\\" (all 522 mined candidates).\\nraw_results = data\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [49] ASSISTANT · 2026-08-21 19:19:05 UTC

```
Now the `build_example` function (copied as-is from data.py):
```

### [50] TOOL CALL — NotebookEdit · 2026-08-21 19:19:05 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb', 'cell_id': 'e0fb48e2', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': "## Build one dataset example per qualifying repo\n\n`build_example` is copied unchanged from `data.py`. For a qualifying repo it pulls the pre-TFDD authority-diffusion window (`pre`) and the TFDD-snapshot covariates (`cov`) out of the raw mining result, packs the predictors into `input` (a JSON string, matching the corpus's on-disk format), and carries every other field through as `metadata_*` so downstream analysis can recompute alternate windows without re-mining."}
```

### [51] TOOL RESULT — NotebookEdit · 2026-08-21 19:19:05 UTC

```
{"new_source": "## Build one dataset example per qualifying repo\n\n`build_example` is copied unchanged from `data.py`. For a qualifying repo it pulls the pre-TFDD authority-diffusion window (`pre`) and the TFDD-snapshot covariates (`cov`) out of the raw mining result, packs the predictors into `input` (a JSON string, matching the corpus's on-disk format), and carries every other field through as `metadata_*` so downstream analysis can recompute alternate windows without re-mining.", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "5bd767ed", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"874aa4db\",\n   \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"71633375\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru is not pre-installed on Colab\\n_pip('loguru')\\n\\n# matplotlib is pre-installed on Colab; install locally at Colab's exact version\\nif 'google.colab' not in sys.modules:\\n    _pip('matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"d6275476\",\n   \"source\": \"# Original imports from data.py, plus matplotlib for the results plot at the end\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"f217b255\",\n   \"source\": \"## Load the mined repo results\\n\\n`mini_demo_data.json` is a curated subset of the raw per-repo mining output — the same shape as the `temp/repo_results/*.json` files that `data.py` normally globs from disk. It's a mix of 20 **qualified** repos (10 that survived their founder's departure, 10 that didn't) plus one example of each **discard reason** the mining funnel applies, so the filtering step below has something to filter.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is published) and falls back to the local file (works right now, and in this notebook's own working directory on Colab after uploading the file).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"bd9d9fa6\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json\\\"\\nimport os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception:\\n        pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f:\\n            return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"784b150a\",\n   \"source\": \"data = load_data()\\nprint(f\\\"Loaded {len(data)} raw repo mining results\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"2ca19ee2\",\n   \"source\": \"## Config\\n\\nThe original `data.py` has no tunable numeric parameters — it's a deterministic assembly/filtering step, not a model with iterations or sample sizes. The one \\\"parameter\\\" is which/how-many raw repo results to process; here that's simply all of `data` (the small curated subset loaded above). No other config is needed to reproduce the full logic end-to-end.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"e0fb48e2\",\n   \"source\": \"# Config — process every record in the loaded (curated) mini dataset.\\n# In the full pipeline this would instead be every file matched by\\n# RESULTS_GLOB = \\\"temp/repo_results/*.json\\\" (all 522 mined candidates).\\nraw_results = data\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"874aa4db\",\n   \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"71633375\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru is not pre-installed on Colab\\n_pip('loguru')\\n\\n# matplotlib is pre-installed on Colab; install locally at Colab's exact version\\nif 'google.colab' not in sys.modules:\\n    _pip('matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"d6275476\",\n   \"source\": \"# Original imports from data.py, plus matplotlib for the results plot at the end\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"f217b255\",\n   \"source\": \"## Load the mined repo results\\n\\n`mini_demo_data.json` is a curated subset of the raw per-repo mining output — the same shape as the `temp/repo_results/*.json` files that `data.py` normally globs from disk. It's a mix of 20 **qualified** repos (10 that survived their founder's departure, 10 that didn't) plus one example of each **discard reason** the mining funnel applies, so the filtering step below has something to filter.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is published) and falls back to the local file (works right now, and in this notebook's own working directory on Colab after uploading the file).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"bd9d9fa6\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json\\\"\\nimport os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception:\\n        pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f:\\n            return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"784b150a\",\n   \"source\": \"data = load_data()\\nprint(f\\\"Loaded {len(data)} raw repo mining results\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"2ca19ee2\",\n   \"source\": \"## Config\\n\\nThe original `data.py` has no tunable numeric parameters — it's a deterministic assembly/filtering step, not a model with iterations or sample sizes. The one \\\"parameter\\\" is which/how-many raw repo results to process; here that's simply all of `data` (the small curated subset loaded above). No other config is needed to reproduce the full logic end-to-end.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"e0fb48e2\",\n   \"source\": \"# Config — process every record in the loaded (curated) mini dataset.\\n# In the full pipeline this would instead be every file matched by\\n# RESULTS_GLOB = \\\"temp/repo_results/*.json\\\" (all 522 mined candidates).\\nraw_results = data\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"5bd767ed\",\n   \"source\": \"## Build one dataset example per qualifying repo\\n\\n`build_example` is copied unchanged from `data.py`. For a qualifying repo it pulls the pre-TFDD authority-diffusion window (`pre`) and the TFDD-snapshot covariates (`cov`) out of the raw mining result, packs the predictors into `input` (a JSON string, matching the corpus's on-disk format), and carries every other field through as `metadata_*` so downstream analysis can recompute alternate windows without re-mining.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [52] TOOL CALL — NotebookEdit · 2026-08-21 19:19:13 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb', 'cell_id': '5bd767ed', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'def build_example(r: dict) -> dict:\n    pre = r["pre_tfdd_window"]\n    cov = r["tfdd_snapshot_covariates"]\n    input_features = {\n        "founder_commit_share_pre_tfdd": pre["founder_commit_share"],\n        "n_distinct_new_primary_owners_pre_tfdd": pre["n_distinct_new_primary_owners"],\n        "founder_early_authorship_share": r["founder_early_authorship_share"],\n        "stars": cov["stars"],\n        "forks": cov["forks"],\n        "total_contributors": cov["total_contributors"],\n        "language": cov["language"],\n        "license": cov["license"],\n        "project_age_days": cov["project_age_days"],\n        "n_commits_total": r["n_commits"],\n        "n_files_total": r["n_files"],\n        "history_span_years": r["history_span_years"],\n    }\n    example = {\n        "input": json.dumps(input_features, sort_keys=True),\n        "output": r["survival_label"],\n        "metadata_full_name": r["full_name"],\n        "metadata_activity_bucket": r["activity_bucket"],\n        "metadata_founder": r["founder"],\n        "metadata_tfdd": r["tfdd"],\n        "metadata_pre_tfdd_window": pre,\n        "metadata_tfdd_snapshot_covariates": cov,\n        "metadata_yearly_doa_tf_tables": r["yearly_tables"],\n        "metadata_post_tfdd_monthly_commits": r["post_tfdd_monthly_commits"],\n        "metadata_post_tfdd_months_available": r["post_tfdd_months_available"],\n        "metadata_years_after_tfdd": r["years_after_tfdd"],\n        "metadata_repo_meta": r["meta"],\n        "metadata_repo_first_commit": r["repo_first_commit"],\n        "metadata_repo_last_commit": r["repo_last_commit"],\n        "metadata_task_type": "binary_classification",\n        "metadata_n_classes": 2,\n    }\n    return example'}
```

### [53] TOOL RESULT — NotebookEdit · 2026-08-21 19:19:13 UTC

```
{"new_source": "def build_example(r: dict) -> dict:\n    pre = r[\"pre_tfdd_window\"]\n    cov = r[\"tfdd_snapshot_covariates\"]\n    input_features = {\n        \"founder_commit_share_pre_tfdd\": pre[\"founder_commit_share\"],\n        \"n_distinct_new_primary_owners_pre_tfdd\": pre[\"n_distinct_new_primary_owners\"],\n        \"founder_early_authorship_share\": r[\"founder_early_authorship_share\"],\n        \"stars\": cov[\"stars\"],\n        \"forks\": cov[\"forks\"],\n        \"total_contributors\": cov[\"total_contributors\"],\n        \"language\": cov[\"language\"],\n        \"license\": cov[\"license\"],\n        \"project_age_days\": cov[\"project_age_days\"],\n        \"n_commits_total\": r[\"n_commits\"],\n        \"n_files_total\": r[\"n_files\"],\n        \"history_span_years\": r[\"history_span_years\"],\n    }\n    example = {\n        \"input\": json.dumps(input_features, sort_keys=True),\n        \"output\": r[\"survival_label\"],\n        \"metadata_full_name\": r[\"full_name\"],\n        \"metadata_activity_bucket\": r[\"activity_bucket\"],\n        \"metadata_founder\": r[\"founder\"],\n        \"metadata_tfdd\": r[\"tfdd\"],\n        \"metadata_pre_tfdd_window\": pre,\n        \"metadata_tfdd_snapshot_covariates\": cov,\n        \"metadata_yearly_doa_tf_tables\": r[\"yearly_tables\"],\n        \"metadata_post_tfdd_monthly_commits\": r[\"post_tfdd_monthly_commits\"],\n        \"metadata_post_tfdd_months_available\": r[\"post_tfdd_months_available\"],\n        \"metadata_years_after_tfdd\": r[\"years_after_tfdd\"],\n        \"metadata_repo_meta\": r[\"meta\"],\n        \"metadata_repo_first_commit\": r[\"repo_first_commit\"],\n        \"metadata_repo_last_commit\": r[\"repo_last_commit\"],\n        \"metadata_task_type\": \"binary_classification\",\n        \"metadata_n_classes\": 2,\n    }\n    return example", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "ac1eb1ef", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"874aa4db\",\n   \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"71633375\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru is not pre-installed on Colab\\n_pip('loguru')\\n\\n# matplotlib is pre-installed on Colab; install locally at Colab's exact version\\nif 'google.colab' not in sys.modules:\\n    _pip('matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"d6275476\",\n   \"source\": \"# Original imports from data.py, plus matplotlib for the results plot at the end\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"f217b255\",\n   \"source\": \"## Load the mined repo results\\n\\n`mini_demo_data.json` is a curated subset of the raw per-repo mining output — the same shape as the `temp/repo_results/*.json` files that `data.py` normally globs from disk. It's a mix of 20 **qualified** repos (10 that survived their founder's departure, 10 that didn't) plus one example of each **discard reason** the mining funnel applies, so the filtering step below has something to filter.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is published) and falls back to the local file (works right now, and in this notebook's own working directory on Colab after uploading the file).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"bd9d9fa6\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json\\\"\\nimport os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception:\\n        pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f:\\n            return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"784b150a\",\n   \"source\": \"data = load_data()\\nprint(f\\\"Loaded {len(data)} raw repo mining results\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"2ca19ee2\",\n   \"source\": \"## Config\\n\\nThe original `data.py` has no tunable numeric parameters — it's a deterministic assembly/filtering step, not a model with iterations or sample sizes. The one \\\"parameter\\\" is which/how-many raw repo results to process; here that's simply all of `data` (the small curated subset loaded above). No other config is needed to reproduce the full logic end-to-end.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"e0fb48e2\",\n   \"source\": \"# Config — process every record in the loaded (curated) mini dataset.\\n# In the full pipeline this would instead be every file matched by\\n# RESULTS_GLOB = \\\"temp/repo_results/*.json\\\" (all 522 mined candidates).\\nraw_results = data\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"5bd767ed\",\n   \"source\": \"## Build one dataset example per qualifying repo\\n\\n`build_example` is copied unchanged from `data.py`. For a qualifying repo it pulls the pre-TFDD authority-diffusion window (`pre`) and the TFDD-snapshot covariates (`cov`) out of the raw mining result, packs the predictors into `input` (a JSON string, matching the corpus's on-disk format), and carries every other field through as `metadata_*` so downstream analysis can recompute alternate windows without re-mining.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"874aa4db\",\n   \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"71633375\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru is not pre-installed on Colab\\n_pip('loguru')\\n\\n# matplotlib is pre-installed on Colab; install locally at Colab's exact version\\nif 'google.colab' not in sys.modules:\\n    _pip('matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"d6275476\",\n   \"source\": \"# Original imports from data.py, plus matplotlib for the results plot at the end\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"f217b255\",\n   \"source\": \"## Load the mined repo results\\n\\n`mini_demo_data.json` is a curated subset of the raw per-repo mining output — the same shape as the `temp/repo_results/*.json` files that `data.py` normally globs from disk. It's a mix of 20 **qualified** repos (10 that survived their founder's departure, 10 that didn't) plus one example of each **discard reason** the mining funnel applies, so the filtering step below has something to filter.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is published) and falls back to the local file (works right now, and in this notebook's own working directory on Colab after uploading the file).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"bd9d9fa6\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json\\\"\\nimport os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception:\\n        pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f:\\n            return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"784b150a\",\n   \"source\": \"data = load_data()\\nprint(f\\\"Loaded {len(data)} raw repo mining results\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"2ca19ee2\",\n   \"source\": \"## Config\\n\\nThe original `data.py` has no tunable numeric parameters — it's a deterministic assembly/filtering step, not a model with iterations or sample sizes. The one \\\"parameter\\\" is which/how-many raw repo results to process; here that's simply all of `data` (the small curated subset loaded above). No other config is needed to reproduce the full logic end-to-end.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"e0fb48e2\",\n   \"source\": \"# Config — process every record in the loaded (curated) mini dataset.\\n# In the full pipeline this would instead be every file matched by\\n# RESULTS_GLOB = \\\"temp/repo_results/*.json\\\" (all 522 mined candidates).\\nraw_results = data\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"5bd767ed\",\n   \"source\": \"## Build one dataset example per qualifying repo\\n\\n`build_example` is copied unchanged from `data.py`. For a qualifying repo it pulls the pre-TFDD authority-diffusion window (`pre`) and the TFDD-snapshot covariates (`cov`) out of the raw mining result, packs the predictors into `input` (a JSON string, matching the corpus's on-disk format), and carries every other field through as `metadata_*` so downstream analysis can recompute alternate windows without re-mining.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"ac1eb1ef\",\n   \"source\": \"def build_example(r: dict) -> dict:\\n    pre = r[\\\"pre_tfdd_window\\\"]\\n    cov = r[\\\"tfdd_snapshot_covariates\\\"]\\n    input_features = {\\n        \\\"founder_commit_share_pre_tfdd\\\": pre[\\\"founder_commit_share\\\"],\\n        \\\"n_distinct_new_primary_owners_pre_tfdd\\\": pre[\\\"n_distinct_new_primary_owners\\\"],\\n        \\\"founder_early_authorship_share\\\": r[\\\"founder_early_authorship_share\\\"],\\n        \\\"stars\\\": cov[\\\"stars\\\"],\\n        \\\"forks\\\": cov[\\\"forks\\\"],\\n        \\\"total_contributors\\\": cov[\\\"total_contributors\\\"],\\n        \\\"language\\\": cov[\\\"language\\\"],\\n        \\\"license\\\": cov[\\\"license\\\"],\\n        \\\"project_age_days\\\": cov[\\\"project_age_days\\\"],\\n        \\\"n_commits_total\\\": r[\\\"n_commits\\\"],\\n        \\\"n_files_total\\\": r[\\\"n_files\\\"],\\n        \\\"history_span_years\\\": r[\\\"history_span_years\\\"],\\n    }\\n    example = {\\n        \\\"input\\\": json.dumps(input_features, sort_keys=True),\\n        \\\"output\\\": r[\\\"survival_label\\\"],\\n        \\\"metadata_full_name\\\": r[\\\"full_name\\\"],\\n        \\\"metadata_activity_bucket\\\": r[\\\"activity_bucket\\\"],\\n        \\\"metadata_founder\\\": r[\\\"founder\\\"],\\n        \\\"metadata_tfdd\\\": r[\\\"tfdd\\\"],\\n        \\\"metadata_pre_tfdd_window\\\": pre,\\n        \\\"metadata_tfdd_snapshot_covariates\\\": cov,\\n        \\\"metadata_yearly_doa_tf_tables\\\": r[\\\"yearly_tables\\\"],\\n        \\\"metadata_post_tfdd_monthly_commits\\\": r[\\\"post_tfdd_monthly_commits\\\"],\\n        \\\"metadata_post_tfdd_months_available\\\": r[\\\"post_tfdd_months_available\\\"],\\n        \\\"metadata_years_after_tfdd\\\": r[\\\"years_after_tfdd\\\"],\\n        \\\"metadata_repo_meta\\\": r[\\\"meta\\\"],\\n        \\\"metadata_repo_first_commit\\\": r[\\\"repo_first_commit\\\"],\\n        \\\"metadata_repo_last_commit\\\": r[\\\"repo_last_commit\\\"],\\n        \\\"metadata_task_type\\\": \\\"binary_classification\\\",\\n        \\\"metadata_n_classes\\\": 2,\\n    }\\n    return example\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [54] ASSISTANT · 2026-08-21 19:19:19 UTC

```
Now the `main()` filtering logic, adapted minimally to work over the in-memory `raw_results` list instead of globbing files:
```

### [55] TOOL CALL — NotebookEdit · 2026-08-21 19:19:19 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb', 'cell_id': 'ac1eb1ef', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': "## Filter to qualifying repos and assemble the corpus\n\nThis mirrors `data.py`'s `main()`. The only change from the original is the source of the raw results: instead of `glob.glob(RESULTS_GLOB)` reading `temp/repo_results/*.json` off disk, we iterate the `raw_results` list already loaded into memory (each element is exactly one of those per-repo JSON files' contents). Everything else — the qualified/discarded split, the discard-reason tally, and the final `output` dict with its `metadata` block — is unchanged."}
```

### [56] TOOL RESULT — NotebookEdit · 2026-08-21 19:19:19 UTC

```
{"new_source": "## Filter to qualifying repos and assemble the corpus\n\nThis mirrors `data.py`'s `main()`. The only change from the original is the source of the raw results: instead of `glob.glob(RESULTS_GLOB)` reading `temp/repo_results/*.json` off disk, we iterate the `raw_results` list already loaded into memory (each element is exactly one of those per-repo JSON files' contents). Everything else — the qualified/discarded split, the discard-reason tally, and the final `output` dict with its `metadata` block — is unchanged.", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "fb2272b8", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"874aa4db\",\n   \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"71633375\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru is not pre-installed on Colab\\n_pip('loguru')\\n\\n# matplotlib is pre-installed on Colab; install locally at Colab's exact version\\nif 'google.colab' not in sys.modules:\\n    _pip('matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"d6275476\",\n   \"source\": \"# Original imports from data.py, plus matplotlib for the results plot at the end\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"f217b255\",\n   \"source\": \"## Load the mined repo results\\n\\n`mini_demo_data.json` is a curated subset of the raw per-repo mining output — the same shape as the `temp/repo_results/*.json` files that `data.py` normally globs from disk. It's a mix of 20 **qualified** repos (10 that survived their founder's departure, 10 that didn't) plus one example of each **discard reason** the mining funnel applies, so the filtering step below has something to filter.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is published) and falls back to the local file (works right now, and in this notebook's own working directory on Colab after uploading the file).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"bd9d9fa6\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json\\\"\\nimport os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception:\\n        pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f:\\n            return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"784b150a\",\n   \"source\": \"data = load_data()\\nprint(f\\\"Loaded {len(data)} raw repo mining results\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"2ca19ee2\",\n   \"source\": \"## Config\\n\\nThe original `data.py` has no tunable numeric parameters — it's a deterministic assembly/filtering step, not a model with iterations or sample sizes. The one \\\"parameter\\\" is which/how-many raw repo results to process; here that's simply all of `data` (the small curated subset loaded above). No other config is needed to reproduce the full logic end-to-end.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"e0fb48e2\",\n   \"source\": \"# Config — process every record in the loaded (curated) mini dataset.\\n# In the full pipeline this would instead be every file matched by\\n# RESULTS_GLOB = \\\"temp/repo_results/*.json\\\" (all 522 mined candidates).\\nraw_results = data\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"5bd767ed\",\n   \"source\": \"## Build one dataset example per qualifying repo\\n\\n`build_example` is copied unchanged from `data.py`. For a qualifying repo it pulls the pre-TFDD authority-diffusion window (`pre`) and the TFDD-snapshot covariates (`cov`) out of the raw mining result, packs the predictors into `input` (a JSON string, matching the corpus's on-disk format), and carries every other field through as `metadata_*` so downstream analysis can recompute alternate windows without re-mining.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"ac1eb1ef\",\n   \"source\": \"def build_example(r: dict) -> dict:\\n    pre = r[\\\"pre_tfdd_window\\\"]\\n    cov = r[\\\"tfdd_snapshot_covariates\\\"]\\n    input_features = {\\n        \\\"founder_commit_share_pre_tfdd\\\": pre[\\\"founder_commit_share\\\"],\\n        \\\"n_distinct_new_primary_owners_pre_tfdd\\\": pre[\\\"n_distinct_new_primary_owners\\\"],\\n        \\\"founder_early_authorship_share\\\": r[\\\"founder_early_authorship_share\\\"],\\n        \\\"stars\\\": cov[\\\"stars\\\"],\\n        \\\"forks\\\": cov[\\\"forks\\\"],\\n        \\\"total_contributors\\\": cov[\\\"total_contributors\\\"],\\n        \\\"language\\\": cov[\\\"language\\\"],\\n        \\\"license\\\": cov[\\\"license\\\"],\\n        \\\"project_age_days\\\": cov[\\\"project_age_days\\\"],\\n        \\\"n_commits_total\\\": r[\\\"n_commits\\\"],\\n        \\\"n_files_total\\\": r[\\\"n_files\\\"],\\n        \\\"history_span_years\\\": r[\\\"history_span_years\\\"],\\n    }\\n    example = {\\n        \\\"input\\\": json.dumps(input_features, sort_keys=True),\\n        \\\"output\\\": r[\\\"survival_label\\\"],\\n        \\\"metadata_full_name\\\": r[\\\"full_name\\\"],\\n        \\\"metadata_activity_bucket\\\": r[\\\"activity_bucket\\\"],\\n        \\\"metadata_founder\\\": r[\\\"founder\\\"],\\n        \\\"metadata_tfdd\\\": r[\\\"tfdd\\\"],\\n        \\\"metadata_pre_tfdd_window\\\": pre,\\n        \\\"metadata_tfdd_snapshot_covariates\\\": cov,\\n        \\\"metadata_yearly_doa_tf_tables\\\": r[\\\"yearly_tables\\\"],\\n        \\\"metadata_post_tfdd_monthly_commits\\\": r[\\\"post_tfdd_monthly_commits\\\"],\\n        \\\"metadata_post_tfdd_months_available\\\": r[\\\"post_tfdd_months_available\\\"],\\n        \\\"metadata_years_after_tfdd\\\": r[\\\"years_after_tfdd\\\"],\\n        \\\"metadata_repo_meta\\\": r[\\\"meta\\\"],\\n        \\\"metadata_repo_first_commit\\\": r[\\\"repo_first_commit\\\"],\\n        \\\"metadata_repo_last_commit\\\": r[\\\"repo_last_commit\\\"],\\n        \\\"metadata_task_type\\\": \\\"binary_classification\\\",\\n        \\\"metadata_n_classes\\\": 2,\\n    }\\n    return example\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"874aa4db\",\n   \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"71633375\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru is not pre-installed on Colab\\n_pip('loguru')\\n\\n# matplotlib is pre-installed on Colab; install locally at Colab's exact version\\nif 'google.colab' not in sys.modules:\\n    _pip('matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"d6275476\",\n   \"source\": \"# Original imports from data.py, plus matplotlib for the results plot at the end\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"f217b255\",\n   \"source\": \"## Load the mined repo results\\n\\n`mini_demo_data.json` is a curated subset of the raw per-repo mining output — the same shape as the `temp/repo_results/*.json` files that `data.py` normally globs from disk. It's a mix of 20 **qualified** repos (10 that survived their founder's departure, 10 that didn't) plus one example of each **discard reason** the mining funnel applies, so the filtering step below has something to filter.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is published) and falls back to the local file (works right now, and in this notebook's own working directory on Colab after uploading the file).\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"bd9d9fa6\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json\\\"\\nimport os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception:\\n        pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f:\\n            return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"784b150a\",\n   \"source\": \"data = load_data()\\nprint(f\\\"Loaded {len(data)} raw repo mining results\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"2ca19ee2\",\n   \"source\": \"## Config\\n\\nThe original `data.py` has no tunable numeric parameters — it's a deterministic assembly/filtering step, not a model with iterations or sample sizes. The one \\\"parameter\\\" is which/how-many raw repo results to process; here that's simply all of `data` (the small curated subset loaded above). No other config is needed to reproduce the full logic end-to-end.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"e0fb48e2\",\n   \"source\": \"# Config — process every record in the loaded (curated) mini dataset.\\n# In the full pipeline this would instead be every file matched by\\n# RESULTS_GLOB = \\\"temp/repo_results/*.json\\\" (all 522 mined candidates).\\nraw_results = data\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"5bd767ed\",\n   \"source\": \"## Build one dataset example per qualifying repo\\n\\n`build_example` is copied unchanged from `data.py`. For a qualifying repo it pulls the pre-TFDD authority-diffusion window (`pre`) and the TFDD-snapshot covariates (`cov`) out of the raw mining result, packs the predictors into `input` (a JSON string, matching the corpus's on-disk format), and carries every other field through as `metadata_*` so downstream analysis can recompute alternate windows without re-mining.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"ac1eb1ef\",\n   \"source\": \"def build_example(r: dict) -> dict:\\n    pre = r[\\\"pre_tfdd_window\\\"]\\n    cov = r[\\\"tfdd_snapshot_covariates\\\"]\\n    input_features = {\\n        \\\"founder_commit_share_pre_tfdd\\\": pre[\\\"founder_commit_share\\\"],\\n        \\\"n_distinct_new_primary_owners_pre_tfdd\\\": pre[\\\"n_distinct_new_primary_owners\\\"],\\n        \\\"founder_early_authorship_share\\\": r[\\\"founder_early_authorship_share\\\"],\\n        \\\"stars\\\": cov[\\\"stars\\\"],\\n        \\\"forks\\\": cov[\\\"forks\\\"],\\n        \\\"total_contributors\\\": cov[\\\"total_contributors\\\"],\\n        \\\"language\\\": cov[\\\"language\\\"],\\n        \\\"license\\\": cov[\\\"license\\\"],\\n        \\\"project_age_days\\\": cov[\\\"project_age_days\\\"],\\n        \\\"n_commits_total\\\": r[\\\"n_commits\\\"],\\n        \\\"n_files_total\\\": r[\\\"n_files\\\"],\\n        \\\"history_span_years\\\": r[\\\"history_span_years\\\"],\\n    }\\n    example = {\\n        \\\"input\\\": json.dumps(input_features, sort_keys=True),\\n        \\\"output\\\": r[\\\"survival_label\\\"],\\n        \\\"metadata_full_name\\\": r[\\\"full_name\\\"],\\n        \\\"metadata_activity_bucket\\\": r[\\\"activity_bucket\\\"],\\n        \\\"metadata_founder\\\": r[\\\"founder\\\"],\\n        \\\"metadata_tfdd\\\": r[\\\"tfdd\\\"],\\n        \\\"metadata_pre_tfdd_window\\\": pre,\\n        \\\"metadata_tfdd_snapshot_covariates\\\": cov,\\n        \\\"metadata_yearly_doa_tf_tables\\\": r[\\\"yearly_tables\\\"],\\n        \\\"metadata_post_tfdd_monthly_commits\\\": r[\\\"post_tfdd_monthly_commits\\\"],\\n        \\\"metadata_post_tfdd_months_available\\\": r[\\\"post_tfdd_months_available\\\"],\\n        \\\"metadata_years_after_tfdd\\\": r[\\\"years_after_tfdd\\\"],\\n        \\\"metadata_repo_meta\\\": r[\\\"meta\\\"],\\n        \\\"metadata_repo_first_commit\\\": r[\\\"repo_first_commit\\\"],\\n        \\\"metadata_repo_last_commit\\\": r[\\\"repo_last_commit\\\"],\\n        \\\"metadata_task_type\\\": \\\"binary_classification\\\",\\n        \\\"metadata_n_classes\\\": 2,\\n    }\\n    return example\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"fb2272b8\",\n   \"source\": \"## Filter to qualifying repos and assemble the corpus\\n\\nThis mirrors `data.py`'s `main()`. The only change from the original is the source of the raw results: instead of `glob.glob(RESULTS_GLOB)` reading `temp/repo_results/*.json` off disk, we iterate the `raw_results` list already loaded into memory (each element is exactly one of those per-repo JSON files' contents). Everything else — the qualified/discarded split, the discard-reason tally, and the final `output` dict with its `metadata` block — is unchanged.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [57] TOOL CALL — NotebookEdit · 2026-08-21 19:19:27 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb', 'cell_id': 'fb2272b8', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'logger.info(f"Found {len(raw_results)} mined repo result records")\nqualified = []\ndiscard_reasons = {}\nfor r in raw_results:\n    if r.get("status") == "qualified":\n        qualified.append(r)\n    else:\n        reason = r.get("discard_reason", "unknown")\n        discard_reasons[reason] = discard_reasons.get(reason, 0) + 1\nlogger.info(f"Qualified repos: {len(qualified)}")\nlogger.info(f"Discard reasons: {json.dumps(discard_reasons, indent=2)}")\n\nexamples = [build_example(r) for r in qualified]\noutput = {\n    "metadata": {\n        "source": "GitHub REST search API (candidate discovery) + git log (--filter=blob:none) "\n                   "for full commit history mining",\n        "description": "Single-founder GitHub repos with founder-only Truck-Factor-Developer-"\n                        "Detachment (TFDD) events, per Avelino et al. ICPC\'16 (DOA/TF algorithm) "\n                        "and Avelino et al. ESEM\'19 (TFDD/survival definitions). Each example is "\n                        "one qualifying repo; input=pre-TFDD/snapshot covariates, output=survival "\n                        "label (Active_survived / Inactive_did_not_survive).",\n        "n_qualified": len(qualified),\n        "discard_reason_counts": discard_reasons,\n        "doa_formula": "DOA(d,f) = 3.293 + 1.098*FirstAuthor(d,f) + 0.164*Deliveries(d,f) "\n                       "- 0.321*ln(1+Acceptances(d,f))",\n        "tf_algorithm": "greedy removal of highest-file-count DOA-primary-author while "\n                        "remaining-authors\' file coverage >= 0.5",\n    },\n    "datasets": [\n        {"dataset": "founder_departure_tfdd_corpus", "examples": examples}\n    ],\n}\nlogger.info(f"Assembled {len(examples)} examples into the demo corpus")'}
```

### [58] TOOL RESULT — NotebookEdit · 2026-08-21 19:19:27 UTC

```
{"new_source": "logger.info(f\"Found {len(raw_results)} mined repo result records\")\nqualified = []\ndiscard_reasons = {}\nfor r in raw_results:\n    if r.get(\"status\") == \"qualified\":\n        qualified.append(r)\n    else:\n        reason = r.get(\"discard_reason\", \"unknown\")\n        discard_reasons[reason] = discard_reasons.get(reason, 0) + 1\nlogger.info(f\"Qualified repos: {len(qualified)}\")\nlogger.info(f\"Discard reasons: {json.dumps(discard_reasons, i... [truncated, 22663 chars total]
```

### [59] ASSISTANT · 2026-08-21 19:19:33 UTC

```
Now the results/visualization cell:
```

### [60] TOOL CALL — NotebookEdit · 2026-08-21 19:19:33 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb', 'cell_id': '6c6eea4b', 'cell_type': 'markdown', 'edit_mode': 'insert', 'new_source': '## Results\n\nA summary table of the assembled examples, followed by a plot of the two headline pre-TFDD covariates split by survival label — the question this dataset was built to let downstream experiments answer: does authority diffusion *before* the founder leaves predict whether the project survives?'}
```

### [61] TOOL RESULT — NotebookEdit · 2026-08-21 19:19:33 UTC

```
{"new_source": "## Results\n\nA summary table of the assembled examples, followed by a plot of the two headline pre-TFDD covariates split by survival label — the question this dataset was built to let downstream experiments answer: does authority diffusion *before* the founder leaves predict whether the project survives?", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "162368dd", "error": "", "notebook_path": "/ai-inventor/aii_data/ru... [truncated, 23708 chars total]
```

### [62] TOOL CALL — NotebookEdit · 2026-08-21 19:19:41 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb', 'cell_id': '162368dd', 'cell_type': 'code', 'edit_mode': 'insert', 'new_source': 'print(f"{\'repo\':40s} {\'label\':28s} {\'founder_share_pre\':>18s} {\'new_owners_pre\':>15s}")\nprint("-" * 105)\nfor ex in examples:\n    feats = json.loads(ex["input"])\n    print(\n        f"{ex[\'metadata_full_name\']:40s} {ex[\'output\']:28s} "\n        f"{feats[\'founder_commit_share_pre_tfdd\']:18.3f} "\n        f"{feats[\'n_distinct_new_primary_owners_pre_tfdd\']:15d}"\n    )\n\nprint(f"\\nDiscard reasons seen in this demo subset: {json.dumps(discard_reasons, indent=2)}")\n\n# Plot: pre-TFDD founder commit share vs. number of new primary owners, colored by survival\nactive_x, active_y = [], []\ninactive_x, inactive_y = [], []\nfor ex in examples:\n    feats = json.loads(ex["input"])\n    if ex["output"] == "Active_survived":\n        active_x.append(feats["founder_commit_share_pre_tfdd"])\n        active_y.append(feats["n_distinct_new_primary_owners_pre_tfdd"])\n    else:\n        inactive_x.append(feats["founder_commit_share_pre_tfdd"])\n        inactive_y.append(feats["n_distinct_new_primary_owners_pre_tfdd"])\n\nplt.figure(figsize=(7, 5))\nplt.scatter(active_x, active_y, label="Active_survived", color="tab:green", s=80, edgecolor="black")\nplt.scatter(inactive_x, inactive_y, label="Inactive_did_not_survive", color="tab:red", s=80, edgecolor="black")\nplt.xlabel("Founder commit share in pre-TFDD window")\nplt.ylabel("# distinct new primary owners in pre-TFDD window")\nplt.title("Pre-departure authority diffusion vs. survival outcome")\nplt.legend()\nplt.tight_layout()\nplt.show()'}
```

### [63] TOOL RESULT — NotebookEdit · 2026-08-21 19:19:41 UTC

```
{"new_source": "print(f\"{'repo':40s} {'label':28s} {'founder_share_pre':>18s} {'new_owners_pre':>15s}\")\nprint(\"-\" * 105)\nfor ex in examples:\n    feats = json.loads(ex[\"input\"])\n    print(\n        f\"{ex['metadata_full_name']:40s} {ex['output']:28s} \"\n        f\"{feats['founder_commit_share_pre_tfdd']:18.3f} \"\n        f\"{feats['n_distinct_new_primary_owners_pre_tfdd']:15d}\"\n    )\n\nprint(f\"\\nDiscard reasons seen in this demo subset: {json.dumps(disc... [truncated, 27196 chars total]
```

### [64] ASSISTANT · 2026-08-21 19:19:45 UTC

```
Now let's test-run in a clean environment.
```

### [65] TOOL CALL — Bash · 2026-08-21 19:19:45 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
/usr/local/bin/python3.12 -m venv .nb_env 2>&1 | tail -5
.nb_env/bin/pip install -q pip jupyter ipykernel 2>&1 | tail -10
```

### [66] TOOL RESULT — Bash · 2026-08-21 19:22:46 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "baiha1dy3", "timedOutAfterMs": 180000, "backgroundCwdHint": "Session cwd remains /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k; directory changes made by the backgrounded command do not apply to subsequent commands."}
```

### [67] ASSISTANT · 2026-08-21 19:22:48 UTC

```
Waiting for background setup to finish.
```

### [68] TOOL CALL — Bash · 2026-08-21 19:22:48 UTC

```
sleep 60; tail -20 /tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-70BX2SQt9m6k/b62a383e-01aa-4fbb-9ec7-9cc20a1fcec2/tasks/baiha1dy3.output
```

### [69] TOOL RESULT — Bash [ERROR] · 2026-08-21 19:22:48 UTC

```
Error: Blocked: sleep 60 followed by: tail -20 /tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-70BX2SQt9m6k/b62a383e-01aa-4fbb-9ec7-9cc20a1fcec2/tasks/baiha1dy3.output. To wait for a condition, use Monitor with an until-loop (e.g. `until <check>; do sleep 2; done`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block.
```

### [70] TOOL CALL — ToolSearch · 2026-08-21 19:22:50 UTC

```
{'query': 'select:Monitor', 'max_results': 3}
```

### [71] TOOL RESULT — ToolSearch · 2026-08-21 19:22:50 UTC

```
{"matches": ["Monitor"], "query": "select:Monitor", "total_deferred_tools": 22}
```

### [72] ASSISTANT · 2026-08-21 19:22:54 UTC

```
I'll wait for the background pip install to finish (I'll be notified automatically).
```

### [73] TOOL CALL — Monitor · 2026-08-21 19:22:54 UTC

```
{'command': 'until ! kill -0 $(pgrep -f "pip install -q pip jupyter ipykernel" | head -1) 2>/dev/null; do sleep 3; done; echo done', 'description': 'waiting for jupyter/ipykernel venv install to finish', 'timeout_ms': 300000, 'persistent': False}
```

### [74] TOOL RESULT — Monitor · 2026-08-21 19:22:54 UTC

```
{"taskId": "bxfol1422", "timeoutMs": 300000, "persistent": false}
```

### [75] ASSISTANT · 2026-08-21 19:22:56 UTC

```
I'll wait for the monitor notification before proceeding to execute the notebook.
```

### [76] TOOL CALL — TaskCreate · 2026-08-21 19:22:56 UTC

```
{'subject': 'Test-run code_demo.ipynb in clean venv', 'description': 'Execute code_demo.ipynb with nbconvert in .nb_env, fix any errors, then verify final requirements'}
```

### [77] TOOL RESULT — TaskCreate · 2026-08-21 19:22:56 UTC

```
{"task": {"id": "1", "subject": "Test-run code_demo.ipynb in clean venv"}}
```

### [78] TOOL CALL — Bash · 2026-08-21 19:22:58 UTC

```
true
```

### [79] TOOL RESULT — Bash · 2026-08-21 19:22:58 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [80] TOOL CALL — Bash · 2026-08-21 19:23:04 UTC

```
tail -30 /tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-70BX2SQt9m6k/b62a383e-01aa-4fbb-9ec7-9cc20a1fcec2/tasks/baiha1dy3.output 2>&1
ls /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/bin/ 2>&1 | grep -E "jupyter|python" 
```

### [81] TOOL RESULT — Bash · 2026-08-21 19:23:04 UTC

```
{"stdout": "python\npython3\npython3.12", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [82] ASSISTANT · 2026-08-21 19:23:04 UTC

```
Still installing. I'll wait for the monitor notification.
```

### [83] TOOL CALL — Bash · 2026-08-21 19:23:04 UTC

```
echo waiting
```

### [84] TOOL RESULT — Bash · 2026-08-21 19:23:04 UTC

```
{"stdout": "waiting", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [85] ASSISTANT · 2026-08-21 19:23:08 UTC

```
I'll wait for the monitor's completion notification before continuing.
```

### [86] TOOL CALL — TaskUpdate · 2026-08-21 19:23:08 UTC

```
{'taskId': '1', 'status': 'in_progress'}
```

### [87] TOOL RESULT — TaskUpdate · 2026-08-21 19:23:08 UTC

```
{"success": true, "taskId": "1", "updatedFields": ["status"], "statusChange": {"from": "pending", "to": "in_progress"}}
```

### [88] ASSISTANT · 2026-08-21 19:23:10 UTC

```
Waiting for the venv install to complete before running the notebook test.
```

### [89] TOOL CALL — Bash · 2026-08-21 19:23:10 UTC

```
wait
```

### [90] TOOL RESULT — Bash · 2026-08-21 19:23:10 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": true}
```

### [91] TOOL CALL — Bash · 2026-08-21 19:23:16 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
until [ -f .nb_env/bin/jupyter ]; do sleep 3; done
echo "jupyter installed"
```

### [92] TOOL RESULT — Bash · 2026-08-21 19:25:56 UTC

```
{"stdout": "jupyter installed", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [93] ASSISTANT · 2026-08-21 19:26:00 UTC

```
Now let's execute the notebook.
```

### [94] TOOL CALL — Bash · 2026-08-21 19:26:00 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
.nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb 2>&1 | tail -60
```

### [95] TOOL RESULT — Bash · 2026-08-21 19:26:00 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bigmdy13n", "backgroundCwdHint": "Session cwd remains /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k; directory changes made by the backgrounded command do not apply to subsequent commands."}
```

### [96] ASSISTANT · 2026-08-21 19:26:04 UTC

```
I'll wait for this notebook execution to finish.
```

### [97] TOOL CALL — Bash · 2026-08-21 19:26:04 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
until ! pgrep -f "jupyter nbconvert" > /dev/null; do sleep 5; done
echo "nbconvert finished"
```

### [98] TOOL RESULT — Bash · 2026-08-21 19:36:02 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bzk3kdxks", "timedOutAfterMs": 600000, "backgroundCwdHint": "Session cwd remains /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k; directory changes made by the backgrounded command do not apply to subsequent commands."}
```

### [99] ASSISTANT · 2026-08-21 19:36:04 UTC

```
The nbconvert execution completed with exit code 0. Let me check the output.
```

### [100] TOOL CALL — Read · 2026-08-21 19:36:04 UTC

```
/tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-70BX2SQt9m6k/b62a383e-01aa-4fbb-9ec7-9cc20a1fcec2/tasks/bigmdy13n.output
```

### [101] TOOL RESULT — Read · 2026-08-21 19:36:04 UTC

```
{"type": "text", "file": {"filePath": "/tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-70BX2SQt9m6k/b62a383e-01aa-4fbb-9ec7-9cc20a1fcec2/tasks/bigmdy13n.output", "content": "usage: jupyter [-h] [--version] [--config-dir] [--data-dir] [--runtime-dir]\n               [--paths] [--json] [--debug]\n               [subcommand]\n\nJupyter: Interactive Computing\n\npositional arguments:\n  subcommand     the subcommand to launch\n\noptions:\n  -h, --help     show this help message and exit\n  --version      show the versions of core jupyter packages and exit\n  --config-dir   show Jupyter config dir\n  --data-dir     show Jupyter data dir\n  --runtime-dir  show Jupyter runtime dir\n  --paths        show all Jupyter paths. Add --json for machine-readable\n                 format.\n  --json         output paths as machine-readable json\n  --debug        output debug information about paths\n\nAvailable subcommands: migrate troubleshoot\n\nJupyter command `jupyter-nbconvert` not found.\n\n[exited with code 0]\n", "numLines": 26, "startLine": 1, "totalLines": 26}}
```

### [102] TOOL CALL — Bash · 2026-08-21 19:36:10 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
.nb_env/bin/pip install -q nbconvert 2>&1 | tail -10
echo done
```

### [103] TOOL RESULT — Bash · 2026-08-21 19:36:26 UTC

```
{"stdout": "[notice] A new release of pip is available: 25.0.1 -> 26.2.1\n[notice] To update, run: python3.12 -m pip install --upgrade pip\ndone", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [104] TOOL CALL — Bash · 2026-08-21 19:36:30 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
.nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb 2>&1 | tail -80
echo "EXIT:$?"
```

### [105] TOOL RESULT — Bash · 2026-08-21 19:36:30 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bw5qba3b8", "backgroundCwdHint": "Session cwd remains /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k; directory changes made by the backgrounded command do not apply to subsequent commands."}
```

### [106] ASSISTANT · 2026-08-21 19:36:30 UTC

```
I'll wait for this to finish.
```

### [107] TOOL CALL — Bash · 2026-08-21 19:36:30 UTC

```
echo waiting-for-notification
```

### [108] TOOL RESULT — Bash · 2026-08-21 19:36:30 UTC

```
{"stdout": "waiting-for-notification", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [109] TOOL CALL — Bash · 2026-08-21 19:36:36 UTC

```
until ! pgrep -f "jupyter-nbconvert" >/dev/null 2>&1 && ! pgrep -f "nbconvert" >/dev/null 2>&1; do sleep 5; done; echo done2
```

### [110] TOOL RESULT — Bash · 2026-08-21 19:46:22 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bfoc3ds94", "timedOutAfterMs": 590000}
```

### [111] ASSISTANT · 2026-08-21 19:46:36 UTC

```
The nbconvert execution completed. Let me check the output.
```

### [112] TOOL CALL — Read · 2026-08-21 19:46:36 UTC

```
/tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-70BX2SQt9m6k/b62a383e-01aa-4fbb-9ec7-9cc20a1fcec2/tasks/bw5qba3b8.output
```

### [113] TOOL RESULT — Read · 2026-08-21 19:46:36 UTC

```
{"type": "text", "file": {"filePath": "/tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-70BX2SQt9m6k/b62a383e-01aa-4fbb-9ec7-9cc20a1fcec2/tasks/bw5qba3b8.output", "content": "  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 154, in from_notebook_node\n    nb_copy, resources = self._preprocess(nb_copy, resources)\n                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 353, in _preprocess\n    nbc, resc = preprocessor(nbc, resc)\n                ^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/preprocessors/base.py\", line 48, in __call__\n    return self.preprocess(nb, resources)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/preprocessors/execute.py\", line 103, in preprocess\n    self.preprocess_cell(cell, resources, index)\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/preprocessors/execute.py\", line 124, in preprocess_cell\n    cell = self.execute_cell(cell, index, store_history=True)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/jupyter_core/utils/__init__.py\", line 165, in wrapped\n    return loop.run_until_complete(inner)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/local/lib/python3.12/asyncio/base_events.py\", line 691, in run_until_complete\n    return future.result()\n           ^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbclient/client.py\", line 1062, in async_execute_cell\n    await self._check_raise_for_error(cell, cell_index, exec_reply)\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbclient/client.py\", line 918, in _check_raise_for_error\n    raise CellExecutionError.from_cell_and_msg(cell, exec_reply_content)\nnbclient.exceptions.CellExecutionError: An error occurred while executing the following cell:\n------------------\nlogger.info(f\"Found {len(raw_results)} mined repo result records\")\nqualified = []\ndiscard_reasons = {}\nfor r in raw_results:\n    if r.get(\"status\") == \"qualified\":\n        qualified.append(r)\n    else:\n        reason = r.get(\"discard_reason\", \"unknown\")\n        discard_reasons[reason] = discard_reasons.get(reason, 0) + 1\nlogger.info(f\"Qualified repos: {len(qualified)}\")\nlogger.info(f\"Discard reasons: {json.dumps(discard_reasons, indent=2)}\")\n\nexamples = [build_example(r) for r in qualified]\noutput = {\n    \"metadata\": {\n        \"source\": \"GitHub REST search API (candidate discovery) + git log (--filter=blob:none) \"\n                   \"for full commit history mining\",\n        \"description\": \"Single-founder GitHub repos with founder-only Truck-Factor-Developer-\"\n                        \"Detachment (TFDD) events, per Avelino et al. ICPC'16 (DOA/TF algorithm) \"\n                        \"and Avelino et al. ESEM'19 (TFDD/survival definitions). Each example is \"\n                        \"one qualifying repo; input=pre-TFDD/snapshot covariates, output=survival \"\n                        \"label (Active_survived / Inactive_did_not_survive).\",\n        \"n_qualified\": len(qualified),\n        \"discard_reason_counts\": discard_reasons,\n        \"doa_formula\": \"DOA(d,f) = 3.293 + 1.098*FirstAuthor(d,f) + 0.164*Deliveries(d,f) \"\n                       \"- 0.321*ln(1+Acceptances(d,f))\",\n        \"tf_algorithm\": \"greedy removal of highest-file-count DOA-primary-author while \"\n                        \"remaining-authors' file coverage >= 0.5\",\n    },\n    \"datasets\": [\n        {\"dataset\": \"founder_departure_tfdd_corpus\", \"examples\": examples}\n    ],\n}\nlogger.info(f\"Assembled {len(examples)} examples into the demo corpus\")\n------------------\n\n----- stdout -----\n19:42:27|INFO   |Found 2 mined repo result records\n------------------\n\n\u001b[31m---------------------------------------------------------------------------\u001b[39m\n\u001b[31mAttributeError\u001b[39m                            Traceback (most recent call last)\n\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[7]\u001b[39m\u001b[32m, line 5\u001b[39m\n\u001b[32m      1\u001b[39m logger.info(f\"Found {len(raw_results)} mined repo result records\")\n\u001b[32m      2\u001b[39m qualified = []\n\u001b[32m      3\u001b[39m discard_reasons = {}\n\u001b[32m      4\u001b[39m \u001b[38;5;28;01mfor\u001b[39;00m r \u001b[38;5;28;01min\u001b[39;00m raw_results:\n\u001b[32m----> \u001b[39m\u001b[32m5\u001b[39m     \u001b[38;5;28;01mif\u001b[39;00m r.get(\u001b[33m\"status\"\u001b[39m) == \u001b[33m\"qualified\"\u001b[39m:\n\u001b[32m      6\u001b[39m         qualified.append(r)\n\u001b[32m      7\u001b[39m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m      8\u001b[39m         reason = r.get(\u001b[33m\"discard_reason\"\u001b[39m, \u001b[33m\"unknown\"\u001b[39m)\n\n\u001b[31mAttributeError\u001b[39m: 'str' object has no attribute 'get'\n\nEXIT:0\n\n[exited with code 0]\n", "numLines": 84, "startLine": 1, "totalLines": 84}}
```

### [114] TOOL CALL — Bash · 2026-08-21 19:46:50 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
.nb_env/bin/python -c "
import urllib.request, json
url = 'https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json'
try:
    with urllib.request.urlopen(url) as r:
        d = json.loads(r.read().decode())
        print(type(d), len(d))
        print(d)
except Exception as e:
    print('EXC', e)
"
```

### [115] TOOL RESULT — Bash · 2026-08-21 19:46:52 UTC

```
{"stdout": "<class 'dict'> 2\n{'metadata': {'source': \"GitHub Search API (unauthenticated, 10 req/min search endpoint) for candidate discovery via archived-or-stale x historical-creation-window x language queries (code/find_candidates.py) + GitHub REST API (unauthenticated, 60 req/hour) for repo metadata + `git clone --bare` / `git log --numstat` for full local commit history (code/build_dataset.py). iter_1's liveness_conditioned repos (currently-prominent hand-curated list) ... [truncated, 30581 chars total]
```

### [116] TOOL CALL — Bash · 2026-08-21 19:47:04 UTC

```
which unshare; id
```

### [117] TOOL RESULT — Bash · 2026-08-21 19:47:06 UTC

```
{"stdout": "/usr/bin/unshare\nuid=0(root) gid=0(root) groups=0(root)", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [118] TOOL CALL — Bash · 2026-08-21 19:47:10 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
unshare -n .nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb 2>&1 | tail -100
echo "EXIT:$?"
```

### [119] TOOL RESULT — Bash · 2026-08-21 19:47:12 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bgw3webmf", "backgroundCwdHint": "Session cwd remains /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k; directory changes made by the backgrounded command do not apply to subsequent commands."}
```

### [120] TOOL CALL — Read · 2026-08-21 19:47:14 UTC

```
/tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-70BX2SQt9m6k/b62a383e-01aa-4fbb-9ec7-9cc20a1fcec2/tasks/bgw3webmf.output
```

### [121] TOOL RESULT — Read · 2026-08-21 19:47:14 UTC

```
{"type": "text", "file": {"filePath": "/tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-70BX2SQt9m6k/b62a383e-01aa-4fbb-9ec7-9cc20a1fcec2/tasks/bgw3webmf.output", "content": "unshare: unshare failed: Operation not permitted\nEXIT:0\n\n[exited with code 0]\n", "numLines": 5, "startLine": 1, "totalLines": 5}}
```

### [122] TOOL CALL — Bash · 2026-08-21 19:47:18 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
cp code_demo.ipynb code_demo.ipynb.bak
python3 -c "
import json
nb = json.load(open('code_demo.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code' and any('GITHUB_DATA_URL' in l for l in c['source']):
        c['source'] = [l.replace('https://raw.githubusercontent.com', 'https://raw.githubusercontent.com.invalid') for l in c['source']]
json.dump(nb, open('code_demo.ipynb','w'), indent=1)
print('patched')
"
```

### [123] TOOL RESULT — Bash · 2026-08-21 19:47:22 UTC

```
{"stdout": "patched", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [124] TOOL CALL — Bash · 2026-08-21 19:47:24 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
.nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb 2>&1 | tail -120
echo "EXIT:$?"
```

### [125] TOOL RESULT — Bash · 2026-08-21 19:47:26 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "brvnljy7t", "backgroundCwdHint": "Session cwd remains /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k; directory changes made by the backgrounded command do not apply to subsequent commands."}
```

### [126] TOOL CALL — Bash · 2026-08-21 19:47:28 UTC

```
echo waiting
```

### [127] TOOL RESULT — Bash · 2026-08-21 19:47:28 UTC

```
{"stdout": "waiting", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [128] TOOL CALL — Monitor · 2026-08-21 19:47:30 UTC

```
{'command': 'tail -f /tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-70BX2SQt9m6k/b62a383e-01aa-4fbb-9ec7-9cc20a1fcec2/tasks/brvnljy7t.output | grep -m1 --line-buffered "EXIT:"', 'description': 'waiting for offline nbconvert test to finish', 'timeout_ms': 300000, 'persistent': False}
```

### [129] TOOL RESULT — Monitor · 2026-08-21 19:47:30 UTC

```
{"taskId": "b2bz5qyog", "timeoutMs": 300000, "persistent": false}
```

### [130] TOOL CALL — Bash · 2026-08-21 19:47:32 UTC

```
true
```

### [131] TOOL RESULT — Bash · 2026-08-21 19:47:32 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [132] ASSISTANT · 2026-08-21 19:47:36 UTC

```
Waiting for the test run to complete.
```

### [133] TOOL CALL — Bash · 2026-08-21 19:47:36 UTC

```
sleep 2>/dev/null; :
```

### [134] TOOL RESULT — Bash · 2026-08-21 19:47:36 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [135] TOOL CALL — Read · 2026-08-21 19:47:38 UTC

```
/tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-70BX2SQt9m6k/b62a383e-01aa-4fbb-9ec7-9cc20a1fcec2/tasks/brvnljy7t.output
```

### [136] TOOL RESULT — Read · 2026-08-21 19:47:38 UTC

```
{"type": "text", "file": {"filePath": "/tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-70BX2SQt9m6k/b62a383e-01aa-4fbb-9ec7-9cc20a1fcec2/tasks/brvnljy7t.output", "content": "", "numLines": 1, "startLine": 1, "totalLines": 1}}
```

### [137] ASSISTANT · 2026-08-21 19:47:40 UTC

```
Still running. I'll wait for the notification.
```

### [138] TOOL CALL — Bash · 2026-08-21 19:47:40 UTC

```
:
```

### [139] TOOL RESULT — Bash · 2026-08-21 19:47:42 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [140] ASSISTANT · 2026-08-21 19:47:43 UTC

```
I'll pause here and wait for the background test-run notification before continuing.
```

### [141] SYSTEM-USER prompt · 2026-08-21 19:47:44 UTC

```
<validation-feedback>
Attempt 1 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [142] TOOL CALL — Read · 2026-08-21 19:47:48 UTC

```
/tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-70BX2SQt9m6k/b62a383e-01aa-4fbb-9ec7-9cc20a1fcec2/tasks/brvnljy7t.output
```

### [143] TOOL RESULT — Read · 2026-08-21 19:47:48 UTC

```
{"type": "file_unchanged", "file": {"filePath": "/tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-70BX2SQt9m6k/b62a383e-01aa-4fbb-9ec7-9cc20a1fcec2/tasks/brvnljy7t.output"}}
```

### [144] TOOL CALL — Bash · 2026-08-21 19:47:50 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
ps aux | grep nbconvert | grep -v grep
echo "---"
cat /tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-70BX2SQt9m6k/b62a383e-01aa-4fbb-9ec7-9cc20a1fcec2/tasks/brvnljy7t.output
```

### [145] TOOL RESULT — Bash · 2026-08-21 19:47:50 UTC

```
{"stdout": "root        1632  0.0  0.0   4492  3356 ?        Ss   19:47   0:00 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1787341610827-9i13kl.sh 2>/dev/null || true && shopt -u extglob 2>/dev/null || true && { \\builtin unalias -- 'unsetenv'; \\builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k .nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb 2>&1 | tail -120 echo \"EXIT:$?\"' < /dev/null && pwd -P >| /tmp/claude-9dc5-cwd\nroot        1636  7.9  0.0  82340 71208 ?        S    19:47   0:02 /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/bin/python3.12 .nb_env/bin/jupyter-nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb\n---", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [146] TOOL CALL — Bash · 2026-08-21 19:48:00 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
until ! pgrep -f "jupyter-nbconvert" >/dev/null; do sleep 5; done
echo FINISHED
cat /tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-70BX2SQt9m6k/b62a383e-01aa-4fbb-9ec7-9cc20a1fcec2/tasks/brvnljy7t.output
```

### [147] TOOL RESULT — Bash · 2026-08-21 19:52:56 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bymvy1lzg", "timedOutAfterMs": 300000, "backgroundCwdHint": "Session cwd remains /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k; directory changes made by the backgrounded command do not apply to subsequent commands."}
```

### [148] ASSISTANT · 2026-08-21 19:52:58 UTC

```
Good, it completed. Let me check the output.
```

### [149] TOOL CALL — Read · 2026-08-21 19:52:58 UTC

```
/tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-70BX2SQt9m6k/b62a383e-01aa-4fbb-9ec7-9cc20a1fcec2/tasks/brvnljy7t.output
```

### [150] TOOL RESULT — Read · 2026-08-21 19:52:58 UTC

```
{"type": "text", "file": {"filePath": "/tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-2-art-70BX2SQt9m6k/b62a383e-01aa-4fbb-9ec7-9cc20a1fcec2/tasks/brvnljy7t.output", "content": "[NbConvertApp] Converting notebook code_demo.ipynb to notebook\n[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\nTraceback (most recent call last):\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/bin/jupyter-nbconvert\", line 10, in <module>\n    sys.exit(main())\n             ^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/jupyter_core/application.py\", line 284, in launch_instance\n    super().launch_instance(argv=argv, **kwargs)\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/traitlets/config/application.py\", line 1080, in launch_instance\n    app.start()\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/nbconvertapp.py\", line 420, in start\n    self.convert_notebooks()\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/nbconvertapp.py\", line 597, in convert_notebooks\n    self.convert_single_notebook(notebook_filename)\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/nbconvertapp.py\", line 563, in convert_single_notebook\n    output, resources = self.export_single_notebook(\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/nbconvertapp.py\", line 487, in export_single_notebook\n    output, resources = self.exporter.from_filename(\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 201, in from_filename\n    return self.from_file(f, resources=resources, **kw)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 220, in from_file\n    return self.from_notebook_node(\n           ^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/notebook.py\", line 36, in from_notebook_node\n    nb_copy, resources = super().from_notebook_node(nb, resources, **kw)\n                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 154, in from_notebook_node\n    nb_copy, resources = self._preprocess(nb_copy, resources)\n                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 353, in _preprocess\n    nbc, resc = preprocessor(nbc, resc)\n                ^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/preprocessors/base.py\", line 48, in __call__\n    return self.preprocess(nb, resources)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/preprocessors/execute.py\", line 103, in preprocess\n    self.preprocess_cell(cell, resources, index)\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/preprocessors/execute.py\", line 124, in preprocess_cell\n    cell = self.execute_cell(cell, index, store_history=True)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/jupyter_core/utils/__init__.py\", line 165, in wrapped\n    return loop.run_until_complete(inner)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/local/lib/python3.12/asyncio/base_events.py\", line 691, in run_until_complete\n    return future.result()\n           ^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbclient/client.py\", line 1062, in async_execute_cell\n    await self._check_raise_for_error(cell, cell_index, exec_reply)\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbclient/client.py\", line 918, in _check_raise_for_error\n    raise CellExecutionError.from_cell_and_msg(cell, exec_reply_content)\nnbclient.exceptions.CellExecutionError: An error occurred while executing the following cell:\n------------------\nlogger.info(f\"Found {len(raw_results)} mined repo result records\")\nqualified = []\ndiscard_reasons = {}\nfor r in raw_results:\n    if r.get(\"status\") == \"qualified\":\n        qualified.append(r)\n    else:\n        reason = r.get(\"discard_reason\", \"unknown\")\n        discard_reasons[reason] = discard_reasons.get(reason, 0) + 1\nlogger.info(f\"Qualified repos: {len(qualified)}\")\nlogger.info(f\"Discard reasons: {json.dumps(discard_reasons, indent=2)}\")\n\nexamples = [build_example(r) for r in qualified]\noutput = {\n    \"metadata\": {\n        \"source\": \"GitHub REST search API (candidate discovery) + git log (--filter=blob:none) \"\n                   \"for full commit history mining\",\n        \"description\": \"Single-founder GitHub repos with founder-only Truck-Factor-Developer-\"\n                        \"Detachment (TFDD) events, per Avelino et al. ICPC'16 (DOA/TF algorithm) \"\n                        \"and Avelino et al. ESEM'19 (TFDD/survival definitions). Each example is \"\n                        \"one qualifying repo; input=pre-TFDD/snapshot covariates, output=survival \"\n                        \"label (Active_survived / Inactive_did_not_survive).\",\n        \"n_qualified\": len(qualified),\n        \"discard_reason_counts\": discard_reasons,\n        \"doa_formula\": \"DOA(d,f) = 3.293 + 1.098*FirstAuthor(d,f) + 0.164*Deliveries(d,f) \"\n                       \"- 0.321*ln(1+Acceptances(d,f))\",\n        \"tf_algorithm\": \"greedy removal of highest-file-count DOA-primary-author while \"\n                        \"remaining-authors' file coverage >= 0.5\",\n    },\n    \"datasets\": [\n        {\"dataset\": \"founder_departure_tfdd_corpus\", \"examples\": examples}\n    ],\n}\nlogger.info(f\"Assembled {len(examples)} examples into the demo corpus\")\n------------------\n\n----- stdout -----\n19:49:32|INFO   |Found 2 mined repo result records\n------------------\n\n\u001b[31m---------------------------------------------------------------------------\u001b[39m\n\u001b[31mAttributeError\u001b[39m                            Traceback (most recent call last)\n\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[7]\u001b[39m\u001b[32m, line 5\u001b[39m\n\u001b[32m      1\u001b[39m logger.info(f\"Found {len(raw_results)} mined repo result records\")\n\u001b[32m      2\u001b[39m qualified = []\n\u001b[32m      3\u001b[39m discard_reasons = {}\n\u001b[32m      4\u001b[39m \u001b[38;5;28;01mfor\u001b[39;00m r \u001b[38;5;28;01min\u001b[39;00m raw_results:\n\u001b[32m----> \u001b[39m\u001b[32m5\u001b[39m     \u001b[38;5;28;01mif\u001b[39;00m r.get(\u001b[33m\"status\"\u001b[39m) == \u001b[33m\"qualified\"\u001b[39m:\n\u001b[32m      6\u001b[39m         qualified.append(r)\n\u001b[32m      7\u001b[39m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[32m      8\u001b[39m         reason = r.get(\u001b[33m\"discard_reason\"\u001b[39m, \u001b[33m\"unknown\"\u001b[39m)\n\n\u001b[31mAttributeError\u001b[39m: 'str' object has no attribute 'get'\n\nEXIT:0\n\n[exited with code 0]\n", "numLines": 119, "startLine": 1, "totalLines": 119}}
```

### [151] TOOL CALL — Bash · 2026-08-21 19:53:06 UTC

```
env | grep -i proxy
.nb_env/bin/python -c "
import urllib.request, json
url='https://raw.githubusercontent.com.invalid/foo/bar.json'
try:
    with urllib.request.urlopen(url, timeout=10) as r:
        print(r.status)
        d = r.read().decode()
        print(len(d), d[:300])
except Exception as e:
    print('EXC', type(e), e)
" 2>&1 | tail -30
```

### [152] TOOL RESULT — Bash · 2026-08-21 19:53:08 UTC

```
{"stdout": "AII_SERVER_URL=https://6w20x2e7vmsuqe-8020.proxy.runpod.net\nEXC <class 'urllib.error.URLError'> <urlopen error [Errno -2] Name or service not known>", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [153] TOOL CALL — Bash · 2026-08-21 19:53:14 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
python3 -c "
import json
nb = json.load(open('code_demo.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code' and any('GITHUB_DATA_URL' in l for l in c['source']):
        print(''.join(c['source']))
"
```

### [154] TOOL RESULT — Bash · 2026-08-21 19:53:16 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [155] TOOL CALL — Bash · 2026-08-21 19:53:26 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
python3 -c "
import json
nb = json.load(open('code_demo.ipynb'))
for i,c in enumerate(nb['cells']):
    print(i, c['cell_type'], repr(''.join(c['source']))[:80])
"
```

### [156] TOOL RESULT — Bash · 2026-08-21 19:53:28 UTC

```
{"stdout": "0 markdown '# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly \n1 code \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-\n2 code '# Original imports from data.py, plus matplotlib for the results plot at the en\n3 markdown \"## Load the mined repo results\\n\\n`mini_demo_data.json` is a curated subset of \n4 code 'GITHUB_DATA_URL = \"https://raw.githubusercontent.com/ai-inventor-outputs/ai-inv\n5 code 'data = load_data()\\nprint(f\"Loaded {len(data)} raw repo mining results\")'\n6 markdown '## Config\\n\\nThe original `data.py` has no tunable numeric parameters — it\\'s a\n7 code '# Config — process every record in the loaded (curated) mini dataset.\\n# In the\n8 markdown \"## Build one dataset example per qualifying repo\\n\\n`build_example` is copied u\n9 code 'def build_example(r: dict) -> dict:\\n    pre = r[\"pre_tfdd_window\"]\\n    cov = \n10 markdown \"## Filter to qualifying repos and assemble the corpus\\n\\nThis mirrors `data.py`\n11 code 'logger.info(f\"Found {len(raw_results)} mined repo result records\")\\nqualified =\n12 markdown '## Results\\n\\nA summary table of the assembled examples, followed by a plot of \n13 code 'print(f\"{\\'repo\\':40s} {\\'label\\':28s} {\\'founder_share_pre\\':>18s} {\\'new_owne", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [157] TOOL CALL — Bash · 2026-08-21 19:53:34 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
python3 << 'EOF'
import json
nb = json.load(open('code_demo.ipynb'))
print(''.join(nb['cells'][4]['source']))
EOF
```

### [158] TOOL RESULT — Bash · 2026-08-21 19:53:34 UTC

```
{"stdout": "GITHUB_DATA_URL = \"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json\"\nimport os\n\ndef load_data():\n    try:\n        import urllib.request\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\n            return json.loads(response.read().decode())\n    except Exception:\n        pass\n    if os.path.exists(\"mini_demo_data.json\"):\n        with open(\"mini_demo_data.json\") as f:\n            return json.load(f)\n    raise FileNotFoundError(\"Could not load mini_demo_data.json\")", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [159] TOOL CALL — Bash · 2026-08-21 19:53:38 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
diff code_demo.ipynb code_demo.ipynb.bak | head -20
echo "---"
grep -c "invalid" code_demo.ipynb code_demo.ipynb.bak
```

### [160] TOOL RESULT — Bash · 2026-08-21 19:53:38 UTC

```
{"stdout": "6c6\n<    \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events \\u2014 the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover \\u226550% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic \\u2014 filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema \\u2014 on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n---\n>    \"source\": \"# Founder Departure Survival Corpus\\n\\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\\n\\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \\\"truck factor\\\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\\n\\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\\n\\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.\",\n28c28\n<    \"source\": \"## Load the mined repo results\\n\\n`mini_demo_data.json` is a curated subset of the raw per-repo mining output \\u2014 the same shape as the `temp/repo_results/*.json` files that `data.py` normally globs from disk. It's a mix of 20 **qualified** repos (10 that survived their founder's departure, 10 that didn't) plus one example of each **discard reason** the mining funnel applies, so the filtering step below has something to filter.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is published) and falls back to the local file (works right now, and in this notebook's own working directory on Colab after uploading the file).\",\n---\n>    \"source\": \"## Load the mined repo results\\n\\n`mini_demo_data.json` is a curated subset of the raw per-repo mining output — the same shape as the `temp/repo_results/*.json` files that `data.py` normally globs from disk. It's a mix of 20 **qualified** repos (10 that survived their founder's departure, 10 that didn't) plus one example of each **discard reason** the mining funnel applies, so the filtering step below has something to filter.\\n\\nThe loader tries the GitHub raw URL first (works once this artifact is published) and falls back to the local file (works right now, and in this notebook's own working directory on Colab after uploading the file).\",\n50c50\n<    \"source\": \"## Config\\n\\nThe original `data.py` has no tunable numeric parameters \\u2014 it's a deterministic assembly/filtering step, not a model with iterations or sample sizes. The one \\\"parameter\\\" is which/how-many raw repo results to process; here that's simply all of `data` (the small curated subset loaded above). No other config is needed to reproduce the full logic end-to-end.\",\n---\n>    \"source\": \"## Config\\n\\nThe original `data.py` has no tunable numeric parameters — it's a deterministic assembly/filtering step, not a model with iterations or sample sizes. The one \\\"parameter\\\" is which/how-many raw repo results to process; here that's simply all of `data` (the small curated subset loaded above). No other config is needed to reproduce the full logic end-to-end.\",\n56c56\n<    \"source\": \"# Config \\u2014 process every record in the loaded (curated) mini dataset.\\n# In the full pipeline this would instead be every file matched by\\n# RESULTS_GLOB = \\\"temp/repo_results/*.json\\\" (all 522 mined candidates).\\nraw_results = data\",\n---\n>    \"source\": \"# Config — process every record in the loaded (curated) mini dataset.\\n# In the full pipeline this would instead be every file matched by\\n# RESULTS_GLOB = \\\"temp/repo_results/*.json\\\" (all 522 mined candidates).\\nraw_results = data\",\n78c78\n<    \"source\": \"## Filter to qualifying repos and assemble the corpus\\n\\nThis mirrors `data.py`'s `main()`. The only change from the original is the source of the raw results: instead of `glob.glob(RESULTS_GLOB)` reading `temp/repo_results/*.json` off disk, we iterate the `raw_results` list already loaded into memory (each element is exactly one of those per-repo JSON files' contents). Everything else \\u2014 the qualified/discarded split, the discard-reason tally, and the final `output` dict with its `metadata` block \\u2014 is unchanged.\",\n---\n>    \"source\": \"## Filter to qualifying repos and assemble the corpus\\n\\nThis mirrors `data.py`'s `main()`. The only change from the original is the source of the raw results: instead of `glob.glob(RESULTS_GLOB)` reading `temp/repo_results/*.json` off disk, we iterate the `raw_results` list already loaded into memory (each element is exactly one of those per-repo JSON files' contents). Everything else — the qualified/discarded split, the discard-reason tally, and the final `output` dict with its `metadata` block — is unchanged.\",\n---\ncode_demo.ipynb:0\ncode_demo.ipynb.bak:0", "stderr": "", "interrupted": false, "isImage": false, "returnCodeInterpretation": "No matches found", "noOutputExpected": false}
```

### [161] TOOL CALL — Bash · 2026-08-21 19:53:46 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
python3 << 'EOF'
import json
nb = json.load(open('code_demo.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code' and 'GITHUB_DATA_URL' in c['source']:
        c['source'] = c['source'].replace('https://raw.githubusercontent.com', 'https://raw.githubusercontent.com.invalid')
json.dump(nb, open('code_demo.ipynb','w'), indent=1)
print('patched')
EOF
grep -c "invalid" code_demo.ipynb
```

### [162] TOOL RESULT — Bash · 2026-08-21 19:53:48 UTC

```
{"stdout": "patched\n1", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [163] ASSISTANT · 2026-08-21 19:53:52 UTC

```
Now re-run the offline test.
```

### [164] TOOL CALL — Bash · 2026-08-21 19:53:52 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
.nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb > /tmp/nbtest.log 2>&1
echo "EXIT:$?" >> /tmp/nbtest.log
tail -100 /tmp/nbtest.log
```

### [165] TOOL RESULT — Bash · 2026-08-21 19:53:54 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "b32qian7u", "backgroundCwdHint": "Session cwd remains /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k; directory changes made by the backgrounded command do not apply to subsequent commands."}
```

### [166] ASSISTANT · 2026-08-21 19:54:00 UTC

```
I'll wait for this test run to complete.
```

### [167] TOOL CALL — Bash · 2026-08-21 19:54:00 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
until [ -f /tmp/nbtest.log ] && grep -q "EXIT:" /tmp/nbtest.log; do sleep 5; done
echo FOUND
```

### [168] TOOL RESULT — Bash · 2026-08-21 19:56:08 UTC

```
{"stdout": "FOUND", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [169] TOOL CALL — Read · 2026-08-21 19:56:08 UTC

```
/tmp/nbtest.log
```

### [170] TOOL RESULT — Read · 2026-08-21 19:56:08 UTC

```
{"type": "text", "file": {"filePath": "/tmp/nbtest.log", "content": "[NbConvertApp] Converting notebook code_demo.ipynb to notebook\n[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\nTraceback (most recent call last):\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/bin/jupyter-nbconvert\", line 10, in <module>\n    sys.exit(main())\n             ^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/jupyter_core/application.py\", line 284, in launch_instance\n    super().launch_instance(argv=argv, **kwargs)\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/traitlets/config/application.py\", line 1080, in launch_instance\n    app.start()\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/nbconvertapp.py\", line 420, in start\n    self.convert_notebooks()\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/nbconvertapp.py\", line 597, in convert_notebooks\n    self.convert_single_notebook(notebook_filename)\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/nbconvertapp.py\", line 563, in convert_single_notebook\n    output, resources = self.export_single_notebook(\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/nbconvertapp.py\", line 487, in export_single_notebook\n    output, resources = self.exporter.from_filename(\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 201, in from_filename\n    return self.from_file(f, resources=resources, **kw)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 220, in from_file\n    return self.from_notebook_node(\n           ^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/notebook.py\", line 36, in from_notebook_node\n    nb_copy, resources = super().from_notebook_node(nb, resources, **kw)\n                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 154, in from_notebook_node\n    nb_copy, resources = self._preprocess(nb_copy, resources)\n                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/exporters/exporter.py\", line 353, in _preprocess\n    nbc, resc = preprocessor(nbc, resc)\n                ^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/preprocessors/base.py\", line 48, in __call__\n    return self.preprocess(nb, resources)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/preprocessors/execute.py\", line 103, in preprocess\n    self.preprocess_cell(cell, resources, index)\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbconvert/preprocessors/execute.py\", line 124, in preprocess_cell\n    cell = self.execute_cell(cell, index, store_history=True)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/jupyter_core/utils/__init__.py\", line 165, in wrapped\n    return loop.run_until_complete(inner)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/local/lib/python3.12/asyncio/base_events.py\", line 691, in run_until_complete\n    return future.result()\n           ^^^^^^^^^^^^^^^\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbclient/client.py\", line 1062, in async_execute_cell\n    await self._check_raise_for_error(cell, cell_index, exec_reply)\n  File \"/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/.nb_env/lib/python3.12/site-packages/nbclient/client.py\", line 918, in _check_raise_for_error\n    raise CellExecutionError.from_cell_and_msg(cell, exec_reply_content)\nnbclient.exceptions.CellExecutionError: An error occurred while executing the following cell:\n------------------\nprint(f\"{'repo':40s} {'label':28s} {'founder_share_pre':>18s} {'new_owners_pre':>15s}\")\nprint(\"-\" * 105)\nfor ex in examples:\n    feats = json.loads(ex[\"input\"])\n    print(\n        f\"{ex['metadata_full_name']:40s} {ex['output']:28s} \"\n        f\"{feats['founder_commit_share_pre_tfdd']:18.3f} \"\n        f\"{feats['n_distinct_new_primary_owners_pre_tfdd']:15d}\"\n    )\n\nprint(f\"\\nDiscard reasons seen in this demo subset: {json.dumps(discard_reasons, indent=2)}\")\n\n# Plot: pre-TFDD founder commit share vs. number of new primary owners, colored by survival\nactive_x, active_y = [], []\ninactive_x, inactive_y = [], []\nfor ex in examples:\n    feats = json.loads(ex[\"input\"])\n    if ex[\"output\"] == \"Active_survived\":\n        active_x.append(feats[\"founder_commit_share_pre_tfdd\"])\n        active_y.append(feats[\"n_distinct_new_primary_owners_pre_tfdd\"])\n    else:\n        inactive_x.append(feats[\"founder_commit_share_pre_tfdd\"])\n        inactive_y.append(feats[\"n_distinct_new_primary_owners_pre_tfdd\"])\n\nplt.figure(figsize=(7, 5))\nplt.scatter(active_x, active_y, label=\"Active_survived\", color=\"tab:green\", s=80, edgecolor=\"black\")\nplt.scatter(inactive_x, inactive_y, label=\"Inactive_did_not_survive\", color=\"tab:red\", s=80, edgecolor=\"black\")\nplt.xlabel(\"Founder commit share in pre-TFDD window\")\nplt.ylabel(\"# distinct new primary owners in pre-TFDD window\")\nplt.title(\"Pre-departure authority diffusion vs. survival outcome\")\nplt.legend()\nplt.tight_layout()\nplt.show()\n------------------\n\n----- stdout -----\nrepo                                     label                         founder_share_pre  new_owners_pre\n---------------------------------------------------------------------------------------------------------\nmholt/PapaParse                          Active_survived                           0.000               6\nkaelzhang/node-ignore                    Active_survived                           0.000               2\nhapijs/boom                              Active_survived                           0.000               2\nqbittorrent/qBittorrent                  Active_survived                           0.000              14\nruby-grape/grape                         Active_survived                           0.000              18\n------------------\n\n\u001b[31m---------------------------------------------------------------------------\u001b[39m\n\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)\n\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[8]\u001b[39m\u001b[32m, line 7\u001b[39m\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mfor\u001b[39;00m ex \u001b[38;5;28;01min\u001b[39;00m examples:\n\u001b[32m      4\u001b[39m     feats = json.loads(ex[\u001b[33m\"input\"\u001b[39m])\n\u001b[32m      5\u001b[39m     print(\n\u001b[32m      6\u001b[39m         f\"{ex[\u001b[33m'metadata_full_name'\u001b[39m]:40s} {ex[\u001b[33m'output'\u001b[39m]:28s} \"\n\u001b[32m----> \u001b[39m\u001b[32m7\u001b[39m         f\"{feats[\u001b[33m'founder_commit_share_pre_tfdd'\u001b[39m]:18.3f} \"\n\u001b[32m      8\u001b[39m         f\"{feats[\u001b[33m'n_distinct_new_primary_owners_pre_tfdd'\u001b[39m]:15d}\"\n\u001b[32m      9\u001b[39m     )\n\u001b[32m     10\u001b[39m \n\n\u001b[31mTypeError\u001b[39m: unsupported format string passed to NoneType.__format__\n\nEXIT:1\n", "numLines": 122, "startLine": 1, "totalLines": 122}}
```

### [171] TOOL CALL — Bash · 2026-08-21 19:56:14 UTC

```
WS=/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
python3 -c "
import json
d = json.load(open('$WS/mini_demo_data.json'))
for r in d:
    if r.get('status')=='qualified':
        pre = r.get('pre_tfdd_window', {})
        print(r['full_name'], pre.get('founder_commit_share'), pre.get('n_distinct_new_primary_owners'))
"
```

### [172] TOOL RESULT — Bash · 2026-08-21 19:56:16 UTC

```
{"stdout": "mholt/PapaParse 0.0 6\nkaelzhang/node-ignore 0.0 2\nhapijs/boom 0.0 2\nqbittorrent/qBittorrent 0.0 14\nruby-grape/grape 0.0 18\nflightphp/core None 3\nexpressjs/response-time None 1\nice-cube-ruby/ice_cube 0.0 4\nhttp-party/http-server 0.0 5\nklee/klee 0.0 20\ngraphql/dataloader 0.0 12\nmrwill84/DOClever 0.0 3\nguzzle/guzzle 0.0 14\nfastlane/fastlane 0.0 250\nidank/explainshell 0.0 4\nmaxs15/react-native-modalbox 0.0 5\njekyll/jekyll-admin 0.0 18\nbiometrics/openbr 0.0 26\npiskelapp/piskel None 13\nlaurentj/slimerjs 0.0 10", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [173] TOOL CALL — Read · 2026-08-21 19:56:20 UTC

```
/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb
```

### [174] TOOL RESULT — Read · 2026-08-21 19:56:20 UTC

```
{"type": "notebook", "file": {"filePath": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb", "cells": [{"cellType": "markdown", "source": "# Founder Departure Survival Corpus\n\nThis notebook demonstrates the assembly script (`data.py`) from the **Founder Departure Survival Corpus** dataset artifact.\n\nThe full pipeline mines public GitHub repositories for founder-only **Truck-Factor-Developer-Detachment (TFDD)** events — the moment a project's sole \"truck factor\" developer (the person whose departure would leave the project unable to continue, per the Degree-of-Authorship/Truck-Factor methodology of Avelino et al. ICPC'16 / ESEM'19) goes silent. For each mined repository it computes:\n\n- **DOA** (Degree of Authorship) per file per author: `DOA = 3.293 + 1.098*FirstAuthor + 0.164*Deliveries - 0.321*ln(1+Acceptances)`\n- **Truck Factor (TF)**: greedy removal of the highest-file-count DOA-primary author while remaining authors still cover ≥50% of files, recomputed yearly to locate the first TFDD event\n- Pre-TFDD covariates (6-12 month authority-diffusion window) and TFDD-snapshot covariates (stars, forks, contributors, language, etc.)\n- A binary survival label: whether the project was still active after the founder's departure (`Active_survived`) or not (`Inactive_did_not_survive`)\n\nThis demo notebook takes the **already-mined per-repo results** (the `temp/repo_results/*.json` files the full pipeline produces after cloning and walking each repo's commit history) and runs the exact same `data.py` assembly logic — filtering to qualifying repos, extracting predictor covariates, and building the final `input`/`output` schema — on a small curated subset. It ends with a summary table and a plot of the predictor/label relationship.", "cell_id": "874aa4db"}, {"cellType": "code", "source": "import subprocess, sys\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\n\n# loguru is not pre-installed on Colab\n_pip('loguru')\n\n# matplotlib is pre-installed on Colab; install locally at Colab's exact version\nif 'google.colab' not in sys.modules:\n    _pip('matplotlib==3.10.0')", "cell_id": "71633375", "language": "python"}, {"cellType": "code", "source": "# Original imports from data.py, plus matplotlib for the results plot at the end\nimport json\nimport sys\nfrom pathlib import Path\n\nfrom loguru import logger\nimport matplotlib.pyplot as plt\n\nlogger.remove()\nlogger.add(sys.stdout, level=\"INFO\", format=\"{time:HH:mm:ss}|{level:<7}|{message}\")", "cell_id": "d6275476", "language": "python"}, {"cellType": "markdown", "source": "## Load the mined repo results\n\n`mini_demo_data.json` is a curated subset of the raw per-repo mining output — the same shape as the `temp/repo_results/*.json` files that `data.py` normally globs from disk. It's a mix of 20 **qualified** repos (10 that survived their founder's departure, 10 that didn't) plus one example of each **discard reason** the mining funnel applies, so the filtering step below has something to filter.\n\nThe loader tries the GitHub raw URL first (works once this artifact is published) and falls back to the local file (works right now, and in this notebook's own working directory on Colab after uploading the file).", "cell_id": "f217b255"}, {"cellType": "code", "source": "GITHUB_DATA_URL = \"https://raw.githubusercontent.com.invalid/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json\"\nimport os\n\ndef load_data():\n    try:\n        import urllib.request\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\n            return json.loads(response.read().decode())\n    except Exception:\n        pass\n    if os.path.exists(\"mini_demo_data.json\"):\n        with open(\"mini_demo_data.json\") as f:\n            return json.load(f)\n    raise FileNotFoundError(\"Could not load mini_demo_data.json\")", "cell_id": "bd9d9fa6", "language": "python"}, {"cellType": "code", "source": "data = load_data()\nprint(f\"Loaded {len(data)} raw repo mining results\")", "cell_id": "784b150a", "language": "python"}, {"cellType": "markdown", "source": "## Config\n\nThe original `data.py` has no tunable numeric parameters — it's a deterministic assembly/filtering step, not a model with iterations or sample sizes. The one \"parameter\" is which/how-many raw repo results to process; here that's simply all of `data` (the small curated subset loaded above). No other config is needed to reproduce the full logic end-to-end.", "cell_id": "2ca19ee2"}, {"cellType": "code", "source": "# Config — process every record in the loaded (curated) mini dataset.\n# In the full pipeline this would instead be every file matched by\n# RESULTS_GLOB = \"temp/repo_results/*.json\" (all 522 mined candidates).\nraw_results = data", "cell_id": "e0fb48e2", "language": "python"}, {"cellType": "markdown", "source": "## Build one dataset example per qualifying repo\n\n`build_example` is copied unchanged from `data.py`. For a qualifying repo it pulls the pre-TFDD authority-diffusion window (`pre`) and the TFDD-snapshot covariates (`cov`) out of the raw mining result, packs the predictors into `input` (a JSON string, matching the corpus's on-disk format), and carries every other field through as `metadata_*` so downstream analysis can recompute alternate windows without re-mining.", "cell_id": "5bd767ed"}, {"cellType": "code", "source": "def build_example(r: dict) -> dict:\n    pre = r[\"pre_tfdd_window\"]\n    cov = r[\"tfdd_snapshot_covariates\"]\n    input_features = {\n        \"founder_commit_share_pre_tfdd\": pre[\"founder_commit_share\"],\n        \"n_distinct_new_primary_owners_pre_tfdd\": pre[\"n_distinct_new_primary_owners\"],\n        \"founder_early_authorship_share\": r[\"founder_early_authorship_share\"],\n        \"stars\": cov[\"stars\"],\n        \"forks\": cov[\"forks\"],\n        \"total_contributors\": cov[\"total_contributors\"],\n        \"language\": cov[\"language\"],\n        \"license\": cov[\"license\"],\n        \"project_age_days\": cov[\"project_age_days\"],\n        \"n_commits_total\": r[\"n_commits\"],\n        \"n_files_total\": r[\"n_files\"],\n        \"history_span_years\": r[\"history_span_years\"],\n    }\n    example = {\n        \"input\": json.dumps(input_features, sort_keys=True),\n        \"output\": r[\"survival_label\"],\n        \"metadata_full_name\": r[\"full_name\"],\n        \"metadata_activity_bucket\": r[\"activity_bucket\"],\n        \"metadata_founder\": r[\"founder\"],\n        \"metadata_tfdd\": r[\"tfdd\"],\n        \"metadata_pre_tfdd_window\": pre,\n        \"metadata_tfdd_snapshot_covariates\": cov,\n        \"metadata_yearly_doa_tf_tables\": r[\"yearly_tables\"],\n        \"metadata_post_tfdd_monthly_commits\": r[\"post_tfdd_monthly_commits\"],\n        \"metadata_post_tfdd_months_available\": r[\"post_tfdd_months_available\"],\n        \"metadata_years_after_tfdd\": r[\"years_after_tfdd\"],\n        \"metadata_repo_meta\": r[\"meta\"],\n        \"metadata_repo_first_commit\": r[\"repo_first_commit\"],\n        \"metadata_repo_last_commit\": r[\"repo_last_commit\"],\n        \"metadata_task_type\": \"binary_classification\",\n        \"metadata_n_classes\": 2,\n    }\n    return example", "cell_id": "ac1eb1ef", "language": "python"}, {"cellType": "markdown", "source": "## Filter to qualifying repos and assemble the corpus\n\nThis mirrors `data.py`'s `main()`. The only change from the original is the source of the raw results: instead of `glob.glob(RESULTS_GLOB)` reading `temp/repo_results/*.json` off disk, we iterate the `raw_results` list already loaded into memory (each element is exactly one of those per-repo JSON files' contents). Everything else — the qualified/discarded split, the discard-reason tally, and the final `output` dict with its `metadata` block — is unchanged.", "cell_id": "fb2272b8"}, {"cellType": "code", "source": "logger.info(f\"Found {len(raw_results)} mined repo result records\")\nqualified = []\ndiscard_reasons = {}\nfor r in raw_results:\n    if r.get(\"status\") == \"qualified\":\n        qualified.append(r)\n    else:\n        reason = r.get(\"discard_reason\", \"unknown\")\n        discard_reasons[reason] = discard_reasons.get(reason, 0) + 1\nlogger.info(f\"Qualified repos: {len(qualified)}\")\nlogger.info(f\"Discard reasons: {json.dumps(discard_reasons, indent=2)}\")\n\nexamples = [build_example(r) for r in qualified]\noutput = {\n    \"metadata\": {\n        \"source\": \"GitHub REST search API (candidate discovery) + git log (--filter=blob:none) \"\n                   \"for full commit history mining\",\n        \"description\": \"Single-founder GitHub repos with founder-only Truck-Factor-Developer-\"\n                        \"Detachment (TFDD) events, per Avelino et al. ICPC'16 (DOA/TF algorithm) \"\n                        \"and Avelino et al. ESEM'19 (TFDD/survival definitions). Each example is \"\n                        \"one qualifying repo; input=pre-TFDD/snapshot covariates, output=survival \"\n                        \"label (Active_survived / Inactive_did_not_survive).\",\n        \"n_qualified\": len(qualified),\n        \"discard_reason_counts\": discard_reasons,\n        \"doa_formula\": \"DOA(d,f) = 3.293 + 1.098*FirstAuthor(d,f) + 0.164*Deliveries(d,f) \"\n                       \"- 0.321*ln(1+Acceptances(d,f))\",\n        \"tf_algorithm\": \"greedy removal of highest-file-count DOA-primary-author while \"\n                        \"remaining-authors' file coverage >= 0.5\",\n    },\n    \"datasets\": [\n        {\"dataset\": \"founder_departure_tfdd_corpus\", \"examples\": examples}\n    ],\n}\nlogger.info(f\"Assembled {len(examples)} examples into the demo corpus\")", "cell_id": "6c6eea4b", "language": "python"}, {"cellType": "markdown", "source": "## Results\n\nA summary table of the assembled examples, followed by a plot of the two headline pre-TFDD covariates split by survival label — the question this dataset was built to let downstream experiments answer: does authority diffusion *before* the founder leaves predict whether the project survives?", "cell_id": "162368dd"}, {"cellType": "code", "source": "print(f\"{'repo':40s} {'label':28s} {'founder_share_pre':>18s} {'new_owners_pre':>15s}\")\nprint(\"-\" * 105)\nfor ex in examples:\n    feats = json.loads(ex[\"input\"])\n    print(\n        f\"{ex['metadata_full_name']:40s} {ex['output']:28s} \"\n        f\"{feats['founder_commit_share_pre_tfdd']:18.3f} \"\n        f\"{feats['n_distinct_new_primary_owners_pre_tfdd']:15d}\"\n    )\n\nprint(f\"\\nDiscard reasons seen in this demo subset: {json.dumps(discard_reasons, indent=2)}\")\n\n# Plot: pre-TFDD founder commit share vs. number of new primary owners, colored by survival\nactive_x, active_y = [], []\ninactive_x, inactive_y = [], []\nfor ex in examples:\n    feats = json.loads(ex[\"input\"])\n    if ex[\"output\"] == \"Active_survived\":\n        active_x.append(feats[\"founder_commit_share_pre_tfdd\"])\n        active_y.append(feats[\"n_distinct_new_primary_owners_pre_tfdd\"])\n    else:\n        inactive_x.append(feats[\"founder_commit_share_pre_tfdd\"])\n        inactive_y.append(feats[\"n_distinct_new_primary_owners_pre_tfdd\"])\n\nplt.figure(figsize=(7, 5))\nplt.scatter(active_x, active_y, label=\"Active_survived\", color=\"tab:green\", s=80, edgecolor=\"black\")\nplt.scatter(inactive_x, inactive_y, label=\"Inactive_did_not_survive\", color=\"tab:red\", s=80, edgecolor=\"black\")\nplt.xlabel(\"Founder commit share in pre-TFDD window\")\nplt.ylabel(\"# distinct new primary owners in pre-TFDD window\")\nplt.title(\"Pre-departure authority diffusion vs. survival outcome\")\nplt.legend()\nplt.tight_layout()\nplt.show()", "cell_id": "dd45b0f7", "language": "python"}]}}
```

### [175] TOOL CALL — NotebookEdit · 2026-08-21 19:56:29 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k/code_demo.ipynb', 'cell_id': 'dd45b0f7', 'cell_type': 'code', 'new_source': 'def _fmt(v, spec):\n    return format(v, spec) if v is not None else "N/A".rjust(int("".join(c for c in spec if c.isdigit()) or "0"))\n\nprint(f"{\'repo\':40s} {\'label\':28s} {\'founder_share_pre\':>18s} {\'new_owners_pre\':>15s}")\nprint("-" * 105)\nfor ex in examples:\n    feats = json.loads(ex["input"])\n    print(\n        f"{ex[\'metadata_full_name\']:40s} {ex[\'output\']:28s} "\n        f"{_fmt(feats[\'founder_commit_share_pre_tfdd\'], \'18.3f\')} "\n        f"{_fmt(feats[\'n_distinct_new_primary_owners_pre_tfdd\'], \'15d\')}"\n    )\n\nprint(f"\\nDiscard reasons seen in this demo subset: {json.dumps(discard_reasons, indent=2)}")\n\n# Plot: pre-TFDD founder commit share vs. number of new primary owners, colored by survival\n# (skip any example with a missing covariate — pre-TFDD windows can be null for some repos)\nactive_x, active_y = [], []\ninactive_x, inactive_y = [], []\nfor ex in examples:\n    feats = json.loads(ex["input"])\n    x, y = feats["founder_commit_share_pre_tfdd"], feats["n_distinct_new_primary_owners_pre_tfdd"]\n    if x is None or y is None:\n        continue\n    if ex["output"] == "Active_survived":\n        active_x.append(x)\n        active_y.append(y)\n    else:\n        inactive_x.append(x)\n        inactive_y.append(y)\n\nplt.figure(figsize=(7, 5))\nplt.scatter(active_x, active_y, label="Active_survived", color="tab:green", s=80, edgecolor="black")\nplt.scatter(inactive_x, inactive_y, label="Inactive_did_not_survive", color="tab:red", s=80, edgecolor="black")\nplt.xlabel("Founder commit share in pre-TFDD window")\nplt.ylabel("# distinct new primary owners in pre-TFDD window")\nplt.title("Pre-departure authority diffusion vs. survival outcome")\nplt.legend()\nplt.tight_layout()\nplt.show()'}
```

### [176] TOOL RESULT — NotebookEdit · 2026-08-21 19:56:31 UTC

```
{"new_source": "def _fmt(v, spec):\n    return format(v, spec) if v is not None else \"N/A\".rjust(int(\"\".join(c for c in spec if c.isdigit()) or \"0\"))\n\nprint(f\"{'repo':40s} {'label':28s} {'founder_share_pre':>18s} {'new_owners_pre':>15s}\")\nprint(\"-\" * 105)\nfor ex in examples:\n    feats = json.loads(ex[\"input\"])\n    print(\n        f\"{ex['metadata_full_name']:40s} {ex['output']:28s} \"\n        f\"{_fmt(feats['founder_commit_share_pre_tfdd'], '18.3f')}... [truncated, 31147 chars total]
```

### [177] ASSISTANT · 2026-08-21 19:56:35 UTC

```
Now re-run the offline test.
```

### [178] TOOL CALL — Bash · 2026-08-21 19:56:35 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
rm -f /tmp/nbtest.log
.nb_env/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb > /tmp/nbtest.log 2>&1
echo "EXIT:$?" >> /tmp/nbtest.log
tail -100 /tmp/nbtest.log
```

### [179] TOOL RESULT — Bash · 2026-08-21 19:56:37 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "blggddu16", "backgroundCwdHint": "Session cwd remains /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k; directory changes made by the backgrounded command do not apply to subsequent commands."}
```

### [180] TOOL CALL — Bash · 2026-08-21 19:56:43 UTC

```
until [ -f /tmp/nbtest.log ] && grep -q "EXIT:" /tmp/nbtest.log; do sleep 5; done
echo FOUND
```

### [181] TOOL RESULT — Bash · 2026-08-21 19:58:41 UTC

```
{"stdout": "FOUND", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [182] TOOL CALL — Read · 2026-08-21 19:58:41 UTC

```
/tmp/nbtest.log
```

### [183] TOOL RESULT — Read · 2026-08-21 19:58:41 UTC

```
{"type": "text", "file": {"filePath": "/tmp/nbtest.log", "content": "[NbConvertApp] Converting notebook code_demo.ipynb to notebook\n[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m A new release of pip is available: \u001b[0m\u001b[31;49m25.0.1\u001b[0m\u001b[39;49m -> \u001b[0m\u001b[32;49m26.2.1\u001b[0m\n\u001b[1m[\u001b[0m\u001b[34;49mnotice\u001b[0m\u001b[1;39;49m]\u001b[0m\u001b[39;49m To update, run: \u001b[0m\u001b[32;49mpython3.12 -m pip install --upgrade pip\u001b[0m\n[NbConvertApp] Writing 69581 bytes to code_demo.ipynb\nEXIT:0\n", "numLines": 11, "startLine": 1, "totalLines": 11}}
```

### [184] ASSISTANT · 2026-08-21 19:58:47 UTC

```
Success. Now let's restore the correct GITHUB_DATA_URL (removing the `.invalid` test patch) and verify.
```

### [185] TOOL CALL — Bash · 2026-08-21 19:58:47 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
python3 << 'EOF'
import json
nb = json.load(open('code_demo.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code' and 'GITHUB_DATA_URL' in c['source']:
        c['source'] = c['source'].replace('raw.githubusercontent.com.invalid', 'raw.githubusercontent.com')
json.dump(nb, open('code_demo.ipynb','w'), indent=1)
print('restored')
EOF
grep -c "\.invalid" code_demo.ipynb
python3 -c "
import json
nb = json.load(open('code_demo.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code' and 'GITHUB_DATA_URL' in c['source']:
        print(c['source'].splitlines()[0])
"
rm -f code_demo.ipynb.bak
```

### [186] TOOL RESULT — Bash · 2026-08-21 19:58:49 UTC

```
{"stdout": "restored\n1", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [187] TOOL CALL — Bash · 2026-08-21 19:58:51 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
grep -n "invalid" code_demo.ipynb
```

### [188] TOOL RESULT — Bash · 2026-08-21 19:58:51 UTC

```
{"stdout": "129:    \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com.invalid/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json\\\"\\n\",", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [189] TOOL CALL — Bash · 2026-08-21 19:58:59 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
python3 << 'EOF'
import json
nb = json.load(open('code_demo.ipynb'))
c = nb['cells'][4]
print(type(c['source']))
EOF
```

### [190] TOOL RESULT — Bash · 2026-08-21 19:58:59 UTC

```
{"stdout": "<class 'list'>", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [191] ASSISTANT · 2026-08-21 19:59:03 UTC

```
Confirmed — source is now a list of lines after nbconvert rewrote it. Let me fix properly.
```

### [192] TOOL CALL — Bash · 2026-08-21 19:59:03 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
python3 << 'EOF'
import json
nb = json.load(open('code_demo.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        src = c['source']
        if isinstance(src, list):
            joined = ''.join(src)
            if 'GITHUB_DATA_URL' in joined:
                fixed = joined.replace('raw.githubusercontent.com.invalid', 'raw.githubusercontent.com')
                # re-split preserving newlines like nbformat expects
                lines = fixed.splitlines(keepends=True)
                c['source'] = lines
        else:
            if 'GITHUB_DATA_URL' in src:
                c['source'] = src.replace('raw.githubusercontent.com.invalid', 'raw.githubusercontent.com')
json.dump(nb, open('code_demo.ipynb','w'), indent=1)
print('fixed')
EOF
grep -n "invalid" code_demo.ipynb || echo "no invalid found - good"
```

### [193] TOOL RESULT — Bash · 2026-08-21 19:59:05 UTC

```
{"stdout": "fixed\nno invalid found - good", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [194] ASSISTANT · 2026-08-21 19:59:09 UTC

```
Now let's verify the exact URL string and clean up the venv/scratch files.
```

### [195] TOOL CALL — Bash · 2026-08-21 19:59:09 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
grep -n "GITHUB_DATA_URL = " code_demo.ipynb
echo "---"
python3 -c "
import json
nb = json.load(open('code_demo.ipynb'))
print(len(nb['cells']), 'cells')
"
rm -rf .nb_env
ls -la
```

### [196] TOOL RESULT — Bash · 2026-08-21 20:00:41 UTC

```
{"stdout": "129:    \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-2/dataset-1/demo/mini_demo_data.json\\\"\\n\",\n---\n14 cells\ntotal 3965\ndrwxr-xr-x 2 root root 1089103 Aug 21 20:00 .\ndrwxr-xr-x 5 root root 2057699 Aug 21 19:16 ..\n-rw-r--r-- 1 root root  751819 Aug 21 20:00 .repl_agent.ptylog\n-rw-r--r-- 1 root root   69627 Aug 21 19:59 code_demo.ipynb\n-rw-r--r-- 1 root root   90976 Aug 21 19:18 mini_demo_data.json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [197] ASSISTANT · 2026-08-21 20:00:47 UTC

```
The URL matches exactly the required string. Now let's verify the executed notebook's output looks correct.
```

### [198] TOOL CALL — Bash · 2026-08-21 20:00:47 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
python3 -c "
import json
nb = json.load(open('code_demo.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        for o in c.get('outputs', []):
            if o.get('output_type')=='error':
                print(i, 'ERROR', o.get('ename'), o.get('evalue'))
print('scan done')
"
```

### [199] TOOL RESULT — Bash · 2026-08-21 20:00:47 UTC

```
{"stdout": "scan done", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [200] ASSISTANT · 2026-08-21 20:00:53 UTC

```
All checks pass. Let's write the final struct output.
```

### [201] TOOL CALL — Bash · 2026-08-21 20:00:53 UTC

```
WS=/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_70BX2SQt9m6k
cat > "$WS/.terminal_claude_agent_struct_out.json" << 'EOF'
{
  "out_expected_files": {
    "notebook": "code_demo.ipynb",
    "mini_data_file": "mini_demo_data.json"
  }
}
EOF
cat "$WS/.terminal_claude_agent_struct_out.json"
```

### [202] TOOL RESULT — Bash · 2026-08-21 20:00:53 UTC

```
{"stdout": "{\n  \"out_expected_files\": {\n    \"notebook\": \"code_demo.ipynb\",\n    \"mini_data_file\": \"mini_demo_data.json\"\n  }\n}", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [203] ASSISTANT · 2026-08-21 20:00:56 UTC

```
Done. I built `code_demo.ipynb` (14 cells: setup, data loading with GitHub-URL/local-fallback pattern, config, `build_example` copied verbatim from `data.py`, the filtering/assembly logic mirroring `main()`, and a results table + scatter plot) alongside `mini_demo_data.json` (27 curated raw repo-mining records: 20 qualified repos balanced across survival labels, plus one example of each discard reason). Tested end-to-end in a clean venv via nbconvert — it executes without errors and produces the summary table and plot. The struct output file is written at `.terminal_claude_agent_struct_out.json`.
```
