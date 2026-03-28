---
template: work_item
template_version: 0.4
template_date: 2026-03-11
template_last_reviewed: 2026-03-11
type: work_item
item_id: TEMPLATE-015
title: Add a risk-based Git workflow policy for Codex-first projects
status: done
owner: codex
updated: 2026-03-28
next_action: Validate the policy in one fresh `Use this template` run and confirm a newcomer can choose a publish path without unnecessary branch churn.
blocked_on: none
---

# Add a risk-based Git workflow policy for Codex-first projects

## Summary
- Convert the recent branching and PR friction into an explicit template rule instead of
  leaving it as an oral tradition from this session.
- Teach users to separate local checkpoints from publish boundaries and to choose branches
  based on repo governance, not habit.

## Acceptance Criteria
- A dedicated Git workflow guidance doc exists and is linked from the main onboarding and
  workflow docs.
- The template explicitly distinguishes private/solo/unprotected repos from
  protected/public/shared repos.
- The bootstrap handoff docs in fresh downstream repos mention the Git workflow guidance.
- Smoke checks cover the new Git workflow doc and at least one or two key links to it.
- Verification is rerun and reported.

## Progress Log
- 2026-03-28: task created after reviewing whether repeated short-lived branches were the
  right default and concluding the template needs a context-sensitive policy instead of a
  blanket branch-per-task rule.
- 2026-03-28: added `docs/GIT_WORKFLOW.md` and updated the onboarding, workflow, and
  bootstrap handoff docs to separate local checkpoints from publish boundaries.
- 2026-03-28: updated the bootstrap tests and newcomer smoke checks so the Git workflow
  guidance is covered in both the template docs and fresh downstream repos.
- 2026-03-28: reran the local maintenance suite successfully.

## Verification
- `./.venv/bin/ruff format .`
- `./.venv/bin/ruff check .`
- `./.venv/bin/pytest -q` (result: `9 passed, 1 skipped`)
- `./.venv/bin/python scripts/run_prompt_evals.py`
- `./.venv/bin/python scripts/newcomer_smoke_test.py`

## Next Action
- Validate the policy in one fresh `Use this template` run and confirm a newcomer can
  choose a publish path without unnecessary branch churn.

## Notes
- The goal is not to force PR branches in all repos. The goal is to teach
  "checkpoint always, branch when publishing across a review/protection boundary."
