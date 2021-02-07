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

center = []

class Center:
    def __init__(self):
        self.


class CenterPile:
    def __init__(self):
        self.pile = [] #to append cards to centerPile we must append to centerPile.pile
        self.builtValue = 0
        self.isBuilt = True
        self.isCollect = False
    
    def create_empty_builtPile(self):
        center.append(self)
    
    def collectCards(indexOne, )

    
def move_to_center(player, indexCard, centerPile):
    centerPile.create_empty_builtPile()
    center[-1].pile.append(player.hand.pop(indexCard))

def moveFromCenter(player, indexCenterPile): #this should be in an if centerPile.isCollect == True statement.
    if center[indexCenterPile].isCollect:
        for indexCard in range(len(center[indexCenterPile].pile)):
            player.discard.append(center[indexCenterPile].pile.pop(indexCard))
        center.pop(indexCenterPile)
    else:
        print()


    
    
centerPile = CenterPile()

# class BuiltPile(CenterPile):
#     def __init__(self):
#         super().__init__


        
    
# class CollectPile(CenterPile):
#     def __init__(self):
#         super().__init__
        
    




class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.builtValue = value #maybe a way we can build cards while preserving the original suit and value

    def return_card(self):
        return self.suit, self.value

    def __add__(self, other):
        self.builtValue += other.builtValue
        return self



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
            

def prettyPrint(players, center):
    for p in players:
        print(f"Player: {p.playerName}")
        print(f"    Hand:")
        for c in p.hand:
            print(f"        {c.value} of {c.suit}")
        print(f"    Discard:")
        for c in p.discard:
            print(f"        {c.value} of {c.suit}")
        
    

