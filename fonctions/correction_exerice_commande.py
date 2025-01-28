def afficher_prix_total(prix_plat_principal, prix_entree, *command_suppl, prix_dessert = 10, **details_commande):
    print(f"Le prix du {prix_plat_principal}, l'entree {prix_entree}, le prix desert {prix_dessert}")
    somme = prix_plat_principal + prix_entree + prix_dessert + sum(command_suppl)
    print(details_commande)
    print(f"Somme {somme}")

details_command_arg = {'client':'John Doe', 'table':5, 'alergie':'sans gluten'}

afficher_prix_total(10 , 12, 10 , 20 + 30, desert = 50, **details_command_arg)

