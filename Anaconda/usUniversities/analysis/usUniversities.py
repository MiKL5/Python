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


# In[6]:


# Avec un print classique, c'est dûr à lire ; utiliser value
print(data_universities.columns.values)


# In[7]:


# Le titre des colonnes, leur type (toutes les colonnes)
data_universities.info(max_cols = len(data_universities))


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

# ## **Quelles sont les 20 universités ayant le plus grand nombre de candidatures**

# In[25]:


top20 = data[['Name', 'Applicants_total']].sort_values('Applicants_total', ascending=False).head(20)
top20


# In[26]:


plt.figure(figsize=(16,10))
sns.barplot(x='Applicants_total', y='Name', data=top20, hue='Name', legend=False)


# In[27]:


plt.figure(figsize=(16,10))
sns.barplot(x='Applicants_total', y='Name', data=top20)
plt.title('Top 20', fontsize=16)
plt.xlabel('Candidatures')
plt.ylabel('Universités')


# Les universités de 'Los Angeles', 'Berkeley' et 'San Diego' sont les 3 premières suivies de celle de 'New York'.

# ## **Y a-t-il une corélation en les candidature, les inscriptions & les admissions ?**

# In[28]:


df=data[['Applicants_total', 'Admissions_total', 'Enrolled_total']]
df.head()


# In[29]:


correlation=df.corr()
correlation


# Il y a une forte corrélation entre les candidatures et les admissions.  
# Idem pour les  admissions et les inscrits.  
# Ainsi qu'entre les inscrits et les candidatures et les admissions.

# In[30]:


# graphique de corrélations
sns.heatmap(correlation, annot=True)


# On voit la forte corrélation positive.

# ## **Classement**

# ### _Par candidatures_

# In[31]:


plt.figure(figsize = (14,8))

sns.histplot(data['Applicants_total'], bins = 40)                              # bins=interval
plt.title("Universités selon ls candidatures")
plt.xlabel("Candidatures")
plt.ylabel("Universités")
plt.axis([0,75000, 0,450])


# In[32]:


Moyenne = "La moyenne est {:.2f}".format(data['Applicants_total'].mean())
Mediane = "La mediane est {:.2f}".format(data['Applicants_total'].median())

print(Moyenne + "\n")
Mediane


# La majorité des universités ont moins de 5000 candidatures (3 premières barres).

# ### _Par admissions_

# In[33]:


plt.figure(figsize = (14,8))

sns.histplot(data['Admissions_total'], bins = 40)
plt.title("Universités selon les admissions")
plt.xlabel("Candidatures")
plt.ylabel("ºniversités")
plt.axis([0,75000, 0,450])

Moyenne = "La moyenne est {:.2f}".format(data['Admissions_total'].mean())
Mediane = "La mediane est {:.2f}".format(data['Admissions_total'].median())

print(Moyenne + "\n")
print(Mediane)


# Les 3 premières barres correspondent à environ 2500 ce qui est le nombre d'admissions de la majorité des universités.

# ### _Par inscription_

# In[34]:


plt.figure(figsize = (14,8))

sns.histplot(data['Enrolled_total'], bins = 30)
plt.title("ºniversités par inscriptions")
plt.xlabel("Candidatures")
plt.ylabel("Universités")
plt.axis([0,12000, 0,500])

Moyenne = "La moyenne est {:.2f}".format(data['Enrolled_total'].mean())
Mediane = "La mediane est {:.2f}".format(data['Enrolled_total'].median())

print(Moyenne + "\n")
print(Mediane)


# Toules les moyennes et médianes corroborent.  
# La majorité des universités ont environs moins de 1 000 inscrits.  
# Peu en ont plus de 4 000.

# ## **Les universités au grand nombre d'admissions sont-elles préférées ?**

# In[35]:


plt.figure(figsize = (12,8))
sns.scatterplot(x = data.Applicants_total, y=data.Admissions_total, hue = data.Control_of_institution)
plt.xlabel("Candidatures")
plt.ylabel("Asmissions")
plt.title("Croisement des candidatures et admissions")
plt.grid()


