users = ["user_01",
         "user_02",
         "user_03",
         "user_04",
         "user_05",
         "user_06"]

print(users[0     ]) # user_01
print(users[0: 1  ]) # idem
print(users[0: 4  ]) # les 4 premiers
print(users[0: 6  ]) # Tous
print(users[1: 2  ]) # le 2d
print(users[ :    ]) # Tous
print(users[ :-1  ]) # sauf 6
print(users[2:    ]) # de 3 à 6
print(users[:: 2  ]) # 1/2
print(users[:: 4  ]) # 1/4
print(users[1:-2:2]) # 2 et 4
print(users[::-1  ]) # inverser ; le pas est -1
print(users[1:-1  ]) # le 1er et le dernier sont exclus



liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
trois_premiers  = print(liste[ : 3])
trois_derniers  = print(liste[3:  ])
milieu          = print(liste[1:-1])
premier_dernier = print(liste[:: 5])