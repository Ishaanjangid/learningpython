import pprint

# message  = "It was a bright cold day in April, and thw clocks were striking thirteen."
# # message = "ABCDEAAA"
# count = {}

# for character in message:
#     count.setdefault(character,0)
#     count[character] = count[character] + 1

# pprint.pprint(count)
    
theBoard = {"top-L":" " , "top-M":" " , "top-R":" ",
            "mid-L":" " , "mid-M":" " , "mid-R":" ",
            "low-L":" " , "low-M":" " , "low-R":" "}

def printBoard(board):
    print(board['top-L'] + "|" + board['top-M'] + "|" + board["top-R"])
    print("-+-+-")
    print(board['mid-L'] + "|" + board['mid-M'] + "|" + board["mid-R"])
    print("-+-+-")
    print(board['low-L'] + "|" + board['low-M'] + "|" + board["low-R"])


turn = "X"
for i in range(9):
    printBoard(theBoard)
    print(f"Turn for {turn}. Move on which space?")
    move = input()
    theBoard[move] = turn

    if turn == "X":
        turn = "O"

    else:
        turn = "X"

printBoard(theBoard)