# 2) Vous trouverez ci-dessous un tuple contenant plusieurs noms :

# names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")
# Utilisez une compréhension de liste avec une condition de filtrage afin que seuls les noms de moins de 8 caractères se retrouvent dans la nouvelle liste. Assurez-vous que toutes les premières lettres des noms de la nouvelle liste soient en majuscules.


from operator import methodcaller
names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")
names_title = map(methodcaller("title"), filter(lambda name: len(name) < 8, names))