# Active Tasks
*Version:* v2.7  
*Date:* 2026-03-28  
*Last reviewed:* 2026-03-28

This file is the canonical current task list for the repo.

## Active
| ID | Title | Status | Owner | Next action | Last updated |
| --- | --- | --- | --- | --- | --- |
| TEMPLATE-015 | Add a risk-based Git workflow policy for Codex-first projects | done | codex | Validate the policy in one fresh `Use this template` run and confirm a newcomer can choose a publish path without unnecessary branch churn | 2026-03-28 |
| TEMPLATE-014 | Clean up doc hygiene after the context-engineering rollout | done | codex | Keep the newcomer smoke checks covering the amended docs and do a fresh template-user trial to confirm no stale onboarding references remain | 2026-03-24 |
| TEMPLATE-013 | Harden the template around context engineering and just-in-time context loading | done | codex | Run a fresh `Use this template` trial and confirm a new user can follow the context-pack workflow without being told to read the whole repo | 2026-03-24 |
| TEMPLATE-012 | Fix ship-blocking bootstrap handoff gaps before template trial | done | codex | Wait for the repaired branch CI to pass, then run a fresh GitHub `Use this template` trial and verify the generated session starter rewrites the landing docs cleanly | 2026-03-23 |
| TEMPLATE-011 | Add guided Codex bootstrap takeover with strong recommendations and skip path | done | codex | Run one fresh GitHub `Use this template` flow and confirm a new user can hand the repo to Codex with the generated session starter alone | 2026-03-23 |
| TEMPLATE-010 | Make post-bootstrap onboarding project-facing and explicit for first-time users | done | codex | Run one fresh GitHub `Use this template` flow and confirm the generated handoff docs are clear without extra chat guidance | 2026-03-23 |
| TEMPLATE-009 | Reduce onboarding friction and harden release/CI reliability | done | codex | Run one throwaway `Use this template` flow and measure newcomer completion time | 2026-03-12 |
| TEMPLATE-008 | Launch template with neutral public branding and Codex-first positioning | done | codex | Run one throwaway `Use this template` bootstrap test and capture friction as TEMPLATE-009 | 2026-03-12 |
| TEMPLATE-007 | Normalize docs and maintenance commands for OS-agnostic usage | done | codex | Run external newcomer passes on Linux and Windows to validate command conventions | 2026-03-12 |
| TEMPLATE-006 | Run first-time user trial and harden cross-platform onboarding | done | codex | Run one external newcomer trial and capture friction as TEMPLATE-007 | 2026-03-11 |
| TEMPLATE-005 | Implement best-in-class gaps: eval runner, rules/skills scaffolding, newcomer harness, and issue templates | done | codex | Run a real first-time user trial and convert friction into follow-up tasks | 2026-03-11 |
| TEMPLATE-004 | Align template with latest OpenAI Codex best practices for newbie onboarding and agentic reliability | done | codex | Run a newcomer usability pass and capture friction as follow-up tasks | 2026-03-11 |
| TEMPLATE-003 | Harden template bootstrap and verification after repo inventory | done | codex | Do one final bootstrap smoke test on a machine with PowerShell before publishing as a GitHub template | 2026-03-11 |
| TEMPLATE-001 | Harden the repo template to current OpenAI-aligned Codex best practices | done | codex | Bootstrap a real project from this template or keep iterating on optional variants | 2026-03-11 |
| TEMPLATE-002 | Make the repo template-ready for cloning and bootstrap | done | codex | Publish as a GitHub template repo, confirm or change the MIT license, and bootstrap a real project from it | 2026-03-11 |

## Rules
- Update status and next action before ending meaningful work.
- Link to a detailed file in `work/items/` when a task needs history or acceptance criteria.
- Capture durable discoveries in `work/LEARNINGS.md` when they should influence future work.
- Remove or archive stale rows once the task is truly done.
