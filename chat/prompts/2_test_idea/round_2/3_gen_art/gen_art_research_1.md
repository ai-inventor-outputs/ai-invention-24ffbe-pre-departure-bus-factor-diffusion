# gen_art_research_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `run_5SMkWpWKNLxk` — Measuring Authority Diffusion Before Founders Leave Open Source Projects
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_research_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-08-20 20:10:57 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An artifact executor (Step 3.3: GEN_ART in the invention loop)

Executing a plan to produce a concrete artifact.
GEN_PAPER_TEXT will use your artifact in the next paper draft.

Rigorous artifact with clear results → strong paper. Sloppy artifact → misdirected research.
</your_role>
</ai_inventor_context>

<task>
Conduct thorough, unbiased research on the given topic.
Adapt your investigation approach based on the research question and domain.
</task>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape. Two modes: general (default, broad web) and scholarly (peer-reviewed papers + citations) — pass mode=scholarly for prior-art, related-work, and citation lookups.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<critical_requirements>
1. SOURCE DIVERSITY - Consult MANY sources (10+), not just the first few results
2. AVOID SELECTION BIAS - Actively seek contradicting viewpoints, not just confirming ones
3. TRIANGULATE - Cross-reference claims across multiple independent sources
4. ACKNOWLEDGE UNCERTAINTY - Be honest about confidence levels and limitations
5. SYNTHESIZE - Produce a coherent answer that accounts for conflicting evidence
</critical_requirements>

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

Read and STRICTLY follow these skills: aii-web-tools.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_research_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_research_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_research_1/file.py`, `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/3_invention_loop/iter_2/gen_art/gen_art_research_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_5SMkWpWKNLxk/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for prior work and the field's landscape to ground your research.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<artifact_plan>
id: gen_plan_research_1_idx1
type: research
title: OSS Community-Health Framing + Bias-Free Corpus Sources
summary: >-
  Web research to (1) ground the pre-departure authority-diffusion construct in OSS-native community-health/onboarding literature
  (CHAOSS, Apache Incubator graduation, newcomer/core-team formation studies) alongside the existing firm-succession analogy,
  and (2) identify and concretely characterize data sources (GH Archive, World of Code, GHTorrent/Libraries.io legacy dumps)
  that can supply a historical, present-day-liveness-non-conditioned GitHub repository snapshot without requiring an authenticated
  GitHub REST token, recommending the single most viable concrete pull-path for the dataset artifact.
runpod_compute_profile: cpu_light
question: >-
  What OSS-native community-health/onboarding frameworks already measure something like 'pre-departure authority diffusion'
  (so the construct can be positioned against them, not just the firm-succession analogy), and what concrete, token-free,
  historically-snapshotted data source can supply commit/file-level authorship data for a GitHub repository corpus that does
  not condition on present-day project liveness?
