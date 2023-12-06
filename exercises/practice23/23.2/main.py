# Réécrire ce code
# names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]
# names = map(lambda name: name.strip().title(), names)
# en un expression de générateur


names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]
names = (name.strip().split() for name in names)

names = list(names) # Conversion en liste car une expression génératrice est un itérateur qui produit des éléments à la volée
print(names)