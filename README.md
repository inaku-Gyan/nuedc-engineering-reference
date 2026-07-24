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

1. Agent 首次使用：根据 [Agent 模式](docs/agent-modes.md)初始化本地配置。
2. 查资料：先打开 [`catalog/README.md`](catalog/README.md)。
3. 查某个器件或工具：进入 `library/` 下对应的资料包，先读资料包的 `README.md`。
4. 查跨器件经验：进入 `knowledge/`。
5. 添加资料：遵循 [`docs/ingestion-guide.md`](docs/ingestion-guide.md)。
6. Agent 使用本仓库：遵循 [`AGENTS.md`](AGENTS.md)。

## Agent 模式配置

每个本地 checkout 首次由 Agent 使用前都必须创建被 Git 忽略的
`.agent-mode.yaml`。可以复制 [`.agent-mode.example.yaml`](.agent-mode.example.yaml)
自行配置；如果文件不存在，Agent 必须暂停原任务，依次询问模式、自动提交和自动
推送选项，展示最终 YAML 并在用户确认后创建。

支持四种模式：

- `readonly`：只读仓库，可联网核验；
- `curate-on-use`：把本次实际使用的现有原件按需整理成摘要或摘录；
- `autonomous`：资料缺失时围绕当前任务搜索、下载和整理入库；
- `maintainer`：允许主动的全库质量维护，重大删除或重组仍需确认。

配置格式、无效配置修复、临时权限提升和 Git 自动化规则见
[`docs/agent-modes.md`](docs/agent-modes.md)。

## 目录结构

```text
.
├── AGENTS.md                 # Agent 的检索、引用和上下文控制规则
├── .agent-mode.example.yaml  # 本地 Agent 模式配置模板
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
