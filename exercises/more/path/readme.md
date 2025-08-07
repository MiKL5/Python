# **Le problèmes des chemins**<a href="../../../"><img align="right" src="../../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
Il y a 3 modules pour créer ou gérer les fichiers.
* `os` Concatener des morceaux de chemains. Créer et gérer des fichiers.
* `shutil` pour déplacer les fichiers.
* `glob` pour scanner le disque dur afin de récupérer des chemins de fichiers.

Le souci avec ces modules est l'utilisation des chaînes de caractères.  
Soit il faut avec `OS` le passer à différentes fonctions disponibles dans ces modules.  
Ou des opérations de caractère (split, join, ...) pour récupérer certaines parties d'un fichier (extension, dossier parent, ...)
```py
os.path.dirname("/users/mikl/project/main.py") # pour le dossier parent
os.path.dirname(os.path.dirname("/users/mikl/project/main.py")) # pour le dossier parent du parent
```
Ça devient rapidement lourd textuellement.  
Depuis la version 3.4, la librairie '`PathLib`' palie à ça.
```py
os.path.splitext("/users/mikl/projects/main.py")[1]
# Il y a bcp de risque d'erreur, on peut récupérer le mauvais indice. Ce n'est pas partique.
```
La librairie '`PathLib`' a aussi une solution.  
`PathLib` utilise des objets.
```py
path=Path("/users/mikl/project/main.py")
paht.parent   # /users/mikl
path.suffix   # .py
```
<!-- C'est le principe de la P2O. -->