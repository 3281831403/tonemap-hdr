"""HDR 色调映射：曝光、ACES 与 LUT：待实现的核心模块。"""


def ev_exposure(ev):
    """EV 转曝光倍数。"""
    raise NotImplementedError

def aces(x):
    """ACES 拟合曲线。"""
    raise NotImplementedError

def bloom_threshold(value, threshold):
    """泛光只保留阈值以上部分。"""
    raise NotImplementedError

def linear_to_srgb(value):
    """线性值转 sRGB。"""
    raise NotImplementedError

def dither(value, noise):
    """输出加抖动噪声。"""
    raise NotImplementedError

def lut_sample(values, t):
    """LUT 按 t 做线性插值。"""
    raise NotImplementedError

def vignette(distance, radius, softness):
    """暗角在半径内软边衰减。"""
    raise NotImplementedError

def auto_exposure(average_luminance, key):
    """自动曝光按平均亮度计算。"""
    raise NotImplementedError

def highlight_rolloff(value, knee):
    """高光在拐点后平滑滚降。"""
    raise NotImplementedError

def commit_frames(results):
    """批量帧全部成功才提交。"""
    raise NotImplementedError
