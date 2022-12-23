import time
import random
player_total = 0
player1_extra = 0
player1_card = 0
player1_card2 = 0
player1_extras = 0
dealer1_card = 0
dealer1_card2 = 0
dealer_total = 0
dealer1_extra = 0
dealer1_extras = 0
randodealer2 = 0
decision = 0
bet1 = 0

# Lists declaring deck of cards
clubs = [2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K', 'As']
diamonds = [2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K', 'As']
hearts = [2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K', 'As']
spades = [2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K', 'As']

#class player with name, cash and bet variables. Also has a method that saves the bet as a variable and substract it from the entrance fee
#inserted by the player
class Player:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash

    def bet(self,number):
        self.cash -= number
        self.betx = number
        print('\nBet ${bet}\n'.format(bet= number))
        time.sleep(1)
        print('Cash left ${cash}\n'.format(cash = self.cash))


#function with one argument that will return a card depending on the argument which is random between 0 to 3, if 0 a random card will be chosen from clubs
#1 diamonds, 2 hearts and 3 spades. 
#a variable will store a random number from 0 to the length of the suit list, that number will be the index of the card in the specific suit
#it prints which is the card selected and then the card is removed from the list, for the cards that arent int, and if statement will 
#return the specific value
def card1(number):
    if number == 0:
        rando_card1 = random.randint(0,len(clubs)-1)
        card1_selected = clubs[rando_card1]
        print('Card 1 is Clubs {card}'.format(card = card1_selected))
        value = card1_selected
        clubs.pop(rando_card1)
        if card1_selected == 'J':
            value = 10
        elif card1_selected == 'Q':
            value = 10
        elif card1_selected == 'K':
            value = 10
        return value
        
    elif number == 1:
        rando_card1_2 = random.randint(0,len(diamonds)-1)
        card1_2selected = diamonds[rando_card1_2]
        print('Card 1 is Diamonds {card}'.format(card = card1_2selected))
        diamonds.pop(rando_card1_2)
        value = card1_2selected
        if card1_2selected == 'J':
            value = 10
        elif card1_2selected == 'Q':
            value = 10
        elif card1_2selected == 'K':
            value = 10
        return value

    elif number == 2:
        rando_card1_3 = random.randint(0,len(hearts)-1)
        card1_3selected = hearts[rando_card1_3]
        print('Card 1 is Hearts {card}'.format(card = card1_3selected))
        hearts.pop(rando_card1_3)
        value = card1_3selected
        if card1_3selected == 'J':
            value = 10
        elif card1_3selected == 'Q':
            value = 10
        elif card1_3selected == 'K':
            value = 10
        return value
        
    else:
        rando_card1_4 = random.randint(0,len(spades)-1)
        card1_4selected = spades[rando_card1_4]
        print('Card 1 is Spades {card}'.format(card = card1_4selected))
        spades.pop(rando_card1_4)
        value = card1_4selected
        if card1_4selected == 'J':
            value = 10
        elif card1_4selected == 'Q':
            value = 10
        elif card1_4selected == 'K':
            value = 10
        return value
       
        

def card2(number):
    if number == 0:
        rando_card2 = random.randint(0,len(clubs)-1)
        card2_selected = clubs[rando_card2]
        print('Card 2 is Clubs {card}'.format(card = card2_selected))
        clubs.pop(rando_card2)
        value = card2_selected
        if card2_selected == 'J':
            value = 10
        elif card2_selected == 'Q':
            value = 10
        elif card2_selected == 'K':
            value = 10
        return value
        
    elif number == 1:
        rando_card2_2 = random.randint(0,len(diamonds)-1)
        card2_2selected = diamonds[rando_card2_2]
        print('Card 2 is Diamonds {card}'.format(card = card2_2selected))
        diamonds.pop(rando_card2_2)
        value = card2_2selected
        if card2_2selected == 'J':
            value = 10
        elif card2_2selected == 'Q':
            value = 10
        elif card2_2selected == 'K':
            value = 10
        return value
        
    elif number == 2:
        rando_card2_3 = random.randint(0,len(hearts)-1)
        card2_3selected = hearts[rando_card2_3]
        print('Card 2 is Hearts {card}'.format(card = card2_3selected))
        hearts.pop(rando_card2_3)
        value = card2_3selected
        if card2_3selected == 'J':
            value = 10
        elif card2_3selected == 'Q':
            value = 10
        elif card2_3selected == 'K':
            value = 10
        return value
        
    else:
        rando_card2_4 = random.randint(0,len(spades)-1)
        card2_4selected = spades[rando_card2_4]
        print('Card 2 is Spades {card}'.format(card = card2_4selected))
        spades.pop(rando_card2_4)
        value = card2_4selected
        if card2_4selected == 'J':
            value = 10
        elif card2_4selected == 'Q':
            value = 10
        elif card2_4selected == 'K':
            value = 10
        return value

def extra_card(number):
    if number == 0:
        rando_card_extra = random.randint(0,len(clubs)-1)
        card_selected_extra = clubs[rando_card_extra]
        print('Extra Card is Clubs {card}'.format(card = card_selected_extra))
        clubs.pop(rando_card_extra)
        value = card_selected_extra
        if card_selected_extra == 'J':
            value = 10
        elif card_selected_extra == 'Q':
            value = 10
        elif card_selected_extra == 'K':
            value = 10
        return value
        
    elif number == 1:
        rando_card_2_extra = random.randint(0,len(diamonds)-1)
        card_2selected_extra = diamonds[rando_card_2_extra]
        print('Extra Card is Diamonds {card}'.format(card = card_2selected_extra))
        diamonds.pop(rando_card_2_extra)
        value = card_2selected_extra
        if card_2selected_extra == 'J':
            value = 10
        elif card_2selected_extra == 'Q':
            value = 10
        elif card_2selected_extra == 'K':
            value = 10
        return value
        
    elif number == 2:
        rando_card_3_extra = random.randint(0,len(hearts)-1)
        card_3selected_extra = hearts[rando_card_3_extra]
        print('Extra Card is Hearts {card}'.format(card = card_3selected_extra))
        hearts.pop(rando_card_3_extra)
        value = card_3selected_extra
        if card_3selected_extra == 'J':
            value = 10
        elif card_3selected_extra == 'Q':
            value = 10
        elif card_3selected_extra == 'K':
            value = 10
        return value
        
    else:
        rando_card_4_extra = random.randint(0,len(spades)-1)
        card_4selected_extra = spades[rando_card_4_extra]
        print('Extra Card is Spades {card}'.format(card = card_4selected_extra))
        spades.pop(rando_card_4_extra)
        value = card_4selected_extra
        if card_4selected_extra == 'J':
            value = 10
        elif card_4selected_extra == 'Q':
            value = 10
        elif card_4selected_extra == 'K':
            value = 10
        return value


def dealer1(number):
    if number == 0:
        rando_card1_dealer = random.randint(0,len(clubs)-1)
        card1_selected_dealer = clubs[rando_card1_dealer]
        print('Dealer Card is Clubs {card}'.format(card = card1_selected_dealer))
        clubs.pop(rando_card1_dealer)
        value = card1_selected_dealer
        if card1_selected_dealer == 'J':
            value = 10
        elif card1_selected_dealer == 'Q':
            value = 10
        elif card1_selected_dealer == 'K':
            value = 10
        return value
        
    elif number == 1:
        rando_card1_2_dealer = random.randint(0,len(diamonds)-1)
        card1_2selected_dealer = diamonds[rando_card1_2_dealer]
        print('Dealer Card is Diamonds {card}'.format(card = card1_2selected_dealer))
        diamonds.pop(rando_card1_2_dealer)
        value = card1_2selected_dealer
        if card1_2selected_dealer == 'J':
            value = 10
        elif card1_2selected_dealer == 'Q':
            value = 10
        elif card1_2selected_dealer == 'K':
            value = 10
        return value
        
    elif number == 2:
        rando_card1_3_dealer = random.randint(0,len(hearts)-1)
        card1_3selected_dealer = hearts[rando_card1_3_dealer]
        print('Dealer Card is Hearts {card}'.format(card = card1_3selected_dealer))
        hearts.pop(rando_card1_3_dealer)
        value = card1_3selected_dealer
        if card1_3selected_dealer == 'J':
            value = 10
        elif card1_3selected_dealer == 'Q':
            value = 10
        elif card1_3selected_dealer == 'K':
            value = 10
        return value
        
    else:
        rando_card1_4_dealer = random.randint(0,len(spades)-1)
        card1_4selected_dealer = spades[rando_card1_4_dealer]
        print('Dealer Card is Spades {card}'.format(card = card1_4selected_dealer))
        spades.pop(rando_card1_4_dealer)
        value = card1_4selected_dealer
        if card1_4selected_dealer == 'J':
            value = 10
        elif card1_4selected_dealer == 'Q':
            value = 10
        elif card1_4selected_dealer == 'K':
            value = 10
        return value


def dealer2(number):
    if number == 0:
        rando_card2_dealer = random.randint(0,len(clubs)-1)
        card2_selected_dealer = clubs[rando_card2_dealer]
        print('Dealer Card is Clubs {card}\n'.format(card = card2_selected_dealer))
        clubs.pop(rando_card2_dealer)
        value = card2_selected_dealer
        if card2_selected_dealer == 'J':
            value = 10
        elif card2_selected_dealer == 'Q':
            value = 10
        elif card2_selected_dealer == 'K':
            value = 10
        return value
        
    elif number == 1:
        rando_card2_2_dealer = random.randint(0,len(diamonds)-1)
        card2_2selected_dealer = diamonds[rando_card2_2_dealer]
        print('Dealer Card is Diamonds {card}\n'.format(card = card2_2selected_dealer))
        diamonds.pop(rando_card2_2_dealer)
        value = card2_2selected_dealer
        if card2_2selected_dealer == 'J':
            value = 10
        elif card2_2selected_dealer == 'Q':
            value = 10
        elif card2_2selected_dealer == 'K':
            value = 10
        return value
        
    elif number == 2:
        rando_card2_3_dealer = random.randint(0,len(hearts)-1)
        card2_3selected_dealer = hearts[rando_card2_3_dealer]
        print('Dealer Card is Hearts {card}\n'.format(card = card2_3selected_dealer))
        hearts.pop(rando_card2_3_dealer)
        value = card2_3selected_dealer
        if card2_3selected_dealer == 'J':
            value = 10
        elif card2_3selected_dealer == 'Q':
            value = 10
        elif card2_3selected_dealer == 'K':
            value = 10
        return value
        
    else:
        rando_card2_4_dealer = random.randint(0,len(spades)-1)
        card2_4selected_dealer = spades[rando_card2_4_dealer]
        print('Dealer Card is Spades {card}\n'.format(card = card2_4selected_dealer))
        spades.pop(rando_card2_4_dealer)
        value = card2_4selected_dealer
        if card2_4selected_dealer == 'J':
            value = 10
        elif card2_4selected_dealer == 'Q':
            value = 10
        elif card2_4selected_dealer == 'K':
            value = 10
        return value

# function o evaluate an as card, it will ask if the player wants to use the card as a 1 or 11. dependeding on the answer, the function will 
#return the value the player chose
def as_card():    
    print('As can be used as a 1 or 11')
    time.sleep(0.5)
    print('Enter 1 to use it as a 1 or 2 as a 11\n')
    as_card = int(input())
    if as_card == 1:
        value_card = 1
    elif as_card == 2:
        value_card = 11
    return value_card

#function used by the dealer to randomly use the as card as a 1 or 11
def as_card_dealer():
    rando = random.randint(0,1)
    if rando == 0:
        value_card = 1
    else:
        value_card = 11
    return value_card

#function that starts asks the custome to input the bet, minimum was declared $10, if below it will loop until the bet is greater or equal to 10
# the function also uses a class method from the player to substract the bet from the entrance fee
def start():
    print('Please enter your bet (min $10)\n')
    bet1= int(input())
    while bet1 < 10:
        print('\nBet below minimum\nPlease enter your bet (min $10)\n')
        bet1= int(input())
        time.sleep(1)
    time.sleep(1)
    player1.bet(bet1)
    time.sleep(1)
    print('Dealer is shuffling your cards...\n')  
    time.sleep(3) 

#function to pick a card from the deck, variable with a random number between 0 to 3 for the suits
def start_card1():
    randosuit1 = random.randint(0,3)
    card = card1(randosuit1)
    time.sleep(2)
    return card

def start_card2():
    randosuit2 = random.randint(0,3)
    card = card2(randosuit2)
    print('\n')
    time.sleep(2)
    return card

def start_dealer1():
    randodealer1 = random.randint(0,3)
    card = dealer1(randodealer1)
    time.sleep(2)
    return card

def start_dealer2():
     number = random.randint(0,3)
     print('\n')
     time.sleep(2)
     return number

print('Welcome to your favorite online BlackJack Game\n')
time.sleep(2)
print('Please insert you name and press enter\n')
name_input = input()
print('\n')
time.sleep(1)
print('Please enter entrance fee (min $100)\n')
entrance_input = int(input())
time.sleep(1)
while entrance_input < 100: #loop expecting an entrance fee greater or equal to $100    
    print('\nEntrance fee below minimum\nPlease enter entrance fee (min $100)\n')
    entrance_input = int(input())
    time.sleep(1)
time.sleep(1)
player1 = Player(name_input, entrance_input) #player1 variable declaring Player class with name and entrance fee variables
print('\nWelcome {player}\n'.format(player = player1.name))
time.sleep(1)

start() 
player1_card = start_card1()
player1_card2 = start_card2()
dealer1_card = start_dealer1()
randodealer2 = start_dealer2()

while True:  #a while loop to repeat the game over and over until the player cashes out
    print('Would you like to stay or get one more card?')
    time.sleep(1)
    print('Enter a 1 to stay or a 2 for an extra card\n')
    decision = int(input()) #input from the player deciding to stay or get one more card
    print('\n')
    time.sleep(0.5)
    if decision == 1: #stay part of the code
        dealer1_card2 = dealer2(randodealer2)  #second dealer's card is shown
        time.sleep(1)
        if player1_card  == 'As': #if statements to check As cards and return the int value depending on the player choice
            player1_card = as_card()
        if player1_card2 == 'As':
            player1_card2 = as_card()
        player_total = player1_card + player1_card2 + player1_extras #sum of the first two cards, extras is the sum of the extra cards the player gets
        print('\nPlayer 1 sum is {total}\n'.format(total = player_total))
        time.sleep(2)
        if dealer1_card == 'As': #As check
            dealer1_card = as_card_dealer()
            time.sleep(2)
        if dealer1_card2 == 'As':
            dealer1_card2 = as_card_dealer()
            time.sleep(2)
        dealer_total = dealer1_card + dealer1_card2 + dealer1_extras
        while dealer_total <= player_total: #While statement to keep picking cards if player sum is greater or equal than the dealer's
            if dealer_total == player_total: #If sum is equal to the player's stop picking more cards
                break
            else:
                randodealer3 = start_dealer2()
                dealer1_extra2 = dealer2(randodealer3)
                time.sleep(2)
                if dealer1_extra2 == 'As':
                    dealer1_extra2 = as_card_dealer()
                    time.sleep(2)
                dealer1_extras += dealer1_extra2
                dealer_total = dealer1_card + dealer1_card2 + dealer1_extras
        print('Dealer sum is {dealer}\n'.format(dealer = dealer_total))
        time.sleep(2)
        if dealer_total > player_total: #If statements to check who the winner is if the dealer's total is greater than the player's
            if dealer_total <= 21:
                print('The Dealer is the WINNER!!!\n') #if the dealer's sum is less than 21 but greater than the player´s, dealer is the winner
            else:
                print('The Player is the WINNER!!!\n') #if the dealer's sum is greater than 21 and greater than player's, the player is the winner if sum is below 21
                earned = player1.betx * 2 # earning is class bet variable times 2
                player1.cash += earned #earnings added to the class variable cash
                print('You earned ${earned}, cash available is ${cash}\n'.format(earned = earned, cash = player1.cash))
        if player_total > dealer_total:
            if player_total <= 21: #If player's sum is greater than dealer's and below 21, the player is the winner
                print('The Player is the WINNER!!!\n')
                earned = player1.betx  *2
                player1.cash += earned
                print('You earned ${earned}, cash available is ${cash}\n'.format(earned = earned, cash = player1.cash))
            else:
                print('The Dealer is the WINNER!!!\n') #if player's sum is greater than 21, dealer is the winner if sum is below 21
        if player_total == dealer_total:
            print('No winner this time!!!\n') #both sums are equal 
            time.sleep(2)
            player1.cash += player1.betx #bet is sum back to the player class variable
            print('Current cash is {cash}'.format(cash = player1.cash)) #prints the current cash of the player available to bet
        time.sleep(2)        
        print('Would you like to play again or cash out?\n')
        time.sleep(2)
        print('You still have ${cash} available to bet\n'.format(cash = player1.cash))
        print('Enter 1 to play again or 2 to cash out\n')
        play = int(input())
        print('\n')
        if play == 1: #decision to play again
            start()
            player1_card = start_card1() #start function and first two player's cards and dealer's are picked, dealer's second random number two 
            player1_card2 = start_card2()
            dealer1_card = start_dealer1()
            randodealer2 = start_dealer2()
            player_total = 0 #player's and dealer's sum totals are equalled to 0 for new game
            dealer_total = 0
            player1_extras = 0
            dealer1_extras = 0
            dealer1_extra = 0
            player1_extra = 0
            pass

        elif play == 2: #cash out option
            print('Thank you for playing with us, good luck {player}\n'.format(player = player1.name))
            time.sleep(2)
            print('You still have in your digital wallet ${cash}'.format(cash = player1.cash))
            exit()    #ends the game


    elif decision == 2: #decision to pick new card
        randosuit_extra = random.randint(0,3)
        player1_extra = extra_card(randosuit_extra) #picks extra card
        print('\n')
        time.sleep(2)
        if player1_extra == 'As': #checks for as card
            player1_extra = as_card()
        ('\n')
        dealer1_extra = dealer2(randodealer2) #extra card from dealer is picked
        time.sleep(2)
        if dealer1_extra == 'As': #checks for as card
            dealer1_extra = as_card_dealer()
        player1_extras += player1_extra #sums extra cards picked for the player, then extra cards are added to the first two cards picked
        dealer1_extras += dealer1_extra
        if player1_card  == 'As': 
            player1_card = as_card()
        if player1_card2 == 'As':
            player1_card2 = as_card()
        player_total = player1_card + player1_card2 + player1_extras
        if player_total > 21: #checks if the sum total is over 21, if it is player loses and has the choice for a new game or end it
            print('Sum is over 21, you lose, dealer is the WINNER!!!')
            time.sleep(2)
            print('Would you like to play again or cash out?\n')
            time.sleep(2)
            print('You still have ${cash} available to bet\n'.format(cash = player1.cash))
            print('Enter 1 to play again or 2 to cash out\n')
            play = int(input())
            print('\n')
            if play == 1:
                start()
                player1_card = start_card1()
                player1_card2 = start_card2()
                dealer1_card = start_dealer1()
                randodealer2 = start_dealer2()
                player_total = 0
                dealer_total = 0
                player1_extras = 0
                dealer1_extras = 0
                dealer1_extra = 0
                player1_extra = 0
                pass

            elif play == 2:
                print('Thank you for playing with us, good luck {player}\n'.format(player = player1.name))
                time.sleep(2)
                print('You still have in your digital wallet ${cash}'.format(cash = player1.cash))
                exit()    

        if dealer1_card == 'As':
            dealer1_card = as_card_dealer()
            time.sleep(2)
        if dealer1_card2 == 'As':
            dealer1_card2 = as_card_dealer()
            time.sleep(2)
        dealer_total = dealer1_card + dealer1_card2 + dealer1_extras
        if dealer_total > 21:
            print('Sum is over 21, dealer loses, player is the WINNER!!!')
            time.sleep(2)
            earned = player1.betx  * 2
            player1.cash += earned
            print('You earned ${earned}, cash available is ${cash}\n'.format(earned = earned, cash = player1.cash))
            time.sleep(2)
            print('Would you like to play again or cash out?\n')
            time.sleep(2)
            print('You still have ${cash} available to bet\n'.format(cash = player1.cash))
            print('Enter 1 to play again or 2 to cash out\n')
            play = int(input())
            print('\n')
            if play == 1:
                start()
                player1_card = start_card1()
                player1_card2 = start_card2()
                dealer1_card = start_dealer1()
                randodealer2 = start_dealer2()
                player_total = 0
                dealer_total = 0
                player1_extras = 0
                dealer1_extras = 0
                pass

            elif play == 2:
                print('Thank you for playing with us, good luck {player}\n'.format(player = player1.name))
                time.sleep(2)
                print('You still have in your digital wallet ${cash}'.format(cash = player1.cash))
                exit()    
            
        


        







