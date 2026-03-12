# Codex Environment
*Version:* v0.7  
*Date:* 2026-03-12  
*Last reviewed:* 2026-03-12

This file describes the shared Codex environment choices that make agent behavior more
predictable and reviewable.

## Shared defaults
Recommended shared defaults for this template:
- approvals: `on-request`
- sandbox: `workspace-write`
- network: off by default unless a task clearly needs it
- project docs: large enough to include `AGENTS.md` plus the key policy files
- shell environment: inherit core variables only and avoid leaking secrets by default

These choices mirror current OpenAI guidance to keep Codex constrained by default and
to make broader permissions explicit.

## Config precedence and trust
Codex reads configuration from multiple layers. Practical rule:
- user-level config controls personal defaults
- repo-level `.codex/config.toml` defines shared project defaults
- only use project config from trusted repositories

Keep shared project config minimal and reviewable so contributors can audit it quickly.

## Project config
Use `.codex/config.toml` for repo-shared Codex settings. This template ships with a
conservative `.codex/config.toml` plus `.codex/config.toml.example` as the editable
starting point.

Recommended shared settings to review:
- approval policy
- sandbox mode
- whether network access should be enabled
- environment-variable inheritance rules
- any repo-specific notes about fallback docs or trusted paths
- document why any non-default `project_doc_max_bytes` value is needed

## Maintenance stack note
Codex can still read, review, and improve most of this template without Python.
Python is only needed when you want to run the full local maintenance gates defined in
`docs/TEMPLATE_MAINTENANCE.md`.

## Environment preparation
If Codex needs a prepared environment:
- prefer documented setup over hidden one-off machine state
- use repeatable setup scripts or checked-in environment actions
- explain what external services or credentials are required before work begins
- keep command guidance OS agnostic; if shells differ, provide explicit alternatives
- prefer venv-activated `python` for repo commands and note `python3` fallback where needed

## External access policy
Default posture:
- keep network access off during normal agent work
- if internet access is enabled, narrow it to necessary domains and safe methods
- document why the broader access is needed
- keep secrets out of prompts, logs, and tracked config

## OpenAI docs access
For OpenAI or Codex implementation questions, the best source is the official OpenAI
developer documentation. If the OpenAI docs MCP server is available in your setup,
prefer it over pasted notes.
