'''
neunte Übungsfile - Themen: 2D Listen
Lucas
14.03.2022
'''


x_dim = 3
y_dim = 3
counter = x_dim * y_dim
player = 1
symbol = "X"
player_name = []

def show(list):
    # own loop for showing the coords
    for x in range(0,20,1):
        print("")
    print("")
    print("████████╗██╗ ██████╗████████╗ █████╗  ██████╗████████╗ ██████╗ ███████╗")
    print("╚══██╔══╝██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔════╝")
    print("   ██║   ██║██║        ██║   ███████║██║        ██║   ██║   ██║█████╗  ")
    print("   ██║   ██║██║        ██║   ██╔══██║██║        ██║   ██║   ██║██╔══╝  ")
    print("   ██║   ██║╚██████╗   ██║   ██║  ██║╚██████╗   ██║   ╚██████╔╝███████╗")
    print("   ╚═╝   ╚═╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚══════╝")
    print("")
    for x_coords in range(x_dim):
        print(" {}".format(x_coords + 1), end="")
    print()

    for y in range(y_dim):
        for x in range(x_dim):
            print("|{}".format(list[x][y]), end='')
        print("|", y + 1)

def check_for_win():
    for row in range(0,3,1):
        if(field[0][row] == field[1][row] == field[2][row] != " "):
            return 1
        elif(field[row][0] == field[row][1] == field[row][2] != " "):
            return 1
        elif(field[0][0] == field[1][1] == field[2][2] != " "):
            return 1
        elif(field[2][0] == field[1][1] == field[0][2] != " "):
            return 1
    return 0
# 2D Liste mit frei Einträgen
field = [[" " for i in range(y_dim)] for j in range(x_dim)]

player_name.append(input("Player 1 enter your name: "))
player_name.append(input("Player 2 enter your name: "))
show(field)

# \/ Main game loop starts here \/
while (True):

    x = int(input("{} it's your turn. Enter the X Coord here: ".format(player_name[player - 1])))
    y = int(input("{} it's your turn. Enter the Y Coord here: ".format(player_name[player - 1])))

    if (y-1) >= y_dim or (x-1) >= x_dim or (x-1) < 0 or (y-1) < 0:
        print("Are you fucking dumm you idiot. In Germany we say: \"Warst du in Mathe Kreide holn oder was!\"")
        continue

    else:
        # if coords are on the field
        # check if field is still free
        if (field[x - 1][y - 1] == " "):
            field[x - 1][y - 1] = symbol
            show(field)

        else:
            print("Are you fucking dumm you ugly bastard. You can't erase the other Players marker!!")
            continue
        counter -= 1
        if(counter == 0):
            print("It's a draw")
            break

        # if Player has 3 in a row or diagonal than return 1 else return 0
        if(check_for_win()):
            print("{} won!!".format(player_name[player - 1]))
            break

        if(player == 1):
            player += 1
            symbol = "O"
        else:
            player -= 1
            symbol = "X"
