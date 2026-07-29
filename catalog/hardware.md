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

## 已入库资料

### MCU

- [ST STM32F405/407](../library/hardware/mcu/st/stm32f405-407/README.md)：
  168 MHz Cortex-M4F MCU 的 DS8626 Rev 12、RM0090 Rev 22 和 ES0182 Rev 19；
  包含 RoboMaster C 板所用 STM32F407IGH6TR 的资料入口。
- [TI MSPM0G3507](../library/hardware/mcu/ti/mspm0g3507/README.md)：
  MSPM0G350x 中文数据表 Rev. C，涵盖器件特性、引脚和电气参数。

### 开发板

- [DJI RoboMaster 开发板 C 型](../library/hardware/board/dji/robomaster-development-board-type-c/README.md)：
  STM32F407IGH6TR 控制板的 V1.0 原理图、供电、下载方式和接口 IO 速查。
- [立创·天猛星 MSPM0G3507](../library/hardware/board/lckfb/tmx-mspm0g3507/README.md)：
  板卡规格书、引脚复用图和三页原理图。

### 显示模块

- [金逸晨 GME12864-49～54](../library/hardware/display/goldenmorning/gme12864-49-54/README.md)：
  0.96 英寸 128 × 64 SSD1315 四针 I²C OLED，涵盖接口、地址推导、供电边界和
  随附 SPI 示例的不适用性。

### 传感器模块

- [WHEELTEC LF04](../library/hardware/sensor/wheeltec/lf04/README.md)：
  四路 940 nm 反射式巡线模块，涵盖通道/针位、比较器有效电平、阈值调节和
  3.3 V MCU 接口风险。

### 电机与执行器

- [DJI RoboMaster GM6020](../library/hardware/motor-control/dji/gm6020/README.md)：
  24 V 内置 FOC 驱动云台电机，涵盖额定参数、CAN/PWM 协议、拨码 ID 和反馈帧。
- [飞特 FT6335M](../library/hardware/motor-control/feetech/ft6335m/README.md)：
  360°磁编码 PWM 舵机规格、电气参数与控制速查。
- [MG370 12 V 约 1:34 GMR 版本](../library/hardware/motor-control/generic/mg370-gmr-12v-34/README.md)：
  来源未明随货资料中的电机参数和六针线序；PPR 仍须实测。

### 电机驱动

- [杭州中科微 AT8236](../library/hardware/motor-control/zhongkewei/at8236/README.md)：
  单通道有刷直流电机 H 桥驱动芯片，涵盖推荐/极限电流、PWM、限流和保护。
- [亚博 YB-MTNO3-V1.0](../library/hardware/motor-control/yahboom/yb-mtno3-v1.0/README.md)：
  双路 AT8236 成品板的接口、供电、控制协议和板级证据边界。
- [NXP PCA9685](../library/hardware/motor-control/nxp/pca9685/README.md)：
  16 路 12 位 I²C PWM 控制器的 7/8 位地址、预分频、Sleep/Wake 和 OE 安全关断。
