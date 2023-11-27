class Personnage :
    # Constructeur
    def __init__(self, nom) :
        self.nom = nom
        self.vie = 5
    # Augmentation de vie
    def augmanterVie(self, vieEnPlus = 1) : # s'il n'y a pas `=1`, alors 1 en plus par défaut
        self.vie += vieEnPlus
    # Diminution de vie en évitant d'être inférieur à 0
    def diminueVie(self, vieEnMoins = 1) :
        self.vie = max(0, self.vie - vieEnMoins)
    # Attaqque un personnage
    def attaque(self, unPersonnage) :
        unPersonnage.diminueVie(2) # Pas de chiffre en () si diminueVie était initialisé à 2, ici, je met 2
        self.augmanterVie()

# Code principal
# liste de personnage
lesPersonnages = list()
# Boucle sur le menu
choix = "x"
while choix != "Q" and choix != 'q' :
    print("""
        Créer un nouveau personnage ...... 1
        Gérer une attaque ................ 2
        Quitter .......................... Q""")
    choix = input("        Votre choix                      : ")
    # Gestion du choix
    if choix == "1" :
        nom = input("        Saisissez le nom                 : ")
        nouveau = Personnage(nom)
        lesPersonnages.append(nouveau) # append est utilisable car la taille de la liste n'est pas définie
    elif choix == "2" :
        # Afficher la liste des personnages
        for k, unPersonnage in enumerate(lesPersonnages) :
            print("       ", k, ":", unPersonnage.nom), "(vie :", unPersonnage.vie, ")"
        # Choix de l'attaquant et de l'attaqué
        numAttaquant = int(input("        n° de l'attaquant : ") )
        numAttaque = int(input("        n° de l'attaqué : ") )
        attaquant = lesPersonnages[numAttaquant]
        attaque = lesPersonnages[numAttaque]
        # Gestion de l'attaque
        attaquant.attaque(attaque)
        print("       ", attaquant.nom, "(a", attaquant.vie, "vie.s), a attaqué", attaque.nom, "(qui n'a plus que", attaque.vie, "vie.s)")