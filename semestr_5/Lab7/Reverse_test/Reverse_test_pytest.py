from Reverse_app.reverse import reverse
import pytest


def test_reverse():
    assert reverse('roman') == 'namor'


def test_wrong_type():
    with pytest.raises(TypeError):
        reverse(32)


def test_wrong_type_2():
    with pytest.raises(TypeError):
        reverse([32, 14, 85])


def test_empty():
    assert reverse("") == ""


def test_one_simvol():
    assert reverse("a") == "a"


def test_palindrom():
    assert reverse("abba") == "abba"
