from casino import *


p1 = Player()
p1.show()


deck = create_deck()
for i in deck:
    print(i.suit)

