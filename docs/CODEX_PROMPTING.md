# Codex Prompting
*Version:* v0.6  
*Date:* 2026-03-11  
*Last reviewed:* 2026-03-11

This file captures the prompting patterns that make Codex more reliable in practice.

## Core prompt shape
For most tasks, structure the request like this:
- Goal: what outcome you want
- Context: which files or decisions matter
- Constraints: what not to change, risk boundaries, or stack limits
- Done when: what success looks like and how to verify it

This follows current OpenAI guidance to make requests concrete, scoped, and easy to
verify.

## Plan first for complex work
If the task is ambiguous, risky, or large, ask for a plan before implementation.
Examples:
- propose the smallest correct slice
- identify files to change first
- list risks and unknowns
- say what tests or evals will prove it worked

## Keep task slices small
Codex is strongest when prompts ask for one focused, reviewable slice instead of a broad
multi-feature rewrite.

Practical default:
- one task that can usually be completed and verified in one focused session
- explicit non-goals to avoid scope creep
- clear verification target before editing starts

## Point Codex at the repo, not chat history
Good prompts usually name the files Codex should read first. Prefer:
- `AGENTS.md`
- the relevant docs in `docs/`
- the active queue in `work/ACTIVE_TASKS.md`
- the detailed work item in `work/items/`
- the prompt or eval files involved

## Use issue-style prompts
Treat your prompt like a well-written issue or task ticket.
Include:
- the current problem
- the target behavior
- explicit non-goals
- relevant files
- expected verification

## Use MCP and official docs when context is external
When the repo is not enough:
- use official docs instead of copied summaries
- prefer MCP servers when they provide trustworthy source access
- for OpenAI or Codex questions, prefer the OpenAI docs MCP server if available

## Prompt asset design for runtime prompts
When the product itself sends prompts to models:
- keep stable instructions near the top
- keep reusable examples above highly variable inputs when practical
- keep machine-consumed output contracts explicit
- keep prompt changes linked to eval changes
- run `python scripts/run_prompt_evals.py` when changing prompt/eval assets

## Recommended prompt templates
### Planning request
```text
Goal: Propose the smallest safe implementation plan.
Context: Read AGENTS.md, docs/PROJECT_CHARTER.md, docs/CODEX_PROMPTING.md,
and work/ACTIVE_TASKS.md.
Constraints: Keep the change minimal. Do not broaden scope.
Done when: There is a clear plan, risks are listed, and the work tracker update is defined.
```

### Implementation request
```text
Goal: Implement the next task slice.
Context: Read AGENTS.md, docs/TASK_MANAGEMENT.md, the relevant work item, and the target files.
Constraints: Keep the diff scoped. Update docs, tests, and work tracking in the same diff.
Done when: The change is implemented, verification is reported, and `work/` shows the next step.
```

### Review request
```text
Goal: Review this change for bugs, regressions, missing tests, and contract drift.
Context: Read AGENTS.md, docs/GUARDRAILS.md, docs/MODEL_POLICY.md, and the changed files.
Constraints: Prioritize correctness over style.
Done when: Findings are listed with file references and missing verification is called out.
```
