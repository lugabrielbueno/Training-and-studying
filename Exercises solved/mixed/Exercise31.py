#Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

num = int(input('Number > 1: '))
steps = 0
while num != 1:
    if num % 2 ==0:
        num /= 2
    else:
        num = (num*3) +1
    steps +=1
print(str(steps)+' steps.')