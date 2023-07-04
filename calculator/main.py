# Vérif que l'opération demandée est valide
chunks = []
while len(chunks) != 3: # si la liste ne contient pas 3 éléments demander de saisir une opération
    operation = input("""Seules les opérations à 3 éléments sont acceptées !
    Les opérateurs sont
        _ `+`  pour l'addition ;
        _ `-`  pour la soustraction ;
        _ '*'  pour la multiplication ;
        _ `/`  pour la division réelle ;
        _ `//` pour la division entière ;
        _ `%`  pour le modulo (correspond au reste d'une division Euclidiene)
        
Saisissez une opération : """)
    chunks = operation.split() # split forcément sur un espace

# first_number = chunks[0]
# operator = chunks[1]
# second_number = chunks[2]

# Assignation multiple
first_number, operator, second_number = chunks

# Vérifications (vérifier que ce sont que des nombres puis que c'est un opérateur valide
valid_numbers = first_number.isdigit() and second_number.isdigit() # `isdigit` retourne vrai si c'est un chiffre ou un nombre et avec `and` si l'un est faux, tout est faux
valid_operator  = operator in  ["+", "-", "*", "/", "%", "//"] # in vérifie que la variable dans operator est bien dans la liste

if valid_operator and valid_numbers:
    print(f"{operation} = {eval(operation)}") # `eval()` évalue la chaîne de caractère comme du code Python et l'additioner ou autre s'il le faut
else:
    print(f"L'opératon {operation} est invalide.")