#Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20

def sum_20(a,b):
    if 15<=(a+b)<=20:
        return 20
    else:
        return a+b

print(sum_20(41,21))
print(sum_20(3,11))
print(sum_20(6,12))