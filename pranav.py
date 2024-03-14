# Tic-Tac-Toe game
# Initial game board
board =[' ',' ',' ',' ',' ',' ',' ',' ',' ']

# Function to print the game board

# Function to print the game board
def print_board():
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' ')
    print("---+---+---")
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' ')
    print("---+---+---")
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' ')


# Function to check if the game is over
def is_game_over():
    # Check for a win
    if ((board[0] == board[1] == board[2] and board[0] != ' ') or
    (board[3] == board[4] == board[5] and board[3]!= ' ' ) or
    (board[6] == board[7] == board[8] and board [6]!= ' ') or
    (board[0] == board[3]== board[6] and board[0]!= ' ') or
    (board [1] == board [4] == board [7] and board[1]!= ' ') or
    (board[2] == board[5] == board [8] and board [2]!= ' ') or
    (board [0] == board [4] == board [8] and board[0]!= ' ') or
    (board[2] == board[4] == board[6] and board [2]!= ' ')) :
     print_board()
     print ("Game over! Player" + turn +" wins!")
     return True
     # Check for a tie
    elif ' ' not in board:
        print_board()
        print("Game over! It's a tie!")
        return True
    # Game is not over
    else:
        return False
#Function to get the next move from the player
def get_move():
    while True:
        try:
            move = int(input ("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move. Please enter a number between 1 and 9.")
            elif board[move - 1] != ' ':
                print ("That space is already occupied. Please choose a different space.")
            else:
                return move
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
# The main game loop
turn = 'X'
while True:
    # Print the current game board
    print_board()
    # Get the next move from the player
    print("Player " + turn + "'s turn.")
    move = get_move ()
    # Update the game board
    board [move - 1] = turn
    # Check if the game is over
    if is_game_over ():
       break
    # Switch the turn to the other player
    if turn == 'X':
      turn = 'o'
    else:
       turn = 'X'

