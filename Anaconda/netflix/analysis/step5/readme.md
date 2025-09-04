# Tendance des acquisitions de <a href="#"><img align="center" src="https://upload.wikimedia.org/wikipedia/commons/0/0c/Netflix_2015_N_logo.svg?uselang=fr" alt="netflix" height="36"></a>etflix<a href="../"><img align="right" src="../../../../assets/logo/Jupyter.svg" alt="Jupyter" height="64px"></a></h1>
## 🎯 Objectif
> Étudier l’évolution du catalogue Netflix entre 2011 et 2021 en mettant en évidence :
> - Les tendances de production (films vs séries).
> - La répartition par catégories de contenu (`rating`).
> - Les dynamiques temporelles d’acquisition de contenu.
## 🛠️ Outils et technologies
- **Python 3**
- **Bibliothèques utilisées** :
  - `pandas` → manipulation et agrégation des données.
  - `numpy` → opérations numériques.
  - `matplotlib` et `seaborn` → visualisations descriptives.
  - `plotly.express` → graphiques interactifs.
___
## 🔄 Étapes d’analyse (extrait du projet)
### 1. Analyse des classifications (`rating`)
- Étude de la distribution des catégories de censure et d’âge.
- Visualisation via :
  - Histogrammes (`matplotlib`).
  - Diagrammes circulaires (`pandas.plot.pie`).
  - Catplots (`seaborn`).
### 2. Répartition par type de production
- Films vs Séries TV.
- Comparaison en fréquence et en pourcentage.
- Visualisations :
  - Graphiques en barres.
  - Diagrammes circulaires avec surlignage (`explode`).
### 3. Dynamique temporelle
- Nombre de contenus ajoutés par année.
- Croissance significative à partir de 2011.
- Visualisation :
  - Histogrammes par année.
  - Countplots segmentés par type (`seaborn`).
### 4. Répartition annuelle par type (%)
- Transformation en **tableau croisé dynamique** (`pivot`).
- Graphiques en barres empilées avec annotations de pourcentages.
- Mise en avant de l’évolution des parts de marché Films vs Séries.
### 5. Tendance des acquisitions 2011–2021
- Agrégation des données par année et par type.
- Visualisation avec **`plotly.express.line`** pour un rendu interactif.
___
## 📈 Résultats clés
- **Films** dominent largement le catalogue global.
- **Séries** sont plus présentes dans les contenus jeunesse.
- Forte **croissance des acquisitions à partir de 2011**, avec un pic 2018–2020.
- Diversification progressive des types de productions et montée en puissance des séries.
---
## 🤝 Compétences démontrées
- Préparation et nettoyage des données.
- Analyses descriptives avancées.
- Visualisations statistiques et interactives.
- Storytelling orienté données (transformer des données brutes en insights exploitables).
---
## 🚀 Perspectives
- Étendre l’analyse par **pays de production**.
- Croiser avec d’autres sources (IMDB, Rotten Tomatoes).
- Construire un **modèle prédictif** sur les acquisitions futures.
- Explorer les **corrélations entre genres, ratings et tendances temporelles**.