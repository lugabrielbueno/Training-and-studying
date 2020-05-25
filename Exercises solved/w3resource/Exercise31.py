#Write a Python program to compute the greatest common divisor (GCD) of two positive integers

from math import gcd

print('Calculator of GCD.')
while True:
    try:
        a = input()
        b = input()
        if not a or not b:
            break
        answer = gcd(int(a),int(b))
    except :
        print("WHOOPS! That's not a number")
    else:
        print(answer)
        break