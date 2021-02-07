from casino import *



players = []
players.append(Player("Lars"))
players.append(Player("Max"))

deck = create_deck()

for card in deck[0:26:]:
    players[0].discard += [card]

for card in deck[26:53:]:
    players[1].discard += [card]



compare_players(players)

for player in players:
    player.show_points();


# firstCard = players[0].discard[0]
# secondCard = players[0].discard[1]



# builtCard = firstCard + secondCard

# second = secondCard + builtCard + firstCard

# print(firstCard.builtValue, 
# secondCard.builtValue,
# builtCard.builtValue, second.builtValue)
