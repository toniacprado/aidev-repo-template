# Newcomer Usability Checklist
*Version:* v0.2  
*Date:* 2026-03-11  
*Last reviewed:* 2026-03-11

Use this checklist before calling the template "ready for first-time Codex users."

## Automated smoke check
- Run: `python scripts/newcomer_smoke_test.py` (from the activated virtual environment)
- Expected: all required checks pass.

## Manual first-hour walkthrough
1. Start with `docs/START_HERE.md` and `docs/CODEX_FIRST_HOUR.md`.
2. Run bootstrap on your OS:
   - `python3 scripts/bootstrap_new_project.py --project-name "Trial Project"` (macOS/Linux)
   - `python scripts/bootstrap_new_project.py --project-name "Trial Project"` (Windows)
3. Ask Codex for a plan on one small task (`/plan`).
4. Implement one thin slice with verification.
5. Ask for a review pass (`/review`).
6. Confirm handoff state in `work/ACTIVE_TASKS.md`.

## Pass criteria
- New user can complete one end-to-end task without relying on hidden chat context.
- Prompt/eval assets and deterministic eval checks are understandable and runnable.
- Task state and next action are visible in `work/`.

## Follow-up rule
- If any step is confusing, create a task in `work/` and fix docs/scripts before release.
