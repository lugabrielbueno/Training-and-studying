#Count Vowels - Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.

from collections import Counter

strin = input('Text : ')

x = Counter(strin)

print('a: '+str(x['a']))
print('e: '+str(x['e']))
print('i: '+str(x['i']))
print('o: '+str(x['o']))
print('u: '+str(x['u']))