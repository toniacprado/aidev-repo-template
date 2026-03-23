# Newcomer Usability Checklist
*Version:* v0.3  
*Date:* 2026-03-23  
*Last reviewed:* 2026-03-23

Use this checklist before calling the template "ready for first-time Codex users."

## Automated smoke check
- Run: `python scripts/newcomer_smoke_test.py` (from the activated virtual environment)
- Expected: all required checks pass.

## Manual first-hour walkthrough
1. Start with `docs/START_HERE.md` and `docs/CODEX_FIRST_HOUR.md`.
2. Run bootstrap on your OS:
   - `python3 scripts/bootstrap_new_project.py --project-name "Trial Project"` (macOS/Linux)
   - `python scripts/bootstrap_new_project.py --project-name "Trial Project"` (Windows)
3. Confirm the new repo now points first-time users to `docs/BOOTSTRAP_NEXT_STEPS.md`
   and that the generated manifesto/charter/stack docs are project-facing drafts rather
   than template narrative.
4. Ask Codex for a plan on one small task (`/plan`).
5. Implement one thin slice with verification.
6. Ask for a review pass (`/review`).
7. Confirm handoff state in `work/ACTIVE_TASKS.md`.

## Pass criteria
- New user can complete one end-to-end task without relying on hidden chat context.
- Prompt/eval assets and deterministic eval checks are understandable and runnable.
- Task state and next action are visible in `work/`.

## Follow-up rule
- If any step is confusing, create a task in `work/` and fix docs/scripts before release.
