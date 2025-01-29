def generateur(max):
    for i in range(0, max+1):
        yield i 
        print("After yield")

gen = generateur(10)

""" print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


next(gen) # erreur StopIteration """

for i in generateur(10):
    print(i)

for i in generateur(20):
    print(i)