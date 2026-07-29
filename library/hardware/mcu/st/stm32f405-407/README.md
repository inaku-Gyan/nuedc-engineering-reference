# ST STM32F405/407

> 最高 168 MHz 的 Arm Cortex-M4F 微控制器系列。资料包归档数据手册、参考手册
> 和器件勘误表，适合核对器件能力、引脚、电气参数、外设寄存器和芯片限制；
> RoboMaster C 型开发板使用其中的 `STM32F407IGH6TR`。

## 快速定位

- 对象：STM32F405xx、STM32F407xx
- 厂商：STMicroelectronics
- 资料包 ID：`hw-mcu-st-stm32f405-407`
- 数据手册：DS8626 Rev 12，2026-03
- 参考手册：RM0090 Rev 22，2026-05
- 勘误表：ES0182 Rev 19，2026-07

## 关键能力

DS8626 Rev 12 第 1–2 页给出的系列级能力包括：

- Arm Cortex-M4，单精度 FPU 与 DSP 指令，最高 168 MHz；
- 最高 1 MB Flash；
- 最高 192 KB SRAM，另有 4 KB 备份 SRAM；其中包含 64 KB CCM RAM；
- 1.8–3.6 V 应用供电与 IO；
- 三个 12 位 2.4 MSPS ADC、两个 12 位 DAC；
- 最多 17 个定时器、两个 32 位通用定时器；
- 最多 3×I2C、4×USART、2×UART、3×SPI、2×CAN、SDIO；
- USB OTG FS、USB OTG HS、10/100 Ethernet 和 DCMI；
- SWD、JTAG 和 ETM 调试/跟踪接口。

具体资源随型号、封装和存储容量变化，不能把系列最大值直接当作每颗器件的保证值。

## 资料入口

| 需求 | 推荐入口 | 来源定位 |
| --- | --- | --- |
| 系列特性、型号和封装 | [DS8626 数据手册](originals/stm32f405-407-datasheet-ds8626-rev12.pdf) | 第 1–20 页 |
| 引脚、复用和存储映射 | [DS8626 数据手册](originals/stm32f405-407-datasheet-ds8626-rev12.pdf) | 第 4–5 章 |
| 编码器定时器、PWM 与 C 板相关复用 | [定时器编码器与 PWM 能力](extracts/timer-encoder-and-pwm-capabilities.md) | DS8626 第 3.21 节、Table 9；RM0090 第 17.3.16 节 |
| 电气与时序参数 | [DS8626 数据手册](originals/stm32f405-407-datasheet-ds8626-rev12.pdf) | 第 6 章 |
| 寄存器和外设工作方式 | [RM0090 参考手册](originals/stm32f4-reference-manual-rm0090-rev22.pdf) | 按外设章节查询 |
| 已知芯片限制与规避方式 | [ES0182 勘误表](originals/stm32f405-407-errata-es0182-rev19.pdf) | 第 1–2 章 |
| C 板的接口连接 | [RoboMaster C 型开发板](../../../board/dji/robomaster-development-board-type-c/README.md) | 原理图 V1.0 |

## 文档适用范围

- DS8626 专用于 STM32F405xx、STM32F407xx。
- ES0182 同时适用于 STM32F405/407xx 和 STM32F415/417xx；应用限制前必须
  读取器件硅版本。第 1 页给出封装标记与 `DBGMCU_IDCODE.REV_ID` 的对应关系。
- RM0090 同时覆盖 STM32F405/415、STM32F407/417、STM32F427/437 和
  STM32F429/439。查寄存器前应先核对该外设是否存在于目标型号。
- RoboMaster C 板原理图 U12 标注为 `STM32F407IGH6TR`，属于 DS8626 中的
  STM32F407IG 器件。

## 覆盖范围

已覆盖：

- 文档版本、适用系列和各文档的查询职责；
- STM32F405/407 系列定位与主要能力；
- C 板精确 MCU 型号与器件资料的关联；
- 定时器硬件编码器/PWM 能力及 C 板相关引脚复用；
- 勘误表按硅版本使用的基本要求。

尚未整理：

- 各封装的完整引脚与复用速查；
- 时钟树、DMA、CAN、USB 等专题摘录；
- 电气设计检查表；
- ES0182 全部限制的中文索引；
- Cortex-M4 编程手册 PM0214 与启动加载器应用笔记。

## 使用注意

- STM32F407 与 STM32F401 不是同一器件系列，数据手册和参考手册不能混用。
- RM0090 描述功能和寄存器，封装引脚与电气极限仍应以 DS8626 为准。
- ES0182 Rev 19 列出多个对所有硅版本都适用的限制；量产固件不能只依据
  RM0090 编写而忽略勘误。
- `STM32F407IGH6TR` 的完整后缀包含容量、封装、温度等级和交付形式信息；
  采购或替换器件时必须核对完整料号。

## 官方入口

- [STM32F407 产品页](https://www.st.com/en/microcontrollers-microprocessors/stm32f407-417.html)
- [STM32F4 系列文档中心](https://www.st.com/en/microcontrollers-microprocessors/stm32f4-series/documentation.html)
