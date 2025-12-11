from pathlib import Path


entree = Path("miniProjets/folderOrganizer/firstname.txt")
sortie = Path("miniProjets/folderOrganizer/sorted.txt")

# Vérification que le fichier existe avant de commencer
if entree.exists():
    contenu           = entree.read_text(encoding="utf-8")
    contenu_normalise = contenu.replace("\n", ",").replace(".", ",")
    liste_brute       = contenu_normalise.split(",")
    pronoms_tries     = [nom.strip() for nom in liste_brute if nom.strip()]
    pronoms_tries.sort()
    texte_final = "\n".join(pronoms_tries)
    sortie.write_text(texte_final, encoding="utf-8")
    
    print(f"Voici les {len(pronoms_tries)} prénoms ordonés alphabétiquement dans '{sortie.name}'.")
else:
    print(f"Le fichier '{entree.name}' est introuvable.")