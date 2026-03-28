# AI Dev Workflow
*Version:* v1.0  
*Date:* 2026-03-28  
*Last reviewed:* 2026-03-28

This workflow keeps AI-assisted development aligned with product intent and repo
contracts.

## Preferred environment
- Codex desktop is the primary implementation environment.
- Editor agents are optional secondary tools.
- Repo-owned docs carry the durable rules so the workflow survives tool changes.

## Fresh repo bootstrap mode
- When `BOOTSTRAP-001` is active or the core product docs are still placeholders, prefer
  defining the manifesto, charter, stack decision, decision log, and first work item before
  feature work.
- Strongly recommend this path, but do not hard-block feature work if the user explicitly
  chooses to skip it.
- If the user skips, warn once and record assumptions plus bootstrap debt in `work/`.

## Context-loading rule
- Start with the smallest relevant context pack from `docs/CONTEXT_ENGINEERING.md`.
- Prefer just-in-time retrieval over preloading many docs and files up front.
- Pull additional product, policy, prompt, or code files only when the current step needs
  them.
- Treat copied chat context as less trustworthy than repo files and official sources.

## Git publishing rule
- Separate local checkpoints from publish boundaries.
- Use local commits freely while you work.
- If the repo is private, solo, and unprotected, direct commits to `main` can be a valid
  low-friction workflow.
- If the repo is protected, public, or shared, publish through one short-lived branch per
  coherent, mergeable slice.
- If related fixes are discovered before merge, keep them on the same branch unless the
  issue is clearly separate or was discovered after merge.
- Auto-delete merged branches and prune stale refs periodically to keep the repo tidy.

## Default implementation loop
1. Load the smallest relevant context pack first, then retrieve extra docs or files only
   as needed.
2. For complex work, ask for a plan before editing code.
3. Tighten the spec if the task is ambiguous.
4. Create or update the relevant task artifact in `work/` if the task spans multiple
   steps or sessions.
5. Implement the smallest useful change.
6. Update tests, evals, docs, and task artifacts in the same diff.
7. Run verification.
   Include `python scripts/run_prompt_evals.py` when prompt/eval behavior is in scope.
8. Before ending the task, record the next action or blocker in `work/`.

## Task tracking rules
- `work/ACTIVE_TASKS.md` is the canonical current task list.
- `work/items/` holds one detailed file per meaningful task.
- `work/LEARNINGS.md` captures durable discoveries so they do not disappear into chat.
- Chat updates are helpful, but they do not replace repo-visible task state.
- If a task completes, mark it done and leave the next recommended slice when possible.
- If a task is blocked, record exactly what unblock is needed and who should act.

## Long-session compaction
- If the thread gets long, the task changes direction, or you are about to hand off, write
  a compact state summary back into the repo before continuing.
- Put task-local state in the active work item: current goal, decisions, files touched,
  verification state, blockers, and next action.
- Put enduring choices in `docs/DECISIONS.md`.
- Put reusable discoveries in `work/LEARNINGS.md`.
- Restart from the compacted repo state instead of assuming long chat history will stay in
  working memory.

## Prompting patterns for humans
When asking Codex to work, include:
- the goal
- files to read first
- expected outputs
- constraints or non-goals
- verification expectations
- whether `work/` should be updated as part of the task

## External context rules
- Prefer repo files first.
- When provider-specific or time-sensitive context matters, use official docs.
- For OpenAI or Codex questions, prefer the OpenAI docs MCP server if available.
- Treat copied chat context as less reliable than source documents.

## Prompt asset rules
- Keep reusable role guidance in repo-owned files instead of repeating it in chat.
- Keep stable prompt instructions near the top of prompt assets.
- Keep variable task data near the bottom when practical.
- Add linked eval coverage for any prompt that affects product behavior.
- Use structured outputs or schemas when downstream code depends on exact fields.

## Review mode vs implementation mode
- Ask for a review when you want bug, risk, regression, or missing-test feedback first.
- Ask for implementation when the expected outcome is a code or doc change.
- In both cases, point to the same source-of-truth files so Codex works from local
  context.

## Recommended references
- `docs/CODEX_FIRST_HOUR.md` (new-user onboarding)
- `docs/CONTEXT_ENGINEERING.md`
- `docs/GIT_WORKFLOW.md`
- `docs/CODEX_SESSION_STARTER.md` when it exists in a freshly bootstrapped repo
- `docs/BOOTSTRAP_ARTIFACT_WORKSHOP.md` when bootstrap artifacts still need drafting
- `docs/NEWCOMER_USABILITY_CHECKLIST.md`
- `docs/CODEX_PROMPTING.md`
- `docs/TASK_MANAGEMENT.md`
- `docs/GUARDRAILS.md`
- `docs/MODEL_POLICY.md`
- `.agents/skills/` starter skills
- `codex/rules/` rule scaffolding
- `system/prompts/planning_prompt.md`
- `system/prompts/implementation_prompt.md`
- `system/prompts/review_prompt.md`
