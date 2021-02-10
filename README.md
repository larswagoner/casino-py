# casino

### Terminal based `game.py` function calls

#### Player Initialization and game setup
First instantiate the number of players playing in the game with their names. 
Add them to a list holding player objects and instantiate a deck.
``` python
def setup():
    deck = create_deck()
    players = []
    numPlayers = int(input('Enter how many players: '))
    for i in range(numPlayers):
        playername = input('Enter your name: ')
        players.append(Player(playername))

setup()
```

