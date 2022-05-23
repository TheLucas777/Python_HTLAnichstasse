'''
Multicalc for GET
Lucas
23.05.2022
'''

def paralell(r1, r2):
    return (1/(1/r1+1/r2))

def serienschalltung(r1, r2):
    return r1+r2

def spannungsteiler(r1, r2, u_ges):
    u1 = r1 * (u_ges / (r1 + r2))
    u2 = r2 * (u_ges / (r1 + r2))
    return (u1, u2)


def stromteiler(r1, r2, i_ges):
    i1 = i_ges*((1/(1/r1+1/r2))/r1)
    i2 = i_ges*((1/(1/r1+1/r2))/r2)
    return (i1, i2)

def welcome():
    for i in range(20):
        print("")

    print("\n ██████╗ ███████╗████████╗    ██████╗ ███████╗ ██████╗██╗  ██╗███╗   ██╗███████╗██████╗ ")
    print("██╔════╝ ██╔════╝╚══██╔══╝    ██╔══██╗██╔════╝██╔════╝██║  ██║████╗  ██║██╔════╝██╔══██╗")
    print("██║  ███╗█████╗     ██║       ██████╔╝█████╗  ██║     ███████║██╔██╗ ██║█████╗  ██████╔╝")
    print("██║   ██║██╔══╝     ██║       ██╔══██╗██╔══╝  ██║     ██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗")
    print("╚██████╔╝███████╗   ██║       ██║  ██║███████╗╚██████╗██║  ██║██║ ╚████║███████╗██║  ██║")
    print(" ╚═════╝ ╚══════╝   ╚═╝       ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝\n")

    while(True):
        choose = int(input("Willst du Stromteiler (1), Spannungsteiler(2), Paralellschaltung(3) oder Serienschaltung(4) rechnen: "))
        R1 = float(input("Gib R1 in k\u03A9 ein: "))
        R2 = float(input("Gib R2 in k\u03A9 ein: "))
        if (choose == 2):
            Uges = float(input("Gib Uges in V ein: "))
            print(" \nErgebnisse:\nU1 = {}V \nU2 = {}V".format(spannungsteiler(R1, R2, Uges)[0],
                                                               spannungsteiler(R1, R2, Uges)[1]))
            break
        elif (choose == 1):
            Iges = float(input("Gib Iges in A ein: "))
            print(" \nErgebnisse:\nI1 = {}A \nU2 = {}A".format(stromteiler(R1, R2, Iges)[0], stromteiler(R1, R2, Iges)[1]))
            break
        elif (choose == 4):
            print(" \nErgebnis:\n Rges = {}".format(serienschalltung(R1,R2)))
            break
        elif (choose == 3):
            print(" \nErgebnis:\n Rges = {}".format(paralell(R1,R2)))
            break
        else:
            if (random.randint(0, 100) <= 10):
                print("Du bist behindert und kannst nicht lesen")
                continue
            else:
                print("Du kannst nur 1,2,3,4 eingeben.")
                continue

welcome()