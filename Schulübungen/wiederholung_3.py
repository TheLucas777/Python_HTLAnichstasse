'''
Themen: Wiederhohlung_3
Lucas
24.01.2022
'''

geheim = 42
counter = 1
while (True):
    ui = int(input("{}. Versuch. Bitte eine Zahl eingeben -> ".format(counter)))
    if (ui == geheim):
        print("Du hast es nach {}. Versuchen erraten!".format(counter))
        break
    if (ui > geheim):
        print("Zahl kleiner")
        counter = counter + 1
    else:
        print("Zahl groesser")
        counter = counter + 1
