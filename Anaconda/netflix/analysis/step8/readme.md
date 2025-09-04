## **Productions <a href="#"><img align="center" src="https://upload.wikimedia.org/wikipedia/commons/0/0c/Netflix_2015_N_logo.svg?uselang=fr" alt="netflix" height="36px"></a>etflix par pays selon le type**<a href="../"><img align="right" src="../../../../assets/logo/Jupyter.svg" alt="Jupyter" height="64px"></a></h1>
## **🎯 Objectif**
Identifier et comparer la répartition des productions audiovisuelles (films et émissions) dans les 10 pays les plus producteurs, afin de mettre en évidence les spécificités nationales.
## **🛠️ Étapes du traitement**
### 1. Sélection des pays les plus producteurs
Filtrage des données pour conserver uniquement les 10 pays leaders en volume de productions :
🇺🇸 United States
🇮🇳 India
🇬🇧 United Kingdom
🇨🇦 Canada
🇫🇷 France
🇯🇵 Japan
🇪🇸 Spain
🇰🇷 South Korea
🇩🇪 Germany
🇲🇽 Mexico
```py
data_producteurs = data[(data['country']=="United States")|(data['country']=="India")
                       |(data['country']=="United Kingdom")|(data['country']=="Canada")
                       |(data['country']=="France")|(data['country']=="Japan")
                       |(data['country']=="Spain")|(data['country']=="South Korea")
                       |(data['country']=="Germany")|(data['country']=="Mexico")]
```
### 2. Analyse quantitative
* Nombre total de productions issues de ces 10 pays : 5 269.
* Chaque ligne correspond à une production classée par pays et par type (Movie ou TV Show).
### 3. Visualisation comparative
Création d’un graphique en barres avec Seaborn permettant de comparer, pour chaque pays, la proportion de films et d’émissions.
## **📈 Résultats**
, 🇬🇧 Royaume-Uni, 🇯🇵 Japon et 🇰🇷 Corée du Sud se distinguent par une production plus élevée d’émissions TV que de films.
, 🇺🇸 États-Unis et 🇮🇳 Inde dominent en volume global, avec une forte proportion de films.
, Les autres pays présentent une répartition plus équilibrée.
## **🤝 Compétences démontrées**
* Nettoyage et filtrage des données avec pandas.
* Sélection conditionnelle efficace sur des critères multiples (OR).
* Analyse descriptive appliquée à des sous-ensembles ciblés.
* Visualisation comparative avec Seaborn et gestion des catégories (hue).
* Production de résultats clairs et directement interprétables pour un public non technique.
---
## **🚀 Perspectives**
* Étendre l’analyse à d’autres pays émergents (ex. Brésil, Italie, Turquie).
* Normaliser les libellés pour éviter les doublons (ex. "USA" vs "United States").
* Calculer des ratios films/émissions par pays pour une comparaison plus fine.
* Étudier l’évolution chronologique (tendances par décennie).
* Développer des visualisations interactives (plotly, dash, streamlit).

👉 Ce travail illustre la capacité à isoler des sous-ensembles pertinents, comparer des catégories et communiquer les résultats de manière professionnelle, compétences attendues d’un Data Scientist / Analyst.