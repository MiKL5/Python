# Écrivez une fonction qui prend un seul nombre et renvoie True ou False selon que le nombre est premier ou non.

dividend = int(input("Veuillez saisir un nombre : "))
for divisor in range(2, dividend):
    if dividend % divisor == 0:
        print(f"{dividend} n'est pas premier !")
        break
else:
    print(f"{dividend} est premier !")


def is_prime(dividend):
    if dividend < 2:
        return False
    for divisor in range(2, dividend):
        if dividend % divisor == 0:
            return False
    return True