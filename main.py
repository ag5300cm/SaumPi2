
import random
import CardDeck


arrayPlayer1 = []
arrayPlayer2 = []


for x in range(3):
    rando_card = random.choice(CardDeck.cardDictiony)
    arrayPlayer1.append(rando_card)

print(arrayPlayer1)



