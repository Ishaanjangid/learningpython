import copy 

### Question 1 

# Fantisy Game Inventory 

inventory = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}



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
lst = copy.deepcopy(loot)
# print(lst)
for k,v in inv.items():
    if k in loot:                
        print("yes!")
        value = loot.count(k)
        inv[k] += value 
        removeValue(loot,k)
        
    else:
        for i in loot:
            print(i,end= ' ')
            value = lst.count(i)

            inv[i] = value
        

    
print(inv)
print(loot)


# value = loot.count('b')
# print(value)
