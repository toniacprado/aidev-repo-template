# Project Charter
*Version:* v0.3  
*Date:* 2026-03-12  
*Last reviewed:* 2026-03-12

## Scope
### In scope
- a reusable repo layout for Codex-first greenfield projects
- human-facing guidance for planning, implementation, review, and handoff
- versioned prompt, eval, schema, and automation scaffolding
- lightweight verification that proves the template is internally consistent

### Out of scope for now
- shipping full framework starter apps for every stack
- bundling deployment infrastructure for every cloud or hosting provider
- automating complex multi-agent orchestration by default

## Primary users
- solo builders or small teams starting a new project with Codex as a daily tool
- teams that want AI-friendly repos without sacrificing human readability

## Success metrics
- a new project can be bootstrapped from this template in under one working session
- contributors can identify the repo's source of truth in under 10 minutes
- prompt or workflow changes are reflected in docs and verification, not only chat

## Risks
- the template becomes too generic and stops making useful decisions
- the lightweight Python verification defaults are mistaken for the downstream product
  stack
- docs drift away from how real contributors actually use the repo

## Delivery approach
- Start with the smallest useful template that carries strong boundaries.
- Prefer durable repo conventions over one-off chat advice.
- Keep docs, prompts, evals, and tests evolving together.

## Next in fast path
Open `AGENTS.md`, then `docs/AI_DEV_WORKFLOW.md`.
