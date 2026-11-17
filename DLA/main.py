#!/usr/bin/env -S uv run --script
import argparse
import random
from pathlib import Path

from image import Image


class DLA:
    def __init__(self, width: int, height: int) -> None:
        self._image = Image(width, height, (255, 255, 255, 255))

    @property
    def width(self) -> int:
        return self._image.width

    @property
    def height(self) -> int:
        return self._image.height

    def save(self, file_name: str) -> None:
        self._image.save(file_name)

    def set_seed(self, x: int, y: int) -> None:
        try:
            self._image.set_pixel(x, y, (255, 0, 0, 0))
        except IndexError:
            print(f"{x} or {y} out of range of image {self._image.shape}")

    def random_seed(self, ammount: int) -> None:
        """fill sim with ammount random seeds, for now alpha is 0 for seed and has colour red"""
        for _ in range(ammount):
            x, y = self._random_start()
            self._image.set_pixel(x, y, (255, 0, 0, 0))

    def _random_start(self) -> tuple[int, int]:
        x = random.randint(1, self.width - 1)
        y = random.randint(1, self.height - 1)
        return x, y

    def walk(self) -> bool:
        x, y = self._random_start()
        walking = True
        offsets = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1)]
        while walking:
            if x <= 1 or x >= self.width - 1 or y <= 1 or y >= self.height - 1:
                walking = False
                print("hit wall exiting")
                return False
            else:
                for x_offset, y_offset in offsets:
                    colour = self._image.get_pixel(x + x_offset, y + y_offset)
                    if colour[3] == 0:
                        self._image.set_pixel(x, y, (255, 0, 0, 0))
                        print("found seed")
                        walking = False
                        return True
            x += random.choice([-1, 0, 1])
            y += random.choice([-1, 0, 1])


def run_sim(width: int, height: int, sim_steps: int, filename: str):
    print("running sim")
    Path("/transfer/DLA").mkdir(parents=True, exist_ok=True)
    sim = DLA(width, height)
    # sim.random_seed(5)
    for x in range(sim.width):
        sim.set_seed(x, sim.height // 2)

    frame = 0
    found = 0
    for _ in range(sim_steps):
        if sim.walk():
            found+=1
            if found % 10 == 0 :
                sim.save(f"/transfer/DLA/{filename}.{frame:04d}.png")
                frame += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple DLA simulation")
    parser.add_argument("-iw", "--width", type=int, default=200, help="image width")
    parser.add_argument("-ih", "--height", type=int, default=200, help="image height")
    parser.add_argument("-s", "--sim_steps", type=int, default=100, help="simulation steps")
    parser.add_argument("-f", "--filename", type=str, default="sim", help="the base file name for the sim")
    args = parser.parse_args()
    run_sim(args.width, args.height, args.sim_steps, args.filename)
