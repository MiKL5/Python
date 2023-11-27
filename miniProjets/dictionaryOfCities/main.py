import os

villes = {}

# Saisie des villes et population
ville = input("Saisissez une ville (Validez pour arrêter la saisie) : ")

while ville != "" :
    villes[ville] = int(input("Saisissez la population = ") )
    ville = input("Saisissez une ville (Validez pour arrêter la saisie) : ")

# Recherche d'une ville
recherche = input("Saisissez la ville recherchée (validez pour arrêter la recherche) : ")
while recherche != "" :
    try :
        population = villes[recherche]
        print("Il y a", population, "habitants à", recherche)
    except :
        print(recherche, "n'est pas référencée")
    recherche = input("Saisissez la ville recherchée (validez pour arrêter la recherche) : ")

os.system("pause")