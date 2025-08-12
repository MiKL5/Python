# **Trier les fichiers par extension**<a href="../../../"><img align="right" src="../../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
```py
dirs = {
    ".png"  : "Images",
    ".jpeg" : "Images",
    ".jpg"  : "Images",
    ".gif"  : "Images",
    ".mp4"  : "Videos",
    ".mov"  : "Videos",
    ".zip"  : "Archives",
    ".pdf"  : "Documents",
    ".txt"  : "Documents",
    ".json" : "Documents",
    ".mp3"  : "Musiques"
}

tri_dir = Path.home() / "Tri" # dossier à classer
files   = [f for f in tri_dir.iterdir() if f.is_file]
for f in files:
    output_dir = tri_dir / dirs.get(f.suffix, "Autres")
    output_dir.suffix(exist_ok=True)
    f,rename(output_dir / f.name)