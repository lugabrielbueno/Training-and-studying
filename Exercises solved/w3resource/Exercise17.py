#Write a Python program to test whether a number is within 100 of 1000 or 2000

def test(n):
    try:
        n = int(n)
    except :
        print("WHOOPS! That's not a number.")
    else:
        return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

print(test(120))
print(test(0))
print(test(80))
print(test(999))
print(test(1000))