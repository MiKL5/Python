from datetime import datetime
import locale, os, json


# La date locale en français
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
date_formatee = datetime.now().strftime("%A %d %B %Y")

def afficher_menu():
    print("""\nQue veux-tu faire à la liste de courses ?\nChoisis une option entre 1 et 5.\n
           1. Ajouter un élément ✅
           2. En retirer un ❌
           3. Lister 📋
           4. Vider 🗑️
           5. Quitter 🚪""")

def charger_liste_de_courses(): # liste la liste
    if os.path.exists("/exercises/more/shoppingList2/list.json"):
        with open("list.json", "r") as fichier:
            return json.load(fichier)
    return []

def sauvegarder_liste_de_courses(liste): # enregistrer la liste
    with open("list.json", "w") as fichier:
        json.dump(liste, fichier, indent = 4)

def main():
    liste_de_courses = charger_liste_de_courses() # Charger la liste depuis le fichier JSON
    while True:
        afficher_menu() # Affichage du menu
        choix = input("\nQue veux-tu faire ? 👉      ")

        if choix == "1": # Ajout d'un élément
            element = input("De quoi as-tu besoin ? 👉   ")
            liste_de_courses.append(element)
            print(f"'{element}' a été ajouté.") # Confirmation
            print("La liste au " + date_formatee + " contient 👇")
            for i, element in enumerate(liste_de_courses, start=1):
                print(f"{i}. {element}")

        elif choix == "2": # Retirer un élément
            if not liste_de_courses:
                print("\nElle est vide 🤷")
            else:
                print("La liste au " + date_formatee)
                [print(f"{i + 1}. {element}") for i, element in enumerate(liste_de_courses)]
                try:
                    indice = int(input("Quel est l'indice de l'élément à enlever ? 👉 ")) - 1
                    if 0 <= indice < len(liste_de_courses):
                        element_retire = liste_de_courses.pop(indice)
                        print(f"❌ {element_retire} est retiré.")
                        print("Il reste au " + date_formatee)
                        [print(f"{i}. {element}") for i, element in enumerate(liste_de_courses, start=1)]
                    else:
                        print("L'indice est inexistant.")
                except ValueError:
                    print("Choisis entre 1 et 5 👉")

        elif choix == "3": # Lister les éléments
            if not liste_de_courses:
                print("\nElle est vide. 🤷")
            else:
                print("La liste au " + date_formatee + " contient")
                [print(f"{i}. {element}") for i, element in enumerate(liste_de_courses, start=1)]

        elif choix == "4": # Vider la liste
            liste_de_courses.clear()
            print("\nTu l'as vidée 🗑️")

        elif choix == "5": # Quitter le programme
            sauvegarder_liste_de_courses(liste_de_courses) # Sauvegarder la liste dans le fichier JSON
            print("\nÀ bientôt ! 😉\n")
            break # Sortie

        else:
            print("\n⚠️ L'option est inexistante.\n💡 Choisi une option de 1 à 5.")

main()