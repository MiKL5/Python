# 1) Créez un programme court qui demande à l’utilisateur une liste de notes séparées par des virgules. Divisez la chaîne en notes individuelles et utilisez une compréhension de liste pour convertir chaque chaîne en un nombre entier. Vous devez utiliser une instruction try pour informer l’utilisateur lorsque les valeurs qu’il a saisies ne peuvent pas être converties.


grades = input("Veuillez saisir vos notes, séparées par des virgules : ").split(",")
try:
    grades = [int(grade) for grade in grades]
except ValueError:
    print("Les notes que vous avez saisies étaient dans un format invalide.")
# else:
#     print(grades)