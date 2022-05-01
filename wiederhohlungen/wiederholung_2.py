'''
Themen: Wiederhohlung_2
Lucas
17.01.2022
'''

#variables
z1 = 2          #integer
z2 = 3.412345   #float
s1 = "Hallo"    #string
b1 = True       #boolean (True/False)

#user input and output
print("Hallo z1= {} und z2 = {:.2f}".format(z1,z2))
ui = int(input("Bitte eine int Zahl eingeben: "))


#if-elif-else-statements
if(ui > 0):
    print("Dein Input ist groesser als 0")
else:
    print("Dein Input ist kleiner als 0")

#Schleifen
x = 6
while(x > 0):
    print(x)
    x = x - 1

for x in range(12,2,-2):
    print(x)

s2 = "Hallo liebe Leute!"
for buchstabe in s2:
    print(buchstabe)