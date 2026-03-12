# Model Policy
*Version:* v0.4  
*Date:* 2026-03-11  
*Last reviewed:* 2026-03-11

This file defines how the repo should choose, pin, and change models.

## Core policy
- Use the best available interactive coding model for live repo work.
- For production or user-facing model behavior, prefer pinned dated snapshots rather
  than moving aliases.
- Treat model changes like behavior changes: rerun evals and review the consequences.

## Why this matters
OpenAI's current model guidance distinguishes between moving aliases and dated versions.
Inference from that guidance: aliases are convenient for interactive use, while dated
versions are safer when you need predictable production behavior.

## Recommended defaults
- Codex interactive work: use the team's current approved Codex-capable model alias.
- Automated CI or product behavior that depends on model output: pin a dated model
  version and track it in code or config.
- High-risk launches: require eval baselines and explicit review before model changes.

## Every model change should answer
- What model or snapshot changed?
- Which prompts or structured outputs depend on it?
- Which eval set was rerun?
- What behavior improved, regressed, or stayed the same?
- Should the default change for everyone or only for a specific workflow?

## Minimum change process
1. Update the relevant prompt or config.
2. Rerun the linked evals.
3. Record the result in the work item or decision log.
4. Update this file or a project-specific model decision if the default changes.

## As of 2026-03-11
OpenAI's public model guidance still supports the pattern above: use current model
aliases for exploration and dated snapshots when consistent behavior matters.
