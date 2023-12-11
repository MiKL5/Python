# Demander un nombre entier de 0 à 10 et informer l'utilisateur s'il en donne un en dehors

while True:
    try:
        number = int(input("Veuillez saisir un nombre entier entre 1 et 10 : ") )
        # Vérifier si le nombre est entre 1 e 10
        if number not in range(1, 11):
            raise ValueError(f"Vous avez saisi {number}.\nLe nombre doit être compris entre 1 et 10.")
        break
    # Si ce n'est pas un entier
    except ValueError:
        print("Ce nombre est incorrect.\nLe nombre doit être en 1 et 10 sans virglue.\n")

print(f"{number} est un entier.")