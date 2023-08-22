# My Take in making the BAGEL GAME :->
import random, sys

### Program 1

# def main():
#     print("The is a DECTETIVE LOGIC game.")
#     print("The AI will pass on a random 2-digit number.")
#     print("You have to guess it ;->")
#     print()
#     print('Term:\tWhat they mean')
#     print('YES:\tNumber is correct and is in correct Place.')
#     print('NO:\tNumber is correct but in incorrect Place.')
#     print('WRONG:\tNo digit is correct.')
#     print()
#     print('If I give 248 and you write 824...')
#     print('I will say: \'YES NO\'')
#     print()
#     print("You have 10 Guesses to guess the Number")

#     number = list('012345689')
#     random.shuffle(number)
#     secretNum = f"{number[0]}{number[1]}{number[2]}"


#     # Main Program Loop

#     for i in range(10):
#         guess = input('> ')
#         hint = clues(guess,secretNum)

#         print(hint)

#         if hint == 'you got it !'.lower():
#             break
        
#     print('Tnx for playing!!!')
        

# def clues(guess,secretNum):
#     # Check if the 'guess' == 'secretNum'
#     if guess == secretNum:
#         return 'you got it !'
    
#     clue = ''

#     for i in range(3):

#         if guess[i] == secretNum[i]:
#             clue += 'Yes '
        
#         elif guess[i] in secretNum:
#             clue += 'No '

#     if len(clue) == 0:
#         return 'WRONG'
#     else:
#         return clue
    

# main()


def getBirthdays(numberOfbirthdays):
    """Return a list of birthday dates."""

    birthdays = []

    for i in range(numberOfbirthdays):
        dayOfYear = random.randint(1,365)

        if dayOfYear > 334:
            month = 'Dec'
            day = dayOfYear - 334

        elif dayOfYear > 304:
            month = 'Nov'
            day = dayOfYear - 304

        elif dayOfYear > 273:
            month = 'Oct'
            day = dayOfYear - 273

        elif dayOfYear > 243:
            month = 'Sep'
            day = dayOfYear - 243

        elif dayOfYear > 212:
            month = 'Aug'
            day = dayOfYear - 212

        elif dayOfYear > 181:
            month = 'Jul'
            day = dayOfYear - 181

        elif dayOfYear > 151:
            month = 'Jun'
            day = dayOfYear - 151

        elif dayOfYear > 120:
            month = 'May'
            day = dayOfYear - 120

        elif dayOfYear > 90:
            month = 'Apr'
            day = dayOfYear - 90

        elif dayOfYear > 59:
            month = 'Mar'
            day = dayOfYear - 59
        
        elif dayOfYear > 31:
            month = 'Feb'
            day = dayOfYear - 31

        elif dayOfYear > 0 :
            month = 'Jan'
            day = dayOfYear - 0


        birthdays.append(month + str(day))

    return birthdays

def getMatch(birthdays):
    """"Returns the birthday that occurs more than once in the list."""

    # Compare each birthday to every other birthday:

    for a in range(len(birthdays)):
        for b in range(a+1,len(birthdays)):
            if birthdays[a] == birthdays[b]:

                return birthdays[a] # return the matching birthday.
            
    
# Display the intro:

print('Birthday Paradox')
print('by Ishaan Jangid \'ishaanjangid035@gmail.com\'')
print()
print('How many birthdays shall I generate? (max 100)')
response = input('> ')

if not ( 0 < int(response) <= 100):
    print('This is larger than 100.')
    exit()

numBDays = int(response)

# Generate and display the birthday:
print()
print("Hereare")





        







