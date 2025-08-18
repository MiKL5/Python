# **La fonction "`linspace()`"**<a href="../../"><img align="right" src="../../../assets/numpy_2020.svg" alt="Numpy" height="64px"></a>
Les fonctions numpy.linspace et numpy.arange sont toutes deux utilisées pour créer des séquences de nombres, mais elles fonctionnent différemment et sont adaptées à des besoins distincts. Voici leurs différences principales :
## **numpy.linspace**
Objectif : Génère un nombre fixe de valeurs équidistantes entre une valeur de départ (start) et une valeur de fin (stop).
Utilisation : Idéal lorsque vous savez combien de points vous voulez dans un intervalle donné.
```py
 Copiernp.linspace(0, 10, num=5)  # Résultat : [0., 2.5, 5., 7.5, 10.]
```
## **numpy.arange**
Objectif : Génère des valeurs dans un intervalle donné avec un pas fixe entre chaque valeur.
Utilisation : Idéal lorsque vous savez quel est l'espacement (le pas) entre les valeurs.
```py
 Copiernp.arange(0, 10, 2)  # Résultat : [0, 2, 4, 6, 8]
```

## Résumé
Fonction|Critère de génération|Inclut la valeur de fin ?
---|---|:-:
linspace|Nombre fixe de valeurs (num)|Oui (par défaut)
arange|Pas fixe entre les valeurs (step)|Non

> Utilisez :
* `linspace` : un nombre précis de valeurs dans un intervalle,
* `arange` : un espacement précis entre les valeurs.