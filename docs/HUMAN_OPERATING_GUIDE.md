# Human Operating Guide
*Version:* v0.8  
*Date:* 2026-03-28  
*Last reviewed:* 2026-03-28

This document explains how a human teammate should use this template day to day.

## What this template is for
Use this repo when you want AI assistance to be strong, reviewable, and grounded in
project files instead of private chat memory.

The template helps you:
- capture intent before implementation starts
- keep Codex aligned with humans through local docs
- version prompts and evals like real product assets
- keep task state and next steps visible across sessions
- keep model, guardrail, and environment choices explicit
- keep generated artifacts out of canonical source-of-truth paths

## The 10-minute orientation
- If you are new to Codex, start with `docs/CODEX_FIRST_HOUR.md`.
- Then read `docs/CONTEXT_ENGINEERING.md` so you know which context pack to use.
- Read `docs/GIT_WORKFLOW.md` if you will publish changes through GitHub or collaborate
  with others.
- Validate onboarding quality with `docs/NEWCOMER_USABILITY_CHECKLIST.md`.
- `docs/` explains why the project exists, what is in scope, and how the team works.
- `work/` stores the active task list, durable learnings, and detailed task files.
- `.codex/` stores shared Codex config examples and local-environment notes.
- `system/` contains reusable contracts, templates, prompts, and policy assets.
- `prompts/` stores runtime prompts that the product sends to models.
- `evals/` stores test cases and rubrics for prompt or agent behavior.
- `src/` and `tests/` contain implementation and deterministic verification.
- `runtime/` is for rebuildable outputs only.

## The default work loop
1. Clarify the change in `docs/` first if intent or scope is fuzzy.
2. Ask Codex to read the smallest relevant context pack from `docs/CONTEXT_ENGINEERING.md`
   before changing anything.
3. Make sure there is a current task artifact in `work/` for multi-step work.
4. Implement the smallest correct slice.
5. Review the diff for contract drift, missing tests, prompt or eval updates, and task
   state updates.
6. Run verification and record any residual risk.
7. Before ending the session, compact the durable state into `work/` if the session became
   long, then make sure `work/` shows what is next.

## Git workflow default
- Use local commits or checkpoints freely while you work.
- If the repo is private, solo, and unprotected, direct commits to `main` can be the
  simplest correct workflow.
- If the repo is protected, public, or shared, publish through one short-lived branch per
  mergeable slice instead of pushing directly to `main`.
- If you discover related fixes before merge, keep them on the same branch unless the issue
  is genuinely separate.

## How to prompt Codex well
Good requests usually include:
- the exact task
- the files Codex should read first
- the expected output
- constraints or non-goals
- verification expectations
- whether the task tracker should be updated before closing

Example:

```text
Read docs/PROJECT_CHARTER.md, docs/CODEX_PROMPTING.md, docs/TASK_MANAGEMENT.md,
docs/CONTEXT_ENGINEERING.md, and work/ACTIVE_TASKS.md. Implement the next slice, keep the
change minimal, update the relevant task file with status and next action, and run the
default verification.
```

## When to create or update specific artifacts
- Update `docs/PROJECT_MANIFESTO.md` when the product purpose or non-goals change.
- Update `docs/PROJECT_CHARTER.md` when scope, users, or success metrics change.
- Update `docs/DECISIONS.md` when a meaningful architectural or workflow decision is
  made.
- Add or update files in `work/` when a task or discovery should survive beyond the
  current chat.
- Add or update files in `prompts/` when runtime model behavior changes.
- Add or update files in `evals/` when prompt or agent behavior should be tested.
- Review `docs/MODEL_POLICY.md` and `docs/GUARDRAILS.md` when AI behavior or tool
  permissions change.

## Human review checklist
- Is the source of truth still obvious after this change?
- Did the diff update docs, prompts, evals, tasks, and tests together where needed?
- Are there any hidden assumptions still living only in chat?
- Can a new teammate find the next step in the repo without asking?
- Are model, guardrail, and environment changes explicit and reviewable?
- Did we keep the repo simpler instead of more clever?
