'''
Themen: Strucktogramme
Lucas
28.01.2022
'''

ui = int(input("Bitte eine Zahl eingeben --> "))

if (ui%2 == 0):
    aus = ui * 2
else:
    aus = ui + 1
print (aus)
'''
'''
ui = int(input("Bitte ihr Geburtsjahr eingeben --> "))

sj = False

if (ui%4 == 0): 
    if(ui%100 == 0):
        if(ui%400 == 0):
            sj = True
    else:
        sj = True

if (sj == True):
    print("Dieses Jahr ist ein Schaltjahr")
else:
    print("Dieses Jahr ist kein Schaltjahr")

x = 100
counter = 0
while (x <= 1000):
    counter = counter + x
    x = x + 1