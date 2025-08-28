from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0
    assert bound_to_180(180) == 180
    assert bound_to_180(200) == -160
    assert bound_to_180(-180) == -180
    assert bound_to_180(-200) == 160
    assert bound_to_180(369) == 9


""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)
    assert not(is_angle_between(0, -1, 2))
    assert not(is_angle_between(0, 3, 2))
    assert is_angle_between(0, 2, 2)
    assert is_angle_between(0, 0, 2)
