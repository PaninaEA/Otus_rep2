import pytest

from src.Rectangle import Rectangle
from src.Square import Square


@pytest.fixture()
def create_square():
    s = Square(8)
    return s


@pytest.fixture()
def create_rectangle():
    s = Rectangle(4, 3)
    return s
