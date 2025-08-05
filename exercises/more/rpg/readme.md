# **🎮 Jeu de role**<a href="../../../"><img align="right" src="../../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
Avec ce jeu de rôle très basique vous combattez un ennemi dans le terminal.  
L'intérêt de ce projet est d'utiliser plusieurs concepts de programmation de base pour créer une expérience de jeu interactive.
## 📋 Description
Vous incarnerez un héros combattant un ennemi. Vous pourrez attaquer, utiliser des potions pour vous soigner, et subir les attaques de l'ennemi. Le jeu s'arrête quand l'un est vaincu.
## 🛠️ Concepts Utilisés
- **Variables et initialisation** : Utilisation de variables pour suivre les points de vie, les potions, etc.
- **Boucles** : Utilisation d'une boucle `while` pour faire tourner le jeu jusqu'à ce qu'une condition de fin soit atteinte.
- **Structures conditionnelles** : Utilisation de `if`, `elif`, et `else` pour gérer les différentes actions et états du jeu.
- **Saisie de l'utilisateur** : Utilisation de `input()` pour permettre au joueur de choisir ses actions.
- **Module `random`** : Pour générer des valeurs aléatoires pour les attaques et les potions.
- **Opérations mathématiques** : Calcul des dégâts d'attaque et des points de vie restaurés par les potions.
- **Affichage d'informations avec les f-strings** : Pour afficher dynamiquement les informations du jeu.
- **Instructions de contrôle de flux** : Utilisation de `continue` pour sauter des itérations de boucle sous certaines conditions.

## 🚀 Comment Jouer
1. Avoir Python.
2. Téléchargez le fichier du jeu.
3. Ouvrez un terminal et naviguez jusqu'au répertoire contenant le fichier du jeu.
4. Exécutez le fichier avec la commande `python main.py`.
## 🎮 Commandes du Jeu
- **Attaquer** ·················· Touche <kbd>1</kbd>.
- **Boire la potion 🍾** ··· Touche <kbd>2</kbd>.
## 🎯 Règles du Jeu
- Tu commences avec 100 points de vie et 3 potions.
- L'ennemi commence également avec 100 points de vie et un nombre aléatoire de potions (max. 3).
- Chaque attaque inflige des dégâts aléatoires entre 10 et 20 points de vie.
- Les potions restaurent un nombre aléatoire de points de vie entre 15 et 30.
- Si tu utilises une potion, l'ennemi ne t'attaquera pas pendant ce tour.
- L'ennemi utilise une potion s'il a moins de 50 points de vie et s'il lui reste des potions.
- Le jeu se termine lorsque l'un n'a plus de points de vie.