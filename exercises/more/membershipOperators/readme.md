# **Les opérateurs d'appartenances**<a href="../../../"><img align="right" src="../../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
Il s'agit d'`IN` et `NOT IN`
La casse est importante.
```py
utilisateurs = ["Paul", "Pierre", "Mary"]
"Paul" in utilisateurs                    # True
print("Paul" in utilisateurs)
print("paul" in utilisateurs)             # False
if "Paul" in utilisateurs:
    print("Hello Paul")
if "Paul" in utilisateurs:
    utilisateurs.remove("Paul")           # annonce une erreur si l'objet n'est pas dans la liste
print("Java" in "JavaScript")             # True
```