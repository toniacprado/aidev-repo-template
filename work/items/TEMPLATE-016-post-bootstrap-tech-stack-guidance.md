---
template: work_item
template_version: 0.4
template_date: 2026-03-11
template_last_reviewed: 2026-03-11
type: work_item
item_id: TEMPLATE-016
title: Harden post-bootstrap tech stack decision and adoption guidance
status: done
owner: codex
updated: 2026-03-29
next_action: Validate the revised stack handoff in one fresh `Use this template` run and confirm a newcomer can replace the inherited Python defaults without extra chat guidance.
blocked_on: none
---

# Harden post-bootstrap tech stack decision and adoption guidance

## Summary
- Review the current bootstrap and newcomer handoff flow for how it teaches stack choice
  after a fresh repo is created.
- Convert the weak spot into explicit repo guidance so users know how to pick the real
  stack and what repo surfaces need to change after that decision.

## Acceptance Criteria
- The template-level and generated post-bootstrap docs explain that stack selection also
  requires naming canonical setup and verification commands plus the repo changes needed
  to adopt the chosen stack.
- The bootstrap artifact workshop prompts Codex to ask about stack adoption, not only
  framework choice.
- The generated bootstrap work item and handoff docs make the follow-through visible in
  `work/`.
- Bootstrap tests and newcomer smoke checks cover the strengthened guidance.

## Progress Log
- 2026-03-29: task created after a real template-user pass surfaced a gap between
  choosing a tech stack and reconciling the repo with that choice after bootstrap.
- 2026-03-29: strengthened the template-level stack-selection guidance, bootstrap
  checklist, prompting docs, and decision log so the stack step now includes canonical
  commands plus repo follow-through.
- 2026-03-29: updated both bootstrap generators, the generated bootstrap work item, and
  newcomer coverage so fresh repos now ask for stack adoption decisions instead of only
  framework choice.
- 2026-03-29: reran the local maintenance suite successfully after tightening the new
  assertions.

## Verification
- `./.venv/bin/ruff format .`
- `./.venv/bin/ruff check .`
- `./.venv/bin/pytest -q` (result: `9 passed, 1 skipped`)
- `./.venv/bin/python scripts/run_prompt_evals.py`
- `./.venv/bin/python scripts/newcomer_smoke_test.py`

## Next Action
- Validate the revised stack handoff in one fresh `Use this template` run and confirm a
  newcomer can replace the inherited Python defaults without extra chat guidance.

## Notes
- Prefer strengthening the existing bootstrap path over adding a separate mandatory setup
  workflow unless the current docs cannot carry the change cleanly.
