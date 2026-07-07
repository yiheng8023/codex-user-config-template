# Private / Public Sync Model

Use a public-core plus private-overlay model.

```text
public template
  -> sync reusable structure, docs, examples, validation scripts

private configuration
  -> owns real user state, memory, preferences, local paths, and runtime integration
```

## Safe direction

Public to private can be mostly automated because the public template is
designed to be non-sensitive. Active instruction surfaces still require care:
public guidance and the starter root `AGENTS.md` should be merged as reviewed
material, not blindly copied over a user's existing root `AGENTS.md`.

The public template may ship a public-safe starter root `AGENTS.md`. Treat it
as a baseline for new private configurations or as a reviewed update source for
existing ones. It must not contain private memory, local paths, credentials,
account state, personal preferences, or runtime-only assumptions.

## Guarded direction

Private to public must be a promote step:

1. select candidate reusable change;
2. remove personal data and local state;
3. scan for secrets and restricted content;
4. check license and provenance;
5. remove exact-thread, screenshot, or probe-specific overfitting;
6. restate the change as a semantic class that works across paraphrases,
   languages, and future equivalent requests;
7. open a reviewed pull request;
8. merge only after human approval.

Do not run blind bidirectional sync between private and public repositories.

Do not promote a private root `AGENTS.md` wholesale as a public root
`AGENTS.md`. If a rule is reusable, extract the smallest public-safe rule,
remove personal meta guidance and local assumptions, restate it as a semantic
class, and publish it as starter guidance, documentation, or a clearly named
example fragment. The private repository remains the authority for the user's
live instruction stack.
