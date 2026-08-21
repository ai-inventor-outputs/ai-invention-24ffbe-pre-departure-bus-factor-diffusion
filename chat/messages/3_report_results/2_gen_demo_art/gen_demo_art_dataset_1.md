# gen_demo_art_dataset_1 — report_results

> Phase: `gen_paper_repo` · `gen_demo_art`
> Run: `iter1_0b7b616dce39` — Does Pre-Departure Authority Diffusion Predict Open-Source Project Survival? A Unified-Corpus Retest with a Window-Boundary-Noise Control
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_demo_art_dataset_1` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-08-21 19:16:54 UTC

```
model: claude-sonnet-5 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu
```

### [2] SYSTEM-USER prompt · 2026-08-21 19:17:02 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/`:
GOOD: `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/file.py`, `/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/results/out.json`
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
out_demo_files:
- path: data.py
  description: Dataset fetching/generation script
</artifact_info>

<github_repo>
Repo URL: https://github.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion
Raw data URL: https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/dataset-1/demo/mini_demo_data.json

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
GITHUB_DATA_URL = "https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/dataset-1/demo/mini_demo_data.json"
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
TODO 6. Verify: (1) code_demo.ipynb contains GITHUB_DATA_URL = "https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/dataset-1/demo/mini_demo_data.json" exactly, (2) mini_demo_data.json exists, (3) uses GitHub URL pattern not just open('mini_demo_data.json').
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

### [3] HUMAN-USER prompt · 2026-08-21 19:17:02 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [4] TOOL CALL — Skill · 2026-08-21 19:17:06 UTC

```
aii-colab
```

### [5] TOOL CALL — Skill · 2026-08-21 19:17:06 UTC

```
aii-long-running-tasks
```

### [6] TOOL RESULT — Skill · 2026-08-21 19:17:06 UTC

```
{"success": true, "commandName": "aii-colab"}
```

### [7] TOOL RESULT — Skill · 2026-08-21 19:17:06 UTC

```
{"success": true, "commandName": "aii-long-running-tasks"}
```

### [8] TOOL CALL — Bash · 2026-08-21 19:17:06 UTC

```
ls /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/
```

### [9] TOOL RESULT — Bash · 2026-08-21 19:17:06 UTC

```
{"stdout": "__pycache__\ndata.py\nfull_data_out.json\nlogs\nmine_repo.py\nmini_data_out.json\npreview_data_out.json\npyproject.toml\nrun_mining.py\nsearch_candidates.py\ntemp", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [10] TOOL CALL — Read · 2026-08-21 19:17:10 UTC

```
/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/data.py
```

### [11] TOOL CALL — Bash · 2026-08-21 19:17:10 UTC

```
head -c 3000 /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/preview_data_out.json
```

### [12] TOOL RESULT — Read · 2026-08-21 19:17:10 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/data.py", "content": "#!/usr/bin/env python3\n\"\"\"Assemble mined repo results into the exp_sel_data_out.json schema:\none dataset group ('founder_departure_tfdd_corpus'), one example per\nqualifying repo. `input` = JSON of pre-TFDD/TFDD-snapshot covariates\n(the predictors); `output` = survival_label (the target). All raw\nper-year DOA/TF tables, TFDD metadata, and post-TFDD monthly series are\ncarried as metadata_* fields so downstream experiment code can recompute\nor verify authority-diffusion trajectories without re-cloning repos.\n\"\"\"\nimport glob\nimport json\nimport sys\nfrom pathlib import Path\n\nfrom loguru import logger\n\nlogger.remove()\nlogger.add(sys.stdout, level=\"INFO\", format=\"{time:HH:mm:ss}|{level:<7}|{message}\")\nlogger.add(\"logs/data.log\", rotation=\"10 MB\", level=\"DEBUG\")\n\nRESULTS_GLOB = \"temp/repo_results/*.json\"\nOUT_PATH = Path(\"full_data_out.json\")\n\n\ndef build_example(r: dict) -> dict:\n    pre = r[\"pre_tfdd_window\"]\n    cov = r[\"tfdd_snapshot_covariates\"]\n    input_features = {\n        \"founder_commit_share_pre_tfdd\": pre[\"founder_commit_share\"],\n        \"n_distinct_new_primary_owners_pre_tfdd\": pre[\"n_distinct_new_primary_owners\"],\n        \"founder_early_authorship_share\": r[\"founder_early_authorship_share\"],\n        \"stars\": cov[\"stars\"],\n        \"forks\": cov[\"forks\"],\n        \"total_contributors\": cov[\"total_contributors\"],\n        \"language\": cov[\"language\"],\n        \"license\": cov[\"license\"],\n        \"project_age_days\": cov[\"project_age_days\"],\n        \"n_commits_total\": r[\"n_commits\"],\n        \"n_files_total\": r[\"n_files\"],\n        \"history_span_years\": r[\"history_span_years\"],\n    }\n    example = {\n        \"input\": json.dumps(input_features, sort_keys=True),\n        \"output\": r[\"survival_label\"],\n        \"metadata_full_name\": r[\"full_name\"],\n        \"metadata_activity_bucket\": r[\"activity_bucket\"],\n        \"metadata_founder\": r[\"founder\"],\n        \"metadata_tfdd\": r[\"tfdd\"],\n        \"metadata_pre_tfdd_window\": pre,\n        \"metadata_tfdd_snapshot_covariates\": cov,\n        \"metadata_yearly_doa_tf_tables\": r[\"yearly_tables\"],\n        \"metadata_post_tfdd_monthly_commits\": r[\"post_tfdd_monthly_commits\"],\n        \"metadata_post_tfdd_months_available\": r[\"post_tfdd_months_available\"],\n        \"metadata_years_after_tfdd\": r[\"years_after_tfdd\"],\n        \"metadata_repo_meta\": r[\"meta\"],\n        \"metadata_repo_first_commit\": r[\"repo_first_commit\"],\n        \"metadata_repo_last_commit\": r[\"repo_last_commit\"],\n        \"metadata_task_type\": \"binary_classification\",\n        \"metadata_n_classes\": 2,\n    }\n    return example\n\n\ndef main():\n    files = sorted(glob.glob(RESULTS_GLOB))\n    logger.info(f\"Found {len(files)} mined repo result files\")\n    qualified = []\n    discard_reasons = {}\n    for f in files:\n        r = json.loads(Path(f).read_text())\n        if r.get(\"status\") == \"qualified\":\n            qualified.append(r)\n        else:\n            reason = r.get(\"discard_reason\", \"unknown\")\n            discard_reasons[reason] = discard_reasons.get(reason, 0) + 1\n    logger.info(f\"Qualified repos: {len(qualified)}\")\n    logger.info(f\"Discard reasons: {json.dumps(discard_reasons, indent=2)}\")\n\n    examples = [build_example(r) for r in qualified]\n    output = {\n        \"metadata\": {\n            \"source\": \"GitHub REST search API (candidate discovery) + git log (--filter=blob:none) \"\n                       \"for full commit history mining\",\n            \"description\": \"Single-founder GitHub repos with founder-only Truck-Factor-Developer-\"\n                            \"Detachment (TFDD) events, per Avelino et al. ICPC'16 (DOA/TF algorithm) \"\n                            \"and Avelino et al. ESEM'19 (TFDD/survival definitions). Each example is \"\n                            \"one qualifying repo; input=pre-TFDD/snapshot covariates, output=survival \"\n                            \"label (Active_survived / Inactive_did_not_survive).\",\n            \"n_qualified\": len(qualified),\n            \"discard_reason_counts\": discard_reasons,\n            \"doa_formula\": \"DOA(d,f) = 3.293 + 1.098*FirstAuthor(d,f) + 0.164*Deliveries(d,f) \"\n                           \"- 0.321*ln(1+Acceptances(d,f))\",\n            \"tf_algorithm\": \"greedy removal of highest-file-count DOA-primary-author while \"\n                            \"remaining-authors' file coverage >= 0.5\",\n        },\n        \"datasets\": [\n            {\"dataset\": \"founder_departure_tfdd_corpus\", \"examples\": examples}\n        ],\n    }\n    OUT_PATH.write_text(json.dumps(output, indent=2))\n    logger.info(f\"Wrote {len(examples)} examples to {OUT_PATH}\")\n\n\nif __name__ == \"__main__\":\n    main()\n", "numLines": 106, "startLine": 1, "totalLines": 106}}
```

### [13] TOOL RESULT — Bash · 2026-08-21 19:17:10 UTC

```
{"stdout": "{\n  \"metadata\": {\n    \"source\": \"GitHub REST search API (candidate discovery) + git log (--filter=blob:none) for full commit history mining\",\n    \"description\": \"Single-founder GitHub repos with founder-only Truck-Factor-Developer-Detachment (TFDD) events, per Avelino et al. ICPC'16 (DOA/TF algorithm) and Avelino et al. ESEM'19 (TFDD/survival definitions). Eac...\",\n    \"n_qualified\": 32,\n    \"discard_reason_counts\": {\n      \"no_qualifying_founder_only_tfdd\": 120,\n      \"too_few_commits\": 15,\n      \"non_software_repo_low_code_fraction\": 24,\n      \"right_censored_insufficient_post_tfdd_history\": 11,\n      \"mining_artifact_migration_squash\": 11,\n      \"too_large_history\": 3\n    },\n    \"doa_formula\": \"DOA(d,f) = 3.293 + 1.098*FirstAuthor(d,f) + 0.164*Deliveries(d,f) - 0.321*ln(1+Acceptances(d,f))\",\n    \"tf_algorithm\": \"greedy removal of highest-file-count DOA-primary-author while remaining-authors' file coverage >= 0.5\"\n  },\n  \"datasets\": [\n    {\n      \"dataset\": \"founder_departure_tfdd_corpus\",\n      \"examples\": [\n        {\n          \"input\": \"{\\\"forks\\\": 346, \\\"founder_commit_share_pre_tfdd\\\": 0.0, \\\"founder_early_authorship_share\\\": 0.68, \\\"history_span_years\\\": 7.67, \\\"language\\\": \\\"Go\\\", \\\"license\\\": null, \\\"n_commits_total\\\": 116, \\\"n_distinct_new_prim...\",\n          \"output\": \"Active_survived\",\n          \"metadata_full_name\": \"0xAX/go-algorithms\",\n          \"metadata_activity_bucket\": \"maintained\",\n          \"metadata_founder\": \"mail:testtest.89@mail.ru\",\n          \"metadata_tfdd\": {\n            \"year\": 2015,\n            \"date\": \"2015-12-31T00:00:00+00:00\",\n            \"developer\": \"mail:testtest.89@mail.ru\",\n            \"last_commit_date\": \"2014-08-12T18:08:36+00:00\",\n            \"silence_years\": 1.38\n          },\n          \"metadata_pre_tfdd_window\": {\n            \"window_start\": \"2014-12-31T00:00:00+00:00\",\n            \"window_end\": \"2015-12-31T00:00:00+00:00\",\n            \"founder_commit_share\": 0.0,\n            \"n_pre_window_commits\": 4,\n            \"n_distinct_new_primary_owners\": 2\n          },\n          \"metadata_tfdd_snapshot_covariates\": {\n            \"stars\": 1950,\n            \"forks\": 346,\n            \"total_contributors\": 22,\n            \"language\": \"Go\",\n            \"license\": null,\n            \"project_age_days\": 557\n          },\n          \"metadata_yearly_doa_tf_tables\": [\n            {\n              \"year\": 2014,\n              \"truck_factor\": 1,\n              \"tf_developers\": [\n                \"mail:testtest.89@mail.ru\"\n              ],\n              \"n_files\": 28,\n              \"n_active_authors_in_doa\": 3\n            },\n            {\n              \"year\": 2015,\n              \"truck_factor\": 1,\n              \"tf_developers\": [\n                \"mail:testtest.89@mail.ru\"\n              ],\n              \"n_files\": 28,\n              \"n_active_authors_in_doa\": 3\n            },\n            {\n              \"year\": 2016,\n              \"truck_factor\": 1,\n              \"tf_developers\": [\n                \"mail:testtest.89@mail.ru\"", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [14] TOOL CALL — Bash · 2026-08-21 19:17:18 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/
ls temp/repo_results 2>/dev/null | head -5
wc -c full_data_out.json mini_data_out.json
python3 -c "
import json
d=json.load(open('mini_data_out.json'))
print(json.dumps(d,indent=2)[:2000])
"
```

