print(list(enumerate(['apple', 'banana', 'cherry'])))
#[(0, 'apple'), (1, 'banana'), (2, 'cherry')]

liste = ['apple', 'banana', 'cherry']
for index, element in enumerate(liste):
    liste[index] = element.upper()
    print(f"{index} : {element}")
    
print(liste)
