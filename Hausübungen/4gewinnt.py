'''
Game - Thema: 4 Gewinnt
Lucas
04.04.2022
'''

#
# Config
#
DEBUG = False                   # True: print debug messages                                    [Default: False]
Title = True                    # True: print title                                             [Default: True]
symbol_player1 = "●"            # Player 1 symbol                                               [Default: "●"]
symbol_player2 = "◌"            # Player 2 symbol                                               [Default: "◌"]
board_directly_under = False    # True: print board directly under the game (no empty lines)    [Default: False]
empty_line_between_boards = 20  # how many empty lines between boards                           [Default: 20]

language = "de"  # "de" or "en" (DEBUG stays english)

#
# Don't change anything below this line (you will regret it)
#
x_dim = 7  # x dimension of the board
y_dim = 6  # y dimension of the board
y = 0
player = 1  # player 1 starts
symbol = symbol_player1  # set symbol
counter = x_dim * y_dim  # counter for the board (0 = draw)
player_name = []  # player names

# creaing the board
field = [[" " for i in range(y_dim)] for j in range(x_dim)]

#
# prints the board, title and empty lines
#
def show(list):
    # empty lines
    if board_directly_under == False:
        for x in range(0, empty_line_between_boards, 1):
            print("")

    # title with ascii art
    if (Title == True):

        if language == "de":
            print("")
            print("██╗  ██╗     ██████╗ ███████╗██╗    ██╗██╗███╗   ██╗███╗   ██╗████████╗")
            print("██║  ██║    ██╔════╝ ██╔════╝██║    ██║██║████╗  ██║████╗  ██║╚══██╔══╝")
            print("███████║    ██║  ███╗█████╗  ██║ █╗ ██║██║██╔██╗ ██║██╔██╗ ██║   ██║   ")
            print("╚════██║    ██║   ██║██╔══╝  ██║███╗██║██║██║╚██╗██║██║╚██╗██║   ██║   ")
            print("     ██║    ╚██████╔╝███████╗╚███╔███╔╝██║██║ ╚████║██║ ╚████║   ██║   ")
            print("     ╚═╝     ╚═════╝ ╚══════╝ ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝   ╚═╝   ")
            print("")

        elif language == "en":

            print("")
            print("██╗  ██╗    ██╗███╗   ██╗     █████╗     ██████╗  ██████╗ ██╗    ██╗")
            print("██║  ██║    ██║████╗  ██║    ██╔══██╗    ██╔══██╗██╔═══██╗██║    ██║")
            print("███████║    ██║██╔██╗ ██║    ███████║    ██████╔╝██║   ██║██║ █╗ ██║")
            print("╚════██║    ██║██║╚██╗██║    ██╔══██║    ██╔══██╗██║   ██║██║███╗██║")
            print("     ██║    ██║██║ ╚████║    ██║  ██║    ██║  ██║╚██████╔╝╚███╔███╔╝")
            print("     ╚═╝    ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ")
            print("")

    # prints the row numbers on top of the board
    for x_coords in range(x_dim):
        print(" {}".format(x_coords), end="")
    print()

    # prints the board
    for y in range(y_dim):

        for x in range(x_dim):
            print("|{}".format(list[x][y]), end='')

        if DEBUG:
            # shows row number on the right side of the board (only for debug)
            print("|{}".format(y))

        else:
            print("|")


