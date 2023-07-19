# Conway's Game of Life

import random,time,copy

WIDTH = 60
HEIGHT = 20

# Create a list of list foe the cells:

nextCells = []

for x in range(WIDTH):
    column = [] # Create a new column.
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append("#")  #Add a living cell.

        else:
            column.append(" ") # Add a dead cell.

        nextCells.append(column) # nextCells is a list of column lists

while True:   # Main Program Loop
    print("\n\n\n\n\n")  # Seprate each step with newlines

    currentCells = copy.deepcopy(nextCells)


    # Print currentCells on the screen:

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y],end = '') # Print the # or space

        print() # print a new line at the end of the row


    # calculate the next step's cells based on the current step's cells:

    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates:
            # '5 WIDTH' ensure leftCoord is always between 0 and WIDTH - 1

            leftCoord  = (x-1) % WIDTH
            rightCoord = (x+1) % WIDTH
            aboveCoord = (y-1) % HEIGHT
            belowCoord = (y+1) % HEIGHT


            # Count number of living neighbors:

            numNeighbors = 0

            if currentCells[leftCoord][aboveCoord] == "#":
                numNeighbors += 1 # Top-left neighbor is alive.
            
            if currentCells[x][aboveCoord] == "#":
                numNeighbors += 1 # Top neighbor is alive.

            if currentCells[rightCoord][aboveCoord] == "#":
                numNeighbors += 1 # Top-right neighbor is alive.

            if currentCells[leftCoord][y] == "#":
                numNeighbors += 1 # Left neighbor is alive.

            if currentCells[rightCoord][y] == "#":
                numNeighbors += 1 # Right neighbor is alive.

            if currentCells[leftCoord][belowCoord] == "#":
                numNeighbors += 1 # Bottem-left neighbor is alive.

            if currentCells[x][belowCoord] == "#":
                numNeighbors += 1 # Bottem neighbor is alive.

            if currentCells[rightCoord][belowCoord] == "#":
                numNeighbors += 1 # Bottem-right neighbor is alive.

            # Set cell based on Conway's Game of life rules:

            if currentCells[x][y] == "#" and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = "#"

            elif currentCells[x][y] == " " and numNeighbors == 3:
                # dead cells with 3 neighbors become alive:
                nextCells[x][y] = "#"

            else:
                # Everthing stay dies or stays dead:

                nextCells[x][y] = ' '
            

    time.sleep(1) # Add a 1-second pause to reduce flickering.




