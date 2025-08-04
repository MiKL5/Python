import random


player = input("Quel est ton nom ? 👉   ").strip() or "Joueur" # nom du joueur

print(f"\nBienvenue {player} dans le jeu : Devine le nombre ! 🎲")
print("Je pense à un nombre entre 1 et 100. Tu as 5 essais pour le trouver.\n")

nombre_secret = random.randint(1, 100)
tentatives = 0
max_tentatives = 5

while tentatives < max_tentatives:
    remaining = max_tentatives - tentatives # nombre de tentatives
    if remaining <= 3:
        print(f"⚠️ {player}, il ne te reste plus que {remaining} essai·s !")

    guess = input(f"Essai {tentatives + 1}/{max_tentatives} pour {player} : Quel est ton choix ? 👉   ") # deviner

    if not guess.isdigit():
        print("Choisi un nombre 👉   ")
        continue

    guess = int(guess)
    tentatives += 1

    if guess < nombre_secret:
        print("🔻 Trop bas !")
    elif guess > nombre_secret:
        print("🔺 Trop haut !")
    else:
        print(f"🎉 Bravo {player} ! Tu as trouvé le nombre {nombre_secret} en {tentatives} coups.")
        break
else:
    print(f"😢 Désolé {player}. Tu as dépassé les {max_tentatives} essai·s. Le nombre était {nombre_secret}.")