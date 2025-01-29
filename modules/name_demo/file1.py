attribut_du_module_file = "Attribut du module file1"
print(f"file1.py __name__ :  {__name__}")
def fonction_file1():
    print(attribut_du_module_file)

if __name__ == "__main__":
    fonction_file1() 