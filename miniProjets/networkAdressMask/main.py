import conversion

# Saisie de l'adresse du poste en binaire, conversion en entier et affichage
adresse = input("Entrez l'adresse binaire du poste : ")
nbAdresse = conversion.binaireVersEntier(adresse)
print("La conversion en entier donne ", nbAdresse)

# Saisie du masque due réseau en binaire, conversion en entier et affichage
masque = input("Entrez le masque du réseau en binaire : ")
nbMasque = conversion.binaireVersEntier(masque)
print("La conversion en entier donne ", nbMasque)

# Calcul de l'adresse réseau (avec ET entre adresse poste et masque)
reseau = nbAdresse & nbMasque
print("L'adresse réseau en entier est ", reseau)

# Conversion de l'adresse réseau en binaire
binaire = conversion.entierVersBinaire(reseau)
print("L'adresse réseau en binaire est ", binaire)