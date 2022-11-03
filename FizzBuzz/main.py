# Le projet d’aujourd’hui est en fait une question d’entretien très courante, qui tourne autour d’un jeu d’enfant de comptage qui s’appelle Fizz Buzz.

# Au cas où vous ne connaîtriez pas ce jeu, voici comment il se déroule :

# Un joueur commence par dire le chiffre 1.
# Chaque joueur dit ensuite à tour de rôle le chiffre suivant, en comptant un par un.
# Si le nombre est divisible par 3, au lieu de dire le nombre, le joueur doit dire « Fizz ».
# Si le nombre est divisible par 5, au lieu de dire le nombre, le joueur doit dire « Buzz ».
# Si le nombre est divisible par 3 et 5, au lieu de dire le nombre, le joueur doit dire « Fizz Buzz ».
# Si vous faites une erreur, vous êtes généralement éliminé du jeu, et le jeu continue jusqu’à ce qu’il ne reste plus qu’un seul joueur.

# Fizz = divisible par 3, Buzz = divisible par 5, Fizz = les deux, sinon affichier le ciffre ou nombre
for number in range(1 , 101) :
    if number % 3 == 0 :
    # if (number / 3).is_integer():
        if number % 5 == 0 :
            print("Fizz Buzz")
        else :
            print("Fizz")
    elif number %5 == 0 :
        print("Buzz")
    else:
        print(number)

# nom imbriqué et plus claire
for number in range(1 , 101) :
    if number % 3 == 0 and number % 5 == 0 : # je préfère vérifier les deux même si 15 est logique
    # if number % 15 == 0: # s'il n'est pas en 1er il n'est pas vérifier
        print("Fizz Buzz")
    elif number % 3 == 0 :
        print("Fizz")
    elif number % 5 == 0 :
        print("Buzz")
    else :
        print(number)
