from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def faire_du_bruit(self):
        """Méthode à implémenter obligatoirement."""
        pass

class Chien(Animal):
    def faire_du_bruit(self):
        return "Le chien aboie : Woof!"
    
def faire_bruit(animal: Animal):
    print(animal.faire_du_bruit())

chien = Chien()
faire_bruit(chien)  # Le chien aboie : Woof!

class Oiseau(Animal):
    pass

oiseau = Oiseau() #TypeError: Can't instantiate abstract class Oiseau without an implementation for abstract method 'faire_du_bruit'