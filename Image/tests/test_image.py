import pytest

from image import RGBA_DTYPE, Image


def test_image_construct():
    width = 40
    height = 20
    img = Image(width, height)
    assert img
    assert img.width == width
    assert img.height == height
    assert img.pixels.shape == (height, width)
    assert img.pixels[0, 0].dtype == RGBA_DTYPE
    assert img.pixels.shape == (height, width)


fail_cases = [(0, 0, ValueError), (1.0, 0, TypeError), ("h", 0, TypeError), (10, 0, ValueError), (0, 10, ValueError)]


@pytest.mark.parametrize("w,h,ex", fail_cases)
def test_fail_image_construct(w, h, ex):
    with pytest.raises(ex):
        _ = Image(w, h)


def test_save_image():
    img = Image(400, 200, (255, 0, 0, 255))
    img.save("test.png")


def test_subscript():
    img = Image(10, 20, (0, 0, 0, 255))
    assert img[0, 0] == (0, 0, 0, 255)
    with pytest.raises(IndexError):
        img[-1, 0]
    with pytest.raises(IndexError):
        img[1, 22]

    img[0, 0] = (255, 0, 0, 255)
    assert img[0, 0] == (255, 0, 0, 255)

    img.set_pixel(1, 1, (128, 128, 128, 128))
    assert img.get_pixel(1, 1) == (128, 128, 128, 128)


def test_visual_correct():
    img = Image(3, 1, (255, 255, 255, 255))
    img.save("white.png")

    img.set_pixel(0, 0, (255, 0, 0, 255))
    img.set_pixel(1, 0, (0, 255, 0, 255))
    img.set_pixel(2, 0, (0, 0, 255, 255))
    img.save("rgb.png")
