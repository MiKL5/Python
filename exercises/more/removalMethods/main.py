# Le dernier arrivé est partit
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
employes.pop(-1)
print(employes)

# Martine est partie
employes.pop(2)
print(employes)

# Partick part
element = employes.pop(-1)
print(element)

# La société à fait faillite
employes.clear()
print(employes)