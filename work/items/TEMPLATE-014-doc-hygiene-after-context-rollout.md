---
template: work_item
template_version: 0.4
template_date: 2026-03-11
template_last_reviewed: 2026-03-11
type: work_item
item_id: TEMPLATE-014
title: Clean up doc hygiene after the context-engineering rollout
status: done
owner: codex
updated: 2026-03-24
next_action: Keep the newcomer smoke checks covering the amended docs and do a fresh template-user trial to confirm no stale onboarding references remain.
blocked_on: none
---

# Clean up doc hygiene after the context-engineering rollout

## Summary
- Fix the README metadata gap and align the remaining onboarding and maintenance docs that
  still describe the older preload-heavy flow or still carry stale review stamps.
- Add lightweight smoke-check coverage for the docs that should now point at context packs
  and compaction guidance.

## Acceptance Criteria
- `README.md` metadata and bootstrap instructions reflect the current context-pack workflow.
- Secondary onboarding and maintenance docs that should mention `docs/CONTEXT_ENGINEERING.md`
  or compaction guidance are updated.
- Repo-visible task state and changelog reflect the follow-up cleanup.
- Smoke checks cover the most important amended docs.
- Verification is rerun and reported.

## Progress Log
- 2026-03-24: task created after noticing the merged README content had current substance but
  stale metadata and after identifying adjacent docs that still reflected the older flow.
- 2026-03-24: updated README metadata and bootstrap wording, aligned the bootstrap checklist,
  human guide, instruction layering, template maintenance doc, scripts README, changelog, and
  learnings with the context-pack workflow.
- 2026-03-24: extended the newcomer smoke checks to cover the bootstrap checklist and human
  guide so similar drift is caught earlier next time.
- 2026-03-24: reran the local maintenance suite successfully.

## Verification
- `./.venv/bin/ruff format .`
- `./.venv/bin/ruff check .`
- `./.venv/bin/pytest -q` (result: `9 passed, 1 skipped`)
- `./.venv/bin/python scripts/run_prompt_evals.py`
- `./.venv/bin/python scripts/newcomer_smoke_test.py`

## Next Action
- Keep the newcomer smoke checks covering the amended docs and do a fresh template-user trial
  to confirm no stale onboarding references remain.

## Notes
- This is a hygiene follow-up, not a new workflow redesign; keep the changes narrowly scoped
  to drift correction and coverage.
