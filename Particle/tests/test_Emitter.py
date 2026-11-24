import pytest

from Emitter import Emitter
from Vec3 import Vec3


def test_emitter():

    num_particles = 100
    e = Emitter(Vec3(0, 0, 0), num_particles)
    assert e
    assert e.position == Vec3()
    assert e.num_particles == num_particles
    assert len(e.particles) == num_particles
