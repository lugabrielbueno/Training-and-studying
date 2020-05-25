#Write a Python program to accept a filename from the user and print the extension of that.
import sys

n = input('File name: ')
n = n.split('.')
print('The extension of the file is '+n[1]+'.')