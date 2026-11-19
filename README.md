# HDR 色调映射：曝光、ACES 与 LUT

HDR 画面亮部一片死白、暗部发灰：曝光没有按 EV 换算，ACES 曲线系数错，泛光阈值按线性算，线性转 sRGB 少了一段，抖动噪声没加，LUT 采样只取最近点，暗角没有软边，自动曝光不按平均亮度，高光滚降在拐点处断裂，批量帧只提交一半。

## 目录结构

```
README.md
conftest.py
.gitignore
render/__init__.py
render/tonemap.py
tests/test_tonemap.py
```

## 当前状态

`render/tonemap.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_tonemap.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 曝光按 EV 换算
2. ACES 拟合曲线
3. 泛光阈值在线性空间
4. 线性转 sRGB 分段
5. 输出加抖动噪声
6. LUT 双线性插值
7. 暗角软边衰减
8. 自动曝光按平均亮度
9. 高光滚降在拐点连续
10. 批量帧统一提交

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `render/tonemap.py`
后 15 条用例应全部通过。
