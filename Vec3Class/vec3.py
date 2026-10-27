import math


class Vec3:
    """A vec3 class for float data"""

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        """build Vec3 from 3 floats defaults to 0,0,0
        Args :
            x : float  the x values will be converted to float
            y : float  the y values will be converted to float
            z : float  the z values will be converted to float
        """
        self._x = float(x)
        self._y = float(y)
        self._z = float(z)

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, v: float):
        self._x = float(v)

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, v):
        self._y = float(v)

    @property
    def z(self) -> float:
        return self._z

    @z.setter
    def z(self, v):
        self._z = float(v)

    def __eq__(self, rhs: object) -> bool:
        if not isinstance(rhs, Vec3):
           return  NotImplemented
        return math.isclose(self.x, rhs.x) and math.isclose(self.y, rhs.y) and math.isclose(self.z, rhs.z)
