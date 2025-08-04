import random

print("""Bienvenue dans le jeu : Devine le nombre ! 🎲
         Devines le nombre entre 1 et 100.""")

# Générer un nombre aléatoire
nombre_secret = random.randint(1, 100)
tentatives = 0

while True:
    guess = input("Quel est ton choix ? 👉   ")
    
    # Vérification si c'est bien un nombre
    if not guess.isdigit():
        print("Devines le nombre 👉   ")
        continue

    guess = int(guess)
    tentatives += 1

    if guess < nombre_secret:
        print("🔻 Trop bas !")
    elif guess > nombre_secret:
        print("🔺 Trop haut !")
    else:
        print(f"🎉 Bravo ! Tu as trouvé le nombre {nombre_secret} en {tentatives} tentatives.")
        break
