# Récupérer les nombre positifs
liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nombres_positifs = []
for i in liste:
    if i > 0:
        nombres_positifs.append(i)


liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nombres_positifs = (i for i in liste if i > 0)     # 1,2,3,4,5

liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nombres_positifs = (i * 2 for i in liste if i > 0) # 2,4,6,8,10