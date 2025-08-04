# **Listes imbriquées**<a href="../../../"><img align="right" src="../../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
<!-- Les slices sont utilisables avec les listes imbriquées. -->
```py
liste = ["Python", ["Java", "C++"], ['C'], ["Ruby"]]
print(liste[1][0])

print(liste[0][0:2])

second_element = liste[1]
print(second_element[1])
```
⚠️ Avec la méthode '`remove`', il faut désigner l'élément, pas l'indice. S'il y a 2 fois le même élément, le premier est enlevé.  
⚠️ Avec la méthode '`remove`', il faut désigner l'élément, pas l'indice. S'il y a 2 fois le même élément, le premier est enlevé.  
⚠️ C'est '`pop`' qui permet le retrait d'un élément via l'indice. Sans précision, c'est le dernier élément qui est retiré.
___
Une liste est une structure de données _muable_ et ordonnée dans laquelle est stocker n'importe quel type d'objet.  
C'est une séquence de données. Signifiant qu'il est possible d'itérer sur cette séquence, avec une boucle 'for' par exemple.