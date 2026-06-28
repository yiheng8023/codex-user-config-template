# Public / Private Boundary

## Public template

This repository may contain:

- placeholder configuration;
- setup instructions;
- validation scripts;
- public-safe examples;
- generic repository maps.

## Private configuration

A user's private repository may contain:

- real preferences;
- reviewed memory snapshots;
- local install and rollback policy;
- machine-specific paths;
- account-specific choices;
- private notes.

## Never promote automatically

The following must not be copied from private to public without explicit declassification:

- secrets, tokens, cookies, OAuth state, or credentials;
- personal memory, chat logs, private notes, or preferences;
- local filesystem paths or device identifiers;
- account, billing, session, browser, or app runtime state;
- third-party restricted material.

Reusable request-intake or capability-routing rules may be promoted only after
they are stripped of private facts, exact thread context, screenshots,
probe-only wording, personal preferences, and local runtime assumptions. Public
rules should describe semantic classes and verification expectations, not a
single user's live configuration.
