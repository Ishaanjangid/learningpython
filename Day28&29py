import copy 

### Question 1 

# Fantisy Game Inventory 

inventory = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}

# Function to display the items of the dictionary
def displayInventory(inv):
    numItem = 0
    for k,v in inv.items():
        print(f"{v} {k}")
        numItem += v
    
    print(f"Total number of items: {numItem}")

# displayInventory(inventory)


### Question 2

### Function to remove all occurence of the element
def removeValue(lst,value):
    for i in range(lst.count(value)):
        lst.remove(value)

    return lst

# some Variable
inv = {'gold coin': 42, 'rope': 1}

loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Original Code for "Adding the items"
# it did't have the ability to "add a new key to dictionary"

# for k,v in inv.items():
#     if k in loot:                
#         print("yes!")
#         value = loot.count(k)
#         inv[k] += value 
        
#     else:
#         pass


# Modified code with adding the ability
# lst = copy.deepcopy(loot)
# print(lst)
# for k,v in inv.items():
#     if k in loot:                
#         print("yes!")
#         value = loot.count(k)
#         inv[k] += value 
#         removeValue(loot,k)
        
#     else:
#         for i in loot:
#             print(i,end= ' ')
#             value = lst.count(i)

#             inv[i] = value

# Creating Function for add to inventory  

def addToInventory(inventory,addedItems):
    for k,v in inventory.items():
        if k in addedItems:                
            print("yes!")
            value = addedItems.count(k)
            inventory[k] += value 
            addedItems = removeValue(addedItems,k)
            
        
        if k not in addedItems:
            print('no')
            for i in addedItems:
                
                value = addedItems.count(i)

                inv[i] = value

        return inventory


### This is AI helped me 
def addToInventory(inventory, addedItems):
    for k in addedItems:
        if k in inventory:
            inventory[k] += 1
        else:
            inventory[k] = 1
    return inventory
inv = {'a': 42, 'x': 1}

loot = ['a', 'b', 'a', 'a', 'b','c','c','x','X']


### Question 3

# Function to generate LIST of all possible places in a chess-Board
def chessBoardPlace():
    places = []

    for i in range(1,9):
        value = 'a' + str(i)
        places.append(value)
    
    for i in range(1,9):
        value = 'b' + str(i)
        places.append(value)
    
    for i in range(1,9):
        value = 'c' + str(i)
        places.append(value)

    for i in range(1,9):
        value = 'd' + str(i)
        places.append(value)

    for i in range(1,9):
        value = 'e' + str(i)
        places.append(value)

    for i in range(1,9):
        value = 'f' + str(i)
        places.append(value)

    for i in range(1,9):
        value = 'g' + str(i)
        places.append(value)

    for i in range(1,9):
        value = 'h' + str(i)
        places.append(value)
    
    places_new = []
    for i in places:
        places_new.append(i[1]+i[0])

    return places + places_new

# Function to generate LIST of all peices in a chess-Board
def chessBoardPiece():
    piece = []

    for i in range(8):
        piece.append('bpawn')
    
    for i in range(8):
        piece.append('wpawn')

    piece.append('bking')
    piece.append('wking')
    piece.append('bqueen')
    piece.append('wqueen')
    piece.append('brook')
    piece.append('wrook')
    piece.append('bknight')
    piece.append('wknight')
    piece.append('bbishop')
    piece.append('wbishop')
    return piece


# Function to check of the chess board is valid or not 
board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

def chessBoardValid(board):
    key = board.keys()
    value = board.values()

    for i in key:
        if i not in chessBoardPlace():
            return False
    
    for i in value:
        if i not in chessBoardPiece():
            return False
    
    return True
       
print(chessBoardValid(board))


