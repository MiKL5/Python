# Analyse des productions <a href="#"><img align="center" src="https://upload.wikimedia.org/wikipedia/commons/0/0c/Netflix_2015_N_logo.svg?uselang=fr" alt="netflix" height="36px"></a>etflix ajoutées par année<a href="../../"><img align="right" src="../../../../assets/logo/Jupyter.svg" alt="Jupyter" height="64px"></a>
Ce projet propose une **analyse exploratoire des données (EDA)** issues d’un dataset Netflix.  
L’accent est mis sur la **visualisation et l’interprétation des tendances** liées aux productions présentes sur la plateforme.
---
## 🎯 Objectifs
- Étudier l’évolution des contenus ajoutés sur Netflix au fil des années.  
- Comparer la répartition des films et séries.  
- Identifier les pays les plus contributeurs.  
- Mettre en évidence les réalisateurs et acteurs les plus fréquents.  
- Explorer la distribution par genres et par durée.  
---
## 🛠️ Technologies utilisées
- **Python 3.x**
- Bibliothèques :
  - `pandas` : manipulation et nettoyage des données  
  - `matplotlib` & `seaborn` : visualisations statistiques  
  - `numpy` : opérations numériques  
## 📂 Organisation du code (à partir de la ligne 282)
- **Ajout de productions par année**  
  Histogrammes de la variable `year_added`.
- **Répartition Films vs Séries**  
  Diagrammes pour comparer le nombre de films et de séries dans le catalogue.
- **Analyse par pays d’origine**  
  Mise en avant des pays les plus représentés.
- **Réalisateurs et acteurs les plus fréquents**  
  Classements et visualisations des personnalités les plus présentes.
- **Analyse par genres et catégories**  
  Distribution des genres dominants.
- **Durée des films et séries**  
  Étude des longueurs moyennes et distribution des durées.
## 🚀 Exécution

1. Cloner le dépôt ou récupérer le fichier `netflix.py`.  
2. Installer les dépendances :  
   ```bash
   pip install pandas matplotlib seaborn numpy
   ```
3. Lancer le script :  
   ```bash
   python netflix.py
   ```
   ou exécuter dans un notebook Jupyter pour voir les graphiques.
## 📊 Résultats attendus
- Visualisations claires et lisibles pour interpréter les tendances.  
- Identification des **pics d’ajout de contenu** par année.  
- Mise en évidence de la **domination des films** par rapport aux séries.  
- Constat des **pays majeurs producteurs de contenu Netflix**.  
<!-- ## 📌 Améliorations possibles
- Automatiser les visualisations via une interface interactive (Dash, Streamlit).  
- Étendre l’analyse aux tendances temporelles (séries ajoutées par mois/semestre).  
- Explorer les corrélations entre durée, genre et popularité.  
- Ajouter un modèle de prédiction sur les futures tendances de production.   -->