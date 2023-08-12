# yes baby back to basics 


allGuests = {'Ishaan':{'apple':5,"banana":12},
             'Aaradhya':{'ham sandwiches':3,'apple':2},
             'Rajvir':{'cups':3,"apple pies":1}}

def totalBrought(guests,item):
    numBrought = 0
    for k,v in guests.items():
        numBrought = numBrought + v.get(item,0)
    
    return numBrought

print(f'Apple {totalBrought(allGuests,"apple")}')
print(f'Banana {totalBrought(allGuests,"banana")}')
print(f'Ham Sandwiches {totalBrought(allGuests,"ham sandwiches")}')
print(f'Cups {totalBrought(allGuests,"cups")}')
print(f'Apple Pies {totalBrought(allGuests,"apple pies")}')

print()


### Question 1 

# Fantisy Game Inventory 

inventory = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}

numItem = 0

def displayInventory(inv):
    for k,v in inv.items():
        print(f"{v} {k}")
        # numItem += v.get(k,0)

displayInventory(inventory)

 

