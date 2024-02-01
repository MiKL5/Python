# **Fonctions de premières classes et compréhensions lambda**  <a href="../../"><img align="right" src="../../src/images/Python-logo-notext.svg" alt="Python" title="Phthon" widht="auto" height="64px"></a>

Toutes les fonctions en Python sont des fonctions de première classes. 

## **Que sont les fonctions de premières classes ?**

Ce sont des fonctions qui sont traitées comme n'importe quel autre type. On dit qu'elles sont des citoyens de premières classes du langage.  

Généralement, ça signifie que nous pouvons passer des foncitons comme argument à d'autres fonctions, les retournées à partir de fonctions et les affecter à des variables.  

## **Affectation des fonctions de variables**

Lorsque l'on défini une fonction à l'aide de `def`, elle est nommée. Deux choses se produisent :
* elle est nommée conformément à nos spécifications ;
* Python créée une variable pour nous en utilisant ce nom et assigne la fonction à ce nom.

Tout d’abord, les deux fonctions sont exactement le même objet. Nous pouvons le constater car leurs adresses mémoire (à l’extrême droite) sont identiques.

Deuxièmement, les deux fonctions sont toujours appelées add lorsque nous imprimons cette représentation en chaîne des fonctions.

C’est parce que le nom de la variable que nous utilisons pour faire référence à la fonction et le nom de la fonction sont deux choses différentes.

## Foncitons en tant qu'arguments

Puisque nous pouvons affecter des fonctions à des variables, il est logique que nous puissions également passer des fonctions en tant qu’arguments, car les paramètres ne sont que des variables, et les arguments sont les valeurs que nous attribuons à ces variables.

## Retourner des fonctions à partir d'autres fonctions



## Expressions lambda

Les expressions lambda sont une syntaxe alternative pour définir des fonctions simples. L’une des caractéristiques très utiles de ces expressions est le fait qu’elles sont des expressions, et que la valeur à laquelle elles sont évaluées est la fonction que nous voulons créer.

En revanche, les définitions de fonctions utilisant le mot-clé def sont des déclarations. Elles n’ont pas de valeur, c’est pourquoi Python se donne la peine d’attribuer un nom à la fonction pour nous. L’une des principales limitations de cette méthode est que nous devons toujours définir nos fonctions séparément de l’endroit où nous voulons les utiliser.

Il n’y avait aucun moyen de définir la fonction dans le cadre de l’appel `max` lorsque l’on utilisait def. Cependant, nous n’avons pas cette limitation lorsque nous utilisons des expressions lambda, ce qui les rend très pratiques pour des choses comme les fonctions clés, qui ont généralement un corps de fonction d’une ligne.

La première partie de toute expression lambda est le mot-clé lambda. Directement après le mot-clé lambda, nous spécifions éventuellement les paramètres de la fonction que nous voulons créer. Contrairement aux définitions de fonctions ordinaires, ces valeurs ne sont pas placées entre parenthèses. Cette section de l’expression lambda est fermée par un deux-points.

Après les deux points vient une expression, et cette expression est ce que nous voulons retourner de la fonction.

Les expressions lambda sont limitées à des expressions simples et ne peuvent pas contenir de déclarations.

Toutes les fonctions en Python sont des fonctions de première classe, donc nous pouvons assigner les fonctions crées avec des expressions lambda à des variables.

### _**Note de style**_
Ne pas abuser des expressions lambda. Bien que nous puissions écrire des expressions très longues et compliquées comme valeurs de retour, ce n’est pas une bonne idée.

Si il y a besoin d’une fonction qui exécute une logique vraiment complexe, il est préférable de définir une fonction à l’aide de `def`, et de décomposer les opérations en étapes plus simples afin de pouvoir utiliser des variables descriptives et des commentaires pour documenter ce qui se passe.