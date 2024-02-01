# **Qu'est qu'un dictionnaire ?**  <a href="../../"><img align="right" src="../../src/images/Python-logo-notext.svg" alt="Python" title="Phthon" widht="auto" height="64px"></a>

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

## **Le définir**

Nous créons un dictionnaire en utilisant une paire d’accolades : `{}`
Il s’agit en fait d’un dictionnaire vide, tout comme `[]` est une liste vide.

Lorsque nous voulons créer un dictionnaire avec du contenu, nous devons travailler par paires de clés et de valeurs. Un dictionnaire ne peut pas avoir de clé sans valeur, et nous ne pouvons pas avoir de valeur qui ne soit pas associée à une clé.

Imaginons que nous créons un dictionnaire pour un élève et que nous voulons commencer par une clé et une valeur représentant son nom :
```py
student = {"name": "John Smith"}
```
Tout d’abord, nous avons la clé – qui, dans ce cas, est la chaîne "name" – suivie de deux points ( :), puis la valeur associée à cette clé.

Si nous voulons ajouter plusieurs clés et valeurs, nous devons séparer chaque paire clé-valeur à l’aide de virgules.

Par exemple, ajoutons une liste de notes pour cet étudiant à côté de son nom :
```py
student = {
    "name": "John Smith",
    "grades": [88, 76, 92, 85, 69]
}
```
Note de style
Dans l’exemple ci-dessus, le dictionnaire a été réparti sur plusieurs lignes, comme nous l’avons fait avec nos tuples et nos listes. C’est une pratique courante lorsque le dictionnaire devient assez long, car elle facilite la lisibilité.

Ne vous sentez pas obligé de tout faire tenir sur une seule ligne comme ceci :
```py
student = {"name": "John Smith", "grades": [88, 76, 92, 85, 69]}
```
Si le dictionnaire peut facilement tenir sur une ligne, veillez à toujours mettre un espace après chaque virgule, comme nous le faisons pour les autres collections.

Un autre facteur important pour créer des dictionnaires lisibles consiste à ajouter un espace après les deux points. Cela permet de séparer les clés et les valeurs, ce qui permet de les repérer plus rapidement d’un coup d’œil.

## **Les noms de clés**

Il existe également certaines limitations techniques quant à ce que nous pouvons utiliser comme clé dans les dictionnaires Python.

Comme nous l’avons déjà vu, les chaînes de caractères conviennent parfaitement, mais aussi les nombres et même les tuples. Cependant, _nous ne pouvons jamais utiliser une liste comme clé_. Pourquoi pas ? _Parce qu’une liste peut changer_.

L’_une des principales caractéristiques des dictionnaires_ est que leurs _clés_ sont _uniques_. C’est très important pour la récupération des valeurs. Le problème des _listes est qu’elles offrent la possibilité de violer cette règle_, car nous pouvons modifier une liste après l’avoir définie comme clé. En ajoutant ou en supprimant des éléments, nous pouvons modifier une paire de listes de sorte qu’elles finissent par être identiques.

Le fait que cela puisse se produire signifie que Python ne nous permet tout simplement pas d’utiliser des listes comme clés, et il en va de même pour tout autre type que nous pouvons modifier.

Certains d’entre vous se demandent peut-être pourquoi nous pouvons utiliser des chaînes de caractères comme clés, puisqu’il semble que nous puissions également modifier des chaînes de caractères. Cependant, nous ne modifions jamais réellement une chaîne de caractères : nous en créons toujours une nouvelle.

Nous pouvons utiliser un tuple comme clé, avec quelques limitations. En effet, _les tuples peuvent pas contenir des éléments tels que des listes_, et nous pouvons modifier ces listes internes.

Par exemple, nous pouvons faire ceci :
```py
student = (
    "John Smith",
    [88, 76, 92, 85, 69]
)
# Ajouter 77 à la liste à l'index 1
student[1].append(77)
print(student)  # ('John Smith', [88, 76, 92, 85, 69, 77])
```
On ne peut donc utiliser comme clé dans un dictionnaire qu’un tuple qui ne contient pas de valeurs mutables.

___
>>> NB :  
Si la clé n'existe pas on obtient un keyError.
Cependant, si on est pas sûr qu'une clé existe sans levé d'error, il y a le méthode `get`.  
Ce dernier fonctionne comme une expression de souscription mais renvoi `None` sans planter le programme.

>> cf. [ce lien Docstring](https://www.docstring.fr/glossaire/dictionnaire/)  
cf. [Doc de Python](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)  
cf. [ce lien W3school](https://www.w3schools.com/python/python_dictionaries.asp)