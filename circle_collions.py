import math

from hypothesis import given
from hypothesis import composite


class Circle():
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


class Quad():
    def __init__(self, circle):
        self.point = circle


def collide(node):
    nr = node.radius + 16
    nx1 = node.x - nr
    nx2 = node.x + nr
    ny1 = node.y - nr
    ny2 = node.y + nr

    def fixer(quad, x1, y1, x2, y2):
        if quad.point and (quad.point != node):
            x = node.x - quad.point.x
            y = node.y - quad.point.y
            l = math.sqrt(x * x + y * y)
            r = node.radius + quad.point.radius
            if (l < r):
                l = (l - r) / l * 0.5
                x = x * l
                y = y * l
                node.x = node.x - x
                node.y = node.y - y
                quad.point.x = quad.point.x + x
                quad.point.y = quad.point.y + y
        return x1 > nx2 or x2 < nx1 or y1 > ny2 or y2 < ny1
    return fixer


def is_collision(circle1, circle2):
    dx = circle1.x - circle2.x
    dy = circle1.y - circle2.y
    distance = math.sqrt(dx * dx + dy * dy)

    return distance < circle1.radius + circle2.radius


@composite
def circle():
    pass


@given(text())
def test_decode_inverts_encode(circle1, circle2):
    assert is_collision(circle1, circle2)
