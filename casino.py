import random

class Player:
    def __init__(self, name):
        self.hand = []
        self.discard = []
        self.cards = 0
        self.spades = 0
        self.aces = 0
        self.smallCasino = 0
        self.bigCasino = 0
        self.cardWinner = False
        self.spadesWinner = False
        self.points = 0
        self.playerName = name
    
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



class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

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
        for pile in table[0::2]:
            pile.append(deck.pop(0))
            pile.append(deck.pop(0))

    return table

# def move_card(card, from_pile, to_pile):


def compare_players(players):
    cardList = []
    spadesList = []
    lastPlayerCards = 0
    lastPlayerSpades = 0
    
    for player in players:
        playerCards, playerSpades = player.count()
        cardList.append(playerCards)
        spadesList.append(playerSpades)
    

    cardWinner = players[cardList.index(max(cardList))]
    spadesWinner = players[spadesList.index(max(spadesList))]

    cardWinner.points += 3 
    spadesWinner.points += 1

    # for player in players:
    #     playerCards, playerSpades = player.count()
    #     print(playerCards, playerSpades)
        
    #     if playerCards > lastPlayerCards:
    #         winnerCards = player
    #     elif playerCards == lastPlayerCards:
    #         winnerCards.cardWinner = False

    #     if playerSpades > lastPlayerSpades:
    #         winnerSpades = player
    #     elif playerSpades == lastPlayerSpades:
    #         winnerSpades.spadeWinner = False
            


    for player in players:
        if player.cardWinner == True:
            player.points += 3
        if player.spadesWinner == True:
            player.points += 1




# def declare_winner(players):
    
