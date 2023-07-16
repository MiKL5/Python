# 3) Utilisez filter pour supprimer tous les nombres négatifs de la plage suivante : range(-5, 11). Imprimez les nombres restants sur la console.

# solution 1
print(*filter(lambda number: number >= 0, range(-5, 11)))

# Solution 2 avec une fonction pour le prédicat de filter
def is_positive(number):
    return number >= 0
print(*filter(is_positive, range(-5, 11)))