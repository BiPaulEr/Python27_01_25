noms = ["Martin", "Dupont", "Genevieve"]
prenoms = ["Paul", "Ernest", "Sophie"]
nationalite = ["Fr", "Fr", "Fr"]
#[(0, ('Paul', 'Martin', 'Fr')), (1, ('Ernest', 'Dupont', 'Fr'))]

print(list(enumerate(zip(prenoms, noms, nationalite))))

for index, (prenom, nom, nation) in enumerate(zip(prenoms, noms, nationalite)):
    print(f"{prenom} {nom} {nation}")
    prenoms[index] = prenom.upper()

print(prenoms)