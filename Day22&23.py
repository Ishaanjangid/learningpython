# In this file I will create TIC-TAC-TOE using LIST.
# After sussfully failing by making using Dictionary (Which I Will Make soon)

import random

# lst = [' ','X','X','X','O','O','O','X','X','X']

def drawBoard(board):
    print(f"   |   |")
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print(f"   |   |")
    print(f'------------')
    print(f"   |   |")
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print(f"   |   |")
    print(f'------------')
    print(f"   |   |")
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print(f"   |   |")

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
        return "computer"   
    else:
        return "player"

# Function to ask player to play again
def playAgain():
    print("Do you want to play? (yes or no)")
    return input().lower().startswith('y')

# Functon to make the next move
def makeMove(board,letter,move):
    board[move] = letter

# Function check if the player is WINNER!
def isWinner(bo,le):
    return (( bo[7]==le and bo[8]==le and bo[9]==le) or # across the top
            ( bo[4]==le and bo[5]==le and bo[6]==le) or # across the middle
            ( bo[1]==le and bo[2]==le and bo[3]==le) or # across the bottom
            ( bo[7]==le and bo[4]==le and bo[1]==le) or # down the left side
            ( bo[8]==le and bo[5]==le and bo[2]==le) or # down the middle
            ( bo[9]==le and bo[6]==le and bo[3]==le) or # down the right side
            ( bo[7]==le and bo[5]==le and bo[3]==le) or # diognal
            ( bo[9]==le and bo[5]==le and bo[1]==le) # diognal
            )

# Function to duplicate the list
def getBoardCopy(board):

    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

# Function that check for empty space on the Board
def isSpaceFree(board,move):
    return board[move] == " "

# Function to let the player enter the first move
def getPlayerMove(board):
    move =' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
        print("What is your next move? (1-9)")

        move = input()
    return int(move)

# Function which guide AI to take a move
def chooseRandomMoveFromList(board,movesList):

    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    
    else:
        return None
    
# Function that Guid AI to play the game 
def getComputerMove(board, computerLetter):
    if computerLetter == "X":
        playerletter = 'O'
    else:
        playerletter = "X"

    # AI Check if it can win in one move
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy,computerLetter,i)
            if isWinner(copy,computerLetter):
                return i 
            
    
    # Check of player could win in the next move, block it
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy,playerletter,i)
            if isWinner(copy,playerletter):
                return i
            
    # Check the corner spaces are free.
    move = chooseRandomMoveFromList(board,[1,3,7,9])
    if move != None:
        return move
    
    # Check if Center space is free.
    if isSpaceFree(board,5):
        return 5
    
    # Move on one of the sides.
    return chooseRandomMoveFromList(board,[2,4,6,8])

# Function Check if the board is full 

def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
        
    return True


### The main Game START !!!

print("Welcome to Tic Tak Toe!")

while True:
    theBoard = [' ']*10

    playerLetter,computerLetter = inputPlayerLetter()

    turn = whoGoFirst()
    print(f"The {turn} will go First.")
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == "player":
            # Player trun
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard,playerLetter,move)

            if isWinner(theBoard,playerLetter):
                drawBoard(theBoard)
                print("Hooray! You have won the game!")
                gameIsPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is  a tie!")
                    break

                else:
                    turn = "computer"
        
        else:
            # Computer turn

            move = getComputerMove(theBoard,computerLetter)
            makeMove(theBoard,computerLetter,move)

            if isWinner(theBoard,computerLetter):
                drawBoard(theBoard)
                print("The Computer is beaten you! You lose.")
                gameIsPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn = "player"

    if not playAgain():
        break

















