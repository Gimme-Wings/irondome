class Circle:
    pi = 3.14#class variable, applies everywhere
    def __init__(self,radius = 1):# constructor method
        self.radius = radius#set radius 1
        self.area = (radius**2)*Circle.pi#or self.pi
    def setR(self,new_rad):#always put self
        self.radius = new_rad
        self.area = new_rad**2*self.pi
    def circumeference(self):
        return self.radius*2*Circle.pi
circle1 = Circle(10)
circle2 = Circle(20)
print(circle2.circumeference())
circle2.setR(1)
print(circle2.circumeference())