liste =("1", "4", "25", "Paul", "3", "Pierre", "z") 
for element in liste:
    if element.isdigit(): # False s'il y a au moins une lettre et passe à 'print()'
        continue # tant qu'il y a un chiffre, il envoi à la réitération
    print(element)

liste =("1", "4", "25", "Paul", "3", "Pierre", "z") 
for element in liste:
    if element.isdigit(): # False s'il y a au moins une lettre et passe à 'print()'
        break # s'il y a un nombre, il sort de la boucle
    print(element)

liste = [0, 1 ,2 ,3, 4, 5, 6, 7, 8, 9]
for i in liste:
    if i % 2 == 1:
        continue
    else:
        print(i)