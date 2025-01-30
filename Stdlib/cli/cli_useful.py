import argparse

parser = argparse.ArgumentParser(description="Traite les arguments.")
parser.add_argument('--color', choices=['red', 'green', 'blue'], help="Couleur préférée")
parser.add_argument('--verbose', action='store_true', help='Mode verbeux')

args = parser.parse_args()

print(f"Flag {args.verbose}")

print(f"Couleur choisie : {args.color}")