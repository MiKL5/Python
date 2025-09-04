# **Créer une liste depuis chaîne de caractères**<a href="../../../"><img align="right" src="../../../assets/logo/Python-logo-notext.svg" alt="Python" height="64px"></a>
**La méthode `split`** converti une chaîne de caractère en liste.
```py
courses = "Riz, Pommes, Lait, Salade, Saumon, Beure"
courses = courses.split() # va spliter à l'espace
print(courses)

courses = "Riz, Pommes, Lait, Salade, Saumon, Beure"
courses = courses.split(",") # 1 espace avant chaque mot
print(courses)

courses = "Riz, Pommes, Lait, Salade, Saumon, Beure"
courses = courses.split(", ")
print(courses)

courses = "Riz, Pommes, Lait, Salade, Saumon, Beure"
courses.split(", ") # si la variable n'est ni écrasée ni changée, il ne se passe rien
print(courses)

courses = "Riz, Pommes, Lait, Salade, Saumon, Beure"
courses = courses.split("-") # si le caractère n'est pas à la liste, rien ne change
print(courses)
```