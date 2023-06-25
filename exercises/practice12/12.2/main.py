# 2) Définissez une fonction appelée print_show_info qui a un seul paramètre. L’argument qui lui est passé sera un dictionnaire contenant des informations sur une série télé.
tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
 }
#  print_show_info(tv_show)
# La fonction print_show_info doit imprimer les informations stockées dans le dictionnaire, d’une manière agréable.
# Breaking Bad (2008) - 5 saisons
# N’oubliez pas que vous devez définir votre fonction avant de l’appeler ! 😉

def print_show_info(show):
    print(f"{show['title']} ({show['initial_release']}) - {show['seasons']} saison(s)")


print_show_info(tv_show)