from random import randint

board = []

# Creates the board
for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    """ Function that prints the board """
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    """ Function that returns a random space in the board """
    return randint(0, len(board) - 1)

def random_col(board):
    """ Function that returns a random column in the board """
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    # If the user guesses, end the loop
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        # If there are still turns available
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        # If this space was already selected
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        print "Turn", turn + 1
        # If there are no more turns
        if(turn == 3):
            print "Game Over"
        print_board(board)
