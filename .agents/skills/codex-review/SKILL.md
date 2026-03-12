# Skill: codex-review

## Use when
- You need a correctness-first review of a proposed change.
- You want explicit findings for bugs, regressions, missing tests, and contract drift.

## Workflow
1. Read `AGENTS.md`, `docs/GUARDRAILS.md`, `docs/MODEL_POLICY.md`, and changed files.
2. Identify concrete findings first; include file references.
3. Prioritize issues by impact and likelihood.
4. Call out missing verification, missing evals, and missing task-state updates.
5. End with residual risk and smallest next fix.

## Output contract
- Findings are primary output.
- If no findings exist, say so explicitly and list residual risk/testing gaps.
