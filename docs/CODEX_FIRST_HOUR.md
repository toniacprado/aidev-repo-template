# Codex First Hour
*Version:* v0.4  
*Date:* 2026-03-11  
*Last reviewed:* 2026-03-11

This guide is for first-time Codex users who want a clean, high-signal start.

## Outcome after 60 minutes
- You run Codex with safe defaults.
- You complete one small task end to end.
- You leave durable repo state (`work/`, tests, docs) instead of chat-only memory.

## Step 1: Start in safe mode (5 minutes)
- Use `on-request` approvals, `workspace-write` sandbox, and network off by default.
- Keep tasks narrow until the workflow feels predictable.
- Do not grant broader permissions unless the task truly needs them.

## Step 2: Load repo context (10 minutes)
- Ask Codex to read `AGENTS.md` and `docs/START_HERE.md` first.
- Then point it at the specific files for your task.
- Keep prompts in this shape: goal, context, constraints, done-when.

## Step 3: Plan before editing (10 minutes)
- For non-trivial work, ask Codex for a small plan first.
- Keep task slices small enough to finish and verify quickly.
- Prefer one focused task over broad, multi-feature prompts.
- Use `/plan` to enter planning mode before implementation.

## Step 4: Implement one thin slice (20 minutes)
- Ask Codex to edit only the minimum files needed.
- Require docs/tests/work updates in the same diff when behavior changes.
- Keep changes reviewable; avoid unrelated refactors.

## Step 5: Verify and review (10 minutes)
- Run the declared quality gates.
- Run `python scripts/newcomer_smoke_test.py` from the activated virtual environment.
- Ask Codex to do a review pass for bugs, regressions, missing tests, and contract drift.
- If checks cannot run, record the exact blocker.
- Use `/review` for a focused review pass and `/status` to confirm active model, permissions, and workspace roots.

## Step 6: Leave handoff state (5 minutes)
- Update `work/ACTIVE_TASKS.md` and the relevant `work/items/` file.
- Record verification results honestly.
- Leave a clear next action so another person can continue without chat history.
- Create Git checkpoints before and after substantial changes to keep rollback simple.

## Essential slash commands
- `/init`: scaffold an `AGENTS.md` file in the current directory.
- `/permissions`: tighten or relax what Codex can do without asking.
- `/plan`: switch to plan mode for complex tasks.
- `/review`: run a risk-focused review on your working tree.
- `/status`: confirm model, approval mode, and workspace roots.

## New-user pitfalls to avoid
- Starting with a huge ambiguous prompt.
- Changing code without naming files and constraints.
- Trusting a successful edit without verification.
- Ending a session without updating `work/`.
- Enabling broad permissions by default.

## Keep this open while working
- `AGENTS.md`
- `docs/CODEX_PROMPTING.md`
- `docs/TASK_MANAGEMENT.md`
- `docs/GUARDRAILS.md`
- `work/ACTIVE_TASKS.md`
