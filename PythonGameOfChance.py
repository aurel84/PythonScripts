import random

numbers = 100

def coin_flip(bet, amount):

    global numbers
    
    flip_a_coin = ["Heads", "Tails"]

    result = random.choice(flip_a_coin)

    print("A coin is flipped, and lands on... "+result+"!")
        
    if result == bet:
        numbers += amount
        print("You wagered correctly.")

    elif result != bet:
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

        make_bet = input("Heads or Tails, make your call: ")
        make_wager = int(input("Ok, now add your wager: "))

        print(coin_flip(make_bet, make_wager))