#
# checks with a simple algorithm if the player can wins --> checks down, right, left, and diagonal
#
def check(x, y, field, playersymbol):
    if DEBUG:
        print("x: {} y: {}".format(x, y))  # shows the coordinates of the last move (debug only)
    win = 0

    # go down and check if there is a playersymbol if not break
    for d in range(y_dim - 1, -1, -1):
        if field[x][d] == playersymbol:
            win += 1
        else:
            break

    # shows current win (debug only)
    if DEBUG:
        print("win down: {}".format(win))
        print("")

    if win != 4:
        win = 1

    # go left and check if there is a playersymbol if not break
    for l in range(x - 1, -1, -1):
        if (field[l][y] == playersymbol):
            win += 1
        else:
            break

    # shows current win (debug only)
    if DEBUG:
        print("win left: {}".format(win))

    # go right and check if there is a playersymbol if not break
    for r in range(x + 1, x_dim, 1):
        if (field[r][y] == playersymbol):
            win += 1
        else:
            break

    # shows current win (debug only)
    if DEBUG:
        print("win right: {}".format(win))
        print("")

    # resets win because of game rules
    if win != 4:
        win = 1

    # go diagonal left up and check if there is a playersymbol if not break
    y_diag = y - 1
    for dlu in range(x - 1, -1, -1):
        if (field[dlu][y_diag] == playersymbol):
            y_diag -= 1
            win += 1
        else:
            break

    # shows current win (debug only)
    if DEBUG:
        print("win diagonal left up: {}".format(win))

    # go diagonal right down and check if there is a playersymbol if not break
    y_diag = y + 1
    for drd in range(x + 1, x_dim - 1):
        if (y_diag < y_dim):
            if (field[drd][y_diag] == playersymbol):
                y_diag += 1
                win += 1
            else:
                break
        else:
            break

    # shows current win (debug only)
    if DEBUG:
        print("win diagonal right down: {}".format(win))
        print("")

    # resets win because of game rules
    if win != 4:
        win = 1

    # go diagonal right up and check if there is a playersymbol if not break
    y_diag = y - 1
    for dru in range(x + 1, x_dim - 1):
        if (field[dru][y_diag] == playersymbol):
            y_diag -= 1
            win += 1
        else:
            break

    # shows current win (debug only)
    if DEBUG:
        print("win diagonal right up: {}".format(win))

    # go diagonal left down and check if there is a playersymbol if not break
    y_diag = y + 1
    for dld in range(x - 1, -1, -1):
        if y_diag < y_dim:
            if (field[dld][y_diag] == playersymbol):
                y_diag += 1
                win += 1
            else:
                break
        else:
            break

    # shows current win (debug only)
    if DEBUG:
        print("win diagonal left down: {}".format(win))

    return win


# Entering the player names
if language == "de":
    player_name.append(input("Spieler 1 gib deinen Namen ein: "))
    player_name.append(input("Spieler 2 gib deinen Namen ein: "))
elif language == "en":
    player_name.append(input("Player 1 enter your name: "))
    player_name.append(input("Player 2 enter your name: "))

show(field)

# Main loop
while (True):
    # Player chooses collumn
    if language == "de":
        x = int(input("{} ist an der Reihe. Gib die Zeile ein, in die du einen Stein setzen willst: ".format(player_name[player - 1]))) - 1
    elif language == "en":
        x = int(input("It's {}'s turn. Enter the row you want to insert the chip: ".format(player_name[player - 1]))) - 1

    # checks if the player chose a valid collumn
    if x >= x_dim or x < 0:
        # error if not
        if language == "de":
            print("Diese Zeile existiert nicht.")
        elif language == "en":
            print("This row does not exist.")
        continue

    # checks if the player chose a collumn that is already full or places chip at the lowest possible position
    for place in range(y_dim - 1, -1, -1):
        if (field[x][place] == " "):
            y = place
            field[x][place] = symbol
            show(field)
            break

        elif (field[x][0] != " "):
            if language == "de":
                print("Die Reihe ist voll!")
            elif language == "en":
                print("The Row is full!")
            break

    # checks if the player won (wich check() function)
    if (check(x, y, field, symbol) == 4):

        if language == "de":
            print("{} hat gewonnen!".format(player_name[player - 1]))

        elif language == "en":
            print("{} won!".format(player_name[player - 1]))

        break

    # checks for a draw
    counter -= 1
    if (counter == 0):

        if language == "de":
            print("Das Spiel ist unentschieden!")

        elif language == "en":
            print("The game is a draw!")
        break

    # switches player
    if (player == 1):

        player += 1
        symbol = symbol_player2

    else:

        player -= 1
        symbol = symbol_player1
