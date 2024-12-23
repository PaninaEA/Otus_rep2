import pytest

from src.Circle import Circle


@pytest.mark.parametrize(
    ("radius", "area"),
    [
        pytest.param(9, 254.46900494077323, id="integer"),
        pytest.param(9.5, 283.5287369864788, id="float"),
    ],
)
def test_circle_area(radius, area):
    r = Circle(radius)
    assert r.get_area == area, f"circle area must be {area}"


@pytest.mark.parametrize(
    ("radius", "perimeter"),
    [
        pytest.param(6, 37.69911184307752, id="integer"),
        pytest.param(6.5, 40.840704496667314, id="float"),
    ],
)
def test_circle_perimeter(radius, perimeter):
    r = Circle(radius)
    assert r.get_perimeter == perimeter, f"circle perimeter must be {perimeter}"


@pytest.mark.parametrize(
    ("radius", "add_area"),
    [
        pytest.param(9, 318.46900494077323, id="integer"),
        pytest.param(9.5, 347.5287369864788, id="float"),
    ],
)
def test_circle_add_area(radius, add_area, create_square):
    r = Circle(radius)
    assert (
        r.add_area(other_figure=create_square) == add_area
    ), f"sum area square and area circle must be {add_area}"


@pytest.mark.parametrize(
    "radius",
    [pytest.param(0, id="radius = 0"), pytest.param(-1, id="radius = negative")],
)
def test_circle_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)
