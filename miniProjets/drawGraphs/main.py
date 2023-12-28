from os import path
from chart import create_chart
from dataStorage import read_column

user_menu = """Veuillez choisir parmi les options suivantes :
- Saisissez 'c' ou 't' pour tracer un graphique.
- Saisissez 'q' pour quitter.
Quel est votre choix : """

charting_menu = "Saisissez la colonne que vous souhaitez représenter (un entier est attendu) : "

filename_prompt = "Saisissez le nom de fichier : "

def handle_chart(): 
    while True:
        column_input = input(charting_menu)
        # Vérifie que la chaîne entrée ne contient que des chiffres
        if not column_input.isdigit():
            print("Veuillez entrer un nombre entier.")
            continue
        # Convertir la chaîne
        column = float(column_input)
        # Si la valeur est valide, sortir
        break
    # Recherche le fichier
    if not path.isfile("iris.csv"):
        raise FileNotFoundError(f"Le fichier '{path.abspath('iris.csv')}' n'existe pas.")
    
    x = read_column(-1)
    y = [float(n) for n in read_column(column) ]
    create_chart(x, y)

    filename = input(filename_prompt)
    create_chart(x,y, filename.strip() )

while True:
    user_selection = input(user_menu)
    if user_selection == "q":
        break
    elif user_selection == "c" or user_selection == "t":
        handle_chart()
    else:
        print(f"Désolé, '{user_selection}' n'est pas une option valide.")