# codex-user-config-template

English | [简体中文](README.zh-CN.md)

Public-safe template for creating a private Codex user-configuration repository without publishing personal memory, preferences, credentials, account state, or machine-local runtime details.

## Repository Role

This repository is a template, not a live user configuration. It helps a user build their own private configuration repository with clear safety boundaries, portable structure, and verification hooks.

## What This Repository Provides

- A public-safe repository layout for a private Codex configuration baseline.
- Example configuration files with placeholders only.
- Verification scripts that check the template stays public-safe and structurally valid.
- Documentation for public/private sync, license boundaries, and private setup.

## What This Repository Does Not Own

- Real Codex memory snapshots.
- Personal preferences, prompts, account choices, or local machine paths.
- OAuth state, credentials, tokens, cookies, browser sessions, logs, caches, or app runtime state.
- Third-party Skill content governance; use a curated Skills repository for that.
- Resource discovery, scoring, or lifecycle governance; use a resource-radar repository for that.

## Relationship To The Private Repository

Recommended model:

```text
codex-user-config-template
  -> provides public-safe structure, docs, placeholder examples, and validation

private codex-user-config
  -> consumes the template as a starting point
  -> owns real preferences, memory snapshots, local install policy, backups, verification, and rollback
  -> must remain private unless carefully declassified
```

Public-to-private sync can be automated for reusable template surfaces. Private-to-public promotion must be filtered, reviewed, and manually approved.

## Relationship To The Wider System

This template is one lane in a modular resource-governance system:

- `resource-radar` discovers and evaluates public resources.
- `agent-skills-curated` governs reviewed Skill content and release manifests.
- bookmark repositories provide public-safe source directories and private overlays.
- private user configuration repositories install, verify, and operate the user's actual environment.

## Layout

```text
config/                  Placeholder example configuration
docs/                    Public/private boundaries and setup guidance
hooks/                   Hook policy placeholder, not live automation
memory/                  Memory boundary placeholder, not real memory
scripts/verify.py        Public-safety and structure validation
skills/                  Skill install-policy placeholder, not vendored Skills
```

## Verification

Run:

```bash
python -B scripts/verify.py
```

GitHub Actions runs the same verification on pull requests and pushes to `main`.

## Update Rules

1. Keep this repository public-safe by default.
2. Add only placeholders, examples, schemas, scripts, and generic documentation.
3. Do not copy private configuration, memory, credentials, local paths, account state, or personal preference files into this repository.
4. Promote reusable private improvements only through a filtered, reviewed, public-safe change.

## Safety Boundaries

Treat private configuration as the authority for a user's actual environment. Treat this template as scaffolding only. If a change might expose personal information, account state, private preferences, or local runtime details, keep it out of this repository.
