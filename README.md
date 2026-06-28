# codex-user-config-template

English | [简体中文](README.zh-CN.md)

Public-safe template for creating a private Codex user-configuration repository without publishing personal memory, preferences, credentials, account state, or machine-local runtime details.

This is a Codex-specific implementation of a more general pattern: keep an
AI/agent working environment portable through a public-safe template plus a
private overlay for real memory, preferences, credentials, local paths,
installed state, backup, verification, restore, and rollback. Other agents may
need different templates because their runtime files and setup surfaces differ.

## Start here

| If you want to... | Go here |
| --- | --- |
| Create your own private Codex config repo | Use this template as the public-safe starting point |
| Check what is safe to copy | [`docs/`](docs) and placeholder examples under `config/`, `memory/`, and `skills/` |
| Preserve request-intake and capability-routing boundaries | [`docs/request-intake-and-capability-boundaries.md`](docs/request-intake-and-capability-boundaries.md) |
| Verify the template | `python -B scripts/verify.py` |
| Understand the full system | [`open-resource-governance/docs/system-topology.md`](https://github.com/yiheng8023/open-resource-governance/blob/main/docs/system-topology.md) |

## System context

This repository is the public Codex-specific configuration template workstream in the
[`open-resource-governance`](https://github.com/yiheng8023/open-resource-governance)
ecosystem. It demonstrates the broader agent-environment portability pattern;
it is not a claim that the pattern is limited to Codex.

```text
open-resource-governance
  -> maps the whole repository family and public/private rules

codex-user-config-template
  -> provides public-safe structure, placeholders, validation, and setup guidance

private codex-user-config
  -> owns real Codex memory snapshots, preferences, install policy, backups, and rollback

agent-skills-curated
  -> may publish reviewed Skill releases that a private Codex configuration can consume
```

Use this repository when you want a safe starting point. Use the hub topology
when you want to understand the wider system:
[`open-resource-governance/docs/system-topology.md`](https://github.com/yiheng8023/open-resource-governance/blob/main/docs/system-topology.md).

## Repository Role

This repository is a template, not a live user configuration. It helps a user build their own private Codex configuration repository with clear safety boundaries, portable structure, and verification hooks. The general idea is portable across agents; this repository only implements the Codex-specific file and workflow shape.

## What This Repository Provides

- A public-safe repository layout for a private Codex configuration baseline.
- Example configuration files with placeholders only.
- Verification scripts that check the template stays public-safe and structurally valid.
- Documentation for public/private sync, license boundaries, and private setup.
- Public-safe request-intake and capability-routing boundary guidance that can
  be absorbed into a private `AGENTS.md`, intake Skill, routing Skill, and
  verification fixtures.

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

This template is one workstream in a modular resource-governance system:

- `resource-radar` discovers and evaluates public resources.
- `agent-skills-curated` governs reviewed Skill content and release manifests.
- bookmark repositories provide public-safe source directories while private bookmark repositories keep private content.
- private user configuration repositories install, verify, and operate the user's actual environment.

## Layout

```text
config/                  Placeholder example configuration
docs/                    Public/private, intake/routing, and setup guidance
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
