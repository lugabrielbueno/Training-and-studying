class American():
    #A class to define americans
    def __init__(self,name,state,city,age,candidate):
        self.name = name
        self.state = state
        self.city = city
        self.age = age
        self.candidate = candidate

class NewYorker(American):
    def __init__(self,name,state,city,age,candidate):
        American.__init__(self,name,state,city,age,candidate)
    
    def vote(self):
        print(self.candidate)
    
george = NewYorker('George','New York','New York city',25,'Obama')
print(george.name)
print(george.city)
print(george.candidate)
george.vote()
print(george.state)
print(george.age)