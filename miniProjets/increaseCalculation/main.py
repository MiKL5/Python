def calculer_augmentation(ventes):
    """
    Calcule le montant de l'augmentation en fonction du chiffre d'affaires réalisé par un employé.

    Paramètres:
    ventes (float) : Montant des ventes réalisées par l'employé.

    Retourne:
    float : Montant de l'augmentation.
    """
    if ventes < 100000:
        return 0
    elif 100000 <= ventes <= 150000:
        return 2500
    else:
        return 5000