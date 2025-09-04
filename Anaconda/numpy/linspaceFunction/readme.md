# **La fonction "`linspace()`"**<a href="../../"><img align="right" src="../../../assets/logo/numpy_2020.svg" alt="Numpy" height="64px"></a>
Si vous avez déjà eu besoin de créer une série de nombres régulièrement espacés (par exemple, pour tracer un graphique ou faire des calculs), cette fonction est faite pour vous.

## **À quoi ça sert ?**
Imaginez que vous voulez créer une liste de nombres entre 0 et 10, mais pas n’importe comment : vous voulez que ces nombres soient équidistants, c’est-à-dire qu’il y ait le même écart entre chacun d’eux. Par exemple, si vous voulez 5 nombres entre 0 et 10, vous obtiendrez : 0, 2.5, 5, 7.5, 10.
C’est exactement ce que fait linspace : elle génère une séquence de nombres régulièrement espacés entre une valeur de départ et une valeur de fin.

## **Comment ça marche ?**
La syntaxe de base est très simple :
```py
numpy.linspace(start, stop, num=50, endpoint=True)
```
start : Le premier nombre de la séquence (par exemple, 0).
stop : Le dernier nombre de la séquence (par exemple, 10).
num : Le nombre total de valeurs que vous voulez dans la séquence (par défaut, 50).
endpoint : Si True (par défaut), la valeur stop est incluse dans la séquence. Si False, elle ne l’est pas.
### **Exemple Concret**
Prenons un exemple simple. Supposons que vous voulez créer 5 nombres entre 0 et 10 :
```py
import numpy as np


# Générer 5 nombres entre 0 et 10
valeurs = np.linspace(0, 10, num=5)
print(valeurs)

[ 0.   2.5  5.   7.5 10. ]
```
On commence à 0.
On finit à 10.
On a 5 valeurs en tout, régulièrement espacées.

### **_Petit Bonus_ : Connaître l’Espacement**
Si vous voulez aussi savoir quel est l’écart entre chaque nombre, vous pouvez ajouter retstep=True :
```py
valeurs, espacement = np.linspace(0, 10, num=5, retstep=True)
print("Valeurs :", valeurs)
print("Espacement :", espacement)

Valeurs : [ 0.   2.5  5.   7.5 10. ]
Espacement : 2.5
```
Ici, l’espacement entre chaque nombre est de 2.5.
## **Pourquo est-ce utile ?**
Graphiques : Si vous tracez une courbe, vous pouvez utiliser linspace pour créer les valeurs de l’axe des abscisses (axe x).
Simulations : Pour créer des intervalles de temps ou d’espace régulièrement espacés.
Calculs : Pour générer des plages de valeurs dans des calculs mathématiques.
## **_À Retenir_**
`linspace` génère une séquence de nombres équidistants entre une valeur de départ et une valeur de fin.
Par défaut, elle inclut la valeur de fin (endpoint=True).
Vous pouvez choisir le nombre de valeurs avec num.
Si vous voulez connaître l’espacement entre les valeurs, utilisez retstep=True.
### Exercice Pratique
Essayez de créer une séquence de 10 nombres entre 1 et 20, puis affichez-la. Que remarquez-vous ?
```py
import numpy as np


# À vous de jouer !
valeurs = np.linspace(1, 20, num=10)
print(valeurs)
```
___
"`linspace`" est une contraction de l'anglais "linear spacing", ce qui signifie "espacement linéaire" en français.  
"Linear" fait référence à une progression régulière et constante, comme une ligne droite.  
"Spacing" signifie "espacement" ou "intervalle".  

Ainsi, "`linspace`" signifie littéralement "espacement linéaire", décrivant parfaitement son rôle : créer une séquence de nombres avec un espacement régulier et constant entre eux.