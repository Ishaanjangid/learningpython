# Checking for the board is full or empty 


def isSpaceFree(board,move):
    if board[move] == ' ':
        return True
    else:
        return False
    

theboard = [' '] * 10 

lst = [' ',' ',' ',' ',' ','X',' ',' ',' ',' ']
# print(isSpaceFree(theboard,5)


# Function to check is the board is empty of full
def isBoardFull(board):
    for i in range(1,10):
        value = isSpaceFree(board,i)

        if value:
            return False
            

    return True

print(isBoardFull(theboard))
