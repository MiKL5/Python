# **Modules et fonctions**
Un module est un fichier de Python contenant des fonctions prêtent à l'emploi.
```py
import module
```
## **Le module `random`**
### **La fonction `randint`**
C'est une fonction inclusive ; tous les nombres entre parathèses sont inclus.
```py
import random


r = random.randint(0 , 1)
print(r)

r = random.randint(0 , 2)
print(r)
```
### **La fonction `uniform`**
Ça différence, c'est les décimales. Et, s'utilise avec `random`.
```py
r = random.uniform(0 , 2)
print(r)
```
### **La fonction `randrange`**
Un argument qui est la fin de l'intervale exclusive.
```py
r = random.randrange(1) # 0
print(r)
```
Elle peut inclure un pas.
```py
r = random.randrange(0 , 101 , 10)
print(r)
```
## **Le module `OS`**
Bien que `pathllib` existe depuis 3.6, `OS` reste parfoir utile.
`OS` sert plus à créer / supprimer des dossiers.
```py
import OS


chemin = "docs/samples/modules&Functions/os"

# Nex folder
os.path.join(chemin , "folder")
```
⚠️ `join` gère les slash ; cela l'OS, ils n'ont pas le même sens.

⚠️ Pour la création de dossier, il y a `mkdir` et `makedirs`.  
`makedirs` peut créer plusieurs dossiers en une commande. E.g. `os.path.join(chemin , "folder" , "test")`.