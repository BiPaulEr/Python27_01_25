produits = [
    {'name': 'yaourt', 'date_expiration': "aujourdhui", 'prix': 100.0},
    {'name': 'lait', 'date_expiration': "demain", 'prix': 50},
    {'name': 'oeufs', 'date_expiration': "aujourdhui", 'prix': 20},
]
for produit in produits:
    if produit['date_expiration'] != "aujourdhui":
            print(f"Prix pour le produit {produit['name']} est inchange")
            continue
    produit['prix'] *= 0.8  # Application d'une réduction de 20%
    print(f"Prix pour le produit {produit['name']} est maintenant {produit['prix']}")