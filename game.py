from casino import *





players = []
players.append(Player("Lars"))
players.append(Player("Max"))



deck = create_deck()

for card in deck[10:14:]:
    players[0].hand += [card]

for card in deck[4:8:]:
    players[1].hand += [card]

deal_to_center(deck, 4, centerPile)


prettyPrint(players, center.list)




# move_to_center(players[0], 0, centerPile)
# move_to_center(players[0], 1, centerPile)
# # move_to_center(players[0], 2, centerPile)
# prettyPrint(players, center.list)
# moveFromCenter(players[0], 0)
# moveFromCenter(players[0], 1)
# # moveFromCenter(players[0], 2)
# prettyPrint(players, center.list)


