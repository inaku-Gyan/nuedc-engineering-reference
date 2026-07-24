# Parent Repository Integration

当本知识库作为业务仓库的普通子目录或 Git Submodule 使用时，不应假设业务仓库中
启动的 Agent 会自动发现知识库内部的 `KNOWLEDGE_AGENT.md`。

以 Codex 为例，启动时会聚合从项目根到当前工作目录路径上的指令文件；更深层的
`AGENTS.md` 对其所在目录树具有作用域，但任意自定义知识库提示词不会因为存在就
自动进入业务仓库根目录任务的初始上下文：

- [Unrolling the Codex agent loop](https://openai.com/index/unrolling-the-codex-agent-loop/)
- [Introducing Codex](https://openai.com/index/introducing-codex/)

不同 Agent 对嵌套指令文件的发现策略可能不同。最稳妥的做法是在业务仓库根
`AGENTS.md` 中提供一个很短的触发式入口。

## 由脚本输出

在知识库根目录运行以下命令，可以把实际路径直接代入提示词并输出到 stdout：

```powershell
python configure_agent.py --print-integration-prompt third_party/nuedc-engineering-reference
```

默认输出推荐的父仓库 `AGENTS.md` 片段。输出单次用户提示词：

```powershell
python configure_agent.py --print-integration-prompt third_party/nuedc-engineering-reference --prompt-kind user
```

同时输出两种示例：

```powershell
python configure_agent.py --print-integration-prompt third_party/nuedc-engineering-reference --prompt-kind both
```

该命令不需要 `.agent-mode.json`，也不会创建或修改文件。

## 推荐：业务仓库 `AGENTS.md` 片段

将下面内容复制到业务仓库根 `AGENTS.md`，并把
`<NUEDC_REFERENCE_PATH>` 替换为实际相对路径，例如
`third_party/nuedc-engineering-reference`：

```markdown
## NUEDC engineering knowledge base

An Agent-oriented NUEDC engineering reference repository is available at `<NUEDC_REFERENCE_PATH>`.
It curates official manuals, datasheets, and other originals (usually PDFs) alongside
selective extracts, concise summaries, metadata, indexes, and source links. Its purpose is to help
Agents locate and verify reusable hardware and toolchain facts.

Consult it only when the task involves NUEDC, electronic components, development boards,
instruments, embedded toolchains, hardware design, measurement, or debugging:

1. If `<NUEDC_REFERENCE_PATH>/KNOWLEDGE_AGENT.md` exists, read and follow it before using or
   changing the knowledge base.
2. If that file is missing, treat the knowledge base as read-only, start from
   `<NUEDC_REFERENCE_PATH>/catalog/README.md`, and tell the user to run
   `python <NUEDC_REFERENCE_PATH>/configure_agent.py` before any knowledge-base update.
   next and open original PDFs only when exact verification is necessary.
3. Keep project-specific decisions in this business repository. Put only reusable
   engineering knowledge in the reference repository.

Do not preload or scan the knowledge base for unrelated tasks.
```

这段提示只负责“发现和路由”。详细的读取、整理、联网和 Git 权限仍来自知识库内
由 `configure_agent.py` 生成的本地 `KNOWLEDGE_AGENT.md`，因此不会把整套规则
重复放进业务仓库上下文。

## 单次用户提问示例

不方便修改业务仓库 `AGENTS.md` 时，可以在具体问题中附上：

```text
本任务需要查阅 NUEDC 工程知识库，路径为 `<NUEDC_REFERENCE_PATH>`。
这是面向 Agent 的电赛工程资料库，不是业务代码仓库。它集中保存官方 manual、datasheet 等原件（通常为 PDF），以及按需摘录、简明总结、元数据、索引和资料链接，用于低上下文地定位并核验可复用的软硬件与工具链知识。
请先读取该目录下的 `KNOWLEDGE_AGENT.md`；如果不存在，则只读使用 `catalog/README.md` 作为入口，不要修改知识库，并提醒我先运行该目录下的 `configure_agent.py`。
查找资料时依次阅读目录、资料包 README/meta、相关摘录，只有需要精确核验时才打开原始 PDF。
```

## Submodule 初始化

首次克隆业务仓库后：

```powershell
git submodule update --init --recursive
Set-Location <NUEDC_REFERENCE_PATH>
python configure_agent.py
Set-Location -
```

`.agent-mode.json` 和生成的 `KNOWLEDGE_AGENT.md` 都是 checkout 本地文件，不会
随 Submodule 提交传播。团队成员和独立 Agent 环境需要分别运行一次生成器。
