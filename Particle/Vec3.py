import math


def _validate_input(value):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{value=} but must be a number")
    return value


class Vec3:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        self._x = _validate_input(x)
        self._y = _validate_input(y)
        self._z = _validate_input(z)

    @property
    def x(self):
        return self._x

    def __str__(self) -> str:
        return f"Vec3({self.x},{self.y},{self.z})"

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = _validate_input(value)

    @property
    def z(self):
        return self._z

    def __eq__(self, rhs):
        if not isinstance(rhs, Vec3):
            return NotImplemented
        return math.isclose(self._x, rhs._x) and math.isclose(self._y, rhs._y) and math.isclose(self._z, rhs.z)

    def __add__(self, rhs):
        if isinstance(rhs, Vec3):
            return Vec3(self._x + rhs._x, self._y + rhs._y, self._z + rhs._z)
        else:
            raise TypeError(f"Unsuported type for Vec3 + {type(rhs).__name__}")

    def __mul__(self, rhs):
        if isinstance(rhs, Vec3):
            return Vec3(self._x * rhs._x, self._y * rhs._y, self._z * rhs._z)
        elif isinstance(rhs, (int, float)):
            return Vec3(self._x * rhs, self._y * rhs, self._z * rhs)
        else:
            raise TypeError(f"Unsupported type for Vec3 * {type(rhs).__name__}")
