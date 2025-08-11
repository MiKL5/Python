# **Lire et écrire un fichier**<a href="../../../"><img align="right" src="../../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
```py
Path.home().iterdir()                             # un generator est un objet itérable

for f in Path.home().iterdir():
    print(f.name)


[f for r in Path.home().iterdir() if f.is_dir()]   # récupère tous les fichiers dont le chemin est un dossier
[f for r in Path.home().iterdir() if f.is_file()]  # récupère tous les fichiers répertoriés
```
Il y a aussi glob, puis rglob, qui lui est récursif.
```py
for f in p.glob("*.png"):                           # au premier niveau
    print(f.name)

for f in p.rglob("*.png"):                          # récursif ; va dans les sous-dossiers
    print(f.name)