import time

def cache(fonction):
    resultat = {}
    def wrapper(*args):
        if args in resultat:
            print(f"Résultat {args} cache avec la valeur {resultat[args]}")
            return resultat[args]
        result  = fonction(*args)
        resultat[args] = result
        print(f"update dict {resultat}") 
        return result
    return wrapper

@cache
def fonction_a(a, b):
    time.sleep(3)
    print(f"addition : {a + b}")
    return a + b


fonction_a(3, 8)

fonction_a(4, 9)

fonction_a(3, 8)

addition : 11
update dict {(3, 8): 11}
addition : 13
update dict {(3, 8): 11, (4, 9): 13}
Résultat (3, 8) cache avec la valeur 11