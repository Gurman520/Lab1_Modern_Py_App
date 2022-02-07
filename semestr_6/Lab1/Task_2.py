from zipfile import ZipFile
import os


def resize(size):
    index = 0
    fff = {0: "Байт", 1: "КБ", 2: "МБ", 3: "ГБ"}
    while size > 1024:
        size /= 1024
        index += 1
    print(round(size), fff[index])


with ZipFile('1 OS/archive.zip') as myzip:
    for name in myzip.namelist():
        # print(name)
        items = name.rstrip("/").split("/")
        if os.path.isfile(name):
            size = os.path.getsize(name)
            print(1)
            print("  "*(len(items)-1) + items[-1], resize(size))
        else:
            print("  " * (len(items) - 1) + items[-1])