import random 


### tic-tak-toe using dictionary data type 

# Creating the dictionary


theboard = {"top-L":" ","top-M":" ","top-R":" ",
            "mid-L":" ","mid-M":" ","mid-R":" ",
            "low-L":" ","low-M":" ","low-R":" "
            }


 
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

# Function check for win
# def checkWin(board):
#     # if theboard["top-L"] == theboard["top-M"] == theboard["t"]

#     if board["top-L"] == board["mid-M"] == board["low-R"]:
#         print(f"Win {theboard['top-L']}")
#         return "Win"

#     elif board["top-R"] == board["mid-M"] == board["low-L"]:
#         print(f"Win {theboard['top-R']}")
#         return "Win"

# Creating function to print the Board
def printBoard(board):
    print(f"{board['top-L']}|{board['top-M']}|{board['top-R']}")
    print("-+-+-")
    print(f"{board['mid-L']}|{board['mid-M']}|{board['mid-R']}")
    print("-+-+-")
    print(f"{board['low-L']}|{board['low-M']}|{board['low-R']}")


# Program ask player to choose (X or Y)
enter_letter = input("Choose ('X' or 'Y'): ")

if player_letter.upper() == "X" :
    computer_letter = "O"

else:
    computer_letter = "X"

# Program Randomly deside who to Go First

if random.randint(0,1) == 0:
    print("Player's Turn")
else:
    print("Computer's Turn")


# Printing the board
printBoard(theboard)

turn = "X"
for i in range(9):
    print(f"Turn: {turn}")
    board_value = int(input("Enter the Place: "))
    
    theboard[findPlace(board_value)] = turn

    if turn == "X":
        turn = "O"
    else:
        turn = "X"

    printBoard(theboard)

print("done!!!")