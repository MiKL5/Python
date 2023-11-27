import math
import os

# Liste que mémorise les nombres premiers
premier = [0]*50 # Initialisée à 0 et contient 50 cases

# Initialisation de la première case
premier[0] = 2

# Boucle sur la recherche des 50 premiers nombres premiers (boucle indéterministe car je ne sais pas quand je vais trouver le 50e)
max = 1 # Initialiser à 1 car la liste contient déjà une valeur
nb = 3 # Variable qui sera testée
while max < 50 :
    # test si nb est premier
    k = 0 # indice pour parcourir la liste
    while k < max and premier[k] < math.sqrt(nb) and nb%premier[k] !=0 : 
        k += 1
    # si nb n'est pas divisible
    if nb%premier[k] != 0 :
        # nb est premier, donc mémorisé
        premier[max] = nb
        max += 1
    # Passage au nobre suivant à tester
    nb += 1
# Affichage des 50 nombres premiers
for k in range(0, 50) :
    print(premier[k] )

os.system('pause')