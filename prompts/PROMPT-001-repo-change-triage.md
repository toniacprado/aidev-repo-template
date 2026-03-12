---
template: prompt_asset
template_version: 0.2
template_date: 2026-03-11
template_last_reviewed: 2026-03-11
type: prompt_asset
prompt_id: PROMPT-001
title: Repo change triage summary
owner: template-maintainer
status: active
model_scope: general
linked_evals:
  - EVAL-001
---

# Repo change triage summary

## Goal
- Produce a concise, risk-first summary of a proposed code or docs change.

## Inputs
- A list of changed files.
- A short description of the intended behavior change.
- Optional verification output (tests, lint, evals).

## Constraints
- Prioritize correctness and regression risk over style.
- Flag missing verification clearly.
- Keep recommendations scoped to the stated behavior.
- Do not invent file paths or test results.

## Output Contract
- Return JSON with this shape:
  - `summary`: short text of what changed
  - `findings`: array of `{severity, file, issue, recommendation}`
  - `verification`: `{status, evidence, gaps}`
  - `next_actions`: ordered list of concrete follow-ups

## Eval Link
- `evals/EVAL-001-repo-change-triage.md`

## Change Notes
- 2026-03-11: initial concrete prompt example added to template.
