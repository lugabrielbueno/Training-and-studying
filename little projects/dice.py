import random,sys

class Dice:
    def __init__(self,sides,dice_number ):
        self.sides =sides
        self.dice_number = dice_number

    def play(self):
        while True:
            for x in range(self.dice_number):
                print(random.randint(1,self.sides))
            sair = input('Do you want keep playing ?  (y/n)')
            if sair == 'n':
                sys.exit()


while True:
    try:
        sds = input('Sides of dice: ')
        dc_nm = input('Number of dices that you want: ')
        if not sds or not dc_nm:
            break
        sides = int(sds)
        dice_number = int(dc_nm)
    except :
        print('Invalid input,try again')
    else:
        dado = Dice(sides,dice_number)
        dado.play()

