import argparse

livres = [
    {"id" : 1, "titre": "Les Misérables", "auteur": "Victor Hugo", "annee_publication": 1862},
    {"id" : 2, "titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupéry", "annee_publication": 1943},
    {"id" : 3, "titre": "Candide", "auteur": "Voltaire", "annee_publication": 1759},
]

parser = argparse.ArgumentParser(description="Ajouter des livres à une bilbiotheque")
sub_parser = parser.add_subparsers(dest="command", help="Commandes utilisateur add / del")

add_parser = sub_parser.add_parser("add", help="Ajouter")
add_parser.add_argument("titre", type=str, help="Titre du livre")
add_parser.add_argument("--auteur", default="Auteur Inconnu", type=str, help="Auteur du livre")
add_parser.add_argument("--annee_publication", default=-999999, type=int, help="Annee de publication du livre")

del_parser = sub_parser.add_parser("del", help="Delete")
del_parser.add_argument("id", type=int, help="identifiant")

args = parser.parse_args()
if args.command == "add":
    if args.titre in map(lambda x: x["titre"], livres):
        print("Titre already in the dictionnary. Abort")
    else:
        current_id = max(map(lambda x: x["id"], livres))
        livres.append( { "id" : current_id+1, "titre" : args.titre,  "auteur": args.auteur, "annee_publication" : args.annee_publication})
        print("Livre added to the dictionanry")
        print(livres)
else:
    if args.id in map(lambda x: x["id"], livres):
       index = list(map(lambda x: x["id"], livres)).index(args.id)
       livres.pop(index)
       print("Deletion")
       print(livres)
    else:
        print("Bad idea")
