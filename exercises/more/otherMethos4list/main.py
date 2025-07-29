# Les employés sont listés par ordre d'arrivée. Dans quelle position est arrivé Max ?
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
resultat = employes.index("Max")
print(resultat)

resultat = employes.index("Alex")
print(resultat)

# Combien se nomment Max ?
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex", "Max"]
resultat = employes.count("Max")
print(resultat)

# Trier alphabétiquement
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
employes.sort()
print(employes)

employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
liste_triee = sorted(employes) # retourn une liste triée, si le nom de la variable est le même, elle est écrasée
print(liste_triee)

# Inverser la liste
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
employes.reverse()
print(employes)