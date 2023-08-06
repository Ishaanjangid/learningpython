# Tic-Tak-Toe my version
import random

# Function that randomly gives a list
def randomLst():
    lst = []

    for i in range(10):
        value = random.randint(0,1)
        if value == 0:
            lst.append('X')

        else:
            lst.append('O')

    return lst

# Function to input user letter [X,O]
def userInput():

    while True:
        option = input("Enter user Input: ").upper()

        if option in ['X','O']:
            if option == 'X':
                return ['X','O']
            else:
                return ['O','X']
        else:
            continue

# Function to show Board
def showBoard(board):
    print(f"  |   |")
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print(f"  |   |")
    print(f"---------")
    print(f"  |   |")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print(f"  |   |")
    print(f"---------")
    print(f"  |   |")
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print(f"  |   |")

# Function randomly decide who will Go First!
def randomChoice():
    value = random.randint(0,1)

    if value == 0:
        # Player 1 chance
        return 'player_1'
    
    else:
        return 'player_2'
    
# Function checks that is board is full or not 
def isSpaceFree(board,move):
    if board[move] == ' ':
        return True
    else:
        return False

# Function checks the move is a winning move
def isWinner(bo,le):
    return((bo[7]==le and bo[8]==le and bo[9]==le) or 
           (bo[4]==le and bo[5]==le and bo[6]==le) or
           (bo[1]==le and bo[2]==le and bo[3]==le) or
           (bo[7]==le and bo[4]==le and bo[1]==le) or
           (bo[8]==le and bo[5]==le and bo[2]==le) or
           (bo[9]==le and bo[6]==le and bo[3]==le) or
           (bo[7]==le and bo[5]==le and bo[3]==le) or
           (bo[9]==le and bo[5]==le and bo[1]==le))

# Function that make player Move
def playerMove(board,move,playerLetter):
    board[move] = playerLetter


lst = [' ']*10

showBoard(lst)
move = int(input("Enter the move: "))
playerMove(lst,move,"X")
showBoard(lst)







