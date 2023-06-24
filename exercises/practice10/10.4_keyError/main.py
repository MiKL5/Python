album = {
    "title": "The Dark Side of the Moon",
    "artist": "Pink Floyd",
    "year": 1973,
    "tracks": [
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
    ]
}

del album["year"]
album.update({"Release date": "1er mars 1973"})
for key, value in album.items():
    print(f"{key}: {value}")

# 4) Essayez de récupérer l’une des valeurs que vous avez supprimées du dictionnaire. Cela devrait vous donner une KeyError. Une fois que vous avez essayé, répétez l’étape en utilisant la méthode get pour éviter que l’exception ne soit levée.

# print(album("year")) # affiche la keyError
print(album.get("year")) # affiche none dans le terminal