import os
from os import listdir
from os.path import isfile, join
from pprint import pprint


# print (os.getcwd())
# print (os.getlogin())

# env = os.environ.__dict__["_data"]
# pprint.pprint(env)

mypath = os.getcwd()
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


# for dirpath, dirs, files in os.walk(mypath):
#   for file in files:
#     file_name = os.path.join(dirpath, file)
#     print(file_name)
#     # if file_name.endswith('.py'):
#     #     print(file_name)

# for dirpath, dirs, files in os.walk(mypath):
#   for file in files:
#     file_name = os.path.join(dirpath, file)
#     print(file_name)



# print(d)
# for dirpath, dirs, files in os.walk(mypath):
#     print(dirs)

import os 
from pathlib import Path

path = Path.home()

size = 1024*1024

large_files = [e for e in path.rglob('*.*') if e.is_file() and os.path.getsize(e) >= size]

for file in large_files:
    print(f'{file} {os.path.getsize(file)}')