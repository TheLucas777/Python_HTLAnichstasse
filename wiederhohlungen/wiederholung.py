'''
Themen: Wiederhohlung
Lucas
10.01.2022
'''

#eins = 12          #DISABLED
#zwei = 2.3456      #DISABLED
#drei = "Helo123"   #DISABLED
#vier = False       #DISABLED

#User output input
#print("Guten Morgen 1BHEL")                             #DISABLES
#print("Der Wert von zwei = ",zwei)                      #DISABLES
#print("zwei = {:.2f} und drei = {}".format(zwei,drei))  #DISABLES

#fuenf = input("Bitte eine Zahl eingeben -> ")  #DISABES
#print("fuenf hat den datentyp: ",type(fuenf))  #DISABES
#fuenf = float(fuenf)                           #DISABES
#print("fuenf hat den datentyp: ",type(fuenf))  #DISABES

#if (eins > 10):                         #DISABLED
#    print("eins ist groesser als 10")   #DISABLED
#else:                                   #DISABLED
#    print("eins ist kleiner als 10")    #DISABLED

x = float(input("Bitte eine Zahl(0-100) eingeben -> "))

if (x <= 33):
    print("Deine Eingabe war kleiner gleich 33")
elif (x <= 66):
    print("Deine Eingabe war zwischen 34 und 66")
elif(x <= 100):
    print("Deine Eingabe war zwischen 67 und 100")
else:
    print("Deine Eingabe war nicht zwischen 0 und 100")