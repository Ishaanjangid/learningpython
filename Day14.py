# Conway game of life 

### Rules of the Game 
# Any live cell with two or more live neighbour survive
# Any dead cell with three live neighbour become a live cell
# All other live cells die in the next generation. Similarly,
# all other dead cells stay dead.

import random,time,copy

# WIDTH = 60  # Number of list
# HEIGHT= 20  # Number of element in the list

# # create a list of list foe the cells:

# nextCells = [] 

# for x in range(WIDTH):
#     column = [] # Create a new column.

#     for y in range(HEIGHT):
#         if random.randint(0,1) == 0 :
#             column.append("#") # Add aliving cell.

#         else:
#             column.append(" ") # Add a dead cell.

#     nextCells.append(column) # nextCells is a list o column lists.




# while True: # Main game loop
#     print("\n\n\n\n\n") # Seperate each step with newlines.
#     currentCells = copy.deepcopy(nextCells)

#     # Print currentCells on the screen:
#     for y in range(HEIGHT):
#         for x in range(WIDTH):
#             print(currentCells[x][y],end = "") # Print the # or space.
#         print() # Print a newline at the end of the row
    
#     time.sleep(2)

#     # Calculate the next step's cells based on current step's cells:

#     for x in range(WIDTH):
#         for y in range(HEIGHT):
#             # Get neighboring coordinates:
#             # "%WIDTH" ensure LeftCooed is always between 0 and WIDTH -1

#             leftCoord = (x-1) % WIDTH
#             rightCoord= (x+1) % WIDTH
#             aboveCoord= (y-1) % HEIGHT
#             belowCoord= (y+1) % HEIGHT


#             # Count number of living neighbors:

#             numNeighbors = 0

#             if currentCells[leftCoord][aboveCoord] == "#":
#                 numNeighbors += 1  # Top-left neighbor is alive

#             if currentCells[x][aboveCoord] == "#":
#                 numNeighbors += 1 # Top neighbor is alive.

#             if currentCells[rightCoord][aboveCoord] == "#":
#                 numNeighbors += 1 # Top-right neighbor is alive.

#             if currentCells[leftCoord][y] == '#':
#                 numNeighbors += 1 # Left neighbor is alive.

#             if currentCells[rightCoord][y] == "#":
#                 numNeighbors += 1 # Right neighbore is alive.

#             if currentCells[leftCoord][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom-Left neighbore is alive.

#             if currentCells[x][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom neighbore is alive.
            
#             if currentCells[rightCoord][belowCoord]:
#                 numNeighbors += 1 # Bottom-right neighbore is alive.


#             # Set cell based on Conway's Game of Life rues:

#             if currentCells[x][y] == "#" and (numNeighbors==2 or numNeighbors == 3):
#                 # Livingcells with 2 or 3 neighbore stay alive:
#                 nextCells[x][y] = "#"
            
#             elif currentCells[x][y] == " " and numNeighbors == 3:
#                 # Dead cells with 3 neighbore become alive:
#                 nextCells = "#"

#             else:

#                 # Everting else dies or stays dead:

#                 nextCells[x][y] = " "



#     time.sleep(1)


### Practice Question 1


# spam = [12,3,34,35,34,545,6,-56,"dvd",'vd',5.46]



# def elobrate_lst(lst):
#     if len(lst) == 0:
#         print(lst)
    
#     elif len(lst) == 1:
#         print(lst[0])
    
#     else:
#         for i in range(len(lst)-1):
#             print(lst[i],end=',')
            
#         print(f" and {lst[-1]}")
# elobrate_lst(spam)


### Practice Question 2

# numberOfStreaks = 0
# numberOfExperiment = 10000
# numberOfTosses = 100

# toss_lst = []
# headStreak = ["H","H","H","H","H","H"]
# tailStreak = ["T","T","T","T","T","T"]
# for experimentNumber in range(numberOfExperiment):
#     for tosses in range(numberOfTosses):
#         toss_lst.append(random.randint(0,1))

#     for i in range(len(toss_lst)):
#         if i == 0:
#             numberOfStreaks += 1
        
#         elif toss_lst[i] == toss_lst[i-1]:
#             numberOfStreaks += 1



# print('Chance of streak: %s%%' % (numberOfStreaks / 100))

# print(toss_lst)

### Practice Question 3


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for x in range(len(grid)):
    for y in range(x):
        print(grid[x][y],end='')
    print()