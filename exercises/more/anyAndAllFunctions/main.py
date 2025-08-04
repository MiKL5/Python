any(False, False, True, False) # 1 vrai suffit à retourné True
all(False, False, True, False) # 1 vrai alors False


all([f.endswith(".jpg") for f in files]) # Si 1 fichier n'est pas un jpg ; False


# Au moins un élève a-t-il eu plus de 18 ?
notes = [12, 14, 20, 10, 8]
any([x > 18 for x in notes]) # 20 est supérieur à 18 ; True