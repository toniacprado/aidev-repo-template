# AGENTS.md - Rules for AI Coding Agents (Codex-first)
*Version:* v1.4  
*Date:* 2026-03-28  
*Last reviewed:* 2026-03-28

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
7. `docs/CONTEXT_ENGINEERING.md`
8. `docs/GIT_WORKFLOW.md`
9. `docs/REPO_STRUCTURE.md`
10. task-specific contracts in `work/`, `.codex/`, `system/`, `prompts/`, and `evals/`

---

## Default Context Load
1. `docs/PROJECT_MANIFESTO.md`
2. `docs/PROJECT_CHARTER.md`
3. `docs/CONTEXT_ENGINEERING.md`
4. `docs/GIT_WORKFLOW.md`
5. `work/ACTIVE_TASKS.md`
6. the relevant file in `work/items/`
7. only the smallest additional context pack from `docs/CONTEXT_ENGINEERING.md`

Additional defaults:
- If you are new to the repo, also read `docs/CODEX_FIRST_HOUR.md`.
- Do not preload the full repo by default; retrieve additional docs, prompts, policies,
  and source files only when the current task requires them.
- When working on model behavior, add `prompts/README.md`, `evals/README.md`, and the
  touched prompt/eval assets.

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
- Prefer the smallest relevant context pack over broad preloading. Retrieve extra files
  just in time as the task sharpens.
- When work depends on external changing context, prefer MCP or official docs over pasted
  summaries.
- For OpenAI or Codex usage questions, prefer the OpenAI developer docs MCP server when
  it is available; otherwise use official OpenAI docs.
- Keep shared Codex config conservative: `on-request` approvals, `workspace-write`, and
  network off by default unless the task clearly needs more.
- Treat the Python tooling in this repo as template-maintenance-only, not as a product-stack assumption.
- Use nested `AGENTS.override.md` files for genuinely different rules in subtrees.
- If a session becomes long or changes direction, compact the durable state back into
  `work/`, `docs/DECISIONS.md`, and `work/LEARNINGS.md` before continuing.

## Fresh repo bootstrap mode
- If this repo was freshly created from the template and `work/items/BOOTSTRAP-001-initialize-project.md`
  is still active, or the core product docs still contain obvious placeholders, strongly
  recommend finishing the bootstrap artifacts before feature implementation.
- When they exist, start with `docs/CODEX_SESSION_STARTER.md`, `docs/BOOTSTRAP_NEXT_STEPS.md`,
  and `docs/BOOTSTRAP_ARTIFACT_WORKSHOP.md` before broad implementation work.
- Prefer a short focused interview that drafts the core artifacts directly over asking the
  user to fill blank forms by hand.
- Do not suggest rerunning `scripts/bootstrap_new_project.py` or
  `scripts/bootstrap_new_project.ps1` after bootstrap has already completed unless the user
  explicitly asks to reset the repo state.
- If the user explicitly wants to skip bootstrap, warn once that implementation quality will
  be weaker because product intent is not yet durable in the repo.
- After a skip, proceed if the user confirms, but record assumptions, unresolved product
  questions, and follow-up bootstrap debt in `work/`.

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
- Use local checkpoints freely while working, but prefer one short-lived branch per
  coherent, mergeable slice when publishing to a protected, public, or shared repo.
- If related fixes are found before that branch is merged, keep them on the same branch
  unless the issue is clearly separate or was discovered after merge.

---

## Key commands
These are maintenance commands for the template itself, not a claim about the downstream
project stack.

- Bootstrap (one-time reset for a fresh template copy): `python scripts/bootstrap_new_project.py --project-name "Your Project"` (or `python3` if needed before venv activation on macOS/Linux)
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
