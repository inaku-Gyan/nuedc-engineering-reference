# Parent Repository Integration

当本知识库作为业务仓库的普通子目录或 Git Submodule 使用时，不应假设业务仓库中
启动的 Agent 会自动发现知识库内部的 `AGENTS.md`。

以 Codex 为例，启动时会聚合从项目根到当前工作目录路径上的指令文件；更深层的
`AGENTS.md` 对其所在目录树具有作用域，但任意子目录中的文件不会因为存在就自动
进入业务仓库根目录任务的初始上下文：

- [Unrolling the Codex agent loop](https://openai.com/index/unrolling-the-codex-agent-loop/)
- [Introducing Codex](https://openai.com/index/introducing-codex/)

不同 Agent 对嵌套指令文件的发现策略可能不同。最稳妥的做法是在业务仓库根
`AGENTS.md` 中提供一个很短的触发式入口。

## 推荐：业务仓库 `AGENTS.md` 片段

将下面内容复制到业务仓库根 `AGENTS.md`，并把
`<NUEDC_REFERENCE_PATH>` 替换为实际相对路径，例如
`third_party/nuedc-engineering-reference`：

```markdown
## NUEDC engineering knowledge base

A reusable NUEDC engineering knowledge base is available at
`<NUEDC_REFERENCE_PATH>`.

Use it only when the task involves NUEDC, electronic components, development boards,
instruments, embedded toolchains, hardware design, measurement, or debugging:

1. If `<NUEDC_REFERENCE_PATH>/AGENTS.md` exists, read and follow it before using or
   changing the knowledge base.
2. If that file is missing, treat the knowledge base as read-only, start from
   `<NUEDC_REFERENCE_PATH>/catalog/README.md`, and tell the user to run
   `python <NUEDC_REFERENCE_PATH>/configure_agent.py` before any knowledge-base update.
3. Follow catalog links to a package `README.md` and `meta.yaml`; read focused extracts
   next and open original PDFs only when exact verification is necessary.
4. Cite repository-relative paths and original document pages/chapters for exact claims.
5. Keep project-specific decisions in this business repository. Put only reusable
   engineering knowledge in the reference repository.

Do not preload or scan the knowledge base for unrelated tasks.
```

这段提示只负责“发现和路由”。详细的读取、整理、联网和 Git 权限仍来自知识库内
由 `configure_agent.py` 生成的本地 `AGENTS.md`，因此不会把整套规则重复放进业务
仓库上下文。

## 单次用户提问示例

不方便修改业务仓库 `AGENTS.md` 时，可以在具体问题中附上：

```text
本任务需要查阅 NUEDC 工程知识库，路径为
`<NUEDC_REFERENCE_PATH>`。

请先读取该目录下的 `AGENTS.md`；如果不存在，则只读使用
`catalog/README.md` 作为入口，不要修改知识库，并提醒我先运行该目录下的
`configure_agent.py`。查找资料时依次阅读目录、资料包 README/meta、相关摘录，
只有需要精确核验时才打开原始 PDF。回答中的精确参数请给出知识库相对路径以及
原件页码或章节。
```

## Submodule 初始化

首次克隆业务仓库后：

```powershell
git submodule update --init --recursive
Set-Location <NUEDC_REFERENCE_PATH>
python configure_agent.py
Set-Location -
```

`.agent-mode.json` 和生成的 `AGENTS.md` 都是 checkout 本地文件，不会随 Submodule
提交传播。团队成员和独立 Agent 环境需要分别运行一次生成器。