research_plan: |-
  PART A — OSS-native community-health/onboarding grounding (produces 1-2 positioning sentences)

  1. CHAOSS metrics (already partially scoped by prior searches this session — verify and deepen):
     - Fetch https://www.chaoss.community/kb/metric-elephant-factor/ and https://www.chaoss.community/kb/metric-contributor-absence-factor/ (formerly 'Bus Factor') — get their EXACT definitions, formulas, and whether either is computed longitudinally (trend over time) or only as a single snapshot. This is the key comparison point: Avelino et al.'s TF and this hypothesis's diffusion trajectory are both snapshot-vs-trend variants of the same idea CHAOSS already names.
     - Fetch https://github.com/chaoss/wg-risk/blob/main/focus-areas/business-risk/contributor-absence-factor.md for the CHAOSS working-group's own methodology writeup (more detail than the KB page).
     - Search specifically for 'CHAOSS contributor absorption rate' and 'CHAOSS onboarding metrics' definitions (the KB page https://chaoss.community/kb/metrics-model-starter-project-health/ found this session is the right starting point — fetch it and grep for 'absorption', 'onboarding', 'time to first response', 'time to first commit').
     - Deliverable: 2-4 sentences precisely stating what CHAOSS's Elephant Factor / Contributor Absence Factor measure, confirming (or refuting) that they are snapshot metrics like Avelino et al.'s TF, and explicitly noting they do NOT track a pre-departure temporal trend — this is the gap this hypothesis's construct fills relative to CHAOSS, in exactly the same way it fills the gap relative to Avelino et al.

  2. Apache Incubator podling graduation criteria:
     - Fetch https://incubator.apache.org/guides/graduation.html (the canonical 'Guide to Successful Graduation') and grep/search it for language about 'diverse', 'authority', 'meritocratic', 'committers', 'PMC' — the graduation checklist explicitly assesses whether commit/PMC authority has spread beyond the founding contributor(s) before a podling is allowed to graduate to a top-level project.
     - Also check https://incubator.apache.org/policy/incubation.html or the IPMC maturity model (Apache Project Maturity Model, https://community.apache.org/apache-way/apache-project-maturity-model.html) if graduation.html does not itself contain a hard diversity checklist — the Maturity Model has an explicit 'CD (Community Diversity)' criteria block (CD10, CD20, CD30) that is the closest real-world analogue to this hypothesis's diffusion metric and should be quoted if found.
     - Deliverable: identify whether ASF operationalizes 'authority has diffused' as a graduation gate (binary human judgment) versus this hypothesis's proposal of a continuous, DOA-computed, retrospective metric — note this is a validation-committee heuristic, not a predictive statistical measurement, which is exactly the distinction worth stating in the positioning paragraph.

  3. OSS newcomer onboarding / core-team formation literature (to round out non-CHAOSS, non-ASF grounding):
     - Scholarly search (mode=scholarly) for: 'core team formation open source' Fagerholm OR Jergensen OR onboarding barriers Steinmacher; and 'from periphery to core' OSS contributor trajectory.
     - Specifically try to confirm/locate: Jergensen, Sarma & Wagstrom 'The Onion Patch' (core-periphery structure in OSS teams) and Steinmacher et al.'s onboarding-barriers work (multiple papers, e.g. 'A Systematic Literature Review on the Barriers Faced by Newcomers'); fetch abstracts, do not need full text.
     - Deliverable: 1-2 sentences noting that onboarding/core-formation literature studies how NEW contributors become core (join trajectory), which is the mirror image of this hypothesis's DEPARTURE trajectory (existing founder authority dispersing outward) — a clean complementary framing to include in the paper's related-work section.

  PART B — Historical, liveness-non-conditioned GitHub corpus sources (produces a concrete recommended pull-path)

  4. GH Archive (gharchive.org):
     - Fetch https://www.gharchive.org/ and https://github.com/igrigorik/gharchive.org/blob/master/bigquery/README.md.
     - Report EXACTLY: (a) what event types are recorded (PushEvent has commit SHAs + author but NOT full diffs/file lists — confirm this precisely, since DOA needs per-file change history, which raw GH Archive events do NOT contain, only pointers/metadata); (b) the two access paths — hourly gzipped JSON files at http://data.gharchive.org/YYYY-MM-DD-H.json.gz (no auth needed, direct HTTP download) vs the public BigQuery dataset `githubarchive` (needs only a free Google Cloud project + BigQuery sandbox, NOT a GitHub token) — confirm the BigQuery sandbox free tier's query-volume limits (typically 1TB/month scan); (c) whether repo creation/star/fork events in a given historical month can be used to build a 'top-N repos that existed as of year Y' sampling frame WITHOUT reference to whether they are still active today (yes — this is exactly what Avelino et al.'s method needs: a repo list frozen at a point in time). Flag clearly that GH Archive alone cannot supply per-file DOA data; it can only supply the REPO SELECTION frame (which repos existed/were popular circa year Y), and per-file commit history must then be pulled via `git clone` of each selected repo's normal git history (which is not conditioned on present liveness — you can clone and analyze a repo's history regardless of whether the repo is later archived/deleted, as long as it is still on GitHub or in a mirror).

  5. World of Code (WoC):
     - Fetch the arXiv abstract page https://arxiv.org/pdf/2607.06183 (author-identity map) and the original https://link.springer.com/article/10.1007/s10664-020-09905-9 EMSE paper abstract; also web-search 'World of Code access request how to use da API' to find the current access mechanism (WoC has historically required either direct SSH access to the maintainers' server at UTEP, requested via a form, OR downloadable Hugging Face bundles for specific derived datasets like the author-identity map).
     - Report EXACTLY: whether WoC provides full per-commit, per-file author/timestamp data (it does — this is its core product: cross-referenced commit/blob/author/project maps) and whether any of it is downloadable WITHOUT an application/access-request process (the Hugging Face-hosted derived bundles, e.g. the author-identity map from the 2607.06183 paper, ARE self-contained no-account-needed downloads — check if a similarly self-contained bundle exists that includes per-project commit-author-file triples, not just the identity map, which alone is insufficient for DOA). If the full commit graph requires the request/SSH process, state this plainly as a BLOCKER for a 3-hour, token-budget-constrained execution window, and recommend against WoC as the primary path for this specific study.

  6. GHTorrent / Libraries.io legacy dumps:
     - Fetch https://github.com/ghtorrent/ghtorrent.org/blob/master/faq.md and search 'GHTorrent MySQL dump download 2021' / 'GHTorrent Google BigQuery dataset public' to determine: (a) whether the historical MongoDB/MySQL dumps are still hosted and downloadable (GHTorrent's own infrastructure was largely decommissioned after ~2021 — verify current status, do not assume); (b) whether a mirror exists on Google BigQuery's public dataset marketplace (`ghtorrent-bq` or similar) that is still queryable; (c) Libraries.io's own open data dumps (libraries.io publishes periodic full CSV/JSON exports of package/repo metadata under Zenodo DOIs — these ARE static, no-token, permissively licensed, and searchable by Zenodo) — check the most recent Libraries.io Zenodo release for whether it includes per-repo star/fork/language/creation-date fields sufficient for building a stratified top-N-per-language sampling frame circa a fixed year, keeping in mind it will NOT contain commit-level data (same limitation as GH Archive: repo-selection metadata only, not DOA inputs).
     - Deliverable: state plainly whether GHTorrent is USABLE TODAY or effectively dead infrastructure (report what is found, do not guess).

  7. Synthesize a single recommended concrete pull-path for the dataset artifact, in this priority order given the 3-hour/low-budget constraints of this project: (a) use GH Archive's hourly JSON dumps (direct HTTP, no token, e.g. `http://data.gharchive.org/2016-01-{01..07}-*.json.gz` covering a full week to catch CreateEvent/WatchEvent/ForkEvent activity) OR the free BigQuery sandbox querying the public `githubarchive.year.YYYY` tables, to build a repo-selection frame frozen at a chosen historical year (recommend mirroring Avelino et al.'s own approach: top-N repos per language ranked by stars/forks AS OF that year, not today) — this sidesteps the GitHub REST API token/rate-limit problem entirely for repo SELECTION; (b) for each selected repo, its full commit/file history for the DOA computation can be obtained via plain `git clone` (unauthenticated, unlimited, no token needed for public repos) rather than the GitHub REST API — commit history is retrievable regardless of the repo's current activity status, which is the actual bottleneck Avelino et al. hit (their 83x query-budget claim is about REST metadata calls, not git clone, and git clone is not rate-limited by a token at all for public repos); (c) note precisely which repos this excludes: any repo that was later made private or fully deleted (not just archived/renamed) between the historical snapshot year and today — GH Archive event data proves the repo existed and was active in year Y, but the study will still lose the subset that was later deleted outright, and this residual (much smaller) survivorship consideration should be reported honestly as a remaining limitation, distinct from and much weaker than the present-liveness-conditioning problem this whole direction exists to fix.

  Execution notes: run all Part A and Part B searches/fetches in parallel batches (independent topics). Use fetch_grep on the Apache Maturity Model page and CHAOSS KB pages to pull exact defined-metric text rather than paraphrasing from a general fetch summary. Cap total tool calls at roughly 25-30 search+fetch+grep calls; this is a zero-cost web-research task (no OpenRouter LLM calls needed beyond the report-writing step itself, which should use minimal tokens). Write findings into research_out.json (answer/sources/follow_up_questions) plus a readable research_report.md with two clearly separated sections mirroring Part A and Part B above, each ending in an explicit, actionable recommendation sentence the dataset-artifact executor can act on directly.
