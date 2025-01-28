def max(numbre1, numbre2, *args):
    maximum = numbre1 if (numbre1 > numbre2) else numbre2
    for element in args:
        if element > maximum:
            maximum = element
    return maximum

print(max(4, 5, 6, 7, 90, 4, "s"))