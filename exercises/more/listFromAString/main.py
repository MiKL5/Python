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