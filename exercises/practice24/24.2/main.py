# Attraper les exceptions `ZeroDivisionError`, `TypeError` et `ArithmeticError`


# from numpy import divide

# divide(abc, base64)
#     try:
#         print(a / b)
#     except ZeroDivisionError:
#         print(f"Il est impossible de diviser par zéro")
#     except TypeError:
#         print(f"Les deux valeurs doivent être des chiffres ou des nombres. Impossible de diviser {a} et {b}.")
#     except ArithmeticError:
#         print(f"Impossible d'effectuer la division. Les chiffres ou nombres étaient probablement trop grands.")



try:
    a = int(input("Quel chiffre ou nombre voulez-vous diviser (le dividende) ➤  ") )
    b = int(input("Pour auel chiffre ou nombre voulez-vous le diviser (le diviseur) ➤  ") )
    quotient = int(a / b)
    int(print(f"Le quotient de {a} / {b} est ⫸  {quotient}.\n") )
except ZeroDivisionError:
    print(f"Il est impossible de diviser par zéro")
except TypeError:
    print(f"Les deux valeurs doivent être des chiffres ou des nombres. Impossible de diviser {a} et {b}.")
except ArithmeticError:
    print(f"Impossible d'effectuer la division. Les chiffres ou nombres étaient probablement trop grands.")