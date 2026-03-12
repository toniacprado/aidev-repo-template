# Codex Project Files
*Version:* v0.6  
*Date:* 2026-03-11  
*Last reviewed:* 2026-03-11

Use this directory for repo-shared Codex configuration and local-environment notes.

Recommended usage:
- keep `.codex/config.toml` in Git with conservative shared defaults
- keep `config.toml.example` as the editable starting point for future changes
- document any environment setup or external service assumptions near the config
- keep network and permissions as narrow as the repo can tolerate by default
- only rely on project config in trusted repositories
- document why non-default `project_doc_max_bytes` values are chosen
- keep project-scoped rules scaffolding in `codex/rules/`
