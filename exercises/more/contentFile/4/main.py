chemin = "/Volumes/T7/gh/Python/exercises/more/contentFile/file.txt"

with open(chemin, "r") as f:
    contenu = repr(f.readline()) # chaque mot en une liste avec \n
    print(contenu)