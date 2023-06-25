# Créez une séquence de nombres à l’aide de range, puis demandez à l’utilisateur de saisir un nombre. Indiquez à l’utilisateur si son nombre se situe ou non dans la plage de valeurs que vous avez spécifiée.

numbers = range(27, 54)
# Demaner la saisie d'un nombre
user_number = int(input("Saisir un nombre : "))
# in vérifie si le nombre est dans la fourchette de valeurs
if user_number in numbers:
    print("Votre nombre se situe dans la plage de validité.")
else:
    if user_number < numbers[0]:
        print("Votre nombre est trop bas.")
    else:
        print("Votre nombre est trop haut.")