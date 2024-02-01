# **Les `Sets`**  <a href="../"><img align="right" src="../../src/images/Python-logo-notext.svg" alt="Python" title="Phthon" widht="auto" height="64px"></a>

Ils sont un peu différents car ils ne sont pas ordonnés de manière fiable. Une liste ou un tuple imprime les éléments dans l’ordre défini. Ce n’est pas le cas pour un set (ensemble).

En outre, les sets ne peuvent contenir que des éléments uniques, comme avec les clés de dictionnaire. En fait, on peut considérer un ensemble comme un dictionnaire qui ne contient que des clés.

Alors pourquoi s’intéresser aux sets ? Tout d’abord, ils sont accompagnés d’un certain nombre d’opérations très utiles pour comparer les membres d’une collection : filtrer les valeurs, et il est également très efficace d’effectuer ce type de tests d’appartenance pour les sets.

## **Définir**

Comme pour les dictionnaires, les ensembles (sets) sont définis à l’aide d’accolades, mais au lieu de paires clé-valeur, il y a simplement une série de valeurs séparées par des virgules.
```py
vegetables = {"carotte", "laitue", "brocoli", "oignon", "carotte"}
```
Dans cet ensemble a la chaîne "carotte" deux fois. Cela ne produira pas d’erreur, mais l’ensemble ne contiendra qu’une seule instance de "carotte".
IL est possible de  définir un dictionnaire vide en utilisant {}. Pour cette raison, nous ne pouvons pas utiliser cette option pour définir un ensemble vide. Au lieu de cela, nous devons écrire ceci : `set()`.
Si nous imprimons un ensemble qui est vide, nous obtiendrons également cette représentation set(), pour distinguer la sortie d’un dictionnaire vide.

Il existe des valeurs interdite dans un ensemble, comme avec les clés du dictionnaire. Les limitations sont exactement les mêmes, ne pas inclure de types mutables dans un ensemble, ni de types immuables contenant des types mutables.

Pour cette raison, il est impossible d'ajouter de listes ou de dictionnaires à un ensemble, ni ajouter de tuples qui contiennent des choses comme des listes ou des dictionnaires.

On ne peut pas non plus inclure des ensembles dans d’autres ensembles, car les ensembles peuvent aussi être modifiés. Ce qui suit est donc illégal en Python :
```py
nested_sets = {{1,  2,  3},  {"a",  "b",  "c"}}
```
Si nous essayons, nous obtiendrons une TypeError :
```py
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    nested_sets = {{1, 2, 3}, {"a", "b", "c"}}
TypeError: unhashable type: 'set'
```

## **Modifier les sets**

La méthode `add()` permet l'ajout d'un seul élément et la méthode `update()` de plusieurs.  
Impossible d'ajouter un élément mutable.

La méthode `remove()` pour supprimer un seul élément.  
Si l'élément n'existe pas, il y aura une KeyError.  
L'utilisation de discard() supprime que les éléments existant donc ne renvoi pas d'erreur.  
Pour supprimer un élément sans savoir son nom, utiliser la méthode `pop()`.

## **Les opérations**

La méthode **union** permet d'unir deux ensembles, les membres en doubles ne sont inclus qu'une seule fois.
```py
letters_and_numbers = letters.union(numbers)
```
Contrairement à `update()` union crée un nouvel ensemble.  

L'**intersection** de deux ensembles, engendre l'obtention d'un nouvel ensemble contenant les éléments communs.  

Il faut être plus prudent avec la méthode `différence`, car l'ordre des ensembles a de l'importance.  
Avec `symmetric_difference` l'ordre des ensembles n'a pas d'importance et donne tous les éléments qui figurent dans l'un des ensembles. Donc, le contraire de `difference()`.  

Il est possible d'appeler les méthodes de l’opérateur set que sur des ensembles, mais il est possible de passer n’importe quelle collection dans la méthode. En effet, Python va convertir la collection en un ensemble avant d’effectuer l’opération.

## Vérifier la présence d'un élément

Le mot-clé `in` donne 'true' s'il élément est dans la collection, sinon 'false'.  
Il permet aussi de trouvé un clé dans un dictionnaire.

> cf.  
https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset