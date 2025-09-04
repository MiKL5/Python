# **Création de vecteur**<a href="../"><img align="right" src="../../../assets/logo/Numpy.svg" alt="Numpy" height="64px"></a>
## 1️⃣ **À partir d’une liste existante**
```py
import numpy as np


lst = [1, 2, 3, 4, 5]
```
# Vecteur 1D classique
```py
a = np.array(lst)
```
# Vecteur colonne (2D)
```py
b = np.array(lst).reshape(-1, 1)

# Vecteur ligne (2D)
c = np.array(lst).reshape(1, -1)
```
## 2️⃣ **Avec des fonctions de création directe**
Fonction | Exemple | Description
---|---|---
np.zeros(n) | np.zeros(5) → [0,0,0,0,0] | Tableau rempli de 0
np.ones(n) | np.ones(5) → [1,1,1,1,1] | Tableau rempli de 1
np.full(n, valeur) | np.full(5, 7) → [7,7,7,7,7] | Tableau rempli d’une constante
np.arange(start, stop, step) | np.arange(1,6) → [1,2,3,4,5] | Tableau d’entiers espacés
np.linspace(start, stop, n) | np.linspace(0,1,5) → [0,0.25,0.5,0.75,1] | Tableau de valeurs espacées uniformément
## 3️⃣ **À partir de listes imbriquées**
Pour créer une matrice 2D ou 3D :
```py
lst2D = [[1,2,3],[4,5,6]]
mat = np.array(lst2D)
```
## 4️⃣ **Avec des fonctions aléatoires**
```py
np.random.rand(5)          # 5 valeurs aléatoires uniformes [0,1)
np.random.randn(5)         # 5 valeurs aléatoires normales
np.random.randint(0,10,5)  # 5 entiers aléatoires entre 0 et 9
```
### 🔹 ***Points clés à retenir***
* *np.array() → transformation directe d’une liste ou liste de listes.
* Fonctions comme zeros, ones, full, arange, linspace → création sans liste initiale.
* Reshape → transforme un vecteur en matrice ligne ou colonne.
* Random → génère des vecteurs aléatoires pour simulations ou ML.

#### 💡 Il y a au moins 6-7 façons différentes de créer un vecteur ou tableau avec NumPy, selon que tu pars d’une liste ou que tu veux initialiser directement ton tableau.

Méthode / Fonction | Exemple | Forme | Usage / Description
---|---|---|---
np.array() | np.array([1,2,3]) | 1D ou 2D | Transformation directe d’une liste Python en tableau NumPy
np.array().reshape() | np.array([1,2,3]).reshape(-1,1) | 2D (colonne) | Convertir un vecteur 1D en vecteur colonne ou ligne
np.zeros(n) | np.zeros(5) | 1D | Tableau rempli de zéros, utile pour initialisation
np.ones(n) | np.ones(5) | 1D | Tableau rempli de uns, initialisation
np.full(n, valeur) | np.full(5, 7) | 1D | Tableau rempli d’une constante
np.arange(start, stop, step) | np.arange(1,6) | 1D | Tableau d’entiers espacés, comme range mais en tableau NumPy
np.linspace(start, stop, n) | np.linspace(0,1,5) | 1D | Tableau avec n valeurs uniformément espacées entre start et stop
np.random.rand(n) | np.random.rand(5) | 1D | Tableau de nombres aléatoires uniformes [0,1), utile pour simulations ou ML
np.random.randn(n) | np.random.randn(5) | 1D | Tableau de nombres aléatoires selon loi normale
np.random.randint(low, high, n) | np.random.randint(0,10,5) | 1D | Tableau d’entiers aléatoires, pratique pour ML
np.array(list_of_lists) | np.array([[1,2,3],[4,5,6]]) | 2D | Création de matrices ou tableaux multidimensionnels
### 🔹 **Notes pratiques**
Reshape (-1,1) ou (1,-1) → vecteur colonne ou ligne pour ML et opérations matricielles.
zeros, ones, full, arange, linspace → ne nécessitent pas de liste initiale.
random → utile pour tests, simulations, apprentissage supervisé/non-supervisé.
Toutes ces méthodes retournent numpy.ndarray, qui supporte les opérations vectorielles ultra rapides.