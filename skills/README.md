# Skills

This directory is a policy placeholder.

Do not vendor third-party Skill content into this template. Curated Skill content should be governed by a dedicated Skills repository with provenance, license, security review, adaptation, validation, and release manifests.

Use native reasoning and the thin kernel first. A private configuration may
load a task-bound Skill when the user explicitly names a Skill or when direct
evidence shows a reproducible residual gap that the native route did not
resolve. Installation or visibility does not activate a Skill or make it task
authority.

The Agent owns task-time capability selection, sequencing, and supported
orchestration. A default private bootstrap should install the thin kernel alone;
first-party collaboration Skills require explicit opt-in after a residual gap
is reproduced. Capability exposure is task-scoped. Re-running a default
bootstrap is not cleanup: the lifecycle owner must deproject it deliberately,
verify the post-state, and preserve shared or unknown-owned resources.

When such a Skill is used, keep its reusable boundary aligned with
`docs/request-intake-and-capability-boundaries.md`: route only after the task
contract is bound, treat probes as liveness checks rather than acceptance, and
avoid optimizing behavior around exact test prompts.
