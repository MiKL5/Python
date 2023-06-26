# Ecrivez une fonction qui prend un tuple contenant des informations sur un acteur et retourne ces données sous forme de dictionnaire.

("Tom Hardy", "English", 42)

def dictify(actor):
    name, nationality, age = actor
    return {
        "name": name,
        "nationality": nationality,
        "age": age
    }