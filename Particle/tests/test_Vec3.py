import pytest

from Vec3 import Vec3


def test_vec3_construct():
    v = Vec3()
    assert v.x == 0.0
    assert v.y == 0.0
    assert v.z == 0.0
    with pytest.raises(TypeError):
        _ = Vec3("err", 1, 0)

    v = Vec3(0.5, 2.0, -3.5)
    assert v.x == pytest.approx(0.5)
    assert v.y == pytest.approx(2.0)
    assert v.z == pytest.approx(-3.5)


def test_eq():
    a = Vec3(0, 0, 0)
    b = Vec3()
    assert a == b
