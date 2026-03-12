# Durable Learnings
*Version:* v0.9  
*Date:* 2026-03-12  
*Last reviewed:* 2026-03-12

Use this file for discoveries that should influence future work but do not fit neatly in
a single task file.

## Entries
- Date: 2026-03-11
  Area: task management
  Learning: if the repo does not require task artifacts and next actions, agents tend to
    finish the current slice without leaving the next step visible.
  Why it matters: handoff quality drops and humans must reconstruct the plan from chat.
  Action or follow-up: keep `work/` mandatory for non-trivial multi-step work.

- Date: 2026-03-11
  Area: Codex environment
  Learning: a checked-in `.codex` example plus explicit guardrail and model docs makes
    the AI operating model more reviewable than relying on user-local setup alone.
  Why it matters: teams can reason about shared agent behavior before problems happen.
  Action or follow-up: promote `.codex/config.toml.example` to a real shared config once
    the team agrees on defaults.

- Date: 2026-03-11
  Area: maintenance stack
  Learning: Codex can maintain the docs, structure, and workflow rules of this template
    without Python, but Python still provides the cleanest way to run full local gates.
  Why it matters: the repo can stay stack-agnostic while still having a real
    verification story.
  Action or follow-up: keep Python clearly labeled as maintenance-only until the real
    project stack replaces it.

- Date: 2026-03-11
  Area: template bootstrap
  Learning: a bootstrap script that looks correct in review can still fail on real repo
    state; executable happy-path coverage caught a `pyproject.toml` rename bug here.
  Why it matters: the first-run path has to be trustworthy because new projects inherit it
    immediately.
  Action or follow-up: keep automated happy-path tests for important repo scripts and rerun
    full gates whenever the bootstrap flow changes.

- Date: 2026-03-11
  Area: bootstrap reliability
  Learning: bootstrap outputs should derive dates at runtime and always write UTF-8 to avoid
    stale metadata and encoding drift across PowerShell variants.
  Why it matters: template adopters judge trust quickly from first-run generated files, and
    stale dates or inconsistent encodings reduce confidence.
  Action or follow-up: keep dynamic-date and cleanup assertions in bootstrap tests, and run at
    least one PowerShell-backed smoke test before publishing.

- Date: 2026-03-11
  Area: Codex onboarding
  Learning: policy-heavy docs are necessary but insufficient for first-time Codex users; a
    short first-hour workflow plus concrete prompt/eval starter assets reduces adoption friction.
  Why it matters: templates fail in practice when newcomers cannot translate principles into the
    first successful end-to-end session.
  Action or follow-up: keep `docs/CODEX_FIRST_HOUR.md` current with official docs and run a
    newcomer usability pass before major releases.

- Date: 2026-03-11
  Area: prompt/eval reliability
  Learning: prompt/eval quality guidance should be enforced by deterministic tooling and CI,
    not docs alone.
  Why it matters: without executable checks, prompt/eval assets drift and lose trust quickly.
  Action or follow-up: keep `scripts/run_prompt_evals.py` and `scripts/newcomer_smoke_test.py`
    in required verification and extend golden fixtures as prompt coverage grows.

- Date: 2026-03-11
  Area: newcomer onboarding
  Learning: PowerShell-only bootstrap instructions and `python`-only command examples create
    avoidable first-run failures on macOS/Linux environments.
  Why it matters: template adoption depends on a successful first 10 minutes; command-not-found
    errors undermine confidence immediately.
  Action or follow-up: keep a cross-platform bootstrap entrypoint (`scripts/bootstrap_new_project.py`)
    as the primary path and keep OS-specific setup guidance explicit in docs.

- Date: 2026-03-12
  Area: OS-agnostic docs
  Learning: shell labels can accidentally imply platform requirements even when commands are
    platform neutral.
  Why it matters: newcomers copy/paste literally; misleading shell labels create avoidable setup
    confusion and lower trust in the template.
  Action or follow-up: use `text` code blocks for shell-neutral command lists and keep
    shell-specific code blocks only where syntax actually differs.

- Date: 2026-03-12
  Area: GitHub branch protection
  Learning: required status checks must match the actual job context names, not only workflow
    names, or merges will be blocked even when CI appears green.
  Why it matters: publish-time branch protection mistakes can create false-negative merge blocks
  and slow urgent fixes.
  Action or follow-up: when enabling required checks, verify exact context names from a real run
  before locking protection policy.

- Date: 2026-03-12
  Area: onboarding UX
  Learning: long sequential reading lists create navigation drop-off; users lose context and
    momentum when they must repeatedly return to an index.
  Why it matters: both newcomers and senior engineers prefer low-friction, linear activation
    paths that get to productive work quickly.
  Action or follow-up: keep a short fast path (5 docs max) and add explicit "next file" hints
    inside fast-path docs.

- Date: 2026-03-12
  Area: newcomer verification
  Learning: structural smoke checks are necessary but insufficient; they miss failures where
    files exist but workflows break.
  Why it matters: template confidence depends on proving behavior, not only presence of assets.
  Action or follow-up: keep at least one deterministic behavioral check in newcomer smoke tests
    (bootstrap execution on temp scaffold).
