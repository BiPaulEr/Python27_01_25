from abc import ABC, abstractmethod

class Instrument(ABC):
    @abstractmethod
    def jouer(self):
        pass

class Guitare(Instrument):
    def jouer(self):
        print("Dring")

class Piano(Instrument):
    def jouer(self):
        print("Piout")

guitare = Guitare()
piano = Piano()
liste_instrument = [piano, guitare]

class Batterie(Instrument):
    def jouer(self):
        print("Boom Boom")

batterie = Batterie()
liste_instrument.append(batterie)

class Chien(Instrument): 
    def jouer(self):
        print("Wouah")

chien = Chien()
liste_instrument.append(chien)

def faire_jouer(liste_instrument):
    for instrument in liste_instrument:
        instrument.jouer()

#faire_jouer(liste_instrument)

class Orchestre():
    def __init__(self, liste_instrument):
        self.liste_instrument = liste_instrument
    
    def ajouter(self, instrument):
        self.liste_instrument.append(instrument)

    def faire_jouer(self):
        for instrument in self.liste_instrument:
            instrument.jouer()

orchestre  = Orchestre(liste_instrument)
orchestre.ajouter( Guitare())
orchestre.faire_jouer()