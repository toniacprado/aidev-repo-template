---
template: work_item
template_version: 0.4
template_date: 2026-03-11
template_last_reviewed: 2026-03-11
type: work_item
item_id: TEMPLATE-001
title: Harden the repo template to current OpenAI-aligned Codex best practices
status: done
owner: codex
updated: 2026-03-11
next_action: Bootstrap a real project from this template or keep iterating on optional variants.
blocked_on: none
---

# Harden the repo template to current OpenAI-aligned Codex best practices

## Summary
- Extend the template with stronger Codex prompting, environment, model, guardrail,
  task-tracking, maintenance, and cross-tool compatibility guidance.

## Acceptance Criteria
- The repo includes explicit Codex prompting guidance.
- The repo includes explicit environment, model, and guardrail policy docs.
- The repo includes durable task tracking and learnings files.
- The repo clearly explains that Python is a maintenance-only layer.
- The repo includes cross-tool compatibility guidance for Claude-style workflows.
- Template contract checks pass.

## Progress Log
- 2026-03-11: rewrote core repo docs into a Codex-first operating model.
- 2026-03-11: added `work/` task tracking and next-step requirements.
- 2026-03-11: added `docs/CODEX_PROMPTING.md`, `docs/CODEX_ENVIRONMENT.md`,
  `docs/MODEL_POLICY.md`, `docs/GUARDRAILS.md`, `.codex/`, `CLAUDE.md`, and policy assets.
- 2026-03-11: clarified that Python in this repo is a template-maintenance-only layer
  and added `docs/TEMPLATE_MAINTENANCE.md`.
- 2026-03-11: ran repo-local structure checks successfully.
- 2026-03-11: created a local virtual environment, installed maintenance dependencies,
  and ran the full Ruff and Pytest gates successfully.

## Verification
- `ruff format .`
- `ruff check .`
- `pytest -q`

## Next Action
- Bootstrap a real project from this template or keep iterating on optional variants.

## Notes
- The Codex shell could use Python once the interpreter was called by absolute path.
