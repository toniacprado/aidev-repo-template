---
template: work_item
template_version: 0.4
template_date: 2026-03-11
template_last_reviewed: 2026-03-11
type: work_item
item_id: TEMPLATE-010
title: Make post-bootstrap onboarding project-facing and explicit for first-time users
status: done
owner: codex
updated: 2026-03-23
next_action: Run one fresh GitHub `Use this template` flow and confirm the generated handoff docs are clear without extra chat guidance.
blocked_on: none
---

# Make post-bootstrap onboarding project-facing and explicit for first-time users

## Summary
- Replace the current "template still talking about itself" post-bootstrap state with a
  guided handoff that clearly tells a first-time user what to edit, what to run, and
  what "ready" means.

## Acceptance Criteria
- Bootstrap rewrites the main landing docs into project-facing draft content rather than
  leaving template manifesto/charter text in place.
- A fresh repo has one obvious post-bootstrap guide with concrete next steps and command
  guidance.
- Python and PowerShell bootstrap paths stay aligned.
- Newcomer smoke checks and bootstrap tests cover the new guided handoff behavior.

## Progress Log
- 2026-03-23: task created from a real newcomer bootstrap pass that revealed the repo
  still reads like the template after initialization.
- 2026-03-23: updated both bootstrap scripts to generate project-facing draft docs plus
  a `docs/BOOTSTRAP_NEXT_STEPS.md` handoff guide.
- 2026-03-23: expanded bootstrap tests, newcomer smoke coverage, and onboarding docs to
  enforce the new post-bootstrap flow.
- 2026-03-23: ran local verification successfully.

## Verification
- `./.venv/bin/ruff format .`
- `./.venv/bin/ruff check .`
- `./.venv/bin/pytest -q` (result: `9 passed, 1 skipped`)
- `./.venv/bin/python scripts/run_prompt_evals.py`
- `./.venv/bin/python scripts/newcomer_smoke_test.py`

## Next Action
- Run one fresh GitHub `Use this template` flow and confirm the generated handoff docs
  are clear without extra chat guidance.

## Notes
- Prefer a generated post-bootstrap guide over adding a second required starter script
  unless a script materially reduces confusion.
