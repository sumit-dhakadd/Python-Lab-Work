
from abc import ABC, abstractmethod
import math

class AbstractShape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    def __add__(self, shape):
        return self.calculate_area() + shape.calculate_area()

    def __sub__(self, shape):
        return self.calculate_area() - shape.calculate_area()

    def __mul__(self, value):
        return self.calculate_area() * value


class Circle(AbstractShape):

    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return math.pi * self.r * self.r


class Rectangle(AbstractShape):

    def __init__(self, l, b):
        self.l = l
        self.b = b

    def calculate_area(self):
        return self.l * self.b


class Triangle(AbstractShape):

    def __init__(self, b, h):
        self.b = b
        self.h = h

    def calculate_area(self):
        return (self.b * self.h) / 2


c = Circle(5)
r = Rectangle(10, 5)
t = Triangle(8, 6)

print("Area of Circle:", round(c.calculate_area(), 2))
print("Area of Rectangle:", r.calculate_area())
print("Area of Triangle:", t.calculate_area())

print("\n--- Shape Mathematical Operations ---")
print("Sum of Circle and Rectangle:", round(c + r, 2))
print("Difference of Rectangle and Triangle:", r - t)
print("Circle Area multiplied by 2:", round(c * 2, 2))
