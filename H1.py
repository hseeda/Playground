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


for dirpath, dirs, files in os.walk(mypath):
  for file in files:
    file_name = os.path.join(dirpath, file)
    print(file_name)
    # if file_name.endswith('.py'):
    #     print(file_name)

for dirpath, dirs, files in os.walk(mypath):
  for file in files:
    file_name = os.path.join(dirpath, file)
    print(file_name)

    