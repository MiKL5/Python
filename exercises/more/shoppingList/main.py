import sys
from datetime import datetime
import locale


# la date locale en français
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
date_formatee = datetime.now().strftime("%A %d %B %Y")

def afficher_menu():
    print("""\nQue veux-tu faire à la liste de courses ?\nChoisi une option entre 1 et 5.\n
           1. Ajouter un élément  ✅
           2. En retirer un       ❌ 
           3. Lister              📋 
           4. Vider               🗑️ 
           5. Quitter             🚪""")

def main():
    liste_de_courses = [] # initialisée

    while True:
        afficher_menu() # affichage
        choix = input("\nQue veux-tu faire ? 👉  ")

        if choix == "1": # ajout
            element = input("De quoi à tu besoin ? 👉  ")
            liste_de_courses.append(element)
            print(f"'{element}' a été ajouté.") # confirmation
            print("La liste au " + date_formatee + " contient 👇")
            for i, element in enumerate(liste_de_courses, start=1):
                    print(f"{i}. {element}")
        elif choix == "2": # retirer
            if not liste_de_courses:
                print("\nElle est vide 🤷")
            else:
                print("La liste au " + date_formatee)
                for i, element in enumerate(liste_de_courses):
                    print(f"{i + 1}. {element}")
                try:
                    indice = int(input("Quel est l'indice de l'élément à enlever ? 👉  ")) - 1
                    if 0 <= indice < len(liste_de_courses):
                        element_retire = liste_de_courses.pop(indice)
                        print(f"❌ {element_retire} est retiré.")
                        print("Il reste au " + date_formatee)
                        for i, element in enumerate(liste_de_courses, start=1):
                            print(f"{i}. {element}")
                    else:
                        print("L'ndice est inexistant.")
                except ValueError:
                    print("Choisis entre 1 et 5 👉")

        elif choix == "3":
            if not liste_de_courses:
                print("\nElle est vide. 🤷")
            else:
                print("La liste au " + date_formatee + " contient")
                for i, element in enumerate(liste_de_courses, start=1):
                    print(f"{i}. {element}")

        elif choix == "4":
            liste_de_courses.clear()
            print("\nTu l'a vidée 🗑️")

        elif choix == "5":
            print("\nÀ bientôt ! 😉\n")
            sys.exit() # sortie

        else:
            print("Cette option n'existe pas.\nVeuillez entrer un nombre entre 1 et 5.")


main()