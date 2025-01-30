import argparse

parser = argparse.ArgumentParser(description="Traite les arguments.")
parser.add_argument('--scores', nargs='+', type=int, help='Liste des scores de lutilisateur')
parser.add_argument('--range', nargs=2, type=int, help="Définir une plage de valeurs")
args = parser.parse_args()
print(f"Scores fournis : {args.scores}")
print(f"Scores fournis : {args.range}")