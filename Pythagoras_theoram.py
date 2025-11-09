# WAP to implement the Pythagoras Theorem in Python using functions.

import math

def calculate_hypotenuse(a,b):
    return math.sqrt(a**2+b**2)
side1=float(input("Enter length of first side (a): "))
side2=float(input("Enter length of second side (b): "))
hypotenuse=calculate_hypotenuse(side1,side2)
print(f"The hypotenuse is: {hypotenuse}")