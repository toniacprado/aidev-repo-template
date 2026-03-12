# AGENTS.md - Rules for AI Coding Agents (Codex-first)
*Version:* v1.0  
*Date:* 2026-03-12  
*Last reviewed:* 2026-03-12

This repository is designed for Codex-first development. Repository-level instructions
live here so project norms survive tool changes and can be read directly from disk.

---

## North Star
Use the repo itself as the durable source of truth.

Operating model:
- `docs/` defines product intent, scope, human workflow, prompting guidance, and policy.
- `work/` stores active task state, learnings, progress history, and explicit next actions.
- `.codex/` stores shared Codex configuration examples and local-environment guidance.
- `.agents/skills/` stores reusable Codex skills for repeatable workflows.
- `codex/rules/` stores Codex execution-policy rule scaffolding.
- `system/` defines reusable schemas, templates, prompts, and policies.
- `prompts/` stores runtime prompt assets that the product uses.
- `evals/` stores prompt or agent evaluation cases and rubrics.
- `src/` stores implementation code.
- `tests/` stores deterministic verification.
- `runtime/` stores rebuildable outputs and is never canonical.

When sources conflict, prefer:
1. `docs/PROJECT_MANIFESTO.md`
2. `docs/PROJECT_CHARTER.md`
3. `docs/ENGINEERING_STANDARDS.md`
4. `docs/GUARDRAILS.md`
5. `docs/MODEL_POLICY.md`
6. `docs/TASK_MANAGEMENT.md`
7. `docs/REPO_STRUCTURE.md`
8. task-specific contracts in `work/`, `.codex/`, `system/`, `prompts/`, and `evals/`

---

## Read These First (in order)
1. `docs/PROJECT_MANIFESTO.md`
2. `docs/PROJECT_CHARTER.md`
3. `docs/AI_DEV_WORKFLOW.md`
4. `docs/CODEX_FIRST_HOUR.md` (especially for newcomers)
5. `docs/CODEX_PROMPTING.md`
6. `docs/TASK_MANAGEMENT.md`
7. `docs/GUARDRAILS.md`
8. `docs/MODEL_POLICY.md`
9. `docs/CODEX_ENVIRONMENT.md`
10. `docs/TEMPLATE_MAINTENANCE.md`
11. `docs/TECH_STACK_SELECTION.md`
12. `docs/ENGINEERING_STANDARDS.md`
13. `docs/REPO_STRUCTURE.md`
14. relevant files in `work/`, `.codex/`, `.agents/skills/`, `codex/rules/`,
    `system/schemas/`, `system/templates/`, and `system/prompts/`
15. `prompts/README.md` and `evals/README.md` when working on model behavior

If any canonical file is missing or empty, create a meaningful placeholder before
implementing behavior.

---

## Product & planning rules
- Respect the manifesto and charter before optimizing implementation details.
- If the task is ambiguous, improve the spec first instead of guessing.
- Preserve explicit non-goals so the repo does not drift into side quests.
- Record meaningful product, architecture, or workflow decisions in `docs/DECISIONS.md`.
- If a task spans multiple steps or sessions, create or update its work item in `work/`
  before doing substantial implementation.
- Before ending work, update the relevant task artifact with current status,
  verification state, blockers, learnings, and the next recommended action.

---

## Engineering rules
- Prefer the simplest readable approach that works.
- Avoid future-scope knobs unless the current task needs them.
- Keep modules focused and split files when it improves clarity.
- Use intention-revealing names.
- Handle errors with user-actionable messages.
- Keep write paths idempotent where possible.
- Update docs, prompts, evals, and contracts in the same diff when behavior changes.
- Do not leave important plan state only in chat when the work should survive the session.
- Never leave zero-byte canonical docs, schemas, templates, prompts, or policies.
- When materially editing Markdown guidance files, update version/date/review stamps.

---

## Codex-specific rules
- Use the prompt structure in `docs/CODEX_PROMPTING.md`: goal, context, constraints,
  and done-when.
- Plan first for complex or ambiguous tasks before changing code.
- Prefer small slices that are realistically finishable and verifiable in one focused session.
- When work depends on external changing context, prefer MCP or official docs over pasted
  summaries.
- For OpenAI or Codex usage questions, prefer the OpenAI developer docs MCP server when
  it is available; otherwise use official OpenAI docs.
- Keep shared Codex config conservative: `on-request` approvals, `workspace-write`, and
  network off by default unless the task clearly needs more.
- Treat the Python tooling in this repo as template-maintenance-only, not as a product-stack assumption.
- Use nested `AGENTS.override.md` files for genuinely different rules in subtrees.

---

## AI workflow rules
- Keep durable instructions in repo files, not only in chat history.
- Prefer single-agent designs until evals justify extra coordination complexity.
- Version prompt assets in `prompts/` and link them to eval coverage in `evals/`.
- Use explicit schemas or structured outputs when model output is machine-consumed.
- Keep stable instructions and reusable examples ahead of variable data in prompt assets
  when practical.
- Apply the guardrails in `docs/GUARDRAILS.md` and the model rules in `docs/MODEL_POLICY.md`.
- Ask for approval before destructive actions or external sends.
- For non-trivial tasks, leave a repo-visible next step in `work/` before considering
  the task handoff complete.

---

## Key commands
These are maintenance commands for the template itself, not a claim about the downstream
project stack.

- Bootstrap (cross-platform): `python scripts/bootstrap_new_project.py --project-name "Your Project"` (or `python3` if needed before venv activation on macOS/Linux)
- Setup (macOS/Linux): `python3 -m venv .venv`, `source .venv/bin/activate`, `python -m pip install --upgrade pip`, then `python -m pip install -e ".[dev]"`
- Setup (Windows PowerShell): `python -m venv .venv`, `.\.venv\Scripts\Activate.ps1`, `python -m pip install --upgrade pip`, then `python -m pip install -e ".[dev]"`
- Format: `ruff format .`
- Lint: `ruff check .`
- Tests: `pytest -q`
- Prompt eval checks: `python scripts/run_prompt_evals.py`
- Newcomer smoke checks: `python scripts/newcomer_smoke_test.py`
- Read the active queue: open `work/ACTIVE_TASKS.md`
- Command conventions: read `docs/COMMAND_CONVENTIONS.md`

---

## Verification expectations
- Run the repo quality gates when touching code, prompts, or contracts.
- Every important behavior needs at least one happy-path test or eval case.
- Add regression coverage for non-trivial bug fixes.
- For model, prompt, or agent changes, rerun the linked evals.
- For generated artifacts, prefer explicit assertions or golden fixtures.
- Do not claim verification you did not run.

---

## Tooling notes
- Codex desktop is primary; Copilot or editor agents are optional helpers.
- Ask for missing permissions, network access, or environment grants if correctness
  depends on them.
- Prefer official vendor documentation for provider-specific guidance.
- Verify before claiming a workflow works.

---

## Definition of done
- Behavior or template guidance is improved.
- Docs, prompts, evals, and contracts are updated when applicable.
- Task artifacts are updated with current status and next action when applicable.
- Verification is run and reported.
- Risks or follow-up items are called out explicitly.
