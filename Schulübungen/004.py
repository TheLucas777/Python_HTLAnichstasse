'''
vierte Übungsfile - Themen: Wiederhohlungen und Schleifen (loops)
Lucas
10.01.2022
'''
import random
#while loop

#counter
x = 5
while(x != 0):
    #solange die Bedingung WAHR ist,
    #wird der code block ausgeführt
    print("Hello")

    #counter -1
    x = x -1


#loop bis user 'end' eingibt
y = 0
while(True):
    y = input("Gib etwas lustiges ein -> ")

    lustig = random.randrange(1,10)
    if(lustig <= 5):
        print("HAHAHHAHA so lustig")
    else:
        print("Neeee bei dem drückt die Cringeträne")

    if(y == "end"):
        break

z = 0
while(z != 101):
    print(" ",z,end="")
    z = z + 1



#for loop
print("")
for masi in range(100,-1,-10):
    print(masi)