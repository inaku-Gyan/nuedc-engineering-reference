# DJI RoboMaster GM6020

> 内置 FOC 驱动器和 13 位位置传感器的 24 V 直流无刷云台电机，支持 CAN 与
> PWM 控制，适合机器人云台和低速大扭矩直接驱动。

## 快速定位

- 型号：GM6020
- 厂商：DJI RoboMaster
- 额定电压：DC 24 V
- 文档版本：v1.4，2023.10
- 资料包 ID：`hw-motor-control-dji-gm6020`

## 关键参数

| 参数 | 数值 |
| --- | ---: |
| 最大空载转速 | 320 rpm |
| 额定扭矩（最大连续扭矩） | 1.2 N·m |
| 额定扭矩下最高转速 | 132 rpm |
| 额定电流 | 1.62 A |
| 转矩常数 | 741 mN·m/A |
| 转速常数 | 13.33 rpm/V |
| 定位精度 | 0.05° |
| 工作环境温度 | 0–55 ℃ |
| 绕组最高允许温度 | 125 ℃ |
| 重量 | 约 468 g |

结构参数：空心轴内径 18 mm，电机外径 66.7 mm，总高度 45 mm。转子端使用
3×M3、深 4 mm 的安装孔，定子端使用 3×M4、深 6 mm 的安装孔。

## 资料入口

| 需求 | 推荐入口 | 来源定位 |
| --- | --- | --- |
| CAN、PWM 和拨码速查 | [控制协议摘录](extracts/can-and-pwm-control.md) | 手册第 5–9 页 |
| 接口线序与机械尺寸 | [v1.4 使用说明](originals/robomaster-gm6020-user-manual-v1.4-zh-cn.pdf) | PDF 第 3–5 页 |
| 指示灯与异常状态 | [v1.4 使用说明](originals/robomaster-gm6020-user-manual-v1.4-zh-cn.pdf) | PDF 第 6 页 |
| 负载曲线与工作范围 | [v1.4 使用说明](originals/robomaster-gm6020-user-manual-v1.4-zh-cn.pdf) | PDF 第 10–11 页 |
| 电气与结构参数 | [v1.4 使用说明](originals/robomaster-gm6020-user-manual-v1.4-zh-cn.pdf) | PDF 第 12 页 |

## 覆盖范围

已覆盖：

- 额定电气、机械和环境参数；
- CAN 控制帧、反馈帧、拨码 ID 与终端电阻；
- PWM 速度/位置控制和行程校准；
- 接口线序、指示灯和保护状态。

尚未整理：

- RoboMaster Assistant 的软件包与完整配置项；
- 固件版本差异；
- 负载曲线的数字化数据；
- 实际散热条件下的连续工作能力。

## 使用注意

- CAN 总线比特率固定为 1 Mbit/s，使用标准数据帧。
- ID 由前三位拨码开关设置，`000` 无效；第四位控制 CAN 终端电阻。
- CAN 与 PWM 同时输入时优先使用 CAN。
- 从输出轴端观察，逆时针为正方向。
- 电机应远离强磁场和铁磁材料，避免角度传感器受干扰。
- 额定参数和负载曲线基于 24 V、25 ℃及正常散热条件。

## 官方入口

- [GM6020 官方产品页](https://www.robomaster.com/zh-CN/products/components/general/gm6020/info)
- [RoboMaster Assistant](https://www.robomaster.com/zh-CN/products/components/assistant)
