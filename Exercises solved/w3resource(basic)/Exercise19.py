#Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

def new_stirng(string):
    if string.find('Is') == 0:
        return string
    else:
        return 'Is'+string

print(new_stirng('sCheryl'))
print(new_stirng('IsCal'))
print(new_stirng('Doctor'))