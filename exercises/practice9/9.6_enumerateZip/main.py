# Un avertissement pour l’utilisation de enumerate et zip

# Une chose dont vous devez être conscient en ce qui concerne les objets enumerate et zip c’est qu’ils sont consommés (donc vides) lorsque nous itérons sur eux. Ce n’est généralement pas un problème lorsque nous les utilisons directement dans des boucles, mais cela peut parfois faire trébucher les nouveaux développeurs lorsqu’ils assignent un objet zip ou enumerate à une variable.

movie_titles = [
    "Forrest Gump",
    "Howl's Moving Castle",
    "No Country for Old Men"
]
movie_directors = [
    "Robert Zemeckis",
    "Hayao Miyazaki",
    "Joel and Ethan Coen"
]

movies = zip(movie_titles, movie_directors)
for title, director in movies:
    print(f"{title} by {director}.")
movies_list = list(movies)
# Accessible une seul fois
"""
print(f"There are {len(movies_list)} movies in the collection.")
print(f"These are our movies: {movies_list}.")
"""

# Conversion en list non itérative
movies = list(zip(movie_titles, movie_directors))