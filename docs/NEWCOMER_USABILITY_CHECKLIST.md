# Newcomer Usability Checklist
*Version:* v0.6  
*Date:* 2026-03-28  
*Last reviewed:* 2026-03-28

Use this checklist before calling the template "ready for first-time Codex users."

## Automated smoke check
- Run: `python scripts/newcomer_smoke_test.py` (from the activated virtual environment)
- Expected: all required checks pass.

## Manual first-hour walkthrough
1. Start with `docs/START_HERE.md`, `docs/CODEX_FIRST_HOUR.md`, and `docs/CONTEXT_ENGINEERING.md`.
2. Run bootstrap on your OS:
   - `python3 scripts/bootstrap_new_project.py --project-name "Trial Project"` (macOS/Linux)
   - `python scripts/bootstrap_new_project.py --project-name "Trial Project"` (Windows)
3. Confirm the new repo points first-time users to `docs/CODEX_SESSION_STARTER.md` and
   `docs/BOOTSTRAP_NEXT_STEPS.md` instead of expecting a blank one-shot prompt.
4. Use the generated session starter to hand the repo to Codex and confirm Codex begins
   by drafting the core artifacts or explicitly offers the skip path with warnings.
5. Confirm the generated manifesto/charter/stack/decision docs are project-facing drafts
   rather than template narrative.
6. Ask Codex for a plan on one small task (`/plan`) using only the smallest relevant context
   pack rather than a broad repo preload.
7. Implement one thin slice with verification.
8. Use the guidance in `docs/GIT_WORKFLOW.md` to choose whether this repo should publish from
   `main` directly or through a short-lived PR branch.
9. Ask for a review pass (`/review`).
10. Confirm handoff state in `work/ACTIVE_TASKS.md`.
11. If the session became long, confirm the durable state was compacted back into `work/`
    rather than left only in chat.

## Pass criteria
- New user can complete one end-to-end task without relying on hidden chat context.
- New user can choose an appropriate context pack without being told to read the whole repo.
- New user can choose a sensible Git publish path without defaulting to unnecessary branch
  churn or unsafe direct-to-main behavior.
- Prompt/eval assets and deterministic eval checks are understandable and runnable.
- Task state and next action are visible in `work/`.

## Follow-up rule
- If any step is confusing, create a task in `work/` and fix docs/scripts before release.
