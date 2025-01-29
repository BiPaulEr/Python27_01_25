class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def saluer(self):
        print(f"Bonjour {self.nom} {self.prenom}")

personne1 = Personne("Alice", "Prenom1")
personne1.saluer()

personne2 = Personne("Jean",  "Prenom2")
personne2.saluer()