# 4) Utilisez la fonction randint de l’exercice ci-dessus pour créer une nouvelle version du jeu de devinette que nous avons créé au Jour 8. Cette fois, le programme doit générer un nombre aléatoire et vous devez indiquer à l’utilisateur si son estimation est trop élevée ou trop basse, jusqu’à ce qu’il obtienne le bon nombre.


import random as rand


target_number = rand.randint(1, 100) # random génère un chiffre ou nmbre

guess = int(input("Devinez un chiffre ou un nombre : "))
while guess != target_number:
    if guess > target_number:
        print("Troop élevé, réessayez !")
    else:
        print("Trop bas, réessayez !")
    guess = int(input("Ressaisissez : "))
print("Bravo !")