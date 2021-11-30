class RectangleError(Exception):
    pass


class ValueError(RectangleError):
    pass


class TypeError(RectangleError):
    pass


class Rectangle:
    def __init__(self, length, width):
        if not isinstance(length, int) or not isinstance(width, int):
            raise TypeError("TypeError")
        if length < 0 or width < 0:
            raise ValueError("ValueError")
        self.length = length
        self.width = width

    def get_area(self):
        s = self.length * self.width
        return s

    def get_perimeter(self):
        p = (self.length + self.width) * 2
        return p
