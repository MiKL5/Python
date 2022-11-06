# 1. Demander le nom et le prénom. split pour extraire les noms et les afficher à différente variables. Un seul prénom et un seul nom.
names = input("Saisissez votre nom complet : ").split()
given_name = names[0] # prénom
surname = names[1] # nom patronyèmique
maiden_name = names[2] # nom de jeune fille
print(given_name)
print(surname)
print(maiden_name)