class Simplest():
    attribut_de_classe = " Je suis un attribut de classe "

print(Simplest.attribut_de_classe)

simp1 = Simplest()
print(simp1.attribut_de_classe)
simp1.attribut_de_classe = "Redéfini"

simp2 = Simplest() 
print(simp2.attribut_de_classe) # Je suis un attribut de classe
print(simp1.attribut_de_classe) #Redéfini

Simplest.attribut_de_classe = "QUOI ?"
print(simp2.attribut_de_classe) #QUOI ?

simp3 = Simplest()
print(simp3.attribut_de_classe)
print(simp1.attribut_de_classe)

del simp1.attribut_de_classe
print(simp1.attribut_de_classe)