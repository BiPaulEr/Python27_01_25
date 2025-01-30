import argparse

livres = [
    {"titre": "Les Misérables", "auteur": "Victor Hugo", "annee_publication": 1862},
    {"titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupéry", "annee_publication": 1943},
    {"titre": "Candide", "auteur": "Voltaire", "annee_publication": 1759},
]

parser = argparse.ArgumentParser(description="Ajouter des livres à une bilbiotheque")
parser.add_argument("titre", type=str, help="Titre du livre")
parser.add_argument("--auteur", default="Auteur Inconnu", type=str, help="Auteur du livre")
parser.add_argument("--annee_publication", default=-999999, type=int, help="Annee de publication du livre")

args = parser.parse_args()

if args.titre in map(lambda x: x["titre"], livres):
    print("Titre already in the dictionnary. Abort")
else:
    livres.append( {"titre" : args.titre,  "auteur": args.auteur, "annee_publication" : args.annee_publication})
    print("Livre added to the dictionanry")
    print(livres)