class Voiture:
    def __init__(self, modele, marque_nom = "Renault"):
        print(self) #<__main__.Voiture object at 0x000002A20D95FBC0>
        self.marque = marque_nom
        self.modele = modele
    
    def afficher(self):
        print(self.marque, self.modele)


clio = Voiture("Clio")
print(clio)
print(clio.marque)
clio.afficher() #Renault Clio

Voiture.afficher(clio) #Renault Clio

polo = Voiture("Polo", "Volfswagen")
print(polo)
print(polo.marque)

"""
clio = Voiture("Renault")

polo = Voiture("Volfwagen")
print(polo.marque)

ds = Voiture("Citroen")
print(ds.marque)
"""