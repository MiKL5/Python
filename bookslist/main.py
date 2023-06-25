reading_list = []

# Création du menu

# Le menu
menu_prompt = """Veuillez saisir l'une des options suivantes :
- 'a' pour ajouter un livre
- 'd' pour lister les livres
- q' pour quitter
Que voulez-vous faire ? """

selected_option = input(menu_prompt).strip().lower()

def add_book():
    title = input("Titre : ").strip().title()
    author = input("Auteur/autrice : ").strip().title()
    year = input("Année de publication : ").strip()
    new_book = {
        "title": title,
        "author": author,
        "year": year
    }
    reading_list.append(new_book)



def show_books():
    for book in reading_list:
        title, author, year = book.values()
        print(f"{title}, par {author} ({year})")


while selected_option != "q":
    if selected_option == "a":
        add_book()
        print("Ajout...")
    elif selected_option == "d":
        if reading_list:
            show_books()
        else:
            print("La liste de lecture est vide.")
        print("Affichage...")
        show_books()
    else:
        print(f"Désolé, '{selected_option}' n'est pas une option valide.")

    # Permettre à l'utilisateur de modifier sa sélection à la fin de chaque itération.
    selected_option = input(menu_prompt).strip().lower()

