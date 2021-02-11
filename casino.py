import random
import sys

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.discard = []
        self.cards = 0
        self.spades = 0
        self.aces = 0
        self.smallCasino = 0
        self.bigCasino = 0
        self.points = 0
        
    def show_points(self):
        print(self.points)
    
    def count(self):
        self.cards = len(self.discard)
        for card in self.discard:
            if card.suit == 'spades' : self.spades += 1 
            if card.value == 1 : self.aces += 1 
            if card.suit == 'spades' and card.value == 2 : self.smallCasino = 1 
            if card.suit == 'diamonds' and card.value == 10 : self.bigCasino = 2 
        
        self.points += (self.aces + self.smallCasino + self.bigCasino)
        return self.cards, self.spades



class CenterPile:
    def __init__(self):
        self.pile = [] 
        self.builtValue = 0 
        self.collectValue = self.builtValue
        self.isBuilt = True
    


class Center:
    def __init__(self):
        self.pile = []
        

    def buildCards(self, indexOne, indexTwo, player):
        print("in buildCards")
        temp = False
        newBuiltValue = (center.pile[indexOne].builtValue + center.pile[indexTwo].builtValue)
        for i in range(len(player.hand)):
            if newBuiltValue == player.hand[i].value:
                temp = True
                print("TESTICLES")
                break
        
        print("TESTIES")
        if center.pile[indexOne].isBuilt and center.pile[indexTwo].isBuilt and temp:
            for i in range(len(center.pile[indexOne].pile)):
                self.pile[indexTwo].pile.append(self.pile[indexOne].pile.pop(0))

        
            self.pile[indexTwo].builtValue = newBuiltValue
            self.pile[indexTwo].collectValue = newBuiltValue
            self.pile.pop(indexOne)
        else:
            print("NEIN")
        

    def collectCards(self, indexOne, indexTwo):
        if self.pile[indexOne].collectValue == self.pile[indexTwo].collectValue:
            for i in range(len(center.pile[indexOne].pile)):
                self.pile[indexTwo].pile.append(self.pile[indexOne].pile.pop(0))

            self.pile[indexTwo].isBuilt = False
            self.pile.pop(indexOne)
        else:
            print("NEIN")



class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.builtValue = value 
        self.wasLastPlayed = False #at the end of each turn, all of the .wasLastPlayed values should be set to False

    def return_card(self):
        return self.suit, self.value



##################
##################
#GLOBAL FUNCTIONS#
##################
##################






def create_deck():
    suits = ['spades', 'clubs', 'diamonds', 'hearts']
    deck = []
    for suit in suits:
        for value in range(1, 14):
            deck.append(Card(suit, value))
    random.shuffle(deck)
    return deck



def deal_to_center(deck, numCards):
    for i in range(numCards):
        center.pile.append(CenterPile())
        center.pile[-1].pile.append(deck.pop(0))
        center.pile[-1].builtValue = center.pile[-1].pile[0].builtValue
        center.pile[-1].collectValue = center.pile[-1].pile[0].builtValue



def deal_to_player(deck, player, numCards):
    for i in range(numCards):
            player.hand.append(deck.pop(0))



def dealCards(deck, players):
    if deck:
        if len(deck) == 52:
                for i in range(2):
                    for player in players:
                        deal_to_player(deck, player, 2)
                deal_to_center(deck, 4)

        else:
            for i in range(2):
                    for player in players:
                        deal_to_player(deck, player, 2)
    else: 
        print('This round has ended')



def move_to_center(player, indexCard):
    center.pile.append(CenterPile())
    
    center.pile[-1].pile.append(player.hand.pop(indexCard))
    center.pile[-1].builtValue += center.pile[-1].pile[0].builtValue
    center.pile[-1].collectValue += center.pile[-1].pile[0].builtValue
    center.pile[-1].pile[0].wasLastPlayed = True
    center.pile[-1].pile[0].isBuilt = True



def moveFromCenter(player, indexCenterPile):
    temp = False
    print('Aloha', indexCenterPile)
    for card in center.pile[indexCenterPile].pile:
        print('continue on soldier')
        if card.wasLastPlayed:
            temp = True
           
            break

    if not center.pile[indexCenterPile].isBuilt and temp:
        print("aloha from inside if")

        while center.pile[indexCenterPile].pile: #range(len(center.pile[indexCenterPile].pile)):
            player.discard.append(center.pile[indexCenterPile].pile.pop(0))
        center.pile.pop(indexCenterPile)
    else:
        print("NEIN")



