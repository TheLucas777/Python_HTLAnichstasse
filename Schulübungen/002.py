'''
zweite Übungsfile - Themen: User I/O und Verzweigungen
Lucas
20.12.2021
'''


#nun startet das eigentliche Programm mit einer Frage an den User
#Datentypen: int, float, string

user_input = input("Bitte eine Zahl eingeben --> ")
user_input2 = input("Bitte noch eine Zahl eingeben --> ")

#welcher Datentyp ist user_input?                                       #DISABLED
#print("user_input ist vom Datentyp: {}".format(type(user_input)))      #DISABLED


#nun eine einfache Ausgabe mit print()                                  #DISABLED
#print("Deine Eingabe war: {}".format(user_input))                      #DISABLED

#strings addieren                                                       #DISABLED
#erg = user_input + user_input2                                         #DISABLED
#print("Erg = {}".format(erg))                                          #DISABLED

#strings in int umwandeln                                               #DISABLED
#user_input = int(user_input)                                           #DISABLED
#user_input2 = int(user_input2)                                         #DISABLED

#int addieren                                                           #DISABLED
#erg = user_input + user_input2                                         #DISABLED
#print("Erg = {}".format(erg))                                          #DISABLED

#string in float
user_input = float(user_input)
user_input2 = float(user_input2)

#float addieren
erg = user_input + user_input2
print("Erg = {:.3f}".format(erg))