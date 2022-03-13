from player import *
from dealer import *

player1=player('Player')
players.append(player1)

dealer=dealer()
dealer.createDeck()
dealer.shuffleDeck()
dealer.initialDeal()

while player1.isBusted==False:
    choice=input("Wanna hit? ")
    if choice=='y':
        dealer.dealCard(player1)
    else:
        dealer.setPlayersDone()
        dealer.getHands()
        dealer.dealerHits()
        break