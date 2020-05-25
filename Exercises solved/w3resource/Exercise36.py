#Write a Python program to add two objects if both objects are an integer type.

def sumint(a,b):
    if a == int(a) and b == int(b):
        return a+b
    else:
        raise TypeError('Inputs must be integers')
print(sumint(5,9))
print(sumint(7.6,4))