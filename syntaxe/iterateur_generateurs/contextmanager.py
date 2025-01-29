file = open("./text.txt", "r")
for line in file.readlines():
    print(line.rstrip())
file.close()

with open("./text.txt", "r") as file:
    for line in file.readlines():
        print(line.rstrip())
