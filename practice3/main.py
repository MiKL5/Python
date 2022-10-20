# 1. En utilisant la variable ci-dessous, imprimez « Hello, world ! ».
greeting = "Hello, world"
print(f"{greeting}")
# 2. Demandez à l’utilisateur son nom, puis saluez-le en utilisant son nom comme partie de la salutation (greeting). Le nom doit avoir sa première lettre en majuscule et ne doit pas être entouré d’espace blanc excessif.
name = input("What's your name ? ")
print(f"Hi {name.capitalize()}")
# 3. Concaténez la chaîne de caractères « J’ai  » et le nombre entier 29 pour produire une chaîne de caractères qui se lit « J’ai 29 ».
age = 29
print(f"i'm {age} yo.")
# 4. Formatez et imprimez les informations ci-dessous en utilisant l’interpolation de chaînes de caractères :
title = "Joker"
director = "Todd Phillips"
release_year = 2019
print(f"{title} ({release_year}) realized by {director}.")