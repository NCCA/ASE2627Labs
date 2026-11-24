from dataclasses import dataclass, field

from Vec3 import Vec3


@dataclass
class Particle:
    position: Vec3 = field(default_factory=Vec3)
    direction: Vec3 = field(default_factory=Vec3)
    colour: Vec3 = field(default_factory=Vec3)
    max_life: int = 1000
    life: int = 0
    scale: float = 1.0

    def __str__(self) -> str:
        return f"{self.position} {self.colour} {self.direction} {self.max_life} {self.life} {self.scale}"
