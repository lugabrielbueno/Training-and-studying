#Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum

def summ(a,b,c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
    except :
        print("WHOOPS! That's not a number")
    else:
        if a == b == c:
            return (a + b+ c) *3
        else:
            return a+b+c
print(summ(2,3,5))
print(summ(58,94,3))
print(summ(0,6,7))
print(summ(5,5,5))