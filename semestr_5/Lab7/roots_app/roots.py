import math


def roots(a, b, c):
    z = ()
    if type(a) != (float and int) or type(b) != (float and int) or type(c) != (float and int):
        return None
    if a == 0 and b == 0 and c == 0:
        return None
    if a == 0:
        return None
    dis = b ** 2 - 4 * a * c
    if dis < 0:
        return None
    elif dis == 0:
        x1 = -b / (2 * a)
        z = (x1, x1)
        return z
    elif dis > 0:
        x1 = (-b + math.sqrt(dis)) / (2 * a)
        x2 = (-b - math.sqrt(dis)) / (2 * a)
        if x1 > x2:
            z = (x2, x1)
        else:
            z = (x1, x2)
        return z
