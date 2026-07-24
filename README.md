# NUEDC Engineering Reference

面向电赛（NUEDC）项目与 Agents 的工程资料知识库。

本仓库保存：

- 芯片、模块、仪器、开发工具等的 manual、reference manual、datasheet 和官方文档；
- 资料原件（通常为 PDF）；
- 从原件中按实际需求提取的纯文本片段；
- 简短摘要、速查表、专题知识和故障排查记录；
- 无法或不适合归档原件时的可靠外部链接。

目标不是收集得最多，而是让人和 Agent 用尽量少的上下文，快速找到可信、可追溯、可复用的信息。

## 从哪里开始

1. Agent 首次使用：运行 `python configure_agent.py` 生成本地指令。
2. 查资料：先打开 [`catalog/README.md`](catalog/README.md)。
3. 查某个器件或工具：进入 `library/` 下对应的资料包，先读资料包的 `README.md`。
4. 查跨器件经验：进入 `knowledge/`。
5. 添加资料：遵循 [`docs/ingestion-guide.md`](docs/ingestion-guide.md)。

## Agent 本地设置

每个本地 checkout 首次由 Agent 使用前，先运行无第三方依赖的交互脚本：

```powershell
python configure_agent.py
```

用户选择权限和 Git 行为后，脚本会生成被 Git 忽略的 `.agent-mode.json` 和根
`AGENTS.md`。Agent 只读取已经展开的当前规则，不需要加载、校验或理解不同权限
预设。再次运行脚本可以修改选择或刷新提示词。

完整设置方法和四种权限预设见 [`docs/agent-setup.md`](docs/agent-setup.md)。

## 作为业务仓库的子目录

业务仓库从根目录启动 Agent 时，不应依赖 Agent 自动发现任意子目录或 Submodule
内部的 `AGENTS.md`。建议在业务仓库根 `AGENTS.md` 中加入一个短的触发式入口：
只有任务涉及电赛、器件、工具链或硬件调试时，才读取本知识库的本地指令并从
`catalog/README.md` 开始。

可直接复制的父仓库片段、单次用户提示词和 Submodule 初始化命令见
[`docs/parent-repository-integration.md`](docs/parent-repository-integration.md)。

## 目录结构

```text
.
├── agent-policy/             # 生成 Agent 提示词的受控规则分片
├── configure_agent.py        # 本地提示词配置与生成工具
├── .agent-mode.example.json  # 本地配置格式示例
├── catalog/                  # 全库轻量入口与导航，不存长篇正文
│   ├── README.md
│   ├── hardware.md
│   ├── software.md
│   ├── knowledge.md
│   └── external-links.md
├── library/                  # 按“对象/主题”组织的一手资料包
│   ├── hardware/
│   ├── software/
│   ├── standards/
│   └── competition/
├── knowledge/                # 跨资料的二次整理、经验与专题知识
│   ├── quick-reference/
│   ├── design-guides/
│   ├── troubleshooting/
│   └── workflows/
├── inbox/                    # 新资料的临时待整理区
├── templates/                # 资料包、摘录和知识文章模板
└── docs/                     # 仓库维护规则与结构说明
```

## 核心组织方式

### 1. 主题优先，而不是文件类型优先

同一对象的 PDF、摘要、摘录和链接放在同一个资料包中。例如：

```text
library/hardware/mcu/stmicroelectronics/stm32f103/
├── README.md
├── meta.yaml
├── originals/
│   ├── rm0008-rev21-reference-manual.pdf
│   └── stm32f103x8-b-datasheet.pdf
└── extracts/
    ├── gpio.md
    └── timers.md
```

这样查询某个器件时不需要在 `pdf/`、`text/`、`summary/` 等多个目录之间跳转。

### 2. 每个资料包分三层

- `README.md`：最小可用知识胶囊。说明它是什么、何时使用、关键结论、资料覆盖范围和入口。
- `extracts/`：仅提取高频、重要、实际使用过或 PDF 难以检索的内容，并保留页码/章节来源。
- `originals/`：权威原件，供核验细节；默认不应让 Agent 整份读取。

`meta.yaml` 提供稳定标识、别名、标签、版本和来源等机器可读信息。

### 3. 一手资料与二次知识分离

- `library/` 回答“官方资料怎么说”，一个资料包对应一个产品、工具、标准或赛题资料对象。
- `knowledge/` 回答“实践中应该怎么做”，可以综合多个资料包，但必须列出依据。

### 4. 控制上下文，而不是追求全文化

- 不默认对所有 PDF 做全文 OCR 或全文 Markdown 转换。
- 摘录按问题或功能拆分，单文件只解决一个清晰主题。
- 摘要不复制大段原文；写结论、限制条件、关键参数和来源定位。
- 原件更新后，要标记摘要和摘录是否仍然有效。

## 命名约定

- 路径和文件名使用小写 ASCII `kebab-case`，正文可使用中文。
- 厂商使用稳定的官方英文名，例如 `st`, `ti`, `analog-devices`。
- 型号目录使用可搜索的规范型号，例如 `stm32f103`、`ads1115`。
- 原件文件名包含型号、文档类型和版本，例如
  `stm32f103x8-b-datasheet-rev19.pdf`。
- 每个资料包有全库唯一的 `id`，例如 `hw-mcu-st-stm32f103`。
- 不在路径里编码容易变化的信息，如当前版本号、年份或“最新”。

## 大文件

PDF、压缩包、原理图工程等二进制文件建议使用 Git LFS。仓库已在
`.gitattributes` 中提供常见规则。公开可访问的官方工程资料在许可未明确时可以
归档，但必须在元数据中标记 `redistribution: unknown`；付费、需登录、保密或
明确限制传播的资料不得归档，只保存允许公开的链接和元数据。
