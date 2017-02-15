import random
import math

class player(object):
    def __init__(self, name, age, gender):
        self. name = name
        self.age = age
        self.gender = gender


    def taunt(self, message):
        print message

    def burp(self):
        print ("sorry guys, i need to get some tea")


kennedy = player("kennedy", 33, "male", )
kennedy.taunt("sooka bliat")
kennedy.burp()
joey = player("joey", 28, "male", )
joey.taunt("doma")
Patrick = player("patrick", 27, "male", )
patrick.taunt("diuu lae lowmow")

class card(object):
    def __init__(self,suit, value):
        self.suit = suit
        self.value = value
        print ("good card!")

queen_of_heart = card("heart", "queen")

class deck(object):
    def __init__(self):
        deck = ["hearts", "spades", "clubs", "diamonds"]
        card_value = [2,3,4,5,6,7,8,9,10, "jack", "queen", "king", "Ace"]
        self.current_deck = []

        for i in deck:
            for j in card_value:
                current_card = i + " " + str(j)
                self.current_deck.insert(0,current_card)
        print self.current_deck

    def deal_card(self):
        randCard = int(random.random() * len(self.current_deck))
        print self.current_deck[randCard]


first_deck = deck()
first_deck.deal_card()
