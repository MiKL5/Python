import json


chemin = "/Volumes/T7/gh/Python/exercises/more/jsonFile/file.json"

with open(chemin, "w") as f:
    json.dump(list(range(10)), f, indent = 4) # indentation pour la lisibilité