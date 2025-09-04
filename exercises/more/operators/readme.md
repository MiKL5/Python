# **Les opérateurs**<a href="../../../"><img align="right" src="../../../assets/logo/Python-logo-notext.svg" alt="Python" height="64px"></a>
## **Les opérateurs mathématiques**
La division retourne un nombre décimal. Les autres un entier.  
Il est possible de dupliquer ou multiplier des mots.

Les autres sont le `%` modulo, la `//` division entière et la `**` puissance.
### Le modulo
Récupère le reste d'une division.
```py
print(10 % 2)       # 0
print( 6 % 4)       # 2
```
### La division entière
```py
print(10 // 2)       # 2
print(10  / 3)       # 3.3333333333333335
print(10 // 3)       # 3
```
### La puissance
```py
print(2 ** 4)         # 16
```
## **Les opérateurs mathématiques avancées avec le module math**
Pour faire des calculs mathématiques avancés en Python, il faut utiliser le module math.
On l’importe ainsi :
`import math`

Ensuite, on utilise les fonctions du module en les préfixant par math.
Exemple pour la racine carrée :
racine = math.sqrt(16)
```py
print(racine)         # Affiche 4.0
```
**Voici des fonctions utiles du module math :**
* `math.ceil(-4.7)`   : entier supérieur, ici -4.
* `math.exp(2)`       : exponentielle de 2.
* `math.factorial(5)` : factorielle de 5, soit 120 (entiers positifs seulement).
* `math.floor(-4.7)`  : partie entière, ici -5.
* `math.isinf(x)`     : teste si x est infini.
* `math.log(2)`       : logarithme naturel de 2.
* `math.log(8, 2)`    : log de 8 en base 2.
* `math.log10(2)`     : logarithme base 10 de 2.
* `math.pow(2, 3)`    : 2 puissance 3 (équivalent à 2 ** 3).
* `math.sqrt(16)`     : racine carrée de 16, soit 4.

**Fonctions trigonométriques (en radians) :**
* `math.sin`          : sinus
* `math.cos`          : cosinus
* `math.tan`          : tanjante
* `math.asin`         : arc sinus
* `math.acos`         : arc cosinus
* `math.atan`         : arc tanjante

**Fonctions hyperboliques :**
* `math.sinh`         : sinus hyperbolique
* `math.cosh`         : cosinus hyperbolique
* `math.tanh`         : tangente hyperbolique
* `math.asinh`        : arc tangente hyperbolique
* `math.acosh`        : arc cosinus hyperbolique
* `math.atanh`        : arc tangente hyperbolique

**Conversions d’angles :**
* `math.degrees(x)`   : radians → degrés
* `math.radians(x)`   : degrés → radians

**Constantes :**
* `math.pi`           : 3.14159…
* `math.e`            : 2.71828…
## **Les opérateurs d'assignation**
* `=` n'est pas le seul opérateur d'assignation.
* `+=` permet l'assignation d'une incrémentation.
* `-=` pour assigner une décrémentation.
* `*=` assigne la multiplication.  
* `/=`
* `%=`
* `+=`
* `//=` assigne la division entière.
* `**=` élève la variable à gauche à la puissance de l'opérande à droite.
```py
i =     2
i = **= 4             # 16
```
## **Les opérateurs de comparaison**
* `>`
* `<`
* `>=`
* `<=`
* `==` se distingue de `=` pour il s'agit là de la même valeur.
* `!=` différent de (e.g. pour réstrindre l'accés à une pages celon l'utilisateur)

<!-- Il sont utilisés avec des structures conditionnelles. -->
## **La différence entre `is` et `=`**
`is` vérifie que les 2 mêmes objets sont en mémoire.  
`=`  vérifie l'égalité des valeurs en variable.
```py
a = [1,2,3]
b = [1,2,3]
a == b               # True
a is b               # False ; ils n'on pas le même emplaceement en mémoire
id(a)                # 4401429248
id(b)                # 4352810304
```
Sauf comme dit plus tôt. Pour les nombres entre -5 et 256 qui sont en mémoire pour optimiser.
```py
a = -5
b = -5
a =  b               # True
a is b               # True
```