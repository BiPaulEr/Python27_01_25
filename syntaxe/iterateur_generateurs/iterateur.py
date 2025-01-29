i = iter("abc")

print(next(i))
print(next(i))
print(next(i))

next(i) #StopIteration

for carrac in i:
    print(carrac)

for carrac in i:
    print(carrac)