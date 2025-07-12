import math

# boucle sur le menu
menu = "z"
while menu != "Q" and menu != "q" :
    
    # afichage du manu
    print("Convesion d'un entier en binaire ..... 1")
    print("Convesion d'un bianire en entier ..... 2")
    print("Quitter le programme ................. Q")
    menu = input("Votre choix .......................... ")
    
    # Test du chois
    if menu == "1" :
        # Conversion d'un enter en binaire
        nb = int(input("Entrez un entier : ") )
        binaire = ""
        while nb != 0 :
            r = str(nb % 2) # r = reste # `str` transforme l'objet en chaîne
            binaire = r + binaire # `r` devant `binaire` car le nombre binaire se construit du dernier au premier
            nb = nb // 2
        print("Conversion en binaire : ", binaire)
    else :
        if menu == "2" :
            # Conversion d'un binaire en entier
            binaire = input("Entrer un  nombre binaire : ")
            k = 0 # k puissance
            nb = 0
            while len(binaire) > 0 :
                b = int(binaire[len(binaire) -1:] ) # si je ne précise pas le nb de caractère il va jusqu'à la fin et `b` = bit
                nb += b * math.pow(2, k)
                k += 1
                binaire = binaire[: len(binaire)-1] # Du début à l'avant dernier caractère
            print("Conversion en entier : ", nb)