---
template: work_item
template_version: 0.4
template_date: 2026-03-11
template_last_reviewed: 2026-03-11
type: work_item
item_id: TEMPLATE-013
title: Harden the template around context engineering and just-in-time context loading
status: done
owner: codex
updated: 2026-03-24
next_action: Run a fresh `Use this template` trial and confirm a new user can follow the context-pack workflow without being told to read the whole repo.
blocked_on: none
---

# Harden the template around context engineering and just-in-time context loading

## Summary
- Tighten the template so it does not merely say "keep context in the repo," but also
  teaches users and agents to load the smallest high-signal context set for each task.
- Add explicit guidance for task-specific context packs, just-in-time retrieval, and
  compaction into repo-visible memory for long sessions.

## Acceptance Criteria
- A dedicated context-engineering guidance doc exists and is linked from the main
  onboarding and instruction surfaces.
- `AGENTS.md` and the main workflow docs recommend task-specific context packs instead of
  a broad preload-by-default reading list.
- The task-management rules explain how to compact long-session state back into `work/`.
- The template-maintenance prompt assets and newcomer smoke checks reflect the new
  context-engineering contract.
- Verification is rerun and reported.

## Progress Log
- 2026-03-24: task created after reviewing Anthropic's context-engineering article against
  the current repo instruction layer.
- 2026-03-24: added `docs/CONTEXT_ENGINEERING.md` and rewrote the default instruction flow
  around task-specific context packs, just-in-time retrieval, and repo-visible compaction.
- 2026-03-24: updated onboarding docs, shared prompt assets, bootstrap handoff outputs, and
  smoke checks so downstream repos inherit the tighter context-loading policy.
- 2026-03-24: reran the local maintenance suite successfully after the context-engineering
  hardening changes.

## Verification
- `./.venv/bin/ruff format .`
- `./.venv/bin/ruff check .`
- `./.venv/bin/pytest -q` (result: `9 passed, 1 skipped`)
- `./.venv/bin/python scripts/run_prompt_evals.py`
- `./.venv/bin/python scripts/newcomer_smoke_test.py`

## Next Action
- Run a fresh `Use this template` trial and confirm a new user can follow the context-pack
  workflow without being told to read the whole repo.

## Notes
- Preserve the repo's current bias toward single-agent execution; the main gap is context
  curation and compaction, not adding multi-agent complexity.
