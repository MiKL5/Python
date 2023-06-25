# 1) Définissez quatre fonctions : add, substract, divide et multiply. Chaque fonction doit prendre deux arguments, et elles doivent imprimer le résultat de l’opération arithmétique indiquée par le nom de la fonction (addition, soustraction, division et la dernière multiplication).
# Lors de la commande d’une opération, le premier argument doit être traité comme l’opérande de gauche, et le deuxième argument comme l’opérande de droite. Par exemple, si l’utilisateur saisit 6 et 2 pour soustraire, le résultat doit être 4, et non -4.
# Vous devez également vous assurer que l’utilisateur ne peut pas passer 0 comme deuxième argument pour la fonction divide. Si l’utilisateur fournit 0, vous devez imprimer un avertissement au lieu de calculer sa division.

def add(a, b):
    print(a + b)
def subtract(a, b):
    print(a - b)
def multiply(a, b):
    print(a * b)
def divide(a, b):
    if b == 0:
        print("On ne peut pas diviser par 0 !")
    else:
        print(a / b)