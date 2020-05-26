#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero

def sumif(a,b,c):
    if a != b != c and c !=a:
        return a+b+c
    else:
        return 0
    
print(sumif(42,5,9))
print(sumif(8,8,12))
print(sumif(9,54,9))
print(sumif(87,4,9))