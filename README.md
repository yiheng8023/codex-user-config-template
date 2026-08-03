# codex-user-config-template

English | [简体中文](README.zh-CN.md)

Public-safe template for creating a private Codex user-configuration repository without publishing personal memory, preferences, credentials, account state, or machine-local runtime details.

This is a Codex-specific public template: keep a Codex working environment
portable through a public-safe template plus a private overlay for real memory,
preferences, credentials, local paths, installed state, backup, verification,
restore, and rollback. Cross-runtime adaptation is out of scope for this
repository.

## Start here

| If you want to... | Go here |
| --- | --- |
| Create your own private Codex config repo | Use this template as the public-safe starting point |
| Check what is safe to copy | [`docs/`](docs) and placeholder examples under `config/`, `memory/`, and `skills/` |
| Review the public-safe instruction starter | [`AGENTS.md`](AGENTS.md) |
| Preserve request-intake and capability-routing boundaries | [`docs/request-intake-and-capability-boundaries.md`](docs/request-intake-and-capability-boundaries.md) |
| Verify the template | `python -B scripts/verify.py` |
| Understand this template's boundary | [Repository Role](#repository-role) |

## Independent Template Context

This repository is an independently usable public Codex-specific configuration
template. It demonstrates a public-template/private-overlay pattern through
repository-owned structure, validation, and setup guidance.

```text
codex-user-config-template
  -> provides public-safe structure, placeholders, validation, and setup guidance

private codex-user-config
  -> owns real Codex memory snapshots, preferences, install policy, backups, and rollback

optional reviewed Skill policy/source repository
  -> may publish governed Skill policy or releases for private consumers
```

Use this repository as a self-contained safe starting point. Optional external
Skill policy or releases remain separately governed inputs, not topology
authority.

## Repository Role

This repository is a template, not a live user configuration. It helps a user build their own private Codex configuration repository with clear safety boundaries, portable structure, and verification hooks. It intentionally targets Codex-specific files and workflows while removing private content.

This repository ships a public-safe starter root `AGENTS.md`. It is a reviewed
baseline for request intake, external capability boundaries, reasoning cadence,
and closeout coverage. It is not a complete live instruction stack, personal
memory, credential surface, or wholesale replacement for a user's existing
`AGENTS.md`. Treat it as starter material to review and adapt deliberately.

## What This Repository Provides

- A public-safe repository layout for a private Codex configuration baseline.
- Example configuration files with placeholders only.
- Verification scripts that check the template stays public-safe and structurally valid.
- Documentation for public/private sync, license boundaries, and private setup.
- Public-safe request-intake and capability-routing boundary guidance that can
  be absorbed into a private `AGENTS.md`, intake Skill, routing Skill, and
  verification fixtures as reviewed incremental additions.
- A public-safe root `AGENTS.md` starter that avoids private memory, local
  paths, credentials, account state, and runtime-only assumptions.

## What This Repository Does Not Own

- Real Codex memory snapshots.
- Personal preferences, prompts, account choices, or local machine paths.
- OAuth state, credentials, tokens, cookies, browser sessions, logs, caches, or app runtime state.
- Third-party Skill content governance; use a curated Skills repository for that.
- General resource discovery, scoring, or web-wide lifecycle governance.

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

Do not run blind synchronization for active instruction files. If a user
already has a root `AGENTS.md`, preserve their local preferences, authority
boundaries, and existing project or user rules. The public starter `AGENTS.md`
may be used as an initial baseline or reviewed update source, not as an
automatic overwrite.

## Optional External Inputs

Reviewed Skill releases may come from an independently governed curated
repository. The private user configuration decides whether to pin, install,
verify, or reject them. No external repository can modify this template or a
private consumer automatically.

## Layout

```text
config/                  Placeholder example configuration
AGENTS.md                Public-safe starter instruction surface
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

GitHub Actions may repeat the same verification on pull requests and pushes to
`main`; local verification remains sufficient and authoritative.

## Update Rules

1. Keep this repository public-safe by default.
2. Add only placeholders, examples, schemas, scripts, and generic documentation.
3. Do not copy private configuration, memory, credentials, local paths, account state, or personal preference files into this repository.
4. Promote reusable private improvements only through a filtered, reviewed, public-safe change.

## Safety Boundaries

Treat private configuration as the authority for a user's actual environment. Treat this template as scaffolding only. If a change might expose personal information, account state, private preferences, or local runtime details, keep it out of this repository.
