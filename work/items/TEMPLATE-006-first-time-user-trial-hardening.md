---
template: work_item
template_version: 0.4
template_date: 2026-03-11
template_last_reviewed: 2026-03-11
type: work_item
item_id: TEMPLATE-006
title: Run first-time user trial and harden cross-platform onboarding
status: done
owner: codex
updated: 2026-03-11
next_action: Run one external newcomer trial with a user unfamiliar with this repo and capture any friction as TEMPLATE-007.
blocked_on: none
---

# Run first-time user trial and harden cross-platform onboarding

## Summary
- Execute a manual newcomer walkthrough and convert observed onboarding friction into
  concrete docs/script/test improvements.

## Acceptance Criteria
- At least one real newcomer friction point is reproduced and documented.
- Onboarding path includes a cross-platform bootstrap option.
- Docs clearly explain interpreter aliases (`python` vs `python3`) and Python version
  requirement for template maintenance.
- Verification and contract tests pass after changes.

## Progress Log
- 2026-03-11: task created.
- 2026-03-11: reproduced newcomer blockers on macOS shell:
  - `pwsh` command not found while following bootstrap instructions.
  - `python` command not found while following setup/check commands.
- 2026-03-11: added cross-platform bootstrap entrypoint `scripts/bootstrap_new_project.py`
  and tests to cover explicit and derived slug paths.
- 2026-03-11: updated onboarding docs to promote Python bootstrap path first and clarify
  OS-specific maintenance setup commands.
- 2026-03-11: updated newcomer smoke checks to enforce cross-platform bootstrap docs and
  script presence.
- 2026-03-11: reran full quality gates successfully.

## Verification
- `./.venv/bin/ruff format .`
- `./.venv/bin/ruff check .`
- `./.venv/bin/pytest -q` (result: `9 passed, 1 skipped`)
- `./.venv/bin/python scripts/run_prompt_evals.py`
- `./.venv/bin/python scripts/newcomer_smoke_test.py`

## Next Action
- Run one external newcomer trial with a user unfamiliar with this repo and capture any
  friction as `TEMPLATE-007`.

## Notes
- Keep changes stack-agnostic for downstream projects; Python remains maintenance-only.
