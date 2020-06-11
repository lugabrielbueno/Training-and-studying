#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

import random as rn

number = rn.randint(1000,9999)
print("Guess the number of four digits")
while True:
    try:
        guess = input('What number i am thinking?')
        if not guess:
            break
        int(guess)
    except:
        print("That's not a number, try again")
    else:
        cow = 0
        bulls = 0
        i = 0
        guess = str(guess)
        number = str(number)
        for i in range(0,4):
            if guess[i] == number[i]:
                cow += 1
            elif guess[i] in number:
                bulls += 1
    break
print(str(cow)+' Cows\n'+str(bulls)+' Bulls')