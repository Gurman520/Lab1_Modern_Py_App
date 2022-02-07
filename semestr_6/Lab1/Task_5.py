import os
import shutil
import json
from zipfile import ZipFile


global_path_in = 'arch.zip'
global_path_out = './arch'
archive = ZipFile(global_path_in, 'r')
archive.extractall(global_path_out)
archive.close()


count = 0
for currentdir, dirs, files in os.walk(global_path_out):
    for name in files:
        if os.path.isfile(currentdir+'/'+name):
            if name.endswith(".js"):
                with open(currentdir+'/'+name) as file:
                    data = json.load(file)
                    if data['city'] == 'Moscow':
                        count += 1
print(count)

shutil.rmtree(global_path_out)
