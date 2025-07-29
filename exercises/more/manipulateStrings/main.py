for i in range(100):
    print(str(i).zfill(6))

"bonjour".islower()
True

"Bonjour À Tous".istitle()
True

"000020".isdigit()
True

"20yo".isdigit()
False

"Bonjour le jour".count("jour")
2

"Bonjour le jour".count(" jour")
1

"Bonjour le jour".count("   jour    ")
0

# Le nombre d'occurence d'une lettre
lettre_a_chercher = "o"
phrase = "Bonjour tout le monde"
resultat = phrase.replace("Bonjour", "Bonsoir").count(lettre_a_chercher)

# Combien de phrase
lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
		   Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
		   Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
		   Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
resultat = lorem.count(".")

# Ordonner un chaîne
chaine = "Pierre, Julien, Anne, Marie, Lucien"
liste = chaine.split(", ")
ordre = sorted(liste)
ordre = ", ".join(ordre)