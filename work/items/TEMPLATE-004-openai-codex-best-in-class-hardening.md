---
template: work_item
template_version: 0.4
template_date: 2026-03-11
template_last_reviewed: 2026-03-11
type: work_item
item_id: TEMPLATE-004
title: Align template with latest OpenAI Codex best practices for newbie onboarding and agentic reliability
status: done
owner: codex
updated: 2026-03-11
next_action: Run a real newcomer usability pass (first-time Codex user) and capture friction points as follow-up tasks.
blocked_on: none
---

# Align template with latest OpenAI Codex best practices for newbie onboarding and agentic reliability

## Summary
- Benchmark this template against current OpenAI Codex guidance, then close high-impact gaps that affect newcomer success and durable AI workflow quality.

## Acceptance Criteria
- Repo includes an explicit first-hour Codex workflow for new users.
- Prompt and eval directories include at least one concrete linked example, not only README guidance.
- Template contract checks require the new onboarding and sample assets.
- Core docs reference the new onboarding flow.
- Verification is rerun and reported.

## Progress Log
- 2026-03-11: task created from user request to benchmark against web/OpenAI sources and harden toward best-in-class.
- 2026-03-11: benchmarked repo workflow against current OpenAI Codex docs and identified onboarding, task-scope, and prompt/eval starter gaps.
- 2026-03-11: added `docs/CODEX_FIRST_HOUR.md` and linked it from key onboarding docs.
- 2026-03-11: expanded first-hour and environment docs with slash-command onboarding plus config-precedence/trusted-project guidance.
- 2026-03-11: added concrete linked starter assets in `prompts/` and `evals/`.
- 2026-03-11: expanded template contract checks to require the new onboarding and starter assets.
- 2026-03-11: reran lint and tests after hardening.

## Verification
- `./.venv/bin/ruff format .`
- `./.venv/bin/ruff check .`
- `./.venv/bin/pytest -q` (result: `4 passed, 1 skipped`; PowerShell-dependent bootstrap test skipped on this host)

## Next Action
- Run a real newcomer usability pass (first-time Codex user) and capture friction points as follow-up tasks.

## Notes
- Keep changes scoped to practical adoption quality for first-time Codex users.
