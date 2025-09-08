#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy             as np
import pandas            as pd
import matplotlib.pyplot as plt
import seaborn           as sns
import plotly.express    as px


# In[2]:


data_universities = pd.read_excel('data_universite.xlsx')
data_universities


# In[3]:


data_universities.shape


# In[4]:


data_universities.columns


# In[5]:


data_universities.columns.to_list()


# In[ ]:





# In[6]:


# Avec un print classique, c'est dûr à lire ; utiliser value
print(data_universities.columns.values)


# In[ ]:





# In[7]:


# Le titre des colonnes, leur type (toutes les colonnes)
data_universities.info(max_cols = len(data_universities))


# In[ ]:





# Certaines colonnes manquent de valeurs.

# S'il manque plus de 20 % des valeurs, la représentation des données est trop biaisée.

# 👉 Utiliser `len` et multiplier par 100.

# In[8]:


# Quelles sont les colonnes dont il manque plus de 20 %.
colonnes_nan = data_universities.isnull().sum()/len(data_universities)*100
colonnes_nan


# 👉 Une représentation graphique des valeurs manquantes est nécessaire.

# In[9]:


plt.figure(figsize = (12,10))
nan_pourcent = colonnes_nan[colonnes_nan>=20].sort_values(ascending = False).plot.bar(title = "% de NAN")


# In[10]:


# Copier le dataset
data = data_universities.copy()
data.head()


# In[11]:


# Convertir en liste
liste_colonnes_nan = colonnes_nan[colonnes_nan>=20].index.to_list()
liste_colonnes_nan


# In[12]:


# Supprimer ces colonnes du dataset
data.drop(liste_colonnes_nan, axis = 1, inplace = True)
data.info(max_cols=len(data))


# In[ ]:





# Il reste 127 colonnes.

# La question est : "Quels sont les critères poussant un étudiant à préférer une université ?"
# 
# Donc, 8 colonnes m'intéressent.  
# Elles seront stockées dans une liste ('university preference criteria') :
# * Name ;
# * Applicants total (candidats) ;
# * Adminissions total ;
# * Enrolled total (inscrits) ;
# * Total price for in-state students living on campus 2013-14 ;
# * Total price for out-of-state students living on campus 2013-14 (étudiants étrangés) ;
# * Control of institution (école privée ou publique) ;
# * Total enrollment.

# In[13]:


university_preference_criteria = ['Name', 'Applicants total', 'Admissions total', 'Enrolled total',
                                  'Total price for in-state students living on campus 2013-14',
                                 'Total price for out-of-state students living on campus 2013-14',
                                 'Control of institution', 'Total  enrollment']

preference = data[university_preference_criteria]
preference.head()


# In[14]:


# Y a-t-il des valeurs manquantes ?
na_values = preference.isnull().sum()
na_values


# Ici, il n'y a pas d'autre possibilité que de supprimer les lignes.  
# Le dataset, ne contient pas les données des années précédentes.  
# Par conséquent, il est impossible de calculer une moyenne.

# In[15]:


# Suppression
preference = preference.dropna(subset=['Applicants total', 'Admissions total', 'Enrolled total',
                                       'Total price for in-state students living on campus 2013-14',
                                       'Total price for out-of-state students living on campus 2013-14',
                                       'Total  enrollment'])

na_values = preference.isnull().sum()
na_values


# In[16]:


# Combien de lignes reste t-il ?
preference.shape


# In[17]:


# Avoir un point de vue global de la populationabs
preference.describe()


# 1326 universités  
# 6562 candidatures moyennes par université
# 8887 certaines universités ont un très grand nombre de candidatures  
# D'autres très peu  
# Le dernier quartile, montre qu'une université à 72676 candidatures pour 2013-14

# In[18]:


# Quelle école n'a que 4 candidature ?
preference[['Name', 'Applicants total']].sort_values('Applicants total').head(10)


# Celon "datausa.io", c'est habituel.

# _Les virgules, tirets, barres de fraction, etc, peuvent être problématiques._  
# _Il faut les replacer par "`_`"._
# _Ou l'appeler entre crochets et guillemmets._

# In[19]:


liste = []
mot   = "Total price for in-state students living on campus 2013-14".split()
size  = int(len(mot))
for i in range(size):
    if i < size -1:
        liste.append(mot[i] + '_')
    else:
        liste.append(mot[i])

liste


# In[20]:


intitule = ''.join(liste)
intitule


# C'est une perte de temps, une fonction est plus rapide et plus efficace.

# In[21]:


def remove_space(column_name):
    word_list = []
    words = column_name.split()
    size = len(words)
    for i in range(size):
        if i < size - 1:
            word_list.append(words[i] + '_')
        else:
            word_list.append(words[i])

    new_column_name = ''.join(word_list)
    return new_column_name


# In[22]:


remove_space("Total price for out-of-state students living on campus 2013-14")


# In[23]:


new_title   = []
cols        = data.columns
for col in cols:
    new_col = remove_space(col)
    new_title.append(new_col)

new_title


# In[24]:


data.columns = new_title

data.head()


# Les 127 colonnes ont un intitulé uniforme.
