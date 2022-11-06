# 2. Imprimer les chiffres en utilisant Join, il faut utiliser string
numbers = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
processed_numbers = []

for number in numbers:
    processed_numbers.append(str(number))

print(" | ".join(processed_numbers))