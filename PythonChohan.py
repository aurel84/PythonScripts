import random

numbers = 100

def roll_dice(bet, amount):

    result = ""

    global numbers
    
    Dice1 = random.randrange(2, 6, 2)
    Dice2 = random.randrange(1, 5, 2)

    if Dice1 + Dice2 % 2 == 0:
        result == "Even"
        print("The two dices added up to... even!")

    elif Dice1 + Dice2 % 2 != 0:
        result == "Odd"
        print("The two dices added up to... odd!")

    if result == bet:

        numbers += amount
        print("You wagered correctly.")
        return "You now have "+str(numbers)+" dollars in your pocket."

    else:

        numbers -= amount
        print("Too bad, you wagered incorrectly.")
        return "You now have "+str(numbers)+" dollars in your pocket."

while numbers > 0:

    if numbers <= 0:

        print("You lost the game!")

        break

    elif numbers >= 1000:

        print("Call security, this guy's a dirty cheat!")
        print("The house always wins.")

        break

    else:

        make_bet = input("Odd or Even, make your call: ")
        make_wager = int(input("Ok, now add your wager: "))

        print(roll_dice(make_bet, make_wager))
