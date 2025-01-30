def decorateur(fonction):
    def wrapper():
        print("Je suis une ligne en plus")
        fonction()
        print("Je suis une ligne en plus après l'appel de la fonction")
    return wrapper

@decorateur
def fonction_a():
    print("Je suis dans la fonction")

fonction_a()