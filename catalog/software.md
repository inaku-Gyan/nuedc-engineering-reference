# Software Catalog

软件资料按工具或项目组织在 `library/software/`。建议使用以下一级分类：

- `ide/`：集成开发环境
- `toolchain/`：编译器、链接器、构建系统与烧录工具
- `sdk/`：芯片或平台 SDK
- `library/`：第三方软件库、中间件和协议栈
- `debugging/`：调试器软件、GDB Server、分析工具
- `eda/`：原理图、PCB、仿真与信号完整性工具
- `measurement/`：数据采集、仪器控制与结果分析软件
- `automation/`：脚本工具、CI 和工程自动化

推荐层级为：

```text
library/software/<category>/<vendor-or-project>/<product>/
```

软件版本差异通常很重要。路径保持稳定，版本信息写入 `meta.yaml`，多个版本的
原件放在同一资料包内并在 `README.md` 中说明推荐版本与差异。

