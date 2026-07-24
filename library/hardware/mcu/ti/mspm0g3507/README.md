# TI MSPM0G3507

> 80 MHz Arm Cortex-M0+ 混合信号 MCU，集成双 4 MSPS ADC、DAC、模拟前端、
> CAN-FD 和丰富定时器。当前资料包只归档数据表，适合核对器件能力、封装、
> 引脚、电气参数和订购型号；外设寄存器与模块行为还需要技术参考手册。

## 快速定位

- 对象：MSPM0G3505 / MSPM0G3506 / MSPM0G3507
- 厂商：Texas Instruments
- 资料包 ID：`hw-mcu-ti-mspm0g3507`
- 本地文档：中文数据表 Rev. C，文档编号 ZHCSSC4C
- 英文控制文档：SLASEX6 Rev. C
- 数据表标注：2023 年 2 月发布，2025 年 10 月修订

## MSPM0G3507 关键能力

以下为数据表第 1–2 页的器件级概览：

- Arm Cortex-M0+，最高 80 MHz；
- 128 KB 带 ECC 的 Flash，32 KB 带硬件奇偶校验的 SRAM；
- 1.62–3.6 V，工作温度范围 −40–125 °C；
- 两个 12 位 4 MSPS 同步采样 ADC，合计最多 17 个外部通道；
- 一个 12 位 1 MSPS DAC、两个零漂移运放、一个通用放大器和三个比较器；
- 7 通道 DMA、数学加速器、7 个定时器，最多 22 路 PWM；
- 4×UART、2×I2C、2×SPI、1×CAN 2.0/FD；
- MSPM0G3507 为 128 KB Flash / 32 KB SRAM，提供 28–64 引脚封装，
  不同封装的 GPIO 和模拟通道数量不同。

## 资料入口

| 需求 | 推荐入口 | 来源定位 |
| --- | --- | --- |
| 器件特性和系列差异 | 本文件 | 数据表第 1–2 页 |
| 引脚与复用功能 | [中文数据表](originals/mspm0g350x-datasheet-zh-rev-c.pdf) | 第 4–23 页 |
| 电气与时序参数 | [中文数据表](originals/mspm0g350x-datasheet-zh-rev-c.pdf) | 第 28–81 页 |
| 封装与订购信息 | [中文数据表](originals/mspm0g350x-datasheet-zh-rev-c.pdf) | 第 84 页起 |
| 寄存器和模块行为 | 尚未归档的技术参考手册 | TI 产品页 |

## 覆盖范围

已覆盖：

- MSPM0G350x 的定位和 MSPM0G3507 主要资源；
- 本地数据表的版本、文档编号和官方入口。

尚未整理：

- MSPM0 G 系列 80 MHz 技术参考手册；
- MSPM0G350x 勘误表；
- 具体封装的引脚速查和外设复用表；
- 电源、时钟、调试和启动模式的设计检查表。

## 使用注意

- 中文数据表首页明确说明：译文可能使用自动化工具，精确性应以最新英文版
  SLASEX6 为准。
- 型号后缀决定封装；引用引脚号或 GPIO 数量时必须同时确认完整料号。
- 数据表用于器件级参数。寄存器配置、外设工作模式等问题不要仅凭本文件推断。
- TI 的技术参考手册和勘误表可能比本资料包中的数据表更新，关键设计应在 TI
  产品页复核。

## 官方入口

- [MSPM0G3507 产品页](https://www.ti.com.cn/product/zh-cn/MSPM0G3507)
- [中文数据表在线版](https://www.ti.com.cn/document-viewer/cn/MSPM0G3507/datasheet)

