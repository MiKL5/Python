```python
import numpy            as np
import pandas           as pd
import matplotlib.pylab as plt
import seaborn          as sns
```

# **Analyse des données de Netflix**


```python
data = pd.read_csv('netflix.csv')
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>show_id</th>
      <th>type</th>
      <th>title</th>
      <th>director</th>
      <th>cast</th>
      <th>country</th>
      <th>date_added</th>
      <th>release_year</th>
      <th>rating</th>
      <th>duration</th>
      <th>listed_in</th>
      <th>description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>s1</td>
      <td>Movie</td>
      <td>Dick Johnson Is Dead</td>
      <td>Kirsten Johnson</td>
      <td>NaN</td>
      <td>United States</td>
      <td>September 25, 2021</td>
      <td>2020</td>
      <td>PG-13</td>
      <td>90 min</td>
      <td>Documentaries</td>
      <td>As her father nears the end of his life, filmm...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>s2</td>
      <td>TV Show</td>
      <td>Blood &amp; Water</td>
      <td>NaN</td>
      <td>Ama Qamata, Khosi Ngema, Gail Mabalane, Thaban...</td>
      <td>South Africa</td>
      <td>September 24, 2021</td>
      <td>2021</td>
      <td>TV-MA</td>
      <td>2 Seasons</td>
      <td>International TV Shows, TV Dramas, TV Mysteries</td>
      <td>After crossing paths at a party, a Cape Town t...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>s3</td>
      <td>TV Show</td>
      <td>Ganglands</td>
      <td>Julien Leclercq</td>
      <td>Sami Bouajila, Tracy Gotoas, Samuel Jouy, Nabi...</td>
      <td>NaN</td>
      <td>September 24, 2021</td>
      <td>2021</td>
      <td>TV-MA</td>
      <td>1 Season</td>
      <td>Crime TV Shows, International TV Shows, TV Act...</td>
      <td>To protect his family from a powerful drug lor...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>s4</td>
      <td>TV Show</td>
      <td>Jailbirds New Orleans</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>September 24, 2021</td>
      <td>2021</td>
      <td>TV-MA</td>
      <td>1 Season</td>
      <td>Docuseries, Reality TV</td>
      <td>Feuds, flirtations and toilet talk go down amo...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>s5</td>
      <td>TV Show</td>
      <td>Kota Factory</td>
      <td>NaN</td>
      <td>Mayur More, Jitendra Kumar, Ranjan Raj, Alam K...</td>
      <td>India</td>
      <td>September 24, 2021</td>
      <td>2021</td>
      <td>TV-MA</td>
      <td>2 Seasons</td>
      <td>International TV Shows, Romantic TV Shows, TV ...</td>
      <td>In a city of coaching centers known to train I...</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.columns
```




    Index(['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added',
           'release_year', 'rating', 'duration', 'listed_in', 'description'],
          dtype='object')




