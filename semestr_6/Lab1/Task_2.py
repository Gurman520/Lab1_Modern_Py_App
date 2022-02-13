from zipfile import ZipFile
import os
import shutil


def resize(size):
    index = 0
    fff = {0: "Байт", 1: "КБ", 2: "МБ", 3: "ГБ"}
    while size > 1024:
        size /= 1024
        index += 1
    return str(round(size)) + fff[index]


global_path_in = './1 OS/archive.zip'
global_path_out = '.\\arch'
archive = ZipFile(global_path_in, 'r')
archive.extractall(global_path_out)
archive.close()
count = 0

for currentdir, dirs, files in os.walk(global_path_out):
    items = currentdir.rstrip("\\").split("\\")
    for name in files:
        if os.path.isfile(currentdir + '/' + name):
            size = os.path.getsize(currentdir + '/' + name)
            print("  "*(len(items) - 2) + name, resize(size))
        else:
            print("  " * (len(items) - 2) + name)

shutil.rmtree(global_path_out)
