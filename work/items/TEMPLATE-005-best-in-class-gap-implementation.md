---
template: work_item
template_version: 0.4
template_date: 2026-03-11
template_last_reviewed: 2026-03-11
type: work_item
item_id: TEMPLATE-005
title: Implement best-in-class gaps: eval runner, rules/skills scaffolding, newcomer harness, and issue templates
status: done
owner: codex
updated: 2026-03-11
next_action: Run a real first-time user trial and convert friction into follow-up tasks.
blocked_on: none
---

# Implement best-in-class gaps: eval runner, rules/skills scaffolding, newcomer harness, and issue templates

## Summary
- Close the top remaining template gaps after OpenAI docs benchmarking by adding executable checks and practical scaffolding for repeatable Codex workflows.

## Acceptance Criteria
- Prompt/eval checks are executable and enforced in CI.
- At least one deterministic golden eval case is runnable locally.
- Repo includes Codex rules and skills starter scaffolding.
- Repo includes newcomer smoke-test harness and checklist.
- Repo includes issue templates aligned with Codex task slicing and prompt/eval work.
- Core docs and contracts are updated accordingly.

## Progress Log
- 2026-03-11: task created.
- 2026-03-11: added deterministic prompt/eval tooling (`scripts/run_prompt_evals.py`) plus golden fixtures and automated tests.
- 2026-03-11: integrated prompt/eval checks into CI and core docs/verification commands.
- 2026-03-11: added newcomer harness (`scripts/newcomer_smoke_test.py`) and `docs/NEWCOMER_USABILITY_CHECKLIST.md`.
- 2026-03-11: added starter skills under `.agents/skills/` and Codex rules scaffolding under `codex/rules/`.
- 2026-03-11: added Codex-aligned GitHub issue templates under `.github/ISSUE_TEMPLATE/`.
- 2026-03-11: reran local quality gates and smoke checks successfully.

## Verification
- `./.venv/bin/ruff check .`
- `./.venv/bin/pytest -q` (result: `7 passed, 1 skipped`)
- `./.venv/bin/python scripts/run_prompt_evals.py`
- `./.venv/bin/python scripts/newcomer_smoke_test.py`

## Next Action
- Run a real first-time user trial and convert friction into follow-up tasks.

## Notes
- Keep changes deterministic and runnable offline where possible.
