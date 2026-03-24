# Context Engineering
*Version:* v0.1  
*Date:* 2026-03-24  
*Last reviewed:* 2026-03-24

This file defines how the repo should manage AI context: load the smallest high-signal
set of tokens for the current step, retrieve more only when needed, and write durable
state back into repo files instead of depending on chat memory.

## Core rule
Treat context as a finite attention budget.

Default behavior:
- start with the smallest relevant context pack for the task
- prefer repo files over chat recollection
- retrieve additional files just in time
- compact long-session state back into the repo

## Context layering order
1. Product intent:
   `docs/PROJECT_MANIFESTO.md` and `docs/PROJECT_CHARTER.md`
2. Execution policy:
   `AGENTS.md` and the relevant pack from this file
3. Current task state:
   `work/ACTIVE_TASKS.md` and the relevant work item in `work/items/`
4. Direct targets:
   the exact source, test, prompt, eval, or doc files involved
5. Extra references:
   only the specific policy, standard, or external source needed for the current step

Do not preload categories 4 and 5 until the task actually requires them.

## Task-specific context packs
### Bootstrap / project-definition pack
Use when the repo is freshly bootstrapped or the core product docs are still placeholders.

Load:
- `AGENTS.md`
- `docs/CONTEXT_ENGINEERING.md`
- `docs/CODEX_SESSION_STARTER.md` when it exists
- `docs/BOOTSTRAP_NEXT_STEPS.md` when it exists
- `docs/BOOTSTRAP_ARTIFACT_WORKSHOP.md` when it exists
- `docs/PROJECT_MANIFESTO.md`
- `docs/PROJECT_CHARTER.md`
- `docs/TECH_STACK_SELECTION.md`
- `docs/DECISIONS.md`
- `work/ACTIVE_TASKS.md`
- the active bootstrap work item in `work/items/`

Usually do not load yet:
- full engineering standards
- unrelated source files
- prompt/eval assets unless model behavior is already in scope

### Implementation pack
Use when executing a scoped feature, bug fix, or doc change.

Load:
- `AGENTS.md`
- `docs/CONTEXT_ENGINEERING.md`
- `work/ACTIVE_TASKS.md`
- the relevant work item
- the target files you expect to edit
- the exact tests or evals that should verify the slice

Add only if needed:
- `docs/PROJECT_CHARTER.md` when scope boundaries matter
- `docs/ENGINEERING_STANDARDS.md` when implementation conventions matter
- `docs/GUARDRAILS.md` and `docs/MODEL_POLICY.md` when AI behavior is in scope

### Review pack
Use when reviewing for bugs, regressions, missing tests, or contract drift.

Load:
- `AGENTS.md`
- `docs/CONTEXT_ENGINEERING.md`
- the changed files or diff
- the directly related tests, evals, or contracts

Add only if needed:
- `docs/GUARDRAILS.md` and `docs/MODEL_POLICY.md` for AI-facing behavior
- `docs/ENGINEERING_STANDARDS.md` when code conventions affect correctness
- the relevant work item if verification or task tracking is part of the review

### Prompt / eval pack
Use when editing prompt assets, evals, schemas, or model-facing behavior.

Load:
- `AGENTS.md`
- `docs/CONTEXT_ENGINEERING.md`
- `docs/CODEX_PROMPTING.md`
- `prompts/README.md`
- `evals/README.md`
- the touched prompt, eval, schema, and fixture files

Add only if needed:
- `docs/GUARDRAILS.md`
- `docs/MODEL_POLICY.md`
- downstream code that consumes the model output

### External research pack
Use when the repo alone is not sufficient because the task depends on changing external facts.

Load:
- the smallest relevant repo pack first
- the official external documentation or source
- only the exact pages or excerpts needed for the decision

Do not:
- paste large copied summaries into the prompt when the source can be read directly
- keep stale external summaries as the main source of truth

## Just-in-time retrieval rules
- Use file names, directory structure, and task artifacts as retrieval hints.
- Search narrowly first, then open only the most relevant files.
- Prefer targeted excerpts over large file dumps when reviewing logs or generated data.
- If a prompt is vague, ask for the goal and target files before loading more context.
- When an external source leads to a durable decision, write the decision back into the repo.

## Compaction rules
If a session becomes long, context starts feeling noisy, or you are about to hand off,
compact the durable state back into the repo.

Trigger points:
- before ending a multi-step task
- before switching threads or models
- after a plan change or architecture decision
- after many tool calls, logs, or file reads have accumulated

Minimum compaction payload:
- current goal
- major decisions made
- files touched or the exact files to read next
- verification run and results
- blockers or open questions
- next action

Where it goes:
- `work/items/` for task-local continuity
- `docs/DECISIONS.md` for enduring choices
- `work/LEARNINGS.md` for reusable discoveries

After compaction, restart from the compacted repo state instead of replaying the full
chat transcript.

## Scope discipline
- Prefer single-agent execution unless evals justify more coordination.
- Do the simplest thing that keeps context clear and reviewable.
- If a context pack feels too large, shrink it before adding new instructions.
