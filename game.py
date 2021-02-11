from casino import *


# 1. Create deck, and players
# 2. Game play, big ol while loop
# 3. Compare players
# 4. Print winner

# Game loop


while deck:
    if count % (4 * len(players)) == 0 and len(players[-1].hand) == 0:
        dealCards(deck, players)

    player = players[count % len(players)]

    
    for pile in center.pile:
        for card in pile.pile:
            card.wasLastPlayed = False
    
    try:
        playersTurn(player)
    except:
        print("---------there was an error---------")


    count += 1

compare_players(players)

for player in players:
    player.show_points()
