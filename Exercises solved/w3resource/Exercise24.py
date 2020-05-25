#Write a Python program to test whether a passed letter is a vowel or no

def isvowel(letter):
    vowels = 'aeiou'
    if letter.lower() in vowels:
        return True
    else:
        return False

print(isvowel('a'))
print(isvowel('c'))
print(isvowel('84'))