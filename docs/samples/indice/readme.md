# **Les indices**<a href="../../../"><img align="right" src="../../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
Les indices servent à récupérer les éléments dans une liste.  
C'est la position d'un élément à la structure de données.  
Python commence à compter de 0. Les indices négatifs sont disponibles, et correspondent au nombre éléments contenus. Ici "0" à pour indice négatif "-3".
```py
liste=("neuf", 20, False)
print(liste[ 0]) # neuf
print(liste[ 2]) # False
print(liste[-3]) # neuf
```
```py
liste = [1, 2, [3, "Python", 4], 5, 6]
print([2][1])
```