explanation: >-
  This research directly de-risks two concrete gaps flagged in the reviewer-driven revision of this hypothesis. First, the
  paper currently justifies its diffusion construct only via a cross-domain analogy (firm succession); grounding it against
  CHAOSS's Elephant/Contributor-Absence Factor, Apache Incubator's community-diversity graduation checks, and OSS core-team-formation
  literature gives it an OSS-native theoretical home and answers the likely reviewer question 'isn't this just bus factor
  over time' with a precise, sourced distinction. Second, and more consequentially, the current 15-repo corpus is invalidated
  by construction because it was sampled by starting from tools known today to still exist — this research finds and characterizes
  the concrete, no-token data sources (GH Archive event dumps for repo selection frozen at a historical year, plain git clone
  for commit/file history, with World of Code and GHTorrent/Libraries.io as characterized fallbacks) that a follow-up dataset
  artifact needs to build a corpus that does not condition on present-day liveness, which is the specific fix this hypothesis's
  own text says is required before the causal diffusion-predicts-survival claim can be tested at all.
</artifact_plan>

<investigation_process>
1. DIVERGE: Brainstorm multiple angles/framings of the question before searching. Think across fields — what adjacent domains might have relevant insights?
2. SEARCH: Multiple queries per angle with different phrasings to discover the landscape
3. FETCH: Read promising URLs at high level. Snippets are NOT enough — fetch full pages
4. DETAIL: aii-web-tools fetch_grep for specifics from key pages/PDFs
5. CONTRAST: Actively try to disprove your emerging conclusions. Search with different phrasings, "[topic] criticism", "[topic] limitations". Check across fields — the same finding may exist under different names
6. SYNTHESIZE: Integrate into balanced conclusion
7. ITERATE: Expect to repeat steps 2-6 if findings are incomplete or one-sided. Don't settle on first results
8. SUMMARIZE: Output JSON must include 'title' and 'summary' fields
</investigation_process>

