---
template: work_item
template_version: 0.4
template_date: 2026-03-11
template_last_reviewed: 2026-03-11
type: work_item
item_id: TEMPLATE-003
title: Harden template bootstrap and verification after repo inventory
status: done
owner: codex
updated: 2026-03-11
next_action: Run one final manual bootstrap smoke test on a machine with PowerShell before publishing as a GitHub template.
blocked_on: none
---

# Harden template bootstrap and verification after repo inventory

## Summary
- Audit the template for release readiness and close critical gaps that can break first-run bootstrap or verification trust.

## Acceptance Criteria
- Bootstrap script no longer writes stale hardcoded dates.
- Bootstrap cleanup removes template-only work item files reliably.
- Bootstrap writes remain UTF-8 across PowerShell variants.
- Bootstrap test skips cleanly when PowerShell is unavailable.
- Template contract test coverage reflects canonical docs and assets.
- Verification is rerun and accurately reported with any environment limits.

## Progress Log
- 2026-03-11: task created from inventory findings.
- 2026-03-11: updated bootstrap script to use dynamic dates, UTF-8 writes, and removal of all `TEMPLATE-*.md` work items.
- 2026-03-11: updated bootstrap test to skip when PowerShell is unavailable and to assert dynamic-date output plus full template-item cleanup.
- 2026-03-11: expanded template contract checks to cover more canonical docs, policy assets, prompts, schemas, templates, and GitHub workflow files.
- 2026-03-11: updated CI verification to run on both Ubuntu and Windows to keep bootstrap coverage active in PowerShell-capable runners.
- 2026-03-11: reran lint and tests in local venv after installing fallback tooling.

## Verification
- `./.venv/bin/ruff format tests/test_bootstrap_new_project_script.py tests/test_template_contract.py`
- `./.venv/bin/ruff check .`
- `./.venv/bin/pytest -q` (result: `4 passed, 1 skipped`; skip is expected when PowerShell is unavailable locally)

## Next Action
- Run one final manual bootstrap smoke test on a machine with PowerShell before publishing as a GitHub template.

## Notes
- Full default setup `python -m pip install -e ".[dev]"` was not runnable here because the host only has Python 3.9 while the template requires `>=3.12`.
