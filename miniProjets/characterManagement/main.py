class Personnage :
    # Constructeur
    def __init__(self, nom) :
        self._nom = nom # Les propriétés précédés d'un underscore ne sont pas directement accessibles, c'est une protection illusoir, mais ça permet de garder un code propre
    # Attaqque un personnage
    def attaque(self, unPersonnage) :
        if isinstance(unPersonnage, Mortel) :
            unPersonnage.diminueVie(2) # Pas de chiffre en () si diminueVie était initialisé à 2, ici, je met 2
        if isinstance(self, Mortel) :
            self.augmanterVie()
    # Getter sur le nom
    def _getNom(self):
        return self._nom
    # affectation du getter
    nom = property(_getNom) # pseudo propriété

# Classe Mortel
class Mortel(Personnage) : # Hérite de tout le contenu de la classe mère
    def __init__(self, nom):
        Personnage.__init__(self, nom)
        self._vie = 5
    # Augmentation de vie
    def augmanterVie(self, vieEnPlus = 1):  # s'il n'y a pas `=1`, alors 1 en plus par défaut
        self._vie += vieEnPlus
    # Diminution de vie en évitant d'être inférieur à 0
    def diminueVie(self, vieEnMoins = 1):
        self._vie = max(0, self._vie - vieEnMoins)
    # Getter sur la vie
    def _getVie(self):
        return self._vie
    vie= property(_getVie)

# Classe immortels
class Immortel(Personnage) :
    def __init__(self, nom, pouvoir):
        Personnage.__init__(self, nom)
        self._pouvoir = pouvoir
    def _getPouvoir(self):
        return self._pouvoir
    pouvoir = property(_getPouvoir)

# Fonction d'affichage des personnages
def affichePersonnages(lesPersonnages) :
    for k, unPersonnage in enumerate(lesPersonnages):
        if isinstance(unPersonnage, Mortel) :
            print("       ", k, ":", unPersonnage.nom, "a", unPersonnage.vie, "vie.s")
        else :
            print("       ", k, ":", unPersonnage.nom, "a", unPersonnage.pouvoir,)



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
        type = input("        Est-il mortel (M) ou immortel (I) ? ")
        if type == "I" :
            pouvoir = input("        Son pouvoir est                  : ")
            nouveau = Immortel(nom, pouvoir)
        else :
            nouveau = Mortel(nom)
        lesPersonnages.append(nouveau) # append est utilisable car la taille de la liste n'est pas définie
    elif choix == "2" :
        # affichier la liste des personnages
        affichePersonnages(lesPersonnages)
        # Choix de l'attaquant et de l'attaqué
        numAttaquant = int(input("        N° de l'attaquant                : ") )
        numAttaque = int(input("        N° de l'attaqué                  : ") )
        attaquant = lesPersonnages[numAttaquant]
        attaque = lesPersonnages[numAttaque]
        # Gestion de l'attaque
        attaquant.attaque(attaque)
        # Liste des personnages
        affichePersonnages(lesPersonnages)