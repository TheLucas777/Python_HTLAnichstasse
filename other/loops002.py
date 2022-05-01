'''
erste Hausübung - Themen: Wiederhohlungen und Schleifen (loops)
Abfrage für range(start,stop,step)
Lucas
10.01.2022
'''

#User input
start = int(input("Gib einen Startwert ein -> "))
stop = int(input("Gib einen Endwert ein -> "))
step = int(input("Gib einen Schrittwert ein -> "))

#Ausgabe
for output in range(start,stop,step):
    print(output)