#Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script

words = input().split()

print('Program: '+words[0]+'\n Script: '+words[1])
print('Number of arguments: {}'.format(len(words)))
print('Arguments: {}'.format(', '.join(words[1:])))

#another solution
'''
import sys
print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))
'''