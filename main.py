
import random
import CardDeck


def draw_cards():  # todo "pop" cards from deck when pulled
    rande_number = random.randint(0, 52)
    rando_card = (CardDeck.cardDictiony.pop(rande_number))
    #CardDeck.cardDictiony.pop(rando_card)
    return rando_card


arrayPlayer1 = []
arrayPlayer2 = []
arrayPlayer3 = []
arrayPlayer4 = []



for x in range(3):
    card = draw_cards()
    arrayPlayer1.append(card)




print("Your cards are: ")
print(arrayPlayer1)
#print("Player two cards: ")
#print(arrayPlayer2)



