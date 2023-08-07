# Game of tic-tak-toe Start

import random


# Dictionary of Tic-Tak-Toe
theboard = {"top-L":" ","top-M":" ","top-R":" ",
            "mid-L":" ","mid-M":" ","mid-R":" ",
            "low-L":" ","low-M":" ","low-R":" "
            }

# Function to print the BOARD
def printBoard(board):
    
    print(f"{board['top-L']}|{board['top-M']}|{board['top-R']}")
    print("-+-+-")
    print(f"{board['mid-L']}|{board['mid-M']}|{board['mid-R']}")
    print("-+-+-")
    print(f"{board['low-L']}|{board['low-M']}|{board['low-R']}")

# Function to detect the place of the board by number
def findPlace(value):
    if value == 1:
        return "top-L"
    
    elif value == 2:
        return "top-M"
    
    elif value == 3:
        return "top-R"
    
    elif value == 4:
        return "mid-L"

    elif value == 5:
        return "mid-M"
    
    elif value == 6:
        return "mid-R"
    
    elif value == 7:
        return "low-L"
    
    elif value == 8:
        return "low-M"
    
    elif value == 9:
        return "low-R"

# Function to Randomly choose value [1-9]
def randomValue():
    return random.randint(1,9)

# Function to choose player letter [X-O]
def inputPlayerLetter():

    letter = ''
    while not(letter == "X" or letter == 'O'):
        letter = (input("Enter letter [X-O]: ")).upper()
    
    if letter == "X":
        return ['X','O']
    else:
        return ['O','X']

# Function to decide who GO FIRST!
def whoGoFirst():

    if random.randint(0,1) == 0:

        print("User's Turn")
        return "User"   
    else:
        print("AI's turn")
        return "AI"

# Function to ask player to play again
def playAgain():
    print("Do you want to play? (yes or no)")
    return input().lower().startswith('y')

# Functon to make the next move
def makeMove(board,letter,move):
    board[move] = letter

# Function check if the player is WINNER!
def isWinner(bo,le):
    return (( bo["top-L"]==le and bo["top-M"]==le and bo["top-R"]==le) or # across the top
            ( bo["mid-L"]==le and bo["mid-M"]==le and bo["mid-R"]==le) or # across the middle
            ( bo["low-L"]==le and bo["low-M"]==le and bo["low-R"]==le) or # across the bottom
            ( bo["top-L"]==le and bo["mid-L"]==le and bo["low-L"]==le) or # down the left side
            ( bo["top-M"]==le and bo["mid-M"]==le and bo["low-M"]==le) or # down the middle
            ( bo["top-R"]==le and bo["mid-R"]==le and bo["low-R"]==le) or # down the right side
            ( bo["top-L"]==le and bo["mid-M"]==le and bo["low-R"]==le) or # diognal
            ( bo["top-R"]==le and bo["mid-M"]==le and bo["low-L"]==le) # diognal
            )

# Function to copy the Dictionary
def getBoardCopy(board):
    dupeBoard = board.copy()
    return dupeBoard

# Function that check for empty space on the Board
def isSpaceFree(board,move):
    return board[move] == " "


### Program Start's
print("The Game of Tic-Tak-Toe Start")

# Asking user to choose letter [x,o]
turn_user = input("Enter the letter ['X' or 'O']: ")


# Checking for letter [x,o]

# option_lst = inputPlayerLetter()
# turn_user = option_lst[0]
# turn_AI = option_lst[0]
if turn_user.upper() == "X":
    turn_AI = "O"
else:
    turn_AI = "X"


# cheacking for who will GO FIRST!

# chance = whoGoFirst()
if random.randint(0,1) == 0:
    print("User's Turn")
    move = "User"   
else:
    print("AI's turn")
    move = "AI"

if move == "User":
    turn = turn_user
else :
    turn = turn_AI


# Main Game Loop
for i in range(9):
    # Tells who's turn is Coming
    # print(f"Turn: {turn}")

    if move == "User":
        # if USER turn, then What to do ?
        print(f"Turn: {turn}")
        printBoard(theboard)
        board_value = int(input("Enter the Place: "))
        theboard[findPlace(board_value)] = turn
        printBoard(theboard)
        move = "AI"
        turn = turn_AI
    else:
        # if AI turn, then What to do ?
        print(f"Turn: {turn}")

        board_value_AI = randomValue()
    
        theboard[findPlace(board_value_AI)] = turn
        printBoard(theboard)

        move = "User"
        turn = turn_user
    

# After Game loop end's
print("Done!!!")