from roots_app.roots import roots
import pytest


def test_good():
    assert roots(3, 7, -6) == (-3.0, 0.6666666666666666)


def test_one_root():
    assert roots(4, 4, 1) == (-0.5, -0.5)


def test_not_root():
    assert roots(2, 1, 1) is None


def test_wrong_type():
    assert roots(32, 9, "hello") is None


def test_zero():
    assert roots(0, 0, 0) is None


def test_first_zero():
    assert roots(0, 0, 2) is None
