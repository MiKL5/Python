from pathlib import Path


p = Path("/Volumes/T7/gh/Python/exercises/more/retrievePathInformation/main.py")
print(p.name)            # nom : main.py
print(p.stem)            # av. l'extention
print(p.suffix)          # extention
print(p.suffixes)        # s'il y a plusieurs extentions
print(p.parent)          # dossier logeant le fichier
print(p.parent.parent)   # le dosier logeant le dossier logeant le fichier
print(p.parts)           # toutes les parties du chemin
print(p.exists)          # exist ou non
print(p.is_dir)          # dossier ?
print(p.is_file)         # fichier ?

print(dir(p))