### [15] TOOL RESULT — Bash · 2026-08-21 19:17:18 UTC

```
{"stdout": "0xAX__go-algorithms.json\nA9T9__RPA.json\nActiveState__code.json\nBelval__pdf2image.json\nBetterErrors__better_errors.json\n178502 full_data_out.json\n 15564 mini_data_out.json\n194066 total\n{\n  \"metadata\": {\n    \"source\": \"GitHub REST search API (candidate discovery) + git log (--filter=blob:none) for full commit history mining\",\n    \"description\": \"Single-founder GitHub repos with founder-only Truck-Factor-Developer-Detachment (TFDD) events, per Avelino et al. ICPC'16 (DOA/TF algorithm) and Avelino et al. ESEM'19 (TFDD/survival definitions). Each example is one qualifying repo; input=pre-TFDD/snapshot covariates, output=survival label (Active_survived / Inactive_did_not_survive).\",\n    \"n_qualified\": 32,\n    \"discard_reason_counts\": {\n      \"no_qualifying_founder_only_tfdd\": 120,\n      \"too_few_commits\": 15,\n      \"non_software_repo_low_code_fraction\": 24,\n      \"right_censored_insufficient_post_tfdd_history\": 11,\n      \"mining_artifact_migration_squash\": 11,\n      \"too_large_history\": 3\n    },\n    \"doa_formula\": \"DOA(d,f) = 3.293 + 1.098*FirstAuthor(d,f) + 0.164*Deliveries(d,f) - 0.321*ln(1+Acceptances(d,f))\",\n    \"tf_algorithm\": \"greedy removal of highest-file-count DOA-primary-author while remaining-authors' file coverage >= 0.5\"\n  },\n  \"datasets\": [\n    {\n      \"dataset\": \"founder_departure_tfdd_corpus\",\n      \"examples\": [\n        {\n          \"input\": \"{\\\"forks\\\": 346, \\\"founder_commit_share_pre_tfdd\\\": 0.0, \\\"founder_early_authorship_share\\\": 0.68, \\\"history_span_years\\\": 7.67, \\\"language\\\": \\\"Go\\\", \\\"license\\\": null, \\\"n_commits_total\\\": 116, \\\"n_distinct_new_primary_owners_pre_tfdd\\\": 2, \\\"n_files_total\\\": 83, \\\"project_age_days\\\": 557, \\\"stars\\\": 1950, \\\"total_contributors\\\": 22}\",\n          \"output\": \"Active_survived\",\n          \"metadata_full_name\": \"0xAX/go-algorithms\",\n          \"metadata_activity_bucket\": \"maintained\",\n          \"metadata_founder\": \"mail:testtest.89@mail.ru\",\n          \"metadata_tfdd\": {\n            \"year\": 2015,\n            \"date\": \"2015-12-31T00:00:00+00:00\",\n            \"developer\": \"mail:testtest.89@mail.ru\",\n            \"last_commit_date\": \"2014-08-12T18:08:36+00:00\",\n            \"silence_years\": 1.38\n          },", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [16] TOOL CALL — Bash · 2026-08-21 19:17:24 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/
ls temp/repo_results | wc -l
python3 -c "
import json, glob
files = sorted(glob.glob('temp/repo_results/*.json'))
print(len(files))
statuses={}
for f in files:
    d=json.loads(open(f).read())
    s=d.get('status','?')
    statuses[s]=statuses.get(s,0)+1
print(statuses)
"
```

### [17] TOOL RESULT — Bash · 2026-08-21 19:17:30 UTC

```
{"stdout": "219\n219\n{'qualified': 32, 'discarded': 187}", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [18] TOOL CALL — Bash · 2026-08-21 19:17:34 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/
python3 -c "
import json, glob, random
files = sorted(glob.glob('temp/repo_results/*.json'))
qual=[]; disc=[]
for f in files:
    d=json.loads(open(f).read())
    (qual if d.get('status')=='qualified' else disc).append((f,d))
print('qual',len(qual),'disc',len(disc))
random.seed(0)
sel_q = qual[:15]
sel_d = disc[:10]
out = {}
for f,d in sel_q+sel_d:
    out[f.split('/')[-1]] = d
print(len(out))
import os
s=json.dumps(out)
print(len(s))
"
```

### [19] TOOL RESULT — Bash · 2026-08-21 19:17:38 UTC

```
{"stdout": "qual 32 disc 187\n25\n46229", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [20] ASSISTANT · 2026-08-21 19:17:42 UTC

```
46KB is fine. Let me write mini_demo_data.json to the workspace.
```

### [21] TOOL CALL — Bash · 2026-08-21 19:17:42 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/
python3 -c "
import json, glob
files = sorted(glob.glob('temp/repo_results/*.json'))
qual=[]; disc=[]
for f in files:
    d=json.loads(open(f).read())
    (qual if d.get('status')=='qualified' else disc).append((f,d))
sel_q = qual[:15]
sel_d = disc[:10]
out = {}
for f,d in sel_q+sel_d:
    out[f.split('/')[-1]] = d
with open('/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/mini_demo_data.json','w') as fh:
    json.dump(out, fh, indent=2)
print('done', len(out))
"
ls -la /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/
```

### [22] TOOL RESULT — Bash · 2026-08-21 19:17:46 UTC

```
{"stdout": "done 25\ntotal 2150\ndrwxr-xr-x 2 root root 1015756 Aug 21 19:17 .\ndrwxr-xr-x 4 root root 1023217 Aug 21 19:16 ..\n-rw-r--r-- 1 root root   95681 Aug 21 19:17 .repl_agent.ptylog\n-rw-r--r-- 1 root root   65665 Aug 21 19:17 mini_demo_data.json", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [23] ASSISTANT · 2026-08-21 19:17:48 UTC

```
Now let's build the notebook.
```

### [24] TOOL CALL — ToolSearch · 2026-08-21 19:17:48 UTC

```
{'query': 'select:NotebookEdit'}
```

### [25] TOOL RESULT — ToolSearch · 2026-08-21 19:17:48 UTC

```
{"matches": ["NotebookEdit"], "query": "select:NotebookEdit", "total_deferred_tools": 22}
```

### [26] TOOL CALL — Write · 2026-08-21 19:17:52 UTC

```
File: /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb

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

### [27] TOOL RESULT — Write · 2026-08-21 19:17:52 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb", "content": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": [\"# placeholder\"],\n   \"id\": \"cell-0\"\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"},\n  \"language_info\": {\"name\": \"python\", \"version\": \"3.12.0\"}\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [28] TOOL CALL — Read · 2026-08-21 19:17:54 UTC

```
/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb
```

### [29] TOOL RESULT — Read · 2026-08-21 19:17:54 UTC

```
{"type": "notebook", "file": {"filePath": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb", "cells": [{"cellType": "markdown", "source": "# placeholder", "cell_id": "cell-0"}]}}
```

### [30] TOOL CALL — NotebookEdit · 2026-08-21 19:18:02 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb', 'cell_id': 'cell-0', 'cell_type': 'markdown', 'new_source': "# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\\n"}
```

### [31] TOOL RESULT — NotebookEdit · 2026-08-21 19:18:02 UTC

```
{"new_source": "# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\\n", "old_source": "# placeholder", "cell_type": "markdown", "language": "python", "edit_mode": "replace", "cell_id": "cell-0", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": [\"# placeholder\"],\n   \"id\": \"cell-0\"\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"},\n  \"language_info\": {\"name\": \"python\", \"version\": \"3.12.0\"}\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}\n", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\\\n\\\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\\\n\\\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\\\n\\\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\\\n\\\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\\\\n\",\n   \"id\": \"cell-0\"\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [32] TOOL CALL — Read · 2026-08-21 19:18:08 UTC

```
/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb
```

### [33] TOOL RESULT — Read · 2026-08-21 19:18:08 UTC

```
{"type": "notebook", "file": {"filePath": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb", "cells": [{"cellType": "markdown", "source": "# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\\n", "cell_id": "cell-0"}]}}
```

### [34] ASSISTANT · 2026-08-21 19:18:14 UTC

```
Confirmed — literal `\n` got embedded. I need actual newlines in the parameter text.
```

