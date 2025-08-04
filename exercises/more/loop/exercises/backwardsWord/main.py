mot = "python"
for lettre in [mot[i] for i in range(len(mot)-1, -1, -1)]:
    print(lettre)


mot = "python"
mot_a_lenvers = mot[::-1]
print(mot_a_lenvers)


mot = "python"
mot_a_lenvers = ''.join([mot[i] for i in range(len(mot)-1, -1, -1)])
print(mot_a_lenvers)


mot = "Python"
print(list(reversed(mot)))


mot = "Python"
for lettre in reversed(mot):
    print(lettre)