
import random
import CardDeck
import PlayerClass
# for uplead



numbers_used_list = []  # where used to try and make sure you don't draw the same card twice
def draw_cards():  # This function will add a random card

    rande_number = random.randint(1, 52)  # will pick a number from 0 to 52

    checker = True
    while checker == True:
        if rande_number not in numbers_used_list:  # checks if number in master list, so we don't get duplicate cards
            rando_card_num = CardDeck.numberMatchDictiony[rande_number]  # this works to return the card over the number
            numbers_used_list.append(rande_number)  # adding number to master list
            #print(numbers_used_list)  # used for testting to make sure no numbers are matching
            return rando_card_num  # returning card type

        rande_number = random.randint(1, 52)  # will start over is number is in master list



arrayPlayer1 = []
arrayPlayer2 = []
arrayPlayer3 = []
arrayPlayer4 = []

for x in range(3):
    card = draw_cards()
    arrayPlayer1.append(card)
    card2 = draw_cards()
    arrayPlayer2.append(card2)
    card3 = draw_cards()
    arrayPlayer3.append(card3)


#Player = bob()
#bob = Player()
#bob.play()
#bob.play_winner()

print("Your cards are: ")
print(arrayPlayer1)
print("Player two cards: ")
print(arrayPlayer2)
print("Player three cards: ")
print(arrayPlayer3)

billyBob = PlayerClass.Player("bob")



