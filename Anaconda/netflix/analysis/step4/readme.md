# Analyse exploratoir du catalogue de <a href="#"><img align="center" src="https://upload.wikimedia.org/wikipedia/commons/0/0c/Netflix_2015_N_logo.svg?uselang=fr" alt="netflix" height="36px"></a>etflix<a href="../../"><img align="right" src="../../../../assets/logo/Jupyter.svg" alt="Jupyter" height="64px"></a>
## 🎯 Objectif
> L’objectif de ce projet est d’explorer et de visualiser les données du catalogue Netflix afin de :
> - Comprendre la répartition des programmes par type (Films vs Séries).
> - Analyser l’évolution des acquisitions au fil des années.
> - Identifier les tendances de classification (`rating`) et leur impact sur la production.
---
## 🛠️ Outils et technologies
- **Python 3**
- **Bibliothèques principales** :
  - `pandas` → manipulation et préparation des données.
  - `numpy` → calculs numériques.
  - `matplotlib` & `seaborn` → visualisations descriptives et analytiques.
---
## 🔄 Étapes d’analyse (extrait)
### 1. Répartition des catégories de classification
- Analyse de la variable **`rating`** pour comprendre les restrictions d’âge et les usages.
- Visualisations :
  - Histogrammes (`matplotlib`).
  - Catplots (`seaborn`).
  - Diagrammes circulaires.
### 2. Analyse par type de programme
- Comparaison entre **Films** et **Séries** :
  - Distribution en volume.
  - Répartition en pourcentage.
- Visualisations :
  - Graphiques en barres (`seaborn`).
  - Diagrammes circulaires avec mise en évidence (`explode`).
### 3. Productions ajoutées par année
- Histogramme simple des ajouts annuels.
- Identification des périodes de forte croissance.
### 4. Répartition temporelle par type
- Étude de la proportion **Films vs Séries** par année.
- Calculs normalisés (%).
- Visualisation via :
  - Countplots segmentés par type.
  - Graphiques en barres empilées annotées (%).
## 📈 Résultats principaux
- Les **Films** constituent la majorité du catalogue.
- Les **Séries** occupent une place plus forte dans les contenus destinés à la jeunesse.
- Forte croissance des acquisitions après **2011**, avec un pic entre **2018 et 2020**.
- Diversification progressive et montée en puissance des séries au cours de la décennie.
## 🤝 Compétences démontrées
- Nettoyage et préparation de données réelles.
- Analyse descriptive et agrégation par catégories et périodes.
- Visualisations claires et adaptées (comparatif, temporel, proportionnel).
- **Data storytelling** : transformer des données brutes en insights lisibles pour décideurs et non-techniciens.
<!-- ## 🚀 Perspectives
- Étendre l’analyse aux **genres** et aux **pays de production**.
- Ajouter des visualisations interactives (`plotly`, `dash`).
- Développer un modèle prédictif pour anticiper les tendances futures de production. -->