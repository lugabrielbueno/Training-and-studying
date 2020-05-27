#Given a string, return a new string where the first and last chars have been exchanged.

#front_back('code') → 'eodc'
#front_back('a') → 'a'
#front_back('ab') → 'ba'

def front_back(string):
    if len(string) <=1:
        return string
    mid = string[1:len(string)-1]
    return string[len(string)-1]+mid+string[0]

print(front_back('code'))