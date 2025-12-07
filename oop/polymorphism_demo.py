import math

class Shape:
    def area(self):
        raise NotImplementedError("Not implemented error!")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        rect = self.length * self.width
        return rect


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circ = self.radius**2 * math.pi
        return circ

# ["** 2"]