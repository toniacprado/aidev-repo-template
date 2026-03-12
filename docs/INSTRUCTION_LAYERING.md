# Instruction Layering
*Version:* v0.4  
*Date:* 2026-03-11  
*Last reviewed:* 2026-03-11

This file explains how to layer instructions without losing a single source of truth.

## Codex-first layering
Use these layers in order:
1. `AGENTS.md` for shared repo rules
2. topic docs in `docs/` for durable workflow, policy, and prompting guidance
3. nested `AGENTS.override.md` files only when a subtree genuinely needs different rules
4. user-level Codex config for personal preferences that should not affect the whole repo

## Claude-inspired ideas worth borrowing
Anthropic's `CLAUDE.md` workflow is good at two things:
- keeping tool-specific memory in repo files
- composing instructions from smaller files instead of one giant wall of text

This template borrows the idea, but keeps `AGENTS.md` as the canonical root for shared
rules and uses `CLAUDE.md` only as a compatibility shim.

## Personal preferences
Use `AGENTS.local.md.example` as inspiration for personal preferences, but do not treat
it as a shared source of truth.

Good uses:
- verbosity preferences
- preferred editor commands
- local fixture names or sample accounts
- personal no-go operations

## Scoped overrides
If one part of the repo has genuinely different rules, place an `AGENTS.override.md`
close to that subtree. Keep overrides short and explain why they differ.
Use `AGENTS.override.md.example` as the starting point.
