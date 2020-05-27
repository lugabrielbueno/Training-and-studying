import unittest

class Strings:
    # A class for string workers
    def __init__(self):
        # Initialize the class Strings
        pass
        
        # A method to get a string
    def get_str(self):
        self.stir = str(input('Type a phrase: '))

        # A method to print a string in upper case
    def print_str(self):
        print(self.stir.upper())

# Creating an instance
arch = Strings()

# Calling the methods
arch.get_str()
arch.print_str()
str.split()