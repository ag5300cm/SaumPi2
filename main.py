
import random
import CardDeck
import PlayerClass
import FindWinner
# for uplead2


#player_name = input("Whats your name? ")
p1 = PlayerClass.Player(input("Whats your name? "))
print(p1.name)



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

# used to hold list of players cards
arrayPlayer1 = []
arrayPlayer2 = []
arrayPlayer3 = []  # currently at three players
arrayPlayer4 = []

# used to hold list of player cards value
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
    arrayPlayer2Numbers.append(card2[1])
    card3 = draw_cards()
    arrayPlayer3.append(card3[0])
    arrayPlayer3Numbers.append(card3[1])

# this list is used to determine whom wins the match
playerListNumbers = [FindWinner.total_score(arrayPlayer1Numbers), FindWinner.total_score(arrayPlayer2Numbers),
                     FindWinner.total_score(arrayPlayer3Numbers)]



#Player = bob()
#bob = Player()
#bob.play()
#bob.play_winner()

print("Your cards are: ", arrayPlayer1, "Your score is: ", FindWinner.total_score(arrayPlayer1Numbers))  # not sure which looks better for viewing change how you wish lucky
#print(arrayPlayer1)
print("Player two cards: ", arrayPlayer2, "score is: ", FindWinner.total_score(arrayPlayer2Numbers))
print("Player three cards: ")
print(arrayPlayer3, "score is: ", FindWinner.total_score(arrayPlayer3Numbers))
FindWinner.compare_score(playerListNumbers)


billyBob = PlayerClass.Player("bob")



