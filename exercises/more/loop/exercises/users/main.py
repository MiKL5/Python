# Afficher utilisateur 1 à 10
for i in range(10):
    print(f"Utilisateur {i + 1}")


for i in range(1,11):
    print(f"Utilisateur {i}")


i = 1
while i < 10:
    print(f"Utilisateur {i + 1}")
    i += 1


[print(f"Utilisateur {i}") for i in range(1, 11)] # 11 est exclu