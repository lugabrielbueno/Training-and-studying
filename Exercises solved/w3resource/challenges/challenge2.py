# Write a Python program to check if a given positive integer is a power of three

def ispower3(num):
    count = 0
    for x in range(1000):
        if 3**x == num:
           count += 1 
    return count > 0
print(ispower3(9))
print(ispower3(15))
print(ispower3(20))