# Guardrails
*Version:* v0.4  
*Date:* 2026-03-11  
*Last reviewed:* 2026-03-11

This file defines the operational guardrails for AI-assisted work in the repo.

## Core rule
Keep the agent as capable as needed, but no more capable than the task requires.

## Default boundaries
- read access is broadly allowed inside the repo
- writes should stay scoped to the task and the workspace
- destructive actions require explicit human approval
- external network use should stay off by default and be justified when enabled
- model or automation changes that affect user-facing behavior require reviewable docs
  and eval updates

## Human-in-the-loop triggers
Require explicit human review before:
- deleting or overwriting important data
- broad dependency or environment changes
- enabling wider network access
- changing model defaults for user-facing behavior
- automated external sends or publication
- any work touching sensitive data or regulated workflows

## Runtime AI safety reminders
If the downstream product uses models directly:
- constrain tools and permissions as tightly as possible
- validate model outputs before using them as commands or writes
- keep structured outputs explicit when code depends on exact fields
- log enough context to debug failures without leaking secrets
- plan for recovery when the model is wrong or unavailable

## Repo-level policy assets
- `docs/DATA_POLICY.md`
- `docs/MODEL_POLICY.md`
- `system/policies/tool_risk_matrix.md`
- `system/automations/policy.md`
- `system/automations/approvals.md`
