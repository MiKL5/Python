import json

with open(test.json, "w") as f:
    json.dump("Pèche", f, ensure_ascii=False) # code ascii d"sactivé