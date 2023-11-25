""" conversion entier <---> binaire """

import math

def binaireVersEntier(binaire) :
    k = 0
    nb = 0
    while len(binaire) > 0 :
        b = int(binaire[len(binaire) -1: ] )
        nb += b * math.pow(2, k)
        k += 1
        binaire = binaire[: len(binaire)-1]
    return int(nb)


def entierVersBinaire(nbEntier) :
    binaire = ""
    while nbEntier != 0 :
        r = str(nbEntier % 2)
        binaire = r + binaire
        nbEntier = nbEntier // 2
    return binaire