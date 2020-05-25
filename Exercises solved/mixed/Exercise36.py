#Check if Palindrome - Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”

strin = input("Text: ").lower()
print(strin)
print(strin[::-1] == strin.lower())