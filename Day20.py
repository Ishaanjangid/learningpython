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

### Program Start's
print("The Game of Tic-Tak-Toe Start")

# Asking user to choose letter [x,o]
turn_user = input("Enter the letter ['X' or 'O']: ")


# Checking for letter [x,o]
if turn_user.upper() == "X":
    turn_AI = "O"
else:
    turn_AI = "X"


# cheacking for who will GO FIRST!
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
    print(f"Turn: {turn}")

    if move == "User":
        

        board_value = int(input("Enter the Place: "))
        theboard[findPlace(board_value)] = turn
        printBoard(theboard)
        move = "AI"
        turn = turn_AI
    else:
        
        board_value_AI = randomValue()
    
        theboard[findPlace(board_value_AI)] = turn
        printBoard(theboard)

        move = "User"
        turn = turn_user
    # printBoard(theboard)

print("Done!!!")