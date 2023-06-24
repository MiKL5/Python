# La fonction intégrée `enumerate` génère un compteur

# Obtenir une sortie comme ceci :
# 1. Eternal Sunshine of the Spotless Mind (2004), réalisé par Michel Gondry
# 2. Memento (2000), réalisé par Christopher Nolan
# 3. Requiem for a Dream (2000), réalisé par Darren Aronofsky

movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]

# si title, director, year ne sont pas entre parenthèse, il y aura une erreur car il y aurait deux noms pour quatres valeurs ; les () font décomposer la deuxième valeur (le tuple) en trois variables
for counter, (title, director, year) in enumerate(movies, start=1):
    print(f"{counter}. {title} ({year}), réalisé par {director}")