# Qu'est qu'un dictionnaire ?

Un tableau associatif est pour Python un dictionnaire, et fonctionne un peu différemment des listes, des chaînes de caractères et des tuples.

La séquence est un terme technique en Python, qui fait référence à une collection qui satisfait au protocole de séquence. Pour qu’un élément soit une séquence, il doit avoir des indices ordonnés qui commencent à 0 et qui s’incrémentent par pas de 1. Il doit également être possible de trouver la longueur de la collection avec len.

Dans un tableau associatif, et donc un dictionnaire, les valeurs sont plutôt associées à un autre terme. Si nous changeons l’ordre des valeurs, cela n’a pas d’importance, car chaque valeur sera toujours associée au même terme. Ces termes associés sont appelés `clés`.

Une clé (`key`) est un peu comme une variable, c’est-à-dire qu’il s’agit d’un élément que nous pouvons utiliser pour faire référence à une valeur. Contrairement aux variables, les clés sont elles-mêmes des valeurs, car elles s’écrivent sous forme de chaînes de caractères, d’entiers, etc.

Dans un seul dictionnaire, chaque clé doit être unique, mais des dictionnaires différents peuvent avoir les mêmes clés les uns que les autres.

Un dictionnaire peut avoir plusieurs clés, mais chaque clé doit être unique à l’intérieur de ce dictionnaire, et chaque clé doit avoir une seule valeur. Cette valeur peut toutefois être une collection, y compris un autre dictionnaire.

Un cas d’utilisation courant des dictionnaires est très similaire à la façon dont nous avons utilisé les tuples pour représenter les lignes d’un tableau. Par exemple, au lieu d’avoir un tuple comme celui-ci pour représenter un film :
```py
("Up", "Pete Doctor", 2009)
```
Nous pourrions utiliser un dictionnaire avec trois clés : "title", "director", et "release_year". Nous pourrions ensuite récupérer la valeur que nous voulons en demandant au dictionnaire la valeur associée à une clé donnée. Par exemple, nous pourrions vouloir la valeur associée à la clé "title". Dans ce cas, on nous donnerait la chaîne "Up".


>> cf. [ce lien Docstring](https://www.docstring.fr/glossaire/dictionnaire/)  
cf. [ce lien W3school](https://www.w3schools.com/python/python_dictionaries.asp)