```python
# infos détaillées
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 8807 entries, 0 to 8806
    Data columns (total 12 columns):
     #   Column        Non-Null Count  Dtype 
    ---  ------        --------------  ----- 
     0   show_id       8807 non-null   object
     1   type          8807 non-null   object
     2   title         8807 non-null   object
     3   director      6173 non-null   object
     4   cast          7982 non-null   object
     5   country       7976 non-null   object
     6   date_added    8797 non-null   object
     7   release_year  8807 non-null   int64 
     8   rating        8803 non-null   object
     9   duration      8804 non-null   object
     10  listed_in     8807 non-null   object
     11  description   8807 non-null   object
    dtypes: int64(1), object(11)
    memory usage: 825.8+ KB


'release_year' est en `int`.  
director, cast, counrty, date_added, rating et duration ont des valeurs manquantes.


```python
# QUe les types de données
data.dtypes
```




    show_id         object
    type            object
    title           object
    director        object
    cast            object
    country         object
    date_added      object
    release_year     int64
    rating          object
    duration        object
    listed_in       object
    description     object
    dtype: object



1. Enlever les colonnes inutiles.  
Ici, il n'y en a qu'une.  
'Show_idi'.


```python
data = data.drop('show_id', axis=1)
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>type</th>
      <th>title</th>
      <th>director</th>
      <th>cast</th>
      <th>country</th>
      <th>date_added</th>
      <th>release_year</th>
      <th>rating</th>
      <th>duration</th>
      <th>listed_in</th>
      <th>description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Movie</td>
      <td>Dick Johnson Is Dead</td>
      <td>Kirsten Johnson</td>
      <td>NaN</td>
      <td>United States</td>
      <td>September 25, 2021</td>
      <td>2020</td>
      <td>PG-13</td>
      <td>90 min</td>
      <td>Documentaries</td>
      <td>As her father nears the end of his life, filmm...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TV Show</td>
      <td>Blood &amp; Water</td>
      <td>NaN</td>
      <td>Ama Qamata, Khosi Ngema, Gail Mabalane, Thaban...</td>
      <td>South Africa</td>
      <td>September 24, 2021</td>
      <td>2021</td>
      <td>TV-MA</td>
      <td>2 Seasons</td>
      <td>International TV Shows, TV Dramas, TV Mysteries</td>
      <td>After crossing paths at a party, a Cape Town t...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>TV Show</td>
      <td>Ganglands</td>
      <td>Julien Leclercq</td>
      <td>Sami Bouajila, Tracy Gotoas, Samuel Jouy, Nabi...</td>
      <td>NaN</td>
      <td>September 24, 2021</td>
      <td>2021</td>
      <td>TV-MA</td>
      <td>1 Season</td>
      <td>Crime TV Shows, International TV Shows, TV Act...</td>
      <td>To protect his family from a powerful drug lor...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>TV Show</td>
      <td>Jailbirds New Orleans</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>September 24, 2021</td>
      <td>2021</td>
      <td>TV-MA</td>
      <td>1 Season</td>
      <td>Docuseries, Reality TV</td>
      <td>Feuds, flirtations and toilet talk go down amo...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TV Show</td>
      <td>Kota Factory</td>
      <td>NaN</td>
      <td>Mayur More, Jitendra Kumar, Ranjan Raj, Alam K...</td>
      <td>India</td>
      <td>September 24, 2021</td>
      <td>2021</td>
      <td>TV-MA</td>
      <td>2 Seasons</td>
      <td>International TV Shows, Romantic TV Shows, TV ...</td>
      <td>In a city of coaching centers known to train I...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>8802</th>
      <td>Movie</td>
      <td>Zodiac</td>
      <td>David Fincher</td>
      <td>Mark Ruffalo, Jake Gyllenhaal, Robert Downey J...</td>
      <td>United States</td>
      <td>November 20, 2019</td>
      <td>2007</td>
      <td>R</td>
      <td>158 min</td>
      <td>Cult Movies, Dramas, Thrillers</td>
      <td>A political cartoonist, a crime reporter and a...</td>
    </tr>
    <tr>
      <th>8803</th>
      <td>TV Show</td>
      <td>Zombie Dumb</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>July 1, 2019</td>
      <td>2018</td>
      <td>TV-Y7</td>
      <td>2 Seasons</td>
      <td>Kids' TV, Korean TV Shows, TV Comedies</td>
      <td>While living alone in a spooky town, a young g...</td>
    </tr>
    <tr>
      <th>8804</th>
      <td>Movie</td>
      <td>Zombieland</td>
      <td>Ruben Fleischer</td>
      <td>Jesse Eisenberg, Woody Harrelson, Emma Stone, ...</td>
      <td>United States</td>
      <td>November 1, 2019</td>
      <td>2009</td>
      <td>R</td>
      <td>88 min</td>
      <td>Comedies, Horror Movies</td>
      <td>Looking to survive in a world taken over by zo...</td>
    </tr>
    <tr>
      <th>8805</th>
      <td>Movie</td>
      <td>Zoom</td>
      <td>Peter Hewitt</td>
      <td>Tim Allen, Courteney Cox, Chevy Chase, Kate Ma...</td>
      <td>United States</td>
      <td>January 11, 2020</td>
      <td>2006</td>
      <td>PG</td>
      <td>88 min</td>
      <td>Children &amp; Family Movies, Comedies</td>
      <td>Dragged from civilian life, a former superhero...</td>
    </tr>
    <tr>
      <th>8806</th>
      <td>Movie</td>
      <td>Zubaan</td>
      <td>Mozez Singh</td>
      <td>Vicky Kaushal, Sarah-Jane Dias, Raaghav Chanan...</td>
      <td>India</td>
      <td>March 2, 2019</td>
      <td>2015</td>
      <td>TV-14</td>
      <td>111 min</td>
      <td>Dramas, International Movies, Music &amp; Musicals</td>
      <td>A scrappy but poor boy worms his way into a ty...</td>
    </tr>
  </tbody>
