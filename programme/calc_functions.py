'''
Simple calculator functions
Lucas
09.05.2021
'''

import colorama

# adds two numbers
def add(x, y):
    return x + y


# subtracts two numbers
def subtract(x, y):
    return x - y


# multiplies two numbers
def multiply(x, y):
    return x * y


# divides two numbers
def divide(x, y):
    return x / y


while (True):
    for i in range(30):
        print("")
    print("")
    print(colorama.Fore.GREEN+" ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ ")
    print("██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗")
    print("██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝")
    print("██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗")
    print("╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║")
    print(" ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝")
    print("")

    z1 = input(colorama.Fore.CYAN+"Enter your first number : ")
    calc = input("Enter your operator(+ - / *): ")
    z2 = input("Enter your second number: ")

    if z1 == "end" or z2 == "end" or calc == "end":
        break

    try:
        z1_cast = float(z1)
    except ValueError:
        print(colorama.Fore.RED+"Your first number is not a number")

    if calc != "+" and calc != "-" and calc != "/" and calc != "*":
        print(colorama.Fore.RED+"Your operator is not valid")

    try:
        z2_cast = float(z2)
    except ValueError:
        print(colorama.Fore.RED+"Your second number is not a number")


    if calc == "+":
        print(colorama.Fore.CYAN+z1, " ", calc, " ", z2, " = ", add(float(z1), float(z2)))
    elif calc == "-":
        print(colorama.Fore.CYAN+z1, " ", calc, " ", z2, " = ", subtract(float(z1), float(z2)))
    elif calc == "/":
        print(colorama.Fore.CYAN+z1, " ", calc, " ", z2, " = ", divide(float(z1), float(z2)))
    elif calc == "*":
        print(colorama.Fore.CYAN+z1, " ", calc, " ", z2, " = ", multiply(float(z1), float(z2)))

    print("")
    input(colorama.Fore.WHITE+"Press enter to continue...")