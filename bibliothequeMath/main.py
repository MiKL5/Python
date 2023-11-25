import os
import math

# saisie de la puissance max
n = int(input("Entrer la puissance max ") )

# calcul de la somme des puissances de 2
somme = 0
for k in range(1, n+1) :
    somme += math.pow(2, k)

# affocher le résultat
print("La somme des puissances de 2 jusqu'à puissance", n, "est", somme)

os.system("pause")