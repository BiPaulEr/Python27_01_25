class Animal:
    def __init__(self, nom):
        self.nom = nom
    def parler(self):
        return "Je suis un animal"

class Chien(Animal):
     def parler(self):
        return "Wouf!"

class Chat(Animal):
    def parler(self):
        return "Miaou!"
    
animal = Animal("Oiseau")
chien = Chien("Rex")
chat = Chat("Mimi")

print(animal.nom, "dit :", animal.parler())

print(chien.nom, "dit :", chien.parler())

print(chat.nom, "dit :", chat.parler())