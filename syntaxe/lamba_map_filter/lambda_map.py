#addition = lambda x, y: x + y

def addition(x, y):
    return x + y

def multiplier(x):
    return x * 5
    
nombres = [1, 2, 3, 4]  

print(list(map(multiplier, nombres))) #[5, 10, 15, 20]

for index, valeur in enumerate(nombres):
    nombres[index] = multiplier(valeur)

def diviser(x):
    return x / 5

print(list(map(diviser, nombres))) #[1.0, 2.0, 3.0, 4.0]

print(list(map(lambda x: x ** 2, nombres))) #[25, 100, 225, 400]

prenoms = ["Paul", "Ernesrt"]
print(list(map(lambda x: x.upper(), prenoms))) #['PAUL', 'ERNESRT']

mots = ["Python", "", "est", "", "génial", ""] 
mots_filtre = list(filter(lambda x: x != "", mots)) #['Python', 'est', 'génial']
print(mots_filtre )
