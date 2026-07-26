# PCA9685 寄存器与安全初始化

> 适用于 PCA9685 Rev.4。写 PRE_SCALE 前必须休眠，唤醒后等待至少 500 μs；
> 有条件时用低有效 OE 做硬件默认关闭和总线故障关断。

## 地址与关键寄存器

PCA9685 单颗地址格式为 `1 A5 A4 A3 A2 A1 A0`。常见全部地址脚接地得到七位地址
`0x40`。Rev.4 第 7.1 节同时指出：

- `0x70` 是上电启用的默认 LED All Call 地址，不能作为单颗地址；
- `0x78`–`0x7F` 属于保留/特殊地址范围，不能分配；
- 实际地址必须按模块 A0–A5 焊桥或扫描结果确认。

| 地址 | 寄存器 | 用途 |
| ---: | --- | --- |
| `0x00` | MODE1 | RESTART、EXTCLK、AI、SLEEP、ALLCALL |
| `0x01` | MODE2 | 输出驱动、极性、OE 高时输出状态 |
| `0x06 + 4n` | LEDn_ON_L | 通道 n 的 ON 计数低 8 位 |
| `0x07 + 4n` | LEDn_ON_H | ON 高 4 位和 Full-On |
| `0x08 + 4n` | LEDn_OFF_L | OFF 计数低 8 位 |
| `0x09 + 4n` | LEDn_OFF_H | OFF 高 4 位和 Full-Off |
| `0xFA`–`0xFD` | ALL_LED_* | 全通道 ON/OFF |
| `0xFE` | PRE_SCALE | PWM 频率预分频 |

MODE1.AI 置 1 后，控制寄存器地址自动递增，适合一次连续写四个舵机通道。

## 频率和脉宽换算

Rev.4 第 7.3.5 节给出的关系可写为：

```text
prescale = round(oscillator_hz / (4096 × pwm_hz)) - 1
actual_pwm_hz = oscillator_hz / (4096 × (prescale + 1))
pulse_count = round(pulse_us × actual_pwm_hz × 4096 / 1,000,000)
```

标称 25 MHz、目标 50 Hz 时，PRE_SCALE 计算为 121（`0x79`），实际约
50.03 Hz。内部 25 MHz 是典型值，不是精密时基；舵机端点需要结合实测周期标定。

Rev.4 规定 PRE_SCALE 范围 `0x03`–`0xFF`，对应典型 1526–24 Hz。Rev.3 旧手册
写的是 40–1000 Hz，不能用旧范围否定 Rev.4 的 50 Hz 配置。

## 安全初始化顺序

建议在上层保持输出关闭时执行：

1. 若 OE 已接 MCU，上电即驱动为高；
2. 读 MODE1，写回 `SLEEP=1`；
3. 写 PRE_SCALE；
4. 配置 MODE1.AI 和所需 MODE2 输出行为，清除 SLEEP；
5. 等待至少 500 μs，让振荡器稳定；
6. 把 ALL_LED_OFF_H 的 Full-Off 位置 1，或逐通道写入安全值；
7. 所有配置和首帧目标成功后，才把 OE 拉低。

Rev.4 第 7.3.1 说明，清除 SLEEP 后振荡器最多需要 500 μs；第 7.3.5 说明
PRE_SCALE 只能在 SLEEP=1 时写。OE 高时的输出状态由 MODE2.OUTNE 决定，若要求
真正高阻，还必须配置对应位并核对成品模块外围电路。

总线超时、NACK 或批量写中途失败时，应立即拉高 OE 并锁存软件故障。没有 OE 的
模块只能退化为寄存器 All-Off；若 I²C 本身已经失败，这条路径不具备同等保障。

## 来源

- [NXP PCA9685 Rev.4 官方 PDF](https://www.nxp.com/docs/en/data-sheet/PCA9685.pdf)，
  第 7.1、7.3.1、7.3.3、7.3.5、7.4 节，最后核验 2026-07-27。
- [本地 PCA9685 Rev.3](../originals/pca9685-datasheet-rev3.pdf)，用于版本差异核对。
