# Bienvenue à cette deuxième version sur le projet de liste de lecture, où nous allons nous attaquer à la version difficile du projet.
# Pour ce projet, l’application doit avoir les fonctionnalités suivantes :
#
# Les utilisateurs doivent pouvoir ajouter un livre à leur liste de lecture en fournissant un titre de livre, un nom d’auteur et une année de publication.
# Le programme doit stocker des informations sur tous ces livres dans un fichier appelé books.csv, et ces données doivent être stockées au format CSV.
# Les utilisateurs doivent pouvoir récupérer les livres de leur liste de lecture, et ces livres doivent être imprimés dans un format convivial.
# Les utilisateurs doivent être en mesure de rechercher un livre spécifique en fournissant un titre de livre.
# Les utilisateurs doivent pouvoir sélectionner ces options à partir d’un menu textuel, et ils doivent pouvoir effectuer plusieurs opérations sans redémarrer le programme. Vous pouvez voir un exemple de menu fonctionnel dans le post sur les boucles while (jour 8).
# Ce projet est beaucoup plus important que ceux que nous avons abordés auparavant, alors assurez-vous de l’aborder pièce par pièce.
#
# Si vous voulez vous lancer un défi, nous avons également une version un peu plus difficile du projet que vous pouvez essayer, avec des fonctionnalités supplémentaires.


def add_book():
    title = input("Titre : ").strip().title()
    author = input("Auteur : ").strip().title()
    year = input("Année de publication : ").strip()
    with open("books.csv", "a") as reading_list:
        reading_list.write(f"{title},{author},{year}\n")
def find_books():
    reading_list = get_all_books()
    matching_books = []
    search_term = input("Veuillez entrer un titre de livre à rechercher : ").strip().lower()
    for book in reading_list:
        if search_term in book["title"].lower():
            matching_books.append(book)
    return matching_books

# Fonction d'aide pour récupérer les données du fichier csv
def get_all_books():
    books = []
    with open("books.csv", "r") as reading_list:
        for book in reading_list:
            # Extrait les valeurs des données CSV
            title, author, year = book.strip().split(",")
            # Crée un dictionnaire à partir des données csv et l'ajoute à la liste books
            books.append({
                "title": title,
                "author": author,
                "year": year
            })
    return books
def show_books(books):
    
    # Ajoute une ligne vide avant la sortie
    print()
    for book in books:
        print(f"{book['title']}, par {book['author']}, publiée en ({book['year']})")
    print()
menu_prompt = """Veuillez saisir l'une des options suivantes :
- 'a' pour ajouter un livre
- 'l' pour lister les livres
- 's' pour rechercher un livre
- 'q' pour quitter
Que voulez-vous faire ? """

# Obtenir une sélection de l'utilisateur
selected_option = input(menu_prompt).strip().lower()

# Exécutez la boucle jusqu'à ce que l'utilisateur ait sélectionné 'q'.
while selected_option != "q" :
    if selected_option == "a" :
        add_book()
        print("Ajouté...")
    elif selected_option == "l" :
        # Récupère l'ensemble de la liste de lecture pour l'imprimer
        reading_list = get_all_books()
        # Vérifie que la liste de lecture contient au moins un livre
        if reading_list:
            show_books(reading_list)
        else:
            print("Votre liste de lecture est vide.")
    elif selected_option == "s" :
        matching_books = find_books()
        # Vérifie que la recherche a retourné au moins un livre
        if matching_books:
            show_books(matching_books)
        else:
            print("Désolé, il n'y aaucun livre à ce terme de recherche.")
    else:
        print(f"Désolé, '{selected_option}' n'est pas une option valide.")
    # Permettre à l'utilisateur de modifier sa sélection à la fin de chaque itération
    selected_option = input(menu_prompt).strip().lower()