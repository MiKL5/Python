# **Manipuler les chaînes de caractères**<a href="../../../"><img align="right" src="../../../assets/logo/Python-logo-notext.svg" alt="Python" height="64px"></a>
## **Les méthodes pour changer la case**
```py
"Bonjour".uipper()            # BONJOUR
"Bonjour".lower()             # bonjour
"bonjour à tous".capitalize() # Bonjour à tous
"Bonjour à tous".title()      # Bonjour À Tous
```
La méthode `lower()` est utile pour les comparaison sans tenir compte de la casse (E.g. : une recherche).  
`capitalize()` sert à formater un texte en paliiant les ommisions de majuscules.  
`title()` pour les titres.
# **Replacer les éléments**
```py
"Bonjour".replace("jour","soir") # Bonsoir
" Hello ".stripe()               # Hello
"  Bonjour  ".stripe(" ujor")    # Bon
"  Bonjour  ".lstripe(" ujor")   # 'Bonjour  '
"  Bonjour  ".rstripe(" ujor")   # '  Bon'
```
Il peut y avoir plusieurs replace à la suite.  
Si l'on ne précise rien à la suite de la méthode `strip()`, elle retire les espaces unitiles sauf à l'intérieur de la chaîne.  
Par contre, avec `"  Bonjour".stripe(" ujor")`, la méthode retire les 2 espace et s'arrête à B, puis va à la fin et retire `r`, `u`, `o`, `j`.
## **Séparer et joindre**
En programmation, il est commun que les données ne soient pas du bon type. 2 méthodes permettent de sépérer ou joindre les éléments d'une string. Ces méthodes sont jumelles.
```py
"1, 2, 3, 4, 5".split(", ")            # ['1', '2', '3', '4', '5']
", ".join("1, 2, 3, 4, 5".split(", ")) # '1, 2, 3, 4, 5'
".".join("1, 2, 3, 4, 5".split(", "))  # '1.2.3,4.5'
"-".join[(1, 2, 3)]                    # Erreur
"-".join[('1', '2', '3')]              # '1-2-3'
```
## **Remplir de zéros**
Utile pour nommer. les séquences d'image par exemple.
```py
"1".zfill(4)               # '0001'

for i in range(100):
    print(i)               # Pas propore

for i in range(100):
    print(str(i).zfill(6)) # 000001
```
`zfill` ne fonctionne que sur les chaînes de caractères.
## **Les méthodes 'is'**
```py
"bonjour".islower()               # True
"bonjour".isupper()               # False
"Bonjour À Tous".istitle()        # True
"000020".isdigit()                # True
"20yo".isdigit()                  # Falsse
```
`isdigit()` est très utile pour savoir si une chaîne de caractère peut-être convertie en nombre. D'autant plus avec `input()`.
## **Compter les occurences**
```py
"Bonjour le jour".count("jour").  # 2
"Bonjour le jour".count(" jour")  # 1
"Bonjour le jour".count(" jour ") # 0
```
La méhode compte les caractères, pas les mots. Il faut mettre un espace pour compter les mots complet.
## **Trouver une chaîne**
Il y a 3 méthodes `find()`, `index()` et `rfind()`.
```py
"Bonjour".find("jour")            # 3
"Bonjour".index("jour")           # 3
"Bonjour".find("soir")            # -1
"Bonjour".index("soir")           # ValueError
"Bonjour le jour".rfind("jour")   # 11
```
## **Chercher au début et à la fin**
Savoir si le fichier est au bon forrmat
```py
"image,png".endswith(".png")      # True
"image,png".endswith(".jpg")      # False
```
Le fichier commence-t-il par image ?
```py
"image,png".stratswith("image")     # True
"image,png".stratswith("dsc")       # False
"dsc0001,jpg".stratswith("dsc")     # True
```
