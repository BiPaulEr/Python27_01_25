import os 
cwd = os.path.dirname(__file__)
abs_path = os.path.join(cwd, "text.txt")
file = None
try :
    file = open(abs_path, "r")
    file.seek(7)
    content = file.read(7)
    print(content)
except Exception as e:
    print(f"{e}")
finally:
    print("Closed")
    if file:
        file.close()
