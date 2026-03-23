[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectName,

    [string]$ProjectSlug
)

$ErrorActionPreference = 'Stop'
$today = Get-Date -Format 'yyyy-MM-dd'

function Convert-ToSlug {
    param([Parameter(Mandatory = $true)][string]$Value)

    $slug = $Value.ToLowerInvariant()
    $slug = [regex]::Replace($slug, '[^a-z0-9]+', '-')
    $slug = $slug.Trim('-')

    if ([string]::IsNullOrWhiteSpace($slug)) {
        throw 'Could not derive a project slug from ProjectName.'
    }

    return $slug
}

function Assert-Path {
    param([Parameter(Mandatory = $true)][string]$Path)

    if (-not (Test-Path $Path)) {
        throw "Expected path not found: $Path"
    }
}

function Write-Utf8File {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)]$Value
    )

    $parent = Split-Path -Path $Path -Parent
    if ($parent -and -not (Test-Path $parent)) {
        New-Item -ItemType Directory -Path $parent -Force | Out-Null
    }

    Set-Content -Path $Path -Value $Value -Encoding utf8
}

if ([string]::IsNullOrWhiteSpace($ProjectSlug)) {
    $ProjectSlug = Convert-ToSlug -Value $ProjectName
}

@(
    'README.md',
    'pyproject.toml',
    'CHANGELOG.md',
    'work/ACTIVE_TASKS.md',
    'work/LEARNINGS.md',
    'work/items'
) | ForEach-Object { Assert-Path -Path $_ }

$readme = @"
# $ProjectName

This repository was bootstrapped from the Codex-first template on $today. The repo
structure is ready, but the product definition is still in draft form.

## Start Here
1. Read `docs/BOOTSTRAP_NEXT_STEPS.md`.
2. Rewrite `docs/PROJECT_MANIFESTO.md` for the real product.
3. Rewrite `docs/PROJECT_CHARTER.md` with the first-release scope and non-goals.
4. Decide whether to keep or replace the inherited maintenance stack in
   `docs/TECH_STACK_SELECTION.md`.
5. Update `work/items/BOOTSTRAP-001-initialize-project.md` and `work/ACTIVE_TASKS.md`
   before starting the first feature.

## Current Bootstrap Status
- Project name initialized as `$ProjectName`.
- Project slug initialized as `$ProjectSlug`.
- Template-only work items were removed.
- Project-facing draft docs were generated for the manifesto, charter, stack
  decision, and first-session guide.
- Placeholder text still needs to be replaced before feature work begins.

## If You Want Codex To Help
Use a prompt shaped like this:

```text
Goal: Turn the placeholder project docs into a real first-pass spec.
Context: Read AGENTS.md, docs/BOOTSTRAP_NEXT_STEPS.md, docs/PROJECT_MANIFESTO.md,
docs/PROJECT_CHARTER.md, docs/TECH_STACK_SELECTION.md, and
work/items/BOOTSTRAP-001-initialize-project.md.
Constraints: Keep the scope to project-definition docs. Do not start feature
implementation yet.
Done when: README, manifesto, charter, stack selection, and work tracking reflect
the real project.
```

## Verification
If you are keeping the template's maintenance stack for now, create a virtual
environment and run the default checks described in `docs/BOOTSTRAP_NEXT_STEPS.md`.
"@
Write-Utf8File -Path 'README.md' -Value $readme

