# Write a Python program to check if a given positive integer is a power of four

def ispower4(num):
    count = 0
    for x in range(1000):
        if 4**x == num:
           count += 1 
    return count > 0

print(ispower4(20))
print(ispower4(16))
print(ispower4(40))