'''
vierte Hausübung - Themen: Lotto
User guesses 6 numbers in range 1-45 and
if the numbers are equal to 6 random numbers than he won
With bettingsystem
Lucas
02.02.2022
'''
import random

debugMode = True
# two variables numbers guesses
numbers = []
guesses = []
counter = 1
number_count = 1

# Check how many are right
def check(list1, list2):
    right = 0

    if (debugMode):
        print("[DEBUG] Coparing l1 = {} and l2 = {}".format(list1, list2))

    for x in list1:
        if x in list2:
            right = right + 1
    return right


def calcBet(guessedNumbers, bet):
    for x in range(0, 6, 1):
        if (x == guessedNumbers):
            return ((16.6666666666667 * guessedNumbers) / 100) * bet


bettedMoney = int(input("[Lotto] Bet some money --> "))

# six random number to a list
while(number_count < 6):
    rand = random.randint(1, 45)
    if numbers.__contains__(rand):
        if(debugMode):
            print("[DEBUG] Generated one number twice !!")
    else:
        numbers.append(rand)
        number_count = number_count + 1;
        if (debugMode):
            print("[DEBUG] Generated number {} it is {}.        List: {}".format(number_count, rand, numbers))

# user guesses six numbers
for x in range(0, 6, 1):
    guesses.append(int(input("[Lotto] Please set your {}. number --> ".format(counter))))
    counter = counter + 1

# win or lose
if (check(numbers, guesses) == 6):
    print("[Lotto] You guessed EVERY number!! Congrats!")
else:
    print("[Lotto] You guessed {} number(s) right.".format(check(numbers, guesses)))
    print("[Lotto] You got {:.2f}€.".format(calcBet(check(numbers, guesses), bettedMoney)))
