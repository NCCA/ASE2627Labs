import operator
from collections.abc import Sequence
from pathlib import Path

import numpy as np
from PIL import Image as PILImage

# type hint for a colour like objet
ColourLike = Sequence[int] | np.ndarray

RGB_DTYPE = np.dtype([("r", np.uint8), ("g", np.uint8), ("b", np.uint8)])

# Colours could be (r,g,b) [r,g,b], np.array(r,g,b)
WHITE = (255, 255, 255)


class Image:
    def __init__(self, width: int, height: int, bg_colour: ColourLike = WHITE):

        width = operator.index(width)
        height = operator.index(height)
        if width <= 0 or height <= 0:
            raise ValueError(f"width and height must be positive got {width} {height}")

        self._pixels = np.empty((height, width), dtype=RGB_DTYPE)
        self.clear(bg_colour)

    def clear(self, colour: ColourLike = WHITE) -> None:
        self._pixels[:] = np.array((colour[0], colour[1], colour[2]), dtype=RGB_DTYPE)

    @property
    def width(self) -> int:
        return self._pixels.shape[1]

    @property
    def height(self) -> int:
        return self._pixels.shape[0]

    @property
    def pixels(self) -> np.recarray:
        # this allows attribute access via .r
        view = self._pixels.view(np.recarray)
        view.flags.writeable = False
        return view

    def save(self, file_name: str | Path):
        data = self._pixels.view(np.uint8).reshape(self.width, self.height, 3)
        PILImage.fromarray(data).save(file_name)
