# **Lire un fichier**<a href="../../../"><img align="right" src="../../../assets/logo/Python-logo-notext.svg" alt="Python" height="64px"></a>
```py
chemin = "/Volumes/T7/gh/Python/exercises/more/contentFile/file.txt"

with open(chemin, "r") as f:
    contenu = repr(f.read()) # repr retire les retour à la ligne
    print(contenu)