# 1) Réécrivez le morceau de code suivant en utilisant un gestionnaire de contexte :

# f = open("hello_world.txt", "w")
#  f.write("Hello, World!")
#  f.close()


# ouvrir le fichier
with open("hello_world.txt", "w") as f:
    f.write("Hello, World!") # modif du fichier, Python le ferme à la fin