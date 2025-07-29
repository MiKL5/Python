import random


# Générer deux nombres aléatoires (flottants) entre 0 et 100
a = random.randrange(0 , 101 , 10)
b = random.randrange(0 , 101 , 10)

# Comparer les nombres et afficher le message approprié
if   a >  b:
    print("Le nombre a est plus grand que le nombre b.")
elif a <  b:
    print("Le nombre b est plus grand que le nombre a.")
elif a == b:
    print("Le nombre a et le nombre b sont égaux.")