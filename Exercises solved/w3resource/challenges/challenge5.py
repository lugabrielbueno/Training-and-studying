# Write a Python program to check if an integer is the power of another integer

def ispow(num, isintof):
    count = 0
    for x in range(1000):
        if isintof ** x == num:
           count += 1 
    return count > 0


print(ispow(9,3))
print(ispow(11,5))
print(ispow(10,1))
print(ispow(1,1))