### [35] TOOL CALL — NotebookEdit · 2026-08-21 19:18:14 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb', 'cell_id': 'cell-0', 'cell_type': 'markdown', 'new_source': "# Founder-Departure OSS Truck-Factor Corpus\n\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\n\n**Research question:** what determines whether an open-source project survives its founder stepping away?\n\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\n\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result."}
```

### [36] TOOL RESULT — NotebookEdit · 2026-08-21 19:18:14 UTC

```
{"new_source": "# Founder-Departure OSS Truck-Factor Corpus\n\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\n\n**Research question:** what determines whether an open-source project survives its founder stepping away?\n\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\n\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.", "old_source": "# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\\n", "cell_type": "markdown", "language": "python", "edit_mode": "replace", "cell_id": "cell-0", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\\\n\\\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\\\n\\\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\\\n\\\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\\\n\\\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\\\\n\",\n   \"id\": \"cell-0\"\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [37] ASSISTANT · 2026-08-21 19:18:20 UTC

```
Good. Now insert the install cell.
```

### [38] TOOL CALL — NotebookEdit · 2026-08-21 19:18:20 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb', 'cell_id': 'cell-0', 'edit_mode': 'insert', 'cell_type': 'markdown', 'new_source': "## Setup\n\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself."}
```

### [39] TOOL RESULT — NotebookEdit · 2026-08-21 19:18:20 UTC

```
{"new_source": "## Setup\n\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself.", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "479b7f13", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"479b7f13\",\n   \"source\": \"## Setup\\n\\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [40] TOOL CALL — NotebookEdit · 2026-08-21 19:18:24 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb', 'cell_id': '479b7f13', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': "import subprocess, sys\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\n\n# loguru — NOT pre-installed on Colab, always install\n_pip('loguru==0.7.3')\n\n# numpy, pandas, matplotlib — pre-installed on Colab, install locally only to match Colab's env\nif 'google.colab' not in sys.modules:\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')"}
```

### [41] TOOL RESULT — NotebookEdit · 2026-08-21 19:18:24 UTC

```
{"new_source": "import subprocess, sys\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\n\n# loguru — NOT pre-installed on Colab, always install\n_pip('loguru==0.7.3')\n\n# numpy, pandas, matplotlib — pre-installed on Colab, install locally only to match Colab's env\nif 'google.colab' not in sys.modules:\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "b7901ce1", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"479b7f13\",\n   \"source\": \"## Setup\\n\\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"479b7f13\",\n   \"source\": \"## Setup\\n\\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b7901ce1\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru — NOT pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, matplotlib — pre-installed on Colab, install locally only to match Colab's env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [42] TOOL CALL — NotebookEdit · 2026-08-21 19:18:28 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb', 'cell_id': 'b7901ce1', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': '# Imports — same as the original data.py, plus matplotlib/pandas for the results section\nimport glob\nimport json\nimport sys\nfrom pathlib import Path\n\nfrom loguru import logger\n\nimport pandas as pd\nimport matplotlib.pyplot as plt\n\nlogger.remove()\nlogger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")'}
```

### [43] TOOL RESULT — NotebookEdit · 2026-08-21 19:18:28 UTC

```
{"new_source": "# Imports — same as the original data.py, plus matplotlib/pandas for the results section\nimport glob\nimport json\nimport sys\nfrom pathlib import Path\n\nfrom loguru import logger\n\nimport pandas as pd\nimport matplotlib.pyplot as plt\n\nlogger.remove()\nlogger.add(sys.stdout, level=\"INFO\", format=\"{time:HH:mm:ss}|{level:<7}|{message}\")", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "0892f25a", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"479b7f13\",\n   \"source\": \"## Setup\\n\\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b7901ce1\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru — NOT pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, matplotlib — pre-installed on Colab, install locally only to match Colab's env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"479b7f13\",\n   \"source\": \"## Setup\\n\\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b7901ce1\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru — NOT pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, matplotlib — pre-installed on Colab, install locally only to match Colab's env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0892f25a\",\n   \"source\": \"# Imports — same as the original data.py, plus matplotlib/pandas for the results section\\nimport glob\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\n\\nimport pandas as pd\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [44] TOOL CALL — NotebookEdit · 2026-08-21 19:18:32 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb', 'cell_id': '0892f25a', 'edit_mode': 'insert', 'cell_type': 'markdown', 'new_source': '## Load demo data\n\n`mini_demo_data.json` is a curated subset of 25 raw per-repo mining results (15 `qualified`, 10 `discarded`) taken directly from `temp/repo_results/*.json` — the real intermediate files the full mining pipeline (`run_mining.py` / `mine_repo.py`) produces for each candidate repo, before `data.py` assembles them into the final dataset. Loading tries the GitHub-hosted copy first (for Colab), then falls back to the local file.'}
```

### [45] TOOL RESULT — NotebookEdit · 2026-08-21 19:18:34 UTC

```
{"new_source": "## Load demo data\n\n`mini_demo_data.json` is a curated subset of 25 raw per-repo mining results (15 `qualified`, 10 `discarded`) taken directly from `temp/repo_results/*.json` — the real intermediate files the full mining pipeline (`run_mining.py` / `mine_repo.py`) produces for each candidate repo, before `data.py` assembles them into the final dataset. Loading tries the GitHub-hosted copy first (for Colab), then falls back to the local file.", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "14feaa53", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"479b7f13\",\n   \"source\": \"## Setup\\n\\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b7901ce1\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru — NOT pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, matplotlib — pre-installed on Colab, install locally only to match Colab's env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0892f25a\",\n   \"source\": \"# Imports — same as the original data.py, plus matplotlib/pandas for the results section\\nimport glob\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\n\\nimport pandas as pd\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"479b7f13\",\n   \"source\": \"## Setup\\n\\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b7901ce1\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru — NOT pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, matplotlib — pre-installed on Colab, install locally only to match Colab's env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0892f25a\",\n   \"source\": \"# Imports — same as the original data.py, plus matplotlib/pandas for the results section\\nimport glob\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\n\\nimport pandas as pd\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"14feaa53\",\n   \"source\": \"## Load demo data\\n\\n`mini_demo_data.json` is a curated subset of 25 raw per-repo mining results (15 `qualified`, 10 `discarded`) taken directly from `temp/repo_results/*.json` — the real intermediate files the full mining pipeline (`run_mining.py` / `mine_repo.py`) produces for each candidate repo, before `data.py` assembles them into the final dataset. Loading tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [46] TOOL CALL — NotebookEdit · 2026-08-21 19:18:38 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb', 'cell_id': '14feaa53', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': 'GITHUB_DATA_URL = "https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/dataset-1/demo/mini_demo_data.json"\nimport json, os\n\ndef load_data():\n    try:\n        import urllib.request\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\n            return json.loads(response.read().decode())\n    except Exception: pass\n    if os.path.exists("mini_demo_data.json"):\n        with open("mini_demo_data.json") as f: return json.load(f)\n    raise FileNotFoundError("Could not load mini_demo_data.json")'}
```

### [47] TOOL RESULT — NotebookEdit · 2026-08-21 19:18:38 UTC

```
{"new_source": "GITHUB_DATA_URL = \"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/dataset-1/demo/mini_demo_data.json\"\nimport json, os\n\ndef load_data():\n    try:\n        import urllib.request\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\n            return json.loads(response.read().decode())\n    except Exception: pass\n    if os.path.exists(\"mini_demo_data.json\"):\n        with open(\"mini_demo_data.json\") as f: return json.load(f)\n    raise FileNotFoundError(\"Could not load mini_demo_data.json\")", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "0972d85b", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"479b7f13\",\n   \"source\": \"## Setup\\n\\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b7901ce1\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru — NOT pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, matplotlib — pre-installed on Colab, install locally only to match Colab's env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0892f25a\",\n   \"source\": \"# Imports — same as the original data.py, plus matplotlib/pandas for the results section\\nimport glob\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\n\\nimport pandas as pd\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"14feaa53\",\n   \"source\": \"## Load demo data\\n\\n`mini_demo_data.json` is a curated subset of 25 raw per-repo mining results (15 `qualified`, 10 `discarded`) taken directly from `temp/repo_results/*.json` — the real intermediate files the full mining pipeline (`run_mining.py` / `mine_repo.py`) produces for each candidate repo, before `data.py` assembles them into the final dataset. Loading tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"479b7f13\",\n   \"source\": \"## Setup\\n\\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b7901ce1\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru — NOT pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, matplotlib — pre-installed on Colab, install locally only to match Colab's env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0892f25a\",\n   \"source\": \"# Imports — same as the original data.py, plus matplotlib/pandas for the results section\\nimport glob\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\n\\nimport pandas as pd\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"14feaa53\",\n   \"source\": \"## Load demo data\\n\\n`mini_demo_data.json` is a curated subset of 25 raw per-repo mining results (15 `qualified`, 10 `discarded`) taken directly from `temp/repo_results/*.json` — the real intermediate files the full mining pipeline (`run_mining.py` / `mine_repo.py`) produces for each candidate repo, before `data.py` assembles them into the final dataset. Loading tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0972d85b\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/dataset-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [48] TOOL CALL — NotebookEdit · 2026-08-21 19:18:40 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb', 'cell_id': '0972d85b', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': 'data = load_data()\nprint(f"Loaded {len(data)} raw repo-mining result files")\nprint("Example keys:", list(data.keys())[:5])'}
```

### [49] TOOL RESULT — NotebookEdit · 2026-08-21 19:18:42 UTC

```
{"new_source": "data = load_data()\nprint(f\"Loaded {len(data)} raw repo-mining result files\")\nprint(\"Example keys:\", list(data.keys())[:5])", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "65f615bf", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"479b7f13\",\n   \"source\": \"## Setup\\n\\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b7901ce1\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru — NOT pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, matplotlib — pre-installed on Colab, install locally only to match Colab's env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0892f25a\",\n   \"source\": \"# Imports — same as the original data.py, plus matplotlib/pandas for the results section\\nimport glob\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\n\\nimport pandas as pd\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"14feaa53\",\n   \"source\": \"## Load demo data\\n\\n`mini_demo_data.json` is a curated subset of 25 raw per-repo mining results (15 `qualified`, 10 `discarded`) taken directly from `temp/repo_results/*.json` — the real intermediate files the full mining pipeline (`run_mining.py` / `mine_repo.py`) produces for each candidate repo, before `data.py` assembles them into the final dataset. Loading tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0972d85b\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/dataset-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"479b7f13\",\n   \"source\": \"## Setup\\n\\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b7901ce1\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru — NOT pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, matplotlib — pre-installed on Colab, install locally only to match Colab's env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0892f25a\",\n   \"source\": \"# Imports — same as the original data.py, plus matplotlib/pandas for the results section\\nimport glob\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\n\\nimport pandas as pd\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"14feaa53\",\n   \"source\": \"## Load demo data\\n\\n`mini_demo_data.json` is a curated subset of 25 raw per-repo mining results (15 `qualified`, 10 `discarded`) taken directly from `temp/repo_results/*.json` — the real intermediate files the full mining pipeline (`run_mining.py` / `mine_repo.py`) produces for each candidate repo, before `data.py` assembles them into the final dataset. Loading tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0972d85b\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/dataset-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"65f615bf\",\n   \"source\": \"data = load_data()\\nprint(f\\\"Loaded {len(data)} raw repo-mining result files\\\")\\nprint(\\\"Example keys:\\\", list(data.keys())[:5])\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [50] ASSISTANT · 2026-08-21 19:18:46 UTC

```
Now the config cell.
```

### [51] TOOL CALL — NotebookEdit · 2026-08-21 19:18:46 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb', 'cell_id': '65f615bf', 'edit_mode': 'insert', 'cell_type': 'markdown', 'new_source': "## Config\n\nThe original `data.py` has essentially one tunable knob: `RESULTS_GLOB`, the glob pattern selecting which mined per-repo result files to assemble. In the full pipeline this points at `temp/repo_results/*.json` (219 files: 32 qualified, 187 discarded). Here we start with the absolute minimum — a handful of files — and can scale up to the full `mini_demo_data.json` subset (25 files) in one step below, since that's all this demo ships with."}
```

### [52] TOOL RESULT — NotebookEdit · 2026-08-21 19:18:46 UTC

```
{"new_source": "## Config\n\nThe original `data.py` has essentially one tunable knob: `RESULTS_GLOB`, the glob pattern selecting which mined per-repo result files to assemble. In the full pipeline this points at `temp/repo_results/*.json` (219 files: 32 qualified, 187 discarded). Here we start with the absolute minimum — a handful of files — and can scale up to the full `mini_demo_data.json` subset (25 files) in one step below, since that's all this demo ships with.", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "0d4fcea0", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"479b7f13\",\n   \"source\": \"## Setup\\n\\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b7901ce1\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru — NOT pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, matplotlib — pre-installed on Colab, install locally only to match Colab's env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0892f25a\",\n   \"source\": \"# Imports — same as the original data.py, plus matplotlib/pandas for the results section\\nimport glob\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\n\\nimport pandas as pd\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"14feaa53\",\n   \"source\": \"## Load demo data\\n\\n`mini_demo_data.json` is a curated subset of 25 raw per-repo mining results (15 `qualified`, 10 `discarded`) taken directly from `temp/repo_results/*.json` — the real intermediate files the full mining pipeline (`run_mining.py` / `mine_repo.py`) produces for each candidate repo, before `data.py` assembles them into the final dataset. Loading tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0972d85b\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/dataset-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"65f615bf\",\n   \"source\": \"data = load_data()\\nprint(f\\\"Loaded {len(data)} raw repo-mining result files\\\")\\nprint(\\\"Example keys:\\\", list(data.keys())[:5])\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"479b7f13\",\n   \"source\": \"## Setup\\n\\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b7901ce1\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru — NOT pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, matplotlib — pre-installed on Colab, install locally only to match Colab's env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0892f25a\",\n   \"source\": \"# Imports — same as the original data.py, plus matplotlib/pandas for the results section\\nimport glob\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\n\\nimport pandas as pd\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"14feaa53\",\n   \"source\": \"## Load demo data\\n\\n`mini_demo_data.json` is a curated subset of 25 raw per-repo mining results (15 `qualified`, 10 `discarded`) taken directly from `temp/repo_results/*.json` — the real intermediate files the full mining pipeline (`run_mining.py` / `mine_repo.py`) produces for each candidate repo, before `data.py` assembles them into the final dataset. Loading tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0972d85b\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/dataset-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"65f615bf\",\n   \"source\": \"data = load_data()\\nprint(f\\\"Loaded {len(data)} raw repo-mining result files\\\")\\nprint(\\\"Example keys:\\\", list(data.keys())[:5])\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"0d4fcea0\",\n   \"source\": \"## Config\\n\\nThe original `data.py` has essentially one tunable knob: `RESULTS_GLOB`, the glob pattern selecting which mined per-repo result files to assemble. In the full pipeline this points at `temp/repo_results/*.json` (219 files: 32 qualified, 187 discarded). Here we start with the absolute minimum — a handful of files — and can scale up to the full `mini_demo_data.json` subset (25 files) in one step below, since that's all this demo ships with.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [53] TOOL CALL — NotebookEdit · 2026-08-21 19:18:50 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb', 'cell_id': '0d4fcea0', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': '# N_FILES: how many of the loaded raw mining-result files to assemble.\n# Start at the minimum (all 25 shipped in mini_demo_data.json — already tiny), scale up here if a larger\n# mini_demo_data.json is provided later.\nN_FILES = len(data)  # minimum useful value = all files in the demo subset'}
```

### [54] TOOL RESULT — NotebookEdit · 2026-08-21 19:18:50 UTC

```
{"new_source": "# N_FILES: how many of the loaded raw mining-result files to assemble.\n# Start at the minimum (all 25 shipped in mini_demo_data.json — already tiny), scale up here if a larger\n# mini_demo_data.json is provided later.\nN_FILES = len(data)  # minimum useful value = all files in the demo subset", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "efd0fe4a", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"479b7f13\",\n   \"source\": \"## Setup\\n\\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b7901ce1\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru — NOT pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, matplotlib — pre-installed on Colab, install locally only to match Colab's env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0892f25a\",\n   \"source\": \"# Imports — same as the original data.py, plus matplotlib/pandas for the results section\\nimport glob\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\n\\nimport pandas as pd\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"14feaa53\",\n   \"source\": \"## Load demo data\\n\\n`mini_demo_data.json` is a curated subset of 25 raw per-repo mining results (15 `qualified`, 10 `discarded`) taken directly from `temp/repo_results/*.json` — the real intermediate files the full mining pipeline (`run_mining.py` / `mine_repo.py`) produces for each candidate repo, before `data.py` assembles them into the final dataset. Loading tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0972d85b\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/dataset-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"65f615bf\",\n   \"source\": \"data = load_data()\\nprint(f\\\"Loaded {len(data)} raw repo-mining result files\\\")\\nprint(\\\"Example keys:\\\", list(data.keys())[:5])\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"0d4fcea0\",\n   \"source\": \"## Config\\n\\nThe original `data.py` has essentially one tunable knob: `RESULTS_GLOB`, the glob pattern selecting which mined per-repo result files to assemble. In the full pipeline this points at `temp/repo_results/*.json` (219 files: 32 qualified, 187 discarded). Here we start with the absolute minimum — a handful of files — and can scale up to the full `mini_demo_data.json` subset (25 files) in one step below, since that's all this demo ships with.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"479b7f13\",\n   \"source\": \"## Setup\\n\\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b7901ce1\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru — NOT pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, matplotlib — pre-installed on Colab, install locally only to match Colab's env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0892f25a\",\n   \"source\": \"# Imports — same as the original data.py, plus matplotlib/pandas for the results section\\nimport glob\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\n\\nimport pandas as pd\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"14feaa53\",\n   \"source\": \"## Load demo data\\n\\n`mini_demo_data.json` is a curated subset of 25 raw per-repo mining results (15 `qualified`, 10 `discarded`) taken directly from `temp/repo_results/*.json` — the real intermediate files the full mining pipeline (`run_mining.py` / `mine_repo.py`) produces for each candidate repo, before `data.py` assembles them into the final dataset. Loading tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0972d85b\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/dataset-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"65f615bf\",\n   \"source\": \"data = load_data()\\nprint(f\\\"Loaded {len(data)} raw repo-mining result files\\\")\\nprint(\\\"Example keys:\\\", list(data.keys())[:5])\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"0d4fcea0\",\n   \"source\": \"## Config\\n\\nThe original `data.py` has essentially one tunable knob: `RESULTS_GLOB`, the glob pattern selecting which mined per-repo result files to assemble. In the full pipeline this points at `temp/repo_results/*.json` (219 files: 32 qualified, 187 discarded). Here we start with the absolute minimum — a handful of files — and can scale up to the full `mini_demo_data.json` subset (25 files) in one step below, since that's all this demo ships with.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"efd0fe4a\",\n   \"source\": \"# N_FILES: how many of the loaded raw mining-result files to assemble.\\n# Start at the minimum (all 25 shipped in mini_demo_data.json — already tiny), scale up here if a larger\\n# mini_demo_data.json is provided later.\\nN_FILES = len(data)  # minimum useful value = all files in the demo subset\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [55] ASSISTANT · 2026-08-21 19:18:56 UTC

```
Now the processing cells — build_example (copied verbatim) and main-equivalent logic.
```

### [56] TOOL CALL — NotebookEdit · 2026-08-21 19:18:56 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb', 'cell_id': 'efd0fe4a', 'edit_mode': 'insert', 'cell_type': 'markdown', 'new_source': "## `build_example`: raw mined repo -> dataset example\n\nThis is `data.py`'s `build_example` function, copied as-is. It takes one raw mined repo-result dict (the pre-TFDD window, the TFDD-snapshot covariates, and the survival label) and turns it into one dataset example: `input` is a JSON string of the predictor covariates, `output` is the survival label, and everything else is carried as `metadata_*` fields for downstream verification without re-cloning the repo."}
```

### [57] TOOL RESULT — NotebookEdit · 2026-08-21 19:18:56 UTC

```
{"new_source": "## `build_example`: raw mined repo -> dataset example\n\nThis is `data.py`'s `build_example` function, copied as-is. It takes one raw mined repo-result dict (the pre-TFDD window, the TFDD-snapshot covariates, and the survival label) and turns it into one dataset example: `input` is a JSON string of the predictor covariates, `output` is the survival label, and everything else is carried as `metadata_*` fields for downstream verification without re-cloning the repo.", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "42b945f8", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"479b7f13\",\n   \"source\": \"## Setup\\n\\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b7901ce1\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru — NOT pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, matplotlib — pre-installed on Colab, install locally only to match Colab's env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0892f25a\",\n   \"source\": \"# Imports — same as the original data.py, plus matplotlib/pandas for the results section\\nimport glob\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\n\\nimport pandas as pd\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"14feaa53\",\n   \"source\": \"## Load demo data\\n\\n`mini_demo_data.json` is a curated subset of 25 raw per-repo mining results (15 `qualified`, 10 `discarded`) taken directly from `temp/repo_results/*.json` — the real intermediate files the full mining pipeline (`run_mining.py` / `mine_repo.py`) produces for each candidate repo, before `data.py` assembles them into the final dataset. Loading tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0972d85b\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/dataset-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"65f615bf\",\n   \"source\": \"data = load_data()\\nprint(f\\\"Loaded {len(data)} raw repo-mining result files\\\")\\nprint(\\\"Example keys:\\\", list(data.keys())[:5])\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"0d4fcea0\",\n   \"source\": \"## Config\\n\\nThe original `data.py` has essentially one tunable knob: `RESULTS_GLOB`, the glob pattern selecting which mined per-repo result files to assemble. In the full pipeline this points at `temp/repo_results/*.json` (219 files: 32 qualified, 187 discarded). Here we start with the absolute minimum — a handful of files — and can scale up to the full `mini_demo_data.json` subset (25 files) in one step below, since that's all this demo ships with.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"efd0fe4a\",\n   \"source\": \"# N_FILES: how many of the loaded raw mining-result files to assemble.\\n# Start at the minimum (all 25 shipped in mini_demo_data.json — already tiny), scale up here if a larger\\n# mini_demo_data.json is provided later.\\nN_FILES = len(data)  # minimum useful value = all files in the demo subset\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"479b7f13\",\n   \"source\": \"## Setup\\n\\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b7901ce1\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru — NOT pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, matplotlib — pre-installed on Colab, install locally only to match Colab's env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0892f25a\",\n   \"source\": \"# Imports — same as the original data.py, plus matplotlib/pandas for the results section\\nimport glob\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\n\\nimport pandas as pd\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"14feaa53\",\n   \"source\": \"## Load demo data\\n\\n`mini_demo_data.json` is a curated subset of 25 raw per-repo mining results (15 `qualified`, 10 `discarded`) taken directly from `temp/repo_results/*.json` — the real intermediate files the full mining pipeline (`run_mining.py` / `mine_repo.py`) produces for each candidate repo, before `data.py` assembles them into the final dataset. Loading tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0972d85b\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/dataset-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"65f615bf\",\n   \"source\": \"data = load_data()\\nprint(f\\\"Loaded {len(data)} raw repo-mining result files\\\")\\nprint(\\\"Example keys:\\\", list(data.keys())[:5])\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"0d4fcea0\",\n   \"source\": \"## Config\\n\\nThe original `data.py` has essentially one tunable knob: `RESULTS_GLOB`, the glob pattern selecting which mined per-repo result files to assemble. In the full pipeline this points at `temp/repo_results/*.json` (219 files: 32 qualified, 187 discarded). Here we start with the absolute minimum — a handful of files — and can scale up to the full `mini_demo_data.json` subset (25 files) in one step below, since that's all this demo ships with.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"efd0fe4a\",\n   \"source\": \"# N_FILES: how many of the loaded raw mining-result files to assemble.\\n# Start at the minimum (all 25 shipped in mini_demo_data.json — already tiny), scale up here if a larger\\n# mini_demo_data.json is provided later.\\nN_FILES = len(data)  # minimum useful value = all files in the demo subset\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"42b945f8\",\n   \"source\": \"## `build_example`: raw mined repo -> dataset example\\n\\nThis is `data.py`'s `build_example` function, copied as-is. It takes one raw mined repo-result dict (the pre-TFDD window, the TFDD-snapshot covariates, and the survival label) and turns it into one dataset example: `input` is a JSON string of the predictor covariates, `output` is the survival label, and everything else is carried as `metadata_*` fields for downstream verification without re-cloning the repo.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [58] TOOL CALL — NotebookEdit · 2026-08-21 19:19:02 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb', 'cell_id': '42b945f8', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': 'def build_example(r: dict) -> dict:\n    pre = r["pre_tfdd_window"]\n    cov = r["tfdd_snapshot_covariates"]\n    input_features = {\n        "founder_commit_share_pre_tfdd": pre["founder_commit_share"],\n        "n_distinct_new_primary_owners_pre_tfdd": pre["n_distinct_new_primary_owners"],\n        "founder_early_authorship_share": r["founder_early_authorship_share"],\n        "stars": cov["stars"],\n        "forks": cov["forks"],\n        "total_contributors": cov["total_contributors"],\n        "language": cov["language"],\n        "license": cov["license"],\n        "project_age_days": cov["project_age_days"],\n        "n_commits_total": r["n_commits"],\n        "n_files_total": r["n_files"],\n        "history_span_years": r["history_span_years"],\n    }\n    example = {\n        "input": json.dumps(input_features, sort_keys=True),\n        "output": r["survival_label"],\n        "metadata_full_name": r["full_name"],\n        "metadata_activity_bucket": r["activity_bucket"],\n        "metadata_founder": r["founder"],\n        "metadata_tfdd": r["tfdd"],\n        "metadata_pre_tfdd_window": pre,\n        "metadata_tfdd_snapshot_covariates": cov,\n        "metadata_yearly_doa_tf_tables": r["yearly_tables"],\n        "metadata_post_tfdd_monthly_commits": r["post_tfdd_monthly_commits"],\n        "metadata_post_tfdd_months_available": r["post_tfdd_months_available"],\n        "metadata_years_after_tfdd": r["years_after_tfdd"],\n        "metadata_repo_meta": r["meta"],\n        "metadata_repo_first_commit": r["repo_first_commit"],\n        "metadata_repo_last_commit": r["repo_last_commit"],\n        "metadata_task_type": "binary_classification",\n        "metadata_n_classes": 2,\n    }\n    return example'}
```

### [59] TOOL RESULT — NotebookEdit · 2026-08-21 19:19:02 UTC

```
{"new_source": "def build_example(r: dict) -> dict:\n    pre = r[\"pre_tfdd_window\"]\n    cov = r[\"tfdd_snapshot_covariates\"]\n    input_features = {\n        \"founder_commit_share_pre_tfdd\": pre[\"founder_commit_share\"],\n        \"n_distinct_new_primary_owners_pre_tfdd\": pre[\"n_distinct_new_primary_owners\"],\n        \"founder_early_authorship_share\": r[\"founder_early_authorship_share\"],\n        \"stars\": cov[\"stars\"],\n        \"forks\": cov[\"forks\"],\n        \"total_contributors\": cov[\"total_contributors\"],\n        \"language\": cov[\"language\"],\n        \"license\": cov[\"license\"],\n        \"project_age_days\": cov[\"project_age_days\"],\n        \"n_commits_total\": r[\"n_commits\"],\n        \"n_files_total\": r[\"n_files\"],\n        \"history_span_years\": r[\"history_span_years\"],\n    }\n    example = {\n        \"input\": json.dumps(input_features, sort_keys=True),\n        \"output\": r[\"survival_label\"],\n        \"metadata_full_name\": r[\"full_name\"],\n        \"metadata_activity_bucket\": r[\"activity_bucket\"],\n        \"metadata_founder\": r[\"founder\"],\n        \"metadata_tfdd\": r[\"tfdd\"],\n        \"metadata_pre_tfdd_window\": pre,\n        \"metadata_tfdd_snapshot_covariates\": cov,\n        \"metadata_yearly_doa_tf_tables\": r[\"yearly_tables\"],\n        \"metadata_post_tfdd_monthly_commits\": r[\"post_tfdd_monthly_commits\"],\n        \"metadata_post_tfdd_months_available\": r[\"post_tfdd_months_available\"],\n        \"metadata_years_after_tfdd\": r[\"years_after_tfdd\"],\n        \"metadata_repo_meta\": r[\"meta\"],\n        \"metadata_repo_first_commit\": r[\"repo_first_commit\"],\n        \"metadata_repo_last_commit\": r[\"repo_last_commit\"],\n        \"metadata_task_type\": \"binary_classification\",\n        \"metadata_n_classes\": 2,\n    }\n    return example", "cell_type": "code", "language": "python", "edit_mode": "insert", "cell_id": "75ccadea", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"479b7f13\",\n   \"source\": \"## Setup\\n\\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b7901ce1\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru — NOT pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, matplotlib — pre-installed on Colab, install locally only to match Colab's env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0892f25a\",\n   \"source\": \"# Imports — same as the original data.py, plus matplotlib/pandas for the results section\\nimport glob\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\n\\nimport pandas as pd\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"14feaa53\",\n   \"source\": \"## Load demo data\\n\\n`mini_demo_data.json` is a curated subset of 25 raw per-repo mining results (15 `qualified`, 10 `discarded`) taken directly from `temp/repo_results/*.json` — the real intermediate files the full mining pipeline (`run_mining.py` / `mine_repo.py`) produces for each candidate repo, before `data.py` assembles them into the final dataset. Loading tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0972d85b\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/dataset-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"65f615bf\",\n   \"source\": \"data = load_data()\\nprint(f\\\"Loaded {len(data)} raw repo-mining result files\\\")\\nprint(\\\"Example keys:\\\", list(data.keys())[:5])\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"0d4fcea0\",\n   \"source\": \"## Config\\n\\nThe original `data.py` has essentially one tunable knob: `RESULTS_GLOB`, the glob pattern selecting which mined per-repo result files to assemble. In the full pipeline this points at `temp/repo_results/*.json` (219 files: 32 qualified, 187 discarded). Here we start with the absolute minimum — a handful of files — and can scale up to the full `mini_demo_data.json` subset (25 files) in one step below, since that's all this demo ships with.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"efd0fe4a\",\n   \"source\": \"# N_FILES: how many of the loaded raw mining-result files to assemble.\\n# Start at the minimum (all 25 shipped in mini_demo_data.json — already tiny), scale up here if a larger\\n# mini_demo_data.json is provided later.\\nN_FILES = len(data)  # minimum useful value = all files in the demo subset\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"42b945f8\",\n   \"source\": \"## `build_example`: raw mined repo -> dataset example\\n\\nThis is `data.py`'s `build_example` function, copied as-is. It takes one raw mined repo-result dict (the pre-TFDD window, the TFDD-snapshot covariates, and the survival label) and turns it into one dataset example: `input` is a JSON string of the predictor covariates, `output` is the survival label, and everything else is carried as `metadata_*` fields for downstream verification without re-cloning the repo.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"479b7f13\",\n   \"source\": \"## Setup\\n\\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b7901ce1\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru — NOT pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, matplotlib — pre-installed on Colab, install locally only to match Colab's env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0892f25a\",\n   \"source\": \"# Imports — same as the original data.py, plus matplotlib/pandas for the results section\\nimport glob\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\n\\nimport pandas as pd\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"14feaa53\",\n   \"source\": \"## Load demo data\\n\\n`mini_demo_data.json` is a curated subset of 25 raw per-repo mining results (15 `qualified`, 10 `discarded`) taken directly from `temp/repo_results/*.json` — the real intermediate files the full mining pipeline (`run_mining.py` / `mine_repo.py`) produces for each candidate repo, before `data.py` assembles them into the final dataset. Loading tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0972d85b\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/dataset-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"65f615bf\",\n   \"source\": \"data = load_data()\\nprint(f\\\"Loaded {len(data)} raw repo-mining result files\\\")\\nprint(\\\"Example keys:\\\", list(data.keys())[:5])\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"0d4fcea0\",\n   \"source\": \"## Config\\n\\nThe original `data.py` has essentially one tunable knob: `RESULTS_GLOB`, the glob pattern selecting which mined per-repo result files to assemble. In the full pipeline this points at `temp/repo_results/*.json` (219 files: 32 qualified, 187 discarded). Here we start with the absolute minimum — a handful of files — and can scale up to the full `mini_demo_data.json` subset (25 files) in one step below, since that's all this demo ships with.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"efd0fe4a\",\n   \"source\": \"# N_FILES: how many of the loaded raw mining-result files to assemble.\\n# Start at the minimum (all 25 shipped in mini_demo_data.json — already tiny), scale up here if a larger\\n# mini_demo_data.json is provided later.\\nN_FILES = len(data)  # minimum useful value = all files in the demo subset\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"42b945f8\",\n   \"source\": \"## `build_example`: raw mined repo -> dataset example\\n\\nThis is `data.py`'s `build_example` function, copied as-is. It takes one raw mined repo-result dict (the pre-TFDD window, the TFDD-snapshot covariates, and the survival label) and turns it into one dataset example: `input` is a JSON string of the predictor covariates, `output` is the survival label, and everything else is carried as `metadata_*` fields for downstream verification without re-cloning the repo.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"75ccadea\",\n   \"source\": \"def build_example(r: dict) -> dict:\\n    pre = r[\\\"pre_tfdd_window\\\"]\\n    cov = r[\\\"tfdd_snapshot_covariates\\\"]\\n    input_features = {\\n        \\\"founder_commit_share_pre_tfdd\\\": pre[\\\"founder_commit_share\\\"],\\n        \\\"n_distinct_new_primary_owners_pre_tfdd\\\": pre[\\\"n_distinct_new_primary_owners\\\"],\\n        \\\"founder_early_authorship_share\\\": r[\\\"founder_early_authorship_share\\\"],\\n        \\\"stars\\\": cov[\\\"stars\\\"],\\n        \\\"forks\\\": cov[\\\"forks\\\"],\\n        \\\"total_contributors\\\": cov[\\\"total_contributors\\\"],\\n        \\\"language\\\": cov[\\\"language\\\"],\\n        \\\"license\\\": cov[\\\"license\\\"],\\n        \\\"project_age_days\\\": cov[\\\"project_age_days\\\"],\\n        \\\"n_commits_total\\\": r[\\\"n_commits\\\"],\\n        \\\"n_files_total\\\": r[\\\"n_files\\\"],\\n        \\\"history_span_years\\\": r[\\\"history_span_years\\\"],\\n    }\\n    example = {\\n        \\\"input\\\": json.dumps(input_features, sort_keys=True),\\n        \\\"output\\\": r[\\\"survival_label\\\"],\\n        \\\"metadata_full_name\\\": r[\\\"full_name\\\"],\\n        \\\"metadata_activity_bucket\\\": r[\\\"activity_bucket\\\"],\\n        \\\"metadata_founder\\\": r[\\\"founder\\\"],\\n        \\\"metadata_tfdd\\\": r[\\\"tfdd\\\"],\\n        \\\"metadata_pre_tfdd_window\\\": pre,\\n        \\\"metadata_tfdd_snapshot_covariates\\\": cov,\\n        \\\"metadata_yearly_doa_tf_tables\\\": r[\\\"yearly_tables\\\"],\\n        \\\"metadata_post_tfdd_monthly_commits\\\": r[\\\"post_tfdd_monthly_commits\\\"],\\n        \\\"metadata_post_tfdd_months_available\\\": r[\\\"post_tfdd_months_available\\\"],\\n        \\\"metadata_years_after_tfdd\\\": r[\\\"years_after_tfdd\\\"],\\n        \\\"metadata_repo_meta\\\": r[\\\"meta\\\"],\\n        \\\"metadata_repo_first_commit\\\": r[\\\"repo_first_commit\\\"],\\n        \\\"metadata_repo_last_commit\\\": r[\\\"repo_last_commit\\\"],\\n        \\\"metadata_task_type\\\": \\\"binary_classification\\\",\\n        \\\"metadata_n_classes\\\": 2,\\n    }\\n    return example\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [60] ASSISTANT · 2026-08-21 19:19:10 UTC

```
Now the main-logic cell (adapted minimally: iterate over `data` values instead of globbing files).
```

### [61] TOOL CALL — NotebookEdit · 2026-08-21 19:19:10 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb', 'cell_id': '75ccadea', 'edit_mode': 'insert', 'cell_type': 'markdown', 'new_source': "## `main`: assemble the corpus\n\nThis mirrors `data.py`'s `main()` exactly, with one minimal change: instead of `glob.glob(RESULTS_GLOB)` + `Path(f).read_text()` reading files off disk, it iterates the raw-result dicts already loaded into `data` (the in-memory equivalent of the same `temp/repo_results/*.json` files), limited to `N_FILES` from the config cell above. The qualified/discarded split, discard-reason tally, and `build_example` call are untouched."}
```

### [62] TOOL RESULT — NotebookEdit · 2026-08-21 19:19:10 UTC

```
{"new_source": "## `main`: assemble the corpus\n\nThis mirrors `data.py`'s `main()` exactly, with one minimal change: instead of `glob.glob(RESULTS_GLOB)` + `Path(f).read_text()` reading files off disk, it iterates the raw-result dicts already loaded into `data` (the in-memory equivalent of the same `temp/repo_results/*.json` files), limited to `N_FILES` from the config cell above. The qualified/discarded split, discard-reason tally, and `build_example` call are untouched.", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "0de9275b", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb", "original_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"479b7f13\",\n   \"source\": \"## Setup\\n\\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b7901ce1\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru — NOT pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, matplotlib — pre-installed on Colab, install locally only to match Colab's env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0892f25a\",\n   \"source\": \"# Imports — same as the original data.py, plus matplotlib/pandas for the results section\\nimport glob\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\n\\nimport pandas as pd\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"14feaa53\",\n   \"source\": \"## Load demo data\\n\\n`mini_demo_data.json` is a curated subset of 25 raw per-repo mining results (15 `qualified`, 10 `discarded`) taken directly from `temp/repo_results/*.json` — the real intermediate files the full mining pipeline (`run_mining.py` / `mine_repo.py`) produces for each candidate repo, before `data.py` assembles them into the final dataset. Loading tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0972d85b\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/dataset-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"65f615bf\",\n   \"source\": \"data = load_data()\\nprint(f\\\"Loaded {len(data)} raw repo-mining result files\\\")\\nprint(\\\"Example keys:\\\", list(data.keys())[:5])\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"0d4fcea0\",\n   \"source\": \"## Config\\n\\nThe original `data.py` has essentially one tunable knob: `RESULTS_GLOB`, the glob pattern selecting which mined per-repo result files to assemble. In the full pipeline this points at `temp/repo_results/*.json` (219 files: 32 qualified, 187 discarded). Here we start with the absolute minimum — a handful of files — and can scale up to the full `mini_demo_data.json` subset (25 files) in one step below, since that's all this demo ships with.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"efd0fe4a\",\n   \"source\": \"# N_FILES: how many of the loaded raw mining-result files to assemble.\\n# Start at the minimum (all 25 shipped in mini_demo_data.json — already tiny), scale up here if a larger\\n# mini_demo_data.json is provided later.\\nN_FILES = len(data)  # minimum useful value = all files in the demo subset\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"42b945f8\",\n   \"source\": \"## `build_example`: raw mined repo -> dataset example\\n\\nThis is `data.py`'s `build_example` function, copied as-is. It takes one raw mined repo-result dict (the pre-TFDD window, the TFDD-snapshot covariates, and the survival label) and turns it into one dataset example: `input` is a JSON string of the predictor covariates, `output` is the survival label, and everything else is carried as `metadata_*` fields for downstream verification without re-cloning the repo.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"75ccadea\",\n   \"source\": \"def build_example(r: dict) -> dict:\\n    pre = r[\\\"pre_tfdd_window\\\"]\\n    cov = r[\\\"tfdd_snapshot_covariates\\\"]\\n    input_features = {\\n        \\\"founder_commit_share_pre_tfdd\\\": pre[\\\"founder_commit_share\\\"],\\n        \\\"n_distinct_new_primary_owners_pre_tfdd\\\": pre[\\\"n_distinct_new_primary_owners\\\"],\\n        \\\"founder_early_authorship_share\\\": r[\\\"founder_early_authorship_share\\\"],\\n        \\\"stars\\\": cov[\\\"stars\\\"],\\n        \\\"forks\\\": cov[\\\"forks\\\"],\\n        \\\"total_contributors\\\": cov[\\\"total_contributors\\\"],\\n        \\\"language\\\": cov[\\\"language\\\"],\\n        \\\"license\\\": cov[\\\"license\\\"],\\n        \\\"project_age_days\\\": cov[\\\"project_age_days\\\"],\\n        \\\"n_commits_total\\\": r[\\\"n_commits\\\"],\\n        \\\"n_files_total\\\": r[\\\"n_files\\\"],\\n        \\\"history_span_years\\\": r[\\\"history_span_years\\\"],\\n    }\\n    example = {\\n        \\\"input\\\": json.dumps(input_features, sort_keys=True),\\n        \\\"output\\\": r[\\\"survival_label\\\"],\\n        \\\"metadata_full_name\\\": r[\\\"full_name\\\"],\\n        \\\"metadata_activity_bucket\\\": r[\\\"activity_bucket\\\"],\\n        \\\"metadata_founder\\\": r[\\\"founder\\\"],\\n        \\\"metadata_tfdd\\\": r[\\\"tfdd\\\"],\\n        \\\"metadata_pre_tfdd_window\\\": pre,\\n        \\\"metadata_tfdd_snapshot_covariates\\\": cov,\\n        \\\"metadata_yearly_doa_tf_tables\\\": r[\\\"yearly_tables\\\"],\\n        \\\"metadata_post_tfdd_monthly_commits\\\": r[\\\"post_tfdd_monthly_commits\\\"],\\n        \\\"metadata_post_tfdd_months_available\\\": r[\\\"post_tfdd_months_available\\\"],\\n        \\\"metadata_years_after_tfdd\\\": r[\\\"years_after_tfdd\\\"],\\n        \\\"metadata_repo_meta\\\": r[\\\"meta\\\"],\\n        \\\"metadata_repo_first_commit\\\": r[\\\"repo_first_commit\\\"],\\n        \\\"metadata_repo_last_commit\\\": r[\\\"repo_last_commit\\\"],\\n        \\\"metadata_task_type\\\": \\\"binary_classification\\\",\\n        \\\"metadata_n_classes\\\": 2,\\n    }\\n    return example\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}", "updated_file": "{\n \"cells\": [\n  {\n   \"cell_type\": \"markdown\",\n   \"metadata\": {},\n   \"source\": \"# Founder-Departure OSS Truck-Factor Corpus\\n\\nThis notebook demonstrates the **assembly step** of the Founder-Departure OSS Truck-Factor Corpus dataset.\\n\\n**Research question:** what determines whether an open-source project survives its founder stepping away?\\n\\nThe full pipeline mines GitHub repositories (`search_candidates.py`, `mine_repo.py`, `run_mining.py`) to compute, per repo and per year, the **Degree-of-Authorship (DOA)** metric and the **Truck Factor (TF)** from Avelino et al. (ICPC 2016), then flags a **Truck-Factor-Developer-Detachment (TFDD)** event: the first year the sole truck-factor developer (who is also the project's founder) has gone silent for >= 1 year. Repos with a qualifying founder-only TFDD plus >= 3 years of subsequent history are kept; the rest are discarded and logged with a reason.\\n\\nThis notebook runs the **final assembly script, `data.py`**, exactly as written, over a small subset of the raw per-repo mining outputs (`temp/repo_results/*.json`) that would normally be produced by the (expensive, GitHub-API-bound) mining scripts. It builds the same `input`/`output` example schema as the full corpus and visualizes the result.\",\n   \"id\": \"cell-0\"\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"479b7f13\",\n   \"source\": \"## Setup\\n\\nInstall dependencies. `loguru` is not pre-installed on Colab; core scientific packages (numpy, pandas, matplotlib) are pinned to Colab's exact versions when running locally, and left untouched on Colab itself.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"b7901ce1\",\n   \"source\": \"import subprocess, sys\\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\\n\\n# loguru — NOT pre-installed on Colab, always install\\n_pip('loguru==0.7.3')\\n\\n# numpy, pandas, matplotlib — pre-installed on Colab, install locally only to match Colab's env\\nif 'google.colab' not in sys.modules:\\n    _pip('numpy==2.0.2', 'pandas==2.2.2', 'matplotlib==3.10.0')\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0892f25a\",\n   \"source\": \"# Imports — same as the original data.py, plus matplotlib/pandas for the results section\\nimport glob\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\nfrom loguru import logger\\n\\nimport pandas as pd\\nimport matplotlib.pyplot as plt\\n\\nlogger.remove()\\nlogger.add(sys.stdout, level=\\\"INFO\\\", format=\\\"{time:HH:mm:ss}|{level:<7}|{message}\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"14feaa53\",\n   \"source\": \"## Load demo data\\n\\n`mini_demo_data.json` is a curated subset of 25 raw per-repo mining results (15 `qualified`, 10 `discarded`) taken directly from `temp/repo_results/*.json` — the real intermediate files the full mining pipeline (`run_mining.py` / `mine_repo.py`) produces for each candidate repo, before `data.py` assembles them into the final dataset. Loading tries the GitHub-hosted copy first (for Colab), then falls back to the local file.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"0972d85b\",\n   \"source\": \"GITHUB_DATA_URL = \\\"https://raw.githubusercontent.com/ai-inventor-outputs/ai-invention-24ffbe-pre-departure-bus-factor-diffusion/main/round-1/dataset-1/demo/mini_demo_data.json\\\"\\nimport json, os\\n\\ndef load_data():\\n    try:\\n        import urllib.request\\n        with urllib.request.urlopen(GITHUB_DATA_URL) as response:\\n            return json.loads(response.read().decode())\\n    except Exception: pass\\n    if os.path.exists(\\\"mini_demo_data.json\\\"):\\n        with open(\\\"mini_demo_data.json\\\") as f: return json.load(f)\\n    raise FileNotFoundError(\\\"Could not load mini_demo_data.json\\\")\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"65f615bf\",\n   \"source\": \"data = load_data()\\nprint(f\\\"Loaded {len(data)} raw repo-mining result files\\\")\\nprint(\\\"Example keys:\\\", list(data.keys())[:5])\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"0d4fcea0\",\n   \"source\": \"## Config\\n\\nThe original `data.py` has essentially one tunable knob: `RESULTS_GLOB`, the glob pattern selecting which mined per-repo result files to assemble. In the full pipeline this points at `temp/repo_results/*.json` (219 files: 32 qualified, 187 discarded). Here we start with the absolute minimum — a handful of files — and can scale up to the full `mini_demo_data.json` subset (25 files) in one step below, since that's all this demo ships with.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"efd0fe4a\",\n   \"source\": \"# N_FILES: how many of the loaded raw mining-result files to assemble.\\n# Start at the minimum (all 25 shipped in mini_demo_data.json — already tiny), scale up here if a larger\\n# mini_demo_data.json is provided later.\\nN_FILES = len(data)  # minimum useful value = all files in the demo subset\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"42b945f8\",\n   \"source\": \"## `build_example`: raw mined repo -> dataset example\\n\\nThis is `data.py`'s `build_example` function, copied as-is. It takes one raw mined repo-result dict (the pre-TFDD window, the TFDD-snapshot covariates, and the survival label) and turns it into one dataset example: `input` is a JSON string of the predictor covariates, `output` is the survival label, and everything else is carried as `metadata_*` fields for downstream verification without re-cloning the repo.\",\n   \"metadata\": {}\n  },\n  {\n   \"cell_type\": \"code\",\n   \"id\": \"75ccadea\",\n   \"source\": \"def build_example(r: dict) -> dict:\\n    pre = r[\\\"pre_tfdd_window\\\"]\\n    cov = r[\\\"tfdd_snapshot_covariates\\\"]\\n    input_features = {\\n        \\\"founder_commit_share_pre_tfdd\\\": pre[\\\"founder_commit_share\\\"],\\n        \\\"n_distinct_new_primary_owners_pre_tfdd\\\": pre[\\\"n_distinct_new_primary_owners\\\"],\\n        \\\"founder_early_authorship_share\\\": r[\\\"founder_early_authorship_share\\\"],\\n        \\\"stars\\\": cov[\\\"stars\\\"],\\n        \\\"forks\\\": cov[\\\"forks\\\"],\\n        \\\"total_contributors\\\": cov[\\\"total_contributors\\\"],\\n        \\\"language\\\": cov[\\\"language\\\"],\\n        \\\"license\\\": cov[\\\"license\\\"],\\n        \\\"project_age_days\\\": cov[\\\"project_age_days\\\"],\\n        \\\"n_commits_total\\\": r[\\\"n_commits\\\"],\\n        \\\"n_files_total\\\": r[\\\"n_files\\\"],\\n        \\\"history_span_years\\\": r[\\\"history_span_years\\\"],\\n    }\\n    example = {\\n        \\\"input\\\": json.dumps(input_features, sort_keys=True),\\n        \\\"output\\\": r[\\\"survival_label\\\"],\\n        \\\"metadata_full_name\\\": r[\\\"full_name\\\"],\\n        \\\"metadata_activity_bucket\\\": r[\\\"activity_bucket\\\"],\\n        \\\"metadata_founder\\\": r[\\\"founder\\\"],\\n        \\\"metadata_tfdd\\\": r[\\\"tfdd\\\"],\\n        \\\"metadata_pre_tfdd_window\\\": pre,\\n        \\\"metadata_tfdd_snapshot_covariates\\\": cov,\\n        \\\"metadata_yearly_doa_tf_tables\\\": r[\\\"yearly_tables\\\"],\\n        \\\"metadata_post_tfdd_monthly_commits\\\": r[\\\"post_tfdd_monthly_commits\\\"],\\n        \\\"metadata_post_tfdd_months_available\\\": r[\\\"post_tfdd_months_available\\\"],\\n        \\\"metadata_years_after_tfdd\\\": r[\\\"years_after_tfdd\\\"],\\n        \\\"metadata_repo_meta\\\": r[\\\"meta\\\"],\\n        \\\"metadata_repo_first_commit\\\": r[\\\"repo_first_commit\\\"],\\n        \\\"metadata_repo_last_commit\\\": r[\\\"repo_last_commit\\\"],\\n        \\\"metadata_task_type\\\": \\\"binary_classification\\\",\\n        \\\"metadata_n_classes\\\": 2,\\n    }\\n    return example\",\n   \"metadata\": {},\n   \"execution_count\": null,\n   \"outputs\": []\n  },\n  {\n   \"cell_type\": \"markdown\",\n   \"id\": \"0de9275b\",\n   \"source\": \"## `main`: assemble the corpus\\n\\nThis mirrors `data.py`'s `main()` exactly, with one minimal change: instead of `glob.glob(RESULTS_GLOB)` + `Path(f).read_text()` reading files off disk, it iterates the raw-result dicts already loaded into `data` (the in-memory equivalent of the same `temp/repo_results/*.json` files), limited to `N_FILES` from the config cell above. The qualified/discarded split, discard-reason tally, and `build_example` call are untouched.\",\n   \"metadata\": {}\n  }\n ],\n \"metadata\": {\n  \"kernelspec\": {\n   \"display_name\": \"Python 3\",\n   \"language\": \"python\",\n   \"name\": \"python3\"\n  },\n  \"language_info\": {\n   \"name\": \"python\",\n   \"version\": \"3.12.0\"\n  }\n },\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}"}
```

### [63] TOOL CALL — NotebookEdit · 2026-08-21 19:19:18 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb', 'cell_id': '0de9275b', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': 'files = list(data.items())[:N_FILES]\nlogger.info(f"Found {len(files)} mined repo result files")\nqualified = []\ndiscard_reasons = {}\nfor fname, r in files:\n    if r.get("status") == "qualified":\n        qualified.append(r)\n    else:\n        reason = r.get("discard_reason", "unknown")\n        discard_reasons[reason] = discard_reasons.get(reason, 0) + 1\nlogger.info(f"Qualified repos: {len(qualified)}")\nlogger.info(f"Discard reasons: {json.dumps(discard_reasons, indent=2)}")\n\nexamples = [build_example(r) for r in qualified]\noutput = {\n    "metadata": {\n        "source": "GitHub REST search API (candidate discovery) + git log (--filter=blob:none) "\n                   "for full commit history mining",\n        "description": "Single-founder GitHub repos with founder-only Truck-Factor-Developer-"\n                        "Detachment (TFDD) events, per Avelino et al. ICPC\'16 (DOA/TF algorithm) "\n                        "and Avelino et al. ESEM\'19 (TFDD/survival definitions). Each example is "\n                        "one qualifying repo; input=pre-TFDD/snapshot covariates, output=survival "\n                        "label (Active_survived / Inactive_did_not_survive).",\n        "n_qualified": len(qualified),\n        "discard_reason_counts": discard_reasons,\n        "doa_formula": "DOA(d,f) = 3.293 + 1.098*FirstAuthor(d,f) + 0.164*Deliveries(d,f) "\n                       "- 0.321*ln(1+Acceptances(d,f))",\n        "tf_algorithm": "greedy removal of highest-file-count DOA-primary-author while "\n                        "remaining-authors\' file coverage >= 0.5",\n    },\n    "datasets": [\n        {"dataset": "founder_departure_tfdd_corpus", "examples": examples}\n    ],\n}\nlogger.info(f"Assembled {len(examples)} examples into the corpus (in-memory, not written to disk in this demo)")'}
```

### [64] TOOL RESULT — NotebookEdit · 2026-08-21 19:19:18 UTC

```
{"new_source": "files = list(data.items())[:N_FILES]\nlogger.info(f\"Found {len(files)} mined repo result files\")\nqualified = []\ndiscard_reasons = {}\nfor fname, r in files:\n    if r.get(\"status\") == \"qualified\":\n        qualified.append(r)\n    else:\n        reason = r.get(\"discard_reason\", \"unknown\")\n        discard_reasons[reason] = discard_reasons.get(reason, 0) + 1\nlogger.info(f\"Qualified repos: {len(qualified)}\")\nlogger.info(f\"Discard reasons:... [truncated, 22646 chars total]
```

### [65] ASSISTANT · 2026-08-21 19:19:24 UTC

```
Now results/visualization cell.
```

### [66] TOOL CALL — NotebookEdit · 2026-08-21 19:19:24 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb', 'cell_id': '911f36da', 'edit_mode': 'insert', 'cell_type': 'markdown', 'new_source': '## Results\n\nA look at the assembled examples: the survival-label distribution, the discard-reason breakdown, and the predictor covariates (`input`) for the qualified repos.'}
```

### [67] TOOL RESULT — NotebookEdit · 2026-08-21 19:19:24 UTC

```
{"new_source": "## Results\n\nA look at the assembled examples: the survival-label distribution, the discard-reason breakdown, and the predictor covariates (`input`) for the qualified repos.", "cell_type": "markdown", "language": "python", "edit_mode": "insert", "cell_id": "94f36d85", "error": "", "notebook_path": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb", "original_file": ... [truncated, 23428 chars total]
```

### [68] TOOL CALL — NotebookEdit · 2026-08-21 19:19:30 UTC

```
{'notebook_path': '/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/code_demo.ipynb', 'cell_id': '94f36d85', 'edit_mode': 'insert', 'cell_type': 'code', 'new_source': 'df = pd.DataFrame([\n    {"full_name": ex["metadata_full_name"], "survival_label": ex["output"],\n     **json.loads(ex["input"])}\n    for ex in examples\n])\nprint(f"{len(examples)} qualified examples assembled\\n")\nprint(df[["full_name", "survival_label", "language", "stars", "founder_commit_share_pre_tfdd",\n          "n_distinct_new_primary_owners_pre_tfdd"]].to_string(index=False))\n\nfig, axes = plt.subplots(1, 2, figsize=(11, 4))\n\ndf["survival_label"].value_counts().plot(kind="bar", ax=axes[0], color=["#4C72B0", "#DD8452"])\naxes[0].set_title("Survival label distribution (qualified repos)")\naxes[0].set_ylabel("count")\naxes[0].tick_params(axis="x", rotation=20)\n\npd.Series(discard_reasons).sort_values().plot(kind="barh", ax=axes[1], color="#55A868")\naxes[1].set_title("Discard reasons (non-qualifying repos)")\naxes[1].set_xlabel("count")\n\nplt.tight_layout()\nplt.show()'}
```

### [69] TOOL RESULT — NotebookEdit · 2026-08-21 19:19:30 UTC

```
{"new_source": "df = pd.DataFrame([\n    {\"full_name\": ex[\"metadata_full_name\"], \"survival_label\": ex[\"output\"],\n     **json.loads(ex[\"input\"])}\n    for ex in examples\n])\nprint(f\"{len(examples)} qualified examples assembled\\n\")\nprint(df[[\"full_name\", \"survival_label\", \"language\", \"stars\", \"founder_commit_share_pre_tfdd\",\n          \"n_distinct_new_primary_owners_pre_tfdd\"]].to_string(index=False))\n\nfig, axes = plt.subplots(1, 2, figsize=... [truncated, 25697 chars total]
```

### [70] ASSISTANT · 2026-08-21 19:19:34 UTC

```
Now let's test-run the notebook in a clean venv.
```

### [71] TOOL CALL — Bash · 2026-08-21 19:19:34 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu
/usr/local/bin/python3.12 -m venv .nb_env 2>&1 | tail -5
.nb_env/bin/pip install -q pip jupyter ipykernel 2>&1 | tail -10
```

### [72] TOOL RESULT — Bash · 2026-08-21 19:22:34 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bg4f2deo9", "timedOutAfterMs": 180000, "backgroundCwdHint": "Session cwd remains /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu; directory changes made by the backgrounded command do not apply to subsequent commands."}
```

### [73] ASSISTANT · 2026-08-21 19:22:38 UTC

```
Waiting on venv setup in background.
```

### [74] TOOL CALL — Bash · 2026-08-21 19:22:38 UTC

```
sleep 60; cat /tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-1-art-24Q1bYB-ULpu/132d2d25-9c0f-4f2b-b441-3c00b4b54ee1/tasks/bg4f2deo9.output
```

### [75] TOOL RESULT — Bash [ERROR] · 2026-08-21 19:22:38 UTC

```
Error: Blocked: sleep 60 followed by: cat /tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-1-art-24Q1bYB-ULpu/132d2d25-9c0f-4f2b-b441-3c00b4b54ee1/tasks/bg4f2deo9.output. To wait for a condition, use Monitor with an until-loop (e.g. `until <check>; do sleep 2; done`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block.
```

### [76] TOOL CALL — Read · 2026-08-21 19:22:40 UTC

```
/tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-1-art-24Q1bYB-ULpu/132d2d25-9c0f-4f2b-b441-3c00b4b54ee1/tasks/bg4f2deo9.output
```

### [77] TOOL RESULT — Read · 2026-08-21 19:22:40 UTC

```
{"type": "text", "file": {"filePath": "/tmp/claude-0/-ai-inventor-aii-data-runs-run-fvTNuFE3-z80-4-gen-paper-repo--3-gen-demo-art-notebook-workspaces-iter-1-art-24Q1bYB-ULpu/132d2d25-9c0f-4f2b-b441-3c00b4b54ee1/tasks/bg4f2deo9.output", "content": "", "numLines": 1, "startLine": 1, "totalLines": 1}}
```

### [78] TOOL CALL — ToolSearch · 2026-08-21 19:22:42 UTC

```
{'query': 'select:Monitor'}
```

### [79] TOOL RESULT — ToolSearch · 2026-08-21 19:22:42 UTC

```
{"matches": ["Monitor"], "query": "select:Monitor", "total_deferred_tools": 22}
```

### [80] TOOL CALL — Monitor · 2026-08-21 19:22:48 UTC

```
{'description': 'wait for pip install of jupyter/ipykernel to finish', 'command': 'cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu\nuntil .nb_env/bin/python -c "import jupyter, ipykernel" 2>/dev/null; do sleep 3; done\necho "READY"', 'timeout_ms': 240000}
```

### [81] TOOL RESULT — Monitor · 2026-08-21 19:22:48 UTC

```
{"taskId": "bflxsdw1i", "timeoutMs": 240000, "persistent": false}
```

### [82] ASSISTANT · 2026-08-21 19:22:48 UTC

```
I'll wait for that to finish before running the notebook.
```

### [83] TOOL CALL — Bash · 2026-08-21 19:22:48 UTC

```
echo waiting
```

### [84] TOOL RESULT — Bash · 2026-08-21 19:22:48 UTC

```
{"stdout": "waiting", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [85] TOOL CALL — Bash · 2026-08-21 19:22:50 UTC

```
true
```

### [86] TOOL RESULT — Bash · 2026-08-21 19:22:51 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [87] ASSISTANT · 2026-08-21 19:22:55 UTC

```
I'll wait for the monitor notification before proceeding.
```

### [88] TOOL CALL — Bash · 2026-08-21 19:22:55 UTC

```
:
```

### [89] TOOL RESULT — Bash · 2026-08-21 19:22:55 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [90] TOOL CALL — Bash · 2026-08-21 19:22:59 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu
.nb_env/bin/python -c "import jupyter, ipykernel; print('OK')" 2>&1
```

### [91] TOOL RESULT — Bash [ERROR] · 2026-08-21 19:22:59 UTC

```
Error: Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'jupyter'
```

### [92] ASSISTANT · 2026-08-21 19:23:01 UTC

```
Still installing. Let me check the pip process directly.
```

### [93] TOOL CALL — Bash · 2026-08-21 19:23:01 UTC

```
ps aux | grep -i "pip install" | grep -v grep
```

### [94] TOOL RESULT — Bash · 2026-08-21 19:23:01 UTC

```
{"stdout": "root         197  0.0  0.0   4492  1544 ?        Ss   19:19   0:00 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1787339825594-96ohf3.sh 2>/dev/null || true && shopt -u extglob 2>/dev/null || true && { \\builtin unalias -- 'unsetenv'; \\builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu /usr/local/bin/python3.12 -m venv .nb_env 2>&1 | tail -5 .nb_env/bin/pip install -q pip jupyter ipykernel 2>&1 | tail -10' < /dev/null && pwd -P >| /tmp/claude-f99d-cwd\nroot         206  7.0  0.0  99256 92200 ?        S    19:20   0:10 /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/.nb_env/bin/python3.12 .nb_env/bin/pip install -q pip jupyter ipykernel", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [95] ASSISTANT · 2026-08-21 19:23:03 UTC

```
Still running. I'll wait for the monitor notification.
```

### [96] TOOL CALL — Bash · 2026-08-21 19:23:03 UTC

```
:
```

### [97] TOOL RESULT — Bash · 2026-08-21 19:23:03 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [98] ASSISTANT · 2026-08-21 19:23:07 UTC

```
Waiting for the background dependency install to finish before executing the notebook; I'll proceed once the monitor notifies me.
```

### [99] TOOL CALL — Bash · 2026-08-21 19:23:07 UTC

```
sleep 30 && echo done
```

### [100] TOOL RESULT — Bash [ERROR] · 2026-08-21 19:23:07 UTC

```
Error: Blocked: sleep 30 followed by: echo done. To wait for a condition, use Monitor with an until-loop (e.g. `until <check>; do sleep 2; done`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block.
```

### [101] ASSISTANT · 2026-08-21 19:23:09 UTC

```
I'll pause here until the Monitor task notifies me that jupyter/ipykernel finished installing.
```

### [102] SYSTEM-USER prompt · 2026-08-21 19:23:11 UTC

```
<validation-feedback>
Attempt 1 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [103] TOOL CALL — Bash · 2026-08-21 19:23:15 UTC

```
cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu
.nb_env/bin/python -c "import jupyter, ipykernel; print('OK')" 2>&1
```

### [104] TOOL RESULT — Bash [ERROR] · 2026-08-21 19:23:15 UTC

```
Error: Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'jupyter'
```

### [105] TOOL CALL — Bash · 2026-08-21 19:23:19 UTC

```
ps aux | grep -i "pip install" | grep -v grep; echo "---"; ls /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/.nb_env/bin/ 2>&1 | head -20
```

### [106] TOOL RESULT — Bash · 2026-08-21 19:23:19 UTC

```
{"stdout": "root         197  0.0  0.0   4492  1544 ?        Ss   19:19   0:00 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1787339825594-96ohf3.sh 2>/dev/null || true && shopt -u extglob 2>/dev/null || true && { \\builtin unalias -- 'unsetenv'; \\builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu /usr/local/bin/python3.12 -m venv .nb_env 2>&1 | tail -5 .nb_env/bin/pip install -q pip jupyter ipykernel 2>&1 | tail -10' < /dev/null && pwd -P >| /tmp/claude-f99d-cwd\nroot         206  6.6  0.0  99256 92200 ?        S    19:20   0:11 /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/.nb_env/bin/python3.12 .nb_env/bin/pip install -q pip jupyter ipykernel\n---\nActivate.ps1\nactivate\nactivate.csh\nactivate.fish\npip\npip3\npip3.12\npygmentize\npython\npython3\npython3.12\nsend2trash\nwsdump", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [107] ASSISTANT · 2026-08-21 19:23:21 UTC

```
Still installing (slow environment). Let me wait via Monitor properly this time.
```

### [108] TOOL CALL — Monitor · 2026-08-21 19:23:21 UTC

```
{'description': 'wait for jupyter/ipykernel pip install to finish in .nb_env', 'command': 'cd /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu\nuntil .nb_env/bin/python -c "import jupyter, ipykernel" 2>/dev/null; do sleep 5; done\necho "READY"', 'timeout_ms': 600000}
```

### [109] TOOL RESULT — Monitor · 2026-08-21 19:23:21 UTC

```
{"taskId": "bya68c40b", "timeoutMs": 600000, "persistent": false}
```

### [110] TOOL CALL — Write · 2026-08-21 19:23:25 UTC

```
File: /ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/.terminal_claude_agent_struct_out.json

{
  "out_expected_files": {
    "notebook": "code_demo.ipynb",
    "mini_data_file": "mini_demo_data.json"
  }
}
```

### [111] TOOL RESULT — Write · 2026-08-21 19:23:25 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_fvTNuFE3-z80/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_24Q1bYB_ULpu/.terminal_claude_agent_struct_out.json", "content": "{\n  \"out_expected_files\": {\n    \"notebook\": \"code_demo.ipynb\",\n    \"mini_data_file\": \"mini_demo_data.json\"\n  }\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [112] ASSISTANT · 2026-08-21 19:23:27 UTC

```
Output file written. Now I'll wait for the install to finish and test-run the notebook.
```

### [113] TOOL CALL — Bash · 2026-08-21 19:23:27 UTC

```
:
```

### [114] TOOL RESULT — Bash · 2026-08-21 19:23:27 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [115] ASSISTANT · 2026-08-21 19:23:28 UTC

```
I'll pause here and wait for the Monitor notification before running the test.
```
