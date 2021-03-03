import math
from fractions import Fraction


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def kart_to_polar(coord):
    radians = math.atan(Fraction(coord.y, coord.x))
    radius = (coord.x ** 2 + coord.y ** 2) ** 0.5
    return radians, radius


def polar_to_kart(radians, radius):
    x = round(math.cos(radians) * radius)
    y = round(math.sin(radians) * radius)
    return Coord(x, y)


def main():
    my_coord = Coord(4, 3)
    radians, radius = kart_to_polar(my_coord)
    new_coord = polar_to_kart(radians, radius)
    print(new_coord.x, new_coord.y)


if __name__ == '__main__':
    main()
