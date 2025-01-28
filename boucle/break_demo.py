elements = ['pomme', 'banane', 'cerise', 'date', 'banane', 'baie']
tmp = []
for element in elements:
    if element in tmp:
        print(f"Element DOUBLE : {element}")
        break
    print(f"Element : {element}")
    tmp.append(element)