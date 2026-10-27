import pytest

from vec3 import Vec3


def test_construction():
    v = Vec3()
    assert v.x == 0.0
    assert v.y == 0.0
    assert v.z == 0.0


user_values = [(0.0, 0.0, 0.0), (-1.0, 0.0, 2.0), (99, 200, 300)]


@pytest.mark.parametrize("x,y,z", user_values)
def test_user_values(x, y, z):
    v = Vec3(x, y, z)
    assert v.x == x
    assert v.y == y
    assert v.z == z


def test_check_parameters():
    v = Vec3()
    v.x = 0.002
    v.y = 1000.23
    v.z = -0.005

    assert v.x == pytest.approx(0.002)
    assert v.y == pytest.approx(1000.23)
    assert v.z == pytest.approx(-0.005)


bad_values = [(0.0, "b", 0.0), ("a", 0.0, 1.0), ("a", "a", "a")]


@pytest.mark.parametrize("x,y,z", bad_values)
def test_check_bad_parameters(x, y, z):
    with pytest.raises(ValueError):
        _ = Vec3(x, y, z)


def test_vec3_eq():
    a = Vec3(0.1, 0.2, 0.3)
    b = Vec3(0.1, 0.2, 0.3)
    c = Vec3(0.2, 0.3, 0.5)
    assert a == b
    assert a != c
    assert a.__eq__(1) is NotImplemented
