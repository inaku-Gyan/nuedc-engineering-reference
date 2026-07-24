# Repository Development Instructions

本文件用于开发和维护本仓库本身。面向知识库查询、按需整理和资料获取的本地规则
由 `configure_agent.py` 生成到 `KNOWLEDGE_AGENT.md`。

## Knowledge operations

- 查询或修改 `catalog/`、`library/`、`knowledge/`、`inbox/` 前，先读取并遵循
  `KNOWLEDGE_AGENT.md`。
- 如果该文件不存在，将知识库视为只读，并提醒用户运行
  `python configure_agent.py`；不要替用户选择权限。
- 不要手工修改 `KNOWLEDGE_AGENT.md` 或 `.agent-mode.json`，应重新运行生成器。

## Repository development

- 策略源位于 `agent-policy/`，生成器为根目录 `configure_agent.py`。
- 修改生成器、策略分片、配置格式或集成提示词时，同步更新相关文档与测试。
- 保持生成提示词精简，只组合当前选择需要的能力。
- 保持 Python 3.10+ 标准库实现，不无故引入第三方依赖。
- 保留用户已有修改，不使用破坏性 Git 操作。

## Validation

- 运行：`python -m unittest discover -s tests -v`
- 检查 Markdown 本地链接和 `git diff --check`。
- 本地配置存在时运行：`python configure_agent.py --check`
