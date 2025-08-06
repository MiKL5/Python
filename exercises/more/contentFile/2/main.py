chemin = "/Volumes/T7/gh/Python/exercises/more/contentFile/file.txt"

# le ficher sera fermer après usage
with open(chemin, "r") as f:
    contenu = f.read()
    print(contenu)