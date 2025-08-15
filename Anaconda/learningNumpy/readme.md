# **Numpy**<a href="../../"><img align="right" src="../../assets/Numpy.svg" alt="Numpy" height="64px"></a>
C'est une bibliothèque, un package Python signifie "`Numerical Python`" et un module C optimisé : son cœur est écrit en C pour la performance.  
C'est l'une des principale bibliothèque pour l'informatique scientifique.  
Elle est constituée d'objets, tableaux multidimensionnels (ndarray) & d'une collection de routines pour les tableaux ou les traitements de tableaux.

Elle est notament utilisée pour :
* des opérations algébrique linéaires ;
* la génération de nombres aléatoires ;
* les opérations mathématiques et logique appliquées aux tableaux.

Presque toutes les librairies d'analyse de données font de Numpy un principal bloc de construction, rendant Numpy très importante en Data Science.

Ça spécialité est la manipulation de tableau :
* tableau de première dimension (vecteur) ;
* matrice (2D).

Numpy ne gère que les objets de même type. Et propose une grande variété d'outils pour un accès rapide aux données.  
Les tableaux Numpy sont plus rapides et gère de plus grandes volumétries de données.

<!--
1️⃣ Types homogènes
Numpy impose que tous les éléments d’un tableau aient le même type (int, float, bool, etc.).
Conséquence : Cela permet des calculs très rapides en mémoire contiguë et vectorisés.
Limitation : Si tu veux stocker des objets hétérogènes (mix de chaînes, nombres, objets), Numpy n’est pas optimal ; il faut utiliser object dtype, mais tu perds les performances.
2️⃣ Outils et accès rapide
Numpy propose :
Accès par index, slicing, masking, fancy indexing
Opérations vectorisées (évite les boucles Python lentes)
Fonctions mathématiques et statistiques optimisées
Conséquence : Les opérations sur tableaux Numpy sont souvent 10 à 100x plus rapides que sur des listes Python classiques.
3️⃣ Rapidité et volumétrie
Majoritèrement :
Les tableaux Numpy utilisent une mémoire contiguë, donc moins de surcharge que les listes/dictionnaires Python.
Optimisés pour des millions de valeurs.
Limitation : Si tu fais des insertions/suppressions fréquentes ou du stockage très hétérogène, une liste ou un dictionnaire peut parfois être plus pratique malgré une vitesse brute moindre.
-->

Numpy est ultra-rapide pour des données homogènes et volumineuses, grâce à la mémoire contiguë et aux opérations vectorisées. Pour des structures hétérogènes ou dynamiques, les collections Python restent plus flexibles.

Numpy manipule les tableaux pour le calcule numérique.

Un vecteur peut être d'une seule ligne et colonne. La matrice en a <!--forcément plusieurs--> au moins 2 colonnes et lignes. Au delà, un tableau nD.
![dimensions](../assets/diagrams/dimension.png)

##
Type / Ca | Lignes (m) | Colonnes (n) | Exemple en Numpy | Commentaire 
--- | ----------------------- | ------------ | ------------------------- | ---
**Matrice classique** | ≥1 | ≥1 | `np.array([[1,2],[3,4]])` | Matrice 2×2 standard
**Matrice ligne**     | 1  | ≥1 | `np.array([[1,2,3]])`| Une seule ligne, vecteur ligne
**Matrice colonne**   | ≥1 | 1  | `np.array([[1],[2],[3]])` | Une seule colonne, vecteur colonne
**Vecteur 1D**        | 1 (dimension implicite) | n | `np.array([1,2,3])` | Pas strictement 2D, mais souvent utilisé comme matrice
**Matrice vide**      | 0  | 0 | `np.array([[]])` | Numpy permet, mais opérations limitées
**Matrice 1×1**       | 1  | 1 | `np.array([[5]])` | Cas minimal, parfois appelé scalaire 2D

🔹 **Règles clés** 
Une matrice doit avoir au moins 1 ligne et 1 colonne.  
Les matrices 1×n ou m×1 sont valides et souvent utilisées.  
Les vecteurs 1D ne sont pas strictement des matrices, mais Numpy les traite facilement avec reshape si nécessaire.

🔹 **Via Numpy**
Une matrice n’a pas besoin d’avoir ≥2 lignes et ≥2 colonnes.
Cas possibles en Numpy :
1 ligne, plusieurs colonnes → vecteur ligne : np.array([[1,2,3]]). 
Plusieurs lignes, 1 colonne → vecteur colonne : np.array([[1],[2],[3]]). 
1×1 → scalaire 2D : np.array([[5]]). 
Vecteur 1D → np.array([1,2,3]) (pas strictement 2D mais souvent utilisé).  
Numpy impose juste que toutes les lignes aient le même nombre de colonnes, sinon il devient un tableau de type object.

🔹 **En informatique scientifique (Scipy, MATLAB, Julia…)**  
Même logique que Numpy :  
Les matrices peuvent être 1×n, m×1 ou 1×1.  
Les fonctions scientifiques et algorithmes linéaires sont conçus pour gérer ces cas particuliers.  
Par exemple, en algèbre linéaire : un vecteur colonne est traité comme une matrice m×1 pour les multiplications matricielles.

