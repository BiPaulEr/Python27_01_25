import argparse

parser = argparse.ArgumentParser(description="Traite les arguments.")

parser.add_argument('name', type=str, help='Name of the user')
parser.add_argument('--city', type=str, help='City of the user')

args = parser.parse_args()
if args.city:
    print(f"Name: {args.name}, City: {args.city}")
else:
    print(f"Name: {args.name}")