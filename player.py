import random

players=[]

class player:
    def __init__(s,name):
        s.name=name
        s.money=2000
        s.bet=0
        s.handValue=0
        s.hand=[]
        s.hit=False
        s.isBusted=False
    def bet(s,amount):
        if s.money>=amount:
            s.bet=amount
            s.money-=amount
    def addCards(s,cardVal,cardName):
        s.hand.append(cardName)
        s.handValue+=cardVal
    def getValue(s):
        return s.handValue
    def getHand(s):
        return s.hand
    def getName(s):
        return s.name
    def resetBust(s):
        s.isBusted=False
    def bust(s):
        s.isBusted=True
    def win(s):
        #TO-DO
        print(s.name+" Won")
            

