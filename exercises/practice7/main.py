# 1) Demandez à l’utilisateur de saisir son prénom et son nom en réponse à une seule invite. Utilisez split pour extraire les noms, puis affectez chaque nom à une variable différente. Pour cet exercice, vous pouvez supposer que l’utilisateur a un seul prénom et un seul nom de famille.

# 2) Imprimez la liste, [1, 2, 3, 4, 5], au format 1 | 2 | 3 | 4 | 5 en utilisant la méthode join. N’oubliez pas que vous ne pouvez joindre que des collections de chaînes de caractères, vous devrez donc effectuer un traitement initial de la liste de chiffres.

# 3) Vous trouverez ci-dessous une courte liste de guillemets :
# quotes = [
#     "'Quel gâchis serait ma vie sans toutes les belles erreurs 
# que j'ai faites'",
#     "'Un virage sur la route n'est pas la fin de la route... Sauf 
# si vous n'arrivez pas à prendre le virage.",
#     "L'essence même de la romance est l'incertitude.",
#     "Nous ne sommes pas ici pour faire ce qui a déjà été fait."
#     ]
# Chaque guillemet est une chaîne de caractères, mais chaque chaîne contient en fait des guillemets au début et à la fin. En utilisant le slicing (découpage), extrayez le texte de chaque chaîne, sans ces guillemets supplémentaires, et imprimez chaque citation.
# Vous pouvez également essayer une solution utilisant strip.

# 4) Demandez à l’utilisateur de saisir un mot, puis imprimez la longueur de ce mot. Vous devez tenir compte de tout espace excédentaire dans la saisie de l’utilisateur. Vous devrez donc traiter la chaîne de caractères avant de trouver sa longueur.
# Si vous voulez aller un peu plus loin, vous pouvez demander à l’utilisateur un long morceau de texte. Vous pouvez alors lui dire combien de caractères il y a dans l’ensemble du texte, et vous pouvez également lui fournir un nombre de mots.

# 1. Demander le nom et le prénom. split pour extraire les noms et les afficher à différente variables. Un seul prénom et un seul nom.
names = input("Saisissez votre nom complet : ").split()

given_name = names[0] # prénom
surname = names[1] # nom patronyèmique
maiden_name = names[2] # nom de jeune fille

print(given_name)
print(surname)
print(maiden_name)