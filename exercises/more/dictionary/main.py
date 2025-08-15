dictionnaire0 = {"prenom" : "Paul", "profession" : "Ingénieur"}

dictionnaire1 = {
    0: {"prenom":     "Paul",
        "profession": "Ingénieur",
        "ville":      "Paris"},
    1: {"prenom":     "Julie",
        "profession": "Architecte",
        "ville":      "Marseille"},
    2: {"prenom":     "Pierre",
        "profession": "Plombier",
        "ville":      "Nantes"}
}

#print(dictionnaire1[0])                                 # tout
print(dictionnaire1[0]["prenom"])                        # plus clair qu'une liste
print(dictionnaire1.get("nom"))    # 'get' retourne 'none' si l'indice n'exite pas
print(dictionnaire1.get("nom", "La clé n'exite pas"))    # 'get' retourne le message si la clé est inexistante