class Seven:
    def __init__(self):
        pass
    
    def divisible(self,n):
        self.n = n
        results = []
        for number in range(0,self.n):
            if number % 7 == 0:
                results.append(str(number))
        return results          

she = Seven()
a = she.divisible(300)
print(','.join(a))