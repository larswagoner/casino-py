import random


# center, discard - odd, hand - even
def create_table(num_players):
    table = [[]]
    for player in range(1, num_players+1):
        table += [[], []]

    return table


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.builtValue = value

    def return_card(self):
        return self.suit, self.value
    
    def __add__(self, other):
        self.builtValue += other.builtValue
        return self






def create_deck():
    suits = ['spade', 'clubs', 'diamonds', 'hearts']
    deck = []
    for suit in suits:
        for value in range(1, 14):
            deck.append(Card(suit, value))

    random.shuffle(deck)

    return deck


table = create_table(2)
deck = create_deck()


def deal_round_one(table, deck):
    for number in range(0,2):
        for pile in table[0::2]:
            pile.append(deck.pop(0))
            pile.append(deck.pop(0))

    return table


def place_card(to_pile, card, from_pile):
    table[to_pile].append(table[from_pile].pop(card % len(table[from_pile])))


table = deal_round_one(table, deck)


for pile in table:
    for card in pile:
        print(card.return_card())
    print('--------------')

place_card(1, 28, 2)

print('AAAAAAAAAAA')
for pile in table:
    for card in pile:
        print(card.return_card())
    print('--------------')