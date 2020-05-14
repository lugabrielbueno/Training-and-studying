class Transports():
    # A classe to caracterize transports
    def __init__(self, typ, model, capacity, brand):
        self.model = model
        self.capacity = capacity
        self.typ = typ
        self.brand = brand

class Car(Transports):
    def __init__(self, typ, model, capacity, brand):
        Transports.__init__(self, typ, model, capacity,brand)
        self.km_rotate = 0
        self.fuels = 0

    def road(self,distance):
        if (distance / 10) > self.fuels:
            print("You don't have enough fuel")
        else:
            self.fuels -= distance/10
            self.km_rotate += distance
            print('{} kilometers moved.'.format(str(distance)))

    def my_brand(self):
        print('I am (a)an {}.'.format(self.brand.lower()))

    def rotate(self):
        return self.km_rotate
    
    def fuel(self,quantity,typ):
        self.fuels += int(quantity)
        print('{} liters of {} stocked.'.format(str(quantity),typ))

class Airplan(Transports):
    def __init__(self, typ, model, capacity, brand):
        Transports.__init__(self,typ, model, capacity, brand)
    
    def fly(self, destin):
        print('Flying...')
        print('Welcome to {}.'.format(destin))
    
    def board_passengers(self, number):
        if number > self.capacity:
            print('There are more passengers that we support')
        else:
            print('All shipped')
    
    def my_company(self):
        print("{} it's our company".format(self.brand.title()))

class Bike(Transports):
    def __init__(self, typ, model, capacity, brand):
        Transports.__init__(self, typ, model, capacity,brand)

    def pedal(self):
        print('Pedaling')

    def my_brand(self):
        print('The brand of this bike is {}.'.format(self.brand.lower()))


car_jeta = Car('terrestrial','Jetta',5,'Volkswagen')
car_jeta.my_brand()
car_jeta.fuel(70,'alcohol')
car_jeta.road(200)
car_jeta.road(10)

tam = Airplan('air','boeing',100,'Tam')
tam.board_passengers(94)
tam.my_company()
tam.fly('Japan')
tam.board_passengers(102)

caloy = Bike('terrestrial','casual',1,'caloy')
caloy.my_brand()
caloy.pedal()