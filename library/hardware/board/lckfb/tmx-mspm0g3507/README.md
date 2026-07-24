# 立创·天猛星 MSPM0G3507 开发板

> 采用 64 引脚 MSPM0G3507 的立创开发板，面向电赛和 MSPM0 学习。资料包包含
> 图片型板卡规格书与三页原理图，适合查板载资源、接口、供电、下载调试和连接关系。

## 快速定位

- 型号：LCKFB-TMX-MSPM0G3507
- 商品编号：C42378531
- 资料编号：WJ1511101
- 主控：MSPM0G3507，64 引脚 LQFP
- 资料包 ID：`hw-board-lckfb-tmx-mspm0g3507`

## 板载资源概览

- USB Type-C 供电；
- 板载 5 V 转 3.3 V 电源、3.3 V 电源指示灯与用户 LED；
- CH340E USB 转串口，支持串口调试和 MSPM0 BSL 下载；
- SWD 下载/调试焊盘；
- 用户键、复位键、BSL 功能键；
- W25Q128 SPI Flash；
- 常见 SPI LCD/OLED 接口；
- PA0、PA1 上拉电源可选择；
- 板载 3.3 V 参考电压相关配置；
- 约 69.967 mm × 44.975 mm。

完整引脚复用图在规格书第 2 页，密集且为图片，不在本摘要中重复转录。

## 资料入口

| 需求 | 推荐入口 | 来源定位 |
| --- | --- | --- |
| 板载资源位置 | [板卡规格书](originals/tmx-mspm0g3507-board-specification.pdf) | 第 1 页 |
| 双排针引脚复用 | [板卡规格书](originals/tmx-mspm0g3507-board-specification.pdf) | 第 2 页 |
| 主控、时钟、按键和 LED | [原理图](originals/tmx-mspm0g3507-schematic-2024-11-14.pdf) | 第 1 页 `core` |
| USB、电源和参考电压 | [原理图](originals/tmx-mspm0g3507-schematic-2024-11-14.pdf) | 第 2 页 `power` |
| 串口、下载、Flash 和扩展口 | [原理图](originals/tmx-mspm0g3507-schematic-2024-11-14.pdf) | 第 3 页 `extension` |
| 易错硬件配置速查 | [硬件配置摘录](extracts/hardware-configuration.md) | 原理图第 1–3 页 |

## 覆盖范围

已覆盖：

- 板载资源和机械尺寸；
- 主控、电源、参考电压、调试下载与扩展接口的定位；
- 原理图中明确标出的关键硬件注意事项。

尚未整理：

- 所有排针信号的文本化对照表；
- 板卡 BOM、PCB 源文件和封装库；
- SDK 工程、示例代码和出厂测试程序；
- 各跳线/0 Ω 电阻在不同硬件批次上的实测状态。

## 使用注意

- 规格书是整页图片，搜索不到其中的引脚名；查复用关系时直接打开第 2 页。
- 原理图标题栏标注创建/更新日期为 2024-11-14；本地文件名中的
  `2026-07-24` 是导出日期，不代表硬件修订日期。
- 原理图没有清晰给出硬件版本号。涉及板卡批次差异时，应同时核对实物丝印。
- 主控的精确电气限制和引脚能力应回到
  [`TI MSPM0G3507` 资料包](../../../mcu/ti/mspm0g3507/README.md)核验。

## 官方入口

- [天猛星开发板介绍](https://wiki.lckfb.com/zh-hans/tmx-mspm0g3507/)
- [天猛星下载中心](https://wiki.lckfb.com/zh-hans/tmx-mspm0g3507/download-center.html)

