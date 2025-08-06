chemin = "/Volumes/T7/gh/Python/exercises/more/contentFile/file.txt"

with open(chemin, "r") as f:
    contenu = repr(f.read()) # repr retire les retour à la ligne
    print(contenu)