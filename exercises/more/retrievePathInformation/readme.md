# **Les infos de chemins**<a href="../../../"><img align="right" src="../../../assets/logo/Python-logo-notext.svg" alt="Python" height="64px"></a>
```py
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