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
        option = input("Enter Player_1 [X,O] : ").upper()

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
    
# Function checks that space is available 
def isSpaceFree(board,move):
    if board[move] == ' ':
        return True
    else:
        return False

# Function to check is the Board is Fullor not
def isBoardFull(board):
    for i in range(1,10):
        value = isSpaceFree(board,i)

        if value:
            return False
            

    return True

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

# Function that make player Board Move
def playerBoardMove(board,move,playerLetter):
    board[move] = playerLetter

# Function that check player move [1-9]
def getplayerMove():
    while True:
        move = input("Enter move [1-9]: ")

        if move in '1 2 3 4 5 6 7 8 9'.split():
            return int(move)
        else:
            continue

# Function that ask player want to play again 
def playAgain():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')

# Function that make the copy of the Board
def makeBoardCopy():
    pass

### Main Game loop 

print("The Tic-Tak-Toe Game Start!!!")

while True:

    theBoard = [' ']*10
    # theBoard = randomLst()
    # theBoard = [' ',' ',' ',' ',' ','X',' ',' ',' ',' ']
    player_1_move,player_2_move = userInput()

    print(f"Player 1: {player_1_move}")
    print(f"Player 2: {player_2_move}")
    chance = randomChoice()
    gameIsPlaying = True

    while gameIsPlaying:

        if chance == 'player_1':
            # Player_1 Turn

            # Check if the Board is full or not
            if not isBoardFull(theBoard):
                # if 'yes' then continue the game
                print("Player 1 turn",player_1_move)
                showBoard(theBoard)
                
                move = getplayerMove()    # Player make a move
                

                if not isSpaceFree(theBoard,move):      # Check if space available
                    gameIsPlaying = False
                
                playerBoardMove(theBoard,move,player_1_move)

                if isWinner(theBoard,player_1_move):
                    showBoard(theBoard)
                    print('Player 1 Win!!!')
                    gameIsPlaying = False
                else:
                    chance = 'player_2'
                   
                
            else:
                # if 'no' game is tie and exit the game
                print("The game is a Tie")
                gameIsPlaying = False 
                  
                          
            
        else:
            # Player_2 Turn

            # check if the board is full or not
            if not isBoardFull(theBoard):
                # if 'yes' then continue the game 

                print("Player 2 turn",player_2_move)
                showBoard(theBoard)
                move = getplayerMove()


                if not isSpaceFree(theBoard,move):      # Check if space available
                    gameIsPlaying = False
                
                playerBoardMove(theBoard,move,player_2_move)

                if isWinner(theBoard,player_2_move):
                    showBoard(theBoard)
                    print('Player 2 Win!!!')
                    gameIsPlaying = False
                else:
                    chance = 'player_1'
                
            
            else:
                # if 'no' game is tie and exit the game
                print("The game is a Tie")
                gameIsPlaying = False 

    
    if not playAgain():
        
        break

print("Done")

