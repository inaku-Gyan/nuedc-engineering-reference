# DJI RoboMaster 开发板 C 型

> 面向 RoboMaster 机器人控制的 STM32F407 开发板，集成双 CAN、UART、PWM、
> DBUS、USB、DCMI、BMI088 与 IST8310。资料包用于核对板级供电、接口、下载方式
> 和 MCU 连接关系；芯片寄存器与电气限制应转查 STM32F405/407 资料包。

## 快速定位

- 产品：RoboMaster 开发板 C 型
- 厂商：深圳市大疆创新科技有限公司（DJI / RoboMaster）
- 主控：`STM32F407IGH6TR`（原理图 U12）
- 硬件资料版本：原理图 V1.0，2019-12-05
- 资料包 ID：`hw-board-dji-robomaster-development-board-type-c`

## 板载资源概览

- 8–28 V 直流输入，带防反接、缓启动和输入过压关断；
- 三路 24 V 电源输出；
- 7 路 5 V PWM 输出，合计最大 5 A；
- CAN1、CAN2 各两个物理接口，最高 1 Mbit/s；
- 两路 UART、一路 DBUS、一路可配置 I2C/SPI 扩展接口；
- USB 2.0 全速接口，可用于通信、有限供电和 DFU 下载；
- SWD 下载/调试接口；
- 8 位 DCMI 数字摄像头接口；
- BMI088 六轴 IMU、IST8310 三轴磁力计、IMU 加热电路；
- RGB 用户 LED、用户键、蜂鸣器和电池电压检测。

产品页给出的结构参数为 60 × 41 × 16 mm、38 g，工作温度 0–55 ℃。

## 资料入口

| 需求 | 推荐入口 | 来源定位 |
| --- | --- | --- |
| 接口、IO 和供电速查 | [板级接口与供电摘录](extracts/interfaces-power-and-debug.md) | 原理图 Sheet 2–8 |
| 接口线序、功能说明和参数表 | [v1.0 用户手册](originals/robomaster-development-board-type-c-user-manual-v1.0-zh-cn-unlocked.pdf) | PDF 第 3–20 页 |
| 完整连接与元件参数 | [V1.0 原理图](originals/robomaster-development-board-type-c-schematic-v1.0.pdf) | PDF 第 1–7 页，对应 Sheet 2–8 |
| MCU 特性、电气参数和引脚 | [ST STM32F405/407](../../../mcu/st/stm32f405-407/README.md) | DS8626 Rev 12 |
| 外设寄存器和工作方式 | [ST STM32F405/407](../../../mcu/st/stm32f405-407/README.md) | RM0090 Rev 22 |
| 产品规格与官方入口 | [RoboMaster 产品页](https://www.robomaster.com/zh-CN/products/components/general/development-board-type-c) | 技术参数、FAQ |

## 覆盖范围

已覆盖：

- 主控型号、主要板载资源和物理接口；
- 电源树、输入保护、USB/SWD/DFU 下载路径；
- 常用接口与 STM32 IO 的对应关系；
- 原理图和用户手册的版本、来源与许可边界。

尚未整理：

- PCB、BOM、封装库和不同硬件批次差异；
- 全部元件参数与测试点；
- 官方例程、SDK 和出厂固件；
- 传感器芯片各自的数据手册。

## 使用注意

- 原理图 PDF 只有 7 页，标题栏页码从 Sheet 2 开始，未包含 Sheet 1。
- 丝印 `UART1`、`UART2` 与 STM32 外设编号不一致；见接口摘录。
- USB 供电不连接舵机使用的 `VCC_5V_M`，不能由 USB 给 7 路 PWM 接口供电。
- 可配置 I2C/SPI 接口的 5 V/3.3 V 选择需要改焊 0 Ω 电阻，不能只靠软件切换。

## 官方入口

- [RoboMaster 开发板 C 型产品页](https://www.robomaster.com/zh-CN/products/components/general/development-board-type-c)
- [RoboMaster GitHub 组织](https://github.com/RoboMaster)
