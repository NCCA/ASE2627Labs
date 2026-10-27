import pytest

from image import RGB_DTYPE, Image


def test_image_construct():
    width = 40
    height = 20
    img = Image(width, height)
    assert img
    assert img.width == width
    assert img.height == height
    assert img.pixels.shape == (height, width)
    assert img.pixels[0, 0].dtype == RGB_DTYPE


fail_cases = [(0, 0, ValueError), (1.0, 0, TypeError), ("h", 0, TypeError), (10, 0, ValueError), (0, 10, ValueError)]


@pytest.mark.parametrize("w,h,ex", fail_cases)
def test_fail_image_construct(w, h, ex):
    with pytest.raises(ex):
        _ = Image(w, h)


def test_save_image():
    img = Image(400, 200, (255, 0, 0))
    img.save("test.png")
