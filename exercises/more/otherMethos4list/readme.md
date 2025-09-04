# **Autres méhodes pour les listes**<a href="../../../"><img align="right" src="../../../assets/logo/Python-logo-notext.svg" alt="Python" height="64px"></a>
## **La méthode '`inddex`'**
Donne l'ordre des éléments depuis 0.
```py
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
resutalt = employes.index("Max")

print(resultat)
```
## **La méthode '`count`'**
Donne le nombre d'ocurence.
```py
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex", "Max"]
resultat = employes.count("Max")
print(resultat)

employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
liste_triee = sorted(employes)
print(liste_triee)
```
## **La méthode '`reverse`'**
Inverse la liste
```py
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
employes.reverse()
print(employes)
```