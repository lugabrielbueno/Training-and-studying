#Unit Converter (temp, currency, volume, mass and more) - Converts various units between one another. The user enters the type of unit being entered, the type of unit they want to convert to and then the value. The program will then make the conversion.

class Conversor:
    def __init__(self):
        pass
    def temperature(self,get_scale,your_scale,value):
        '''
        F -> Farenheit
        K -> Kelvin
        C -> Celsius
        '''
        
        if get_scale == 'F' and your_scale == 'C':
            get_scale = 1.8*value+32
        elif get_scale == 'C' and your_scale == 'F':
            get_scale = (value-32)/1.8
        elif get_scale == 'F' and your_scale == 'K':
            get_scale = (((value*9)-2457)/5)+32
        elif get_scale == 'K' and your_scale == 'F':
            get_scale = (((value*5)-160)/9)+273
        elif get_scale == 'C' and your_scale == 'K':
            get_scale = value + 273
        elif get_scale == 'K' and your_scale == 'C':
            get_scale = value - 273
        return round(get_scale,2)

    def sizes(self,get_scale,your_scale,value):
        '''
        I -> Inch
        M -> Meter
        C -> Centimeter
        K -> Kilometer
        ML -> Miles
        '''
        if get_scale == 'I' and your_scale == 'C':
            get_scale = value/2,54
        elif get_scale == 'C' and your_scale =='I':
            get_scale = value*2.54
        elif get_scale == 'M' and your_scale ==' K':
            get_scale = value*1000
        elif get_scale == 'K' and your_scale =='M':
            get_scale = value/1000
        elif get_scale == 'K' and your_scale =='ML':
            get_scale = value*1.609
        elif get_scale == 'ML' and your_scale == 'K':
            get_scale = value/1.609
        elif get_scale =='I' and your_scale =='M':
            get_scale = value*39.37
        elif get_scale =='M' and your_scale == 'I':
            get_scale = value/39.37
        elif get_scale == 'C' and your_scale =='M':
            get_scale = value*100
        elif get_scale == 'M' and your_scale == 'I':
            get_scale = value/100
        return round(get_scale,2)

while True:
    try:
        print('1 -> Temperature\n2 -> Sizes')
        n = input('What conversion you need to do? ')
        if not n:
            break
        conv = Conversor()
        try:
            if n ==1:
                print('F -> Farenheit\nK -> Kelvin\nC -> Celsius')
                a = str(input('First tell us what scale you have: '))
                b = str(input('Now, what scale you need ? '))
                c = float(input("Finally, what's the value of the temperature that you have ?  "))
            elif n == 2:
                print('M -> Meter\nML -> Miles\nC -> Centimeter\nI -> Inch\nK -> Kilometer')
                i = str(input('First tell us what scale you have: '))
                j = str(input('Now, tell us what scale you need ? '))
                k = int(input("Finally, what's the value of the measure you have ?" ))
        except:
            print("WHOOPS! That's not a valid input")

        else:
            print(conv.temperature(a.upper(),b.upper(),c)) if n ==1 else print(conv.sizes(i,j,k))
    except :
        print("WHOOPS! That's not a valid input")