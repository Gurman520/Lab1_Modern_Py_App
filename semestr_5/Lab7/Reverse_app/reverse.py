def reverse(s):
    if type(s) != str:
        raise TypeError()
    return s[::-1]
