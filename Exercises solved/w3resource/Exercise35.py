# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5

def equal_or_five(a,b):
    if a+b == 5 or a-b == 5 or a ==b:
        return True
    else:
        return False

print(equal_or_five(8,8))
print(equal_or_five(15,10))
print(equal_or_five(2,3))
print(equal_or_five(12,18))
print(equal_or_five(42,5))
print(equal_or_five(15,0))
