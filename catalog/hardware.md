# Hardware Catalog

硬件资料按对象类型组织在 `library/hardware/`。建议使用以下一级分类：

- `mcu/`：微控制器及配套参考资料
- `processor/`：MPU、DSP、FPGA、SoC
- `analog/`：运放、比较器、ADC、DAC、模拟前端
- `power/`：稳压、电源管理、驱动与功率器件
- `sensor/`：各类传感器及测量前端
- `communication/`：有线、无线通信芯片与模块
- `motor-control/`：电机、编码器及驱动器
- `display/`：显示屏、显示控制器与人机交互器件
- `module/`：难以归入单颗器件的成品模块
- `board/`：开发板、核心板与评估板
- `instrument/`：示波器、万用表、电源、逻辑分析仪等
- `component/`：连接器、磁性元件、无源器件等

实际目录按需创建，不需要提前建立所有空目录。对象目录的推荐层级为：

```text
library/hardware/<category>/<vendor>/<model>/
```

无明确厂商的通用主题不应伪造 `vendor`；应优先写入 `knowledge/`，或使用
明确的 `generic/` 并在元数据中说明。

