from random import randint

board = []

for H in range(11):
    board.append(["O"] * 13)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row1 = random_row(board)
ship_col1 = random_col(board)

ship_row2 = random_row(board)
ship_col2 = random_col(board)

ship_row3 = random_row(board)
ship_col3 = random_col(board)

ship_row4 = random_row(board)
ship_col4 = random_col(board)

ship_row5 = random_row(board)
ship_col5 = random_col(board)

print (int(ship_col1), int(ship_row1))
print (int(ship_col2), int(ship_row2))
print (int(ship_col3), int(ship_row3))
print (int(ship_col4), int(ship_row4))
print (int(ship_col5), int(ship_row5))
# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(10):
    print "Turn", turn + 1
    
    guess_col = int(raw_input("Guess Column:"))
    guess_row = int(raw_input("Guess Row:"))
    
    if (guess_row == ship_row1 and guess_col == ship_col1) or (guess_row == ship_row2 and guess_col == ship_col2) or (guess_row == ship_row3 and guess_col == ship_col3) or (guess_row == ship_row4 and guess_col == ship_col4) or (guess_row == ship_row5 and guess_col == ship_col5):
        print "Congratulations! You sunk my battleship!"
        board[guess_row][guess_col] = "X"
        print_board(board)
        if (board[ship_row1][ship_col1] == "X") and (board[ship_row2][ship_col2] == "X") and (board[ship_row3][ship_col3] == "X") and (board[ship_row4][ship_col4] == "X") and (board[ship_row5][ship_col5] == "X"):
            print "Congratulations! You Win!"
            break
    elif turn == 10:
        print "Game Over"
    else:
        if (guess_row < 0 or guess_row > 13) or (guess_col < 0 or guess_col > 13):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "/"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "/"
        # Print (turn + 1) here!
        print_board(board)
        if turn == 10:
            print "Game Over"