# Repo Structure
*Version:* v0.5  
*Date:* 2026-03-11  
*Last reviewed:* 2026-03-11

This template keeps human intent, AI contracts, task state, code, and generated outputs
in different places on purpose.

```text
repo/
  README.md
  CHANGELOG.md
  CONTRIBUTING.md
  AGENTS.md
  AGENTS.local.md.example
  AGENTS.override.md.example
  CLAUDE.md
  .codex/
  .agents/
  codex/
  .editorconfig
  .env.example
  .gitignore
  .pre-commit-config.yaml
  .github/
  docs/
  work/
  system/
  prompts/
  evals/
  src/
  tests/
  scripts/
  runtime/
```

## Boundary guidance
- `docs/` for intent, plans, decisions, onboarding, prompting guidance, and policy
- `work/` for the active task list, durable learnings, detailed work items, and next-step tracking
- `.codex/` for shared Codex configuration examples and environment notes
- `.agents/skills/` for reusable Codex skills that capture repeatable workflows
- `codex/rules/` for Codex execution-policy rule scaffolding
- `system/` for reusable schemas, templates, prompts, and policy assets
- `prompts/` for runtime prompt assets used by the product
- `evals/` for representative eval cases, rubrics, and grading notes
- `src/` for implementation
- `tests/` for deterministic behavior and regression coverage
- `scripts/` for idempotent repo utilities and automation helpers
- `runtime/` for generated, rebuildable artifacts

## Practical rules
- If a human or AI must repeatedly read it to stay aligned, it belongs in the repo.
- If work should survive beyond the current session, it belongs in `work/`.
- If Codex should share environment defaults with the team, document them in `.codex/`.
- If one subtree genuinely needs different rules, use `AGENTS.override.md` there.
- If the application sends it to a model at runtime, it belongs in `prompts/` or
  application code.
- If a model behavior matters, its evaluation must live in `evals/`.
- If an output can be regenerated, keep it out of canonical paths and put it in
  `runtime/`.
