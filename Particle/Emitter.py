import random

from Particle import Particle
from Random import Random
from Vec3 import Vec3


class Emitter:
    def __init__(self, pos: Vec3, num_particles: int):
        self._position = pos
        self._num_particles = num_particles
        self._particles = []
        self._init_particles()

    def _init_particles(self):
        for _ in range(self._num_particles):
            particle = self._create_particle()
            self._particles.append(particle)

    def _create_particle(self):
        EMIT_DIR = Vec3(0, 1, 0)
        SPREAD = 15

        direction = EMIT_DIR * Random.random_positive_float() + Random.random_vector_on_sphere() * SPREAD
        direction.y = abs(direction.y)
        max_life = random.randint(10, 50)
        colour = Random.random_positive_vec3()
        pos = Vec3(self._position.x, self.position.y, self.position.z)
        return Particle(pos, direction, colour, max_life, 0, 1.0)

    @property
    def particles(self):
        return self._particles

    @property
    def position(self):
        return self._position

    @property
    def num_particles(self):
        return self._num_particles

    def render(self):
        for p in self.particles:
            print(p)
