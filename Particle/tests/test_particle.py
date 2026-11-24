import pytest

from Particle import Particle
from Vec3 import Vec3


def test_particle_contruct():
    p = Particle()
    assert p
    assert p.position == Vec3()
    assert p.direction == Vec3()
    assert p.colour == Vec3()
    assert p.max_life == 1000
    assert p.life == 0
    assert p.scale == pytest.approx(1.0)


def test_setters():
    pos = Vec3(1, 2, 3)
    dir = Vec3(3, 4, 5)
    colour = Vec3(1, 1, 1)
    max_life = 22
    life = 10
    scale = 0.4
    p = Particle(pos, dir, colour, max_life, life, scale)
    assert p.position == pos
    assert p.direction == dir
    assert p.colour == colour
    assert p.max_life == max_life
    assert p.life == life
    assert p.scale == scale
