from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "AGENTS.md",
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
    "docs/request-intake-and-capability-boundaries.md",
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


def verify_public_agents_md() -> None:
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    for phrase in [
        "Public-Safe Codex AGENTS Starter",
        "Execution Front Gate",
        "External Capability Front Gate",
        "Portfolio curation is a distinct use case",
        "Keep third-party payloads exact upstream by default",
        "Repository Posture Front Gate",
        "Status Mutation Front Gate",
        "Long Reasoning And Progress Reporting",
        "Manual selection of a Codex Skill, tool, plugin, MCP server, app, connector",
        "Do not commit, push, publish, delete, install, enable, deploy, migrate, update",
        "This starter must remain public-safe",
    ]:
        if phrase not in agents:
            fail(f"AGENTS.md missing public starter phrase: {phrase}")
    for forbidden in [
        "C:\\",
        "C:/",
        ".codex",
        ".agents",
        "yiheng8023",
        "OPENAI_API_KEY",
    ]:
        if forbidden in agents:
            fail(f"AGENTS.md contains private or runtime-specific marker: {forbidden}")


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
        "Independent Template Context",
        "independently usable public Codex-specific",
        "repository-owned structure, validation, and setup guidance",
        "request-intake and capability-routing boundaries",
    ]:
        if phrase not in english:
            fail(f"README.md missing system-context phrase: {phrase}")
    for phrase in [
        "独立模板定位",
        "可以独立使用的公开 Codex 专用配置模板",
        "本仓自有结构、验证和搭建说明",
        "请求入口与能力路由边界",
    ]:
        if phrase not in chinese:
            fail(f"README.zh-CN.md missing system-context phrase: {phrase}")

    for stale_name in ["agent-skills-curated"]:
        if stale_name in english or stale_name in chinese:
            fail(f"README files retain retired repository name: {stale_name}")

    for phrase in [
        "public-safe starter root `AGENTS.md`",
        "not a complete live instruction stack",
        "starter material to review and adapt deliberately",
    ]:
        if phrase not in english:
            fail(f"README.md missing AGENTS boundary phrase: {phrase}")

    for phrase in [
        "公开安全的根目录 `AGENTS.md` starter",
        "不是完整 live 指令栈",
        "谨慎适配",
    ]:
        if phrase not in chinese:
            fail(f"README.zh-CN.md missing AGENTS boundary phrase: {phrase}")


def verify_intake_boundary_docs() -> None:
    boundary = (ROOT / "docs" / "request-intake-and-capability-boundaries.md").read_text(
        encoding="utf-8"
    )
    for phrase in [
        "negative-boundary-first",
        "exclusionary boundary model",
        "documentation lookup for current",
        "Active instructions are not user-provided artifacts",
        "unnamed idea, plan",
        "candidate evidence, not automatic binding",
        "A user's assertion that a task is clear does not bind missing",
        "Capability routing starts only after the task contract exists",
        "External capability discovery, catalog lookup, installation prompts",
        "Portfolio curation is distinct from task-time expansion",
        "Keep third-party payloads exact upstream",
        "Probe tokens and exact test prompts are liveness or calibration aids only",
        "Apply the boundary by semantic class",
        "doing, viable, mature",
        "multiple plausible subjects",
        "intervening user instructions",
        "event-driven re-intake checkpoints",
    ]:
        if phrase not in boundary:
            fail(f"request-intake boundary doc missing phrase: {phrase}")

    sync_model = (ROOT / "docs" / "private-public-sync-model.md").read_text(encoding="utf-8")
    for phrase in [
        "probe-specific overfitting",
        "semantic class",
        "starter root `AGENTS.md` should be merged as reviewed",
        "may ship a public-safe starter root `AGENTS.md`",
        "Do not promote a private root `AGENTS.md` wholesale as a public root",
    ]:
        if phrase not in sync_model:
            fail(f"private-public sync model missing phrase: {phrase}")


def verify_example_config() -> None:
    example = (ROOT / "config" / "common.example.toml").read_text(encoding="utf-8")
    if "skills_curated" in example or "agent-skills-curated" in example:
        fail("common.example.toml retains retired curated-Skills topology")
    if "skill_policy_source" not in example:
        fail("common.example.toml must expose a neutral optional Skill policy source")


def verify_workflow_runtime() -> None:
    workflow = (ROOT / ".github" / "workflows" / "validate.yml").read_text(
        encoding="utf-8"
    )
    for action in ("actions/checkout@v7", "actions/setup-python@v7"):
        if action not in workflow:
            fail(f"validation workflow must use current action: {action}")


def main() -> None:
    verify_required_files()
    verify_public_agents_md()
    verify_manifest()
    verify_no_private_payloads()
    verify_language_links()
    verify_intake_boundary_docs()
    verify_example_config()
    verify_workflow_runtime()
    print("codex-user-config-template verification passed")


if __name__ == "__main__":
    main()
