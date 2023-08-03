import random

player_1_cash = 100
player_2_cash = 100

card_deck = {
    "Ace": 1, 
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9, 
    "Jack": 10,
    "Queen": 11,
    "King": 12
}

def pick_card():

    global card_deck

    picked_card = random.choice(list(card_deck.keys()))
    
    return picked_card

while player_1_cash > 1 or player_2_cash > 1:

    player_1_card = (pick_card())
    player_2_card = (pick_card())

    player_1_wager = int(input("Player 1: please make your wager: "))

    player_2_wager = int(input("Player 2: please make your wager: "))


    if player_1_card in card_deck:
        card_deck.pop(player_1_card)

    if player_2_card in card_deck:
        card_deck.pop(player_2_card)

    print("Player 1 picks a "+str(player_1_card)+" card.")

    print("Player 2 picks a "+str(player_2_card)+" card.")
    
    if player_1_card > player_2_card:
        player_1_cash += player_2_wager
        player_2_cash -= player_2_wager
    
        print("Player 1 wins this round!")
    
        print("Player 1 has "+str(player_1_cash)+" and Player 2 has "+str(player_2_cash)+" remaining.")
    

    elif player_2_card > player_1_card:
        player_2_cash += player_1_wager
        player_1_cash -= player_1_wager
    
        print("Player 2 wins this round!")
    
        print("Player 2 has "+str(player_2_cash)+" and Player 2 has "+str(player_1_cash)+" remaining.")
    

    if player_2_cash <=0:
    
        print("Player 1 cleaned Player 2's pocket!")
        break

    elif player_1_cash <=0:
    
        print("Player 2 cleaned Player 1's pocket!")
        break
