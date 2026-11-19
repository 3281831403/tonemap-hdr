"""HDR 色调映射：曝光、ACES 与 LUT：待实现的核心模块。"""

import math


def ev_exposure(ev):
    """EV 转曝光倍数。"""
    return 2.0 ** ev

def aces(x):
    """ACES 拟合曲线。"""
    # Narkowicz 的 ACES 拟合曲线：f(x) = (x(2.51x + 0.03)) / (x(2.43x + 0.59) + 0.14)
    return (x * (2.51 * x + 0.03)) / (x * (2.43 * x + 0.59) + 0.14)

def bloom_threshold(value, threshold):
    """泛光只保留阈值以上部分。"""
    # 阈值在线性空间比较，只保留超出的能量。
    return max(0.0, value - threshold)

def linear_to_srgb(value):
    """线性值转 sRGB。"""
    # sRGB 传输函数的两段：线性段与 1/2.4 幂次段。
    if value <= 0.0031308:
        return 12.92 * value
    return 1.055 * (value ** (1.0 / 2.4)) - 0.055

def dither(value, noise):
    """输出加抖动噪声。"""
    return value + noise

def lut_sample(values, t):
    """LUT 按 t 做线性插值。"""
    if not values:
        return 0.0
    if len(values) == 1:
        return values[0]
    # 把归一化坐标 t 映射到表下标区间 [0, len-1]。
    pos = min(max(t, 0.0), 1.0) * (len(values) - 1)
    lower = int(math.floor(pos))
    upper = min(lower + 1, len(values) - 1)
    frac = pos - lower
    return values[lower] * (1.0 - frac) + values[upper] * frac

def vignette(distance, radius, softness):
    """暗角在半径内软边衰减。"""
    # 在 [radius*(1-softness), radius] 区间用 smoothstep 从 1 平滑衰减到 0。
    inner = radius * (1.0 - softness)
    span = radius - inner
    if span <= 0.0:
        return 1.0 if distance <= radius else 0.0
    t = (distance - inner) / span
    t = min(max(t, 0.0), 1.0)
    smooth = t * t * (3.0 - 2.0 * t)
    return 1.0 - smooth

def auto_exposure(average_luminance, key):
    """自动曝光按平均亮度计算。"""
    # 以平均亮度为基准，让中灰键值落到目标亮度。
    if average_luminance <= 0.0:
        return key
    return key / average_luminance

def highlight_rolloff(value, knee):
    """高光在拐点后平滑滚降。"""
    # 拐点处值与斜率都连续，之后平滑趋近 1。
    if value <= knee:
        return value
    span = 1.0 - knee
    if span <= 0.0:
        return value
    return knee + span * math.tanh((value - knee) / span)

def commit_frames(results):
    """批量帧全部成功才提交。"""
    # 任意一帧失败则整批不提交。
    return all(results)
