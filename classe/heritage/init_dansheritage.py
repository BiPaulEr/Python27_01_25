class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        return f"Je suis {self.nom}"

class Chien(Animal):
    def __init__(self, nom, race):
        self.race = race
        super().__init__(nom)
    
    def parler(self):
        parent_message = super().parler()  # Appelle la méthode 'parler' du parent
        return f"{parent_message} et je suis un chien de race {self.race}"

chien = Chien("Rex", "Labrador")

print(chien.parler()) #AttributeError: 'Chien' object has no attribute 'nom'