</table>
<p>8807 rows × 11 columns</p>
</div>



2. Retirer  les valeurs manquantes.  
   6 colonnes sont concernées :
   * director,
   * cast,
   * counrty,
   * date_added,
   * rating,
   * duration.


```python
# Combiens de valeurs manquentes
valeurs_manquantes = data.isnull().sum()
valeurs_manquantes
```




    type               0
    title              0
    director        2634
    cast             825
    country          831
    date_added        10
    release_year       0
    rating             4
    duration           3
    listed_in          0
    description        0
    dtype: int64



Pour trouver celles qui manquent, il faut faire des recherches basées d'autres valeurs,  
E.g. le nom du directeur de production, les acteurs ...  
Ici, les lignes de ces valeurs seront supprimées.  
<!-- L'influence sur les analyses ne sera pas très grave. -->


```python
# Suppression des lignes aux valeurs manquantes colonnes par colonnes
data = data.dropna(subset=['country'])
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>type</th>
      <th>title</th>
      <th>director</th>
      <th>cast</th>
      <th>country</th>
      <th>date_added</th>
      <th>release_year</th>
      <th>rating</th>
      <th>duration</th>
      <th>listed_in</th>
      <th>description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Movie</td>
      <td>Dick Johnson Is Dead</td>
      <td>Kirsten Johnson</td>
      <td>NaN</td>
      <td>United States</td>
      <td>September 25, 2021</td>
      <td>2020</td>
      <td>PG-13</td>
      <td>90 min</td>
      <td>Documentaries</td>
      <td>As her father nears the end of his life, filmm...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TV Show</td>
      <td>Blood &amp; Water</td>
      <td>NaN</td>
      <td>Ama Qamata, Khosi Ngema, Gail Mabalane, Thaban...</td>
      <td>South Africa</td>
      <td>September 24, 2021</td>
      <td>2021</td>
      <td>TV-MA</td>
      <td>2 Seasons</td>
      <td>International TV Shows, TV Dramas, TV Mysteries</td>
      <td>After crossing paths at a party, a Cape Town t...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TV Show</td>
      <td>Kota Factory</td>
      <td>NaN</td>
      <td>Mayur More, Jitendra Kumar, Ranjan Raj, Alam K...</td>
      <td>India</td>
      <td>September 24, 2021</td>
      <td>2021</td>
      <td>TV-MA</td>
      <td>2 Seasons</td>
      <td>International TV Shows, Romantic TV Shows, TV ...</td>
      <td>In a city of coaching centers known to train I...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Movie</td>
      <td>Sankofa</td>
      <td>Haile Gerima</td>
      <td>Kofi Ghanaba, Oyafunmike Ogunlano, Alexandra D...</td>
      <td>United States, Ghana, Burkina Faso, United Kin...</td>
      <td>September 24, 2021</td>
      <td>1993</td>
      <td>TV-MA</td>
      <td>125 min</td>
      <td>Dramas, Independent Movies, International Movies</td>
      <td>On a photo shoot in Ghana, an American model s...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>TV Show</td>
      <td>The Great British Baking Show</td>
      <td>Andy Devonshire</td>
      <td>Mel Giedroyc, Sue Perkins, Mary Berry, Paul Ho...</td>
      <td>United Kingdom</td>
      <td>September 24, 2021</td>
      <td>2021</td>
      <td>TV-14</td>
      <td>9 Seasons</td>
      <td>British TV Shows, Reality TV</td>
      <td>A talented batch of amateur bakers face off in...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>8801</th>
      <td>Movie</td>
      <td>Zinzana</td>
      <td>Majid Al Ansari</td>
      <td>Ali Suliman, Saleh Bakri, Yasa, Ali Al-Jabri, ...</td>
      <td>United Arab Emirates, Jordan</td>
      <td>March 9, 2016</td>
      <td>2015</td>
      <td>TV-MA</td>
      <td>96 min</td>
      <td>Dramas, International Movies, Thrillers</td>
      <td>Recovering alcoholic Talal wakes up inside a s...</td>
    </tr>
    <tr>
      <th>8802</th>
      <td>Movie</td>
      <td>Zodiac</td>
      <td>David Fincher</td>
      <td>Mark Ruffalo, Jake Gyllenhaal, Robert Downey J...</td>
      <td>United States</td>
      <td>November 20, 2019</td>
      <td>2007</td>
      <td>R</td>
      <td>158 min</td>
      <td>Cult Movies, Dramas, Thrillers</td>
      <td>A political cartoonist, a crime reporter and a...</td>
    </tr>
    <tr>
      <th>8804</th>
      <td>Movie</td>
      <td>Zombieland</td>
      <td>Ruben Fleischer</td>
      <td>Jesse Eisenberg, Woody Harrelson, Emma Stone, ...</td>
      <td>United States</td>
      <td>November 1, 2019</td>
      <td>2009</td>
      <td>R</td>
      <td>88 min</td>
      <td>Comedies, Horror Movies</td>
      <td>Looking to survive in a world taken over by zo...</td>
    </tr>
    <tr>
      <th>8805</th>
      <td>Movie</td>
      <td>Zoom</td>
      <td>Peter Hewitt</td>
      <td>Tim Allen, Courteney Cox, Chevy Chase, Kate Ma...</td>
      <td>United States</td>
      <td>January 11, 2020</td>
      <td>2006</td>
      <td>PG</td>
      <td>88 min</td>
      <td>Children &amp; Family Movies, Comedies</td>
      <td>Dragged from civilian life, a former superhero...</td>
    </tr>
    <tr>
      <th>8806</th>
      <td>Movie</td>
      <td>Zubaan</td>
      <td>Mozez Singh</td>
      <td>Vicky Kaushal, Sarah-Jane Dias, Raaghav Chanan...</td>
      <td>India</td>
      <td>March 2, 2019</td>
      <td>2015</td>
      <td>TV-14</td>
      <td>111 min</td>
      <td>Dramas, International Movies, Music &amp; Musicals</td>
      <td>A scrappy but poor boy worms his way into a ty...</td>
    </tr>
  </tbody>
</table>
<p>7976 rows × 11 columns</p>
</div>




```python
# Manque t-il encore des pays ?
valeurs_manquantes = data.isnull().sum()
valeurs_manquantes
```




    type               0
    title              0
    director        2225
    cast             671
    country            0
    date_added         9
    release_year       0
    rating             3
    duration           3
    listed_in          0
    description        0
    dtype: int64




```python
# Combien de lignes reste t-il ?
data.shape
```




    (7976, 11)




```python
# Remplacer les notes manquantes par la plus répendue
# Quel est le mode ?
data['rating'].mode()
```




    0    TV-MA
    Name: rating, dtype: object




```python
# Sasn l'indice
data['rating'].mode()[0]
```




    'TV-MA'




```python
# Remplacer la valeur
data['rating'] = data['rating'].fillna(data['rating'].mode()[0])
```

    /var/folders/n0/_5ytbzzj5tqdxd4yymn1bkhw0000gn/T/ipykernel_12335/4250348504.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      data['rating'] = data['rating'].fillna(data['rating'].mode()[0])


☝️ Info que je modifie le fichier


```python
# Manque t-il encore des notes ?
data['rating'].isnull().sum()
```




    np.int64(0)




```python
# Nouvelles liste des valeurs mavaleurs manquantes
valeurs_manquantes = data.isnull().sum()
valeurs_manquantes
```




    type               0
    title              0
    director        2225
    cast             671
    country            0
    date_added         9
    release_year       0
    rating             0
    duration           3
    listed_in          0
    description        0
    dtype: int64




```python
# Supprimer la date d'ajout et la durée
data = data.dropna(subset=['date_added', 'duration'])
data.isnull().sum()
```




    type               0
    title              0
    director        2216
    cast             671
    country            0
    date_added         0
    release_year       0
    rating             0
    duration           0
    listed_in          0
    description        0
    dtype: int64




```python
# cast est director ne serviront pas
# Quelle quantité de valeurs unique
data.nunique()
```




    type               2
    title           7964
    director        4286
    cast            7095
    country          748
    date_added      1733
    release_year      73
    rating            14
    duration         212
    listed_in        497
    description     7949
    dtype: int64




```python
# Y a-t-il des doublons ?
data.duplicated().sum()
```




    np.int64(0)




```python
# Rendre la date exploitableabs
data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')
data.head()
```

    /var/folders/n0/_5ytbzzj5tqdxd4yymn1bkhw0000gn/T/ipykernel_12335/2688683202.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>type</th>
      <th>title</th>
      <th>director</th>
      <th>cast</th>
      <th>country</th>
      <th>date_added</th>
      <th>release_year</th>
      <th>rating</th>
      <th>duration</th>
      <th>listed_in</th>
      <th>description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Movie</td>
      <td>Dick Johnson Is Dead</td>
      <td>Kirsten Johnson</td>
      <td>NaN</td>
      <td>United States</td>
      <td>2021-09-25</td>
      <td>2020</td>
      <td>PG-13</td>
      <td>90 min</td>
      <td>Documentaries</td>
      <td>As her father nears the end of his life, filmm...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TV Show</td>
      <td>Blood &amp; Water</td>
      <td>NaN</td>
      <td>Ama Qamata, Khosi Ngema, Gail Mabalane, Thaban...</td>
      <td>South Africa</td>
      <td>2021-09-24</td>
      <td>2021</td>
      <td>TV-MA</td>
      <td>2 Seasons</td>
      <td>International TV Shows, TV Dramas, TV Mysteries</td>
      <td>After crossing paths at a party, a Cape Town t...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TV Show</td>
      <td>Kota Factory</td>
      <td>NaN</td>
      <td>Mayur More, Jitendra Kumar, Ranjan Raj, Alam K...</td>
      <td>India</td>
      <td>2021-09-24</td>
      <td>2021</td>
      <td>TV-MA</td>
      <td>2 Seasons</td>
      <td>International TV Shows, Romantic TV Shows, TV ...</td>
      <td>In a city of coaching centers known to train I...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Movie</td>
      <td>Sankofa</td>
      <td>Haile Gerima</td>
      <td>Kofi Ghanaba, Oyafunmike Ogunlano, Alexandra D...</td>
      <td>United States, Ghana, Burkina Faso, United Kin...</td>
      <td>2021-09-24</td>
      <td>1993</td>
      <td>TV-MA</td>
      <td>125 min</td>
      <td>Dramas, Independent Movies, International Movies</td>
      <td>On a photo shoot in Ghana, an American model s...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>TV Show</td>
      <td>The Great British Baking Show</td>
      <td>Andy Devonshire</td>
      <td>Mel Giedroyc, Sue Perkins, Mary Berry, Paul Ho...</td>
      <td>United Kingdom</td>
      <td>2021-09-24</td>
      <td>2021</td>
      <td>TV-14</td>
      <td>9 Seasons</td>
      <td>British TV Shows, Reality TV</td>
      <td>A talented batch of amateur bakers face off in...</td>
    </tr>
  </tbody>
</table>
</div>



☝️ Le messaeg est lié à la gestion des erreurs.


```python
# Extraire l'année dans une colonne
data['year_added'] = data['date_added'].dt.year.astype('Int64')
data.head()
```

    /var/folders/n0/_5ytbzzj5tqdxd4yymn1bkhw0000gn/T/ipykernel_12335/2448975934.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      data['year_added'] = data['date_added'].dt.year.astype('Int64')





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>type</th>
      <th>title</th>
      <th>director</th>
      <th>cast</th>
      <th>country</th>
      <th>date_added</th>
      <th>release_year</th>
      <th>rating</th>
      <th>duration</th>
      <th>listed_in</th>
      <th>description</th>
      <th>year_added</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Movie</td>
      <td>Dick Johnson Is Dead</td>
      <td>Kirsten Johnson</td>
      <td>NaN</td>
      <td>United States</td>
      <td>2021-09-25</td>
      <td>2020</td>
      <td>PG-13</td>
      <td>90 min</td>
      <td>Documentaries</td>
      <td>As her father nears the end of his life, filmm...</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TV Show</td>
      <td>Blood &amp; Water</td>
      <td>NaN</td>
      <td>Ama Qamata, Khosi Ngema, Gail Mabalane, Thaban...</td>
      <td>South Africa</td>
      <td>2021-09-24</td>
      <td>2021</td>
      <td>TV-MA</td>
      <td>2 Seasons</td>
      <td>International TV Shows, TV Dramas, TV Mysteries</td>
      <td>After crossing paths at a party, a Cape Town t...</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TV Show</td>
      <td>Kota Factory</td>
      <td>NaN</td>
      <td>Mayur More, Jitendra Kumar, Ranjan Raj, Alam K...</td>
      <td>India</td>
      <td>2021-09-24</td>
      <td>2021</td>
      <td>TV-MA</td>
      <td>2 Seasons</td>
      <td>International TV Shows, Romantic TV Shows, TV ...</td>
      <td>In a city of coaching centers known to train I...</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Movie</td>
      <td>Sankofa</td>
      <td>Haile Gerima</td>
      <td>Kofi Ghanaba, Oyafunmike Ogunlano, Alexandra D...</td>
      <td>United States, Ghana, Burkina Faso, United Kin...</td>
      <td>2021-09-24</td>
      <td>1993</td>
      <td>TV-MA</td>
      <td>125 min</td>
      <td>Dramas, Independent Movies, International Movies</td>
      <td>On a photo shoot in Ghana, an American model s...</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>8</th>
      <td>TV Show</td>
      <td>The Great British Baking Show</td>
      <td>Andy Devonshire</td>
      <td>Mel Giedroyc, Sue Perkins, Mary Berry, Paul Ho...</td>
      <td>United Kingdom</td>
      <td>2021-09-24</td>
      <td>2021</td>
      <td>TV-14</td>
      <td>9 Seasons</td>
      <td>British TV Shows, Reality TV</td>
      <td>A talented batch of amateur bakers face off in...</td>
      <td>2021</td>
    </tr>
  </tbody>
</table>
</div>




```python
# A-t-elle le bon type (int64) ?
data['year_added'].dtypes
```




    Int64Dtype()


