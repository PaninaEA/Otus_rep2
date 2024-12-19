from src.Figure import Figure


class Square(Figure):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Square sides can't be less than 0")
        self.side_a = side_a

    @property
    def get_area(self):
        return self.side_a * self.side_a

    @property
    def get_perimeter(self):
        return self.side_a * 4
