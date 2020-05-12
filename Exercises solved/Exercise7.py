# Create an array based on a input of 2 number 
# The first number refers to lines and the second to columns

# Import the module numpy
import numpy as np

# Receiving the numbers
Z = input('Type the dimensions of the array: ')

# Spliting to make easy
Z = Z.split(',')

#Expression that make a str turn a int
Z = list(map(lambda x: int(x),Z))

# Creating the array
arr = np.random.randint(0,20,(Z[0],Z[1]))
print(arr)