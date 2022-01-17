'''
drittes Übungsfile - Themen: User I/O und Verzweigungen
Vorbereitung Taschenrechner HÜ
Lucas
20.12.2021
'''

#als erstes den user nach zahlen und operator fragen
z1 = input("Bitte deine erste Zahl eingeben --> ")
z1 = float(z1)

op = input("Bitte deinen Operator(+, -, *, /) eingeben --> ")

z2 = float(input("Bitte deine zweite Zahl eingeben --> "))

erg = 0.00
#if verzweigung
if (op == "+"):
    #dieser Block wird nur ausgeführt wenn das IF-Statement
    # WAHR ist
    erg = z1 + z2

    # Das Ergebnis wird hier ausgegeben
    print("Das Ergebnis = {:.2f}".format(erg))


elif (op == "-"):
    erg = z1 - z2

    # Das Ergebnis wird hier ausgegeben
    print("Das Ergebnis = {:.2f}".format(erg))


elif (op == "*"):
    erg = z1 * z2

    # Das Ergebnis wird hier ausgegeben
    print("Das Ergebnis = {:.2f}".format(erg))


elif (op == "/"):
    erg = z1 / z2

    # Das Ergebnis wird hier ausgegeben
    print("Das Ergebnis = {:.2f}".format(erg))

elif (op == "lorenz"):
    #EASTEREGG
    print("Lorenz is a Lapp")
else:
    # Wird ausgeführt wenn kein valider operator eingegeben wurde
    print(" ")
    print(" ")
    print(" ")
    print("[ERROR]Bitte gib einen validen Operator ein wie : +, -, *, /")
    print(" ")
    print(" ")
    print(" ")