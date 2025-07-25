# **Les slices**<a href="../../../"><img align="right" src="../../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
Ce sont des tranches de lsite. Leur but est de récupérer certains éléménets de la liste (e.g. 1 éléments sur 2 ou les 3 premiers).  
C'est exclusif, le deuxième élément n'est pas pris.
```py
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
print(users[1:-1  ]) # le1er et le dernier sont exclus
```