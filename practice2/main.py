# 1. Demandez à l’utilisateur son nom et son âge, attribuez ces valeurs à deux variables, puis imprimez-les.
# input("What's ur name?")
name = input("What's ur name?")
toshi = input("how old are u?")
print(name + " at " + toshi + ".")
print("")
# 2. Cherchez à savoir ce qui se passe lorsque vous essayez d’attribuer une valeur à une variable que vous avez déjà définie. Essayez d’imprimer la variable avant et après avoir réutilisé le nom.
print(name)
name = print("Moi, moche et méchant")
# Car Python lit de haut en bas
print(name)
print("Python, oubli la valeur")
print("")
# 3. Vous trouverez ci-dessous un code comportant un certain nombre d’erreurs. Essayez de parcourir le programme ligne par ligne et de corriger les problèmes dans le code. Je vous encourage à essayer d’exécuter le programme pendant que vous travaillez dessus, car la lecture des messages d’erreur est un excellent entraînement pour le débogage de vos propres programmes.
hourly_wage = input("Veuillez saisir votre salaire horaire : ")
hours_worked = input("Combien d'heures avez-vous travaillé cette semaine ? ")
print("Salaire horaire : ")
print(hourly_wage)
print("Heures travaillées : ")
print(hours_worked)