from pathlib import Path


# Demander le chemin à l'utilisateur
chemin = input("Quel est lechemin dans lequel créer la structure ? ").strip()

d = {
    "Films": [
        "Le seigneur des anneaux",
        "Harry Potter", 
        "Moon",
    ],
    "Employes": [
        "Paul",
        "Pierre", 
        "Marie"
    ],
    "Exercices": [
        "les_variables",
        "les_fichiers",
        "les_boucles"
    ]
}

# Créer le dossier racine s'il n'existe pas
racine = Path(chemin)
racine.mkdir(parents=True, exist_ok=True)

# Itérer sur le dictionnaire et créer la structure
for nom_dossier_principal, liste_sous_dossiers in d.items():
    dossier_principal = racine / nom_dossier_principal
    
    # Créer le dossier principal
    dossier_principal.mkdir(parents=True, exist_ok=True)
    print(f"✅ Le dossier {dossier_principal} est créé")
    
    # Créer chaque sous-dossier
    for nom_sous_dossier in liste_sous_dossiers:
        sous_dossier = dossier_principal / nom_sous_dossier
        sous_dossier.mkdir(parents=True, exist_ok=True)
        print(f"  📁 Le sous-dessoer {sous_dossier} est créé")

print("\n🎉 La structure de dossiers est créée !")

# Pour vérifier ce qui a été créé
print("\n\nLes éléments existants sont")
for path in racine.rglob("*"):
    if path.is_dir():
        print(f"📁 {path.relative_to(racine)}")