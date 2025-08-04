# **Le tuple**<a href="../../../"><img align="right" src="../../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
Le tuple est limité en fonctionnalités et occupe moins de place en mémoire.  
Il est immutable.

Si la liste a un nombre fixe d'éléments et qu'il faudra gérer de nombreuses listes, les tuples allègent le programme.  
Sa syntaxe est "()". Comme la liste, il peut contenir différents types.
```py
le_tuple = (250, "Python", True)
```
⚠️  "tuple" est réservé.

Il est possible de convertir un tuple en liste et vice versa.
```py
mon_tuple = (1, 2, 3)
liste = list(mon_tuple)
[1, 2, 3]
mon_tuple = tuple(liste)
(1, 2, 3)
```
⚠️ Avec les tuples, il faut aussi utiliser les crochets pour récupérer les éléments.
⚠️ Avec la méthode '`remove`', il faut désigner l'élément, pas l'indice. S'il y a 2 fois le même élément, le premier est enlevé.  
⚠️ C'est '`pop`' qui permet le retrait d'un élément via l'indice. Sans précision, c'est le dernier élément qui est retiré.