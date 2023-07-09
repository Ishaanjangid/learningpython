import random 

rand_num = random.randint(1,20)
print(rand_num)

print("I am Gussing a number between [1-20]")


while True:
    user_input = int(input("Enter: "))

    if user_input < rand_num:
        print("Too low")
        continue

    if user_input > rand_num:
        print("Too high")
        continue

    if user_input == rand_num:
        break

print("Congrulation")