from casino import *

players = []
players.append(Player("Lars"))
players.append(Player("Max"))



deck = create_deck()


deal_to_center(deck,3)

deal_to_player(deck, players[0], 1)
players[0].hand[0].value = 7
players[0].hand[0].builtValue = 7


center.pile[0].pile[0].value = 3
center.pile[0].builtValue = 3
center.pile[1].pile[0].value = 4
center.pile[1].builtValue = 4
center.pile[2].pile[0].value = 7
center.pile[2].builtValue = 7
center.pile[2].collectValue = 7

center.buildCards(0, 1, players[0])
center.collectCards(0, 1)



move_to_center(players[0], 0)

center.collectCards(0, 1)


moveFromCenter(players[0], 0)

prettyPrint(players, center.pile)
compare_players(players)

for player in players:
    player.show_points()

