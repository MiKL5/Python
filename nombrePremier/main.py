import os

# Saisie du permier cheffre ou nombre à tester
val = int(input("Entrez un premier chiffre ou nombre entier (zéro pour finir) : ") )

# boucle générale sur les saisies des bombres à tester
while val != 0 :
    # boucle sur la recherche d'un diviseur
    diviseur = 2
    while val % diviseur != 0 and diviseur < - 1 : # 2 tests car il ce peut que ce soit un nombre permier & il faut s'arrêter un crant plus tôt car à chaque itération 1 est additioner au diviseur 
        diviseur += 1

    # affichage du message
    if val % diviseur != 0 :
        print(val, 'est premier')
    else :
        print(val, 'n\'est pas premier')

    # Saisie d'un cheffre ou nombre à tester
    val = int(input("Entrez un autre chiffre ou nombre entier (zéro pour finir) :") )

os.system("pause")