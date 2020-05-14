class Animals():
    # A class to define animals
        def __init__(self,family, alimentation):
           
           # Here are some of attributes that an animal have
            self.family = family
            self.alimentation = alimentation

class Elefants(Animals):
    def __init__(self, family, alimentation):
        Animals.__init__( self,family, alimentation)

    def walk(self):
        print('We are elefants and we walk step by step carefuly.')
    
    def sound(self,name):
        print('Hey, my name is {}. HOOOWWWLLLL!'.format(name))

    def eat(self):
        print("{}'s  eat plants".format(self.alimentation.title()))

    def reproduct(self):
        print("The {}'s get pregnant and have gestation like humans".format(self.family.lower()))

joe = Elefants('mammal','herbivor')
joe.sound('Joe')
joe.walk()
joe.eat()
joe.reproduct()

class Lions(Animals):
    def __init__(self, family, alimentation):
        Animals.__init__(self,family, alimentation)

    def walk(self):
        ('Lions run, but not so fast')

    def sound(self,name):
        print('I am {} ROOAAARRR !'.format(name))

    def eat(self):
        print("{}'s eat meat".format(self.alimentation.title()) )

    def reproduct(self):
        print("The {}'s get pregnant and have gestation like humans".format(self.family.lower()))

fred = Lions('mammal','carnivore')
fred.sound('Joe')
fred.walk()
fred.eat()
fred.reproduct()

class Vipers(Animals):
    def __init__(self,family,alimentation):
        Animals.__init__(self,family,alimentation)

    def walk(self):
        ('Vipers crawl, be careful')

    def sound(self,name):
        print('I am {} SSSSSSS !'.format(name))

    def eat(self):
        print("{}'s eat meat and eggs".format(self.alimentation.title()) )

    def reproduct(self):
        print("The {}'s lay eggs".format(self.family.lower()))

celest = Vipers('oviparous','carnivor',)
celest.sound('Celest')
celest.walk()
celest.eat()
celest.reproduct()