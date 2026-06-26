# Private Repository Setup

1. Create a private repository from this template.
2. Keep real memory, preferences, tokens, local paths, and runtime state in that private repository only.
3. Replace example URLs and placeholders with your own reviewed values.
4. Add install, backup, verify, and rollback logic only after you understand the permission boundary.
5. Run verification before committing changes.

Recommended command:

```bash
python -B scripts/verify.py
```

If you later want to contribute reusable improvements back to the public template, use the private-to-public promote process described in `docs/private-public-sync-model.md`.
