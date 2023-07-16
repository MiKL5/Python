# Exercice du Jour 21 - Python en 30 jours
# Votre tâche est de diviser ce code en fichiers.
# Créez un nouveau repl et divisez le code comme bon vous semble !

import database


USER_CHOICE = """
Entrez :
- 'a' pour ajouter un nouveau livre
- 'l' pour lister tous les livres
- 'r' pour marquer un livre comme lu
- 'd' pour supprimer un livre
- 'q' pour quitter
Quel est votre choix : """
BOOKS_FILE = 'books.json'


def menu():
    create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()

        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input("Saisissez le nouveau livre : ")
    author = input("Saisissez l'auteur de ce livre : ")

    insert_book(name, author)


def insert_book(name, author):
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    save_all_books(books)


def get_all_books():
    with open(BOOKS_FILE, 'r') as json_file:
        return json.load(json_file)


def save_all_books(books):
    with open(BOOKS_FILE, 'w') as file:
        json.dump(books, file)


def list_books():
    for book in get_all_books():
        read = 'LU' if book['read'] == '1' else 'NON LU'  # book[3] sera une valeur fausse (0) si Non lu.
        print(f"{book['name']}, {book['author']} — {read}")


def prompt_read_book():
    name = input('Saisissez le nom du livre que vous avez lu : ')

    mark_book_as_read(name)


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    save_all_books(books)


def prompt_delete_book():
    name = input('Saisissez le nom du livre à retirer : ')

    delete_book(name)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    save_all_books(books)


menu()