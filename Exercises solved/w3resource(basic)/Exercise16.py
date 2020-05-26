#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference

def diff(n):
    try:
        n = int(n)
    except :
        print("WHOPS! That's not a number")
    else:
        if n >= 17:
            return (n -17 )*2
        else:
            return 17 - n
print(diff(25))
print(diff(5))
print(diff(2))