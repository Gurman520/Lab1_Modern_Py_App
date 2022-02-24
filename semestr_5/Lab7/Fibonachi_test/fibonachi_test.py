import pytest
import Fibonachi_app.fibonachi as fibonachi


@pytest.mark.parametrize("n, output",
                         [(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 56)])
def test_rectangle_1(n, output):
    assert fibonachi.fib(n) == output