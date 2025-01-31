import os 
cwd = os.path.dirname(__file__)
abs_path = os.path.join(cwd, "texergqt.txt")
file = None
try :
    file = open(abs_path, "r")
    for line in file.readlines():
        line = line.rstrip()
        print(line)
except Exception as e:
    print(f"{e}")
finally:
    print("Closed")
    if file:
        file.close()
