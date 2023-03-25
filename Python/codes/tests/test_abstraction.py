from ..src.abstraction import Polygon, Triangle, Rectangle


def test_triangle():
    triangle = Triangle()

    assert triangle.get_angles() == 3
    assert isinstance(triangle, Polygon)


def test_rectangle():
    rectangle = Rectangle()

    assert rectangle.get_angles() == 4
    assert isinstance(rectangle, Polygon)