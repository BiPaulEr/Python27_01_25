def decorateur_avec_argument(nombre_rep):
    def decorateur(fonction):
        def wrapper(*args, **kwargs):
            print(args)
            print("Je suis une ligne en plus")
            for i in range(0, nombre_rep):
                fonction(*args, **kwargs)
            print("Je suis une ligne en plus après l'appel de la fonction")
        return wrapper
    return decorateur

@decorateur_avec_argument(5)
def fonction_a(name):
    print(f"Je suis dans la fonction {name}")

@decorateur_avec_argument(2)
def fonction_b(name, prenom):
    print(f"Je suis dans la fonction {name} {prenom}")

fonction_a("fonction_a")

fonction_b("fonction_b", "fonction_b_prenom")
