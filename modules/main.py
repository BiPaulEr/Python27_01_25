import file
file.bonjour("Paul")
        
print(file.nom_de_famille)

print("end")

print(dir(file))


""" Importation avant definition dans le  __init__ de utils
import utils.salut_module as slt_m

slt_m.salut("TEST")

import utils.math.operations as mo

mo.addition(3, 5)

"""

"""
import utils

utils.addition(3,5)
utils.salut("Importaion facile avant __init__")

"""

from utils import *

addition(3,5)
#salut("directement importé") not disponible pas dans le __all__