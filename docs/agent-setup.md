# Agent Setup

本仓库不要求 Agent 在运行时读取或判断模式。用户先通过交互脚本选择一组权限，
脚本再把对应规则展开为本地 `KNOWLEDGE_AGENT.md`。Agent 只看到当前生效的知识库
指令。

## 首次设置

需要 Python 3.10 或更高版本，无第三方依赖。在仓库根目录运行：

```powershell
python configure_agent.py
```

脚本会依次：

1. 选择权限预设；
2. 在允许写入时选择是否自动提交；
3. 在自动提交开启时选择是否自动推送；
4. 展示权限、Git 副作用和生成文件；
5. 确认后写入 `.agent-mode.json` 与 `KNOWLEDGE_AGENT.md`。

这两个文件均被 Git 忽略，每个 checkout 或 Submodule 工作树需要单独生成。

如果知识库位于业务仓库的子目录，业务仓库根目录启动的 Agent 不一定会自动发现
这里生成的 `KNOWLEDGE_AGENT.md`。请同时按
[`parent-repository-integration.md`](parent-repository-integration.md) 在父仓库中
声明知识库入口。

## 权限预设

### 只读

Agent 可以查询本地资料和联网核验，但不能持久修改仓库、提交或推送。

### 按需整理

Agent 可以把本次实际使用且具有复用价值的现有原件整理为摘要或专题摘录，但不能
下载或归档新原件。

### 自主补全

本地资料不足以回答当前任务时，Agent 可以搜索、下载和整理直接相关的官方资料，
创建完整资料包并更新索引。不得无界扩展相邻主题。

### 维护

在自主补全基础上允许主动核验元数据、版本、链接、重复项和目录一致性。删除原件、
替换版本、批量移动或重大结构调整仍要求 Agent 先征得用户确认。

## Git 选项

- `auto_commit: false`：改动保留在工作区，不自动提交或推送。
- `auto_commit: true, auto_push: false`：校验后创建本地提交，不推送。
- `auto_commit: true, auto_push: true`：校验、提交并推送任务开始时所在的当前分支。

只读预设强制两个选项均为 `false`。禁止 `auto_commit: false` 与
`auto_push: true` 的组合。

## 重新生成与检查

再次运行交互脚本时，可以沿用当前配置重新生成，或修改选择：

```powershell
python configure_agent.py
```

检查配置是否合法、生成提示词是否被手工改动或已经过期：

```powershell
python configure_agent.py --check
```

检查命令不修改任何文件，匹配时退出码为 `0`，缺失、配置无效或提示词不一致时
退出码为 `2`。

为父仓库输出已代入路径的集成提示词：

```powershell
python configure_agent.py --print-integration-prompt third_party/nuedc-engineering-reference
```

完整选项见
[`parent-repository-integration.md`](parent-repository-integration.md)。

## 受版本控制的规则源

生成器从 `agent-policy/` 中组合公共检索、按需整理、资料获取、维护和 Git 行为
分片。修改分片或生成器后，重新运行脚本即可刷新本地
`KNOWLEDGE_AGENT.md`。

生成稿不包含预设名、配置分支或其他预设的说明。它可以说明自己由设置工具生成，
但 Agent 无需读取配置或模式手册。
