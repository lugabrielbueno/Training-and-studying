#Credit Card Validator - Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer) and validates it to make sure that it is a valid number (look into how credit cards use a checksum).
import math
class Validator:
    def __init__(self, flag):
        self.flag = flag    

    def luhn_alg(self):
        self.num = input('Type the number in your card: ')
        def check_flag():
            if self.flag == 'Mastercard':
                return self.num.find('51') == 0 or self.num.find('52') == 0 or self.num.find('53') == 0 or self.num.find('54') == 0 or self.num.find('55') == 0
            elif self.flag =='American Express':
                return self.num.find('37') == 0 or self.num.find('34') == 0
            elif self.flag == 'Visa':
                return self.num.find('4') == 0 
        
        if check_flag() == True:
            i = 0
            self.lis = []
            while i < len(self.num) -1:
                if i % 2 == 0:
                    n = int(self.num[i])*2
                    self.lis.append(str(n))
                else:
                    self.lis.append(int(self.num[i]))
                
                for x in self.lis:
                    if len(str(x)) == 2:
                        self.lis.remove(x)
                        x = int(x[0]) + int(x[1])
                        self.lis.insert(i,x)
                    elif x != int(x):
                        self.lis.remove(x)
                        self.lis.insert(i,int(x))
                i += 1
            return self.lis
    def check_luhn(self):
        try:
            y = sum(self.lis)
            #Algorithm of luhn
            y = abs((((y/10)-((y/10)//1))*10) - 10)
        except AttributeError:
            print('Invalid flag')
        else:    
            return math.ceil(y) == int(self.num[len(self.num)-1])

ok = Validator(input('Your flag: '))
ok.luhn_alg()
ok.check_luhn()