<output_requirements>
- Write research_out.json to your workspace with all findings
- Provide your finding as clear prose WITH NUMBERED CITATIONS
- EVERY factual claim must have a citation number in brackets: [1], [2], [1, 3], etc.
- Include BOTH supporting AND contradicting evidence
- Be explicit about confidence level and what would change it
- End with follow-up questions for further investigation
</output_requirements>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

Research everything specified in the artifact plan, but you may also investigate additional relevant aspects beyond what's listed. Investigate this question thoroughly.

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ResearchExpectedFiles": {
      "description": "All expected output files from research artifact.",
      "properties": {
        "output": {
          "description": "Path to research output JSON. Example: 'research_out.json'",
          "title": "Output",
          "type": "string"
        }
      },
      "required": [
        "output"
      ],
      "title": "ResearchExpectedFiles",
      "type": "object"
    },
    "Source": {
      "description": "A source used in the research.",
      "properties": {
        "index": {
          "description": "Citation number (1, 2, 3, ...)",
          "title": "Index",
          "type": "integer"
        },
        "url": {
          "description": "Full URL of the source",
          "title": "Url",
          "type": "string"
        },
        "title": {
          "description": "Title of the article/page",
          "title": "Title",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this source contributed",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "index",
        "url",
        "title",
        "summary"
      ],
      "title": "Source",
      "type": "object"
    }
  },
  "description": "Research artifact \u2014 structured output + file metadata.\n\nConducts thorough web research using the aii-web-tools skill.\nReturns structured JSON output with citations.",
  "properties": {
    "title": {
      "default": "",
      "description": "Artifact title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); describe the content, not a status.",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "layman_summary": {
      "default": "",
      "description": "One-sentence plain-language summary of what this artifact does, accessible to non-experts. Used only in the per-artifact README, not in downstream prompts.",
      "maxLength": 250,
      "minLength": 80,
      "title": "Layman Summary",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Summary for downstream artifacts: what this artifact provides",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/ResearchExpectedFiles",
      "description": "All output files you created. Must include research_out.json with your research findings."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    },
    "answer": {
      "description": "Comprehensive answer with NUMBERED CITATIONS. Cite sources by number: 'Claim [1].' or 'According to [2, 3]...'",
      "title": "Answer",
      "type": "string"
    },
    "sources": {
      "description": "All sources used, with index matching citation numbers in answer",
      "items": {
        "$ref": "#/$defs/Source"
      },
      "title": "Sources",
      "type": "array"
    },
    "follow_up_questions": {
      "description": "2-3 follow-up questions that emerged from the investigation",
      "items": {
        "type": "string"
      },
      "title": "Follow Up Questions",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files",
    "answer",
    "sources",
    "follow_up_questions"
  ],
  "title": "ResearchArtifact",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-20 20:10:57 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-web-tools · 2026-08-20 20:10:59 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Web research toolkit: free-first web search (general or scholarly, Serper fallback), web page fetch as markdown (HTML and PDF), and regex grep over full page/PDF text. Use whenever a task needs to search the web, read a page, mine a paper/PDF, verify citations, or extract exact quotes, numbers, or methodology from a URL."
---

## Web tools

You have three web capabilities: **search**, **fetch**, and **grep** (exact
regex extraction over a full page or PDF).

**Pick where they come from, in this order:**

1. **If you have built-in `WebSearch` / `WebFetch` tools, PREFER those over the
   scripts below.** They may be **deferred tools** (listed by name but with
   schemas not yet loaded) — if so, call `ToolSearch("select:WebSearch,WebFetch")`
   ONCE to load them, then use them normally. Do not skip them just because they
   need that one extra load step; they are the preferred path. Pair them with the
   `aii_web_tools__fetch_grep` script below when you need exact text / numbers /
   methodology that a summary would miss, or when reading a PDF.
2. **Only if you have NO built-in `WebSearch` / `WebFetch`** (e.g. the OpenHands
   backend), use the scripts in this skill (below). They are our own
   implementations — free-first web search (keyless general/scholarly engines,
   Serper fallback), html2text + PyMuPDF for fetch, and regex grep over the full
   document text. They work without any built-in web tools.

Workflow either way: **search** (discover) → **fetch** (read for the gist) →
**grep** (pull exact details / read PDFs).

---

## Running the scripts

Run every script with the skill's pre-provisioned interpreter (it already has
`requests`, `html2text`, `pymupdf`, `python-dotenv`). Set `PY` once:

```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

### 1. Search the web (free-first: general or scholarly)

```bash
# general web (default): keyless engines (ddgs, marginalia); Serper only if they miss
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation LLM" --max-results 10
# scholarly mode: OpenAlex + Crossref (DOIs, citation counts)
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation" --mode scholarly
```

Returns ranked title / URL / snippet lines. `--mode general` (default) uses
keyless general engines; `--mode scholarly` uses academic APIs. Both fall back
to Serper (paid) only when the free engines miss. Use search first to scan the
landscape; snippets are for discovery only — fetch a page before judging it.

### 2. Fetch a page as markdown (HTML or PDF)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2303.11366" --max-chars 10000
```

`--max-chars` caps output (default 10000); `--char-offset N` pages further in.
Handles PDFs transparently via PyMuPDF.

### 3. Grep a page or PDF (exact regex extraction)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2303.11366" --pattern "verbal reinforcement" --max-matches 20 --context-chars 200
```

Returns only the matching sections with surrounding context — the right tool
for exact numbers, table values, methodology, or long PDFs where a summary
would lose the detail. `-i` for case-insensitive.

**Parallelize** independent searches/fetches in one turn; only sequence a
fetch after the search that produced its URL.

---

## Notes

- The scripts call our ability server. If a script prints
  `Ability service not available`, the server is down — say so rather than
  silently improvising a different search method.
- Do **not** hand-roll your own `requests`/scraping for search when these
  tools are available: Serper returns clean Google results and the fetch/grep
  scripts already handle HTML, PDFs, and encoding.
````

### [4] SYSTEM-USER prompt · 2026-08-20 20:14:53 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `layman_summary`: "Researches how existing open-source health metrics (like CHAOSS bus-factor and Apache's graduation rules) relate to a new 'founder authority spreading out' idea, and finds a way to build a study dataset that doesn't unfairly favor only projects that are still alive today." is too long (at most 250 characters, got 272)
Every required field must be present and every field type must match the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [5] SYSTEM-USER prompt · 2026-08-20 20:15:03 UTC

```
<verification_failed>
Your research output failed verification (attempt 1/10).
</verification_failed>

<schema_errors>
JSON SCHEMA ERRORS:
  - research_out.json: Missing required 'title' field
  - research_out.json: Missing required 'summary' field

Fix: research_out.json must have:
     {
       "answer": "comprehensive answer with [1], [2] citations",
       "sources": [{"index": 1, "url": "...", "title": "...", "summary": "..."}],
       "follow_up_questions": ["Question 1?", "Question 2?"],
       "summary": "what was found"
     }

     Each citation [N] in answer MUST match a source with that index.
</schema_errors>

<content_warnings>
CONTENT ISSUES:
  - research_out.json: 'title' is too short

Fix: Ensure answer is comprehensive, has proper citations, and all sources are cited.
</content_warnings>

<task>
FIX ISSUES:
1. Output valid research_out.json with all required fields
2. Ensure every factual claim has a numbered citation [1], [2], etc.
3. Ensure every source has a matching citation in the answer
</task>
```
