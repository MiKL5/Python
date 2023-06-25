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

# 3) Supprimez la liste des titres et l’année de sortie du dictionnaire que vous avez créé. Une fois que vous avez fait cela, ajoutez une nouvelle clé au dictionnaire pour stocker la date de sortie. La date de sortie de The Dark Side of the Moon est le 1er mars 1973.
del album["year"]
del album["tracks"]
for key, value in album.items():
    print(f"{key}: {value}")

album.update({"releaseDate": "1er mars 1973"})
for key, value in album.items():
    print(f"{key}: {value}")