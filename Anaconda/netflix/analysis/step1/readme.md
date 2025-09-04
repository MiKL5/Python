# Analyse Descriptive des catégories de <a href="#"><img align="center" src="https://upload.wikimedia.org/wikipedia/commons/0/0c/Netflix_2015_N_logo.svg?uselang=fr" alt="netflix" height="36px"></a>etflix<a href="../../"><img align="right" src="../../../../assets/logo/Jupyter.svg" alt="Jupyter" height="64px"></a>
## Description
Ce fichier décrit l'analyse de la colonne `rating` du jeu de données Netflix. Les catégories de notation indiquent l'audience cible pour chaque contenu.
## Catégories de Notation
Voici les différentes catégories de notation et leur signification :
- **`g`** et **`tv-g`** : Contenu adapté à tous les âges.
- **`tv-y`** : Contenu adapté aux enfants de 2 à 6 ans.
- **`tv-y7`** : Contenu recommandé dès 7 ans.
- **`tv-y7-fv`** : Contenu recommandé dès 7 ans avec une nuance supplémentaire.
- **`pg`** : Certains passages ne sont pas adaptés aux enfants.
- **`pg-13`** : Interdit aux moins de 12 ans.
- **`tv-14`** : Contient des passages inadaptés aux moins de 14 ans.
- **`tv-pg`** : Inadapté aux jeunes enfants.
- **`R`** : Les moins de 18 ans doivent être accompagnés d'un adulte.
- **`tv_ma`** : Destiné à un public adulte.
- **`nc-17`** : Réservé à un public adulte uniquement.
- **`nr`** et **`ur`** : Non évalué.
## Visualisations
### Histogramme des Fréquences en Pourcentage
Un histogramme a été créé pour montrer la distribution des catégories de notation en pourcentage.
```python
plt.figure(figsize=(12,6))
data['rating'].value_counts(normalize=True).plot.bar()
plt.title('Distribution des catégories')
plt.xlabel('Catégories')
plt.ylabel('Fréquence en pourcentage')
```
### Histogramme avec Seaborn
Un histogramme utilisant Seaborn a été généré pour afficher le nombre d'occurrences de chaque catégorie.
```python
sns.catplot(x='rating', data=data, kind='count')
fig = plt.gcf()
fig.set_size_inches(12,6)
plt.title('Distribution des catégories')
```
### Diagramme Circulaire
Un diagramme circulaire a été créé pour montrer la répartition des catégories sous forme de camembert.
```python
data['rating'].value_counts().plot.pie(autopct='%1.1f%%', shadow=False, figsize=(12,12))
```