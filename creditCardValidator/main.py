# Utiliser la formule de Luhn. Il est utiliser dans des applications réelles pour tester les numéros de carte de crédit / débit ainsi que les numéro de série des cartes SIM.
# Cet algo identifie les numéros potentiels erronés, car il peut déterminé ou non qu'un numéro donné soit celui d'une carte valide.
# 1. retirer le chiffre le plus à droite du numéro de la carte. C'est le chiffre de control. Il est exclu de la pluspart des calculs
# 2. Inverser l'ordre des chiffres restants.
# 3. Pour cette séquence de chiffres inverser, gerder que les chiffres des indices pairs et les doubler. Si l'un des résultats est sup. à 9 y saoustraire 9.
# 4. Additionner tous les résultats et ajouter le chiffre de control.
# 5. Si le résultat est divisible par 10, le nombre est un numéro de carte valide. Sinon, ce n'est pas le cas.


# dmd le numéro de la carte, et ôter les espaces et convertir le numéro
cardNumber = list(input("Veuillez saisir un numéro de carte : ").strip())
# Ôter le dernier chiffre
checkDigit = cardNumber.pop()
# Inverser l'ordre des chiffres restants
cardNumber.reverse()

# Si le chiffre de chaque indice est pair, le doubler et  Si le nombre est sup. à 9 soustraire 9.
# Vérifier si l'indice est divisible par 2 (pair)
processedDigits = []
for index, digit in enumerate(cardNumber):    
    if index % 2 == 0:
        doubledDigit = int(digit) * 2
        # Soustraire 9 de tout résultat supérieur à 9
        if doubledDigit > 9:
            doubledDigit = doubledDigit - 9
        processedDigits.append(doubledDigit)
    else:
        processedDigits.append(int(digit))
# Additioner les chiffres
total = int(checkDigit) + sum(processedDigits)
# Vérifier si la somme est divivsible par 10
if total % 10 == 0:
    print("Ce numréo est valide")
else:
    print("Ce numéro est invalide")