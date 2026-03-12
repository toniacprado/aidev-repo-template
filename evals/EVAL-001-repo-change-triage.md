---
template: eval_case
template_version: 0.2
template_date: 2026-03-11
template_last_reviewed: 2026-03-11
type: eval_case
eval_id: EVAL-001
title: Repo change triage catches missing verification
status: active
prompt_ids:
  - PROMPT-001
grader_type: pass_fail
---

# Repo change triage catches missing verification

## Intent
- Verify that the triage prompt flags high-risk missing verification when behavior changed.

## Inputs
- Changed files:
  - `src/payments/apply_discount.py`
  - `tests/test_discounts.py`
  - `docs/ENGINEERING_STANDARDS.md`
- Claimed behavior change:
  - Discount cap logic changed from 20% to 30% for enterprise plans.
- Verification output:
  - `ruff check .` passed
  - tests not run

## Expected Result
- Output includes at least one high-severity finding about missing tests for behavior change.
- `verification.status` is not reported as fully complete.
- `next_actions` includes running targeted tests before merge.

## Failure Signals
- Marks verification complete despite tests not run.
- Omits regression risk for pricing logic change.
- Returns non-JSON output or schema-incompatible JSON.

## Notes
- This case is intentionally simple and deterministic for template onboarding.
