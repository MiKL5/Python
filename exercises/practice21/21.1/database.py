import json


BOOKS_FILE = 'books.json'

def create_book_table():
    try:
        with open(BOOKS_FILE, 'x') as file:
            json.dump([], file)  # initialiser le fichier en une liste vide
    except FileExistsError:
        pass


def get_all_books():
    with open(BOOKS_FILE, 'r') as file:
        return json.load(file)


def insert_book(name, author):
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    save_all_books(books)


def save_all_books(books):
    with open(BOOKS_FILE, 'w') as file:
        json.dump(books, file)


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    save_all_books(books)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    save_all_books(books)