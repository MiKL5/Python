from pathlib import Path


# Dossier source fixe : data
source_dir = Path("data")

# Mapping des extensions
ext_map = {
    ".mp3": "Musique", ".wav": "Musique", ".flac": "Musique",
    ".avi": "Videogrammes", ".mp4": "Videogrammess", ".gif": "Videogrammess",
    ".bmp": "Images", ".png": "Images", ".jpg": "Images",
    ".txt": "Documents", ".pptx": "Documents", ".csv": "Documents",
    ".xls": "Documents", ".odp": "Documents", ".pages": "Documents"
}

print(f"Tri des fichiers dans {source_dir.absolute()}")

# Parcourir uniquement les fichiers du dossier data
for fichier in source_dir.iterdir():
    if fichier.is_file():  # Ignorer les sous-dossiers
        extension = fichier.suffix.lower()
        
        # Déterminer le dossier cible
        dossier_cible = "data"
        if extension in ext_map:
            dossier_cible = ext_map[extension]
        
        # Créer le sous-dossier s'il n'existe pas
        sous_dossier = source_dir / dossier_cible
        sous_dossier.mkdir(exist_ok=True)
        
        # Nouveau chemin complet
        nouveau_chemin = sous_dossier / fichier.name
        
        # Déplacer si nécessaire
        if nouveau_chemin != fichier:
            fichier.rename(nouveau_chemin)
            print(f"→ {fichier.name} dans {dossier_cible}")
