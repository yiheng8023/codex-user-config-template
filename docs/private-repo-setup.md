# Private Repository Setup

1. Create a private repository from this template.
2. Keep real memory, preferences, tokens, local paths, and runtime state in that private repository only.
3. Review the starter `AGENTS.md` before treating it as live authority. Merge it with any existing user, organization, or project instructions instead of blindly overwriting them.
4. Keep repository metadata in `config/manifest.example.json`; only put fields
   accepted by the official Codex schema in `config/common.example.toml`.
5. Replace example URLs and placeholders with your own reviewed values.
6. Add install, backup, verify, and rollback logic only after you understand the permission boundary.
7. Run offline and current-upstream verification before committing changes.

Recommended command:

```bash
python -B scripts/verify.py
python -B scripts/audit_codex_upstream.py --baseline config/upstream-contract.json --config config/common.example.toml
```

If you later want to contribute reusable improvements back to the public template, use the private-to-public promote process described in `docs/private-public-sync-model.md`.
