
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
            card_number_worth = CardDeck.cardDictiony[rande_number]  # will get the value of the card
            return rando_card_num, card_number_worth  # returning card type, and card playing value

        rande_number = random.randint(1, 52)  # will start over is number is in master list


def total_score(number_list):  # The purpose of this function is to add up the total scores of the cards in hand
    add_up = 0  # used for adding other numbers to
    for i in number_list:  # goes through each item in the list
        add_up = add_up + i
    return (add_up % 10)  # Going to get remainder for ten division


arrayPlayer1 = []
arrayPlayer2 = []
arrayPlayer3 = []  # currently at three players
arrayPlayer4 = []

arrayPlayer1Numbers = []
arrayPlayer2Numbers = []
arrayPlayer3Numbers = []
arrayPlayer4Numbers = []

for x in range(3):
    card = draw_cards()
    arrayPlayer1.append(card[0])
    arrayPlayer1Numbers.append(card[1])
    #print(arrayPlayer1Numbers)   # used for data testing
    #print(total_score(arrayPlayer1Numbers))
    card2 = draw_cards()
    arrayPlayer2.append(card2[0])
    arrayPlayer2Numbers.append(card[1])
    card3 = draw_cards()
    arrayPlayer3.append(card3[0])
    arrayPlayer3Numbers.append(card[1])


#Player = bob()
#bob = Player()
#bob.play()
#bob.play_winner()

print("Your cards are: ", arrayPlayer1, "Your score is: ", total_score(arrayPlayer1Numbers))  # not sure which looks better for viewing change how you wish lucky
#print(arrayPlayer1)
print("Player two cards: ")
print(arrayPlayer2)
print("Player three cards: ")
print(arrayPlayer3)

billyBob = PlayerClass.Player("bob")



