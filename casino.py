import random

class Player:
    def __init__(self):
        self.hand = []
        self.points = 0
    
    def show(self):
        print("test")

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def return_card(self):
        return self.suit, self.value

def create_deck():
    suits = ['spade', 'clubs', 'diamonds', 'hearts']
    deck = []
    for suit in suits:
        for value in range(1, 14):
            deck.append(Card(suit, value))
    random.shuffle(deck)
    return deck



def printTable(player):
    