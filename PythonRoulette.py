import random

cash = 100

def play_roulette(bet, wager):

    global cash

    print("You wagered "+str(wager)+" out of "+str(cash)+"!")
    cash = cash - wager

    roulette_numbers = random.randrange(0, 38, 1)

    odd_range = range(2, 36, 2)
    even_range = range(1, 35, 2)

    single_zero = 37
    double_zero = 38

    if type(bet) == str: 

        if roulette_numbers in odd_range and bet == "Odd":

            cash = ( wager * 2 ) + cash
            print("Your bet on Odd is correct.")

        elif roulette_numbers in odd_range and bet == "Even":

            print("Your bet on Even is incorrect.")

        elif roulette_numbers in even_range and bet == "Even":

            cash = ( wager * 2 ) + cash
            print("Your bet on Even is correct.")

        elif roulette_numbers in odd_range and bet == "Even":

            print("Your bet on Odd is incorrect.")

        elif roulette_numbers == single_zero:
        
            print("It landed on on a 0, you lose!")

        elif roulette_numbers == double_zero:
        
            print("It landed on on a 00, you lose!")

    elif type(bet) == int: 

        if roulette_numbers == bet:

            cash = ( wager * 35 ) + cash
            print("Your bet on the exact number is correct.")

        elif roulette_numbers != bet:

            print("You bet wrong, it landed on "+str(roulette_numbers)+"!")

        elif roulette_numbers == single_zero:
        
            print("It landed on on a 0, you lose!")

        elif roulette_numbers == double_zero:
        
            print("It landed on on a 00, you lose!")

    return "You now have "+str(cash)+" remaining!"

while cash > 0:

    make_bet = input("Player 1: please pick a number between 1 and 36, or pick Odd or Even: ")

    try:
        
        make_bet = int(make_bet)

        if make_bet > 36 or make_bet < 1:

            print("You need to pick a number between 1 and 36!")

        elif make_bet <= 36 or make_bet >= 1:

            print("You made a bet on "+str(make_bet)+" number.")

            make_wager = int(input("Please choose the amount you want to wager: "))

            print("You've wagered "+str(make_wager)+" dollars!")

            if make_wager < cash:

                print(play_roulette(make_bet, make_wager))

            else:

                print("You can't wager more money than you have available!")

                make_wager

    except:

        make_bet = str(make_bet)

        make_bet = make_bet.title()
        
        if make_bet == "Odd" or make_bet == "Even":
            
            print("You made a bet on a "+make_bet+" space.")

            make_wager = int(input("Please choose the amount you want to wager: "))

            print("You've wagered "+str(make_wager)+" dollars!")

            if make_wager < cash:

                print(play_roulette(make_bet, make_wager))

            else:

                print("You can't wager more money than you have available!")

                make_wager

        else:

            print("You need to type in Odd or Even if you want to make a bet on a space!")

            make_bet

    if cash <= 0:

        print("You ran out of money. The house always wins.")

        break
