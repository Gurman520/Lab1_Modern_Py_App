import unittest
from Reverse_app.reverse import reverse


class ReverseTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            reverse(42)

    def test_wrong_type_2(self):
        with self.assertRaises(TypeError):
            reverse([24, 12, 45])

    def test_good(self):
        self.assertEqual(reverse("abc"), "cba")

    def test_one_simvol(self):
        self.assertEqual(reverse("a"), "a")

    def test_palindrom(self):
        self.assertEqual(reverse("roman"), "namor")


if __name__ == '__main__':
    unittest.main()