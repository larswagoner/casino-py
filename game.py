from casino import *


# 1. empty builtpile
# 2. pop a card from player hand -> created builtpile 




players = []
players.append(Player("Lars"))
players.append(Player("Max"))



deck = create_deck()


for player in players:
    for i in range(4):
        player.hand.append(deck.pop(0))

prettyPrint(players, center.pile)

move_to_center(players[0], 0)
move_to_center(players[0], 2)

prettyPrint(players, center.pile)

center.pile[0].isBuilt = False
moveFromCenter(players[0], 0)

prettyPrint(players, center.pile)

compare_players(players)

for player in players:
    player.show_points()