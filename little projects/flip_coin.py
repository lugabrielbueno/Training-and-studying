
#Coin Flip Simulation - Write some code that simulates flipping a single coin however many times the user decides. The code should record the outcomes and count the number of tails and heads.

#import the module for make the "flippings"
import random

n = input('How many times do you want to flip ? ')
print('Flipping...')

#possibilities
coin = ['tail', 'head']

#shuffling
random.shuffle(coin)

#the counters
choic = 0
tail = 0
head = 0

#game
while choic != int(n):
    answer = random.choice(coin)
    if answer == 'tail':
        tail += 1
    else:
        head += 1
    choic += 1
print('Head : {}\nTail : {}'.format(head,tail))