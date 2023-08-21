import random

number = list('012345689')
random.shuffle(number)
secretNum = f"{number[0]}{number[1]}{number[2]}"

print(secretNum,type(secretNum))