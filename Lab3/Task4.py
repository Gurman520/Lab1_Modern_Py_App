class DefaultList(list):
    def __init__(self, default):
        list.__init__(self)
        self.default = default

    def __getitem__(self, item):
        try:
            return list.__getitem__(self, item)
        except IndexError:
            return self.default


s = DefaultList(51)
s.extend([1, 5, 7])
indexes = [0, 2, 1000, -1]
for i in indexes:
    print(s[i], end=" ")
