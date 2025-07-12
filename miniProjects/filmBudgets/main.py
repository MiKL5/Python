# Pour ce projet, votre programme doit effectuer les opérations suivantes :
# Calculer le budget moyen de tous les films de l’ensemble des données.
# Imprimez chaque film dont le budget est supérieur à la moyenne que vous avez calculée. Vous devez également imprimer de combien le budget du film est supérieur à la moyenne.
# Imprimez le nombre de films dont le budget est supérieur à la moyenne que vous avez calculée.
# Si vous souhaitez relever un défi supplémentaire, permettez aux utilisateurs d’ajouter des films à l’ensemble des données avant d’effectuer les calculs.
# Pour ce faire, demandez à l’utilisateur combien de films il souhaite ajouter, ce qui vous permettra d’utiliser une boucle for et un range pour répéter un code un nombre donné de fois. À l’intérieur de la boucle for, vous pouvez écrire un code qui prend en compte une entrée utilisateur et ajoute à la liste de films un tuple de films contenant les données collectées.

# liste
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
# nouveau films
new_movie_count = int(input("Comnbien de film.s voulez vous ajouter : "))
for _ in range(new_movie_count):
    name = input("Saisissez un titre de film : ")
    budget = int(input("Saisissez son budget : "))
    movie_added = (name, budget)
    movies.append(movie_added)
# variables
high_budget_movies = []
total_budget = 0
# budget moyen
for movie in movies:
    total_budget = total_budget + movie[1]
average_budget = int(total_budget / len(movies))
# lequel dépasse le budget moyen
for movie in movies:
    if movie[1] > average_budget:
        high_budget_movies.append(movie)
        over_average_cost = movie[1] - average_budget
        print(f"{movie[0]} a coûté {movie[1]} €, dont {over_average_cost} € de plus que la moyenne.")
print(f"Il y a {len(high_budget_movies)} film.s au budget supérieur à la moyenne.")