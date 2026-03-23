---
template: work_item
template_version: 0.4
template_date: 2026-03-11
template_last_reviewed: 2026-03-11
type: work_item
item_id: TEMPLATE-012
title: Fix ship-blocking bootstrap handoff gaps before template trial
status: done
owner: codex
updated: 2026-03-23
next_action: Run a fresh GitHub `Use this template` trial from the branch-backed PR and verify the generated session starter rewrites the landing docs cleanly.
blocked_on: none
---

# Fix ship-blocking bootstrap handoff gaps before template trial

## Summary
- Close the review findings that would let a fresh repo complete the recommended
  bootstrap flow while still leaving placeholder landing docs in place or suggesting a
  redundant rerun of bootstrap.

## Acceptance Criteria
- The generated Codex session starter and artifact workshop explicitly include
  `README.md` and `docs/START_HERE.md` as bootstrap artifacts.
- The generated bootstrap handoff and work item acceptance criteria include the landing
  docs, not only the manifesto/charter/stack docs.
- `AGENTS.md` makes clear that bootstrap is a one-time reset for a fresh template copy
  and should not be recommended again after completion unless the user explicitly asks
  for a reset.
- Tests and smoke checks cover the corrected behavior.

## Progress Log
- 2026-03-23: task created from the due-diligence review before the real GitHub template
  trial.
- 2026-03-23: updated the generated session starter, artifact workshop, bootstrap next-step
  guide, and bootstrap work item so the landing docs are part of the required handoff.
- 2026-03-23: updated `AGENTS.md` so Codex treats bootstrap as a one-time reset and does
  not suggest rerunning it after completion.
- 2026-03-23: extended automated coverage and reran the local verification stack successfully.
- 2026-03-23: fixed a PowerShell bootstrap regression that broke CI on `pwsh` runners by
  replacing expandable markdown-heavy here-strings with literal templates plus explicit token
  expansion.

## Verification
- `./.venv/bin/ruff format .`
- `./.venv/bin/ruff check .`
- `./.venv/bin/pytest -q` (result: `9 passed, 1 skipped`)
- `./.venv/bin/python scripts/run_prompt_evals.py`
- `./.venv/bin/python scripts/newcomer_smoke_test.py`

## Next Action
- Wait for the repaired branch CI to pass, then run a fresh GitHub `Use this template`
  trial and verify the generated session starter rewrites the landing docs cleanly.

## Notes
- Keep the fix narrowly scoped to the blocking review findings so the template trial is
  still representative.
