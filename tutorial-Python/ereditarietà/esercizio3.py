import math

class Forma:
    def area(self):
        pass

class Quadrato(Forma):
    def __init__(self, lato):
        self.lato = lato

    def area(self):
        return self.lato ** 2
    
class Cerchio(Forma):
    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        return math.pi * self.raggio ** 2
    
quadrato = Quadrato(5)
print(quadrato.area())

cerchio = Cerchio(5)
print(cerchio.area())