# 3) Vous trouverez ci-dessous une liste contenant des détails sur plusieurs séries télévisées.

series = [
    {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
    {"title": "Fargo", "seasons": 4, "initial_release": 2014},
    {"title": "Firefly", "seasons": 1, "initial_release": 2002},
    {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
    {"title": "True Detective", "seasons": 3, "initial_release": 2014},
    {"title": "Westworld", "seasons": 3, "initial_release": 2016},
 ]
# Utilisez votre fonction, print_show_info, et une boucle for, pour itérer sur la liste series, et appelez votre fonction une fois pour chaque itération, en passant chaque dictionnaire. Vous devriez vous retrouver avec chaque série imprimée dans le format approprié.

def print_show_info(show):
    print(f"{show['title']} ({show['initial_release']}) - {show['seasons']} saison(s)")


for show in series:
    print_show_info(show)