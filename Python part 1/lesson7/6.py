import os, pathlib

#print(os.listdir('data/'))

for entry in os.listdir():
    if os.path.isfile(entry):
        print(entry)
