import pytest
import Rectangle_app.rectangle as rectangle


@pytest.fixture(scope='module')
def create():
    rec = rectangle.Rectangle(10, 2)
    print(1)
    return rec


@pytest.fixture()
def area(create):
    assert create.get_area() == 20


@pytest.fixture()
def perimeter(create):
    assert create.get_perimeter() == 24


def test_1(area):
    print('area')


def test_2(perimeter):
    print("perimeter")


@pytest.mark.parametrize("len, wed, output", [("10", 2, "TypeError"), (1, "23", "TypeError"), (-3, 14, "ValueError"), (3, -14, "ValueError")])
def test_rectangle_2(len, wed, output):
    try:
        rectangle.Rectangle(len, wed)
    except rectangle.RectangleError as e:
        e == output
