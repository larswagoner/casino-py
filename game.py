from casino import *



players = []
players.append(Player("Lars"))
players.append(Player("Max"))

deck = create_deck()

for card in deck[0:5:]:
    players[0].discard += [card]

for card in deck[6:52:]:
    players[1].discard += [card]






# players[0].cards = 5
# players[0].spades = 6
# players[0].aces = 2

# players[1].cards = 2
# players[1].spades = 16
# players[1].aces = 0

compare_players(players)

for player in players:
    player.show_points();
