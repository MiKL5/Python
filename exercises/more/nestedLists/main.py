# Récupérer Java
liste = ["Python", ["Java", "C++", ['C']], ["Ruby"]]
print(liste[1][0])
# Récupérer Python
print(liste[0]     )
print(liste[0][0  ])
print(liste[0][0:2])   # les 2 premières
print(liste[0][0:6])   # entier
# Récupérer ruby
print(liste[2]   )     # le tableau
print(liste[2][0])     # le mot
# Récupérer C
print(liste[1][-1]   ) # le tableau
print(liste[1][-1][0]) # le mot
print(liste[1][ 2]   )
print(liste[1][ 2][0])
# Récupérer le c++
second_element = liste[1]
print(second_element[1])

# ajputer 6
liste = [1, 2, 3, 4, 5]
liste.append(6)
if 6 in liste:
    print("Le nombre 6 a bien été ajouté à la liste.")

langages = [["Python", "C++"], "Java"]
nombres = [1, [4, [2, 3]], 5, [6], [[7]]]

python = langages[ 0][0]
deux   = nombres [ 1][1][0]
sept   = nombres [-1][0][0]