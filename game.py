from casino import *




players = []
players.append(Player("Lars"))
players.append(Player("Max"))

deck = create_deck()

for card in deck[0:4:]:
    players[0].hand += [card]

for card in deck[4:8:]:
    players[1].hand += [card]





for card in players[0].hand:
   print(card.return_card())
 


move_to_center(players[0], 3, centerPile)

print('----------------------')

print(center[0].pile[0].return_card())

print('----------------------')

for card in players[0].hand:
   print(card.return_card())

moveFromCenter(players[0], 0)

print('----------------------')

print(players[0].discard[0].return_card())