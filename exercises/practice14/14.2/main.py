# 2) Utilisez le mode append pour écrire "How are you ?" sur la deuxième ligne du fichier hello_world.txt ci-dessus.


with open("hello_world.txt", "a") as f:
    f.write("\nHow are you?")