# Planning Prompt
*Version:* v0.5  
*Date:* 2026-03-24  
*Last reviewed:* 2026-03-24

Goal: propose the thinnest correct plan for a task before implementation expands.

Instructions:
- read the manifesto, charter, `docs/CONTEXT_ENGINEERING.md`, the Codex prompting guide,
  task management rules, and only the smallest relevant additional docs first
- restate the task, constraints, and assumptions
- identify which docs, prompts, evals, code, policies, and task artifacts should change
- prefer the simplest design that can satisfy the requirement
- call out verification needs and remaining unknowns
- if the task spans multiple steps, include how `work/` should be updated

Suggested output:
1. Assumptions
2. Proposed slices
3. Risks or open questions
4. Verification plan
5. Task tracking update
