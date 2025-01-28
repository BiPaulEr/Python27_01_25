
import copy

def function(liste):
    """
    Function qui modifie
    """
    liste[0] = 42

print(function.__doc__)

liste = [1, 2, 3]
liste_tmp = copy.deepcopy(liste)
function(liste_tmp)
print(liste)
print(liste_tmp)