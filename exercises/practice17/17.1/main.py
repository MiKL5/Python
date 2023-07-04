# 1) Créez une fonction qui accepte un nombre quelconque de nombres comme arguments de position et qui imprime la somme de ces nombres. Rappelez-vous que nous pouvons utiliser la fonction sum pour additionner les valeurs d’un itérable.


def multi_add(*numbers):
    print(sum(numbers))