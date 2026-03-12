---
template: work_item
template_version: 0.4
template_date: 2026-03-11
template_last_reviewed: 2026-03-11
type: work_item
item_id: TEMPLATE-009
title: Reduce onboarding friction and harden release/CI reliability
status: done
owner: codex
updated: 2026-03-12
next_action: Run one throwaway `Use this template` flow from GitHub UI and measure newcomer completion time for the new fast path.
blocked_on: none
---

# Reduce onboarding friction and harden release/CI reliability

## Summary
- Address highest-impact critiques after launch: release bookkeeping consistency, CI
  deprecation risk, onboarding navigation friction, and newcomer checks that are
  behavioral rather than purely structural.

## Acceptance Criteria
- Changelog and version metadata clearly reflect published release state.
- CI workflow no longer emits Node 20 deprecation warning risk.
- Onboarding path is shorter and navigation is linear enough to avoid index backtracking.
- Newcomer smoke checks include at least one deterministic behavioral bootstrap check.
- Full local gates and GitHub CI pass.

## Progress Log
- 2026-03-12: task created from post-launch quality review and user feedback.
- 2026-03-12: fixed release bookkeeping drift by splitting changelog into
  `Unreleased` and `v1.2.0` sections and syncing doc version stamps.
- 2026-03-12: upgraded CI workflow actions to Node-24-ready majors:
  `actions/checkout@v6` and `actions/setup-python@v6`.
- 2026-03-12: reduced onboarding friction with a 5-step fast path in README and
  `docs/START_HERE.md`, plus explicit "next file" hints in fast-path docs.
- 2026-03-12: hardened newcomer smoke checks with a deterministic behavioral
  bootstrap check executed on a temporary scaffold.
- 2026-03-12: ran full local quality gates successfully.

## Verification
- `./.venv/bin/ruff format .`
- `./.venv/bin/ruff check .`
- `./.venv/bin/pytest -q` (result: `9 passed, 1 skipped`)
- `./.venv/bin/python scripts/run_prompt_evals.py`
- `./.venv/bin/python scripts/newcomer_smoke_test.py`

## Next Action
- Run one throwaway `Use this template` flow from GitHub UI and measure newcomer
  completion time for the new fast path.

## Notes
- Keep Codex-first positioning intact while reducing operational friction.
