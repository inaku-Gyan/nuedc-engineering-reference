# Library

`library/` 保存围绕单一对象组织的一手资料包。分类依据是资料所描述的对象，
不是文件格式。

## 资料包结构

```text
<package>/
├── README.md       # Agent 默认读取的简短摘要
├── meta.yaml       # 标识、别名、标签、版本、来源和覆盖范围
├── originals/      # PDF 等原件
└── extracts/       # 按主题选择性提取的纯文本
```

可选目录：

- `images/`：从原件裁出的关键框图、时序图等，文件名须能对应来源页码。
- `examples/`：极小且有解释的官方示例或配置片段。
- `attachments/`：勘误表、应用说明、配套表格等非核心附件。

不要创建空目录；首次加入相应内容时再创建。

## 分类

- `hardware/`：器件、模块、开发板和仪器。
- `software/`：工具、SDK、库和软件平台。
- `standards/`：协议、接口、安全规范和行业标准。
- `competition/`：NUEDC 规则、赛题、官方说明及与具体届次有关的材料。

复制 `templates/reference-readme.md` 和 `templates/meta.yaml` 创建新资料包。

