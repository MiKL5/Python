# 2) Utilisez une compréhension de dictionnaire pour créer un nouveau dictionnaire à partir du dictionnaire ci-dessous, où chacune des valeurs a une majuscule en première lettre.

# movie = {
#     "title": "thor: ragnarok",
#     "director": "taika waititi",
#     "producer": "kevin feige",
#     "production_company": "marvel studios"
# }
# Rappelez-vous que l’itération sur un dictionnaire ne nous donne que les clés par défaut. Vous pouvez utiliser la méthode items pour obtenir les clés et les valeurs.


movie = {
    "title": "thor: ragnarok",
    "director": "taika waititi",
    "producer": "kevin feige",
    "production_company": "marvel studios"
}
movie = {key: value.title() for key, value in movie.items()}