'''
Übungsfile - Themen: Funktionen (Quadratische gleichung loesen)
Lucas
07.03.2022
'''
#import the math library
import math


# define a function with three parameters

def solve(a, b, c):
    erg1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    erg2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    erg_tuple = (erg1, erg2)

    return erg_tuple


# normal program starts here:

print("### Welcome to quadratic solver ###")
print("Enter parameters i form of:")
print("a*x² + b*x + c = 0")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

# call solve function
erg = solve(a, b, c)
print(" ")
print("## Awnser ##")
print("erg = ",erg)
