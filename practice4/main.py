# 1. Créez une liste de films (movies) contenant un seul tuple. Le tuple doit contenir le titre du film, le nom du réalisateur, l’année de sortie du film et le budget du film.
#2. Utilisez la fonction d’entrée input pour recueillir des informations sur un autre film. Vous avez besoin du titre, du nom du réalisateur, de l’année de sortie et du budget.
#3. Créez un nouveau tuple à partir des valeurs que vous avez recueillies à l’aide de la fonction input. Assurez-vous qu’elles sont dans le même ordre que le tuple que vous avez écrit dans la liste des films (movies).
#4. Utilisez une f-string pour imprimer le nom du film et l’année de sortie en accédant à votre nouveau tuple de film.
#5. Ajoutez le nouveau tuple de film à la collection movies en utilisant append.
#6. Imprimez les deux films dans la collection movies.
#7. Supprimez le premier film de movies. Utilisez la méthode de votre choix.

# 1. Liste d'une seul tuple avec le titre, le réalisateur l'année de sortie et le budget
movies = [ ("Maléfique, le pouvoir du mal", "Joachim Roaning" "2019", "185 millions USD"), ]
print(movies[0])

# 2. input pour recueillir les infos d'un autre film
movies = [ ("Maléfique, le pouvoir du mal", "Joachim Roaning" "2019", "185 millions USD"), ]
title = input("Titre : ") # Maléfique
director = input("Réalistateur : ") # Joachim Roaning
year = input("Année : ") # 2014
budget = input("Budget : ") # unknow

# 3. Ajouter un second tuple dans l'ordre du précédant
movies = [ ("Maléfique, le pouvoir du mal", "Joachim Roaning" "2019", "185 millions USD"), ]
title = input("Titre : ")
director = input("Réalistateur : ")
year = input("Année : ")
budget = input("Budget : ")
new_movie = title, director, year, budget

# 4. imprimer avec une f-string
title = input("Titre : ")
director = input("Réalisateur : ")
year = input("Année de sortie : ")
budget = input("Budget : ")
new_movie = title, director, year, budget
print(f"{new_movie[0]} ({new_movie[2]})")

# 5. ajouter avec append
movies = [ ("Maléfique, le pouvoir du mal", "Joachim Roaning" "2019", "185 millions USD"), ]
title = input("Titre : ")
director = input("Réalisateur : ")
year = input("Année de sortie : ")
budget = input("Budget : ")
new_movie = title, director, year, budget
print(f"{new_movie[0]} ({new_movie[2]})")
movies.append(new_movie)

# 6. Imprimer deux films
movies = [ ("Maléfique, le pouvoir du mal", "Joachim Roaning" "2019", "185 millions USD"), ]
title = input("Titre : ")
director = input("Réalisateur : ")
year = input("Année de sortie : ")
budget = input("Budget : ")
new_movie = title, director, year, budget
print(f"{new_movie[0]} ({new_movie[2]})")
movies.append(new_movie)
print(movies[0])
print(movies[1])

# 7. Supprimer le 1er (méthode au choix)
        # solution 1 : pop
movies = [
    ("Maléfique, le pouvoir du mal", "Joachim Roaning" "2019", "185 millions USD"), 
    ("Maléfique", "Joachim Roaning", "2014", "unknow")
]
print(movies)
movies.pop(0)
print(movies)
        # solution 2 : DEL EST CONCIDÉRÉ PLUS PROPRE QUE POP
movies = [
    ("Maléfique, le pouvoir du mal", "Joachim Roaning" "2019", "185 millions USD"), 
    ("Maléfique", "Joachim Roaning", "2014", "unknow")
]
print(movies)
del movies[0]
print(movies)