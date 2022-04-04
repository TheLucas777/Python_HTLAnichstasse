'''
Game - Thema: 4 Gewinnt
Lucas
04.04.2022
'''

x_dim = 7
y_dim = 6
y = 0
player = 1
symbol = "●"
counter = x_dim * y_dim

field = [[" " for i in range(y_dim)] for j in range(x_dim)]


def show(list):
    # own loop for showing the coords
    for x in range(0, 20, 1):
        print("")
    print("")
    print("██╗  ██╗     ██████╗ ███████╗██╗    ██╗██╗███╗   ██╗███╗   ██╗████████╗")
    print("██║  ██║    ██╔════╝ ██╔════╝██║    ██║██║████╗  ██║████╗  ██║╚══██╔══╝")
    print("███████║    ██║  ███╗█████╗  ██║ █╗ ██║██║██╔██╗ ██║██╔██╗ ██║   ██║   ")
    print("╚════██║    ██║   ██║██╔══╝  ██║███╗██║██║██║╚██╗██║██║╚██╗██║   ██║   ")
    print("     ██║    ╚██████╔╝███████╗╚███╔███╔╝██║██║ ╚████║██║ ╚████║   ██║   ")
    print("     ╚═╝     ╚═════╝ ╚══════╝ ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝   ╚═╝   ")
    print("")
    for x_coords in range(x_dim):
        print(" {}".format(x_coords + 1), end="")
    print()

    for y in range(y_dim):
        for x in range(x_dim):
            print("|{}".format(list[x][y]), end='')
        print("|")

def check(x,y,field, playersymbol):
    win = 1
    down = y
    #nach unten gehen
    for z in range(down,-1,-1):
        if(field[x][z] == playersymbol):
            if(z != -1):
                win += 1
        else:
            break
    

show(field)
while (True):

    x = int(input("Reihe: ")) - 1
    if x >= x_dim or x < 0:
        print("Neben das Spielfeld werfen kann ich auch.")
        continue

    for place in range(y_dim - 1, -1, -1):
        if (field[x][place] == " "):
            y = place
            field[x][place] = symbol
            show(field)
            break
        elif (field[x][0] != " "):
            print("Die Reihe ist voll siehst du das nicht")
            break

    print(y)
    counter -= 1
    if (counter == 0):
        print("Unendschieden")
        break

    if (player == 1):
        player += 1
        symbol = "◌"
    else:
        player -= 1
        symbol = "●"
