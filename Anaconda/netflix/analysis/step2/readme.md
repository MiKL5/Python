# Analyse des Données <a href="#"><img align="center" src="https://upload.wikimedia.org/wikipedia/commons/0/0c/Netflix_2015_N_logo.svg?uselang=fr" alt="netflix" height="36px"></a>etflix<a href="../../"><img align="right" src="../../../../assets/logo/Jupyter.svg" alt="Jupyter" height="64px"></a>
Analyse d'un jeu de données de Netflix pour visualiser la répartition des types de programmes (films et séries).
## Description
Les bibliothèques `pandas`, `seaborn`, et `matplotlib` servent à l'analyse et la visualisation des données.
### Visualisations
1. **Graphique en barres** :
   - Utilise `sns.catplot` pour montrer le nombre de films et de séries.
   - Une palette de couleurs personnalisée (bleu et orange) est utilisée.
2. **Diagramme circulaire** :
   - Montre la répartition en pourcentage des types de programmes.
   - Utilise `plot.pie` pour afficher les pourcentages, avec des options pour les ombres, les couleurs, et un titre.
### Calculs
- **Fréquences relatives** :
  - Calcule les fréquences relatives des types de programmes avec `value_counts(normalize=True)`. 
  - Convertit ces fréquences en pourcentages.