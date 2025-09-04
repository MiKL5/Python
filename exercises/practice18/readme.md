# **Les importations**  <a href="../../"><img align="right" src="../../assets/logo/Python-logo-notext.svg" alt="Python" title="Phthon" widht="auto" height="64px"></a>

## **Les importations de base**

```py
import math
```
**Important !**  
Placer toujours les importations en haut !.  
Laisser un espace après avoir terminé vos importations pour les séparer du reste du code.  


## **Importer des éléments spécifique à partir d'un module**

Importation des constantes pi au tau
```py
from math import pi, tau
from tkinter import ttk
```

## **Modules et namespaces**

```py
import math
pritn(globals())
```
**_Important !_**  
Lorsque nous importons un module, Python doit exécuter le module. Cela a beaucoup de sens, car certaines valeurs ou fonctions peuvent dépendre d’autres valeurs du module. Quel que soit le style d’importation utilisé, Python doit toujours exécuter le module.

De nombreux développeurs Python supposent à tort qu’en utilisant un import de ce type :
```py
from math import pi, tau
```
est plus efficace, car nous ne saisissons que quelques valeurs, et Python n’a donc pas eu à exécuter le module. Ce n’est pas le cas, donc ne soyez pas tenté d’utiliser cette syntaxe d’importation spécifique parce que vous voulez rendre le chargement du module plus efficace.

Cependant, la syntaxe ci-dessus peut contribuer à l’efficacité d’une manière importante lors du référencement des valeurs. Si  un nom est utiliser de très nombreuses fois dans une partie de l'application sensible aux performances, la référence directe à pi sera légèrement plus rapide que math.pi. Il s’agit cependant d’un problème très rare, et la différence de vitesse est très faible. Il faut des millions de références pour qu’il y ait une différence notable.

## **Importations alias**

Utile quand le nom du module est long et réutiliser plusieurs foix.
```py
import numpy as np
```

## **Importer en utilisant `*`**

```py
from math import *
```
Signifie importer tout ce qui se trouve dans le module `math`, sauf le contenu des modules nécéssitant une importation spécifique (tel que ttk pour tkinter). Ce style d'importation est inutile 99 % du temps car tous les noms définis dans le module vont être ajoutés au namespace global.  
C'est d'alleurs une mauvaise idée si `math` et `numpy` sont importés car il utilisent tous le deux une valeur nommée `pi` dans le namespace global.  
Ce style d'imporation est surtout là pour facilité les tests rapides. Ceci n'est pas tolérable sur une application sérieuse.