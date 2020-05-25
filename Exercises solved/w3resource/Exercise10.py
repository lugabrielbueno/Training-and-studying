#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

while True:
    try:
        n = input('Type a number: ')
        if not n:
            break
        n = float(n)
    except :
        print("WHOOPS! That's not a number")
    else:
        print(n+(n+n)+(n+n+n))
        break