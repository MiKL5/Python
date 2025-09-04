# **Le format JSON**<a href="../../../"><img align="right" src="../../../assets/logo/Python-logo-notext.svg" alt="Python" height="64px"></a>
Il stock en plus du texte, les listes et bases de données.
## **Écrire**
```py
import json


chemin = "/Volumes/T7/gh/Python/exercises/more/jsonFile/file.json"

with open(chemin, "w") as f:
    json.dump("Hi!", f) # méthode dump + le fichier
```
### **Une liste**
```py
import json


chemin = "/Volumes/T7/gh/Python/exercises/more/jsonFile/file.json"

with open(chemin, "w") as f:
    json.dump(list(range(10)), f, indent = 4) # indentation pour la lisibilité
```
## **Lire**
```py
import json


chemin = "/Volumes/T7/gh/Python/exercises/more/jsonFile/file.json"

with open(chemin, "r") as f:
    liste = json.load(f)
    print(liste)
```
### **Le type**
```py
import json


chemin = "/Volumes/T7/gh/Python/exercises/more/jsonFile/file.json"

with open(chemin, "r") as f:
    liste = json.load(f)
    print(type(liste)) # <class 'list'>
```
## **Ajouter**
La méthode "a" pour append ajouter à la site de la liste existante pas dedans. Et la syntaxe est invalide car il manque la virgule
```py
import json


chemin = "/Volumes/T7/gh/Python/exercises/more/jsonFile/6/data.json"

with open("chemin", "r") as f:
    donnees = json.load(f)

# print(donnees)

    donnees.append(10)

with open("chemin", "w") as f:
    json.dump(donnees, f, indent=4) # les datas dans le f + indentation
```
## **Les erreur courantes avec les fichiers**
Les / sur windows
les modes "r", "w", "a".
Fermer le fichier (close ou with).
Pour relire le fichier utiliser `f,seek(0)` ; le curseur sera au début. Ou un autre chiffre pour repprendre à un autre endroit.  
Et si `print(f.read(10))` ; les 10 premiers caractères sont lus.
## **Les erreur courantes en json**
Un fichier vide est illisible.  
`true` est `false` sont en muniscule en syntaxe json.  
Les caractères accentués, sont représentés par (e.g. \u00e8) ; `ensure_ascii=False` désactive le code ascii