# Private / Public Sync Model

Use a public-core plus private-overlay model.

```text
public template
  -> sync reusable structure, docs, examples, validation scripts

private configuration
  -> owns real user state, memory, preferences, local paths, and runtime integration
```

## Safe direction

Public to private can be mostly automated because the public template is designed to be non-sensitive.

## Guarded direction

Private to public must be a promote step:

1. select candidate reusable change;
2. remove personal data and local state;
3. scan for secrets and restricted content;
4. check license and provenance;
5. open a reviewed pull request;
6. merge only after human approval.

Do not run blind bidirectional sync between private and public repositories.
