<h1>🎓 Études des Universités Américaines<a href="../"><img align="right" src="../../../assets/logo/Jupyter.svg" alt="Jupyter" height="64px"></a></h1>
<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue) ![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellow) ![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-green) ![Plotly](https://img.shields.io/badge/Plotly-Interactive-orange) <!--![Status](https://img.shields.io/badge/Status-In_Progress-red)-->
</div>

---
## **📌 Contexte**
Ce projet analyse un dataset regroupant les universités américaines afin d’identifier les critères influençant le choix des étudiants.  
L’objectif est double :  
- **Nettoyage et préparation des données** (suppression des colonnes/lignes incomplètes, harmonisation des intitulés).  
- **Exploration des facteurs déterminants** dans la sélection d’une université (admissions, frais de scolarité, type d’institution, etc.).
---
## **🛠️ Technologies utilisées**
- **Python 3.x**  
- **Bibliothèques principales** :  
  - `numpy` → calcul numérique  
  - `pandas` → manipulation de données tabulaires  
  - `matplotlib` / `seaborn` → visualisation statique  
  - `plotly.express` → visualisation interactive  
---
## **📂 Données**
- Source : `data_universite.xlsx` de "Kaggle"  
- **Taille initiale** : plus de 130 colonnes  
- **Nettoyage effectué** :  
  - Suppression des colonnes avec +20 % de valeurs manquantes  
  - Uniformisation des noms de colonnes (remplacement espaces par `_`)  
  - travail avec **8 variables exploitables**  
---
## **🎯 Objectif analytique**
### Question clé
👉 _Quels critères poussent un étudiant à choisir une université ?_
### Variables retenues
* `Name` (nom de l’université)
* `Applicants_total` (nombre de candidatures)
* `Admissions_total` (admis)
* `Enrolled_total` (inscrits)
* `Total_price_in_state_on_campus` (frais du pays 2013-14)
* `Total_price_out_of_state_on_campus` (frais pour les étudiants étrangés 2013-14)
* `Control_of_institution` (école public/privé)
* `Total_enrollment` (effectif total)
## 📊 Résultats intermédiaires
* **1326 universités** après nettoyage.
* En moyenne **6562 candidatures par université**, avec des extrêmes allant de 4 à plus de 70 000 candidatures.
* Variabilité forte entre universités selon leur réputation, taille et coût.
---
## **📑 Étapes du projet**
1. **Chargement et inspection** des données.
2. **Nettoyage avancé** :
   - gestion des `NaN`
   - standardisation des colonnes
3. **Sélection des critères pertinents**.
4. **Exploration statistique et visuelle** :
   - distribution des candidatures
   - impact du coût sur les inscriptions
   - comparaison public vs privé
5. **Préparation à la modélisation prédictive** (travail futur).
<!-- ---
## 🚀 Perspectives
- Étendre l’analyse à plusieurs années pour observer les tendances.  
- Construire un modèle de **prédiction du nombre d’inscrits** selon les critères retenus.  
- Étudier l’impact des politiques publiques et des frais de scolarité.  
- Automatiser le pipeline de nettoyage et de visualisation.
---
## 📌 Auteur
👤 **Mickael Gaillard**  
- MBA Big Data & Master IA (en cours)  
- Compétences : Data Science, Machine Learning, Big Data, Python, SQL, IA appliquée  
- Objectif : mettre la donnée au service de l’intelligence artificielle et de la prise de décision -->