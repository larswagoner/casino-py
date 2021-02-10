from casino import *


# 1. Create deck, and players
# 2. Game play, big ol while loop
# 3. Compare players
# 4. Print winner





def setup():
    deck = create_deck()
    players = []

    numPlayers = int(input('Enter how many players: '))
    for i in range(numPlayers):
        playername = input('Enter your name: ')
        players.append(Player(playername))
    
    return deck, players

def playersTurn(player):
    action = input('Enter the command (play, build, collect, take) and the corresponding indices: ')

    while "end" not in action:

        if 'play' in action:
            play, card = action.split()
            move_to_center(player, int(card))

        elif 'build' in action:
            build, pileOne, pileTwo = action.split()
            center.buildCards(int(pileOne), int(pileTwo), player)

        elif 'collect' in action:
            collect, cardOne, cardTwo = action.split()
            center.collectCards(int(cardOne), int(cardTwo))

        elif 'take' in action:
            take, pile = action.split()
            moveFromCenter(player, int(pile))

        testPrint(player, center.pile)
        action = input('Enter the command (play, build, collect, take) and the corresponding indices: ')


deck, players = setup()

count = 0;




# Game loop
while deck:
    if count % (4 * len(players)) == 0:# and players[-1].hand:
        dealCards(deck, players)

    player = players[count % len(players)]

    
    for pile in center.pile:
        for card in pile.pile:
            card.wasLastPlayed = False
    

    playersTurn(player, center.pile)

    count += 1


