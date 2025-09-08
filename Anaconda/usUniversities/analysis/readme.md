<h1>🎓 Études des Universités Américaines<a href="../"><img align="right" src="../../../assets/logo/Jupyter.svg" alt="Jupyter" height="64px"></a></h1>
<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue) ![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellow) ![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-green) ![Plotly](https://img.shields.io/badge/Plotly-Interactive-orange) <!--![Status](https://img.shields.io/badge/Status-In_Progress-red)-->
</div>

___
## **📌 Contexte**
Project d’exploration des données universitaires US. Objectif : identifier les facteurs influençant la préférence étudiante. Nettoyage rigoureux et analyses descriptives suivies d’un pré-pipeline pour modélisation.
---
## **🛠️ Technologies utilisées**
- Python 3.8+  
- numpy, pandas  
- matplotlib, seaborn, plotly.express  
- Jupyter / script `.py` exécutable
## **📂 Données**
- Fichier source : `data_universite.xlsx`  
- Nettoyage : suppression des colonnes >20% de valeurs manquantes, standardisation des noms de colonnes (espaces → `_`).  
- Jeu exploitable après nettoyage : **127 colonnes**.  
- Observations finales utilisées pour les analyses principales : **~1326 universités** (après filtrage NA sur variables clés).
## **🎯 Objectif analytique**
Répondre à : *Quels critères poussent un étudiant à préférer une université ?*  
Distinguer volume de candidatures, taux d'admission, coût, contrôle (public/privé) et effectif.
## **🛠️ Méthodologie**
1. Inspection initiale (`.info()`, `.shape`, `isnull().sum()`).  
2. Suppression colonnes fortement incomplètes (>20%).  
3. Standardisation noms de colonnes via fonction `remove_space`.  
4. Sélection variables d’intérêt.  
5. Nettoyage lignes (dropna sur variables critiques).  
6. Analyses descriptives, corrélations, visualisations.  
7. Préparation pour modèle prédictif (features & target).
## **📊 Variables retenues**
- `Name`  
- `Applicants_total`  
- `Admissions_total`  
- `Enrolled_total`  
- `Total_price_for_in_state_students_living_on_campus_2013-14`  
- `Total_price_for_out_of_state_students_living_on_campus_2013-14`  
- `Control_of_institution` (Public / Private not-for-profit)  
- `Total_enrollment`
## **🔑 Résultats clés**
- **1326** universités analysées.  
- Moyenne candidatures par université : **~6562**. Distribution fortement skew.  
- Forte corrélation positive entre `Applicants_total` ↔ `Admissions_total` ↔ `Enrolled_total`.  
- Les universités publiques reçoivent en moyenne **plus** de candidatures que les privées.  
- Le volume de candidatures n’implique pas systématiquement un taux d’inscription élevé.  
- Calcul d’un `Enrollment_rate = Enrolled_total / Admissions_total * 100` pour évaluer conversion admissions→inscriptions.
## **📈 isualisations produites**
- Top20 universités par `Applicants_total` (barplot horizontal).  
- Heatmap de corrélation entre candidatures, admissions, inscrits.  
- Histogrammes des distributions `Applicants_total`, `Admissions_total`, `Enrolled_total`.  
- Scatterplots : `Applicants_total` vs `Admissions_total` (par `Control_of_institution`), `Admissions_total` vs `Enrolled_total`.  
- Histogramme comparatif public vs privé (stacked).
## **⚙️ Exécution et reproduction**
1. Créer un environnement Python puis installer dépendances :
```bash
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate      # Windows
   pip install -r requirements.txt