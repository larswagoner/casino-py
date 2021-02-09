import random

class Player:
    def __init__(self, name):
        self.playerName = name
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
        self.pile = [] #to append cards to centerPile we must append to centerPile.pile
        self.builtValue = 0 
        self.collectValue = self.builtValue
        self.isBuilt = True
    


class Center:
    def __init__(self):
        self.pile = []
        

    def buildCards(self, indexOne, indexTwo, player):
        temp = False
        newBuiltValue = (center.pile[indexOne].builtValue + center.pile[indexTwo].builtValue)
        for i in range(len(player.hand)):
            if newBuiltValue == player.hand[i].value:
                temp = True
                break
            
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
            for i in range(len(center.pile[indexOne])):
                self.pile[indexTwo].append(self.pile[indexOne].pop(0))

            self.pile.pop(indexOne)
            self.pile[indexTwo].isBuilt = False
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


center = Center()



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



def deal_to_player(deck, player, numCards):
    for i in range(numCards):
            player.hand.append(deck.pop(0))



def dealCards(deck, players):
    if deck:
        if len(deck) == 52:
                for player in players:
                    deal_to_player(deck, player, 2)
                deal_to_center(deck, 4)

        else:
            for player in players:
                    deal_to_player(deck, player, 2)
    else: 
        print('This round has ended')



def move_to_center(player, indexCard):
    center.pile.append(CenterPile())
    
    center.pile[-1].pile.append(player.hand.pop(indexCard))
    center.pile[-1].builtValue += center.pile[-1].pile[0].builtValue
    center.pile[-1].pile[0].wasLastPlayed = True



def moveFromCenter(player, indexCenterPile):
    temp = False
    for card in center.pile[indexCenterPile].pile:
        if card.wasLastPlayed:
            temp = True
            break
        
    if not center.pile[indexCenterPile].isBuilt and temp:
        for indexCard in range(len(center.pile[indexCenterPile].pile)):
            player.discard.append(center.pile[indexCenterPile].pile[indexCenterPile])
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
            


def prettyPrint(players, centerList):
    for p in players:
    
        print(f"Player: {p.playerName}")
        print(f"    Hand:")
        for card in p.hand:
            print(f"        {card.value} of {card.suit}")
        print(f"    Discard:")
        for discardCard in p.discard:
            print(f"        {discardCard.value} of {discardCard.suit}")
        print(f"-----------------------------")
    
    print("Center:")
    for pile in centerList:
        print("    Pile:")
        for c in pile.pile:
            print(f"        {c.value} of {c.suit}")
    print("#################################")