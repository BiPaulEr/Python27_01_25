class ContextIllustration:
    def __enter__(self):
        print("J'entre dans le contexte")
        return "Object disponible dans le contexte"

    def __exit__(self, exc_type, exc_instance, traceback):
        print("Je sors du contexte")
        if (exc_type):
            print(f"Exeption de type {exc_type} avec pour valeur {exc_instance}")
        else:
            print("Pas d'exception dans le contexte")
        return True
    

with ContextIllustration() as object:
    print(object)
    raise Exception("de la valeur")
    print("je suis dans le contexte")