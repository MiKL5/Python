# 3. Extraire le texte des chaînes sans les guillemets avec slice et strip
quotes = [
    "Quel gâchis serait ma vie sans toutes les belles erreurs que j'ai faites.",
    "Un virage sur la route n'est pas la fin de la route... Sauf si vous n'arrivez pas à prendre le virage.",
    "L'essence même de la romance est l'incertitude.",
    "Nous ne sommes pas ici pour faire ce qui a déjà été fait."
    ]

for quote in quotes:
    print(quote[0:-1]) # 0 au lieu de 1 sonon il supprime deux caractère et 0 enlève les premiers guillets et -1 les derniers

for quote in quotes:
    print(quote.strip("'"))