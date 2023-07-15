import json

def add_book():
    books = get_all_books()
    title = input("Titre : ").strip().title()
    author = input("Auteur : ").strip().title()
    year = input("Année de publication : ").strip()
    books.append({
        "title": title,
        "author": author,
        "year": year,
        "read": "Non lu"
    })

    with open("./jsonList/books.json", "w") as reading_list:
        json.dump(books, reading_list)


def create_book_file():
    try:
        with open("./jsonList/books.json", "x") as reading_list:
            json.dump([], reading_list)
    except FileExistsError:
        pass


def delete_book(books, book_to_delete):
    books.remove(book_to_delete)


def find_books():
    reading_list = get_all_books()
    matching_books = []
    search_term = input("Veuillez saisir un titre de livre : ").strip().lower()
    for book in reading_list:
        if search_term in book["title"].lower():
            matching_books.append(book)
    return matching_books


# récupérer les données, marquer comme lu, non lu et lister
def get_all_books():
    with open("./jsonList/books.json", "r") as reading_list:
        return json.load(reading_list)
    

def mark_book_as_read(books, book_to_update):
    index = books.index(book_to_update)
    books[index]['read'] = "Lu"


def mark_book_as_unread(books, book_to_update):
    index = books.index(book_to_update)
    books[index]['read'] = "Non lu"


def update_reading_list(operation):
    books = get_all_books()
    matching_books = find_books()
    if matching_books:
        operation(books, matching_books[0])
        with open("./jsonList/books.json", "w") as reading_list:
            json.dump(books, reading_list)
    else:
        print("Désolé, nous n'avons pas trouvé de livres correspondant à ce titre.")


def show_books(books):
    # Une ligne vide avant la sortie
    print()
    for book in books:
        print("{title}, par {author}, publiée en ({year}) - {read}".format(**book))
    print()
create_book_file()
menu_prompt = """Veuillez saisir l'une des options suivantes :
- 'a' pour ajouter un livre
- 'd' pour supprimer un livre
- 'l' pour lister les livres
- 'r' pour marquer un livre comme lu
- 'u' pour marquer un livre comme non lu
- 's' pour rechercher un livre
- 'q' pour quitter
Que voulez-vous faire ? """

# Obtenir une sélection de l'utilisateur
selected_option = input(menu_prompt).strip().lower()
# Exécuter la boucle jusqu'à ce que l'utilisateur sélectionne 'q'.
while selected_option != "q":
    if selected_option == "a":
        add_book()
    elif selected_option == "d":
        update_reading_list(delete_book)
    elif selected_option == "l":
        # Récupère l'ensemble de la liste de lecture pour l'imprimer
        reading_list = get_all_books()
        # Vérifie que la liste de lecture contient au moins un livre
        if reading_list:
            show_books(reading_list)
        else:
            print("Votre liste de lecture est vide.")
    elif selected_option == "r":
        update_reading_list(mark_book_as_read)
    elif selected_option == "u":
        update_reading_list(mark_book_as_unread)
    elif selected_option == "s":
        matching_books = find_books()
        # Vérifie que la recherche a retourné au moins un livre
        if matching_books:
            show_books(matching_books)
        else:
            print("Désolé, nous n'avons pas trouvé de livres pour ce terme de recherche")
    else:
        print(f"Désolé, '{selected_option}' n'est pas une option valide.")
    # Permettre à l'utilisateur de modifier sa sélection à la fin de chaque itération
    selected_option = input(menu_prompt).strip().lower()