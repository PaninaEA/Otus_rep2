import pytest

from src.Rectangle import Rectangle


@pytest.mark.parametrize(
    ("side_a", "side_b", "area"),
    [pytest.param(2, 4, 8, id="integer"), pytest.param(2.5, 6.5, 16.25, id="float")],
)
def test_rectangle_area(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.get_area == area, f"rectangle area must be {side_a} * {side_b} = {area}"


@pytest.mark.parametrize(
    ("side_a", "side_b", "perimeter"),
    [pytest.param(3, 6, 18, id="integer"), pytest.param(3.5, 6.5, 20, id="float")],
)
def test_rectangle_perimeter(side_a, side_b, perimeter):
    r = Rectangle(side_a, side_b)
    assert (
        r.get_perimeter == perimeter
    ), f"rectangle perimeter must be ({side_a} + {side_b}) * 2 = {perimeter}"


@pytest.mark.parametrize(
    ("side_a", "side_b", "add_area"),
    [pytest.param(3, 6, 82, id="integer"), pytest.param(3.5, 6.5, 86.75, id="float")],
)
def test_rectangle_add_area(side_a, side_b, add_area, create_square):
    r = Rectangle(side_a, side_b)
    assert (
        r.add_area(other_figure=create_square) == add_area
    ), f"sum area square and area rectangle must be ({side_a} * {side_b}) + 64 = {add_area}"


@pytest.mark.parametrize(
    ("side_a", "side_b"),
    [(0, 0), (-1, -1)],
    ids=["side_a or side_b = 0", "side_a or side_b = negative"],
)
def test_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)
