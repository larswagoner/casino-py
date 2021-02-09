from casino import *


# 1. empty builtpile
# 2. pop a card from player hand -> created builtpile 




players = []
players.append(Player("Lars"))
players.append(Player("Max"))



deck = create_deck()

dealCards(deck, players)

dealCards(deck, players)
dealCards(deck, players)
dealCards(deck, players)
dealCards(deck, players)
dealCards(deck, players)
dealCards(deck, players)
dealCards(deck, players)



center.buildCards(0, 1, players[0])

prettyPrint(players, center.pile)

