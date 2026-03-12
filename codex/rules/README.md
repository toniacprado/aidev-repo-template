# Codex Rules Scaffolding
*Version:* v0.1  
*Date:* 2026-03-11  
*Last reviewed:* 2026-03-11

Use this directory to store project-scoped Codex execution-policy rules.

## How to use
- Start from `default.rules.example`.
- Copy it to `default.rules` when your team is ready to enforce the rules.
- Validate rule behavior with:
  - `codex execpolicy check --rule-file codex/rules/default.rules`

## Rule intent
- Block dangerous command prefixes.
- Require a prompt for publishing or externally visible operations.
- Keep rules narrow, reviewable, and easy to justify.
