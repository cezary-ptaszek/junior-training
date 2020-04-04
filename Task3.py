from math import pi
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        return str(self.x) + " " + str(self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y


class Circle:
    """A class representing a circle"""

    def __init__(self, x=0, y=0, radius=1):
        if radius < 0:
            raise ValueError("negative radius")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self): pass  # "Circle(x, y, radius)"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return int(self.radius * self.radius * pi)

    def move(self, x, y):
        return self.pt.move(x, y)

    def distance(self, other):
        return math.sqrt(pow(other.pt.getX() - self.pt.getX(), 2) + pow(other.pt.getY() - self.pt.getY(), 2))

    def cover(self, other):
        if self.distance(other) + self.radius <= other.radius:
            return str(other.radius) + ' ' + str(other.pt.getX()) + ' ' + str(other.pt.getY())
        elif self.distance(other) + other.radius <= self.radius:
            return str(self.radius) + ' ' + str(self.pt.getX()) + ' ' + str(self.pt.getY())
        else:
            if self.radius <= other.radius:
                theta = 1/2 + (self.radius - other.radius) / (2 * self.distance(other))
                point = (1 - theta) * [self.pt.getX(), self.pt.getY()] + theta * [other.pt.getX(), other.pt.getY()]
                x, y = point.split()
                return str(self.radius+other.radius+self.distance(other)) + ' ' + x + ' ' + y


if __name__ == '__main__':
    radius1 = input()
    points1 = input()
    x1, y1 = points1.split()
    radius2 = input()
    points2 = input()
    x2, y2 = points1.split()
    shiftNumbers = input()
    s1, s2 = shiftNumbers.split()

    c1 = Circle(int(x1), int(y1), int(radius1))
    c2 = Circle(int(x2), int(y2), int(radius2))

    print(c1.area())
    print(c1.cover(c2))
    print(c1.move(int(s1), int(s2)))
