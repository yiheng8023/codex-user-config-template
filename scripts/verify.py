from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "README.zh-CN.md",
    "NOTICE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    ".github/FUNDING.yml",
    ".github/workflows/validate.yml",
    "config/common.example.toml",
    "config/manifest.example.json",
    "docs/license-policy.md",
    "docs/public-private-boundary.md",
    "docs/private-public-sync-model.md",
    "docs/private-repo-setup.md",
    "hooks/README.md",
    "memory/README.md",
    "skills/README.md",
]

FORBIDDEN_PATH_PARTS = {
    ".codex",
    ".agents",
    ".cache",
    ".ssh",
    "oauth",
    "session",
    "cookies",
    "tokens",
    "secrets",
}


def fail(message: str) -> None:
    raise SystemExit(f"verify failed: {message}")


def require_file(path: str) -> None:
    candidate = ROOT / path
    if not candidate.is_file():
        fail(f"missing required file: {path}")


def verify_required_files() -> None:
    for path in REQUIRED_FILES:
        require_file(path)


def verify_manifest() -> None:
    manifest_path = ROOT / "config" / "manifest.example.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        fail("manifest.example.json must stay on schema_version 1")
    if data.get("public_safe") is not True:
        fail("manifest.example.json must declare public_safe=true")
    if data.get("private_repository_required") is not True:
        fail("manifest.example.json must declare private_repository_required=true")


def verify_no_private_payloads() -> None:
    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        rel = path.relative_to(ROOT).as_posix()
        lowered_parts = {part.lower() for part in path.relative_to(ROOT).parts}
        if lowered_parts & FORBIDDEN_PATH_PARTS:
            fail(f"forbidden private/runtime path in template: {rel}")
        if path.is_file() and path.suffix.lower() in {".jsonl", ".sqlite", ".db", ".pem", ".key"}:
            fail(f"forbidden private/runtime file type in template: {rel}")


def verify_language_links() -> None:
    english = (ROOT / "README.md").read_text(encoding="utf-8")
    chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
    if "English | [简体中文](README.zh-CN.md)" not in english:
        fail("README.md language switch is missing or inconsistent")
    if "[English](README.md) | 简体中文" not in chinese:
        fail("README.zh-CN.md language switch is missing or inconsistent")
    for phrase in [
        "System context",
        "open-resource-governance/docs/system-topology.md",
        "public Codex-configuration template lane",
    ]:
        if phrase not in english:
            fail(f"README.md missing system-context phrase: {phrase}")
    for phrase in [
        "系统位置",
        "open-resource-governance/docs/system-topology.md",
        "公开 Codex 配置模板 lane",
    ]:
        if phrase not in chinese:
            fail(f"README.zh-CN.md missing system-context phrase: {phrase}")


def main() -> None:
    verify_required_files()
    verify_manifest()
    verify_no_private_payloads()
    verify_language_links()
    print("codex-user-config-template verification passed")


if __name__ == "__main__":
    main()
