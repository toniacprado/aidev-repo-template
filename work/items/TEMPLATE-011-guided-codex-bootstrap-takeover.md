---
template: work_item
template_version: 0.4
template_date: 2026-03-11
template_last_reviewed: 2026-03-11
type: work_item
item_id: TEMPLATE-011
title: Add guided Codex bootstrap takeover with strong recommendations and skip path
status: done
owner: codex
updated: 2026-03-23
next_action: Run one fresh GitHub `Use this template` flow and confirm a new user can hand the repo to Codex with the generated session starter alone.
blocked_on: none
---

# Add guided Codex bootstrap takeover with strong recommendations and skip path

## Summary
- Make the generated repo actively help a new user hand control to Codex for project
  definition, while still allowing experienced users to skip bootstrap with explicit
  warnings and recorded assumptions.

## Acceptance Criteria
- The generated repo includes one obvious first-session prompt the user can paste into
  Codex.
- The generated repo includes artifact-by-artifact guidance that helps Codex interview
  the user and draft the core files.
- Repo instructions tell Codex to strongly recommend bootstrap mode when core docs are
  still placeholders, but to allow a skip if the user insists.
- Onboarding docs and tests reflect the new guided takeover behavior.

## Progress Log
- 2026-03-23: task created after deciding the template should teach the first Codex
  conversation, not only the file structure.
- 2026-03-23: updated bootstrap scripts to generate a session starter prompt, artifact
  workshop, stronger bootstrap handoff, and a reset decisions log in fresh repos.
- 2026-03-23: added inherited bootstrap-mode guidance in `AGENTS.md`,
  `docs/CODEX_FIRST_HOUR.md`, `docs/AI_DEV_WORKFLOW.md`, and
  `docs/CODEX_PROMPTING.md`.
- 2026-03-23: updated onboarding docs and automated checks to enforce the new Codex
  takeover path.
- 2026-03-23: ran local verification successfully.

## Verification
- `./.venv/bin/ruff format .`
- `./.venv/bin/ruff check .`
- `./.venv/bin/pytest -q` (result: `9 passed, 1 skipped`)
- `./.venv/bin/python scripts/run_prompt_evals.py`
- `./.venv/bin/python scripts/newcomer_smoke_test.py`

## Next Action
- Run one fresh GitHub `Use this template` flow and confirm a new user can hand the
  repo to Codex with the generated session starter alone.

## Notes
- Favor high-signal handholding over hard gates; users should feel steered, not trapped.
