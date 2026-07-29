# RoboMaster C 板接口、供电与下载速查

> 汇总 C 板最常查、最容易接错的供电域、下载方式和接口到 STM32 IO 的映射。

## 适用范围

- 对象：RoboMaster 开发板 C 型
- 主控：`STM32F407IGH6TR`
- 原理图：V1.0，2019-12-05
- 用户手册：v1.0，2020-01

## 供电与下载

- 直流输入范围为 8–28 V；原理图包含防反接、缓启动和输入过压关断电路。
- `VCC_5V_M` 给 7 路 PWM 接口供电，5 V 合计最大 5 A。
- `VCC_5V` 给板载器件和后级 3.3 V 电源供电，5 V 最大 1 A。
- USB 供电只进入 `VCC_5V`，不进入 `VCC_5V_M`；USB 供电时 PWM 接口没有
  舵机电源。
- SWD 接口依次提供 SWDIO、SWCLK、GND、3.3 V。
- 默认 BOOT0=0、BOOT1=0，从用户 Flash 启动。进入系统存储器 DFU 时设置
  BOOT0=1、BOOT1=0，然后通过 USB 连接并复位。

## 常用接口与 IO

| 板级功能 | STM32 信号 / IO | 板级注意事项 |
| --- | --- | --- |
| RGB LED | PH10 / PH11 / PH12 | 蓝 / 绿 / 红；控制端高电平点亮 |
| 用户键 | PA0 | 按下为低电平 |
| 可配置 I2C | PF1 / PF0 | I2C2_SCL / I2C2_SDA |
| 可配置 SPI | PB12–PB15 | SPI2_CS / SCK / MISO / MOSI |
| UART 4-pin | PA9 / PB7 | STM32 UART1_TX / UART1_RX |
| UART 3-pin | PG14 / PG9 | STM32 UART6_TX / UART6_RX |
| CAN1 | PD1 / PD0 | CAN1_TX / CAN1_RX；2-pin 接口 |
| CAN2 | PB6 / PB5 | CAN2_TX / CAN2_RX；4-pin 接口带 5 V、GND |
| PWM 1–4 | PE9 / PE11 / PE13 / PE14 | TIM1_CH1–CH4 |
| PWM 5–7 | PC6 / PI6 / PI7 | TIM8_CH1–CH3 |
| DBUS | PC11 | 经反相电路接 UART3_RX，通常配置 100 kbit/s |
| 蜂鸣器 | PD14 | TIM4_CH3，无源蜂鸣器额定频率 4 kHz |
| 电池电压检测 | PF10 | `VCC_BAT` 经 200 kΩ / 22 kΩ 分压接 ADC |
| BMI088 | SPI1；PA4、PB0、PC4、PC5 | 加速度计/陀螺仪独立片选与中断 |
| IMU 加热 | PF6 | TIM10_CH1 控制，原理图标注加热功率约 0.58 W |
| IST8310 | I2C3；PG6、PG3 | 默认 I2C 地址 0x0E |
| DCMI 摄像头 | PB8/PB9、PA6、PH8/PH9 等 | 18-pin FPC，8 位数据总线 |

## 易错点

- 外壳丝印 `UART1` 对应 STM32 的 UART6，外壳丝印 `UART2` 对应 STM32 的
  UART1；接线和代码应以 MCU 外设编号为准。
- UART6 与裁判系统电源模块的接口线序相同，直连时 TX/RX 需要交叉。
- 可配置 I2C/SPI 接口默认电源由 R209/R210 的焊接状态决定。切换到 5 V 设备
  需要改焊，修改前先核对实板电阻状态。
- CAN1 线序为 CANL、CANH；CAN2 线序为 5 V、GND、CANH、CANL。
- 电池检测的理想分压系数为 `22 / (200 + 22) ≈ 0.0991`。这是按原理图阻值
  推导的标称值，换算实际电压时还需考虑 ADC 参考电压和电阻误差。

## 来源

- 文件：`../originals/robomaster-development-board-type-c-schematic-v1.0.pdf`
- 文档版本：V1.0
- 章节/页码：PDF 第 1–7 页，原理图 Sheet 2–8
- 辅助核验：`../originals/robomaster-development-board-type-c-user-manual-v1.0-zh-cn-unlocked.pdf`，
  v1.0，PDF 第 5–20 页
- 官方产品页：<https://www.robomaster.com/zh-CN/products/components/general/development-board-type-c>
- 提取日期：2026-07-29
- 提取方式：文本层提取后人工核对
