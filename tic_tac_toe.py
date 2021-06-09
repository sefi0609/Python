from IPython.display import clear_output
# Display the game board
def display_board(board):
    
    clear_screen()
    print('      |     |     ')
    print(f'   {board[6]}  |  {board[7]}  |  {board[8]} ')
    print('      |     |     ')
    print('  ---------------')
    print('      |     |     ')
    print(f'   {board[3]}  |  {board[4]}  |  {board[5]} ')
    print('      |     |     ')
    print('  ---------------')
    print('      |     |     ')
    print(f'   {board[0]}  |  {board[1]}  |  {board[2]} ')
    print('      |     |     ')
#Print the index board
def print_index_board():
    
    print('      |     |     ')
    print(f'   {7}  |  {8}  |  {9} ')
    print('      |     |     ')
    print('  ---------------')
    print('      |     |     ')
    print(f'   {4}  |  {5}  |  {6} ')
    print('      |     |     ')
    print('  ---------------')
    print('      |     |     ')
    print(f'   {1}  |  {2}  |  {3} ')
    print('      |     |     ')    
# Ask the first player - 'X' or 'O' 
def player_input():
    
    marker = ''
    
    while True:
        try:
            marker = input("Player 1, choose 'X' or 'O': ").upper()
        except:
            print('Sorry invalid selection, Please try again')
        else:
            if marker == 'X' or marker == 'O':
                break
            else:
                print("Sorry need 'X' or 'O'")
# Return a tuple of markers                  
    if marker == 'X':
        return ('X','O')
        
    else:
        return ('O','X')
# Place the marker on the board
def place_marker(board, marker, position):
    
    board[position-1] = marker
# Check if there is a winner
def win_check(board, mark):
    
    #Check row
    for num in range(0,9,3):
        if board[num] == board[num+1] == board[num+2] == mark:
            return True
    #Check column
    for num in range(0,3):
        if board[num] == board[num+3] == board[num+6] == mark:
            return True
    #Check diagonals
    return (board[0] == board[4] == board[8] == mark) or (board[2] == board[4] == board[6] == mark)
import random
# Ramdom selection of player
def choose_first():
    
    first = random.randint(0,1)
    
    if first == 0:
        return 'Player 1'
    else:
        return 'Player 2'
# Checks if this position on the board is free
def space_check(board, position):
    
    return board[position-1] == ' '
# Check if the board is full
def full_board_check(board):
    
    for num in range(0,9):
        if  space_check(board, num):
            return False
        
    return True
# Ask for the player choice and check if the position is free 
def player_choice(board):
    
    position = -1
    
    while position not in range(1,10):
        
        position = int(input('Please choose a position (1-9): '))
        
        if space_check(board, position):
            return position
        else:
            print("Sorry, invalid input, Please try again")
# Check if the players want's to play again
def replay():
    
    while True:
        try:
            play = input("Do you want to play again? enter 'Y' or 'N': ").upper()
        except:
            print('Sorry invalid selection, Please try again')
        else:
            if play.upper() == 'Y':
                return True
            elif play.upper() == 'N':
                return False
            else:
                print("Sorry need 'X' or 'O'")

# Clear the screen for linux,mac and windows
from os import system,name
def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Start of main
if __name__ == '__main__':
    from time import sleep

    print('Welcome to Tic Tac Toe!')
    print("The board look's like this: ")
    print_index_board()
    print("Okay so now let's start to play :-)")

    while True:
        # Set the game up here
        board = [' ']*9
        game_on = True
        player1 , player2 = player_input()
        first = choose_first()
        print(f'{first} goes first')
        sleep(4)
        
        while game_on:
            
            #Player 1 Turn
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1, position)
            display_board(board)
            win = win_check(board, player1)
            if win == True:
                print("Player 1 Won!")
                break
            full = full_board_check(board)
            if full == True:
                print("It's a Tie!")
                break
            # Player2's Turn
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2, position)
            display_board(board)
            win = win_check(board, player2)
            if win == True:
                print("Player 2 Won!")
                break
            full = full_board_check(board)
            if full == True:
                print("It's a Tie!")
                break

        if not replay():
            break