# Write a Python program to calculate the hypotenuse of a right angled triangle

from math import sqrt

def hipotenuse(c1,c2):
    return round(sqrt((c1**2)+(c2**2)),3)

print(hipotenuse(2.5,3))