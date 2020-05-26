#Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)

from math import sqrt

def distance(x1,y1,x2,y2):
    '''
   # Calculate the distance between two points
    '''
    return round(sqrt((x2-x1)**2 +(y2-y1)**2 ),4)

print(distance(5,5,9,9))
print(distance(4,0,6,6))