class Animal:
    def parler(self):
        return "Hoo!"
    
class Chien(Animal):
    def parler(self):
        return "Woof!"
    
class Chat(Animal):
    def parler(self):
        return "Miaou!"
    
animaux = [Chien(), Chat(), Chien()]

for animal in animaux:
    print(animal.parler())  # Polymorphisme en action