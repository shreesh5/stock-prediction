import os
from zipfile import ZipFile

data = '../Data/News/'

files = os.listdir(data)

for f in files:
    dir = f.split('_')
    dir_name = dir[0] + '-' + dir[1]
    with ZipFile(data + f, "r") as zf:
        zf.extractall(data + dir_name)
