# 3) Imaginez que vous avez un fichier nommé data.txt avec le contenu suivant :

# Il y a des données ici !
# Ouvrez-le en lecture à l’aide de Python, mais assurez-vous d’utiliser un bloc try pour attraper une exception qui surviendrait si le fichier n’existe pas. Une fois que vous avez vérifié que votre solution fonctionne avec un fichier réel, supprimez le fichier et voyez si votre bloc try est capable de le gérer.

# Lorsque les fichiers n’existent pas lorsque vous essayez de les ouvrir, l’exception soulevée est FileNotFoundError.


try:
    with open("data.txt", "r") as text_file:
        print(text_file.read())
except FileNotFoundError:
    print("Erreur : Impossible de trouver 'data.txt'")