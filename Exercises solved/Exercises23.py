#Write a Python function to check whether a string is pangram or not.

#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : "The quick brown fox jumps over the lazy dog"

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    for x,letter in enumerate(alphabet):
        if letter not in str1.lower():
            return False
        else:
            if x < len(alphabet)-1:
                continue
            return True
