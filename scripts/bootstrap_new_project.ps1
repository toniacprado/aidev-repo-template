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

$readme = Get-Content 'README.md' -Raw
$readme = [regex]::Replace($readme, '(?m)^# .+$', "# $ProjectName", 1)
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

$activeTasks = @"
# Active Tasks
*Version:* v0.1  
*Date:* $today  
*Last reviewed:* $today

This file is the canonical current task list for the repo.

## Active
| ID | Title | Status | Owner | Next action | Last updated |
| --- | --- | --- | --- | --- | --- |
| BOOTSTRAP-001 | Initialize $ProjectName from the Codex-first template | todo | human | Rewrite the manifesto and charter, then choose the real stack and verification path | $today |

## Rules
- Update status and next action before ending meaningful work.
- Link to a detailed file in `work/items/` when a task needs history or acceptance criteria.
- Capture durable discoveries in `work/LEARNINGS.md` when they should influence future work.
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
next_action: Rewrite docs/PROJECT_MANIFESTO.md and docs/PROJECT_CHARTER.md for the real project.
blocked_on: none
---

# Initialize $ProjectName from the Codex-first template

## Summary
- Replace the remaining template identity with the real project's intent, scope, stack,
  and first task queue.

## Acceptance Criteria
- `README.md` reflects the real project name.
- `docs/PROJECT_MANIFESTO.md` is rewritten for the real project.
- `docs/PROJECT_CHARTER.md` is rewritten for the real project.
- `docs/TECH_STACK_SELECTION.md` reflects the real stack choice.
- `work/ACTIVE_TASKS.md` reflects the real next step.

## Progress Log
- $today: bootstrap task created from the template.

## Verification
- not run yet

## Next Action
- Rewrite `docs/PROJECT_MANIFESTO.md` and `docs/PROJECT_CHARTER.md` for the real project.

## Notes
- Review `docs/REPO_BOOTSTRAP_CHECKLIST.md` before the first real feature.
"@
Write-Utf8File -Path 'work/items/BOOTSTRAP-001-initialize-project.md' -Value $bootstrapItem

Get-ChildItem -Path 'work/items' -Filter 'TEMPLATE-*.md' -File | ForEach-Object {
    Remove-Item -Path $_.FullName -Force
}

Write-Output "Bootstrap complete for $ProjectName ($ProjectSlug)."
Write-Output 'Next: rewrite docs/PROJECT_MANIFESTO.md, docs/PROJECT_CHARTER.md, and docs/TECH_STACK_SELECTION.md.'
