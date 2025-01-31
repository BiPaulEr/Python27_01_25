def convertir_en_entier(chaine: str):
    if not isinstance(chaine, str):
        raise TypeError(f"{chaine} is a {type(chaine)} and not str")
    try:
        result  = int(chaine)
    except ValueError as ve:
        print(f"{ve}")
    else:
        return result
    finally:
        print("Operation de conversion est terminé")

try:
    entier1 = convertir_en_entier("4")
    entier2 = convertir_en_entier("4.5")
    entier3 = convertir_en_entier(["OK"])
except TypeError as te:
    print(f"{te}")

class TailleInvalideException(Exception):
    pass

def verifier_taille(chaine):
    if len(chaine) < 5:
        raise TailleInvalideException(f"La chaine {chaine} est de longeur {len(chaine)}")

try:
    verifier_taille("quelquechose de long")
    verifier_taille("q")
except TailleInvalideException as ti:
    print(f"{ti}")