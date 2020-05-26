#Write a Python program to check whether a specified value is contained in a group of values.

def is_in(value,listi):
    return (value in listi)

print(is_in(4,[5,6,2,3,4,8,6,4]))
print(is_in(2,[23,22,5,4,9]))