import os


def resize(size, path):
    index = 0
    fff = {0: "Байт", 1: "КБ", 2: "МБ", 3: "ГБ"}
    while size > 1024:
        size /= 1024
        index += 1
    print(path, round(size), fff[index])


names = os.listdir(os.getcwd())
for name in names:
    if os.path.isfile(name):
        s_size = os.path.getsize(name)
        resize(s_size, name)
