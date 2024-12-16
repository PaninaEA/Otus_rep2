from src.Figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Circle radius can't be less than 0")
        self.radius = radius

    @property
    def get_area(self):
        return self.radius**2 * math.pi

    @property
    def get_perimeter(self):
        return self.radius * 2 * math.pi
