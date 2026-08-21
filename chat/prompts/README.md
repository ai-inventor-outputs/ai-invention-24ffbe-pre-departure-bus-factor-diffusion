# Prompts

Complete, auto-generated record of **every prompt the AI Inventor system gave each agent** across this run — generated at repository-upload time so it captures all steps. For the full conversation (assistant turns, thinking, tool calls and results) see the sibling `../messages/` folder.

- Run: `iter2_13ec49ac7efb` — Authority Diffusion Before Founder Departure: Diagnosing Sample Starvation in OSS Survival Research

Each prompt is labelled by type and timestamped, with its full untruncated body:

- **SYSTEM-USER** — the pipeline-generated role/instruction prompt placed in the user slot.
- **HUMAN-USER** — the task / human-typed message into the agent stream.
- **SKILL-INPUT** — a skill the agent loaded; its `SKILL.md` instructions, verbatim.

Layout mirrors the run's module tree: one folder per high-level phase, a `round_N/` per iteration where the phase iterates, then each module — a single-task module is one `.md` file, a parallel module (gen_plan / gen_art / gen_viz / gen_demo_art) is a folder with one `.md` per task.

## Index

- **1. test_idea** — `invention_loop`
  - round_2
    - `1_gen_art/` — 2 task(s)
      - `chat/prompts/1_test_idea/round_2/1_gen_art/gen_art_dataset_1.md` — 7 prompts
      - `chat/prompts/1_test_idea/round_2/1_gen_art/gen_art_evaluation_1.md` — 10 prompts
    - `chat/prompts/1_test_idea/round_2/2_gen_paper_text.md` — 3 prompts
    - `chat/prompts/1_test_idea/round_2/3_review_paper.md` — 2 prompts
    - `chat/prompts/1_test_idea/round_2/4_upd_hypo.md` — 3 prompts
- **2. report_results** — `gen_paper_repo`
  - `1_gen_viz/` — 4 task(s)
    - `chat/prompts/2_report_results/1_gen_viz/gen_viz_1.md` — 5 prompts
    - `chat/prompts/2_report_results/1_gen_viz/gen_viz_2.md` — 2 prompts
    - `chat/prompts/2_report_results/1_gen_viz/gen_viz_3.md` — 2 prompts
    - `chat/prompts/2_report_results/1_gen_viz/gen_viz_4.md` — 5 prompts
  - `2_gen_demo_art/` — 5 task(s)
    - `chat/prompts/2_report_results/2_gen_demo_art/gen_demo_art_dataset_1.md` — 9 prompts
    - `chat/prompts/2_report_results/2_gen_demo_art/gen_demo_art_dataset_2.md` — 9 prompts
    - `chat/prompts/2_report_results/2_gen_demo_art/gen_demo_art_evaluation_1.md` — 14 prompts
    - `chat/prompts/2_report_results/2_gen_demo_art/gen_demo_art_evaluation_2.md` — 10 prompts
    - `chat/prompts/2_report_results/2_gen_demo_art/gen_demo_art_experiment_1.md` — 14 prompts
  - `chat/prompts/2_report_results/3_gen_full_paper.md` — 3 prompts
