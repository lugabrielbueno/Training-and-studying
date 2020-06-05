# Write a Python program to check if a given positive integer is a power of two

def ispower2(num):
    count = 0
    for x in range(1000):
        if 2**x == num:
           count += 1 
    return count > 0

print(ispower2(32))
print(ispower2(50))
print(ispower2(25))