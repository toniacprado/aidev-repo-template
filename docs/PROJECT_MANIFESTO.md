# Project Manifesto
*Version:* v0.3  
*Date:* 2026-03-12  
*Last reviewed:* 2026-03-12

This repository is itself a product: a Codex-first template for starting new projects
without losing human clarity or engineering discipline.

---

## Why this exists
New repositories often fail early because the team starts writing code before it writes
down intent, scope, and source-of-truth boundaries. AI assistants make that gap more
visible: when the repo is vague, the model guesses.

This template exists to make that failure mode less likely.

## The promise
This template should help teams:
- onboard humans and Codex from the same local docs
- treat prompts and evals like versioned product assets
- ship early work with explicit scope, verification, and non-goals

## The non-negotiables
- Repo-owned docs outrank hidden chat context.
- Generated outputs never become canonical by accident.
- Prompt changes and eval changes stay linked.
- Verification is a real workflow, not a ceremonial note in the README.

## The anti-goals
This project is not trying to become:
- a giant enterprise process manual
- a framework-specific boilerplate that forces one stack on every team
- a default multi-agent playground with complexity before evidence

## What good looks like
Within the first day of adopting this template, success should feel like:
- the team can explain the repo's source of truth without guessing
- the first real feature lands with docs, code, and verification aligned
- Codex can work effectively after reading repo files, not long chat history

## Constraints
- The template must stay small enough to copy into a new repo without friction.
- Defaults must be cross-platform and easy to replace.
- OpenAI and Codex best practices should shape the workflow without hard-coding one
  provider into downstream product code.

## Living docs that implement this intent
- `docs/PROJECT_CHARTER.md`
- `docs/TECH_STACK_SELECTION.md`
- `docs/ENGINEERING_STANDARDS.md`
- `docs/REPO_STRUCTURE.md`

When implementation feels lost, return here.

## Next in fast path
Open `docs/PROJECT_CHARTER.md`.
