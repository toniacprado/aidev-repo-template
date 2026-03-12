# Tool Risk Matrix
*Version:* v0.4  
*Date:* 2026-03-11  
*Last reviewed:* 2026-03-11

## Low risk
- read files in the repo
- search, inspect, or summarize code
- run formatting, lint, and tests in the workspace

## Medium risk
- write files in the workspace
- change shared repo config
- add or update prompts, evals, or automation rules
- install local dependencies when the task clearly requires them

## High risk
- destructive file operations
- wide network access
- secrets handling
- model-default changes for user-facing behavior
- automated publishing, sending, or production changes

## Approval guidance
- low risk: usually proceed
- medium risk: proceed when clearly in scope and reviewable
- high risk: require explicit human approval and leave a durable record in `work/`
