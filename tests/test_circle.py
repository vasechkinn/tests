import pytest
from circle import Circle

@pytest.mark.parametrize(
    'r, exp_area, exp_len, exp_d',
    [
        [1, 3.14, 6.28, 2],
        [2, 12.56, 12.56, 4],
        [2.1, 13.8474, 13.188, 4.2],
        [10, 314.0, 62.800000000000004, 20],
        [100.1, 31462.831399999995, 628.628, 200.2],
        [0.1, 0.031400000000000004, 0.6280000000000001, 0.2]
    ]
)
def test_positive(r, exp_area, exp_len, exp_d):
    circle = Circle(r)
    assert exp_area == circle.area(), f"sep: {exp_area}, res: {circle.area()}"
    assert exp_len == circle.circumference(), f"exp: {exp_len}, res: {circle.circumference()}"
    assert exp_d == circle.diameter(), f"exp: {exp_d}, res: {circle.diameter()}"

@pytest.mark.parametrize(
    'r, exp',
    [
        [0, ValueError],
        [-1, ValueError],
        ['111', TypeError]
    ]
)
def test_negative(r,exp):
    with pytest.raises(exp):
        Circle(r)