✅ En math et en informatique scientifique, une matrice n’a pas besoin d’avoir deux lignes et deux colonnes. La seule exigence est au moins 1 ligne et 1 colonne, et une structure homogène par ligne.
## **Sa hiérarchie**
```py
NumPy (package)
│
├── __init__.py
│    └── Point d’entrée du package NumPy
│
├── core (module principal)
│    ├── ndarray (classe)
│    ├── numeric (fonctions de base : add, subtract, multiply, divide…)
│    ├── multiarray (gestion mémoire, dtype)
│    ├── umath (opérations universelles : sin, cos, exp…)
│    └── shape_base (reshape, ravel, concatenate, stack)
│
├── linalg (module)
│    ├── inv (inverse)
│    ├── det (déterminant)
│    ├── eig (valeurs et vecteurs propres)
│    ├── svd (décomposition en valeurs singulières)
│    └── solve (résolution de systèmes linéaires)
│
├── fft (module)
│    ├── fft (transformation de Fourier)
│    ├── ifft (inverse FFT)
│    └── rfft, irfft, fft2, ifft2 (FFT 1D/2D spécialisées)
│
├── random (module)
│    ├── Generator (objet principal pour la génération de nombres aléatoires)
│    ├── randint, randn, uniform, normal
│    └── choice, shuffle, permutation
│
├── ma (module : masked array)
│    ├── MaskedArray (tableau avec valeurs masquées)
│    └── masked_where, masked_equal, masked_invalid
│
├── polynomial (module)
│    ├── Polynomial (classe de polynômes)
│    └── polyfit, polyval, roots
│
├── testing (module)
│    ├── assert_allclose, assert_equal
│    └── run_module_suite (tests unitaires)
│
├── lib (module interne)
│    └── fonctions utilitaires (ex : stride tricks, array pad)
│
├── compat (module)
│    └── Compatibilité Python 2/3 (historique)
│
└── distutils (module)
     └── Outils de compilation et distribution pour NumPy
```
## **Fonctionnement entre Python et C**
```py
        ┌─────────────────────────┐
        │     Votre code Python   │
        │  (import numpy as np)   │
        └─────────────┬───────────┘
                      │ API Python
        ┌─────────────▼───────────┐
        │  NumPy (package Python) │
        │  __init__.py            │
        │  numpy.core, numpy.fft… │
        └─────────────┬───────────┘
                      │ Liaison CPython
        ┌─────────────▼───────────┐
        │  Modules C optimisés    │
        │  (BLAS, LAPACK, etc.)   │
        └─────────────┬───────────┘
                      │ Appels système
        ┌─────────────▼───────────┐
        │   CPU / Mémoire         │
        │  (Vecteurs, SIMD)       │
        └─────────────────────────┘
```
## **Tableau comparatif des notions bibliothèque, package, module, framework, avec exemples**
Terme | Définition courte | Structure technique | Exemple Python | Autres exemples
---|---|---|---|---
**Bibliothèque** | Ensemble de fonctions, classes et outils réutilisables pour résoudre des problèmes spécifiques | Peut être un ou plusieurs *packages* ou modules | NumPy, Pandas | OpenCV, Matplotlib
**Package** | Répertoire Python contenant un `__init__.py` et d'autres modules/fichiers| Arborescence avec sous-modules | `numpy` | `scipy`, `requests`
**Module** | Fichier unique `.py` (ou compilé `.pyd/.so`) contenant du code Python | Contient fonctions, classes, variables | `math`, `numpy.linalg` | `os`, `json`
**Framework** | Ensemble structuré de bibliothèques et règles pour construire une application complète | Fournit une architecture et un cycle de vie | Django (web) | TensorFlow, Flask, PyTorch
## **Parangon de bibliothèque, package, module et framework**
```py
                 ┌──────────────────────────────┐
                 │   FRAMEWORK                  │
                 │  (Architecture complète)     │
                 │  Ex: Django, TensorFlow      │
                 └──────────────┬───────────────┘
                                │
                 ┌──────────────▼───────────────┐
                 │   BIBLIOTHÈQUE               │
                 │  (Outils réutilisables)      │
                 │  Ex: NumPy, Pandas           │
                 └──────────────┬───────────────┘
                                │
                 ┌──────────────▼───────────────┐
                 │   PACKAGE                    │
                 │  (Répertoire + __init__.py)  │
                 └──────────────┬───────────────┘
                                │
                 ┌──────────────▼───────────────┐
                 │   MODULE                     │
                 │  (Fichier .py unique)        │
                 └──────────────────────────────┘
```
* Un framework peut contenir plusieurs bibliothèques.
* Elle peut contenir un ou plusieurs packages.
* Un package regroupe un ou plusieurs modules.
* Un module est le niveau le plus bas : un seul fichier de code.

<!--🏢 Immeuble = Framework
* Contient plusieurs bâtiments ou ailes (bibliothèques).
* Fournit la structure complète (plans, règles, gestion).
* Exemple : Django (immeuble entier avec tout pour faire un site).

🏠 Bâtiment = Bibliothèque
* Regroupe plusieurs appartements (packages).
* Fournit un ensemble cohérent d’outils.
* Exemple : NumPy (bâtiment dédié au calcul numérique).

🚪 Appartement = Package
* Regroupe plusieurs pièces (modules) dans un même espace.
* Exemple : numpy (appartement avec pièces core, linalg, random…).

🛋 Pièce = Module
* Un seul espace fonctionnel.
* Exemple : numpy.linalg (pièce dédiée à l’algèbre linéaire).-->