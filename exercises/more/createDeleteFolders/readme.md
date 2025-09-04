# **Créer/supprimer les dossiers**<a href="../../../"><img align="right" src="../../../assets/logo/Python-logo-notext.svg" alt="Python" height="64px"></a>
```py
p = Path.home()

p = p / "DossierTest"

p.mkdir(exist_ok=True)
```
## **Hierarchie de dossier**
```py
p = p / "1" / "2" / "3"
p.mkdir(parents=True)    # s'il ne sait pas qu'il y a un dossier parent mkdir échouera
```
# Créer un fichier
```py
p = p / "readme.txt"
p.touch()
```
# **Supprimer le fichier**
```py
p.unlink()
```
## **Supprimer le dossier**
```py
p.rmdir()                  # pour les dossier vides
shutil.rmtree(p)           # inutile de le convertir en chaîne de caractères
