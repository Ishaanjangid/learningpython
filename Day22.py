# In this file I will create TIC-TAC-TOE using LIST.
# After sussfully failing by making using Dictionary (Which I Will Make soon)

import random

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
    
lst = [' ','X','X','X','O','O','O','X','X','X']

drawBoard(lst)
