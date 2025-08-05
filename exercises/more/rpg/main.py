import random


# Demander le nom de l'utilisateur
user_name      = input("Bonjour ! Quel est ton nom ? 👉 ")

player_hp      = 100
enemy_hp       = 100
player_potions = 3
enemy_potions  = random.randint(1, 3)  # L'ennemi a un nombre aléatoire de potions

# Boucle principale 
while player_hp > 0 and enemy_hp > 0:
    # affichage des informations
    print(f"""\n{user_name}, tu as {player_hp} points de vie et {player_potions} potions.
L'ennemi a {enemy_hp} points de vie et {enemy_potions} potions.\n""")

    # actions du joueur
    action = input("Que veux-tu faire ?\n1. Attaquer 💣\n2. Utiliser une potion 🍾\n👉 ")

    if action == "1":
        # les dégats du joueur sont recalculés à chaque tour
        player_attack = random.randint(10, 20)
        enemy_hp -= player_attack
        print(f"\n🦸 Tu as infligé à l'ennemi {player_attack} dégâts. 🚒")

        # Tour de l'ennemi
        enemy_attack = random.randint(10, 20)
        player_hp -= enemy_attack
        print(f"🦹 L'ennemi t'a infligé {enemy_attack} dégâts. 🚒")

    elif action == "2":
        # Le joueur boie une potion
        if player_potions > 0:
            potion_heal = random.randint(15, 30)  # Restaure un nombre aléatoire de points de vie
            player_hp += potion_heal
            player_potions -= 1
            print(f"\n✅ Tu as récupéré {potion_heal} points de vie. 💪")
        else:
            print("⚠️ Tu n'as plus de potions.")

    else:
        print("❌ Tu as mal saisie.")
        continue  # L'ennemi n'attaque pas si l'action est invalide

    # l'ennemi utilise une potion
    if enemy_hp < 50 and enemy_potions > 0:
        potion_heal = random.randint(15, 25)
        enemy_hp += potion_heal
        enemy_potions -= 1
        print(f"\n🍾 Grâce à la potion, l'ennemi a récupéré {potion_heal} points de vie.")

    # vérifications
    if player_hp <= 0:
        print("😭 Domage ! Tu as été vaincu ⚰️")
        break
    elif enemy_hp <= 0:
        print("🏆 Félicitations ! Tu as vaincu l'ennemi !")
        break

print("\nLe jeu est terminé 👋\nReviens quand tu veux.") # Fin