import pytest

from src.Triangle import Triangle


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "area"),
    [
        pytest.param(8, 4, 6, 135, id="integer"),
        pytest.param(8.5, 6.5, 6.5, 436.88671875, id="float"),
    ],
)
def test_triangle_area(side_a, side_b, side_c, area):
    r = Triangle(side_a, side_b, side_c)
    assert r.get_area == area, f"triangle area must be {area}"


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "perimeter"),
    [
        pytest.param(6, 6, 8, 20, id="integer"),
        pytest.param(6.5, 6.5, 8.5, 21.5, id="float"),
    ],
)
def test_triangle_perimeter(side_a, side_b, side_c, perimeter):
    r = Triangle(side_a, side_b, side_c)
    assert (
        r.get_perimeter == perimeter
    ), f"triangle perimeter must be {side_a} + {side_b}) + {side_c} = {perimeter}"


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "add_area"),
    [
        pytest.param(5, 6, 9, 264, id="integer"),
        pytest.param(5.5, 6.5, 9.5, 363.82421875, id="float"),
    ],
)
def test_triangle_add_area(side_a, side_b, side_c, add_area, create_square):
    r = Triangle(side_a, side_b, side_c)
    assert (
        r.add_area(other_figure=create_square) == add_area
    ), f"sum area triangle and area square must be {add_area}"


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c"),
    [(0, 1, 2), (-1, -2, -3)],
    ids=["side_a or side_b or side_c = 0", "side_a or side_b or side_c = negative"],
)
def test_triangle_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


def test_triangle_not_buid_negative():
    with pytest.raises(ValueError):
        Triangle(2, 4, 1)