# Les universités avec le plus grand nombre de candidatures, n'ont pas le plus d'admissions.  
# Celles qui sont privées ont beaucoup de candidatures et peu d'admissions (- 5 000).

# ## _Croisement des Admissions et inscriptions_

# In[36]:


plt.figure(figsize = (12,8))
sns.scatterplot(x = data.Admissions_total, y=data.Enrolled_total, hue = data.Control_of_institution)
plt.xlabel("Admissions")
plt.ylabel("Inscrits")
plt.title("Croisement des Admissions et inscriptions")
plt.grid()


# Le résultat est analogue.  
# Mais, ça peut prêter à confision.

# In[37]:


data['Enrollment_rate']=(data.Enrolled_total/data.Admissions_total*100).round(2)
data


# In[38]:


plt.figure(figsize = (12,8))
sns.scatterplot(x = data.Admissions_total, y = data.Enrollment_rate)
plt.xlabel("Admissioins")
plt.ylabel("Taux d'inscription")
plt.title("Coroiseemnt des admissions et du taux inscriptions")


# S'il y a un grand nombre d'inscriptions, les admissions sont faibles.  
# Et vice versa.  
# Un étudiant peut être admis à une université sans s'y être inscrit.  
# Un grand nombre de candidatures, n'est pas dû à une préférence des étudiants.

# ## **Les étudient préfèrent-ils les universités publiques ou privées ?**

# In[39]:


plt.figure(figsize = (12,6))
sns.barplot(x = data.Control_of_institution, y=data.Applicants_total)
plt.title("Moyenne de candidatures selon le type les unversités publiques ou privées")
plt.xlabel("Type d'unversité")
plt.ylabel("Candidatures")


# Les universités publiques ont nettement plus de candidatures (environ le double).  
# Cela pourrait être dû au coût, aux conditions, les études proposées, ...  
# L'analyse doit aller plus loins.

# ## **Croisement des candidatures et des universités publiques & privées**

# ###  _Couper le dataframe en 2_

# In[40]:


private = data[data.Control_of_institution =="Private not-for-profit" ]
public  = data[data.Control_of_institution =="Public" ]
public


# In[41]:


private


# In[42]:


# que la colonne concernée
public['Control_of_institution'].head(50)


# In[43]:


# que la colonne concernée
private['Control_of_institution'].head(50)


# In[44]:


plt.figure(figsize = (16,7))
plt.hist([public.Applicants_total, private.Applicants_total], bins = 25, stacked = True)
plt.axis([0,50000,0,700])
plt.title("Candidatures par université publique ou privé")
plt.xlabel("Candidatues")
plt.ylabel("Universités")
plt.legend(['Universités publiques. ({})'.format(len(public)),
            'Universités privées. ({})'.format(len(private))])


# Il y a plus d'universités privées.  
# Les universités privées reçoivent généralement moins de 5 000 candidatures.  

# ## **Y a-t-il une relation entre le taux d'inscription et le type d'université ?**

# In[45]:


plt.figure(figsize = (12,6))
sns.barplot(x = data.Control_of_institution, y = data.Enrollment_rate)
plt.title("Le taux d'inscription selon le type d'universités")
plt.xlabel("Universités")
plt.ylabel("Taux d'inscription")


# Les universités publiques reçoivent plus de candidatures.

# In[46]:


total = data['Enrollment_rate'].sum()
data['Enrollment_pct'] = (data['Enrollment_rate'] / total) * 100

plt.figure(figsize=(12,6))
sns.barplot(x=data['Control_of_institution'], y=data['Enrollment_pct'])
plt.title("Le taux d'inscription selon le type d'universités (%)")
plt.xlabel("Universités")
plt.ylabel("Taux d'inscription (%)")
plt.show()


# Le nombre de candidatures n'est pas un gage de préférence.  
# Sauf exception, les universités ayant moins de candidatures ont plus d'admissions.  
# Le taux d'admissions n'est pas un signe d'influence.  
# Les universités publiques ont plus d'admissions.
