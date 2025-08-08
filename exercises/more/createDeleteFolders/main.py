from pathlib import Path
import shutil


p = Path.home()
p = p / "DossierTest"

p.mkdir()                # erreur s'il exist
p.mkdir(exist_ok=True)   # ne fait rien s'il exist

# Hierarchie de dossier
p = p / "1" / "2" / "3"
p.mkdir(parents=True)    # s'il ne sait pas qu'il y a un dossier parent mkdir échouera

# Créer un fichier
p = p / "readme.txt"
p.touch()                # ajouter

p.unlink()               # supprimer

# Supprimer le dossier
p.rmdir()                  # 3 est supprimer ; il était vide

# Supprimer le DoserTest
p.parent.parent.parent
print(p)

p.rmdir()                 # impossible car il y n'ést pas vide

shutil.rmtree(p)          # inutile de le convertir en chaîne de caractères