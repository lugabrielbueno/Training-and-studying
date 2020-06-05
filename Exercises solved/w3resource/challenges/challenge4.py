#  Write a Python program to check if a number is a perfect square

from math import sqrt

def perfect_square(num):
    return int(sqrt(num)) == float(sqrt(num))

print(perfect_square(100))
print(perfect_square(51))
print(perfect_square(36))