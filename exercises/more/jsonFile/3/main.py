import json


chemin = "/Volumes/T7/gh/Python/exercises/more/jsonFile/file.json"

with open(chemin, "r") as f:
    json.load(f)