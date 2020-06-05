#Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2

def two_copies(string,n):
    if len(string) >= 2:
        return (string[0]+string[1]) * n
    else:
        return string * n

print(two_copies('gabriel',5))
print(two_copies('love', 10))
print(two_copies('O',3))