# Task Management
*Version:* v0.5  
*Date:* 2026-03-24  
*Last reviewed:* 2026-03-24

This file defines how work should stay visible in the repo instead of disappearing into
chat history.

## Canonical task artifacts
- `work/ACTIVE_TASKS.md` is the canonical current task list.
- `work/items/` holds one detailed file per meaningful task.
- `work/LEARNINGS.md` stores durable discoveries, quirks, and recurring setup notes.
- `system/templates/work_item.md` is the starting point for detailed task files.
- Chat summaries are useful, but they do not replace repo-visible task state.

## Agent rules
- If a task spans multiple steps or sessions, create or update a work item before
  doing substantial implementation.
- Before ending work, update the relevant task artifact with status, progress,
  verification state, blockers, learnings, and the next recommended action.
- If a task completes, mark it done and point to the next sensible slice when possible.
- If a task is blocked, say exactly what unblock is needed and who should act next.
- If no task artifact exists for non-trivial work, create one instead of leaving the
  plan only in chat.

## Minimum fields that must stay current
- status
- updated
- owner
- verification state
- blocker state
- next action

## Practical workflow
1. Add or update the item in `work/ACTIVE_TASKS.md`.
2. Create or update the detailed file in `work/items/` when the task needs more than a
   short line.
3. Capture reusable discoveries in `work/LEARNINGS.md`.
4. Do the implementation work.
5. Update progress, verification, and next action before handing off.

## Compaction checkpoints
If a session becomes long or the context feels noisy, compact the durable state back into
`work/` instead of relying on chat history.

Trigger points:
- before handing off multi-step work
- before switching to a new Codex thread or model
- after a meaningful plan change or architecture decision
- when too many files, logs, or tool results have accumulated in chat

Minimum compaction fields:
- current goal
- major decisions made
- files touched or the exact files to read next
- verification run and results
- blockers or open questions
- next action

Escalate durable information:
- move enduring decisions to `docs/DECISIONS.md`
- move reusable discoveries to `work/LEARNINGS.md`

## Handoff rule
A task is not fully handed off until another contributor can open `work/` and see what
is done, what is blocked, what was learned, and what should happen next. The next
contributor should be able to restart from the compacted repo state without reading the
full prior chat transcript.
