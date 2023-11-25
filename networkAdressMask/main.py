import math

# Saisie de l'adresse du poste en binaire, conversion en entier et affichage
adresse = input("Entrez l'adresse binaire du poste : ")
k = 0
nb = 0
while len(adresse) > 0 :
    b = int(adresse[len(adresse) -1: ] )
    nb += b * math.pow(2, k)
    k += 1
    adresse = adresse[: len(adresse)-1]
print("La conversion en entier donne ", int(nb) )
nbAdresse = nb

# Saisie du masque due réseau en binaire, conversion en entier et affichage
masque = input("Entrez le masque du réseau en binaire : ")
k = 0
nbMasque = 0
while len(masque) > 0 :
    b = int(masque[len(masque) -1: ] )
    nbMasque += b * math.pow(2, k)
    k += 1
    masque = masque[: len(masque)-1]
print("La conversion en entier donne ", int(nbMasque) )

# Calcul de l'adresse réseau (avec ET entre adresse poste et masque)
reseau = int(nbAdresse) & int(nbMasque)
print("L'adresse réseau en entier est ", reseau)

# Conversion de l'adresse réseau en binaire
binaire = ""
while reseau != 0 :
    r = str(reseau % 2)
    binaire = r + binaire
    reseau = reseau // 2
print("L'adresse réseau en binaire est ", binaire)