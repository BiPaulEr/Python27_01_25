def decorateur(fonction):
    def wrapper(*args, **kwargs):
        print("Je suis une ligne en plus")
        fonction(*args, **kwargs)
        print("Je suis une ligne en plus après l'appel de la fonction")
    return wrapper

@decorateur
def fonction_a(name):
    print(f"Je suis dans la fonction {name}")

@decorateur
def fonction_b(name, prenom):
    print(f"Je suis dans la fonction {name} {prenom}")

fonction_a("fonction_a")

fonction_b("fonction_b", "fonction_b_prenom")
