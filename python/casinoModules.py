import os


class Print:
    def __init__(self):
        self.whoreVar = "you cant do that you sneaky whore"
        self.buckarooVar = "slow down there buckaroo"
        self.erorVar = "there was an error"
        self.eror2Var = "you typed an invalid command or just play a goddamn card"
        self.neinVar = "NEIN"
        self.endVar = "ye fookin done"
        

    def whore(self, name):
        print(name + ", " + self.whoreVar)
        os.system("say " + name + ", " + self.whoreVar )

    def buckaroo(self, name):
        print(name + ", " + self.buckarooVar)
        os.system("say " + name + ", " + self.buckarooVar )

    def eror(self, name):
        print(name + ", " + self.erorVar)
        os.system("say " + name + ", " + self.erorVar )

    def eror2(self, name):
        print(name + ", " + self.eror2Var)
        os.system("say " + name + ", " + self.eror2Var )

    def nein(self, name):
        print(name + ", " + self.neinVar)
        os.system("say " + name + ", " + self.neinVar)

    def end(self, name):
        print(name + ", " + self.endVar)
        os.system("say " + name + ", " + self.endVar)


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
    
    def handToDiscard(self, indexOne):
        # print(self.hand.pop(indexOne])
        self.discard.append(self.hand.pop(indexOne))


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
        temp = False
        newBuiltValue = (self.pile[indexOne].builtValue + self.pile[indexTwo].builtValue)
        for i in range(len(player.hand)):
            if newBuiltValue == player.hand[i].value:
                temp = True
                break

        if self.pile[indexOne].isBuilt and self.pile[indexTwo].isBuilt and temp:
            for i in range(len(self.pile[indexOne].pile)):
                self.pile[indexTwo].pile.append(self.pile[indexOne].pile.pop(0))

        
            self.pile[indexTwo].builtValue = newBuiltValue
            self.pile[indexTwo].collectValue = newBuiltValue
            self.pile.pop(indexOne)
        else:
            print("NEIN")
        

    def collectCards(self, indexOne, indexTwo):
        if self.pile[indexOne].collectValue == self.pile[indexTwo].collectValue:
            for i in range(len(self.pile[indexOne].pile)):
                self.pile[indexTwo].pile.append(self.pile[indexOne].pile.pop(0))

            self.pile[indexTwo].isBuilt = False
            self.pile.pop(indexOne)
        else:
            print("NEIN")
            # say.nein(player.name)


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.builtValue = value 
        self.wasLastPlayed = False #at the end of each turn, all of the .wasLastPlayed values should be set to False

    def return_card(self):
        return self.suit, self.value
