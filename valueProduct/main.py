import os
import math

# Produit des puissances de 2
# saisie de la puissance max
n = int(input("Entrer la puissance max ") )

# calcul du produit des puissances de 2
produit = 1 # n'est pas initialisable à 0 car 0*0=0
for k in range(1, n+1) :
    produit *= math.pow(2, k)

# affocher le résultat
print("Le produit des puissances de 2 jusqu'à puissance", n, "est", produit)

os.system("pause")