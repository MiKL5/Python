# 1) Nous avons fourni ci-dessous une liste de tuples, où chaque tuple contient des détails sur un employé d’un magasin : son nom, le nombre d’heures travaillées la semaine dernière et son taux horaire. Imprimez le montant que chaque employé doit recevoir à la fin de la semaine dans un format agréable et lisible.
# 2) Pour les employés ci-dessus, imprimez ceux qui gagnent un salaire horaire supérieur à la moyenne.
# Conseil : vous pouvez utiliser une boucle for et deux variables pour garder la trace du salaire total et du nombre d’employés. Ensuite, utilisez ces deux variables pour calculer la moyenne. Enfin, ajoutez une autre boucle qui parcourt à nouveau la liste des employés et n’imprime que ceux dont le salaire horaire est supérieur à la moyenne calculée.

# Tuple contient la listes des employés, heures de la semaine passé et le taux horaire
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
# 1. Salaire hebdomadaire de chaque employé
for employee in employees:
    total_pay = employee[1] * employee[2]
    print(f"{employee[0]} doit être payé.e € {total_pay:.2f}")
# 2. Afficher ceux qui gagne un salaire horaire supérieur à la moyenne
total = 0
count = 0
# soluction 1
for employee in employees:
    total += employee[2] # raccourcis de total = total + employee[2]
    count += 1
    average_wage = total / count
for employee in employees:
    if employee[2] > average_wage:
        print(f"{employee[0]} gagne plus que la moyenne.")
# solution 2
for employee in employees:
    total += employee[2]
average_wage = total / len(employees) # la fonction len remplace la variable count
for employee in employees:
    if employee[2] > average_wage:
        print(f"{employee[0]} gagne plus que la moyenne.")