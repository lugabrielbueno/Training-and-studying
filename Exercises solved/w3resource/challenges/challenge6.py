# Write a Python program to find a missing number from a list

def miss(lis):
    return set(range(max(lis))).difference(lis)

print(miss([1,9,4,6,2,0,6]))
print(miss([1,5,30]))