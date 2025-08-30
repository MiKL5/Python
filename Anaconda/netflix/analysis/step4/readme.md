# Analyse des Données Netflix<a href="../../"><img align="right" src="../../../../assets/Jupyter.svg" alt="Jupyter" height="64px"><img align="left" src="https://upload.wikimedia.org/wikipedia/commons/f/ff/Netflix-new-icon.png" alt="netflix" height="36px"></a>
Analyse d'un jeu de données Netflix afin d'explorer la nature des productions ajoutées au catalogue au fil des années, selon différents critères, et de visualiser ces tendances.
## Description
- Nettoyage approfondi des données : suppression des valeurs manquantes sur des colonnes clés (pays, dates, durées...), conversion des types, suppression des doublons.
- Analyse descriptive avec distributions des catégories, types de production, et notes.
- Calcul et visualisation des pourcentages de types de production (films, séries, etc.) ajoutés chaque année.
- Visualisations avec matplotlib et seaborn : diagrammes en barres, diagrammes circulaires, graphiques empilés avec annotations des pourcentages.
## Fonctionnalités principales
- Nettoyage et préparation des données brutes.
- Calcul des distributions relatives par années et types.
- Génération automatique de graphiques clairs et détaillés.
- Mise en évidence par couleur et annotation des proportions dans les diagrammes empilés.
## Comment utiliser
1. Assurez-vous que le fichier `netflix.csv` est présent dans le même répertoire que le script.
2. Installer les dépendances requises (pandas, matplotlib, seaborn).
3. Exécuter le script `netflix.py` dans un environnement Jupyter Notebook ou un interpréteur Python.
4. Observer les résultats graphiques générés automatiquement.
```py
pip install pandas matplotlib seaborn
jupyter notebook netflix.py
```
## Technologies utilisées
- Python 3.x
- Pandas : manipulation et nettoyage des données
- Matplotlib & Seaborn : visualisation de données