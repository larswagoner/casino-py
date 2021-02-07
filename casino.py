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
        
    def showPoints(self):
        print(self.points)


class CenterPile:
    def __init__(self):
        self.pile = [] #to append cards to centerPile we must append to centerPile.pile
        self.builtValue = 0 
        self.collectValue = self.builtValue
        self.isBuilt = True
    
    def add_empty_pile(self):
        center.list.append(self)


class Center:
    def __init__(self):
        self.list = []
        # for i in range(4):
        #     self.list.append(CenterPile())

    def buildCards(indexOne, indexTwo, player):
        temp = False
        newBuiltValue = (center.list[indexOne].builtValue + center.list[indexTwo].builtValue)
        for i in range(len(player.hand)):
            if newBuiltBV == player.hand[i].value:
                temp = True
                break
            
        if center.list[indexOne].isBuilt and center.list[indexTwo].isBuilt and temp:
            for i in range(len(center.list[indexOne])):
                self.list[indexTwo].append(self.list[indexOne].pop(0))

            self.list.pop(indexOne)
            self.list[indexTwo].builtValue = newBuiltValue
        else:
            print("NEIN")
        
    def collectCards(indexOne, indexTwo):
        if self.list[indexOne].collectValue == self.list[indexTwo].collectValue:
            for i in range(len(center.list[indexOne])):
                self.list[indexTwo].append(self.list[indexOne].pop(0))

            self.list.pop(indexOne)
            self.list[indexTwo].isBuilt = False
        else:
            print("NEIN")



center = Center()
    
centerPile = CenterPile()
    
def move_to_center(player, indexCard, centerPile):
    centerPile.add_empty_pile()
    
    
    print(center.list[-1])
    center.list[-1].pile.append(player.hand.pop(indexCard))
    center.list[-1].builtValue += center.list[-1].pile[0].builtValue

def deal_to_center(deck, numCards, centerPile):
    for i in range(numCards):
        centerPile.add_empty_pile()
        center.list[-1].pile.append()

    
    # center.list[-1].pile.append(player.hand.pop(indexCard))
    # center.list[-1].builtValue += center.list[-1].pile[0].builtValue



def moveFromCenter(player, indexCenterPile):
    if not center.list[indexCenterPile].isBuilt:
        for indexCard in range(len(center.list[indexCenterPile].pile)):
            print(center.list[indexCenterPile].pile[indexCard].return_card())
        # center.list.pop(indexCenterPile)
    else:
        print("noo")


# def moveFromCenter(player, indexCenterPile): #this should be in an if centerPile.isCollect == True statement.
#     if center.list[indexCenterPile].isBuilt:
#         # print("JA")
#         print(range(len(center.list[indexCenterPile].pile)))
#         for indexCard in range(len(center.list[indexCenterPile].pile)):
#             player.discard.append(center.list[indexCenterPile].pile.pop(indexCard))
#         center.list.pop(indexCenterPile)
#     else:
#         print('NEIN')


center = Center()
    
centerPile = CenterPile()

    




class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.builtValue = value #maybe a way we can build cards while preserving the original suit and value

    def return_card(self):
        return self.suit, self.value




def create_deck():
    suits = ['spades', 'clubs', 'diamonds', 'hearts']
    deck = []
    for suit in suits:
        for value in range(1, 14):
            deck.append(Card(suit, value))
    random.shuffle(deck)
    return deck


def deal_round_one(table, deck):
    for number in range(0,2):
        if len(deck) == 52:
            for pile in table[0::2]:
                pile.append(deck.pop(0))
                pile.append(deck.pop(0))
        else:
            for pile in table[1::2]:
                pile.append(deck.pop(0))
                pile.append(deck.pop(0))

    return table


# def move_card(card, from_pile, to_pile):


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
        print(f"-----------------------------")
        print(f"Player: {p.playerName}")
        print(f"    Hand:")
        for card in p.hand:
            print(f"        {card.value} of {card.suit}")
        print(f"    Discard:")
        for discardCard in p.discard:
            print(f"        {discardCard.value} of {discardCard.suit}")
    
    print("Center:")
    for pile in centerList:
        print("    Pile:")
        for c in pile.pile:
            print(f"        {c.value} of {c.suit}")
    print("#################################")