$pyprojectLines = Get-Content 'pyproject.toml'
$replacedProjectName = $false
$updatedPyprojectLines = foreach ($line in $pyprojectLines) {
    if (-not $replacedProjectName -and $line -match '^name\s*=\s*".*"$') {
        $replacedProjectName = $true
        "name = `"$ProjectSlug`""
    }
    else {
        $line
    }
}
if (-not $replacedProjectName) {
    throw 'Could not update the project name in pyproject.toml.'
}
Write-Utf8File -Path 'pyproject.toml' -Value $updatedPyprojectLines

$changelog = @"
# Changelog
*Version:* v0.1
*Date:* $today
*Last reviewed:* $today

## Unreleased
- Initialized $ProjectName from the Codex-first repo template.
"@
Write-Utf8File -Path 'CHANGELOG.md' -Value $changelog

$startHere = @"
# Start Here
*Version:* v0.1
*Date:* $today
*Last reviewed:* $today

This is the shortest useful path for the first working session in $ProjectName.

## First Session
1. Read `docs/BOOTSTRAP_NEXT_STEPS.md`.
2. Rewrite `docs/PROJECT_MANIFESTO.md` so it describes the real user problem.
3. Rewrite `docs/PROJECT_CHARTER.md` with scope, users, success metrics, and
   non-goals.
4. Update `docs/TECH_STACK_SELECTION.md` with the actual stack and verification plan.
5. Confirm the next real task in `work/items/BOOTSTRAP-001-initialize-project.md`.

## Guidance To Keep
These files stay useful after the product docs are rewritten:
- `AGENTS.md`
- `docs/AI_DEV_WORKFLOW.md`
- `docs/CODEX_PROMPTING.md`
- `docs/TASK_MANAGEMENT.md`
- `docs/GUARDRAILS.md`
- `docs/MODEL_POLICY.md`

## After This
Once the project-definition docs are real, choose the first small implementation
slice and keep docs, tests, and `work/` aligned in the same diff.
"@
Write-Utf8File -Path 'docs/START_HERE.md' -Value $startHere

$bootstrapGuide = @"
# Bootstrap Next Steps
*Version:* v0.1
*Date:* $today
*Last reviewed:* $today

This guide is the primary post-bootstrap handoff for $ProjectName. Complete the
steps below before feature work so the repo stops reading like a template and starts
reading like your project.

## What Bootstrap Already Did
- Renamed the repo landing page to `$ProjectName`.
- Set the project slug to `$ProjectSlug` in `pyproject.toml`.
- Reset `CHANGELOG.md`, `work/ACTIVE_TASKS.md`, and `work/LEARNINGS.md`.
- Removed template-only work items under `work/items/TEMPLATE-*.md`.
- Generated project-draft placeholders for the manifesto, charter, stack decision,
  and this guide.

## Complete These Steps Now
1. Rewrite `docs/PROJECT_MANIFESTO.md`.
   Done when: a new contributor can explain why the project exists and what it will
   not do yet.
2. Rewrite `docs/PROJECT_CHARTER.md`.
   Done when: scope, users, success metrics, and non-goals are explicit.
3. Rewrite `docs/TECH_STACK_SELECTION.md`.
   Done when: the real implementation stack and verification path are named, even if
   some decisions are provisional.
4. Replace any remaining placeholder wording in `README.md` and `docs/START_HERE.md`.
   Done when: the repo no longer presents itself as the template.
5. Update `work/items/BOOTSTRAP-001-initialize-project.md` and `work/ACTIVE_TASKS.md`.
   Done when: another contributor can see the next real task without chat history.

## If You Want Codex To Do The First Pass
Use a prompt like this:

```text
Goal: Convert the bootstrapped placeholder docs into a real project definition.
Context: Read AGENTS.md, docs/BOOTSTRAP_NEXT_STEPS.md, docs/PROJECT_MANIFESTO.md,
docs/PROJECT_CHARTER.md, docs/TECH_STACK_SELECTION.md, and
work/items/BOOTSTRAP-001-initialize-project.md.
Constraints: Do not start feature implementation. Keep the diff focused on project
definition and onboarding clarity.
Done when: the project docs, README, and work tracking describe the real product and
the next implementation task.
```

## Current Setup Commands
If you want to keep the template's maintenance stack temporarily, use these commands.

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Default verification while the maintenance stack is still in place:

```text
ruff format .
ruff check .
pytest -q
python scripts/run_prompt_evals.py
python scripts/newcomer_smoke_test.py
```

## Before The First Feature
- Work through `docs/REPO_BOOTSTRAP_CHECKLIST.md`.
- Add at least one real decision entry in `docs/DECISIONS.md`.
- Make sure `work/ACTIVE_TASKS.md` points at the first product slice, not bootstrap
  cleanup.
"@
Write-Utf8File -Path 'docs/BOOTSTRAP_NEXT_STEPS.md' -Value $bootstrapGuide

$manifesto = @"
# Project Manifesto
*Version:* v0.1
*Date:* $today
*Last reviewed:* $today

This draft was generated during bootstrap for $ProjectName. Replace the starter
prompts below with plain-language statements before feature work begins.

## Why This Exists
- Replace this with the concrete problem $ProjectName should solve.
- Replace this with the user or team who feels that problem most sharply.
- Replace this with the reason this repo is the right place to solve it.

## The Promise
- Replace this with the core outcome users should get from the product.
- Replace this with the workflow improvement the product should make obvious.
- Replace this with the trust or reliability bar the product must meet.

## Non-Negotiables
- Keep repo-owned source-of-truth docs so humans and Codex can work from the same
  context.
- Replace this with the most important product-quality bar.
- Replace this with the most important safety, privacy, or compliance boundary.

## Anti-Goals
- Replace this with one tempting expansion you will not do in v1.
- Replace this with one automation or integration you are explicitly deferring.
- Replace this with one complexity trap that should stay out of scope.

## What Good Looks Like First
- Replace this with the smallest useful outcome for a real user.
- Replace this with the signal that proves the first release is working.
- Replace this with the maintenance or handoff behavior you expect from the repo.

## Constraints
- Replace this with platform, environment, or deployment constraints.
- Replace this with team-capacity or maintenance constraints.
- Replace this with data, model, or workflow boundaries that cannot be violated.
"@
Write-Utf8File -Path 'docs/PROJECT_MANIFESTO.md' -Value $manifesto

$charter = @"
# Project Charter
*Version:* v0.1
*Date:* $today
*Last reviewed:* $today

This charter is a starter draft for $ProjectName. Replace each placeholder with the
real first-release boundaries before implementation starts.

## Scope
### In Scope For The First Release
- Replace this with the smallest end-to-end workflow the product must support.
- Replace this with the most important user-visible behavior to get right first.
- Replace this with the supporting capability that must exist for the workflow to work.

### Out Of Scope For Now
- Replace this with a tempting feature that can wait.
- Replace this with a platform, integration, or workflow that should stay deferred.
- Replace this with one operational shortcut you should not take.

## Primary Users
- Replace this with the main user or team.
- Replace this with the second-most-important user only if they materially affect scope.

## Success Metrics
- Replace this with the first signal that proves the product is useful.
- Replace this with the first signal that proves the workflow is reliable.
- Replace this with the first signal that proves the repo is maintainable.

## Risks
- Replace this with the biggest product-delivery risk.
- Replace this with the biggest technical or operational risk.
- Replace this with the biggest ambiguity that should be resolved before broad buildout.

## Delivery Approach
- Start with one thin slice that exercises the core workflow.
- Keep docs, code, prompts, evals, and tests aligned in the same diff when behavior
  changes.
- Replace this with any project-specific rollout or review constraint.

## Next In Fast Path
Open `docs/TECH_STACK_SELECTION.md`, then update
`work/items/BOOTSTRAP-001-initialize-project.md`.
"@
Write-Utf8File -Path 'docs/PROJECT_CHARTER.md' -Value $charter

$techStack = @"
# Tech Stack Selection
*Version:* v0.1
*Date:* $today
*Last reviewed:* $today

This draft records the inherited defaults from the template and the decisions still
needed for $ProjectName.

## Current Inherited Defaults
- Repo slug: `$ProjectSlug`
- Maintenance stack: Python plus `pytest`, `ruff`, and `pre-commit`
- Repo structure: `docs/`, `work/`, `system/`, `prompts/`, `evals/`, `src/`, and
  `tests/`

## Replace These With Real Decisions
- Product surfaces: replace with the app, service, or workflow you are actually
  building.
- Primary implementation language: replace with the language that should own the core
  product logic.
- Main test runner: replace with the verification path that should become canonical.
- Packaging or build tool: replace with the real toolchain or deployment packaging.
- Deployment target: replace with the environment where the product will run.
- Observability and debugging: replace with the logs, metrics, or traces you need.
- Prompt and eval strategy: replace with the real plan if model behavior matters to
  users.

## Decision On The Inherited Python Maintenance Stack
- Replace this with one of:
  - keep it temporarily while the real stack is still being chosen
  - replace it immediately with the project's native tooling
  - remove it if the repo will stay docs-only for now

## Next Decision
- Name the first real implementation slice and the command that should verify it.
"@
Write-Utf8File -Path 'docs/TECH_STACK_SELECTION.md' -Value $techStack

$activeTasks = @"
# Active Tasks
*Version:* v0.1
*Date:* $today
*Last reviewed:* $today

This file is the canonical current task list for the repo.

## Active
| ID | Title | Status | Owner | Next action | Last updated |
| --- | --- | --- | --- | --- | --- |
| BOOTSTRAP-001 | Initialize $ProjectName from the Codex-first template | todo | human | Open docs/BOOTSTRAP_NEXT_STEPS.md and complete Step 1. | $today |

## Rules
- Update status and next action before ending meaningful work.
- Link to a detailed file in `work/items/` when a task needs history or acceptance
  criteria.
- Capture durable discoveries in `work/LEARNINGS.md` when they should influence future
  work.
- Remove or archive stale rows once the task is truly done.
"@
Write-Utf8File -Path 'work/ACTIVE_TASKS.md' -Value $activeTasks

$learnings = @"
# Durable Learnings
*Version:* v0.1
*Date:* $today
*Last reviewed:* $today

Use this file for discoveries that should influence future work but do not fit neatly in
a single task file.

## Entries
"@
Write-Utf8File -Path 'work/LEARNINGS.md' -Value $learnings

$bootstrapItem = @"
---
template: work_item
template_version: 0.4
template_date: 2026-03-11
template_last_reviewed: 2026-03-11
type: work_item
item_id: BOOTSTRAP-001
title: Initialize $ProjectName from the Codex-first template
status: todo
owner: human
updated: $today
next_action: Open docs/BOOTSTRAP_NEXT_STEPS.md and rewrite the manifesto.
blocked_on: none
---

# Initialize $ProjectName from the Codex-first template

## Summary
- Replace the remaining placeholder content with the real project's intent, scope,
  stack, and first task queue.
- Use `docs/BOOTSTRAP_NEXT_STEPS.md` as the primary guide until the repo has a real
  product definition.

## Acceptance Criteria
- `README.md` describes the real project rather than the template.
- `docs/PROJECT_MANIFESTO.md` is rewritten for the real product.
- `docs/PROJECT_CHARTER.md` is rewritten with real scope and non-goals.
- `docs/TECH_STACK_SELECTION.md` reflects the actual stack decision.
- `work/ACTIVE_TASKS.md` points at the first non-bootstrap product task.

## Progress Log
- ${today}: bootstrap task created from the template with project-draft docs and a
  guided handoff.

## Verification
- not run yet

## Next Action
- Open `docs/BOOTSTRAP_NEXT_STEPS.md` and rewrite `docs/PROJECT_MANIFESTO.md`.

## Notes
- Review `docs/REPO_BOOTSTRAP_CHECKLIST.md` before the first real feature.
- Keep placeholder wording only long enough to decide the real product definition.
"@
Write-Utf8File -Path 'work/items/BOOTSTRAP-001-initialize-project.md' -Value $bootstrapItem

Get-ChildItem -Path 'work/items' -Filter 'TEMPLATE-*.md' -File | ForEach-Object {
    Remove-Item -Path $_.FullName -Force
}

Write-Output "Bootstrap complete for $ProjectName ($ProjectSlug)."
Write-Output 'Start here next:'
Write-Output '  1. docs/BOOTSTRAP_NEXT_STEPS.md'
Write-Output '  2. docs/PROJECT_MANIFESTO.md'
Write-Output '  3. docs/PROJECT_CHARTER.md'
Write-Output '  4. docs/TECH_STACK_SELECTION.md'
Write-Output '  5. work/items/BOOTSTRAP-001-initialize-project.md'
