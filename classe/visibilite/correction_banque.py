class Banque:
    def __init__(self, montant):
        self.__compte = montant

    def __operation(self, montant):
        print(f"Before operation {self.__compte}")
        self.__compte += montant
        print(f"After operation {self.__compte}")
    
    def depot(self, montant):
        if (montant > 0):
            self.__operation(montant)
            
banque1  = Banque(1000)
banque1.depot(100)
banque1.depot(-10)

#banque1.__operation(-500) #not possible
#banque1.__compte += 100000000000000 #not possible

#mais
banque1._Banque__compte += 10000000000
banque1._Banque__operation(-500)  #After operation 10000000600