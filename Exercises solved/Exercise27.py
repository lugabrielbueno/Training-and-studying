#Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

n = int(input('How many numbers you want to see ? '))

def fibs(n):
    a = 1
    b = 1
    print(a)
    print(b)
    for x in range(n):
        a,b = b, a+b
        yield b
for x in fibs(n):
    print(x)