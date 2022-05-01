'''
Themen: Strucktogramme
Strucktogramm: https://i.ibb.co/k9kxMDy/2Wuerfel.png
Lucas
28.02.2022
'''
import random

# initiating variables
counter = 0
dice1 = 0
dice2 = 0
augenpaare = []

while (True):
    if (dice1 != 6 or dice2 != 6):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        augenpaare.append(str(dice1) + "+" + str(dice2))
        counter = counter +1
    else:
        break
print("beide Würfel haben nach {} Versuche(n) eine 6 gewürfelt".format(counter))
print("Die vorherigen Augenpaare waren {}".format(augenpaare))
