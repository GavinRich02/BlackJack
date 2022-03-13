from player import *
import random

dealerPlayer=player('Dealer')
deck=[]

class dealer:
    def __init__(s):
        s.money=0
        s.cardVal=0
        s.initialDealDone=False
        s.playersDone=False
        s.BlackJacks=[]
        s.finalVals=[]
        s.playersWhoBeatDealer=[]
    def createDeck(s):
        s.tempdeck=[]
        for i in range(13):
            for j in range(4):
                s.card=i+1
                if s.card==1:
                    s.tempdeck.append('A')
                elif s.card==11:
                    s.tempdeck.append('J')
                elif s.card==12:
                    s.tempdeck.append('Q')
                elif s.card==13:
                    s.tempdeck.append('K')
                else:
                    s.tempdeck.append(s.card)
    def shuffleDeck(s):
        while len(s.tempdeck)>0:
            index=random.randint(0,len(s.tempdeck)-1)
            deck.append(s.tempdeck[index])
            s.tempdeck.pop(index)
    def initialDeal(s):
        for player in players:
            player.resetBust()
            for i in range(2):
                s.dealCard(player)
        s.dealCard(dealerPlayer)
        s.dealCard(dealerPlayer)
        s.initialDealDone=True
        s.getHands()
    def dealCard(s,player):
        card=deck[0]
        deck.pop(0)
        if card=='A':
            if player.getValue()>10:
                s.cardVal=1
            else:
                s.cardVal=11
        elif card=='J' or card=='Q' or card=='K':
            s.cardVal=10
        else:
            s.cardVal=card
        player.addCards(s.cardVal,card)
        if s.initialDealDone:
            s.getHands()
    def setPlayersDone(s):
        s.playersDone=True
    def dealerHits(s):
        while dealerPlayer.getValue()<17:
            s.dealCard(dealerPlayer)
        for player in players:
            #TO-DO: Expand for more players; only usable for one player
            if player.getValue()>dealerPlayer.getValue():
                print(player.getName()+" Won")
            elif player.getValue()==dealerPlayer.getValue():
                print("Draw")
                

            
    def getHands(s):
        if s.playersDone==False:
            print("Dealer: "+str(dealerPlayer.getHand()[0])+" X")
        else:
            hand=""
            for card in dealerPlayer.getHand():
                hand+=str(card)+" "
            print("Dealer: "+hand)
        for player in players:
            hand=""
            for card in player.getHand():
                hand+=str(card)+" "
            print(player.getName()+": "+hand+" Value: "+str(player.getValue()))
            if player.getValue()>21:
                player.bust()
            if player.getValue()==21:
                player.win()