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

# import os 
# from pathlib import Path
# path = Path.home()
# size = 1024*1024
# large_files = [e for e in path.rglob('*.*') if e.is_file() and os.path.getsize(e) >= size]
# for file in large_files:
#     print(f'{file} {os.path.getsize(file)}')

# from prettytable import PrettyTable
# from pathlib import Path
# import time
# pt = PrettyTable()
# path = Path.cwd()
# all_files = []
# pt.field_names = ['File name', 'Suffix', 'Created']
# for e in path.rglob('*.*'):
#     pt.add_row((e.name, e.suffix, time.ctime(e.stat().st_ctime)))
# print(pt)



import pandas as pd
from pathlib import Path
import time

path = Path.cwd()
all_files = []

for e in path.rglob('*.*'):
    all_files.append((e.name, e.parent, time.ctime(e.stat().st_ctime)))

columns = ['File_Name', 'Parent', 'Created']
df = pd.DataFrame.from_records(all_files, columns=columns)

print(df.head(5))