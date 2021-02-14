import random
import sys
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
        
say = Print()



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
            for i in range(len(center.pile[indexOne].pile)):
                self.pile[indexTwo].pile.append(self.pile[indexOne].pile.pop(0))

            self.pile[indexTwo].isBuilt = False
            self.pile.pop(indexOne)
        else:
            say.nein()



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



def move_to_center(player, indexCard):
    center.pile.append(CenterPile())
    
    center.pile[-1].pile.append(player.hand.pop(indexCard))
    center.pile[-1].builtValue += center.pile[-1].pile[0].builtValue
    center.pile[-1].collectValue += center.pile[-1].pile[0].builtValue
    center.pile[-1].pile[0].wasLastPlayed = True
    center.pile[-1].pile[0].isBuilt = True



def moveFromCenter(player, indexCenterPile):
    temp = False
    for card in center.pile[indexCenterPile].pile:
        if card.wasLastPlayed:
            temp = True
           
            break

    if not center.pile[indexCenterPile].isBuilt and temp:
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

    print(highestCards, highestSpades)

    if len(highestCards) == 1:
        cardWinner = players[cardList.index(max(cardList))]
        cardWinner.points += 3 
    
    if len(highestSpades) == 1:
        spadesWinner = players[spadesList.index(max(spadesList))]
        spadesWinner.points += 1
            

def check_commands(player, commands, num):
    if(len(commands)-1 != num):
        say.eror(player.name)
        return False
    else:
        return True

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
    commands = action.split()
    while len(commands) < 3:
        commands.append('')

    temp = 0
    isRunning = True

    try:
        while isRunning:
            if 'end' in action and temp < 1:
                say.eror(player.name)
                
            elif 'end' in action and  temp == 1:
                isRunning = False
                break

            if 'play' in action:
                if temp > 0:
                    say.whore(player.name)
                else:
                    if int(commands[1]) > (len(player.hand) - 1):
                        say.eror(player.name)
                    else:
                        move_to_center(player, int(commands[1]))
                        temp += 1
            elif 'build' in action:
                if check_commands(player, commands, 2):
                    print(commands)
                    if (abs(int(commands[1])) or abs(int(commands[2]))) > (len(center.pile) - 1):
                        print('oops')
                        say.buckaroo(player.name)
                    else:
                        center.buildCards(int(commands[1]), int(commands[2]), player)

            elif 'collect' in action:
                print(commands)
                if (abs(int(commands[1])) or abs(int(commands[2]))) > (len(center.pile) - 1):
                    say.buckaroo(player.name)
                else:
                    center.collectCards(int(commands[1]), int(commands[2]))

            elif 'take' in action:
                if (abs(int(commands[1])) > (len(center.pile) - 1)):
                    say.buckaroo(player.name)
                else:
                    moveFromCenter(player, int(commands[1]))

            elif 'quit' in action:
                quit()

            else:
                say.eror2(player.name)

            testPrint(player, center.pile)
            action = input('Enter the command (play, build, collect, take) and the corresponding indices: ')
            commands = action.split()
            while len(commands) < 3:
                commands.append('')

    except:
        print(sys.exc_info()[0])
        say.end(player.name)
        # quit()

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


while count < 49:
    temp = False
    for player in players:
        if player.hand:
            temp = False
            break
        else:
            temp = True
    if temp:
        dealCards(deck, players)

    player = players[count % len(players)]

    
    for pile in center.pile:
        for card in pile.pile:
            card.wasLastPlayed = False
    
    playersTurn(player)
    


    count += 1

print('done wit game')
compare_players(players)
print('done wit comparision only leads to sadness')
for player in players:
    player.show_points()
