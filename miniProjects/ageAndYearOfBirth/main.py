from datetime import date

ok = False
while not ok :
    try :
        age = int(input("Entrez votre âge : ") )
        assert age > 0
        ajourdhui = date.today().year
        naissance = ajourdhui - age
        print("Vous êtes né.e en", naissance)
        ok = True
    except ValueError :
        print("Veuillez saisir un entier.")
    except AssertionError :
        print("L'âge doit être d'au moins un an")