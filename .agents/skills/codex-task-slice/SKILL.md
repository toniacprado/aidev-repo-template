# Skill: codex-task-slice

## Use when
- You need to implement one focused change with clear verification.
- The task should be small enough to complete in one coding session.

## Workflow
1. Read `AGENTS.md`, `docs/CODEX_PROMPTING.md`, `docs/TASK_MANAGEMENT.md`, and the relevant work item.
2. Restate goal, context, constraints, and done-when.
3. Implement the thinnest useful slice only.
4. Update docs/tests/evals/contracts in the same diff when behavior changes.
5. Run verification and report what was or was not run.
6. Update `work/ACTIVE_TASKS.md` and the matching `work/items/` file with next action.

## Guardrails
- Do not broaden scope without explicit approval.
- Do not claim verification you did not run.
- Call out risks and blockers explicitly before handoff.
