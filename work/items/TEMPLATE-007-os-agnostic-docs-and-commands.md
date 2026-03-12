---
template: work_item
template_version: 0.4
template_date: 2026-03-11
template_last_reviewed: 2026-03-11
type: work_item
item_id: TEMPLATE-007
title: Normalize docs and maintenance commands for OS-agnostic usage
status: done
owner: codex
updated: 2026-03-12
next_action: Run one external newcomer pass on Linux and one on Windows to validate the command conventions in real environments.
blocked_on: none
---

# Normalize docs and maintenance commands for OS-agnostic usage

## Summary
- Remove avoidable OS-specific assumptions from maintenance and onboarding docs while
  keeping optional PowerShell paths for Windows users.

## Acceptance Criteria
- Core onboarding docs present shell-neutral verification commands.
- Maintenance setup clarifies interpreter alias differences (`python` vs `python3`).
- Command conventions for this repo are documented and linked.
- Quality gates pass after updates.

## Progress Log
- 2026-03-12: task created from user request to make the template more OS agnostic.
- 2026-03-12: audited docs and found remaining shell-label drift (PowerShell code
  fences used for shell-neutral command sequences).
- 2026-03-12: added `docs/COMMAND_CONVENTIONS.md` and linked it from core onboarding
  docs and AGENTS guidance.
- 2026-03-12: normalized verification command blocks to shell-neutral snippets where
  commands are not shell-specific.
- 2026-03-12: updated bootstrap checklist to use venv-first `python` with explicit
  macOS/Linux `python3` fallback.
- 2026-03-12: reran full quality gates successfully.

## Verification
- `./.venv/bin/ruff format .`
- `./.venv/bin/ruff check .`
- `./.venv/bin/pytest -q` (result: `9 passed, 1 skipped`)
- `./.venv/bin/python scripts/run_prompt_evals.py`
- `./.venv/bin/python scripts/newcomer_smoke_test.py`

## Next Action
- Run one external newcomer pass on Linux and one on Windows to validate command
  conventions in real environments.

## Notes
- Keep PowerShell as an optional path, not the primary onboarding flow.
