# 1) Utilisez map pour appeler la méthode strip sur chaque chaîne de la liste suivante :

# humpty_dumpty = [
#     "  Humpty Dumpty s'est assis sur un mur, ",
#     "Humpty Dumpty a fait une grande chute ; ",
#     "  Tous les chevaux du roi et tous les hommes du roi ",  
#     "    ne purent remettre Humpty en place."
# ]
# Imprimez les lignes de la comptine sur différentes lignes dans la console.

# N’oubliez pas que vous pouvez utiliser le module operator et la fonction methodcaller au lieu d’une expression lambda si vous le souhaitez.


from operator import methodcaller
humpty_dumpty = [
    "Humpty Dumpty s'est assis sur un mur, ",
    "Humpty Dumpty a fait une grande chute ; ",
    "  Tous les chevaux du roi et tous les hommes du roi ",  
    "    ne purent remettre Humpty en place."
]
print(*map(methodcaller("strip"), humpty_dumpty), sep="\n")