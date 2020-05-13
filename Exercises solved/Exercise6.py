# Calculating with a formula

#Importing the module math
from math import sqrt,trunc

# Lets put the constants
h = 30
c = 50

#Receiving the sequence
d_list = str(input('Type a sequence of numbers: '))
d_list = d_list.split(',')

# List that will take the answer
answer = []


for d in d_list:
    # Trying attribute a integer to each element on 'd_list'
    try:
        d = int(d)
    
    # If the list have an element that's not a integer:
    except ValueError:
        print('Please, type only numbers')

    # If the attribution have sucess
    else:
        Q = sqrt((2*c*d)/h)
        answer.append(trunc(Q))

print(answer)