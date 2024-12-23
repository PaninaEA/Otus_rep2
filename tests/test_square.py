import pytest

from src.Square import Square


@pytest.mark.parametrize(
    ("side_a", "area"),
    [pytest.param(4, 16, id="integer"), pytest.param(6.5, 42.25, id="float")],
)
def test_square_area(side_a, area):
    r = Square(side_a)
    assert r.get_area == area, f"Square area must be {side_a} * {side_a} = {area}"


@pytest.mark.parametrize(
    ("side_a", "perimeter"),
    [pytest.param(3, 12, id="integer"), pytest.param(3.5, 14, id="float")],
)
def test_square_perimeter(side_a, perimeter):
    r = Square(side_a)
    assert (
        r.get_perimeter == perimeter
    ), f"square perimeter must be ({side_a} * 4 = {perimeter}"


@pytest.mark.parametrize(
    ("side_a", "add_area"),
    [pytest.param(6, 48, id="integer"), pytest.param(6.5, 54.25, id="float")],
)
def test_square_add_area(side_a, add_area, create_rectangle):
    r = Square(side_a)
    assert (
        r.add_area(other_figure=create_rectangle) == add_area
    ), f"sum area square and area rectangle must be {side_a}*{side_a} + 12 = {add_area}"


@pytest.mark.parametrize(
    "side_a",
    [pytest.param(0, id="side_a = 0"), pytest.param(-1, id="side_a = negative")],
)
def test_square_negative(side_a):
    with pytest.raises(ValueError):
        Square(side_a)
