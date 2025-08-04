def round_to_significant_figure(num, sig_figs):
    # arrondit un nombre à un certain nombre de chiffres significatifs
    if num == 0:
        return 0

    # utiliser le formatage de chaîne pour arrondir qu'en flottants
    return float(f"{num:.{sig_figs-1}f}")


while True:
    # demander le premier nombre avec validation
    while True:
        try:
            # saisir le premier nombre
            n1 = float(input("Quel est le premier nombre à additioner ? "))
            # si l'entrée est valide, on sort
            break
        except ValueError:
            # si l'entrée invalide
            print("Non, veuillez saisir un chiffre ou un nombre.")

    # idem pour le second
    while True:
        try:
            # saisir le second nombre
            n2 = float(input("Quel est le second nombre ? "))
            # Si l'entrée est valide, on sort de la boucle de validation
            break
        except ValueError:
            # si l'entrée est invalide
            print("Non, veuillez saisir un chiffre ou un nombre.")

    # affiche le résultat
    print(f"Le résultat de {n1} + {n2} est {n1 + n2}")

    # demande s'il souhaite une autre addition
    response = input("Y a-t-il une autre addition ? (o/n) ").strip().lower()

    # vérifie la réponse de l'utilisateur
    if response not in ("oui", "o", "yes", "y"):
        # si la réponse n'est pas affirmative, on sort de la boucle principale
        break