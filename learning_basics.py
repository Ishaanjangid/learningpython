value = False


while value:
    print("Truth Value:",value)

    enter_value = input("Enter Truth Value: ")
    if enter_value.lower() == "f":
        break

print("Came Out of the loop") 

spam = 0

# if spam < 5:
#     print("Hello,world!")

#     spam += 1

while spam < 5:
    print("Hello,World!")

    spam +=1