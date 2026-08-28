#!/usr/bin/env python3
"""Audit Codex TOML files against the current official configuration schema."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import tomllib
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


SCHEMA_URL = "https://learn.chatgpt.com/docs/config-schema.json"


def fetch_schema(source: str, timeout: float) -> tuple[dict[str, Any], bytes]:
    if source.startswith(("https://", "http://")):
        request = urllib.request.Request(
            source,
            headers={"User-Agent": "codex-user-config-upstream-audit/1"},
        )
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = response.read()
    else:
        payload = Path(source).read_bytes()
    schema = json.loads(payload)
    if not isinstance(schema, dict):
        raise ValueError("official schema root must be an object")
    return schema, payload


def resolve_ref(root: dict[str, Any], reference: str) -> dict[str, Any]:
    if not reference.startswith("#/"):
        raise ValueError(f"unsupported external schema reference: {reference}")
    value: Any = root
    for encoded_part in reference[2:].split("/"):
        part = encoded_part.replace("~1", "/").replace("~0", "~")
        value = value[part]
    if not isinstance(value, dict):
        raise ValueError(f"schema reference is not an object: {reference}")
    return value


def type_matches(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, int | float) and not isinstance(value, bool)
    if expected == "null":
        return value is None
    raise ValueError(f"unsupported schema type: {expected}")


def observed_type(value: Any) -> str:
    if isinstance(value, dict):
        return "object"
    if isinstance(value, list):
        return "array"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, str):
        return "string"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, float):
        return "number"
    if value is None:
        return "null"
    return type(value).__name__


def validate_value(
    value: Any,
    schema: dict[str, Any],
    root: dict[str, Any],
    path: str = "$",
) -> list[str]:
    issues: list[str] = []

    reference = schema.get("$ref")
    if isinstance(reference, str):
        issues.extend(validate_value(value, resolve_ref(root, reference), root, path))

    for branch in schema.get("allOf", []):
        if isinstance(branch, dict):
            issues.extend(validate_value(value, branch, root, path))

    for keyword in ("anyOf", "oneOf"):
        branches = schema.get(keyword)
        if isinstance(branches, list):
            matches = [
                branch
                for branch in branches
                if isinstance(branch, dict)
                and not validate_value(value, branch, root, path)
            ]
            required_matches = 1
            if (keyword == "anyOf" and not matches) or (
                keyword == "oneOf" and len(matches) != required_matches
            ):
                issues.append(f"{path}: does not satisfy {keyword}")
            return issues

    expected = schema.get("type")
    if isinstance(expected, str):
        allowed_types = [expected]
    elif isinstance(expected, list):
        allowed_types = [item for item in expected if isinstance(item, str)]
    else:
        allowed_types = []
    if allowed_types and not any(type_matches(value, item) for item in allowed_types):
        issues.append(
            f"{path}: expected {' or '.join(allowed_types)}, observed {observed_type(value)}"
        )
        return issues

    if "const" in schema and value != schema["const"]:
        issues.append(f"{path}: expected constant {schema['const']!r}")
    enum = schema.get("enum")
    if isinstance(enum, list) and value not in enum:
        issues.append(f"{path}: value {value!r} is not in the allowed enum")

    if isinstance(value, dict):
        required = schema.get("required", [])
        if isinstance(required, list):
            for key in required:
                if isinstance(key, str) and key not in value:
                    issues.append(f"{path}.{key}: required value is missing")

        properties = schema.get("properties", {})
        if not isinstance(properties, dict):
            properties = {}
        patterns = schema.get("patternProperties", {})
        if not isinstance(patterns, dict):
            patterns = {}
        additional = schema.get("additionalProperties", True)

        for key, item in value.items():
            child_path = f"{path}.{key}"
            child_schema = properties.get(key)
            if isinstance(child_schema, dict):
                issues.extend(validate_value(item, child_schema, root, child_path))
                continue
            matched_patterns = [
                pattern_schema
                for pattern, pattern_schema in patterns.items()
                if re.search(pattern, str(key)) and isinstance(pattern_schema, dict)
            ]
            if matched_patterns:
                for pattern_schema in matched_patterns:
                    issues.extend(validate_value(item, pattern_schema, root, child_path))
            elif additional is False:
                issues.append(f"{child_path}: unknown configuration key")
            elif isinstance(additional, dict):
                issues.extend(validate_value(item, additional, root, child_path))

    if isinstance(value, list):
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(value):
                issues.extend(validate_value(item, item_schema, root, f"{path}[{index}]"))

    return issues


def load_toml(path: Path) -> dict[str, Any]:
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: TOML root must be a table")
    return data


def load_baseline(path: Path) -> dict[str, Any]:
    baseline = json.loads(path.read_text(encoding="utf-8"))
    if baseline.get("schemaVersion") != 1:
        raise ValueError(f"{path}: unsupported baseline schemaVersion")
    if baseline.get("source") != SCHEMA_URL:
        raise ValueError(f"{path}: baseline source must be {SCHEMA_URL}")
    root_properties = baseline.get("rootProperties")
    if not isinstance(root_properties, list) or not all(
        isinstance(item, str) for item in root_properties
    ):
        raise ValueError(f"{path}: rootProperties must be a string array")
    if root_properties != sorted(set(root_properties)):
        raise ValueError(f"{path}: rootProperties must be sorted and unique")
    return baseline


def compare_baseline(schema: dict[str, Any], baseline: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    if schema.get("title") != baseline.get("schemaTitle"):
        issues.append(
            "schema title changed: "
            f"{baseline.get('schemaTitle')!r} -> {schema.get('title')!r}"
        )
    properties = schema.get("properties", {})
    current = sorted(properties) if isinstance(properties, dict) else []
    expected = baseline["rootProperties"]
    added = sorted(set(current) - set(expected))
    removed = sorted(set(expected) - set(current))
    if added:
        issues.append("official root properties added: " + ", ".join(added))
    if removed:
        issues.append("official root properties removed: " + ", ".join(removed))
    return issues


def run_self_test() -> None:
    fixture = {
        "title": "Fixture",
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "profile": {"type": "string"},
            "features": {"$ref": "#/definitions/Features"},
        },
        "definitions": {
            "Features": {
                "type": "object",
                "additionalProperties": False,
                "properties": {"hooks": {"type": "boolean"}},
            }
        },
    }
    if validate_value({"profile": "default"}, fixture, fixture):
        raise AssertionError("valid fixture was rejected")
    invalid = validate_value({"profile": {"name": "example"}}, fixture, fixture)
    if not any("expected string, observed object" in item for item in invalid):
        raise AssertionError("profile table regression was not detected")
    unknown = validate_value({"features": {"retired": True}}, fixture, fixture)
    if not any("unknown configuration key" in item for item in unknown):
        raise AssertionError("unknown nested key was not detected")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate Codex TOML against the current official schema"
    )
    parser.add_argument("--schema", default=SCHEMA_URL)
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--config", action="append", type=Path, default=[])
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    try:
        if args.self_test:
            run_self_test()
            print("Schema validator self-test passed.")
        if not args.config and args.baseline is None:
            return 0

        schema, payload = fetch_schema(args.schema, args.timeout)
        print(f"Official schema: {args.schema}")
        print(f"Schema title: {schema.get('title', '<missing>')}")
        print(f"Schema SHA-256: {hashlib.sha256(payload).hexdigest()}")

        issues: list[str] = []
        if args.baseline is not None:
            issues.extend(
                compare_baseline(schema, load_baseline(args.baseline.expanduser()))
            )
        for raw_path in args.config:
            path = raw_path.expanduser()
            config_issues = validate_value(load_toml(path), schema, schema)
            if config_issues:
                issues.extend(f"{path.as_posix()}: {item}" for item in config_issues)
            else:
                print(f"Config compatibility: PASS ({path.as_posix()})")

        if issues:
            print("Codex upstream audit failed:", file=sys.stderr)
            for issue in issues:
                print(f"- {issue}", file=sys.stderr)
            return 1
        print("Codex upstream audit passed.")
        return 0
    except (OSError, ValueError, json.JSONDecodeError, tomllib.TOMLDecodeError) as exc:
        print(f"Codex upstream audit could not run: {exc}", file=sys.stderr)
        return 2
    except urllib.error.URLError as exc:
        print(f"Codex upstream audit could not fetch the schema: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