def compare_players(players):
    cardList = []
    spadesList = []
  
    for player in players:
        playerCards, playerSpades = player.count()
        cardList.append(playerCards)
        spadesList.append(playerSpades)
    
    highestCards = [total for total in cardList if total == max(cardList)]
    highestSpades = [total for total in spadesList if total == max(spadesList)]

    if len(highestCards) == 1:
        cardWinner = players[cardList.index(max(cardList))]
        cardWinner.points += 3 
    
    if len(highestSpades) == 1:
        spadesWinner = players[spadesList.index(max(spadesList))]
        spadesWinner.points += 1
            

def setup():
    players = []
    deck = create_deck()
    # center = Center()
    count = 0

    numPlayers = int(input('Enter how many players: '))
    for i in range(numPlayers):
        playername = input('Enter your name: ')
        players.append(Player(playername))
    
    return players, deck, count

players, deck, count = setup()

center = Center()

def playersTurn(player):
    testPrint(player, center.pile)
    action = input('Enter the command (play, build, collect, take) and the corresponding indices: ')

    temp = 0
    isRunning = True

    try:
        while isRunning: 

            if 'end' in action and temp < 1:
                print("don't end before playing you sneaky whore")
            elif 'end' in action and  temp == 1:
                isRunning = False
                break

            if 'play' in action:
                if temp > 1:
                    print('you cant do that you sneaky whore')
                    break
                play, card = action.split()
                if int(card) > (len(player.hand) - 1):
                    print("range error, try again!")
                else:
                    move_to_center(player, int(card))
                    temp += 1
            elif 'build' in action:
                build, pileOne, pileTwo = action.split()
                if (abs(int(pileOne)) or abs(int(pileTwo))) > (len(center.pile) - 1):
                    print('slow down there buckaroo...')
                else:
                    center.buildCards(int(pileOne), int(pileTwo), player)

            elif 'collect' in action:
                collect, pileOne, pileTwo = action.split()
                if (abs(int(pileOne)) or abs(int(pileTwo))) > (len(center.pile) - 1):
                    print('slow down there buckaroo...')
                else:
                    center.collectCards(int(pileOne), int(pileTwo))

            elif 'take' in action:
                take, pile = action.split()
                if abs(int(pile)) > (len(center.pile) - 1):
                    print('slow down there buckaroo...')
                else:
                    moveFromCenter(player, int(pile))
            
            else:
                print('invalid command or play a goddamn card')

            testPrint(player, center.pile)
            action = input('Enter the command (play, build, collect, take) and the corresponding indices: ')
    except:
        print(sys.exc_info()[0])
        print("ye fookin done")

    print("Next person's turn...")



def prettyPrint(players, centerList):
    for p in players:
    
        print(f"Player: {p.name}")
        print(f"    Hand:")
        for card in p.hand:
            print(f"        {card.value} of {card.suit}")#". %d" % card.builtValue)
        print(f"    Discard:")
        for discardCard in p.discard:
            print(f"        {discardCard.value} of {discardCard.suit}")
        print(f"-----------------------------")
    
    print("Center:")
    for pile in centerList:
        print("    Pile:")# % pile.builtValue)
        for c in pile.pile:
            print(f"        {c.value} of {c.suit}")
    print("#################################")

def testPrint(player, center):
    print(f"{player.name}'s Cards: ")
    for card in player.hand:
        print(f"        {card.value} of {card.suit}")
    print('There are %d cards in the discard pile.' % len(player.discard))
    print("Center:")
    for pile in center:
        print(f"    Pile: Collect: {pile.collectValue}. Build: {pile.builtValue}.") # % pile.builtValue)
        for card in pile.pile:
            print(f"        {card.value} of {card.suit}")




##################
##################
#####GAME.PY######
##################
##################


while count < 2:
    if count % (4 * len(players)) == 0 and len(players[-1].hand) == 0:
        dealCards(deck, players)

    player = players[count % len(players)]

    
    for pile in center.pile:
        for card in pile.pile:
            card.wasLastPlayed = False
    
    try:
        playersTurn(player)
    except:
        print(sys.exc_info()[0])
        print("---------there was an error---------")


    count += 1

print('done wit game')
compare_players(players)
print('done wit comparision only leads to sadness')
for player in players:
    player.show_points()
