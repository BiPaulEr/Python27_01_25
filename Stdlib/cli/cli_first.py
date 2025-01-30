import argparse

parser = argparse.ArgumentParser(description="Traite les arguments.")
parser.add_argument('--age', default=28, type=int, help='Votre âge')

args = parser.parse_args()
print(type(args.age))
print(f"Votre âge est: {args.age}")