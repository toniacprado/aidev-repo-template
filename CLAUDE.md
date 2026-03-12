See @AGENTS.md for the repository's canonical agent rules, @docs/TASK_MANAGEMENT.md for
persistent task tracking, @docs/CODEX_PROMPTING.md for request patterns, and
@docs/GUARDRAILS.md for safety boundaries.

# Claude Compatibility

This file exists as a compatibility shim inspired by Anthropic's `CLAUDE.md` memory
pattern. The repo's source of truth remains `AGENTS.md` plus the docs it references.

## Expectations
- Follow the same source-of-truth hierarchy as Codex.
- Keep task state visible in `work/`.
- Update prompts, evals, tests, and docs together when behavior changes.
- Treat model and guardrail changes as first-class repo changes.
