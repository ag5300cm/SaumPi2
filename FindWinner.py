

def total_score(number_list):  # The purpose of this function is to add up the total scores of the cards in hand
    add_up = 0  # used for adding other numbers to
    for i in number_list:  # goes through each item in the list
        add_up = add_up + i
        if add_up >= 10:  # checks if above ten, this is Saum Pi after all
            add_up = add_up - 10
    return_number = add_up
    return return_number  # Going to get remainder for ten division


#def compare_score(alpha, omega):


