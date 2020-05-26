#Write a python program to call an external command in Python

from os import system

com = system(input('Type the command: '))

print(com)