# Decisions Log
*Version:* v0.4  
*Date:* 2026-03-11  
*Last reviewed:* 2026-03-11

Use this file to record meaningful product, architecture, or workflow decisions.

### 2026-03-11 - Codex-first but repo-owned workflow
- Decision: Codex desktop is the primary AI environment, but durable instructions must
  live in repo files instead of chat-only memory.
- Why: This keeps the workflow portable, reviewable, and easier for humans to audit.
- Alternatives considered: tool-specific private prompts only, or no AI-specific repo
  contracts at all.
- Consequences: `AGENTS.md`, `docs/`, and `system/` remain first-class project assets.
- Revisit when: the team's primary AI environment changes or the instruction split no
  longer feels useful.

### 2026-03-11 - Prompt and eval assets are versioned in the repo
- Decision: Runtime prompts live in `prompts/` and model behavior coverage lives in
  `evals/`.
- Why: Important AI behavior should be diffable, reviewable, and testable.
- Alternatives considered: storing prompts in code only, or relying on chat history.
- Consequences: prompt changes should usually travel with eval changes.
- Revisit when: a downstream project has a stronger domain-specific convention.

### 2026-03-11 - The template ships with lightweight Python verification
- Decision: The template uses Python 3.12, `pytest`, and `ruff` for maintenance checks.
- Why: The tooling is lightweight, cross-platform, and easy to replace.
- Alternatives considered: shipping no verification, or choosing a heavier framework.
- Consequences: downstream repos must confirm whether to keep or replace these defaults.
- Revisit when: a simpler and equally portable verification stack becomes preferable.

### 2026-03-11 - Task state must survive beyond chat
- Decision: `work/` is the canonical location for active tasks, detailed work items,
  and durable learnings.
- Why: Multi-step work should not depend on a human reconstructing the next step from
  chat history.
- Alternatives considered: chat-only planning, or an external tracker with no repo link.
- Consequences: meaningful work now requires repo-visible status and next-action updates.
- Revisit when: the team adopts a stronger external planning system that stays in sync.

### 2026-03-11 - Shared Codex config and explicit guardrails are first-class repo assets
- Decision: the template includes `.codex/` guidance plus dedicated model and guardrail
  policy docs.
- Why: OpenAI guidance emphasizes clear environment setup, scoped permissions, and evals
  around model behavior changes.
- Alternatives considered: relying on user-specific local config only.
- Consequences: teams can review shared AI operating choices in the repo.
- Revisit when: Codex configuration and policy mechanisms change materially.
