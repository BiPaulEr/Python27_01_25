import os 
cwd = os.path.dirname(__file__)
abs_path = os.path.join(cwd, "texegegt.txt")

with open(abs_path, "r") as file:
    for line in file.readlines():
        line = line.rstrip()
        print(line)