#Factorial Finder - The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1. Solve this using loops

def fac(n):
    if int(n) ==0:
        return 1
    i = int(n)
    x = int(n)
    while i >1:
        x *= (i-1)
        i -= 1
    return x

while True:
    try:
        num = input('Factorial: ')
        if not num:
            break
        answer = fac(num)
    except :
        print("WHOPS! That's not a number")
    else:
        print(answer)