# 1) Convertisr le tuple externe en un dictionnaire à quatre clés (title, artist, year, track).

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

# 4) Essayez de récupérer l’une des valeurs que vous avez supprimées du dictionnaire. Cela devrait vous donner une KeyError. Une fois que vous avez essayé, répétez l’étape en utilisant la méthode get pour éviter que l’exception ne soit levée.