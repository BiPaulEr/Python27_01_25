def fonction(tele = "05", forfait = 20, marque = "BalckBuerry", **kwargs):
    print(kwargs) #{'details_1': 'Noir', 'details_2': 'Pour 4'} {}
    print(tele, forfait, marque) 

fonction(tele = 3)
