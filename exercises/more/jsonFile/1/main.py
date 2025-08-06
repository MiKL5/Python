import json


chemin = "/Volumes/T7/gh/Python/exercises/more/jsonFile/file.json"

with open(chemin, "w") as f:
    json.dump("Hi!", f) # méthode dump + le fichier