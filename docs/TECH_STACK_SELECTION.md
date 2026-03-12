# Tech Stack Selection
*Version:* v0.5  
*Date:* 2026-03-11  
*Last reviewed:* 2026-03-11

This template is intentionally stack-agnostic for downstream projects, but the template
itself still needs a maintenance stack for verification.

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

## How downstream repos should use this file
Before real feature work speeds up, document:
- who will maintain the code
- required platforms and deployment targets
- privacy or compliance constraints
- expected product lifetime
- observability and debugging needs
- whether prompt or agent behavior is core product functionality

Then decide:
- the main implementation language per service
- the primary test runner
- the packaging or build tool
- the deployment path
- the eval and observability approach for AI features

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
Keep the Python maintenance stack only if it is helping you maintain the template.
Replace or remove it as soon as the real project has a better verification story.
