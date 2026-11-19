import pytest

from render import tonemap as mod

CASES = [
    ('ev_exposure', [0], 1.0, True),
    ('ev_exposure', [2], 4.0, True),
    ('aces', [0.5], 0.6163069544364508, True),
    ('bloom_threshold', [1.5, 1.0], 0.5, True),
    ('bloom_threshold', [0.5, 1.0], 0.0, True),
    ('linear_to_srgb', [0.5], 0.7353569830524495, True),
    ('linear_to_srgb', [0.001], 0.012920000000000001, True),
    ('dither', [0.5, 0.01], 0.51, True),
    ('lut_sample', [[0.0, 1.0], 0.25], 0.25, True),
    ('lut_sample', [[0.0, 1.0], 1.0], 1.0, True),
    ('vignette', [0.5, 1.0, 0.5], 1.0, True),
    ('vignette', [1.5, 1.0, 0.5], 0.0, True),
    ('auto_exposure', [0.5, 0.18], 0.36, True),
    ('highlight_rolloff', [0.5, 0.8], 0.5, True),
    ('commit_frames', [[True, False]], False, False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_tonemap_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
