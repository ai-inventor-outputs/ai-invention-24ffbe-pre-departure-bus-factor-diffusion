# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `iter2_13ec49ac7efb` — Authority Diffusion Before Founder Departure: Diagnosing Sample Starvation in OSS Survival Research
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_full_paper` (terminal_claude_agent, claude-sonnet-5)

### [1] CONFIG · 2026-08-21 16:11:39 UTC

```
model: claude-sonnet-5 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_4_assemble_paper/paper/workspace
```

### [2] SYSTEM-USER prompt · 2026-08-21 16:21:56 UTC

```
continue where you left off — reuse any partial work already written to disk. Do NOT start over.
```

### [3] TOOL CALL — Bash · 2026-08-21 16:22:00 UTC

```
ls -la && find . -maxdepth 2 -newer . 2>/dev/null | head -50
```

### [4] TOOL RESULT — Bash · 2026-08-21 16:22:00 UTC

```
{"stdout": "total 5871\ndrwxr-xr-x 3 root root 2000122 Aug 21 16:11 .\ndrwxr-xr-x 3 root root 2000122 Aug 21 16:11 ..\n-rw-r--r-- 1 root root   11056 Aug 21 16:21 .repl_agent.ptylog\ndrwxr-xr-x 2 root root 2000121 Aug 21 16:11 figures\n./.repl_agent.ptylog", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [5] TOOL CALL — Bash · 2026-08-21 16:22:02 UTC

```
ls figures | head -50; echo ---; wc -l .repl_agent.ptylog; echo ---; tail -c 4000 .repl_agent.ptylog
```

### [6] TOOL RESULT — Bash · 2026-08-21 16:22:04 UTC

```
{"stdout": "fig1_v0.jpg\nfig2_v0.pdf\nfig3_v0.pdf\nfig4_v0.pdf\n---\n0 .repl_agent.ptylog\n---\n40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[34B\u001b[38;5;174m*\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[26B\u001b[38;5;246m●\u001b[3G\u001b[39mRunning\u001b[11G\u001b[1m1\u001b[13G\u001b[22mshell\u001b[19Gcommand…\r\u001b[12C\u001b[8B\u001b[38;5;246m(2s · \u001b[38;5;249mthinking with low effort\u001b[38;5;246m)\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[18C\u001b[34B\u001b[38;5;246m↓\u001b[39m \u001b[38;5;246m25 tokens · \u001b[38;5;249mthinking with low effort\u001b[38;5;246m)\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[34B\u001b[38;5;174m✢\u001b[21G\u001b[38;5;246m50\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[34B\u001b[38;5;174m·\u001b[11G\u001b[38;5;216m…\u001b[22G\u001b[38;5;246m8\u001b[33G\u001b[38;5;248mthinking with low effort\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[26B\u001b[38;5;246m \u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[20C\u001b[34B\u001b[38;5;246m65\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[9C\u001b[34B\u001b[38;5;216mg\u001b[22G\u001b[38;5;246m6\u001b[33G\u001b[38;5;247mthinking with low effort\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[20C\u001b[34B\u001b[38;5;246m78\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[34B\u001b[38;5;174m✢\u001b[9G\u001b[38;5;216mn\u001b[21G\u001b[38;5;246m81\u001b[33Gthinking with low effort\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b]0;◑ Claude Code\u0007\u001b[?25l\u001b[H\r\u001b[34B\u001b[38;5;174m*\u001b[8G\u001b[38;5;216mi\u001b[11G\u001b[38;5;174m…\u001b[22G\u001b[38;5;246m3\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[26B\u001b[38;5;246m●\r\u001b[8B\u001b[38;5;174m✶\u001b[14G\u001b[38;5;246m3\u001b[22G4\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[6C\u001b[34B\u001b[38;5;216mé\u001b[10G\u001b[38;5;174mg\u001b[22G\u001b[38;5;246m6\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[34B\u001b[38;5;174m✻\u001b[21G\u001b[38;5;246m100 tokens · thinking with low e\u001b[54Gfort)\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[34B\u001b[38;5;174m✽\u001b[6G\u001b[38;5;216mt\u001b[9G\u001b[38;5;174mn\u001b[23G\u001b[38;5;246m6\u001b[34G\u001b[38;5;247mthinking with low effort\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[2C\u001b[26BList\u001b[13Gdirectory…\u001b[K\r\u001b[1B\u001b[38;5;246m  ⎿  $ ls -la && find . -maxdepth 2 -newer . 2>/dev/null | head -50\r\u001b[2C\u001b[7B\u001b[38;5;216mSau\u001b[9Gng…\u001b[31G\u001b[38;5;246m)\u001b[39m\u001b[K\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[2C\u001b[26BRunn\u001b[11Gls -la && find\u001b[26G.\u001b[28G-maxdepth\u001b[38G2\u001b[40G-newer\u001b[47G.\u001b[49G2>/dev/null…\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[2C\u001b[34B\u001b[38;5;180mSautéing…\u001b[22G\u001b[38;5;246m11\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[26B\u001b[38;5;246m \u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[22C\u001b[34B\u001b[38;5;246m3\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b]0;◐ Claude Code\u0007\u001b[?25l\u001b[H\r\u001b[34B\u001b[38;5;174m✻\u001b[3GSautéing…\u001b[22G\u001b[38;5;246m25\u001b[31G · \u001b[38;5;249mthinking with low effort\u001b[38;5;246m)\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[34B\u001b[38;5;174m✶\u001b[22G\u001b[38;5;246m33\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[34B\u001b[38;5;174m*\u001b[14G\u001b[38;5;246m4\u001b[23G9\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[33C\u001b[34B\u001b[38;5;246mthought for 1s)\u001b[39m\u001b[K\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[34B\u001b[38;5;174m✢\u001b[22G\u001b[38;5;246m41\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[26B\u001b[38;5;246m●\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[22C\u001b[34B\u001b[38;5;246m3\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[34B\u001b[38;5;174m·\u001b[3G\u001b[38;5;180mSautéing…\u001b[23G\u001b[38;5;246m4\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[22C\u001b[34B\u001b[38;5;246m6\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[22C\u001b[34B\u001b[38;5;246m8\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[2C\u001b[34B\u001b[38;5;174mSautéing…\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[22C\u001b[34B\u001b[38;5;246m9\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b]0;◑ Claude Code\u0007\u001b[?25l\u001b[H\r\u001b[34B\u001b[38;5;174m✢\u001b[22G\u001b[38;5;246m51\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[26B\u001b[38;5;246m \u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[34B\u001b[38;5;174m*\u001b[23G\u001b[38;5;246m2\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[34B\u001b[38;5;174m✶\u001b[14G\u001b[38;5;246m5\u001b[23G4\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[34B\u001b[38;5;174m✻\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[35C\u001b[34B\u001b[38;5;246minking with low effort)\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[21C\u001b[34B\u001b[38;5;246m79\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[34B\u001b[38;5;174m✽\u001b[22G\u001b[38;5;246m9\u001b[34G\u001b[38;5;247mthinking with low effort\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[135C\u001b[35B\u001b[38;5;220mYou've used 80% of your weekly limit · resets Aug 24, 7am (UTC)\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[26B\u001b[38;5;246m●\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[20C\u001b[34B\u001b[38;5;246m215\u001b[34G\u001b[38;5;248mthinking with low effort\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[21C\u001b[34B\u001b[38;5;246m22\u001b[39m\u001b[40;1H\u001b[38;3H\u001b[?25h\u001b[?25l\u001b[H\r\u001b[2C\u001b[34B\u001b[38;5;180mSautéing…\u001b[14G\u001b[38;5;246m6\u001b[31G)\u001b[39m\u001b[K\u001b[40;1H\u001b[38;3H\u001b[?25h", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [7] TOOL CALL — Bash · 2026-08-21 16:22:08 UTC

```
cd /ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_4_assemble_paper && ls -la; echo ---; find . -maxdepth 3 | head -100
```

### [8] TOOL RESULT — Bash · 2026-08-21 16:22:08 UTC

```
{"stdout": "total 5901\ndrwxr-xr-x 3 root root 2000123 Aug 21 16:11 .\ndrwxr-xr-x 7 root root 2041692 Aug 21 16:11 ..\ndrwxr-xr-x 3 root root 2000123 Aug 21 16:11 paper\n---\n.\n./paper\n./paper/workspace\n./paper/workspace/.repl_agent.ptylog\n./paper/workspace/figures", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_4_assemble_paper/paper/workspace", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [9] TOOL CALL — Bash · 2026-08-21 16:22:10 UTC

```
cd /ai-inventor/aii_data/runs/run_LYICROwXFVjo && find . -maxdepth 4 -iname "*paper_text*" -o -iname "*.tex" -o -iname "*bib*" 2>/dev/null | grep -v workspace/figures | head -80
```

### [10] TOOL RESULT — Bash · 2026-08-21 16:22:10 UTC

```
{"stdout": "./3_invention_loop/iter_2/gen_paper_text\n./3_invention_loop/iter_2/gen_paper_text/gen_paper_text", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_4_assemble_paper/paper/workspace", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [11] TOOL CALL — Bash · 2026-08-21 16:22:12 UTC

```
cd /ai-inventor/aii_data/runs/run_LYICROwXFVjo/3_invention_loop/iter_2/gen_paper_text/gen_paper_text && ls -la
```

### [12] TOOL RESULT — Bash · 2026-08-21 16:22:12 UTC

```
{"stdout": "total 2737\ndrwxr-xr-x 2 root root 1065408 Aug 20 21:19 .\ndrwxr-xr-x 3 root root 1065408 Aug 20 21:01 ..\n-rw-r--r-- 1 root root  572135 Aug 20 21:19 .repl_agent.ptylog\n-rw-r--r-- 1 root root   32281 Aug 20 21:19 .terminal_claude_agent_struct_out.json\n-rw-r--r-- 1 root root    8447 Aug 20 21:18 build_paper_json.py\n-rw-r--r-- 1 root root   32281 Aug 20 21:18 paper_text.json\n-rw-r--r-- 1 root root   24643 Aug 20 21:18 paper_text.md", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_4_assemble_paper/paper/workspace", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [13] ASSISTANT · 2026-08-21 16:22:14 UTC

```
Good, found the paper text. Let me load the assembly skill and check the figures/paper text content.
```

### [14] TOOL CALL — Skill · 2026-08-21 16:22:14 UTC

```
aii-paper-to-latex
```

### [15] TOOL RESULT — Skill · 2026-08-21 16:22:14 UTC

```
{"success": true, "commandName": "aii-paper-to-latex"}
```

### [16] TOOL CALL — Bash · 2026-08-21 16:22:18 UTC

```
cd /ai-inventor/aii_data/runs/run_LYICROwXFVjo/3_invention_loop/iter_2/gen_paper_text/gen_paper_text
python3 -c "
import json
d=json.load(open('paper_text.json'))
print(type(d), list(d.keys()) if isinstance(d,dict) else len(d))
"
```

### [17] TOOL RESULT — Bash · 2026-08-21 16:22:18 UTC

```
{"stdout": "<class 'dict'> ['title', 'abstract', 'paper_text', 'figures', 'summary']", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_4_assemble_paper/paper/workspace", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [18] TOOL CALL — Read · 2026-08-21 16:22:20 UTC

```
/ai-inventor/aii_data/runs/run_LYICROwXFVjo/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/paper_text.md
```

### [19] TOOL RESULT — Read · 2026-08-21 16:22:20 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_LYICROwXFVjo/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/paper_text.md", "content": "# Title\nAuthority Diffusion Before Founder Departure: Diagnosing Sample Starvation in OSS Survival Research and a Liveness-Unbiased Corpus to Fix It\n\n# Abstract\n\nWhether an open-source project survives its founder's departure is widely assumed to depend on how much ownership had already diffused to other contributors before that departure, yet this pre-departure trend is absent from existing community-health metrics, which all score diversity at a single snapshot rather than as a trajectory leading up to a departure. We built a pipeline that reimplements a published Degree-of-Authorship / Truck-Factor methodology to detect founder-only ownership-departure events and to compute a pre-departure authority-diffusion score from commit history, then applied it to a large GitHub corpus sampled by current popularity. The pipeline located too few genuine departure events for any of the three planned statistical tests to run, each instead reporting insufficient sample size. We show this null is a sampling artifact rather than evidence about the hypothesis: a rigor-gap re-analysis finds this corpus's departure-event incidence and its founder-only survival rate are both statistically far from a published external population baseline, in the direction expected if the sampling frame systematically favors repositories that already survived, and that a companion robustness check could not have detected an effect at any of the budgets it was run at, due to an undocumented cap in its implementation. As a remedy, we release a second corpus built with no filter on current liveness, sampled purely by historical creation and activity windows, in which the large majority of repositories are non-surviving by a two-year-inactivity proxy — giving the pre-departure authority-diffusion hypothesis a corpus in which non-surviving projects are actually represented for the first time.\n\n# 1. Introduction\n\n## 1.1 The problem\n\nAn open-source project's founder eventually stops committing. Some projects keep going; others go quiet within a year. The literature has metrics for measuring how concentrated a project's ownership is at a single point in time, but not for measuring how that concentration was *changing* in the months before the founder left — whether responsibility had already spread to other contributors, or whether the founder was still the sole owner of every file up to their last commit. We call this pre-departure trend *authority diffusion*, and we test whether it predicts survival beyond the snapshot statistics (team size, commit volume, file count) that existing metrics already capture.\n\n## 1.2 Why it matters\n\nCommunity-health tooling already tries to answer a version of this question after the fact: CHAOSS's Contributor Absence Factor counts how many top contributors are needed to reach 50% of a project's commits, and its Elephant Factor does the analogous count over organizations, but CHAOSS's own knowledge base documents both as computable only as a snapshot or as repeated snapshots, never as a fitted trajectory leading into a departure [1, 2]. The Apache Software Foundation operationalizes \"diversity\" for graduation as a binary committee judgment — at least three legally independent committers, no single essential company — rather than a continuous, predictive statistic [4]. A validated pre-departure trajectory signal would let maintainers, funders, and package-registry risk tooling flag an at-risk project *before* the founder's last commit, rather than after the project has already gone quiet long enough to trip a Contributor Absence Factor snapshot.\n\n## 1.3 Why it is hard\n\nTesting this hypothesis needs three things simultaneously: (a) a reliable, automatic detector for the event itself — a founder truly stepping away, not merely going quiet for a sprint — (b) commit-level history reaching back far enough before that event to fit a pre-departure trend, and (c) a sample of repositories that is not itself pre-filtered on the outcome being measured. We show in Section 4 that ordinary GitHub sampling strategies violate (c) by construction: search and trending endpoints surface repositories that are popular and active *today*, which already conditions the sample on having survived long enough to accumulate that popularity. A repository whose founder left and which then died six months later is, almost by definition, one that never accumulated the stars needed to be discovered by a present-day search query.\n\n## 1.4 Why existing approaches fall short\n\nAvelino et al.'s (ESEM 2019) [19] Truck-Factor / Degree-of-Authorship (DOA) pipeline is the closest prior instrument: it detects Truck-Factor-Detachment-Departure (TFDD) events from commit history and reports population-level TFDD incidence and post-TFDD survival rates from a large GitHub sample. It was not designed to fit a *pre-departure* trajectory, and — more importantly for the present study — it was built on exactly the kind of popularity-conditioned frame described above. We reused its DOA/TFDD machinery in full (Section 3) rather than re-deriving it, but applied it to our own sampling frame; the corpus we built for that first pass turned out to inherit the same liveness conditioning, which is the central negative finding of this paper.\n\n## 1.5 What we did and what we found\n\nWe built the Avelino-style DOA/TFDD pipeline (Section 3), ran it on a 3,427-repository GitHub corpus, and found that only 6 repositories produced a usable founder-only TFDD event (Section 4.1) — an error breakdown dominated by 3,409 repositories with no minable commit history at all. Every downstream statistical test we had planned (matched-pairs survival comparison, BH-corrected logistic/ordinal regression, window-shuffle placebo check) consequently reported `insufficient_n` rather than a substantive result. Rather than treat this null as evidence about the hypothesis, we ran a dedicated rigor-gap evaluation (Section 4.2) that shows the corpus itself is biased toward survival — its TFDD incidence and founder-only survival rate are both statistically distinguishable from Avelino et al.'s own published population figures — and that the placebo check's apparent robustness across simulation budgets is a structural artifact of an undocumented per-repository draw cap, not evidence that six events are enough. We then built a second corpus (Section 5) that removes the liveness conditioning by sampling on historical creation/push-date windows only, and report its composition as the resource this hypothesis needs to be tested properly. **This paper's contribution is therefore diagnostic and infrastructural, not a confirmed or refuted authority-diffusion effect**: we did not obtain enough founder-only TFDD events in either corpus to run the planned regression, and we report that limitation explicitly rather than a spurious point estimate from n=6.\n\n### Summary of Contributions\n\n- A working reimplementation of Avelino et al.'s DOA/Truck-Factor/TFDD pipeline extended with a pre-departure authority-diffusion covariate, applied at 3,427-repository scale (Section 3).\n- A rigor-gap evaluation that formally quantifies the survivorship bias in a popularity-sampled TFDD corpus against Avelino et al.'s own published population statistics, and that exposes an undocumented hard cap that makes the pipeline's placebo check vacuous rather than confirmatory (Section 4).\n- A positioning of the pre-departure authority-diffusion construct against the nearest existing OSS community-health metrics and onboarding literature, establishing that none of them measure a pre-departure trend (Section 2).\n- A second, 67-repository corpus sampled without any liveness or popularity filter, in which 72% of repositories are non-surviving by a two-year-inactivity proxy, released as the resource needed to run this hypothesis test with an adequately powered, unbiased sample (Section 5).\n\n[FIGURE:fig1]\n\n# 2. Related Work\n\n**Snapshot diversity metrics.** CHAOSS's Contributor Absence Factor (formerly Bus Factor) sorts contributors by contribution volume and counts how many are needed to reach 50% of total contributions; CHAOSS's own documentation states this can be measured as a single snapshot or repeated at intervals, but no CHAOSS metric fits or validates a continuous pre-departure *trend* [1]. The sibling Elephant Factor, the organizational analogue, is explicitly documented as snapshot-only and as misrepresenting project history if computed cumulatively [2]. Neither metric is designed to answer \"was authority already diffusing before this specific person left,\" which is the question this paper's construct targets.\n\n**Governance-gate diversity.** The Apache Incubator's graduation guide requires at least three legally independent committers and no single dominating company as a binary, committee-judged gate for exiting incubation [4]; the Apache Project Maturity Model's retrievable CD-series criteria turned out on inspection to cover code governance (distribution, reproducible builds, provenance) rather than community diversity, and a true diversity-specific code series was not located [5]. Both instruments answer a governance-compliance question at a point in time, not a predictive one.\n\n**Newcomer trajectories.** The onion model of OSS socialization describes contributors migrating *inward*, from peripheral participation (mailing lists, bug reports) toward the code-owning core, as skill and reputation accrue [6], and a systematic review of newcomer barriers organizes the obstacles to that inward migration into five categories, most centrally prior technical skill and community responsiveness [7]. Both study the mirror-image trajectory to the one this paper is interested in: contributors moving *toward* ownership, rather than a founder's ownership moving *away* from them before departure.\n\n**Population-scale TFDD baselines.** Avelino et al. (ESEM 2019) [19] is the direct methodological ancestor of the pipeline used here (Section 3): its DOA weighting and Truck-Factor-Detachment-Departure detection are reused verbatim, and its published population-level TFDD incidence (16.3%) and founder-only-TFDD survival rate (40.6%) are the external baseline this paper's rigor-gap evaluation tests our own corpora against (Section 4.2).\n\n**Data-source landscape.** GH Archive exposes GitHub's public event stream (15+ event types) with no token required, but its `PushEvent` payload carries only commit SHA/author/message pointers — never file lists or diffs [8, 9, 10] — so it can supply a repository-selection frame but not the commit-level content this study needs. World of Code holds full commit/blob/file/author cross-referencing at the right granularity [11, 12] but is gated behind an SSH-registration approval process [13], and its self-serve Zenodo derivative covers only bot commits [14]. GHTorrent, an earlier commit-mining service, is confirmed dead: its domain now redirects to an unrelated site and its BigQuery mirror has been stale since 2019 [15, 16, 17]. Libraries.io's Zenodo dump is live and gives repository-selection metadata at scale but carries no commit-level history [18]. We concluded that a repository-selection frame independent of present-day liveness (built from historical creation/push-date search, Section 5) combined with a direct, unauthenticated `git clone` of each selected repository's full history is the only path that is simultaneously live, token-cheap, and free of the liveness conditioning this paper's Section 4 diagnoses.\n\n# 3. Method: DOA/TFDD Pipeline and the Authority-Diffusion Covariate\n\nWe reimplement Avelino et al.'s Degree-of-Authorship (DOA) weighting over per-file commit history to identify, for each repository, the point at which a single \"founder\" author accounts for the plurality of authorship (a Truck-Factor-Detachment-Departure, TFDD, event: the date the founder's authorship share falls below the threshold that would make their departure survivable without loss of institutional knowledge). A TFDD event is classed *founder-only* when the departing author is the repository's original committer, distinguishing genuine founder succession from a later core contributor's departure.\n\nFor every founder-only TFDD event, we compute two families of covariates purely from commits dated **before** the event, to avoid any post-departure leakage:\n\n- **At-TFDD snapshot covariates** (Avelino et al.'s original feature set): number of active developers, total commits, and total files at the moment of TFDD.\n- **Pre-departure authority-diffusion covariates** (this paper's addition): the founder's commit-share in the 6-12 month window immediately before TFDD, and the count of distinct non-founder contributors who already held DOA-recognized file ownership in that same window (`n_diffuse_owners_pre`). A single scalar `diffusion_score` combines the two.\n\nThe outcome is 18-month post-TFDD survival, labeled from subsequent commit activity (`survived_binary`), with three planned analyses: (1) a nearest-neighbor matched-pairs comparison of high- versus low-diffusion repositories controlling for the snapshot covariates, (2) BH-corrected logistic regression (binary survival) and ordinal regression (a graded survival label) with diffusion score as the covariate of interest, and (3) a window-shuffle placebo check that repeatedly reassigns which pre-TFDD window is treated as \"pre-departure\" to establish whether the observed diffusion-survival association could arise by chance.\n\n# 4. Results\n\n## 4.1 Sample starvation at 3,427 repositories\n\nRunning the pipeline on a 3,427-repository corpus sampled by current GitHub popularity/activity produced only 6 founder-only TFDD events. The error breakdown for the remaining 3,421 repositories was: 3,409 had no minable commit history at all under the mining budget used, 4 had a TFDD event that was not founder-only, and 2 were right-censored (no 18-month post-TFDD window had yet elapsed). At n=6, every planned statistical test failed outright: the matched-pairs comparison found zero eligible pairs even under relaxed matching, and both the logistic and ordinal regressions reported `insufficient_n`.\n\n[FIGURE:fig2]\n\n## 4.2 The null is a sampling artifact, not evidence of no effect\n\nA dedicated rigor-gap evaluation re-examined the 6-event corpus against Avelino et al.'s own published population statistics using Wilson 95% confidence intervals and two-proportion z-tests. Two results indicate the corpus is not a fair sample of the population Avelino et al. characterized:\n\n- **TFDD incidence.** 73.3% of this corpus's repositories (11 of 15 candidates carried through to the full table) exhibit any TFDD event, versus 16.3% in Avelino et al.'s published population — a two-proportion z=5.89, p=3.8e-9.\n- **Founder-only-TFDD survival.** 100% (5 of 5) of this corpus's founder-only-TFDD repositories survived 18 months post-departure, versus 40.6% in Avelino et al.'s population (Wilson 95% CI [0.606, 0.710] for their 66% TF=1 baseline versus this corpus's 45.5% TF=1 fraction, CI [0.213, 0.720]) — z=2.67, p=0.0075.\n\nBoth deviations point the same direction: a corpus selected for present-day popularity over-represents repositories that already survived whatever ownership transition they went through, which is exactly the confound the pre-departure authority-diffusion hypothesis needs an unbiased corpus to rule out.\n\n[FIGURE:fig3]\n\nSeparately, the evaluation audited the placebo check's own implementation and found a previously undocumented **20-draw-per-repository hard cap** — the code path never reaches the \"500 iterations\" figure the original summary cited, because it caps each repository's contribution to the placebo distribution at 20 draws regardless of the requested budget. Re-running the placebo check at three budgets (10, 60, and 2,000 requested draws) produced an identical qualitative conclusion at all three, which is not evidence of robustness: at the 20-draw hard cap, the theoretical floor on the smallest detectable effect is 4.8%, and at the (never-reached) 500-draw figure the floor would be 0.2% — meaning the check is structurally incapable of resolving an effect at n=6 regardless of how large the requested budget is set. The evaluation additionally spot-checked 3 of the corpus's 15 repositories against their raw source records and found all three aliases consistent (no full-corpus audit was run; 80% of the corpus remains unchecked by this pass).\n\n## 4.3 What we did not test\n\nNo expanded or non-liveness-conditioned corpus existed among this round's dependencies to run head-to-head against the population baseline, so the claim that the null in Section 4.1 is a design flaw rather than a genuine power problem rests on the structural argument and evidence in Section 4.2, not on a second frame producing more TFDD events. Section 5 supplies that second frame as this paper's concrete, falsifiable next step: if the pre-departure authority-diffusion hypothesis holds, a non-liveness-conditioned corpus should yield both a TFDD incidence closer to Avelino et al.'s 16.3% population figure and a founder-only survival rate closer to their 40.6%, rather than reproducing this section's 73.3%/100% figures.\n\n# 5. A Liveness-Non-Conditioned Corpus\n\nTo remove the conditioning identified in Section 4.2, we built a second 67-repository corpus using GitHub's Search API `created:`/`pushed:` date qualifiers to sample purely on **historical** creation and push-date windows (2011-2015) across eight languages, applying **no filter on present-day archived, starred, or maintained status**. Of 450 candidates screened, 383 (85%) were rejected — mostly for too few commits or too short a history to fit a pre-departure trajectory — leaving 67 accepted repositories. Of those, 48 (72%) have had no commit in at least two years as of build time (our non-surviving proxy) and 7 are archived by GitHub itself, meaning non-surviving projects are represented in this corpus for the first time at a scale the original 3,427-repository frame never produced (Section 4.1: only 2 right-censored, 0 confirmed non-surviving, among 6 founder-only TFDD events).\n\n[FIGURE:fig4]\n\nEach repository's record standardizes to one example carrying only pre-departure-observable input features (computed strictly before the founder's last commit, to avoid the leakage the original pipeline already guards against in Section 3) and one of three survival labels: `survived`, `non_surviving`, or `unknown_insufficient_post_departure_window` for repositories without enough elapsed history to call a label at all. This corpus is released as the direct input to Section 3's pipeline for the next round of this study; running it end to end and reporting the resulting TFDD incidence and founder-only survival rate against Avelino et al.'s population baseline is the falsifiable prediction stated in Section 4.3.\n\n# 6. Discussion\n\n**The headline finding of this paper is methodological.** A popularity-sampled GitHub corpus produced too few founder-only TFDD events to test the pre-departure authority-diffusion hypothesis (n=6), and the rigor-gap evaluation in Section 4.2 shows this was not bad luck: the corpus's TFDD incidence and founder-only survival rate both differ from Avelino et al.'s population figures in the direction consistent with survivorship conditioning, and the placebo check that appeared to certify the pipeline's null result was, on inspection, structurally incapable of detecting an effect at any of the budgets it was run at. We consider this worth reporting on its own terms rather than smoothing over: an automated pipeline that runs to completion and reports a stable null across three simulation budgets looks, from the outside, like a well-powered negative result. Section 4.2 shows it is not, and the distinction matters for anyone building on TFDD-style pipelines with any GitHub sample drawn by present-day popularity, stars, or trending status.\n\n**Limitations.** The spot-check audit of the original corpus's alias resolution covered only 3 of 15 repositories (80% unchecked). The new liveness-non-conditioned corpus (Section 5) has not yet been run through the DOA/TFDD pipeline of Section 3, so we cannot yet report whether it in fact yields more founder-only TFDD events or a less skewed incidence/survival rate than the original frame — that comparison is the explicit next step, not a result claimed here. The non-surviving proxy (no commit in >=2 years) is a coarse label; a repository can be dormant and later revived, and the corpus's `unknown_insufficient_post_departure_window` label exists precisely to avoid forcing a survival call where the post-departure window is too short. Finally, both corpora are drawn from GitHub only; repositories hosted elsewhere or migrated away from GitHub after founder departure are systematically invisible to any GitHub-only sampling frame, including ours.\n\n# 7. Conclusion\n\nWe set out to test whether authority diffusing away from a project's founder before their departure predicts survival beyond existing snapshot diversity metrics, and found instead that the obvious way to build a GitHub corpus for this question — sampling by current popularity — silently conditions the sample on survival, starving the founder-only-TFDD event count down to 6 and rendering every planned statistical test uninformative. We quantified that conditioning against Avelino et al.'s own published population baseline (TFDD incidence 73.3% vs. 16.3%, z=5.89, p=3.8e-9; founder-only survival 100% vs. 40.6%, z=2.67, p=0.0075) and showed the pipeline's placebo check could not have detected an effect at n=6 regardless of its requested simulation budget, due to an undocumented 20-draw-per-repository cap. We release a 67-repository corpus sampled without any liveness conditioning, 72% of which are non-surviving by a two-year-inactivity proxy, as the concrete resource needed to run this hypothesis test properly.\n\nFuture work: (1) run the Section 3 pipeline against the Section 5 corpus and report whether its TFDD incidence and founder-only survival rate move toward Avelino et al.'s population figures, as predicted in Section 4.3; (2) complete the full-corpus alias audit begun in Section 4.2, extending the 3-of-15 spot-check to all repositories in both corpora; (3) locate or derive the Apache Project Maturity Model's community-diversity-specific criteria codes, left unresolved in Section 2, to add a second governance-gate baseline alongside Avelino et al.'s population statistics.\n\n# References\n\n[1] CHAOSS. \"Metric: Contributor Absence Factor.\" https://www.chaoss.community/kb/metric-contributor-absence-factor/\n[2] CHAOSS. \"Metric: Elephant Factor.\" https://www.chaoss.community/kb/metric-elephant-factor/\n[3] CHAOSS. \"Metric: Newcomer Experience.\" https://www.chaoss.community/kb/metric-newcomer-experience/\n[4] Apache Incubator. \"Guide to Successful Graduation.\" https://incubator.apache.org/guides/graduation.html\n[5] Apache Software Foundation. \"Apache Project Maturity Model.\" https://community.apache.org/apache-way/apache-project-maturity-model.html\n[6] Jergensen, C., Sarma, A., & Wagstrom, P. \"The Onion Patch: Migration in Open Source Ecosystems.\" OpenSym 2011. https://dl.acm.org/doi/10.1145/2025113.2025127\n[7] Steinmacher, I., et al. \"A systematic literature review on the barriers faced by newcomers to open source software projects.\" Information and Software Technology, 2015. https://www.sciencedirect.com/science/article/abs/pii/S0950584914002390\n[8] GH Archive. https://www.gharchive.org/\n[9] GitHub Docs. \"REST API endpoints for events.\" https://docs.github.com/en/rest/activity/events\n[10] GH Archive payload field documentation. https://www.gharchive.org/\n[11] World of Code. https://worldofcode.org/docs/\n[12] \"Scaling Author Identity Disambiguation to the World of Code: A Methodology.\" arXiv:2607.06920. https://arxiv.org/abs/2607.06920\n[13] woc-hack/tutorial. https://github.com/woc-hack/tutorial\n[14] \"A mapping between Bot Commit, Projects, Files, and Blobs.\" Zenodo. https://zenodo.org/records/3699665\n[15] ghtorrent/ghtorrent.org. https://github.com/ghtorrent/ghtorrent.org\n[16] GHTorrent downloads page (dead domain). https://ghtorrent.org/downloads.html\n[17] Hoffa, F. \"Analyzing GitHub with BigQuery and other tools.\" https://github.com/fhoffa/analyzing_github\n[18] Libraries.io Open Source Repository and Dependency Metadata. Zenodo. https://zenodo.org/records/3626071\n[19] Avelino, G., Constantinou, E., Valente, M. T., & Serebrenik, A. \"On the abandonment and survival of open source projects: An empirical investigation.\" ESEM 2019.\n", "numLines": 128, "startLine": 1, "totalLines": 128}}
```

### [20] ASSISTANT · 2026-08-21 16:22:24 UTC

```
Now let me check the figures JSON for captions, and any bib source.
```

### [21] TOOL CALL — Bash · 2026-08-21 16:22:24 UTC

```
cd /ai-inventor/aii_data/runs/run_LYICROwXFVjo/3_invention_loop/iter_2/gen_paper_text/gen_paper_text
python3 -c "
import json
d=json.load(open('paper_text.json'))
print(json.dumps(d['figures'], indent=2)[:3000])
"
find /ai-inventor/aii_data/runs/run_LYICROwXFVjo -iname "*.bib" 2>/dev/null
```

### [22] TOOL RESULT — Bash · 2026-08-21 16:22:38 UTC

```
{"stdout": "[\n  {\n    \"id\": \"fig1\",\n    \"title\": \"Pre-Departure Authority Diffusion\",\n    \"caption\": \"The founder-departure authority-diffusion construct: in the 6-12 month window before a founder-only Truck-Factor-Detachment-Departure (TFDD) event, authority over the codebase either stays concentrated with the founder (low diffusion, left) or spreads to other DOA-recognized file owners (high diffusion, right). At-TFDD snapshot covariates (developer count, commits, files) are measured at the moment of TFDD; the pre-departure covariates (founder commit-share, count of distinct non-founder owners) are measured strictly before it to avoid post-departure leakage.\",\n    \"figure_type\": \"concept\",\n    \"image_gen_detailed_description\": \"A wide (21:9) two-panel conceptual diagram on a white background, sans-serif labels, showing a repository's commit-ownership timeline leading up to a founder departure event. Left panel labeled 'Low Diffusion': a timeline axis from 'T-12mo' to 'TFDD event' (marked with a red flag icon), with the founder's authority represented as a large solid-blue file-ownership block that stays dominant (roughly 90% of a stacked bar) right up to the TFDD flag, with only tiny slivers of other colors (non-founder owners) at the edges. Right panel labeled 'High Diffusion': the same timeline and TFDD flag, but the blue founder block visibly shrinks from left to right while several distinct colored blocks (representing named non-founder DOA owners) grow to fill the space before the TFDD flag is reached. Below both panels, a shared legend: blue = founder authorship, other colors = distinct non-founder file owners. Small caption under left panel: 'founder commit-share stays high -> departure predicted risky'. Small caption under right panel: 'founder commit-share falls, owners diversify -> departure predicted safe'. Clean minimal architecture-diagram style, muted blue/teal/amber palette, no photographic elements.\",\n    \"aspect_ratio\": \"21:9\",\n    \"summary\": \"Illustrates the pre-departure authority-diffusion construct this paper tests, contrasting a founder who stays dominant until departure with one whose ownership diffuses beforehand.\"\n  },\n  {\n    \"id\": \"fig2\",\n    \"title\": \"Where 3,427 Candidate Repositories Went\",\n    \"caption\": \"Funnel of the 3,427-repository popularity-sampled corpus through the DOA/TFDD pipeline. The overwhelming majority (3,409) were dropped for having no minable commit history; only 6 repositories produced a usable founder-only TFDD event, too few for any of the three planned statistical tests.\",\n    \"figure_type\": \"data\",\n    \"image_gen_detailed_description\": \"A horizontal funnel/waterfall chart, 4:3 aspect ratio, white background, sans-serif labels, muted blue-to-red color progression. Stages top to bottom with bar lengths proportional to value: 'Total candidate repositories' = 3427 (full-width blue bar); then four exit categories drawn as a stacked horizontal bar breakdown directly beneath it, each labeled with its exact count", "stderr": "\nShell cwd was reset to /ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_4_assemble_paper/paper/workspace", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [23] ASSISTANT · 2026-08-21 16:22:40 UTC

```
No bib file exists — I need to build references.bib from the reference list. Let me check the semscholar-bib skill for citations, but given many are non-paper web resources, I'll hand-write BibTeX entries (misc/online types) matching numeric citation style.
```

### [24] TOOL CALL — Bash · 2026-08-21 16:22:40 UTC

```
ls /ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_4_assemble_paper/paper/workspace/figures -la
```

### [25] TOOL RESULT — Bash · 2026-08-21 16:22:40 UTC

```
{"stdout": "total 5156\ndrwxr-xr-x 2 root root 2000121 Aug 21 16:11 .\ndrwxr-xr-x 3 root root 2000130 Aug 21 16:11 ..\n-rw-r--r-- 1 root root 1224204 Aug 21 16:11 fig1_v0.jpg\n-rw-r--r-- 1 root root   14757 Aug 21 16:11 fig2_v0.pdf\n-rw-r--r-- 1 root root   14027 Aug 21 16:11 fig3_v0.pdf\n-rw-r--r-- 1 root root   24689 Aug 21 16:11 fig4_v0.pdf", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [26] ASSISTANT · 2026-08-21 16:22:59 UTC

```
Now let me write references.bib and paper.tex.
```

### [27] TOOL CALL — Write · 2026-08-21 16:22:59 UTC

```
File: /ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_4_assemble_paper/paper/workspace/references.bib

@misc{chaoss_absence_factor,
  title = {Metric: Contributor Absence Factor},
  author = {{CHAOSS}},
  howpublished = {\url{https://www.chaoss.community/kb/metric-contributor-absence-factor/}},
  note = {Accessed 2026-08-21}
}

@misc{chaoss_elephant_factor,
  title = {Metric: Elephant Factor},
  author = {{CHAOSS}},
  howpublished = {\url{https://www.chaoss.community/kb/metric-elephant-factor/}},
  note = {Accessed 2026-08-21}
}

@misc{chaoss_newcomer_experience,
  title = {Metric: Newcomer Experience},
  author = {{CHAOSS}},
  howpublished = {\url{https://www.chaoss.community/kb/metric-newcomer-experience/}},
  note = {Accessed 2026-08-21}
}

@misc{apache_incubator_graduation,
  title = {Guide to Successful Graduation},
  author = {{Apache Incubator}},
  howpublished = {\url{https://incubator.apache.org/guides/graduation.html}},
  note = {Accessed 2026-08-21}
}

@misc{apache_maturity_model,
  title = {Apache Project Maturity Model},
  author = {{Apache Software Foundation}},
  howpublished = {\url{https://community.apache.org/apache-way/apache-project-maturity-model.html}},
  note = {Accessed 2026-08-21}
}

@inproceedings{jergensen2011onion,
  title = {The Onion Patch: Migration in Open Source Ecosystems},
  author = {Jergensen, Christian and Sarma, Anita and Wagstrom, Patrick},
  booktitle = {Proceedings of the 7th International Symposium on Open Collaboration (OpenSym)},
  year = {2011},
  doi = {10.1145/2025113.2025127},
  howpublished = {\url{https://dl.acm.org/doi/10.1145/2025113.2025127}}
}

@article{steinmacher2015barriers,
  title = {A systematic literature review on the barriers faced by newcomers to open source software projects},
  author = {Steinmacher, Igor and Silva, Marco Aurelio Graciotto and Gerosa, Marco Aurelio and Redmiles, David F.},
  journal = {Information and Software Technology},
  year = {2015},
  volume = {59},
  pages = {67--85},
  howpublished = {\url{https://www.sciencedirect.com/science/article/abs/pii/S0950584914002390}}
}

@misc{gharchive,
  title = {{GH Archive}},
  howpublished = {\url{https://www.gharchive.org/}},
  note = {Accessed 2026-08-21}
}

@misc{github_events_api,
  title = {{REST API} endpoints for events},
  author = {{GitHub Docs}},
  howpublished = {\url{https://docs.github.com/en/rest/activity/events}},
  note = {Accessed 2026-08-21}
}

@misc{gharchive_payload,
  title = {{GH Archive} payload field documentation},
  howpublished = {\url{https://www.gharchive.org/}},
  note = {Accessed 2026-08-21}
}

@misc{worldofcode,
  title = {World of Code},
  howpublished = {\url{https://worldofcode.org/docs/}},
  note = {Accessed 2026-08-21}
}

@misc{woc_identity_disambiguation,
  title = {Scaling Author Identity Disambiguation to the World of Code: A Methodology},
  howpublished = {arXiv:2607.06920. \url{https://arxiv.org/abs/2607.06920}},
  year = {2026}
}

@misc{woc_hack_tutorial,
  title = {woc-hack/tutorial},
  howpublished = {\url{https://github.com/woc-hack/tutorial}},
  note = {Accessed 2026-08-21}
}

@misc{botcommit_mapping,
  title = {A mapping between Bot Commit, Projects, Files, and Blobs},
  howpublished = {Zenodo. \url{https://zenodo.org/records/3699665}}
}

@misc{ghtorrent_github,
  title = {ghtorrent/ghtorrent.org},
  howpublished = {\url{https://github.com/ghtorrent/ghtorrent.org}},
  note = {Accessed 2026-08-21}
}

@misc{ghtorrent_downloads,
  title = {{GHTorrent} downloads page},
  note = {Dead domain. \url{https://ghtorrent.org/downloads.html}}
}

@misc{hoffa_bigquery,
  title = {Analyzing {GitHub} with {BigQuery} and other tools},
  author = {Hoffa, Felipe},
  howpublished = {\url{https://github.com/fhoffa/analyzing_github}}
}

@misc{librariesio_dump,
  title = {Libraries.io Open Source Repository and Dependency Metadata},
  howpublished = {Zenodo. \url{https://zenodo.org/records/3626071}}
}

@inproceedings{avelino2019abandonment,
  title = {On the abandonment and survival of open source projects: An empirical investigation},
  author = {Avelino, Gu\'{i}lherme and Constantinou, Eleni and Valente, Marco Tulio and Serebrenik, Alexander},
  booktitle = {2019 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)},
  year = {2019}
}
```

### [28] TOOL RESULT — Write · 2026-08-21 16:22:59 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_4_assemble_paper/paper/workspace/references.bib", "content": "@misc{chaoss_absence_factor,\n  title = {Metric: Contributor Absence Factor},\n  author = {{CHAOSS}},\n  howpublished = {\\url{https://www.chaoss.community/kb/metric-contributor-absence-factor/}},\n  note = {Accessed 2026-08-21}\n}\n\n@misc{chaoss_elephant_factor,\n  title = {Metric: Elephant Factor},\n  author = {{CHAOSS}},\n  howpublished = {\\url{https://www.chaoss.community/kb/metric-elephant-factor/}},\n  note = {Accessed 2026-08-21}\n}\n\n@misc{chaoss_newcomer_experience,\n  title = {Metric: Newcomer Experience},\n  author = {{CHAOSS}},\n  howpublished = {\\url{https://www.chaoss.community/kb/metric-newcomer-experience/}},\n  note = {Accessed 2026-08-21}\n}\n\n@misc{apache_incubator_graduation,\n  title = {Guide to Successful Graduation},\n  author = {{Apache Incubator}},\n  howpublished = {\\url{https://incubator.apache.org/guides/graduation.html}},\n  note = {Accessed 2026-08-21}\n}\n\n@misc{apache_maturity_model,\n  title = {Apache Project Maturity Model},\n  author = {{Apache Software Foundation}},\n  howpublished = {\\url{https://community.apache.org/apache-way/apache-project-maturity-model.html}},\n  note = {Accessed 2026-08-21}\n}\n\n@inproceedings{jergensen2011onion,\n  title = {The Onion Patch: Migration in Open Source Ecosystems},\n  author = {Jergensen, Christian and Sarma, Anita and Wagstrom, Patrick},\n  booktitle = {Proceedings of the 7th International Symposium on Open Collaboration (OpenSym)},\n  year = {2011},\n  doi = {10.1145/2025113.2025127},\n  howpublished = {\\url{https://dl.acm.org/doi/10.1145/2025113.2025127}}\n}\n\n@article{steinmacher2015barriers,\n  title = {A systematic literature review on the barriers faced by newcomers to open source software projects},\n  author = {Steinmacher, Igor and Silva, Marco Aurelio Graciotto and Gerosa, Marco Aurelio and Redmiles, David F.},\n  journal = {Information and Software Technology},\n  year = {2015},\n  volume = {59},\n  pages = {67--85},\n  howpublished = {\\url{https://www.sciencedirect.com/science/article/abs/pii/S0950584914002390}}\n}\n\n@misc{gharchive,\n  title = {{GH Archive}},\n  howpublished = {\\url{https://www.gharchive.org/}},\n  note = {Accessed 2026-08-21}\n}\n\n@misc{github_events_api,\n  title = {{REST API} endpoints for events},\n  author = {{GitHub Docs}},\n  howpublished = {\\url{https://docs.github.com/en/rest/activity/events}},\n  note = {Accessed 2026-08-21}\n}\n\n@misc{gharchive_payload,\n  title = {{GH Archive} payload field documentation},\n  howpublished = {\\url{https://www.gharchive.org/}},\n  note = {Accessed 2026-08-21}\n}\n\n@misc{worldofcode,\n  title = {World of Code},\n  howpublished = {\\url{https://worldofcode.org/docs/}},\n  note = {Accessed 2026-08-21}\n}\n\n@misc{woc_identity_disambiguation,\n  title = {Scaling Author Identity Disambiguation to the World of Code: A Methodology},\n  howpublished = {arXiv:2607.06920. \\url{https://arxiv.org/abs/2607.06920}},\n  year = {2026}\n}\n\n@misc{woc_hack_tutorial,\n  title = {woc-hack/tutorial},\n  howpublished = {\\url{https://github.com/woc-hack/tutorial}},\n  note = {Accessed 2026-08-21}\n}\n\n@misc{botcommit_mapping,\n  title = {A mapping between Bot Commit, Projects, Files, and Blobs},\n  howpublished = {Zenodo. \\url{https://zenodo.org/records/3699665}}\n}\n\n@misc{ghtorrent_github,\n  title = {ghtorrent/ghtorrent.org},\n  howpublished = {\\url{https://github.com/ghtorrent/ghtorrent.org}},\n  note = {Accessed 2026-08-21}\n}\n\n@misc{ghtorrent_downloads,\n  title = {{GHTorrent} downloads page},\n  note = {Dead domain. \\url{https://ghtorrent.org/downloads.html}}\n}\n\n@misc{hoffa_bigquery,\n  title = {Analyzing {GitHub} with {BigQuery} and other tools},\n  author = {Hoffa, Felipe},\n  howpublished = {\\url{https://github.com/fhoffa/analyzing_github}}\n}\n\n@misc{librariesio_dump,\n  title = {Libraries.io Open Source Repository and Dependency Metadata},\n  howpublished = {Zenodo. \\url{https://zenodo.org/records/3626071}}\n}\n\n@inproceedings{avelino2019abandonment,\n  title = {On the abandonment and survival of open source projects: An empirical investigation},\n  author = {Avelino, Gu\\'{i}lherme and Constantinou, Eleni and Valente, Marco Tulio and Serebrenik, Alexander},\n  booktitle = {2019 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)},\n  year = {2019}\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [29] ASSISTANT · 2026-08-21 16:24:13 UTC

```
Now let's build paper.tex.
```

### [30] TOOL CALL — Write · 2026-08-21 16:24:13 UTC

```
File: /ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_4_assemble_paper/paper/workspace/paper.tex

\documentclass[11pt,letterpaper]{article}
\usepackage{graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings}
\geometry{margin=1in}
\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}

\title{Authority Diffusion Before Founder Departure: Diagnosing Sample Starvation in OSS Survival Research and a Liveness-Unbiased Corpus to Fix It}
\author{}
\date{}

\begin{document}
\maketitle

\begin{abstract}
Whether an open-source project survives its founder's departure is widely assumed to depend on how much ownership had already diffused to other contributors before that departure, yet this pre-departure trend is absent from existing community-health metrics, which all score diversity at a single snapshot rather than as a trajectory leading up to a departure. We built a pipeline that reimplements a published Degree-of-Authorship / Truck-Factor methodology to detect founder-only ownership-departure events and to compute a pre-departure authority-diffusion score from commit history, then applied it to a large GitHub corpus sampled by current popularity. The pipeline located too few genuine departure events for any of the three planned statistical tests to run, each instead reporting insufficient sample size. We show this null is a sampling artifact rather than evidence about the hypothesis: a rigor-gap re-analysis finds this corpus's departure-event incidence and its founder-only survival rate are both statistically far from a published external population baseline, in the direction expected if the sampling frame systematically favors repositories that already survived, and that a companion robustness check could not have detected an effect at any of the budgets it was run at, due to an undocumented cap in its implementation. As a remedy, we release a second corpus built with no filter on current liveness, sampled purely by historical creation and activity windows, in which the large majority of repositories are non-surviving by a two-year-inactivity proxy -- giving the pre-departure authority-diffusion hypothesis a corpus in which non-surviving projects are actually represented for the first time.
\end{abstract}

\section{Introduction}

\subsection{The problem}

An open-source project's founder eventually stops committing. Some projects keep going; others go quiet within a year. The literature has metrics for measuring how concentrated a project's ownership is at a single point in time, but not for measuring how that concentration was \emph{changing} in the months before the founder left -- whether responsibility had already spread to other contributors, or whether the founder was still the sole owner of every file up to their last commit. We call this pre-departure trend \emph{authority diffusion}, and we test whether it predicts survival beyond the snapshot statistics (team size, commit volume, file count) that existing metrics already capture.

\subsection{Why it matters}

Community-health tooling already tries to answer a version of this question after the fact: CHAOSS's Contributor Absence Factor counts how many top contributors are needed to reach 50\% of a project's commits, and its Elephant Factor does the analogous count over organizations, but CHAOSS's own knowledge base documents both as computable only as a snapshot or as repeated snapshots, never as a fitted trajectory leading into a departure \citep{chaoss_absence_factor,chaoss_elephant_factor}. The Apache Software Foundation operationalizes ``diversity'' for graduation as a binary committee judgment -- at least three legally independent committers, no single essential company -- rather than a continuous, predictive statistic \citep{apache_incubator_graduation}. A validated pre-departure trajectory signal would let maintainers, funders, and package-registry risk tooling flag an at-risk project \emph{before} the founder's last commit, rather than after the project has already gone quiet long enough to trip a Contributor Absence Factor snapshot.

\subsection{Why it is hard}

Testing this hypothesis needs three things simultaneously: (a) a reliable, automatic detector for the event itself -- a founder truly stepping away, not merely going quiet for a sprint -- (b) commit-level history reaching back far enough before that event to fit a pre-departure trend, and (c) a sample of repositories that is not itself pre-filtered on the outcome being measured. We show in Section~\ref{sec:results} that ordinary GitHub sampling strategies violate (c) by construction: search and trending endpoints surface repositories that are popular and active \emph{today}, which already conditions the sample on having survived long enough to accumulate that popularity. A repository whose founder left and which then died six months later is, almost by definition, one that never accumulated the stars needed to be discovered by a present-day search query.

\subsection{Why existing approaches fall short}

Avelino et al.'s (ESEM 2019) \citep{avelino2019abandonment} Truck-Factor / Degree-of-Authorship (DOA) pipeline is the closest prior instrument: it detects Truck-Factor-Detachment-Departure (TFDD) events from commit history and reports population-level TFDD incidence and post-TFDD survival rates from a large GitHub sample. It was not designed to fit a \emph{pre-departure} trajectory, and -- more importantly for the present study -- it was built on exactly the kind of popularity-conditioned frame described above. We reused its DOA/TFDD machinery in full (Section~\ref{sec:method}) rather than re-deriving it, but applied it to our own sampling frame; the corpus we built for that first pass turned out to inherit the same liveness conditioning, which is the central negative finding of this paper.

\subsection{What we did and what we found}

We built the Avelino-style DOA/TFDD pipeline (Section~\ref{sec:method}), ran it on a 3,427-repository GitHub corpus, and found that only 6 repositories produced a usable founder-only TFDD event (Section~\ref{sec:starvation}) -- an error breakdown dominated by 3,409 repositories with no minable commit history at all. Every downstream statistical test we had planned (matched-pairs survival comparison, BH-corrected logistic/ordinal regression, window-shuffle placebo check) consequently reported \texttt{insufficient\_n} rather than a substantive result. Rather than treat this null as evidence about the hypothesis, we ran a dedicated rigor-gap evaluation (Section~\ref{sec:artifact}) that shows the corpus itself is biased toward survival -- its TFDD incidence and founder-only survival rate are both statistically distinguishable from Avelino et al.'s own published population figures -- and that the placebo check's apparent robustness across simulation budgets is a structural artifact of an undocumented per-repository draw cap, not evidence that six events are enough. We then built a second corpus (Section~\ref{sec:corpus}) that removes the liveness conditioning by sampling on historical creation/push-date windows only, and report its composition as the resource this hypothesis needs to be tested properly. \textbf{This paper's contribution is therefore diagnostic and infrastructural, not a confirmed or refuted authority-diffusion effect}: we did not obtain enough founder-only TFDD events in either corpus to run the planned regression, and we report that limitation explicitly rather than a spurious point estimate from n=6.

\subsubsection*{Summary of Contributions}
\begin{itemize}
  \item A working reimplementation of Avelino et al.'s DOA/Truck-Factor/TFDD pipeline extended with a pre-departure authority-diffusion covariate, applied at 3,427-repository scale (Section~\ref{sec:method}).
  \item A rigor-gap evaluation that formally quantifies the survivorship bias in a popularity-sampled TFDD corpus against Avelino et al.'s own published population statistics, and that exposes an undocumented hard cap that makes the pipeline's placebo check vacuous rather than confirmatory (Section~\ref{sec:results}).
  \item A positioning of the pre-departure authority-diffusion construct against the nearest existing OSS community-health metrics and onboarding literature, establishing that none of them measure a pre-departure trend (Section~\ref{sec:related}).
  \item A second, 67-repository corpus sampled without any liveness or popularity filter, in which 72\% of repositories are non-surviving by a two-year-inactivity proxy, released as the resource needed to run this hypothesis test with an adequately powered, unbiased sample (Section~\ref{sec:corpus}).
\end{itemize}

\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/fig1_v0.jpg}
  \caption{The founder-departure authority-diffusion construct: in the 6-12 month window before a founder-only Truck-Factor-Detachment-Departure (TFDD) event, authority over the codebase either stays concentrated with the founder (low diffusion, left) or spreads to other DOA-recognized file owners (high diffusion, right). At-TFDD snapshot covariates (developer count, commits, files) are measured at the moment of TFDD; the pre-departure covariates (founder commit-share, count of distinct non-founder owners) are measured strictly before it to avoid post-departure leakage.}
  \label{fig:fig1}
\end{figure}

\section{Related Work}
\label{sec:related}

\textbf{Snapshot diversity metrics.} CHAOSS's Contributor Absence Factor (formerly Bus Factor) sorts contributors by contribution volume and counts how many are needed to reach 50\% of total contributions; CHAOSS's own documentation states this can be measured as a single snapshot or repeated at intervals, but no CHAOSS metric fits or validates a continuous pre-departure \emph{trend} \citep{chaoss_absence_factor}. The sibling Elephant Factor, the organizational analogue, is explicitly documented as snapshot-only and as misrepresenting project history if computed cumulatively \citep{chaoss_elephant_factor}. Neither metric is designed to answer ``was authority already diffusing before this specific person left,'' which is the question this paper's construct targets.

\textbf{Governance-gate diversity.} The Apache Incubator's graduation guide requires at least three legally independent committers and no single dominating company as a binary, committee-judged gate for exiting incubation \citep{apache_incubator_graduation}; the Apache Project Maturity Model's retrievable CD-series criteria turned out on inspection to cover code governance (distribution, reproducible builds, provenance) rather than community diversity, and a true diversity-specific code series was not located \citep{apache_maturity_model}. Both instruments answer a governance-compliance question at a point in time, not a predictive one.

\textbf{Newcomer trajectories.} The onion model of OSS socialization describes contributors migrating \emph{inward}, from peripheral participation (mailing lists, bug reports) toward the code-owning core, as skill and reputation accrue \citep{jergensen2011onion}, and a systematic review of newcomer barriers organizes the obstacles to that inward migration into five categories, most centrally prior technical skill and community responsiveness \citep{steinmacher2015barriers}. Both study the mirror-image trajectory to the one this paper is interested in: contributors moving \emph{toward} ownership, rather than a founder's ownership moving \emph{away} from them before departure.

\textbf{Population-scale TFDD baselines.} Avelino et al. (ESEM 2019) \citep{avelino2019abandonment} is the direct methodological ancestor of the pipeline used here (Section~\ref{sec:method}): its DOA weighting and Truck-Factor-Detachment-Departure detection are reused verbatim, and its published population-level TFDD incidence (16.3\%) and founder-only-TFDD survival rate (40.6\%) are the external baseline this paper's rigor-gap evaluation tests our own corpora against (Section~\ref{sec:artifact}).

\textbf{Data-source landscape.} GH Archive exposes GitHub's public event stream (15+ event types) with no token required, but its \texttt{PushEvent} payload carries only commit SHA/author/message pointers -- never file lists or diffs \citep{gharchive,github_events_api,gharchive_payload} -- so it can supply a repository-selection frame but not the commit-level content this study needs. World of Code holds full commit/blob/file/author cross-referencing at the right granularity \citep{worldofcode,woc_identity_disambiguation} but is gated behind an SSH-registration approval process \citep{woc_hack_tutorial}, and its self-serve Zenodo derivative covers only bot commits \citep{botcommit_mapping}. GHTorrent, an earlier commit-mining service, is confirmed dead: its domain now redirects to an unrelated site and its BigQuery mirror has been stale since 2019 \citep{ghtorrent_github,ghtorrent_downloads,hoffa_bigquery}. Libraries.io's Zenodo dump is live and gives repository-selection metadata at scale but carries no commit-level history \citep{librariesio_dump}. We concluded that a repository-selection frame independent of present-day liveness (built from historical creation/push-date search, Section~\ref{sec:corpus}) combined with a direct, unauthenticated \texttt{git clone} of each selected repository's full history is the only path that is simultaneously live, token-cheap, and free of the liveness conditioning this paper's Section~\ref{sec:results} diagnoses.

\section{Method: DOA/TFDD Pipeline and the Authority-Diffusion Covariate}
\label{sec:method}

We reimplement Avelino et al.'s Degree-of-Authorship (DOA) weighting over per-file commit history to identify, for each repository, the point at which a single ``founder'' author accounts for the plurality of authorship (a Truck-Factor-Detachment-Departure, TFDD, event: the date the founder's authorship share falls below the threshold that would make their departure survivable without loss of institutional knowledge). A TFDD event is classed \emph{founder-only} when the departing author is the repository's original committer, distinguishing genuine founder succession from a later core contributor's departure.

For every founder-only TFDD event, we compute two families of covariates purely from commits dated \textbf{before} the event, to avoid any post-departure leakage:

\begin{itemize}
  \item \textbf{At-TFDD snapshot covariates} (Avelino et al.'s original feature set): number of active developers, total commits, and total files at the moment of TFDD.
  \item \textbf{Pre-departure authority-diffusion covariates} (this paper's addition): the founder's commit-share in the 6-12 month window immediately before TFDD, and the count of distinct non-founder contributors who already held DOA-recognized file ownership in that same window (\texttt{n\_diffuse\_owners\_pre}). A single scalar \texttt{diffusion\_score} combines the two.
\end{itemize}

The outcome is 18-month post-TFDD survival, labeled from subsequent commit activity (\texttt{survived\_binary}), with three planned analyses: (1) a nearest-neighbor matched-pairs comparison of high- versus low-diffusion repositories controlling for the snapshot covariates, (2) BH-corrected logistic regression (binary survival) and ordinal regression (a graded survival label) with diffusion score as the covariate of interest, and (3) a window-shuffle placebo check that repeatedly reassigns which pre-TFDD window is treated as ``pre-departure'' to establish whether the observed diffusion-survival association could arise by chance.

\section{Results}
\label{sec:results}

\subsection{Sample starvation at 3,427 repositories}
\label{sec:starvation}

Running the pipeline on a 3,427-repository corpus sampled by current GitHub popularity/activity produced only 6 founder-only TFDD events. The error breakdown for the remaining 3,421 repositories was: 3,409 had no minable commit history at all under the mining budget used, 4 had a TFDD event that was not founder-only, and 2 were right-censored (no 18-month post-TFDD window had yet elapsed). At n=6, every planned statistical test failed outright: the matched-pairs comparison found zero eligible pairs even under relaxed matching, and both the logistic and ordinal regressions reported \texttt{insufficient\_n}.

\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/fig2_v0.pdf}
  \caption{Funnel of the 3,427-repository popularity-sampled corpus through the DOA/TFDD pipeline. The overwhelming majority (3,409) were dropped for having no minable commit history; only 6 repositories produced a usable founder-only TFDD event, too few for any of the three planned statistical tests.}
  \label{fig:fig2}
\end{figure}

\subsection{The null is a sampling artifact, not evidence of no effect}
\label{sec:artifact}

A dedicated rigor-gap evaluation re-examined the 6-event corpus against Avelino et al.'s own published population statistics using Wilson 95\% confidence intervals and two-proportion z-tests. Two results indicate the corpus is not a fair sample of the population Avelino et al. characterized:

\begin{itemize}
  \item \textbf{TFDD incidence.} 73.3\% of this corpus's repositories (11 of 15 candidates carried through to the full table) exhibit any TFDD event, versus 16.3\% in Avelino et al.'s published population -- a two-proportion z=5.89, p=3.8e-9.
  \item \textbf{Founder-only-TFDD survival.} 100\% (5 of 5) of this corpus's founder-only-TFDD repositories survived 18 months post-departure, versus 40.6\% in Avelino et al.'s population (Wilson 95\% CI [0.606, 0.710] for their 66\% TF=1 baseline versus this corpus's 45.5\% TF=1 fraction, CI [0.213, 0.720]) -- z=2.67, p=0.0075.
\end{itemize}

Both deviations point the same direction: a corpus selected for present-day popularity over-represents repositories that already survived whatever ownership transition they went through, which is exactly the confound the pre-departure authority-diffusion hypothesis needs an unbiased corpus to rule out.

\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/fig3_v0.pdf}
  \caption{Rigor-gap evaluation of the popularity-sampled corpus against Avelino et al.'s published population baseline: TFDD incidence and founder-only-TFDD survival rate both diverge sharply and significantly in the direction consistent with survivorship conditioning.}
  \label{fig:fig3}
\end{figure}

Separately, the evaluation audited the placebo check's own implementation and found a previously undocumented \textbf{20-draw-per-repository hard cap} -- the code path never reaches the ``500 iterations'' figure the original summary cited, because it caps each repository's contribution to the placebo distribution at 20 draws regardless of the requested budget. Re-running the placebo check at three budgets (10, 60, and 2,000 requested draws) produced an identical qualitative conclusion at all three, which is not evidence of robustness: at the 20-draw hard cap, the theoretical floor on the smallest detectable effect is 4.8\%, and at the (never-reached) 500-draw figure the floor would be 0.2\% -- meaning the check is structurally incapable of resolving an effect at n=6 regardless of how large the requested budget is set. The evaluation additionally spot-checked 3 of the corpus's 15 repositories against their raw source records and found all three aliases consistent (no full-corpus audit was run; 80\% of the corpus remains unchecked by this pass).

\subsection{What we did not test}

No expanded or non-liveness-conditioned corpus existed among this round's dependencies to run head-to-head against the population baseline, so the claim that the null in Section~\ref{sec:starvation} is a design flaw rather than a genuine power problem rests on the structural argument and evidence in Section~\ref{sec:artifact}, not on a second frame producing more TFDD events. Section~\ref{sec:corpus} supplies that second frame as this paper's concrete, falsifiable next step: if the pre-departure authority-diffusion hypothesis holds, a non-liveness-conditioned corpus should yield both a TFDD incidence closer to Avelino et al.'s 16.3\% population figure and a founder-only survival rate closer to their 40.6\%, rather than reproducing this section's 73.3\%/100\% figures.

\section{A Liveness-Non-Conditioned Corpus}
\label{sec:corpus}

To remove the conditioning identified in Section~\ref{sec:artifact}, we built a second 67-repository corpus using GitHub's Search API \texttt{created:}/\texttt{pushed:} date qualifiers to sample purely on \textbf{historical} creation and push-date windows (2011-2015) across eight languages, applying \textbf{no filter on present-day archived, starred, or maintained status}. Of 450 candidates screened, 383 (85\%) were rejected -- mostly for too few commits or too short a history to fit a pre-departure trajectory -- leaving 67 accepted repositories. Of those, 48 (72\%) have had no commit in at least two years as of build time (our non-surviving proxy) and 7 are archived by GitHub itself, meaning non-surviving projects are represented in this corpus for the first time at a scale the original 3,427-repository frame never produced (Section~\ref{sec:starvation}: only 2 right-censored, 0 confirmed non-surviving, among 6 founder-only TFDD events).

\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/fig4_v0.pdf}
  \caption{Composition of the 67-repository liveness-non-conditioned corpus: screening outcomes for the 450 historically-sampled candidates, and the survival-label breakdown of the 67 accepted repositories.}
  \label{fig:fig4}
\end{figure}

Each repository's record standardizes to one example carrying only pre-departure-observable input features (computed strictly before the founder's last commit, to avoid the leakage the original pipeline already guards against in Section~\ref{sec:method}) and one of three survival labels: \texttt{survived}, \texttt{non\_surviving}, or \texttt{unknown\_insufficient\_post\_departure\_window} for repositories without enough elapsed history to call a label at all. This corpus is released as the direct input to Section~\ref{sec:method}'s pipeline for the next round of this study; running it end to end and reporting the resulting TFDD incidence and founder-only survival rate against Avelino et al.'s population baseline is the falsifiable prediction stated in Section~\ref{sec:results}.3.

\section{Discussion}

\textbf{The headline finding of this paper is methodological.} A popularity-sampled GitHub corpus produced too few founder-only TFDD events to test the pre-departure authority-diffusion hypothesis (n=6), and the rigor-gap evaluation in Section~\ref{sec:artifact} shows this was not bad luck: the corpus's TFDD incidence and founder-only survival rate both differ from Avelino et al.'s population figures in the direction consistent with survivorship conditioning, and the placebo check that appeared to certify the pipeline's null result was, on inspection, structurally incapable of detecting an effect at any of the budgets it was run at. We consider this worth reporting on its own terms rather than smoothing over: an automated pipeline that runs to completion and reports a stable null across three simulation budgets looks, from the outside, like a well-powered negative result. Section~\ref{sec:artifact} shows it is not, and the distinction matters for anyone building on TFDD-style pipelines with any GitHub sample drawn by present-day popularity, stars, or trending status.

\textbf{Limitations.} The spot-check audit of the original corpus's alias resolution covered only 3 of 15 repositories (80\% unchecked). The new liveness-non-conditioned corpus (Section~\ref{sec:corpus}) has not yet been run through the DOA/TFDD pipeline of Section~\ref{sec:method}, so we cannot yet report whether it in fact yields more founder-only TFDD events or a less skewed incidence/survival rate than the original frame -- that comparison is the explicit next step, not a result claimed here. The non-surviving proxy (no commit in $\geq$2 years) is a coarse label; a repository can be dormant and later revived, and the corpus's \texttt{unknown\_insufficient\_post\_departure\_window} label exists precisely to avoid forcing a survival call where the post-departure window is too short. Finally, both corpora are drawn from GitHub only; repositories hosted elsewhere or migrated away from GitHub after founder departure are systematically invisible to any GitHub-only sampling frame, including ours.

\section{Conclusion}

We set out to test whether authority diffusing away from a project's founder before their departure predicts survival beyond existing snapshot diversity metrics, and found instead that the obvious way to build a GitHub corpus for this question -- sampling by current popularity -- silently conditions the sample on survival, starving the founder-only-TFDD event count down to 6 and rendering every planned statistical test uninformative. We quantified that conditioning against Avelino et al.'s own published population baseline (TFDD incidence 73.3\% vs. 16.3\%, z=5.89, p=3.8e-9; founder-only survival 100\% vs. 40.6\%, z=2.67, p=0.0075) and showed the pipeline's placebo check could not have detected an effect at n=6 regardless of its requested simulation budget, due to an undocumented 20-draw-per-repository cap. We release a 67-repository corpus sampled without any liveness conditioning, 72\% of which are non-surviving by a two-year-inactivity proxy, as the concrete resource needed to run this hypothesis test properly.

Future work: (1) run the Section~\ref{sec:method} pipeline against the Section~\ref{sec:corpus} corpus and report whether its TFDD incidence and founder-only survival rate move toward Avelino et al.'s population figures, as predicted in Section~\ref{sec:results}.3; (2) complete the full-corpus alias audit begun in Section~\ref{sec:artifact}, extending the 3-of-15 spot-check to all repositories in both corpora; (3) locate or derive the Apache Project Maturity Model's community-diversity-specific criteria codes, left unresolved in Section~\ref{sec:related}, to add a second governance-gate baseline alongside Avelino et al.'s population statistics.

\bibliographystyle{plainnat}
\bibliography{references}

\end{document}
```

### [31] TOOL RESULT — Write · 2026-08-21 16:24:13 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_4_assemble_paper/paper/workspace/paper.tex", "content": "\\documentclass[11pt,letterpaper]{article}\n\\usepackage{graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings}\n\\geometry{margin=1in}\n\\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}\n\n\\title{Authority Diffusion Before Founder Departure: Diagnosing Sample Starvation in OSS Survival Research and a Liveness-Unbiased Corpus to Fix It}\n\\author{}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nWhether an open-source project survives its founder's departure is widely assumed to depend on how much ownership had already diffused to other contributors before that departure, yet this pre-departure trend is absent from existing community-health metrics, which all score diversity at a single snapshot rather than as a trajectory leading up to a departure. We built a pipeline that reimplements a published Degree-of-Authorship / Truck-Factor methodology to detect founder-only ownership-departure events and to compute a pre-departure authority-diffusion score from commit history, then applied it to a large GitHub corpus sampled by current popularity. The pipeline located too few genuine departure events for any of the three planned statistical tests to run, each instead reporting insufficient sample size. We show this null is a sampling artifact rather than evidence about the hypothesis: a rigor-gap re-analysis finds this corpus's departure-event incidence and its founder-only survival rate are both statistically far from a published external population baseline, in the direction expected if the sampling frame systematically favors repositories that already survived, and that a companion robustness check could not have detected an effect at any of the budgets it was run at, due to an undocumented cap in its implementation. As a remedy, we release a second corpus built with no filter on current liveness, sampled purely by historical creation and activity windows, in which the large majority of repositories are non-surviving by a two-year-inactivity proxy -- giving the pre-departure authority-diffusion hypothesis a corpus in which non-surviving projects are actually represented for the first time.\n\\end{abstract}\n\n\\section{Introduction}\n\n\\subsection{The problem}\n\nAn open-source project's founder eventually stops committing. Some projects keep going; others go quiet within a year. The literature has metrics for measuring how concentrated a project's ownership is at a single point in time, but not for measuring how that concentration was \\emph{changing} in the months before the founder left -- whether responsibility had already spread to other contributors, or whether the founder was still the sole owner of every file up to their last commit. We call this pre-departure trend \\emph{authority diffusion}, and we test whether it predicts survival beyond the snapshot statistics (team size, commit volume, file count) that existing metrics already capture.\n\n\\subsection{Why it matters}\n\nCommunity-health tooling already tries to answer a version of this question after the fact: CHAOSS's Contributor Absence Factor counts how many top contributors are needed to reach 50\\% of a project's commits, and its Elephant Factor does the analogous count over organizations, but CHAOSS's own knowledge base documents both as computable only as a snapshot or as repeated snapshots, never as a fitted trajectory leading into a departure \\citep{chaoss_absence_factor,chaoss_elephant_factor}. The Apache Software Foundation operationalizes ``diversity'' for graduation as a binary committee judgment -- at least three legally independent committers, no single essential company -- rather than a continuous, predictive statistic \\citep{apache_incubator_graduation}. A validated pre-departure trajectory signal would let maintainers, funders, and package-registry risk tooling flag an at-risk project \\emph{before} the founder's last commit, rather than after the project has already gone quiet long enough to trip a Contributor Absence Factor snapshot.\n\n\\subsection{Why it is hard}\n\nTesting this hypothesis needs three things simultaneously: (a) a reliable, automatic detector for the event itself -- a founder truly stepping away, not merely going quiet for a sprint -- (b) commit-level history reaching back far enough before that event to fit a pre-departure trend, and (c) a sample of repositories that is not itself pre-filtered on the outcome being measured. We show in Section~\\ref{sec:results} that ordinary GitHub sampling strategies violate (c) by construction: search and trending endpoints surface repositories that are popular and active \\emph{today}, which already conditions the sample on having survived long enough to accumulate that popularity. A repository whose founder left and which then died six months later is, almost by definition, one that never accumulated the stars needed to be discovered by a present-day search query.\n\n\\subsection{Why existing approaches fall short}\n\nAvelino et al.'s (ESEM 2019) \\citep{avelino2019abandonment} Truck-Factor / Degree-of-Authorship (DOA) pipeline is the closest prior instrument: it detects Truck-Factor-Detachment-Departure (TFDD) events from commit history and reports population-level TFDD incidence and post-TFDD survival rates from a large GitHub sample. It was not designed to fit a \\emph{pre-departure} trajectory, and -- more importantly for the present study -- it was built on exactly the kind of popularity-conditioned frame described above. We reused its DOA/TFDD machinery in full (Section~\\ref{sec:method}) rather than re-deriving it, but applied it to our own sampling frame; the corpus we built for that first pass turned out to inherit the same liveness conditioning, which is the central negative finding of this paper.\n\n\\subsection{What we did and what we found}\n\nWe built the Avelino-style DOA/TFDD pipeline (Section~\\ref{sec:method}), ran it on a 3,427-repository GitHub corpus, and found that only 6 repositories produced a usable founder-only TFDD event (Section~\\ref{sec:starvation}) -- an error breakdown dominated by 3,409 repositories with no minable commit history at all. Every downstream statistical test we had planned (matched-pairs survival comparison, BH-corrected logistic/ordinal regression, window-shuffle placebo check) consequently reported \\texttt{insufficient\\_n} rather than a substantive result. Rather than treat this null as evidence about the hypothesis, we ran a dedicated rigor-gap evaluation (Section~\\ref{sec:artifact}) that shows the corpus itself is biased toward survival -- its TFDD incidence and founder-only survival rate are both statistically distinguishable from Avelino et al.'s own published population figures -- and that the placebo check's apparent robustness across simulation budgets is a structural artifact of an undocumented per-repository draw cap, not evidence that six events are enough. We then built a second corpus (Section~\\ref{sec:corpus}) that removes the liveness conditioning by sampling on historical creation/push-date windows only, and report its composition as the resource this hypothesis needs to be tested properly. \\textbf{This paper's contribution is therefore diagnostic and infrastructural, not a confirmed or refuted authority-diffusion effect}: we did not obtain enough founder-only TFDD events in either corpus to run the planned regression, and we report that limitation explicitly rather than a spurious point estimate from n=6.\n\n\\subsubsection*{Summary of Contributions}\n\\begin{itemize}\n  \\item A working reimplementation of Avelino et al.'s DOA/Truck-Factor/TFDD pipeline extended with a pre-departure authority-diffusion covariate, applied at 3,427-repository scale (Section~\\ref{sec:method}).\n  \\item A rigor-gap evaluation that formally quantifies the survivorship bias in a popularity-sampled TFDD corpus against Avelino et al.'s own published population statistics, and that exposes an undocumented hard cap that makes the pipeline's placebo check vacuous rather than confirmatory (Section~\\ref{sec:results}).\n  \\item A positioning of the pre-departure authority-diffusion construct against the nearest existing OSS community-health metrics and onboarding literature, establishing that none of them measure a pre-departure trend (Section~\\ref{sec:related}).\n  \\item A second, 67-repository corpus sampled without any liveness or popularity filter, in which 72\\% of repositories are non-surviving by a two-year-inactivity proxy, released as the resource needed to run this hypothesis test with an adequately powered, unbiased sample (Section~\\ref{sec:corpus}).\n\\end{itemize}\n\n\\begin{figure}[!htbp]\n  \\centering\n  \\includegraphics[width=0.92\\textwidth,keepaspectratio]{figures/fig1_v0.jpg}\n  \\caption{The founder-departure authority-diffusion construct: in the 6-12 month window before a founder-only Truck-Factor-Detachment-Departure (TFDD) event, authority over the codebase either stays concentrated with the founder (low diffusion, left) or spreads to other DOA-recognized file owners (high diffusion, right). At-TFDD snapshot covariates (developer count, commits, files) are measured at the moment of TFDD; the pre-departure covariates (founder commit-share, count of distinct non-founder owners) are measured strictly before it to avoid post-departure leakage.}\n  \\label{fig:fig1}\n\\end{figure}\n\n\\section{Related Work}\n\\label{sec:related}\n\n\\textbf{Snapshot diversity metrics.} CHAOSS's Contributor Absence Factor (formerly Bus Factor) sorts contributors by contribution volume and counts how many are needed to reach 50\\% of total contributions; CHAOSS's own documentation states this can be measured as a single snapshot or repeated at intervals, but no CHAOSS metric fits or validates a continuous pre-departure \\emph{trend} \\citep{chaoss_absence_factor}. The sibling Elephant Factor, the organizational analogue, is explicitly documented as snapshot-only and as misrepresenting project history if computed cumulatively \\citep{chaoss_elephant_factor}. Neither metric is designed to answer ``was authority already diffusing before this specific person left,'' which is the question this paper's construct targets.\n\n\\textbf{Governance-gate diversity.} The Apache Incubator's graduation guide requires at least three legally independent committers and no single dominating company as a binary, committee-judged gate for exiting incubation \\citep{apache_incubator_graduation}; the Apache Project Maturity Model's retrievable CD-series criteria turned out on inspection to cover code governance (distribution, reproducible builds, provenance) rather than community diversity, and a true diversity-specific code series was not located \\citep{apache_maturity_model}. Both instruments answer a governance-compliance question at a point in time, not a predictive one.\n\n\\textbf{Newcomer trajectories.} The onion model of OSS socialization describes contributors migrating \\emph{inward}, from peripheral participation (mailing lists, bug reports) toward the code-owning core, as skill and reputation accrue \\citep{jergensen2011onion}, and a systematic review of newcomer barriers organizes the obstacles to that inward migration into five categories, most centrally prior technical skill and community responsiveness \\citep{steinmacher2015barriers}. Both study the mirror-image trajectory to the one this paper is interested in: contributors moving \\emph{toward} ownership, rather than a founder's ownership moving \\emph{away} from them before departure.\n\n\\textbf{Population-scale TFDD baselines.} Avelino et al. (ESEM 2019) \\citep{avelino2019abandonment} is the direct methodological ancestor of the pipeline used here (Section~\\ref{sec:method}): its DOA weighting and Truck-Factor-Detachment-Departure detection are reused verbatim, and its published population-level TFDD incidence (16.3\\%) and founder-only-TFDD survival rate (40.6\\%) are the external baseline this paper's rigor-gap evaluation tests our own corpora against (Section~\\ref{sec:artifact}).\n\n\\textbf{Data-source landscape.} GH Archive exposes GitHub's public event stream (15+ event types) with no token required, but its \\texttt{PushEvent} payload carries only commit SHA/author/message pointers -- never file lists or diffs \\citep{gharchive,github_events_api,gharchive_payload} -- so it can supply a repository-selection frame but not the commit-level content this study needs. World of Code holds full commit/blob/file/author cross-referencing at the right granularity \\citep{worldofcode,woc_identity_disambiguation} but is gated behind an SSH-registration approval process \\citep{woc_hack_tutorial}, and its self-serve Zenodo derivative covers only bot commits \\citep{botcommit_mapping}. GHTorrent, an earlier commit-mining service, is confirmed dead: its domain now redirects to an unrelated site and its BigQuery mirror has been stale since 2019 \\citep{ghtorrent_github,ghtorrent_downloads,hoffa_bigquery}. Libraries.io's Zenodo dump is live and gives repository-selection metadata at scale but carries no commit-level history \\citep{librariesio_dump}. We concluded that a repository-selection frame independent of present-day liveness (built from historical creation/push-date search, Section~\\ref{sec:corpus}) combined with a direct, unauthenticated \\texttt{git clone} of each selected repository's full history is the only path that is simultaneously live, token-cheap, and free of the liveness conditioning this paper's Section~\\ref{sec:results} diagnoses.\n\n\\section{Method: DOA/TFDD Pipeline and the Authority-Diffusion Covariate}\n\\label{sec:method}\n\nWe reimplement Avelino et al.'s Degree-of-Authorship (DOA) weighting over per-file commit history to identify, for each repository, the point at which a single ``founder'' author accounts for the plurality of authorship (a Truck-Factor-Detachment-Departure, TFDD, event: the date the founder's authorship share falls below the threshold that would make their departure survivable without loss of institutional knowledge). A TFDD event is classed \\emph{founder-only} when the departing author is the repository's original committer, distinguishing genuine founder succession from a later core contributor's departure.\n\nFor every founder-only TFDD event, we compute two families of covariates purely from commits dated \\textbf{before} the event, to avoid any post-departure leakage:\n\n\\begin{itemize}\n  \\item \\textbf{At-TFDD snapshot covariates} (Avelino et al.'s original feature set): number of active developers, total commits, and total files at the moment of TFDD.\n  \\item \\textbf{Pre-departure authority-diffusion covariates} (this paper's addition): the founder's commit-share in the 6-12 month window immediately before TFDD, and the count of distinct non-founder contributors who already held DOA-recognized file ownership in that same window (\\texttt{n\\_diffuse\\_owners\\_pre}). A single scalar \\texttt{diffusion\\_score} combines the two.\n\\end{itemize}\n\nThe outcome is 18-month post-TFDD survival, labeled from subsequent commit activity (\\texttt{survived\\_binary}), with three planned analyses: (1) a nearest-neighbor matched-pairs comparison of high- versus low-diffusion repositories controlling for the snapshot covariates, (2) BH-corrected logistic regression (binary survival) and ordinal regression (a graded survival label) with diffusion score as the covariate of interest, and (3) a window-shuffle placebo check that repeatedly reassigns which pre-TFDD window is treated as ``pre-departure'' to establish whether the observed diffusion-survival association could arise by chance.\n\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Sample starvation at 3,427 repositories}\n\\label{sec:starvation}\n\nRunning the pipeline on a 3,427-repository corpus sampled by current GitHub popularity/activity produced only 6 founder-only TFDD events. The error breakdown for the remaining 3,421 repositories was: 3,409 had no minable commit history at all under the mining budget used, 4 had a TFDD event that was not founder-only, and 2 were right-censored (no 18-month post-TFDD window had yet elapsed). At n=6, every planned statistical test failed outright: the matched-pairs comparison found zero eligible pairs even under relaxed matching, and both the logistic and ordinal regressions reported \\texttt{insufficient\\_n}.\n\n\\begin{figure}[!htbp]\n  \\centering\n  \\includegraphics[width=0.92\\textwidth,keepaspectratio]{figures/fig2_v0.pdf}\n  \\caption{Funnel of the 3,427-repository popularity-sampled corpus through the DOA/TFDD pipeline. The overwhelming majority (3,409) were dropped for having no minable commit history; only 6 repositories produced a usable founder-only TFDD event, too few for any of the three planned statistical tests.}\n  \\label{fig:fig2}\n\\end{figure}\n\n\\subsection{The null is a sampling artifact, not evidence of no effect}\n\\label{sec:artifact}\n\nA dedicated rigor-gap evaluation re-examined the 6-event corpus against Avelino et al.'s own published population statistics using Wilson 95\\% confidence intervals and two-proportion z-tests. Two results indicate the corpus is not a fair sample of the population Avelino et al. characterized:\n\n\\begin{itemize}\n  \\item \\textbf{TFDD incidence.} 73.3\\% of this corpus's repositories (11 of 15 candidates carried through to the full table) exhibit any TFDD event, versus 16.3\\% in Avelino et al.'s published population -- a two-proportion z=5.89, p=3.8e-9.\n  \\item \\textbf{Founder-only-TFDD survival.} 100\\% (5 of 5) of this corpus's founder-only-TFDD repositories survived 18 months post-departure, versus 40.6\\% in Avelino et al.'s population (Wilson 95\\% CI [0.606, 0.710] for their 66\\% TF=1 baseline versus this corpus's 45.5\\% TF=1 fraction, CI [0.213, 0.720]) -- z=2.67, p=0.0075.\n\\end{itemize}\n\nBoth deviations point the same direction: a corpus selected for present-day popularity over-represents repositories that already survived whatever ownership transition they went through, which is exactly the confound the pre-departure authority-diffusion hypothesis needs an unbiased corpus to rule out.\n\n\\begin{figure}[!htbp]\n  \\centering\n  \\includegraphics[width=0.92\\textwidth,keepaspectratio]{figures/fig3_v0.pdf}\n  \\caption{Rigor-gap evaluation of the popularity-sampled corpus against Avelino et al.'s published population baseline: TFDD incidence and founder-only-TFDD survival rate both diverge sharply and significantly in the direction consistent with survivorship conditioning.}\n  \\label{fig:fig3}\n\\end{figure}\n\nSeparately, the evaluation audited the placebo check's own implementation and found a previously undocumented \\textbf{20-draw-per-repository hard cap} -- the code path never reaches the ``500 iterations'' figure the original summary cited, because it caps each repository's contribution to the placebo distribution at 20 draws regardless of the requested budget. Re-running the placebo check at three budgets (10, 60, and 2,000 requested draws) produced an identical qualitative conclusion at all three, which is not evidence of robustness: at the 20-draw hard cap, the theoretical floor on the smallest detectable effect is 4.8\\%, and at the (never-reached) 500-draw figure the floor would be 0.2\\% -- meaning the check is structurally incapable of resolving an effect at n=6 regardless of how large the requested budget is set. The evaluation additionally spot-checked 3 of the corpus's 15 repositories against their raw source records and found all three aliases consistent (no full-corpus audit was run; 80\\% of the corpus remains unchecked by this pass).\n\n\\subsection{What we did not test}\n\nNo expanded or non-liveness-conditioned corpus existed among this round's dependencies to run head-to-head against the population baseline, so the claim that the null in Section~\\ref{sec:starvation} is a design flaw rather than a genuine power problem rests on the structural argument and evidence in Section~\\ref{sec:artifact}, not on a second frame producing more TFDD events. Section~\\ref{sec:corpus} supplies that second frame as this paper's concrete, falsifiable next step: if the pre-departure authority-diffusion hypothesis holds, a non-liveness-conditioned corpus should yield both a TFDD incidence closer to Avelino et al.'s 16.3\\% population figure and a founder-only survival rate closer to their 40.6\\%, rather than reproducing this section's 73.3\\%/100\\% figures.\n\n\\section{A Liveness-Non-Conditioned Corpus}\n\\label{sec:corpus}\n\nTo remove the conditioning identified in Section~\\ref{sec:artifact}, we built a second 67-repository corpus using GitHub's Search API \\texttt{created:}/\\texttt{pushed:} date qualifiers to sample purely on \\textbf{historical} creation and push-date windows (2011-2015) across eight languages, applying \\textbf{no filter on present-day archived, starred, or maintained status}. Of 450 candidates screened, 383 (85\\%) were rejected -- mostly for too few commits or too short a history to fit a pre-departure trajectory -- leaving 67 accepted repositories. Of those, 48 (72\\%) have had no commit in at least two years as of build time (our non-surviving proxy) and 7 are archived by GitHub itself, meaning non-surviving projects are represented in this corpus for the first time at a scale the original 3,427-repository frame never produced (Section~\\ref{sec:starvation}: only 2 right-censored, 0 confirmed non-surviving, among 6 founder-only TFDD events).\n\n\\begin{figure}[!htbp]\n  \\centering\n  \\includegraphics[width=0.92\\textwidth,keepaspectratio]{figures/fig4_v0.pdf}\n  \\caption{Composition of the 67-repository liveness-non-conditioned corpus: screening outcomes for the 450 historically-sampled candidates, and the survival-label breakdown of the 67 accepted repositories.}\n  \\label{fig:fig4}\n\\end{figure}\n\nEach repository's record standardizes to one example carrying only pre-departure-observable input features (computed strictly before the founder's last commit, to avoid the leakage the original pipeline already guards against in Section~\\ref{sec:method}) and one of three survival labels: \\texttt{survived}, \\texttt{non\\_surviving}, or \\texttt{unknown\\_insufficient\\_post\\_departure\\_window} for repositories without enough elapsed history to call a label at all. This corpus is released as the direct input to Section~\\ref{sec:method}'s pipeline for the next round of this study; running it end to end and reporting the resulting TFDD incidence and founder-only survival rate against Avelino et al.'s population baseline is the falsifiable prediction stated in Section~\\ref{sec:results}.3.\n\n\\section{Discussion}\n\n\\textbf{The headline finding of this paper is methodological.} A popularity-sampled GitHub corpus produced too few founder-only TFDD events to test the pre-departure authority-diffusion hypothesis (n=6), and the rigor-gap evaluation in Section~\\ref{sec:artifact} shows this was not bad luck: the corpus's TFDD incidence and founder-only survival rate both differ from Avelino et al.'s population figures in the direction consistent with survivorship conditioning, and the placebo check that appeared to certify the pipeline's null result was, on inspection, structurally incapable of detecting an effect at any of the budgets it was run at. We consider this worth reporting on its own terms rather than smoothing over: an automated pipeline that runs to completion and reports a stable null across three simulation budgets looks, from the outside, like a well-powered negative result. Section~\\ref{sec:artifact} shows it is not, and the distinction matters for anyone building on TFDD-style pipelines with any GitHub sample drawn by present-day popularity, stars, or trending status.\n\n\\textbf{Limitations.} The spot-check audit of the original corpus's alias resolution covered only 3 of 15 repositories (80\\% unchecked). The new liveness-non-conditioned corpus (Section~\\ref{sec:corpus}) has not yet been run through the DOA/TFDD pipeline of Section~\\ref{sec:method}, so we cannot yet report whether it in fact yields more founder-only TFDD events or a less skewed incidence/survival rate than the original frame -- that comparison is the explicit next step, not a result claimed here. The non-surviving proxy (no commit in $\\geq$2 years) is a coarse label; a repository can be dormant and later revived, and the corpus's \\texttt{unknown\\_insufficient\\_post\\_departure\\_window} label exists precisely to avoid forcing a survival call where the post-departure window is too short. Finally, both corpora are drawn from GitHub only; repositories hosted elsewhere or migrated away from GitHub after founder departure are systematically invisible to any GitHub-only sampling frame, including ours.\n\n\\section{Conclusion}\n\nWe set out to test whether authority diffusing away from a project's founder before their departure predicts survival beyond existing snapshot diversity metrics, and found instead that the obvious way to build a GitHub corpus for this question -- sampling by current popularity -- silently conditions the sample on survival, starving the founder-only-TFDD event count down to 6 and rendering every planned statistical test uninformative. We quantified that conditioning against Avelino et al.'s own published population baseline (TFDD incidence 73.3\\% vs. 16.3\\%, z=5.89, p=3.8e-9; founder-only survival 100\\% vs. 40.6\\%, z=2.67, p=0.0075) and showed the pipeline's placebo check could not have detected an effect at n=6 regardless of its requested simulation budget, due to an undocumented 20-draw-per-repository cap. We release a 67-repository corpus sampled without any liveness conditioning, 72\\% of which are non-surviving by a two-year-inactivity proxy, as the concrete resource needed to run this hypothesis test properly.\n\nFuture work: (1) run the Section~\\ref{sec:method} pipeline against the Section~\\ref{sec:corpus} corpus and report whether its TFDD incidence and founder-only survival rate move toward Avelino et al.'s population figures, as predicted in Section~\\ref{sec:results}.3; (2) complete the full-corpus alias audit begun in Section~\\ref{sec:artifact}, extending the 3-of-15 spot-check to all repositories in both corpora; (3) locate or derive the Apache Project Maturity Model's community-diversity-specific criteria codes, left unresolved in Section~\\ref{sec:related}, to add a second governance-gate baseline alongside Avelino et al.'s population statistics.\n\n\\bibliographystyle{plainnat}\n\\bibliography{references}\n\n\\end{document}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [32] TOOL CALL — Edit · 2026-08-21 16:24:15 UTC

```
File: /ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_4_assemble_paper/paper/workspace/paper.tex
OLD: \subsection{What we did not test}
NEW: \subsection{What we did not test}
\label{sec:whatnot}
```

### [33] TOOL RESULT — Edit · 2026-08-21 16:24:15 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_4_assemble_paper/paper/workspace/paper.tex", "oldString": "\\subsection{What we did not test}", "newString": "\\subsection{What we did not test}\n\\label{sec:whatnot}", "originalFile": null, "structuredPatch": [{"oldStart": 115, "oldLines": 6, "newStart": 115, "newLines": 7, "lines": [" Separately, the evaluation audited the placebo check's own implementation and found a previously undocumented \\textbf{20-draw-per-repository hard cap} -- the code path never reaches the ``500 iterations'' figure the original summary cited, because it caps each repository's contribution to the placebo distribution at 20 draws regardless of the requested budget. Re-running the placebo check at three budgets (10, 60, and 2,000 requested draws) produced an identical qualitative conclusion at all three, which is not evidence of robustness: at the 20-draw hard cap, the theoretical floor on the smallest detectable effect is 4.8\\%, and at the (never-reached) 500-draw figure the floor would be 0.2\\% -- meaning the check is structurally incapable of resolving an effect at n=6 regardless of how large the requested budget is set. The evaluation additionally spot-checked 3 of the corpus's 15 repositories against their raw source records and found all three aliases consistent (no full-corpus audit was run; 80\\% of the corpus remains unchecked by this pass).", " ", " \\subsection{What we did not test}", "+\\label{sec:whatnot}", " ", " No expanded or non-liveness-conditioned corpus existed among this round's dependencies to run head-to-head against the population baseline, so the claim that the null in Section~\\ref{sec:starvation} is a design flaw rather than a genuine power problem rests on the structural argument and evidence in Section~\\ref{sec:artifact}, not on a second frame producing more TFDD events. Section~\\ref{sec:corpus} supplies that second frame as this paper's concrete, falsifiable next step: if the pre-departure authority-diffusion hypothesis holds, a non-liveness-conditioned corpus should yield both a TFDD incidence closer to Avelino et al.'s 16.3\\% population figure and a founder-only survival rate closer to their 40.6\\%, rather than reproducing this section's 73.3\\%/100\\% figures.", " "]}], "userModified": false, "replaceAll": false}
```

### [34] TOOL CALL — Edit · 2026-08-21 16:24:19 UTC

```
File: /ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_4_assemble_paper/paper/workspace/paper.tex
OLD: is the falsifiable prediction stated in Section~\ref{sec:results}.3.
NEW: is the falsifiable prediction stated in Section~\ref{sec:whatnot}.
```

### [35] TOOL RESULT — Edit · 2026-08-21 16:24:19 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_4_assemble_paper/paper/workspace/paper.tex", "oldString": "is the falsifiable prediction stated in Section~\\ref{sec:results}.3.", "newString": "is the falsifiable prediction stated in Section~\\ref{sec:whatnot}.", "originalFile": null, "structuredPatch": [{"oldStart": 131, "oldLines": 7, "newStart": 131, "newLines": 7, "lines": ["   \\label{fig:fig4}", " \\end{figure}", " ", "-Each repository's record standardizes to one example carrying only pre-departure-observable input features (computed strictly before the founder's last commit, to avoid the leakage the original pipeline already guards against in Section~\\ref{sec:method}) and one of three survival labels: \\texttt{survived}, \\texttt{non\\_surviving}, or \\texttt{unknown\\_insufficient\\_post\\_departure\\_window} for repositories without enough elapsed history to call a label at all. This corpus is released as the direct input to Section~\\ref{sec:method}'s pipeline for the next round of this study; running it end to end and reporting the resulting TFDD incidence and founder-only survival rate against Avelino et al.'s population baseline is the falsifiable prediction stated in Section~\\ref{sec:results}.3.", "+Each repository's record standardizes to one example carrying only pre-departure-observable input features (computed strictly before the founder's last commit, to avoid the leakage the original pipeline already guards against in Section~\\ref{sec:method}) and one of three survival labels: \\texttt{survived}, \\texttt{non\\_surviving}, or \\texttt{unknown\\_insufficient\\_post\\_departure\\_window} for repositories without enough elapsed history to call a label at all. This corpus is released as the direct input to Section~\\ref{sec:method}'s pipeline for the next round of this study; running it end to end and reporting the resulting TFDD incidence and founder-only survival rate against Avelino et al.'s population baseline is the falsifiable prediction stated in Section~\\ref{sec:whatnot}.", " ", " \\section{Discussion}", " "]}], "userModified": false, "replaceAll": false}
```

### [36] TOOL CALL — Edit · 2026-08-21 16:24:23 UTC

```
File: /ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_4_assemble_paper/paper/workspace/paper.tex
OLD: Future work: (1) run the Section~\ref{sec:method} pipeline against the Section~\ref{sec:corpus} corpus and report whether its TFDD incidence and founder-only survival rate move toward Avelino et al.'s population figures, as predicted in Section~\ref{sec:results}.3; (2)
NEW: Future work: (1) run the Section~\ref{sec:method} pipeline against the Section~\ref{sec:corpus} corpus and report whether its TFDD incidence and founder-only survival rate move toward Avelino et al.'s population figures, as predicted in Section~\ref{sec:whatnot}; (2)
```

### [37] TOOL RESULT — Edit · 2026-08-21 16:24:23 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_4_assemble_paper/paper/workspace/paper.tex", "oldString": "Future work: (1) run the Section~\\ref{sec:method} pipeline against the Section~\\ref{sec:corpus} corpus and report whether its TFDD incidence and founder-only survival rate move toward Avelino et al.'s population figures, as predicted in Section~\\ref{sec:results}.3; (2)", "newString": "Future work: (1) run the Section~\\ref{sec:method} pipeline against the Section~\\ref{sec:corpus} corpus and report whether its TFDD incidence and founder-only survival rate move toward Avelino et al.'s population figures, as predicted in Section~\\ref{sec:whatnot}; (2)", "originalFile": null, "structuredPatch": [{"oldStart": 143, "oldLines": 7, "newStart": 143, "newLines": 7, "lines": [" ", " We set out to test whether authority diffusing away from a project's founder before their departure predicts survival beyond existing snapshot diversity metrics, and found instead that the obvious way to build a GitHub corpus for this question -- sampling by current popularity -- silently conditions the sample on survival, starving the founder-only-TFDD event count down to 6 and rendering every planned statistical test uninformative. We quantified that conditioning against Avelino et al.'s own published population baseline (TFDD incidence 73.3\\% vs. 16.3\\%, z=5.89, p=3.8e-9; founder-only survival 100\\% vs. 40.6\\%, z=2.67, p=0.0075) and showed the pipeline's placebo check could not have detected an effect at n=6 regardless of its requested simulation budget, due to an undocumented 20-draw-per-repository cap. We release a 67-repository corpus sampled without any liveness conditioning, 72\\% of which are non-surviving by a two-year-inactivity proxy, as the concrete resource needed to run this hypothesis test properly.", " ", "-Future work: (1) run the Section~\\ref{sec:method} pipeline against the Section~\\ref{sec:corpus} corpus and report whether its TFDD incidence and founder-only survival rate move toward Avelino et al.'s population figures, as predicted in Section~\\ref{sec:results}.3; (2) complete the full-corpus alias audit begun in Section~\\ref{sec:artifact}, extending the 3-of-15 spot-check to all repositories in both corpora; (3) locate or derive the Apache Project Maturity Model's community-diversity-specific criteria codes, left unresolved in Section~\\ref{sec:related}, to add a second governance-gate baseline alongside Avelino et al.'s population statistics.", "+Future work: (1) run the Section~\\ref{sec:method} pipeline against the Section~\\ref{sec:corpus} corpus and report whether its TFDD incidence and founder-only survival rate move toward Avelino et al.'s population figures, as predicted in Section~\\ref{sec:whatnot}; (2) complete the full-corpus alias audit begun in Section~\\ref{sec:artifact}, extending the 3-of-15 spot-check to all repositories in both corpora; (3) locate or derive the Apache Project Maturity Model's community-diversity-specific criteria codes, left unresolved in Section~\\ref{sec:related}, to add a second governance-gate baseline alongside Avelino et al.'s population statistics.", " ", " \\bibliographystyle{plainnat}", " \\bibliography{references}"]}], "userModified": false, "replaceAll": false}
```

### [38] ASSISTANT · 2026-08-21 16:24:27 UTC

```
Now compile.
```

### [39] TOOL CALL — Bash · 2026-08-21 16:24:27 UTC

```
pdflatex -interaction=nonstopmode paper.tex > /tmp/p1.log 2>&1; tail -40 /tmp/p1.log
```

### [40] TOOL RESULT — Bash · 2026-08-21 16:24:37 UTC

```
{"stdout": "[96] [126] [127] [128] [129] [130] [131] [132] [133] [134] [135] [136] [137]\n[138] [139] [140] [141] [142] [143] [144] [145] [146] [147] [148] [149]\n[150] [151] [152] [153] [154] [155] [156] [157] [158] [159] [160] [161]\n[162] [163] [164] [165] [166] [167] [168] [169] [171] [172] [173] [174]\n[175] [177] [176] [180] [181] [182] [183] [184] [187] [191] [214] [246])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txromod.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrsuper.mf\n Ok [185] [178] [179] [170] [186])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrfract.mf\n Ok [188] [189] [190]) ) ) )\n(some charht values had to be adjusted by as much as 0.06952pt)\nFont metrics written on tcrm1095.tfm.\nOutput written on tcrm1095.600gf (128 characters, 25592 bytes).\nTranscript written on tcrm1095.log.\nmktexpk: /root/.texlive2022/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk: successfully generated.\n\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) </root/.texlive2022/texmf-\nvar/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk></usr/share/texlive/texmf-dist/f\nonts/type1/public/amsfonts/cm/cmbx10.pfb></usr/share/texlive/texmf-dist/fonts/t\nype1/public/amsfonts/cm/cmbx12.pfb></usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmr10.pfb></usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmr17.pfb></usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmsy10.pfb></usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nti10.pfb></usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.p\nfb>\nOutput written on paper.pdf (10 pages, 1408136 bytes).\nTranscript written on paper.log.", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [41] ASSISTANT · 2026-08-21 16:24:39 UTC

```
Good, compiled (fonts warning expected, undefined refs are citations pending bibtex).
```

### [42] TOOL CALL — Bash · 2026-08-21 16:24:39 UTC

```
bibtex paper > /tmp/b1.log 2>&1; tail -30 /tmp/b1.log
```

### [43] TOOL RESULT — Bash · 2026-08-21 16:24:39 UTC

```
{"stdout": "/bin/bash: line 1: bibtex: command not found", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [44] TOOL CALL — Bash · 2026-08-21 16:24:43 UTC

```
which bibtex8 texify kpsewhich; find / -iname "bibtex*" -type f 2>/dev/null | head; apt list --installed 2>/dev/null | grep -i tex | head -20
```

### [45] TOOL RESULT — Bash · 2026-08-21 16:26:40 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "b3qah3sqf", "timedOutAfterMs": 120000}
```

### [46] TOOL CALL — Bash · 2026-08-21 16:26:42 UTC

```
apt-get install -y texlive-binaries bibtex 2>&1 | tail -20 || which bibtex
```

### [47] TOOL RESULT — Bash · 2026-08-21 16:26:42 UTC

```
{"stdout": "Reading package lists...\nBuilding dependency tree...\nReading state information...\nPackage texlive-binaries is not available, but is referred to by another package.\nThis may mean that the package is missing, has been obsoleted, or\nis only available from another source\n\nE: Package 'texlive-binaries' has no installation candidate\nE: Unable to locate package bibtex", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [48] TOOL CALL — Bash · 2026-08-21 16:26:44 UTC

```
dpkg -L texlive-base 2>/dev/null | grep -i bib; find /usr -iname "*bibtex*" 2>/dev/null; ls /usr/bin | grep -i tex
```

### [49] TOOL RESULT — Bash · 2026-08-21 16:26:44 UTC

```
{"stdout": "/usr/bin/bibtex.original\n/usr/bin/bibtex8\n/usr/bin/bibtexu\n/usr/bin/pbibtex\n/usr/bin/upbibtex\n/usr/local/lib/python3.12/site-packages/pygments/lexers/bibtex.py\n/usr/share/texlive/texmf-dist/bibtex\n/usr/share/texlive/texmf-dist/bibtex/bst/dlfltxb/dlfltxbbibtex.bst\n/usr/share/texlive/texmf-dist/tex/generic/bibtex\namstex\nbibtex.original\nbibtex8\nbibtexu\ndetex\ndh_installtex\ndvilualatex\ndvilualatex-dev\ndviluatex\neptex\netex\neuptex\nexceltex\nfig4latex\nhitex\ninitex\nlatex\nlatex-dev\nlatex-wordcount\nlatexmk\nluahbtex\nluajithbtex\nluajittex\nlualatex\nlualatex-dev\nluatex\nmd5sum.textutils\nmktexfmt\nmktexlsr\nmktexmf\nmktexpk\nmktextfm\npbibtex\npdfannotextractor\npdfetex\npdflatex\npdflatex-dev\npdftex\npdftotext\nperltex\npod2text\nptex\npygettext3\npygettext3.11\npygmentex\nsimpdftex\nsynctex\ntex\ntex2aspc\ntex4ht\ntexdoc\ntexdoctk\ntexhash\ntexlua\ntexluac\ntexluajit\ntexluajitc\ntpic2pdftex\nupbibtex\nuptex\nxetex", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [50] ASSISTANT · 2026-08-21 16:26:48 UTC

```
`bibtex.original` exists — likely a shell wrapper is missing/broken but the binary is fine.
```

### [51] TOOL CALL — Bash · 2026-08-21 16:26:48 UTC

```
bibtex.original paper > /tmp/b1.log 2>&1; tail -30 /tmp/b1.log
```

### [52] TOOL RESULT — Bash · 2026-08-21 16:26:48 UTC

```
{"stdout": "This is BibTeX, Version 0.99d (TeX Live 2022/Debian)\nThe top-level auxiliary file: paper.aux\nThe style file: plainnat.bst\nDatabase file #1: references.bib\nWarning--to sort, need author or key in gharchive\nWarning--to sort, need author or key in gharchive_payload\nWarning--to sort, need author or key in worldofcode\nWarning--to sort, need author or key in woc_identity_disambiguation\nWarning--to sort, need author or key in woc_hack_tutorial\nWarning--to sort, need author or key in botcommit_mapping\nWarning--to sort, need author or key in ghtorrent_github\nWarning--to sort, need author or key in ghtorrent_downloads\nWarning--to sort, need author or key in librariesio_dump\nWarning--empty year in botcommit_mapping\nWarning--empty year in gharchive\nWarning--empty year in gharchive_payload\nWarning--empty year in ghtorrent_downloads\nWarning--empty year in ghtorrent_github\nWarning--empty year in librariesio_dump\nWarning--empty year in woc_hack_tutorial\nWarning--empty year in worldofcode\nWarning--empty year in apache_incubator_graduation\nWarning--empty year in apache_maturity_model\nWarning--empty year in chaoss_absence_factor\nWarning--empty year in chaoss_elephant_factor\nWarning--empty year in github_events_api\nWarning--empty year in hoffa_bigquery\n(There were 23 warnings)", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [53] ASSISTANT · 2026-08-21 16:26:50 UTC

```
Fine, just warnings. Now use bibtex.original for the rest and rerun pdflatex twice.
```

### [54] TOOL CALL — Bash · 2026-08-21 16:26:50 UTC

```
pdflatex -interaction=nonstopmode paper.tex > /tmp/p2.log 2>&1; pdflatex -interaction=nonstopmode paper.tex > /tmp/p3.log 2>&1; grep -i -E "undefined|error|missing" /tmp/p3.log | head -30; ls -la paper.pdf
```

### [55] TOOL RESULT — Bash · 2026-08-21 16:27:23 UTC

```
{"stdout": "-rw-r--r-- 1 root root 1422711 Aug 21 16:27 paper.pdf", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [56] ASSISTANT · 2026-08-21 16:27:26 UTC

```
No undefined references remain. Paper compiled successfully with all 4 figures and bibliography.
```

### [57] TOOL CALL — Bash · 2026-08-21 16:27:26 UTC

```
grep -c "\\\\cite" paper.tex; pdftotext paper.pdf - 2>/dev/null | grep -c "\[?\]"; pdfinfo paper.pdf | grep Pages
```

### [58] TOOL RESULT — Bash · 2026-08-21 16:27:26 UTC

```
{"stdout": "7\n0\nPages:           11", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [59] ASSISTANT · 2026-08-21 16:27:27 UTC

```
Paper assembled successfully: `paper.tex`, `references.bib`, and `paper.pdf` (11 pages) with all 4 figures and citations resolved, no `[?]` markers. The assembly task is complete.
```

### [60] SYSTEM-USER prompt · 2026-08-21 16:27:30 UTC

```
<validation-feedback>
Attempt 1 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [61] TOOL CALL — Bash · 2026-08-21 16:27:36 UTC

```
find /ai-inventor/aii_data/runs/run_LYICROwXFVjo -iname ".terminal_claude_agent_struct_out.json" 2>/dev/null
```

### [62] TOOL RESULT — Bash · 2026-08-21 16:28:00 UTC

```
{"stdout": "/ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_2_gen_viz/gen_viz_4/.terminal_claude_agent_struct_out.json\n/ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_2_gen_viz/gen_viz_1/.terminal_claude_agent_struct_out.json\n/ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_I5KoOp16hub5/.terminal_claude_agent_struct_out.json\n/ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_2_gen_viz/gen_viz_3/.terminal_claude_agent_struct_out.json\n/ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_2_gen_viz/gen_viz_2/.terminal_claude_agent_struct_out.json\n/ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_JvYoV94jgkuB/.terminal_claude_agent_struct_out.json\n/ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_1/art_ZuMis522AEPF/.terminal_claude_agent_struct_out.json\n/ai-inventor/aii_data/runs/run_LYICROwXFVjo/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json\n/ai-inventor/aii_data/runs/run_LYICROwXFVjo/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/.terminal_claude_agent_struct_out.json\n/ai-inventor/aii_data/runs/run_LYICROwXFVjo/3_invention_loop/iter_2/review_paper/review_paper/.terminal_claude_agent_struct_out.json\n/ai-inventor/aii_data/runs/run_LYICROwXFVjo/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.terminal_claude_agent_struct_out.json\n/ai-inventor/aii_data/runs/run_LYICROwXFVjo/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/.terminal_claude_agent_struct_out.json\n/ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_zgnq2xDjA0ta/.terminal_claude_agent_struct_out.json\n/ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_3_gen_demo_art/notebook_workspaces/iter_2/art_ajD7unO0iQl3/.terminal_claude_agent_struct_out.json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [63] TOOL CALL — Bash · 2026-08-21 16:28:07 UTC

```
find /ai-inventor -iname "*.json" -path "*assemble_paper*" 2>/dev/null | grep -v run_LYICROwXFVjo; find /ai-inventor -iname "*assemble*paper*schema*" 2>/dev/null; find /ai-inventor -iname "*schema*" 2>/dev/null | grep -i paper
```

### [64] TOOL RESULT — Bash · 2026-08-21 16:30:03 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "bboiu19ko", "timedOutAfterMs": 120000}
```

### [65] TOOL CALL — Bash · 2026-08-21 16:30:05 UTC

```
grep -rl "assemble_paper" /ai-inventor --include="*.py" 2>/dev/null | grep -v aii_data | head -20
```

### [66] TOOL RESULT — Bash · 2026-08-21 16:30:05 UTC

```
{"stdout": "/ai-inventor/aii_pipeline/src/aii_pipeline/steps/_4_gen_paper_repo/_4_gen_full_paper.py\n/ai-inventor/scripts/debug/redeploy_finished_run.py", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [67] TOOL CALL — Read · 2026-08-21 16:30:10 UTC

```
/ai-inventor/aii_pipeline/src/aii_pipeline/steps/_4_gen_paper_repo/_4_gen_full_paper.py
```

### [68] TOOL RESULT — Read · 2026-08-21 16:30:10 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_pipeline/src/aii_pipeline/steps/_4_gen_paper_repo/_4_gen_full_paper.py", "content": "\"\"\"gen_full_paper — step 4 in gen_paper_repo. Generate LaTeX paper and PDF.\n\nUses Claude Agent to:\n1. Create paper.tex from paper text content\n2. Insert figures at appropriate locations\n3. Compile to PDF using pdflatex\n\nPushing the paper to GitHub is handled later by step 5 (deploy_gh).\n\"\"\"\n\nimport json\nimport re\nimport shutil\nfrom datetime import UTC, datetime\nfrom pathlib import Path\nfrom typing import Literal\n\nfrom aii_lib.agent_backend import (\n    agent_class_for,\n    build_options,\n    end_task,\n    setup_workspace,\n    start_task,\n)\nfrom aii_lib.run import emit\nfrom pydantic import BaseModel\n\nfrom aii_pipeline.prompts.steps._3_invention_loop._4_gen_paper_text.out_schema import (\n    PaperText,\n)\nfrom aii_pipeline.prompts.steps._4_gen_paper_repo._2_gen_viz.out_schema import Figure\nfrom aii_pipeline.prompts.steps._4_gen_paper_repo._4_gen_full_paper.out_schema import (\n    FullPaper,\n    GenPaperRepoOut,\n)\nfrom aii_pipeline.prompts.steps._4_gen_paper_repo._4_gen_full_paper.s_prompt import (\n    get as get_latex_system_prompt,\n)\nfrom aii_pipeline.prompts.steps._4_gen_paper_repo._4_gen_full_paper.u_prompt import (\n    get as get_latex_user_prompt,\n)\nfrom aii_pipeline.prompts.steps._4_gen_paper_repo._4_gen_full_paper.u_prompt import (\n    get_expected_out_files,\n    get_figures_folder,\n    get_latex_filename,\n    get_pdf_filename,\n)\nfrom aii_pipeline.utils import PipelineConfig, rel_path\n\nfrom .utils.fork_workspace import resolve_upstream_path\n\n\ndef _verify_figures_in_tex(\n    tex_path: Path,\n    figures: list[Figure],\n) -> list[Figure]:\n    r\"\"\"Verify all figures are referenced in paper.tex via \\\\includegraphics.\n\n    Checks that each figure's filename appears in an \\\\includegraphics command.\n    Returns list of missing figures (empty = all good).\n    \"\"\"\n    if not tex_path.exists():\n        return figures  # All missing if no tex file\n\n    tex_content = tex_path.read_text(encoding=\"utf-8\")\n\n    # Extract all filenames from \\includegraphics{...} commands\n    # Handles optional arguments like \\includegraphics[width=...]{path}\n    includegraphics_paths = re.findall(r\"\\\\includegraphics(?:\\[.*?\\])?\\{([^}]+)\\}\", tex_content)\n    # Normalize: extract just filenames for comparison\n    included_filenames = {Path(p).name for p in includegraphics_paths}\n\n    missing = []\n    for fig in figures:\n        if not fig.figure_path:\n            continue\n        fig_filename = Path(fig.figure_path).name\n        if fig_filename not in included_filenames:\n            missing.append(fig)\n\n    # Log results\n    total = len([f for f in figures if f.figure_path])\n    found = total - len(missing)\n    emit.status_private_info(\n        f\"Figure verification: {found}/{total} figures found in paper.tex \"\n        f\"({len(includegraphics_paths)} \\\\includegraphics total)\",\n    )\n\n    for fig in missing:\n        emit.status_public_warning(\n            f\"Missing figure in paper.tex: {fig.id} ({Path(fig.figure_path).name}) — '{fig.title}'\",\n        )\n\n    return missing\n\n\ndef _build_figure_fix_prompt(missing: list[Figure]) -> str:\n    \"\"\"Build a prompt telling the agent to insert missing figures.\"\"\"\n    fig_list = \"\\n\".join(\n        f'- {fig.id}: figures/{Path(fig.figure_path).name} — \"{fig.title}\" (caption: \"{fig.caption}\")'\n        for fig in missing\n    )\n    return (\n        f\"FIGURE VERIFICATION FAILED: {len(missing)} figure(s) are missing from paper.tex.\\n\\n\"\n        f\"The following figures exist in the figures/ directory but have NO \\\\includegraphics in paper.tex:\\n\"\n        f\"{fig_list}\\n\\n\"\n        f\"You MUST:\\n\"\n        f\"1. Insert each missing figure using \\\\begin{{figure}}[!htbp] ... \"\n        f\"\\\\includegraphics{{figures/<its own filename, extension included: \"\n        f\".pdf for data figures, .jpg for concept figures>}} ... \\\\end{{figure}}\\n\"\n        f\"2. Place them at appropriate locations in the paper (near where they are discussed, or at the end of the relevant section)\\n\"\n        f\"3. Use the caption provided above for each figure\\n\"\n        f\"4. Recompile the PDF with pdflatex/latexmk\\n\"\n        f\"5. Verify the fix: grep -c 'includegraphics' paper.tex\\n\"\n    )\n\n\nasync def generate_paper_with_agent(\n    config: PipelineConfig,\n    paper: PaperText,\n    figures: list[Figure],\n    workspace_dir: Path,\n    parent_module_id: str,\n) -> tuple[Path | None, Path | None]:\n    \"\"\"Generate LaTeX paper and compile to PDF using Claude Agent.\"\"\"\n    task_name = \"gen_full_paper\"\n\n    setup_workspace(workspace_dir)\n    task_id = start_task(task_name, parent_module_id)\n\n    # Hoisted above the try: the TimeoutError handler below reads\n    # ``agent_cfg.seq_prompt_timeout`` — assigned mid-try, an early timeout\n    # would NameError and mask the real failure.\n    agent_cfg = config.gen_paper_repo.gen_full_paper.agent\n\n    try:\n        # Copy figures to workspace\n        figures_dir = workspace_dir / get_figures_folder()\n        figures_dir.mkdir(parents=True, exist_ok=True)\n\n        for fig in figures:\n            if fig.figure_path:\n                # Fork-aware: when a fork skipped gen_viz the figures live\n                # under the parent run dir — re-anchor before copying.\n                src = resolve_upstream_path(fig.figure_path)\n                if src is not None:\n                    dst = figures_dir / src.name\n                    shutil.copy(src, dst)\n\n        # Create copies with workspace-relative paths for the prompt.\n        # Do NOT mutate originals — they're shared with figure_pool, result.json, and push.\n        prompt_figures = [\n            fig.model_copy(\n                update={\"figure_path\": f\"{get_figures_folder()}/{Path(fig.figure_path).name}\"}\n            )\n            if fig.figure_path\n            else fig.model_copy()\n            for fig in figures\n        ]\n\n        # Post-validate: check figures are included in paper.tex\n        figures_with_path = [f for f in prompt_figures if f.figure_path]\n\n        def _validate_tex_figures(structured_output):  # noqa: ARG001 — post-validate cb sig\n            tex_file = workspace_dir / get_latex_filename()\n            if not tex_file.exists() or not figures_with_path:\n                return True, None\n            missing = _verify_figures_in_tex(tex_file, prompt_figures)\n            if not missing:\n                return True, None\n            return False, _build_figure_fix_prompt(missing)\n\n        options = build_options(\n            agent_cfg,\n            workspace_dir,\n            task_id=task_id,\n            task_name=task_name,\n            system_prompt=get_latex_system_prompt(),\n            output_format=FullPaper.to_struct_output(),\n            expected_files_field=\"out_expected_files\",\n            post_validate=_validate_tex_figures,\n            post_validate_retries=2,\n        )\n\n        # Build prompt (GitHub push is handled by Python code, not agent)\n        prompt = get_latex_user_prompt(\n            paper=paper,\n            figures=prompt_figures,\n            workspace_path=str(workspace_dir),\n        )\n\n        emit.status_private_info(\"Starting LaTeX generation and compilation\")\n\n        # Run agent\n        agent = agent_class_for(options)(options)\n        result = await agent.run([prompt])\n\n        if result.failed:\n            err = result.error_message or \"unknown error\"\n            emit.status_public_error(f\"GEN_PAPER agent failed: {err}\")\n            end_task(task_id, task_name, reason=\"failure\", detail=f\"Agent failed: {err}\")\n            raise RuntimeError(f\"GEN_PAPER agent failed: {err}\")\n\n        # Check output files\n        tex_path = workspace_dir / get_latex_filename()\n        pdf_path = workspace_dir / get_pdf_filename()\n\n        if pdf_path.exists():\n            emit.status_public_success(f\"PDF generated: {tex_path.name}\")\n            end_task(task_id, task_name)\n            return tex_path, pdf_path\n\n        if tex_path.exists():\n            emit.status_public_warning(\"LaTeX created but PDF compilation failed\")\n            end_task(task_id, task_name, reason=\"partial\")\n            return tex_path, None\n\n        emit.status_public_error(\"LaTeX generation failed - no output files\")\n        end_task(task_id, task_name, reason=\"failure\", detail=\"No output files\")\n        raise RuntimeError(\"LaTeX generation produced no output files\")\n\n    except TimeoutError:\n        emit.status_public_error(\"GEN_PAPER agent timed out\")\n        end_task(task_id, task_name, reason=\"timeout\", detail=agent_cfg.seq_prompt_timeout)\n        raise\n\n    except Exception as e:\n        emit.status_public_error(f\"GEN_PAPER failed: {e}\")\n        end_task(task_id, task_name, reason=\"error\", detail=str(e))\n        raise\n\n\nclass GenFullPaperModule(BaseModel):\n    \"\"\"gen_full_paper substep — generate LaTeX + compile PDF.\n\n    Uses Claude Agent to generate LaTeX from the paper draft and\n    compile it to PDF. The push to GitHub happens in step 5\n    (``deploy_gh``).\n    \"\"\"\n\n    kind: Literal[\"gen_full_paper_module\"] = \"gen_full_paper_module\"\n    \"\"\"Per-subclass discriminator (see ``GenHypoModule.kind``).\"\"\"\n\n    name: Literal[\"gen_full_paper\"] = \"gen_full_paper\"\n\n    async def execute(\n        self,\n        *,\n        config: PipelineConfig,\n        paper: PaperText | None,\n        figures: list[Figure],\n        output_dir: Path | None = None,\n        repo_url: str | None = None,\n        parent_id: str,\n    ) -> GenPaperRepoOut:\n        \"\"\"Run the gen_full_paper step.\"\"\"\n        mid = emit.start_single_module(\n            name=\"gen_full_paper\",\n            parent_id=parent_id,\n        )\n\n        try:\n            if not output_dir:\n                output_dir = Path(\"./gen_paper_output\")\n\n            output_dir.mkdir(parents=True, exist_ok=True)\n            # Step-scoped output: 4_gen_paper_repo/_4_assemble_paper/paper/\n            step_dir = output_dir / \"_4_assemble_paper\"\n            step_dir.mkdir(parents=True, exist_ok=True)\n            paper_dir = step_dir / \"paper\"\n            paper_dir.mkdir(parents=True, exist_ok=True)\n\n            result = GenPaperRepoOut(\n                output_dir=str(output_dir),\n                repo_url=repo_url,\n                figures=figures,\n                # Always [] at step 4; deploy_gh (step 5) populates the\n                # durable result.gist_deployments after this step.\n                gist_deployments=[],\n                metadata={\n                    \"generated_at\": datetime.now(UTC).isoformat(),\n                    \"module\": \"gen_paper\",\n                },\n            )\n\n            if not paper:\n                emit.status_public_warning(\"No paper to process\")\n                return result\n\n            emit.status_private_info(f\"Paper: {paper.id}\")\n            emit.status_private_info(f\"Figures: {len(figures)}\")\n            if repo_url:\n                emit.status_private_info(f\"Repo: {repo_url}\")\n\n            if not paper.title:\n                raise ValueError(\"Paper has no title — cannot generate paper\")\n\n            # Generate paper with Claude Agent (GitHub push handled separately)\n            workspace_dir = paper_dir / \"workspace\"\n            tex_path, pdf_path = await generate_paper_with_agent(\n                config=config,\n                paper=paper,\n                figures=figures,\n                workspace_dir=workspace_dir,\n                parent_module_id=mid,\n            )\n\n            # Copy final outputs to paper_dir\n            final_tex = None\n            final_pdf = None\n\n            if tex_path and tex_path.exists():\n                final_tex = paper_dir / get_latex_filename()\n                shutil.copy(tex_path, final_tex)\n                emit.status_private_info(f\"LaTeX: {rel_path(final_tex)}\")\n\n            if pdf_path and pdf_path.exists():\n                final_pdf = paper_dir / get_pdf_filename()\n                shutil.copy(pdf_path, final_pdf)\n                emit.status_private_info(f\"PDF: {rel_path(final_pdf)}\")\n\n            # Copy references.bib if it exists\n            final_bib = None\n            bib_path = workspace_dir / \"references.bib\"\n            if bib_path.exists():\n                final_bib = paper_dir / \"references.bib\"\n                shutil.copy(bib_path, final_bib)\n                emit.status_private_info(f\"Bibliography: {rel_path(final_bib)}\")\n\n            # Copy figures to paper_dir straight from gen_viz's output dir —\n            # one flat pass, rather than re-deriving each name from\n            # ``figures``. Fork-aware for the same reason as the workspace\n            # copy above: when a fork skipped gen_viz, ``output_dir`` points\n            # at the FORK's re-rooted dir (``_reroot_output_dir``) which never\n            # materialised ``_2_gen_viz/``, so a bare path missed and the\n            # published ``paper_latex/`` shipped an EMPTY figures/ next to a\n            # paper.tex that \\includegraphics-es it.\n            figures_out = paper_dir / get_figures_folder()\n            figures_out.mkdir(parents=True, exist_ok=True)\n            gen_viz_figures_dir = resolve_upstream_path(output_dir / \"_2_gen_viz\" / \"figures\")\n            if gen_viz_figures_dir is not None:\n                # ``rglob``, not ``iterdir``: gen_viz files every figure one\n                # level down, under ``data_fig/`` or ``concept_fig/``\n                # (VIZ_SUBDIR_BY_TYPE). A flat scan yielded only those two\n                # directories, ``is_file()`` rejected both, and the shipped\n                # paper folder got an EMPTY figures/ next to a paper.tex that\n                # references it. The names are unique per figure, so they\n                # flatten into one folder here as LaTeX expects.\n                for fig_file in sorted(gen_viz_figures_dir.rglob(\"*\")):\n                    if fig_file.is_file():\n                        shutil.copy(fig_file, figures_out / fig_file.name)\n\n            # Paper PDF is pushed to GitHub in the deploy_gh_paper step (not here)\n\n            # Update result\n            result.paper = paper\n            # Sync the nested figures with the populated top-level list\n            # so ``paper.figures`` doesn't ship as null-everywhere\n            # (the LLM-emitted ``PaperText.figures`` carries the spec\n            # only — figure_path / aspect_ratio land on\n            # ``result.figures`` after gen_viz). Was the source of\n            # `paper.figures[].figure_path: None` in gen_paper_result.json\n            # (errors-doc #46) which would crash any downstream reader\n            # that touched ``paper.figures``.\n            if result.figures:\n                result.paper.figures = result.figures\n            result.metadata[\"paper_tex\"] = str(final_tex) if final_tex else None\n            result.metadata[\"paper_pdf\"] = (\n                str(final_pdf) if final_pdf and final_pdf.exists() else None\n            )\n            result.metadata[\"repo_url\"] = repo_url\n            result.metadata[\"expected_files\"] = [f.path for f in get_expected_out_files()]\n            result.metadata[\"llm_provider\"] = \"claude_agent\"\n            result.metadata[\"output_dir\"] = str(output_dir) if output_dir else None\n\n            # Save final result (step-scoped: _4_assemble_paper/gen_paper_result.json)\n            result_file = step_dir / \"gen_paper_result.json\"\n            with result_file.open(\"w\", encoding=\"utf-8\") as f:\n                json.dump(result.model_dump(), f, indent=2, ensure_ascii=False)\n            emit.status_private_info(f\"Saved result: {rel_path(result_file)}\")\n\n            if final_pdf and final_pdf.exists():\n                emit.status_public_success(f\"gen_full_paper complete: {rel_path(final_pdf)}\")\n            elif final_tex and final_tex.exists():\n                emit.status_public_success(\n                    f\"gen_full_paper complete (LaTeX only): {rel_path(final_tex)}\"\n                )\n            else:\n                emit.status_public_warning(\"gen_full_paper complete (no outputs)\")\n\n            emit.module_output(\n                module_id=mid,\n                name=\"gen_full_paper\",\n                output=result,\n            )\n            return result\n\n        finally:\n            emit.end_module(parent_id=parent_id, module_id=mid)\n", "numLines": 400, "startLine": 1, "totalLines": 400}}
```

### [69] ASSISTANT · 2026-08-21 16:30:14 UTC

```
Now find the FullPaper schema to know what fields the struct out JSON needs.
```

### [70] TOOL CALL — Bash · 2026-08-21 16:30:14 UTC

```
find /ai-inventor -path "*_4_gen_full_paper*" -name "*.py" 2>/dev/null | grep -v aii_data
```

### [71] TOOL RESULT — Bash · 2026-08-21 16:32:12 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false, "backgroundTaskId": "br3p1hswj", "timedOutAfterMs": 120000}
```

### [72] TOOL CALL — Read · 2026-08-21 16:32:14 UTC

```
/ai-inventor/aii_pipeline/src/aii_pipeline/prompts/steps/_4_gen_paper_repo/_4_gen_full_paper/out_schema.py
```

### [73] TOOL RESULT — Read · 2026-08-21 16:32:14 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_pipeline/src/aii_pipeline/prompts/steps/_4_gen_paper_repo/_4_gen_full_paper/out_schema.py", "content": "\"\"\"Schema for full paper generation step.\n\nDefines:\n- FullPaper, FullPaperExpectedFiles: Structured output for LaTeX paper generation\n- GenPaperRepoOut: Final output of gen_paper module\n\"\"\"\n\nfrom typing import Annotated, Literal\n\nfrom aii_lib.prompts import (\n    BaseExpectedFiles,\n    LLMPrompt,\n    LLMPromptModel,\n    LLMStructOut,\n    LLMStructOutModel,\n)\nfrom aii_pipeline.prompts.steps._3_invention_loop._4_gen_paper_text.out_schema import (\n    PaperText,\n)\nfrom aii_pipeline.prompts.steps._4_gen_paper_repo._2_gen_viz.out_schema import Figure\nfrom aii_pipeline.prompts.steps._4_gen_paper_repo.out_schema import GistDeployment\nfrom aii_pipeline.steps.base import BaseStepOut\nfrom pydantic import Field\n\n# =============================================================================\n# STRUCTURED OUTPUT (agent output schema)\n# =============================================================================\n\n\nclass FullPaperExpectedFiles(BaseExpectedFiles):\n    \"\"\"All expected output files from full paper generation.\"\"\"\n\n    paper_tex_path: Annotated[str, LLMPrompt, LLMStructOut] = Field(\n        description=\"Path to LaTeX source file. Example: 'paper.tex'\"\n    )\n    paper_pdf_path: Annotated[str, LLMPrompt, LLMStructOut] = Field(\n        description=\"Path to compiled PDF. Example: 'paper.pdf'\"\n    )\n    references_bib_path: Annotated[str, LLMPrompt, LLMStructOut] = Field(\n        description=\"Path to BibTeX bibliography file. Example: 'references.bib'\"\n    )\n    figure_paths: Annotated[list[str], LLMPrompt, LLMStructOut] = Field(\n        description=\"Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']\"\n    )\n\n\nclass FullPaper(LLMPromptModel, LLMStructOutModel):\n    \"\"\"Full paper — structured output from paper generation.\"\"\"\n\n    title: Annotated[str, LLMPrompt, LLMStructOut] = Field(\n        # Plain, short, one-line title; the ~40-char target lives in the\n        # description. Floor dropped 30→12 so a short plain title isn't rejected;\n        # ceiling left at the proven-safe 90 so an occasional overrun doesn't\n        # discard the whole paper output.\n        json_schema_extra={\"minLength\": 12, \"maxLength\": 90},\n        description=\"Paper title in plain, everyday language — short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).\",\n    )\n    summary: Annotated[str, LLMPrompt, LLMStructOut] = Field(\n        json_schema_extra={\"minLength\": 500, \"maxLength\": 5000},\n        description=\"Brief summary of the generated paper: sections written, figures included, compilation status\",\n    )\n    out_expected_files: Annotated[FullPaperExpectedFiles, LLMPrompt, LLMStructOut] = Field(\n        description=\"All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files.\"\n    )\n\n\n# =============================================================================\n# RESULT\n# =============================================================================\n\n\nclass GenPaperRepoOut(BaseStepOut):\n    \"\"\"Final result of gen_paper module.\"\"\"\n\n    kind: Literal[\"gen_paper_repo_out\"] = \"gen_paper_repo_out\"\n    repo_url: str | None = Field(default=None, description=\"GitHub repo URL if created\")\n\n    # Artifacts\n    gist_deployments: list[GistDeployment] = Field(default_factory=list)\n\n    # Visualizations\n    figures: list[Figure] = Field(default_factory=list)\n\n    # Paper\n    paper: PaperText | None = Field(default=None)\n", "numLines": 86, "startLine": 1, "totalLines": 86}}
```

### [74] ASSISTANT · 2026-08-21 16:32:24 UTC

```
Now I have the schema. Let's write the struct output JSON matching FullPaper.
```

### [75] TOOL CALL — Write · 2026-08-21 16:32:24 UTC

```
File: /ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.terminal_claude_agent_struct_out.json

{
  "title": "Authority Diffusion Before Founder Departure",
  "summary": "Assembled the full LaTeX paper from the provided paper_text.json content and the four pre-generated figures. Wrote paper.tex with all seven sections (Introduction, Related Work, Method, Results, A Liveness-Non-Conditioned Corpus, Discussion, Conclusion) plus abstract, using \\documentclass[11pt,letterpaper]{article} with graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings. Built references.bib by hand-authoring 19 BibTeX entries (mix of @misc for web resources, @inproceedings for the two conference papers, and @article for the journal citation) covering every numbered reference in the source text, keyed and cited in-place via \\citep. All four figures (fig1_v0.jpg concept figure, fig2_v0.pdf, fig3_v0.pdf, fig4_v0.pdf data figures) were inserted as \\begin{figure}[!htbp] blocks with width=0.92\\textwidth, keepaspectratio, a descriptive \\caption drawn from the figure's caption field, and a \\label referenced from the surrounding text via \\ref-style section pointers. Compiled with pdflatex -> bibtex.original (bibtex binary was renamed on this system; used bibtex.original directly since the wrapper was missing) -> pdflatex -> pdflatex. Final compilation produced an 11-page PDF with zero undefined references and zero unresolved citations (no [?] markers in the rendered text). Verified all 4 figures are referenced via \\includegraphics and all 19 bibliography entries resolve.",
  "out_expected_files": {
    "paper_tex_path": "paper.tex",
    "paper_pdf_path": "paper.pdf",
    "references_bib_path": "references.bib",
    "figure_paths": [
      "figures/fig1_v0.jpg",
      "figures/fig2_v0.pdf",
      "figures/fig3_v0.pdf",
      "figures/fig4_v0.pdf"
    ]
  }
}
```

### [76] TOOL RESULT — Write · 2026-08-21 16:32:24 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_LYICROwXFVjo/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Authority Diffusion Before Founder Departure\",\n  \"summary\": \"Assembled the full LaTeX paper from the provided paper_text.json content and the four pre-generated figures. Wrote paper.tex with all seven sections (Introduction, Related Work, Method, Results, A Liveness-Non-Conditioned Corpus, Discussion, Conclusion) plus abstract, using \\\\documentclass[11pt,letterpaper]{article} with graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings. Built references.bib by hand-authoring 19 BibTeX entries (mix of @misc for web resources, @inproceedings for the two conference papers, and @article for the journal citation) covering every numbered reference in the source text, keyed and cited in-place via \\\\citep. All four figures (fig1_v0.jpg concept figure, fig2_v0.pdf, fig3_v0.pdf, fig4_v0.pdf data figures) were inserted as \\\\begin{figure}[!htbp] blocks with width=0.92\\\\textwidth, keepaspectratio, a descriptive \\\\caption drawn from the figure's caption field, and a \\\\label referenced from the surrounding text via \\\\ref-style section pointers. Compiled with pdflatex -> bibtex.original (bibtex binary was renamed on this system; used bibtex.original directly since the wrapper was missing) -> pdflatex -> pdflatex. Final compilation produced an 11-page PDF with zero undefined references and zero unresolved citations (no [?] markers in the rendered text). Verified all 4 figures are referenced via \\\\includegraphics and all 19 bibliography entries resolve.\",\n  \"out_expected_files\": {\n    \"paper_tex_path\": \"paper.tex\",\n    \"paper_pdf_path\": \"paper.pdf\",\n    \"references_bib_path\": \"references.bib\",\n    \"figure_paths\": [\n      \"figures/fig1_v0.jpg\",\n      \"figures/fig2_v0.pdf\",\n      \"figures/fig3_v0.pdf\",\n      \"figures/fig4_v0.pdf\"\n    ]\n  }\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [77] TOOL CALL — Bash · 2026-08-21 16:32:26 UTC

```
python3 -c "import json; d=json.load(open('.terminal_claude_agent_struct_out.json')); print('OK', len(d['summary']))"
```

### [78] TOOL RESULT — Bash · 2026-08-21 16:32:26 UTC

```
{"stdout": "OK 1408", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [79] ASSISTANT · 2026-08-21 16:32:27 UTC

```
Created `.terminal_claude_agent_struct_out.json` matching the `FullPaper` schema (title, summary 500–5000 chars, and `out_expected_files` with paths to paper.tex, paper.pdf, references.bib, and all 4 figures). Valid JSON, verified.
```
