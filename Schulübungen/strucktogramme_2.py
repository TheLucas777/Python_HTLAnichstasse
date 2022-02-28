'''
Themen: Strucktogramme
Strucktogramm: https://i.ibb.co/YLyPXJQ/Untitled-2022-02-28-0845-1.png
Lucas
28.02.2022
'''

import random

counter = 1
dice = random.randint(1,6)
while(dice != 6):
    dice = random.randint(1,6)
    counter = counter + 1
print(counter)