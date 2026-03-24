# Implementation Prompt
*Version:* v0.5  
*Date:* 2026-03-24  
*Last reviewed:* 2026-03-24

Goal: implement a scoped change without drifting from repo contracts.

Instructions:
- read `AGENTS.md`, `docs/CONTEXT_ENGINEERING.md`, `docs/CODEX_PROMPTING.md`,
  `docs/TASK_MANAGEMENT.md`, and only the most relevant files first
- note assumptions before changing behavior
- edit the smallest useful set of files
- retrieve additional docs or code only when the current change needs them
- update docs, prompts, evals, and tests together when behavior changes
- update `work/` with status, verification state, blockers, and next action before
  ending non-trivial work
- if AI behavior changes, review `docs/MODEL_POLICY.md` and `docs/GUARDRAILS.md`
- run the required verification and report anything you could not verify
