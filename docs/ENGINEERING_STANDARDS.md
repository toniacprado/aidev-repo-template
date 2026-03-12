# Engineering Standards
*Version:* v0.4  
*Date:* 2026-03-11  
*Last reviewed:* 2026-03-11

## Principles
- Keep it simple.
- Avoid speculative future-proofing.
- Prefer explicit behavior over cleverness.
- Keep functions, prompts, docs, and task files focused.
- Choose readable names.
- Handle errors with actionable messages.

## Source-of-truth hierarchy
1. `docs/PROJECT_MANIFESTO.md` and `docs/PROJECT_CHARTER.md`
2. `AGENTS.md`, `docs/AI_DEV_WORKFLOW.md`, `docs/CODEX_PROMPTING.md`,
   `docs/GUARDRAILS.md`, `docs/MODEL_POLICY.md`, `docs/TASK_MANAGEMENT.md`, and
   `docs/REPO_STRUCTURE.md`
3. `work/ACTIVE_TASKS.md`, `work/LEARNINGS.md`, and relevant files in `work/items/`
4. `.codex/` shared config and environment notes
5. `system/` contracts, prompts, templates, and policies
6. `prompts/` and `evals/` assets
7. `src/`, `tests/`, and `scripts/`
8. `runtime/` outputs

## OpenAI-aligned defaults
- Keep durable instructions in repo files instead of only in chat.
- Put stable prompt instructions and reusable examples before highly variable data when
  practical.
- Use explicit schemas or structured outputs when the model is producing
  machine-consumed data.
- Start with single-agent or workflow patterns unless evals show a clear need for
  more coordination.
- Prefer pass/fail, exact-match, or clear rubric-based evals over vibe-based review.
- Keep sandboxing and network permissions as narrow as the task allows.

## Change rules
- Behavior change: update docs and verification in the same diff.
- Prompt change: update linked eval coverage in the same diff.
- Model change: update `docs/MODEL_POLICY.md` or the relevant config and rerun evals.
- Multi-step task change: update `work/` with status, verification state, and next action.
- Guardrail or permission change: update `docs/GUARDRAILS.md`, `docs/DATA_POLICY.md`,
  and `system/policies/` if the risk model changes.
- Material Markdown guidance change: update version/date/review stamps.

## Repo hygiene checklist
- [ ] Did behavior or workflow change? Update docs and contracts too.
- [ ] Is the diff scoped to the current requirement?
- [ ] Are tests or evals covering the behavior or bug fix?
- [ ] Are quality gates run and reported?
- [ ] Are assumptions documented instead of left in chat memory?
- [ ] Can another contributor see the next step in `work/` without asking you?
- [ ] Are model and guardrail implications explicit?

## Testing guidance
- Add at least one happy-path test for new behavior.
- Add regression tests for important bugs.
- Prefer deterministic tests.
- For prompt or agent behavior, add representative eval cases plus relevant edge cases.
- For model changes, rerun the baseline eval set before changing defaults.
- For generated artifacts, prefer golden fixtures or explicit assertions.
