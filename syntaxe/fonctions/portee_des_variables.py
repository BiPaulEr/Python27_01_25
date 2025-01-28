def function():
    c = 8 
    def sous_fonction():
        global a
        nonlocal c
        b = 3
        c = "Modifier dans la sous_fonction"
        a = "Modifié A par sous_fonction"
        print("OK")
    sous_fonction()
    print(c)

a = "Cest A"
object_return = function()
print(a)