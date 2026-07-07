# codex-user-config-template

[English](README.md) | 简体中文

这是一个公开安全模板，用来帮助用户创建自己的私有 Codex 用户配置仓；它不发布个人记忆、偏好、凭据、账号状态或本机运行时细节。

它是 Codex 专用的公开模板：用公开安全模板承载可复用结构，用私有 overlay 保存真实
记忆、偏好、凭据、本机路径、安装状态、备份、验证、恢复和回滚。跨运行时适配不属于本仓范围。

## 从这里开始

| 你想做什么 | 入口 |
| --- | --- |
| 创建自己的私有 Codex 配置仓 | 把本仓作为公开安全起点 |
| 判断哪些内容可以复制 | 查看 [`docs/`](docs) 以及 `config/`、`memory/`、`skills/` 下的占位示例 |
| 查看公开安全的指令入口草案 | [`AGENTS.md`](AGENTS.md) |
| 保留请求入口与能力路由边界 | [`docs/request-intake-and-capability-boundaries.md`](docs/request-intake-and-capability-boundaries.md) |
| 验证模板是否安全 | `python -B scripts/verify.py` |
| 理解整套系统 | [`open-resource-governance/docs/system-topology.md`](https://github.com/yiheng8023/open-resource-governance/blob/main/docs/system-topology.md) |

## 系统位置

本仓库是
[`open-resource-governance`](https://github.com/yiheng8023/open-resource-governance)
生态中的公开 Codex 专用配置模板链路。它展示的是更大公开/私有配置模型中的 Codex 公开模板侧。

```text
open-resource-governance
  -> 负责整个仓库家族地图和公开/私有规则

codex-user-config-template
  -> 提供公开安全结构、占位符、验证和搭建说明

私有 codex-user-config
  -> 负责真实 Codex 记忆快照、偏好、安装策略、备份和回滚

agent-skills-curated
  -> 可发布已审查 Skill 版本，由私有 Codex 配置仓消费
```

如果你需要安全起点，从本仓开始即可。若要理解更大的系统关系，请看总仓拓扑：
[`open-resource-governance/docs/system-topology.md`](https://github.com/yiheng8023/open-resource-governance/blob/main/docs/system-topology.md)。

## 仓库职责

本仓库是模板，不是真实用户配置。它提供安全边界清晰、结构可迁移、可验证的私有 Codex
配置仓起点，并且只面向 Codex 专用文件和工作流，同时去掉私有内容。

本仓库提供一个公开安全的根目录 `AGENTS.md` starter。它是请求入口、外部能力边界、
推理节律与收尾覆盖的公开安全底座，不是完整 live 指令栈、个人记忆、凭据载体，也不是
用户已有 `AGENTS.md` 的整体替代品。使用时应作为起点或经审查的增量材料，谨慎适配。

## 本仓库提供什么

- 面向私有 Codex 配置基线的公开安全目录结构。
- 只包含占位符的示例配置。
- 用于检查公开安全与结构有效性的验证脚本。
- 关于公开/私有同步、许可证边界和私有仓搭建的说明。
- 公开安全的请求入口与能力路由边界说明，可作为经审查的增量内容吸收进私有仓的
  `AGENTS.md`、入口 Skill、路由 Skill 与验证样例。
- 公开安全的根目录 `AGENTS.md` starter，避免私有记忆、本机路径、凭据、账号状态和
  运行时专属假设。

## 本仓库不负责什么

- 真实 Codex 记忆快照。
- 个人偏好、提示词、账号选择或本机路径。
- OAuth 状态、凭据、token、cookie、浏览器会话、日志、缓存或 app 运行状态。
- 第三方 Skill 正文治理；这应由精选 Skills 仓负责。
- 资源发现、评分或生命周期治理；这应由资源雷达仓负责。

## 与私有配置仓的关系

推荐模型：

```text
codex-user-config-template
  -> 提供公开安全结构、文档、占位示例和验证

private codex-user-config
  -> 以模板为起点
  -> 拥有真实偏好、记忆快照、本地安装策略、备份、验证和回滚
  -> 未经严格脱敏与审查，不应公开
```

公开到私有的同步可以自动化；私有到公开的提升必须经过过滤、审查和人工批准。

不要对活指令文件做盲目双向同步。如果用户已经有根目录 `AGENTS.md`，必须保留用户本地
偏好、权限边界以及已有项目或用户规则。公开 starter `AGENTS.md` 可以作为初始底座或
经审查的更新来源，但不应自动覆盖已有配置。

## 与整体体系的关系

本模板是模块化资源治理体系中的一条链路：

- `resource-radar` 负责发现和评估公开资源。
- `agent-skills-curated` 负责已审查 Skill 正文和发布清单。
- 书签仓负责公开安全来源目录；私有书签仓保留私有内容。
- 私有用户配置仓负责真实环境的安装、验证和运行。

## 目录结构

```text
config/                  占位示例配置
AGENTS.md                公开安全的 starter 指令入口
docs/                    公开/私有、入口/路由边界与搭建说明
hooks/                   Hook 策略占位，不是真实运行中的自动化
memory/                  记忆边界占位，不是真实记忆
scripts/verify.py        公开安全与结构验证
skills/                  Skill 安装策略占位，不复制 Skills 正文
```

## 验证方式

运行：

```bash
python -B scripts/verify.py
```

GitHub Actions 会在 pull request 和推送到 `main` 时运行同样的验证。

## 更新规则

1. 默认保持公开安全。
2. 只加入占位符、示例、数据格式、脚本和通用文档。
3. 不要把私有配置、记忆、凭据、本机路径、账号状态或个人偏好文件复制进来。
4. 私有仓中的可复用改进，只有经过过滤、审查、公开安全确认后才能提升到这里。

## 安全边界

真实私有配置仓才是用户实际环境的权威。本仓库只是脚手架。任何可能暴露个人信息、账号状态、私有偏好或本地运行时细节的内容，都应留在私有仓之外。
