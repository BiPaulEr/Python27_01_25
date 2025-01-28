#[nouvel_élément for élément in iterable if condition]

liste = [1, 2, 3, 4]

liste2 = [element**2 for element in liste if (element % 2)]
print(type(liste2)) #<class 'list'>
print(liste2) #[1, 9]

liste3 = map(lambda x : x**2, filter(lambda x : x%2, liste))
print(liste3) #[1, 9]

liste4 = (element**2 for element in liste if (element % 2))
print(type(liste4)) #<class 'generator'>
#print(list(liste4))

print(next(liste4))#1
print(next(liste4))#9
print(next(liste4))#erruer

