'''
fuenftes Übungsfile - Themen: Funktionen
Funktion: Parallelwiederstandsberechnung
Lucas
24.01.2022
'''


# function for calculating r_ges
def parallelcalc(a, b):
    r_ges = a * b / (a + b)
    return r_ges


# willkommen
print("### Willkommen zum Parallel-Wiederstand-Berechnen ###")
# \u03A9 = Ω
r1 = float(input("Bitte den Wert von R1 in k\u03A9 eingeben: "))
r2 = float(input("Bitte den Wert von R2 in k\u03A9 eingeben: "))

print("Rges ist {} k\u03A9".format(parallelcalc(r1, r2)))