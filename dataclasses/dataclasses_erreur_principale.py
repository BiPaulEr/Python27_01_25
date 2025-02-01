from dataclasses import dataclass, field
import math

@dataclass
class Librairie():
   liste_livre : list = field(default_factory=list)
   
   def append(self, livre):
       self.liste_livre.append(livre)

   def afficher(self):
      print(self.liste_livre)

librarie1 = Librairie()
librarie1.append("Le petit Prince")
librarie1.append("Les Misérables")

librarie2 = Librairie()
librarie2.append("Le Corniaud")
librarie2.append("La Grande Vadrouille")

librarie1.afficher() #['Le petit Prince', 'Les Misérables', 'Le Corniaud', 'La Grande Vadrouille']