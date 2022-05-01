'''
Themen: Wiederhohlung_4
Lucas
28.02.2022
'''

# Asks for a Number and sends the type
ui_str = input("Gib hier eine Zahl ein: ")
print("ui_str hat den daten-typ {}".format(type(ui_str)))

#converts the input to a int and sends the type
ui_int = int(ui_str)
print("ui_int hat den daten-typ {}".format(type(ui_int)))

#checks if the converted input is positiv, negativ or null
if(ui_int < 0):
    print("ui_int ist negativ")
elif(ui_int > 0):
    print("ui_int ist positiv")
else:
    print("ui_int ist NULL")

#Sends all numbers until the converted input is 0
while(ui_int >= 0):
    print(ui_int)
    ui_int = ui_int - 1

#Spells a sentence
ui2 = input("Gib einen Satz ein: ")

for z in ui2:
    print(z)

#Sends everything from my_second_list
my_empty_list = []
my_second_list = ["hallo", "Logi", 10, 13.456]

for eintrag in my_second_list:
    print(eintrag)

#sends the second statement from my_second_list
print(my_second_list[1])