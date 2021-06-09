# Side note - this game is for 1-4 players - just need minor adjustments see notes below
# Lists for in Deck and Card class 
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eitgh','Nine','Ten','Eleven','Twelve','Thirteen','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eitgh':8, 'Nine':9, 'Ten':10, 
          'Eleven':10, 'Twelve':10, 'Thirteen':10, 'Ace':11}
# Representation of card object
class Card:
    
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
    def __str__(self):
        return self.rank+ ' of '+ self.suit
# Representation of deck object
class Deck:
    
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank,suit))
                
    def shuffle_deck(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
# Representation of the player money 
class bank_roll:
    
    def __init__(self,money,bet = 0):
        self.money = money
        self.bet = bet
        
    def recive_won(self,amount):
        self.money += amount
        
    def withdraw_lose(self,amount):
        self.money -= amount

    def __str__(self):
        return f'You have only {self.money} chips'
# Representation of player object
class Player(bank_roll):
    
    def __init__(self,name,money):
        self.name = name
        self.player_cards = []
        self.hand_sum = 0
        self.ace = 0
        self.play = True # indicate is the player want's or can't play
        bank_roll.__init__(self,money)
    def recive(self,card):
        self.player_cards.append(card)
        self.hand_sum += card.value
        if card.rank == 'Ace':
            self.ace += 1
    def adjust_for_ace(self):
        while self.hand_sum > 21 and self.ace:
            self.hand_sum -= 10
            self.ace -= 1                
from IPython.display import clear_output
from time import sleep
# Ask the player if he/she still wanna play
def replay(player):
    global zero
    while zero:
        play = input(f'Hey {player.name},\nDo you like to go again? enter Y/N ')
        if play[0].upper() == 'Y':
            print(f'{player.name} you have got {player.money} chips')# At the and of the game print each player chips
            break
        elif play[0].upper() == 'N':
            player.play = False
            player.money = 0
            zero -= 1
            break
        else:
            print("Sorry didn't get it")
#print all the players cards
def print_all_players(game_end):
    #sleep(5)
    #clear_screen()
    if player1.hand_sum <= 21 and player1.money > 0:
        print('***The player1 hand is: ',*player1.player_cards,sep = '\n')
        print(f"The sum of this hand is: {player1.hand_sum}")
    if player2.hand_sum <= 21 and player2.money > 0:
        print('***The player2 hand is: ',*player2.player_cards,sep = '\n')
        print(f"The sum of this hand is: {player2.hand_sum}")
    #if player3.hand_sum <= 21:
        #print('***The player3 hand is: ',*player3.player_cards,sep = '\n') --> for third and fourth players
        #print(f"The sum of this hand is: {player3.hand_sum}")
    #if player4.hand_sum <= 21:
        #print('***The player4 hand is: ',*player4.player_cards,sep = '\n') -->
        #print(f"The sum of this hand is: {player4.hand_sum}")     
    if game_end == True:
        print('The dealer hand is: ',*dealer.player_cards,sep = '\n')
        print(f"The sum of this hand is: {dealer.hand_sum}")
    else:
        print('***The dealer hand is:')
        print(dealer.player_cards[0])
        print(" <card hidden>")
# input from player 'Hit' or 'Stand'
def player_selection(player):
    while True:
        selection = input(f"{player.name} Please select 'Hit' or 'Stand' - H/S ")
        print(selection)
        if selection[0].upper() == 'H' or selection[0].upper() == 'S':
            return selection[0].upper() == 'H'
        else:
            print("Sorry didn't get it")
# input money or bet from player - bet_or_money is True if player inputs a bet else False         
def player_amount(bet_or_money,player):    
    while True:
        try:
            if bet_or_money:
                bet = int(input(f"{player.name} please enter a the amount you want to bet on: "))
                if player.money - bet >= 0: 
                    return bet
                else:
                    print('Sorry not enough money')
                    print(player)
                    continue
            else:    
                money = int(input(f'{player.name} please enter how much chips do you have to bet on: '))
                return money
        except:
            print('Sorry not a number, Please try again ')
# Print only one player            
def print_one_player(player):
    #clear_screen()
    print(f'{player.name} hand is: ',*player.player_cards,sep = '\n')
    print(f'The sum of this hand is: {player.hand_sum}')
# Restart the hands of the game            
def restart():
    player1.hand_sum = 0
    player2.hand_sum = 0
    #player3.hand_sum = 0
    #player4.hand_sum = 0
    dealer.hand_sum = 0
    player1.player_cards = []
    player2.player_cards = []
    #player3.player_cards = [] --> for third and fourth players
    #player4.player_cards = [] -->
    dealer.player_cards = []
# Player select hit or stand - messages for results    
def player_turn(player):
    while True:
        print_all_players(False)
        
        if player.hand_sum == 21:
            print(f'***Congratulations {player.name}!!\nYou have Black-Jack you won!!!*** ')
            player.recive_won(2*player.bet)
            break
        if player.hand_sum < 21:
            if player_selection(player):
                player.recive(game_deck.deal_one())
                player.adjust_for_ace()
            else:
                break
        if player.hand_sum > 21:
            print_one_player(player)
            print(f'Sorry {player.name} you are out')
            player.withdraw_lose(player.bet)
            break
# Check for winners                
def dealer_check(player):
    if player.hand_sum <= 21:
        while True:
            print_all_players(True)
            if dealer.hand_sum == 21:
                print(f'***Sorry lookes like the dealer won, better luck next time {player.name}*** ')
                player.withdraw_lose(player.bet)
                break  
            elif dealer.hand_sum < player.hand_sum or dealer.hand_sum > 21:
                print(f'***Congratulations!!\n{player.name} won!!*** ')
                player.recive_won(2*player.bet)
                break
            elif dealer.hand_sum == player.hand_sum:
                print(f"***Hey {player.name}, It's a tie no one wins!! PUSE*** ")
                break
            elif dealer.hand_sum > player.hand_sum:
                print(f'***Sorry lookes like the dealer won, better luck next time {player.name}*** ')
                player.withdraw_lose(player.bet)
                break
    else:
        print(f'Sorry {player.name} you have {player.hand_sum}, you lose')
# If the dealer have black jack and players don't - print message and take chips prom players       
def dealer_black_jack(dealer):
        if player1.hand_sum != 21 and player2.hand_sum != 21:
            print_all_players(True)
            print("***Sorry lookes like the dealer won, better luck next time*** ")
            player1.withdraw_lose(player1.bet)
            player2.withdraw_lose(player2.bet)
            #player3.withdraw_lose(player3.bet) --> For third and fourth players
            #player4.withdraw_lose(player4.bet) -->
            # Check if players have chips
            replay_check()
# Check if the player have chips       
def check_if_zero(player):
    global zero
    if player.money == 0:
        print(f'Sorry {player.name} you have no chips, you are out.')
        player.play = False
        zero -= 1
# Check_if_zero and replay functions together
def replay_check():
    # Check if player have chips
    if player1.play == True: 
        check_if_zero(player1)
    if player2.play == True:
        check_if_zero(player2)
    #if player3.play == True:
        #check_if_zero(player1) --> For third and fourth players
    #if player4.play == True:
        #check_if_zero(player1) -->
            
    # Asks each player if he/she wants to play
    if player1.play == True:
        replay(player1)
    if player2.play == True:
        replay(player2)
    #if player3.play == True: --> For third and fourth players
        #replay(player3)
    #if player4.play == True: -->
        #replay(player3)

# Clear the screen for linux,mac and windows
from os import system,name
def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
# Start of main
if __name__ == '__main__':
    game_deck = Deck()# The game deck
    game_deck.shuffle_deck()# Shuffle the deck
    dealer = Player('dealer',0)# Create a dealer
    zero = 2 # Counter - if all players have no money, the game ends
    print('Hello and Welcom to Black-Jack in Python')     
    player1 = Player('Player1',0)# Create a player1
    player2 = Player('Player2',0)# Create a player2
    #player3 = Player('player3',0)# Create a player3 --> For third and fourth players
    #player4 = Player('player4',0)# Create a player4 -->
    player1.money = player_amount(False,player1)# Input the amunt of the players money
    player2.money = player_amount(False,player2)# Input the amunt of the players money
    #player3.money = player_amount(False,player3)# Input the amunt of the players money --> For third and fourth players
    #player4.money = player_amount(False,player4)# Input the amunt of the players money -->
    print('Ok so lets get started :-)')
    # Start the game
    while zero:
        # Resets the game hands
        restart()
        # Players place a bet
        if player1.play == True:
            player1.bet = player_amount(True,player1)# input how nuch the player wants to bet on
        if player2.play == True:
            player2.bet = player_amount(True,player2)# input how nuch the player wants to bet on 
        #if player3.play == True:
            #player3.bet = player_amount(True,player3)# input how nuch the player wants to bet on --> For third and fourth players
        #if player4.play == True:
            #player4.bet = player_amount(True,player4)# input how nuch the player wants to bet on -->
        
        # Deals the cards to the players
        for num in range(2):
            if player1.play == True:
                player1.recive(game_deck.deal_one())
            if player2.play == True:
                player2.recive(game_deck.deal_one())
            #if player3.play == True:
                #player3.recive(game_deck.deal_one()) --> For third and fourth players
            #if player4.play == True:
                #player4.recive(game_deck.deal_one()) -->
            dealer.recive(game_deck.deal_one())
        # If the dealer have 21 and palyers don't game over    
        if dealer.hand_sum == 21:
            dealer_black_jack(dealer)
            continue
            
        # Players turn
        if player1.play == True:
            player_turn(player1)
        if player2.play == True:
            player_turn(player2)
        #if player3.play == True:
            #player_turn(player3) --> For third and fourth players
        #if player4.play == True:
            #player_turn(player4) -->
            
        # If dealer hand sum in < 17 than dealer gets new card
        while dealer.hand_sum < 17:
            dealer.recive(game_deck.deal_one())
            dealer.adjust_for_ace()
        # If the dealer have 21 and palyers don't game over      
        if dealer.hand_sum == 21:
            dealer_black_jack(dealer)
            continue  
            
        # Dealer turn - checking for winners   
        if player1.play == True:   
            dealer_check(player1)
        if player2.play == True:
            dealer_check(player2)
        #if player3.play == True:
            #dealer_check(player3) --> For third and fourth players
        #if player4.play == True:
            #dealer_check(player4) -->
        
        replay_check()