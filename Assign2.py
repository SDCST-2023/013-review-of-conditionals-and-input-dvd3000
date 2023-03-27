"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""

import math
a = 0
b = 0
c = 0
x = float(input("Enter a number 1: "))
y = float(input("Enter a number 2: "))

v = input("Is a or b the hypotenuse of right triangle? (yes or no) ")

if v == "yes":
    #find the missing side
    a = x
    c = y
    b = math.sqrt((c ** 2) - (a ** 2))
    print(f"The missing side length is {b}")
elif v == "no":
    #find the hypotenuse
    a = x
    b = y
    c = math.sqrt((a ** 2) + (b ** 2))
    print(f"The missing side length is {c}")
else:
    print("that is a yes or no question")