#Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

n = input()
def even_odd(n):
    if n % 2 ==0:
        return str(n) +' is even'
    else:
        return str(n) +' is odd'
try:
    n = int(n)
except :
    print("WHOOPS! That's not a number")
else:
    print(even_odd(n))
