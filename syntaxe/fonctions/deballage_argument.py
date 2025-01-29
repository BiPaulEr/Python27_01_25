dictionnaire = {"features" : "Photo", "batterie" : "12Kwh"}
tuple_arg = (1, 3, 4, "tuple")

def fonction(tele, forfait, *args,  marque = "BalckBuerry", **kwargs):
    print(args)
    print(kwargs)
    print(tele, forfait, marque) 


fonction("FR", "ADSL", "Argument pos en trop", *tuple_arg,  **dictionnaire)

#transformé en ça
fonction("FR", "ADSL", "Argument pos en trop", 1, 3, 4, "tuple",  features = "Photo", batterie = "12Kwh")
