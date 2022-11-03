# 1) Essayez d’approcher le comportement de l’opérateur is en utilisant ==. Rappelez-vous que nous disposons de la fonction id pour trouver l’adresse mémoire d’une valeur donnée, et que nous pouvons comparer les adresses mémoire pour vérifier l’identité.

# 2) Essayez d’utiliser l’opérateur is ou la fonction id pour étudier la différence entre les deux :
# numbers = [1, 2, 3, 4]
# new_numbers = numbers + [5]
# Et ça :
# numbers = [1, 2, 3, 4]
# numbers.append(5)
# Est-ce que new_numbers et numbers sont la même chose ? Qu’en est-il de numbers avant et après l’ajout de 5 ?

# 3) Demandez à l’utilisateur de saisir un nombre. Dites à l’utilisateur si le nombre est positif, négatif ou nul.

# 4) Écrivez un programme pour déterminer si des heures supplémentaires sont dues à un employé. Vous devez demander à l’utilisateur combien d’heures l’employé a travaillé cette semaine, ainsi que le salaire horaire de cet employé.
# Si l’employé a travaillé plus de 40 heures, vous devez imprimer un message indiquant que l’employé doit recevoir une rémunération supplémentaire, ainsi que le montant dû. Le montant supplémentaire dû est de 10% du salaire horaire de l’employé pour chaque heure travaillée au-delà des 40 heures. En fait, les employés sont payés 110% de leur salaire horaire pour toute heure supplémentaire.

# 1. Rapprocher le comportement de is avec ==, id peut comparer les adresses mémoires
liste1 = [1, 2, 3, 4, 5]
liste2 = [1, 2, 3, 4, 5]
print(id(liste1) == id(liste2))  # False

liste1 = [1, 2, 3, 4, 5]
liste1 = liste2
print(id(liste1) == id(liste2))  # False
print(liste1 is liste2)  # True

# 2.
# is ou id pour étudier la différence des éléments
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers is new_numbers)  # False car c'est une nouvelle liste

# toubrt l'id de numbers avant et aprés append
numbers = [1, 2, 3, 4]
print(id(numbers))  # 140220707722752
numbers.append(5)
print(id(numbers))  # 140220707722752

# is, se référer à la liste
numbers = [1, 2, 3, 4]
numbers_copy = numbers
numbers.append(5)
print(numbers is numbers_copy)  # True
# numbers_copy et numbers sont au début la même liste. modifier les nombresmodifie directement la liste. Les deux listes sont mises à jour et aucune n’est créée.

# 3. Demander un nombre et dire s'il est positif, nul ou négatif
number = float(input("Veuillez saisir un nombre : "))
if number > 0:
    print(f"{number} est positif !")
elif number < 0:
    print(f"{number} est négatif !")
else:
    print(f"Vous avez entré 0 !") # C'est meix ainsi car les conditions sont connectées avec que des if, il y a bcp de vérificcations inutiles

# Vérifier si des heures supp. sont dues
employee_name = input("Saisir le nom de l'employé.e : ")
hours_worked = float(input(f"Combien d'heures {employee_name} a-t-il / elle travaillé.e cette semaine ? "))
hourly_wage = float(input(f"Quel est le salaire horaire de {employee_name} ? "))
if hours_worked > 40:
    regular_pay = 40 * hourly_wage
    overtime_pay = (hours_worked - 40) * hourly_wage * 1.1
    owed_pay = float(regular_pay + overtime_pay)
else:
    owed_pay = float(hours_worked * hourly_wage)
print(f"{employee_name} doit percevoir la semaine {owed_pay:.2f} €.") # :.2f est placé ici pour faire l'arrondi à deux décimales