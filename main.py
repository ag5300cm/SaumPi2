
import random
import CardDeck
import PlayerClass
# for uplead

#counter_down = 52
def draw_cards():  # This function will add a random card
    rande_number = random.randint(1, 52)  # will pick a number from 0 to 52
    rando_card = (CardDeck.cardDictiony.pop(rande_number))  # "pops the card from the deck so will not be drawn again
    return rando_card


arrayPlayer1 = []
arrayPlayer2 = []
arrayPlayer3 = []
arrayPlayer4 = []

for x in range(3):
    card = draw_cards()
    arrayPlayer1.append(card)
    card2 = draw_cards()
    arrayPlayer2.append(card2)


#Player = bob()
#bob = Player()
#bob.play()
#bob.play_winner()

print("Your cards are: ")
print(arrayPlayer1)
print("Player two cards: ")
print(arrayPlayer2)

billyBob = PlayerClass.Player("bob")



