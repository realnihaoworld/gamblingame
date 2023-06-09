import random as rnd
deck = [{"card": 1, "number": 4},
        {"card": 2, "number": 4},
        {"card": 3, "number": 4},
        {"card": 4, "number": 4},
        {"card": 5, "number": 4},
        {"card": 6, "number": 4},
        {"card": 7, "number": 4},
        {"card": 8, "number": 4},
        {"card": 9, "number": 4},
        {"card": 10, "number": 4},
        {"card": 10, "number": 4},
        {"card": 10, "number": 4},
        {"card": 10, "number": 4}]

card = 0

def earnings(money, bet, winner):   #Add the amount to what the player has earned so it can display the current money they have.
    if winner == "You":
        money += int(bet)
    elif winner == "The dealer":
        money -= int(bet)
    return money

def draw(deck): #draw a card from the deck and remove it from the deck
    i = rnd.randint(0,12)
    while deck[i]["number"] == 0:
        i = rnd.randint(0, 12)
    card = int(deck[i]["card"])
    deck[i]["number"] -= 1
    return card

def addDealer(hand, deck, dealerDeck): #Add a card to the hand specificed
    card = draw(deck)
    hand += int(card)
    dealerDeck.append(card)
    return hand

def addPlayer(hand, deck, playerDeck): #Add a card to the hand specificed
    card = draw(deck)
    hand += int(card)
    playerDeck.append(card)
    return hand

def checkWinner(player, dealer): # see which of the players won the game.
    if player == 21 or dealer > 21:
        winner = "You"
        return winner
    elif dealer == 21 or player > 21:
        winner = "The dealer"
        return winner

def play(playerHand, dealerHand, playerDeck, dealerDeck): #actually play each hand
    choice = "n"
    while playerHand < 21 and dealerHand < 21: #while one of the players hasn't won
        if dealerHand > playerHand: #if the players hand is less than the dealer, they have to play.
            print("Your hand is less than the dealers, Hit!")
            playerHand = addPlayer(playerHand, deck, playerDeck)

            print("Dealer Hand:" + str(dealerDeck) + " Total:" + str(dealerHand))
            print("Player Hand:" + str(playerDeck) + " Total:" + str(playerHand))
        else: # give the player the choice to hit or stand
            while choice != "h" and choice != "s": #make sure that they have chosen one of the options
                choice = input("Hit [h] or Stand [s]: ")

            if choice == "h": #if they choose to hit, add the card to the players hand and reset the choice.
                print("Hit!")
                playerHand = addPlayer(playerHand, deck, playerDeck)
                choice = "n"

                print("Dealer Hand:" + str(dealerDeck) + " Total:" + str(dealerHand))
                print("Player Hand:" + str(playerDeck) + " Total:" + str(playerHand))

            elif choice == "s": #if they choose to stand, add a card to the dealers hand and reset choice
                print("Stand!")
                dealerHand = addDealer(dealerHand, deck, dealerDeck)
                choice = "n"

                print("Dealer Hand:" + str(dealerDeck) + " Total:" + str(dealerHand))
                print("Player Hand:" + str(playerDeck) + " Total:" + str(playerHand))

    winner = checkWinner(playerHand, dealerHand) #determine the winner and return who they are
    return winner

def blackjack():
    money = 50 #set baseline money
    print("You have a total of $" + str(money) + ".")
    while 1000 > money > 0:   # continue to play while the player has between 0 and 1000 dollars
        deck = [{"card":1,"number":4},{"card":2,"number":4},{"card":3,"number":4},{"card":4,"number":4},{"card":5,"number":4},{"card":6,"number":4},{"card":7,"number":4},{"card":8,"number":4},{"card":9,"number":4},{"card":10,"number":4},{"card":10,"number":4},{"card":10,"number":4},{"card":10,"number":4}]  #the card deck resets each hand, as do the totals and the bet
        dealerHand, playerHand, dealerDeck, playerDeck = 0, 0, [], []
        bet = 1001
        print("---------------------------------------------------------------------")  #barrier between each hand (makes it easier to seperate the hands)

        while bet > money or bet < 0:   #take bet that is viable
            bet = input("How much do you want to bet? ")
            if bet.isalpha():
                bet = 1001
                continue
            else:
                bet = int(bet)

        dealerHand = addDealer(dealerHand, deck, dealerDeck) #deal the first two cards
        playerHand = addPlayer(playerHand, deck, playerDeck)
        dealerHand = addDealer(dealerHand, deck, dealerDeck)
        playerHand = addPlayer(playerHand, deck, playerDeck)

        print("Dealer Hand:" + str(dealerDeck) + " Total:" + str(dealerHand)) #display starting totals
        print("Player Hand:" + str(playerDeck) + " Total:" + str(playerHand))

        winner = play(playerHand, dealerHand, playerDeck, dealerDeck)   #play the game and determine a winner
        money = earnings(money, bet, winner)    #determine the amount of money the player has and display winner.
        print(winner + " won. You have a total of $" + str(money) + ".")

    if money >= 1000:     #winning/losing conditions
        print("You have won! Congratulations!")
    else:
        print("You have run out of money...")

if __name__ == "__main__":
    blackjack()