---
template: work_item
template_version: 0.4
template_date: 2026-03-11
template_last_reviewed: 2026-03-11
type: work_item
item_id: TEMPLATE-008
title: Launch template with neutral public branding and Codex-first positioning
status: done
owner: codex
updated: 2026-03-12
next_action: Run one throwaway `Use this template` bootstrap test from GitHub UI and capture first-user friction in TEMPLATE-009 if found.
blocked_on: none
---

# Launch template with neutral public branding and Codex-first positioning

## Summary
- Prepare this template for public GitHub release as `aidev-repo-template` while
  keeping Codex-first workflow guidance as the internal product focus.

## Acceptance Criteria
- Public-facing repo identity is neutral (`aidev-repo-template`).
- README title/description are updated and include explicit non-endorsement trademark disclaimer.
- Internal Codex-first workflow references remain intact.
- Full template verification gates pass.
- Local git repository is initialized with an initial baseline commit.
- GitHub publish configuration steps are executed where credentials/permissions allow.

## Progress Log
- 2026-03-12: task created from launch implementation request.
- 2026-03-12: updated public branding and metadata:
  - `README.md` title changed to neutral public name.
  - Added explicit non-endorsement/trademark disclaimer.
  - `pyproject.toml` package name changed to `aidev-repo-template`.
- 2026-03-12: initialized local git repository and created baseline commit.
- 2026-03-12: created and pushed public GitHub repo:
  - `https://github.com/toniacprado/aidev-repo-template`
- 2026-03-12: enabled template mode, set description/topics, configured branch protection,
  and published release tag:
  - tag: `v1.2.0`
  - release: `https://github.com/toniacprado/aidev-repo-template/releases/tag/v1.2.0`
- 2026-03-12: fixed a PowerShell parser issue discovered in CI (`$today:` -> `${today}:`)
  through PR #1 and confirmed green CI on `main`.

## Verification
- `./.venv/bin/ruff format .`
- `./.venv/bin/ruff check .`
- `./.venv/bin/pytest -q` (result: `9 passed, 1 skipped`)
- `./.venv/bin/python scripts/run_prompt_evals.py`
- `./.venv/bin/python scripts/newcomer_smoke_test.py`
- GitHub CI on `main` passed for:
  - `verify (ubuntu-latest)`
  - `verify (windows-latest)`

## Next Action
- Run one throwaway `Use this template` bootstrap test from GitHub UI and capture any
  first-user friction in `TEMPLATE-009`.

## Notes
- Keep `src/repo_template` module path unchanged to avoid unnecessary churn.
