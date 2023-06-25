s = set()

# Ajoutez trois éléments à votre ensemble vide en utilisant soit plusieurs appels de add, soit un seul appel de update.

# Avec add
s.add("chat")
s.add("cheval")
s.add("lapin")

# Avec une boucle
s = set()
for number in range(1, 4):
    s.add(number)

# Avec update()

s = set()
s.update(range(1,4))