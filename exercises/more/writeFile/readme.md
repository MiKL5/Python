# **Écrire un fichier**<a href="../../../"><img align="right" src="../../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
## **Écrire**
```py
chemin = "/Volumes/T7/gh/Python/exercises/more/writeFile/file.txt"

with open(chemin, "w") as f:
    f.write("Hello!") # écrase ce qu'il y avait
```
## **Ajouter**
```py
chemin = "/Volumes/T7/gh/Python/exercises/more/writeFile/file.txt"

with open(chemin, "a") as f:
    f.write("\nComment vas tu !") # écrase ce qu'il y avait
```