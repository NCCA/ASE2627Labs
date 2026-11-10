#!/usr/bin/env -S uv run --script


from image import Image

img = Image(640, 480, (255, 0, 0, 255))
img.save("test.png")
