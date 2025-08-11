from pathlib import Path


Path.home().iterdir()                             # un generator est un objet itérable

for f in Path.home().iterdir():
    print(f.name)                                 # ajout de .name pour n'avoir que les noms si y a que f ; il y a les chemain aussi

[f for r in Path.home().iterdir() if f.is_dir()]  # récupère tous les fichiers dont le chemin est un dossier
[f for r in Path.home().iterdir() if f.is_file()] # récupère tous les fichiers répertoriés

p = Path.home() / "downloads"                     # définir un dosier

# p.glob("*.png")                                   # au premier niveau

for f in p.glob("*.png"):
    print(f.name)

# p.rglob("*.png")                                  # récursif ; va dans les sous-dossiers

for f in p.rglob("*.png"):
    print(f.name)