import os


def resize(size):
    index = 0
    fff = {0: "Байт", 1: "КБ", 2: "МБ", 3: "ГБ"}
    while size > 1024:
        size /= 1024
        index += 1
    return str(round(size)) + fff[index]


rezult = {}
size = 0
glob = "C:\\Users\\Роман Сулима\\Documents"
global_path = os.listdir(glob)
for path in global_path:
    size = 0
    for currentdir, dirs, files in os.walk(glob +'\\'+ path):
        for name in files:
            size += os.path.getsize(currentdir + '\\' + name)
    rezult[path] = size
rezult = sorted(rezult.items(), key=lambda x: x[1], reverse=True)
for i in range(10):
    print(rezult[i][0], resize(rezult[i][1]))
