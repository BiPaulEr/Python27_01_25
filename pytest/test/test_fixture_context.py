import pytest
import os
import time
 
@pytest.fixture(scope="module")
def file_setup():
    print("\nPREPARATION : Phase préparation file_setup\n")
    path = os.path.join(os.path.dirname(__file__), "data.tmp")
    f = open(path, "w")
    f.write("Ceci est de la donnee de test temporaire")
    f.close()
    print(f"Le yield se fait avec {path}")
    yield path
    print(f"\nNETTOYAGE : Après le yield : Phase nettoyage\n")
    time.sleep(5)
    os.remove(path)



def test_lecture_fichier_temporaire(file_setup):
    print("\nDEBUT : test_lecture_fichier_temporaire\n")
    with open(file_setup, "r") as f:
        content = f.read()
    assert content == "Ceci est de la donnee de test temporaire"
    
def test_lecture_fichier_temporaire_2(file_setup):
    print("\nDEBUT : test_lecture_fichier_temporaire\n")
    with open(file_setup, "r") as f:
        content = f.read()
    assert content == "Ceci est de la donnee de test temporaire"
    