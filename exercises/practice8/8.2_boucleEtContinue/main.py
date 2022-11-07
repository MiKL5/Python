# Utilsier une boucle et le mot clé continue la chaîne "Python" sauf le "o".

string = "Python"
for character in string:
    if character == "o":
        continue
    print(character)