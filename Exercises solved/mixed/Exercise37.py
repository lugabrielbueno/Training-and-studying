#Count words in a string - counts the number of individual words in a string. For added complexity read these strings in from a text file.

from collections import Counter

with open('phys.txt') as ph:
    print(Counter(ph.read().split()))