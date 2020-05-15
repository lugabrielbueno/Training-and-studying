class Circle:
    def __init__(self,radius):
        self.radius = radius

    def circunference(self):
        return 2*(3,1415)*self.radius
    
    def area(self):
        return 2*(3,1415)*(self.radius**2)

class Triangle:
    def __init__(self,a,base,c,height):
        self.a = a
        self.b = base
        self.c = c
        self.height
# in this function we'll only classify the thiangle that can be possible to classify by your side measures
    def kind(self):
        if self.a == self.b == self.c :
            print('Equilateral triangle')
        elif (self.a**2 + self.b**2 == self.c**2) or self.a**2 + self.c**2 == self.b**2 or self.c**2 + self.b**2 == self.a**2:
            print('Right triangle')
        elif self.a ==self.b != self.c or self.a ==self.c != self.b or self.b == self.c != self.a:
            print('Isosceles triangle')
        
        def area(self):
            return (self.base*self.height)/2

        def perimeter(self):
            return (a+base+c)/2