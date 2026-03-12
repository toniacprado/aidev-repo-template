---
template: work_item
template_version: 0.4
template_date: 2026-03-11
template_last_reviewed: 2026-03-11
type: work_item
item_id: TEMPLATE-002
title: Make the repo template-ready for cloning and bootstrap
status: done
owner: codex
updated: 2026-03-11
next_action: Publish as a GitHub template repo, confirm or change the MIT license, and bootstrap a real project from it.
blocked_on: none
---

# Make the repo template-ready for cloning and bootstrap

## Summary
- Add the missing assets and workflow needed to copy this repo into a real new project
  without carrying template-specific state forward.

## Acceptance Criteria
- The repo includes an explicit reusable license.
- The README explains the preferred GitHub template flow and the fallback clone flow.
- A bootstrap script resets template identity and starter task state for a new project.
- The bootstrap flow has at least one happy-path automated test.
- Default quality gates pass after the template-ready changes.

## Progress Log
- 2026-03-11: added an MIT `LICENSE` and documented template usage in `README.md`.
- 2026-03-11: added `scripts/bootstrap_new_project.ps1` and updated the bootstrap checklist.
- 2026-03-11: extended the template contract tests to require the new bootstrap assets.
- 2026-03-11: added a happy-path test for `scripts/bootstrap_new_project.ps1`.
- 2026-03-11: fixed a `pyproject.toml` rename bug caught by the new bootstrap test.
- 2026-03-11: reran the Ruff and Pytest gates successfully after the fix.

## Verification
- `ruff format .`
- `ruff check .`
- `pytest -q`

## Next Action
- Publish this repo as a GitHub template, confirm the license choice, and bootstrap a real
  project from it.

## Notes
- MIT was added as the default permissive template license; change it if a different reuse
  model is desired.
