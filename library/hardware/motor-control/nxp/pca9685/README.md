# NXP PCA9685

> 16 路、12 位、统一频率的 I²C PWM 控制器。当前资料包适合核对寄存器、地址、
> 预分频、休眠/唤醒和 OE 安全关断；成品舵机板的 V+ 额定值仍须按具体板卡确认。

## 快速定位

- 型号：PCA9685
- 厂商：NXP Semiconductors
- 资料包 ID：`hw-motor-control-nxp-pca9685`
- 当前控制文档：NXP Product data sheet Rev. 4，2015-04-16
- 本地历史原件：Rev. 3，2010-09-02

## 关键结论

- 逻辑电源 VDD 为 2.3–5.5 V，I²C 支持 Fast-mode Plus 1 MHz；
- 16 路输出共享一个 PWM 频率，每路 12 位、独立设置 ON/OFF 计数；
- 内部振荡器标称 25 MHz，允许使用最高 50 MHz 的外部时钟；
- 12 位计数的占空比步进为 `1/4096`（约 0.0244 个百分点），就近取整的量化
  误差不超过半步；但数据手册只给出内部振荡器 25 MHz 典型值，没有给出频率
  容差，因此不保证 PWM 频率和绝对脉宽的总体误差上限；
- Rev.4 的可编程频率为典型 24–1526 Hz；本地 Rev.3 写的是 40–1000 Hz，
  新设计应以 Rev.4 为准；
- PRE_SCALE 只能在 MODE1.SLEEP=1 时写；清除 SLEEP 后振荡器最多需要 500 μs
  稳定；
- OE 低有效，可异步关闭全部输出。把 OE 接到 MCU 并用上拉保证上电禁用，能为
  I²C 故障提供寄存器以外的关断路径。

## 资料入口

| 需求 | 推荐入口 | 来源定位 |
| --- | --- | --- |
| 地址、寄存器和安全初始化 | [寄存器与安全初始化摘录](extracts/registers-and-safe-init.md) | Rev.4 第 7.1–7.5 节 |
| 当前完整数据手册 | [NXP Rev.4 官方 PDF](https://www.nxp.com/docs/en/data-sheet/PCA9685.pdf) | 全文 |
| 历史版本差异 | [本地 Rev.3](originals/pca9685-datasheet-rev3.pdf) | 第 1、7 章 |
| 通用 16 路模块电路参考 | [来源未明原理图](originals/generic-16-channel-servo-module-schematic.pdf) | 单页 |

## 覆盖范围

已覆盖：

- 逻辑电气边界、I²C 地址、寄存器和输出语义；
- 预分频计算、Sleep/Wake 初始化与 OE 安全策略；
- Rev.3 和 Rev.4 的频率范围差异；
- inbox 通用模块原理图的来源限制。

尚未整理：

- 具体商品模块的厂商、PCB 版本、V+ 铜箔与连接器载流能力；
- 板载振荡器误差、舵机电源纹波和多舵机同时动作实测；
- 外部时钟同步。

## 使用注意

- PCA9685 的 VDD 额定值不等于舵机板 V+ 端子的额定值。V+ 常绕过芯片直接给
  舵机供电，其连接器、电容和铜箔必须另行核对。
- 25 MHz 只是内部振荡器典型值而非有上下限保证的精密时基；需要精确脉宽时应
  测量实际 PWM 周期并回填振荡频率，或使用满足精度要求的外部时钟。
- 默认单颗七位地址是 `0x40`；默认 LED All Call 七位地址是 `0x70`，上电启用，
  不能当作单颗器件地址。`0x78`–`0x7F` 是 I²C 保留地址，标准系统应避免；
  NXP 仅允许在完全封闭、由设计者控制的总线上把它们当普通地址使用。
- 本地模块原理图没有可追溯厂商和公开来源，只能用于识别常见电路结构，不能
  证明手中模块的版本、电气额定值或再分发许可。

## 官方入口

- [PCA9685 产品页](https://www.nxp.com/products/power-drivers/lighting-driver-and-controller-ics/led-drivers/16-channel-12-bit-pwm-fm-plus-ic-bus-led-driver:PCA9685)
- [PCA9685 Rev.4 数据手册](https://www.nxp.com/docs/en/data-sheet/PCA9685.pdf)
