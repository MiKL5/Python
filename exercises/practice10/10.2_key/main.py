album = {
    "title": "The Dark Side of the Moon",
    "artist": "Pink Floyd",
    "year": 1973,
    "tracks": (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
        )
    }

# 2) Interrogez les clés et les valeurs du dictionnaire. Pour chaque clé et valeur, vous devez imprimer le nom de la clé, puis la valeur correspondante.
for key, value in album.items():
    print(f"{key}: {value}")