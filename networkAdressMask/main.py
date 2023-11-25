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


# Saisie de l'adresse du poste en binaire, conversion en entier et affichage
adresse = input("Entrez l'adresse binaire du poste : ")
nbAdresse = binaireVersEntier(adresse)
print("La conversion en entier donne ", nbAdresse)

# Saisie du masque due réseau en binaire, conversion en entier et affichage
masque = input("Entrez le masque du réseau en binaire : ")
nbMasque = binaireVersEntier(masque)
print("La conversion en entier donne ", nbMasque)

# Calcul de l'adresse réseau (avec ET entre adresse poste et masque)
reseau = nbAdresse & nbMasque
print("L'adresse réseau en entier est ", reseau)

# Conversion de l'adresse réseau en binaire
binaire = entierVersBinaire(reseau)
print("L'adresse réseau en binaire est ", binaire)