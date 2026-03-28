# Git Workflow
*Version:* v0.1  
*Date:* 2026-03-28  
*Last reviewed:* 2026-03-28

Use Git as a collaboration and publishing boundary, not as unnecessary ceremony.

## Core rule
Checkpoint always. Branch when publishing across a review, protection, or collaboration
boundary.

That means:
- local commits and checkpoints are always useful
- short-lived PR branches are useful when repo governance makes them useful
- a new branch for every tiny follow-up is usually noise, not discipline

## Choose the workflow by repo context
### Private, solo, and unprotected repos
Direct commits to `main` can be fine when:
- you are the only contributor
- `main` is not protected
- there is no required PR or review gate
- the cost of branch/PR ceremony is higher than the risk

Still do this:
- keep slices small
- commit/checkpoint before and after substantial changes
- run verification before considering the slice done
- keep `work/` current so the repo, not chat, carries the handoff state

### Protected, public, or shared repos
Use one short-lived branch per coherent, mergeable slice when:
- `main` is protected
- CI and required checks gate merges
- the repo is public
- more than one person may review or push changes

Default behavior:
- create a branch for the slice you intend to merge
- keep related fixes on that same branch until the PR is merged
- merge when the branch is green and reviewable
- delete the branch after merge

## Slice rule
One branch per mergeable slice is the default.

Do not create a new branch when:
- the fix is directly related to the same unmerged PR
- you are only addressing review feedback
- you are closing obvious fallout from the same change before merge

Create a new branch when:
- the earlier PR is already merged
- the new issue is clearly separate in scope
- combining the changes would make review materially worse

## Codex collaboration rule
When using Codex as a peer coding agent:
- let Codex make local checkpoints freely
- ask Codex to inspect branch status before publishing
- keep publish behavior consistent with the repo's governance
- do not force Codex into PR-branch ceremony for scratch exploration in a solo repo
- do not let Codex push directly to protected `main`

## Hygiene
- auto-delete merged branches when practical
- prune stale remote refs periodically
- keep branch names short and meaningful
- use a consistent prefix if your tooling already expects one

## Template maintainer default
For this template repo itself, assume:
- `main` is protected
- CI is required
- changes publish through short-lived PR branches

Downstream projects should decide their own publish path during bootstrap instead of
blindly inheriting the template maintainer workflow.
