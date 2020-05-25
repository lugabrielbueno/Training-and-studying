#Write a python program to find the sum of the first n positive integers.

def sumn(n):
    num = 0
    for n in range( n+1):
        num += n
    return num

print(sumn(15))
print(sumn(20))
print(sumn(54))
