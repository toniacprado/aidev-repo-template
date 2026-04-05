# Tech Stack Selection
*Version:* v0.6  
*Date:* 2026-03-29  
*Last reviewed:* 2026-03-29

This template is intentionally stack-agnostic for downstream projects, but every real
repo still needs one explicit moment where the inherited defaults stop being "the
stack" and the real product stack becomes canonical.

Do not stop at naming a language or framework. This file should also say how the repo
changes after that choice.

## Template maintenance stack
The template uses:
- Python 3.12 for lightweight maintenance utilities and tests
- `pytest` for template contract checks
- `ruff` for linting and formatting
- `pre-commit` for local hygiene

This is a template-maintenance choice, not a product-stack recommendation.

## Why this default won
- It is lightweight and easy to replace.
- It works well across Windows, macOS, and Linux.
- It lets the template verify itself without forcing an app framework choice.
- It is simple for Codex and humans to reason about.

## What downstream repos should decide here
Before real feature work speeds up, document:
- who will maintain the code
- required platforms and deployment targets
- privacy or compliance constraints
- expected product lifetime
- observability and debugging needs
- whether prompt or agent behavior is core product functionality

Then name the real operating stack:
- the main implementation language and framework per product surface
- the canonical package, build, or dependency tool
- the canonical setup, run, test, lint, and format commands
- the deployment path
- the eval and observability approach for AI features
- whether the inherited Python maintenance stack stays temporarily, is replaced, or is removed

## Adoption checklist after the decision
After choosing the stack, update the repo so the decision is operational instead of
remaining a note in one doc.

At minimum:
- rewrite `README.md` and `docs/START_HERE.md` so the default commands match the real stack
- update `AGENTS.md`, `docs/COMMAND_CONVENTIONS.md`, and CI or local scripts if the canonical commands changed
- replace or intentionally keep the inherited package/build files and explain that choice
- align `src/`, `tests/`, and any generated starter paths with the chosen stack
- record the first slice and its verification command in `work/`
- if Python maintenance tooling stays temporarily, mark the revisit trigger in `docs/DECISIONS.md`

Do not leave two competing default workflows in the repo without saying which one a
newcomer should actually follow.

## Decision criteria
Score any candidate stack against:
- delivery speed for the MVP
- maintainability for the actual team
- clarity of typing or validation
- testability
- deployment simplicity
- observability and debugging
- AI assistant friendliness

## Template rule
Keep the Python maintenance stack only if it is still helping you maintain the repo.
Replace or remove it as soon as the real project has a better native verification story.
