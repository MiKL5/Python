# Écrir un petit programme pour distribuer les cartes pour une partie de Texas Hold’em.

import itertools
import random

# Prese en compte des cartes et des joueurs
def deal(cards, number_of_players):
    deck = shuffle_deck(cards)
    deal_to_players(deck, number_of_players)
    deal_to_table(deck)


# Piocher des cartes
def deal_to_players(deck, number_of_players):
    first_cards = [next(deck)  for _ in  range(number_of_players)]
    second_cards = [next(deck)  for _ in  range(number_of_players)]
    hands = zip(first_cards, second_cards) # reçoit une cate à la fois en deux tours
    # print()
    for i,  (first_card, second_card)  in  enumerate(hands, start=1):
        print(f"Le joueur {i} a reçu : {first_card} et {second_card}")
    print()


# Distribution des cartes
def deal_to_table(deck):
    next(deck)  # bruler un carte
    flop = ', '.join(str(next(deck))  for _ in  range(3))
    print(f"Le flop: {flop}")
    next(deck)  # bruler une carte
    print(f"La turn: {next(deck)}")
    next(deck)  # bruler un cate
    print(f"La river: {next(deck)}\n")


def get_players():
    while True:
        number_of_players = input("Combien y a-t-il de joueurs ? ").strip()
        try:
            number_of_players = int(number_of_players)
        except ValueError:
            print("Vous devez saisir un entier.")
        else:
            if number_of_players in range(2, 11): # Deux à 10 joueurs
                return number_of_players
            elif number_of_players < 2:
                print("Vous devez avoir au moins 2 joueurs.")
            else:
                print("Vous pouvez avoir un maximum de 10 joueurs.")


# Mélanger le jeu de carte
def shuffle_deck(cards):
    deck = list(cards)
    cards = print(f"\nLe jeu comporte {len(deck)} cartes.\n" ) # Vérifier le nombre de carte
    random.shuffle(deck) # Mélange les cartes
    return iter(deck)

# Jeu de carte
ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "reine", "roi", "as")
suits = ("trèfle", "carreau", "cœur", "pique")

cards = list(itertools.product(ranks, suits))

deal(cards, get_players())