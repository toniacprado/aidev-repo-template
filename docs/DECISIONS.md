# Decisions Log
*Version:* v0.8  
*Date:* 2026-03-28  
*Last reviewed:* 2026-03-28

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

### 2026-03-23 - Bootstrap should generate project-facing handoff docs
- Decision: bootstrap now rewrites the landing docs into project-draft content and
  generates `docs/BOOTSTRAP_NEXT_STEPS.md` instead of relying on template narrative plus
  a scattered checklist.
- Why: first-time users need the generated repo to say "here is your draft project and
  the next steps" immediately, especially on GitHub web before any chat guidance exists.
- Alternatives considered: keeping the existing docs and relying on manual checklist
  navigation, or adding a second required starter script.
- Consequences: Python and PowerShell bootstrap paths must stay aligned, and tests must
  assert the generated handoff behavior instead of only structural cleanup.
- Revisit when: real template-user trials show the generated guide is still too indirect
  or a more interactive bootstrap flow is justified.

### 2026-03-23 - Bootstrap should generate a Codex session starter, not only docs
- Decision: fresh repos now generate `docs/CODEX_SESSION_STARTER.md` and
  `docs/BOOTSTRAP_ARTIFACT_WORKSHOP.md`, and the inherited instruction layer strongly
  recommends bootstrap mode while still allowing an explicit skip.
- Why: most users will otherwise treat Codex like a one-shot prompt box and jump to
  feature work before the repo has durable product context.
- Alternatives considered: leaving the workflow implied in docs only, or hard-blocking
  feature work until all bootstrap artifacts are complete.
- Consequences: bootstrap now resets `docs/DECISIONS.md`, onboarding docs must teach the
  Codex handoff explicitly, and tests must verify the session-starter path.
- Revisit when: real newcomer trials show the generated prompts are still too indirect
  or too verbose.

### 2026-03-24 - Default to task-specific context packs and repo-visible compaction
- Decision: the template should default to task-specific context packs, just-in-time
  retrieval, and compaction of long-session state back into repo files instead of broad
  preloading plus chat-dependent memory.
- Why: context is a finite attention budget; loading too much at once creates noise,
  weakens focus, and pushes durable state back into chat history.
- Alternatives considered: keeping the long ordered read list as the default, or relying
  on ad hoc chat summaries without repo-visible compaction rules.
- Consequences: onboarding, bootstrap handoff docs, prompt assets, and smoke checks need
  to teach `docs/CONTEXT_ENGINEERING.md`, and `work/` becomes the reset point for long
  sessions.
- Revisit when: real template-user trials show the context packs are too heavy, too light,
  or unnecessary because tool behavior changes materially.

### 2026-03-28 - Git workflow should be risk-based, not branch-heavy by default
- Decision: the template should separate local checkpoints from publish boundaries and teach
  short-lived PR branches only when repo governance makes them useful.
- Why: blanket branch-per-task advice creates friction in simple solo repos, but direct-to-main
  is inappropriate in protected, public, or shared repos.
- Alternatives considered: always branch for every task, or treat direct-to-main as the
  default everywhere.
- Consequences: onboarding docs need to distinguish private/solo/unprotected repos from
  protected/public/shared repos, and fresh bootstrapped projects need a visible Git workflow
  policy instead of ad hoc chat advice.
- Revisit when: Codex tooling or common repo protection defaults change materially.
