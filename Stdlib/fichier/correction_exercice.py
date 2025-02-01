import os
from  contextlib import suppress
import gc

dossier = os.path.dirname(__file__)
name = "exercice.txt"
abs_path = os.path.join(dossier, name)

file = None
try:
    file = open(abs_path, "r")
    for line in file.readlines():
        print(line.rstrip())
except Exception as e:
    print(f"{e}")
finally:
    if file:
        file.close()

with suppress(FileNotFoundError), open(abs_path, "r") as file:
    for line in file:
        print(line.rstrip())

with suppress(FileNotFoundError), open(abs_path, "r") as file_test:
    file_test.seek(10)
    contenu = file_test.read(20)
    print(contenu)