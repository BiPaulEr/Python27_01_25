def fonction(tele, forfait, *args,  marque = "BalckBuerry", **kwargs):
    print(args)
    print(kwargs) #{'details_1': 'Noir', 'details_2': 'Pour 4'} {}
    print(tele, forfait, marque) 

fonction("FR", "ADSL", "Argument pos en trop",  features = "Photo", batterie = "12Kwh")

