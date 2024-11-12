class Dog:
    def __init__(self,breed):
        self.breed = breed
sam = Dog("lab")
frank = Dog("Huskie")
print(frank.breed)
#or
class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model
my_car = Car("Toyota","corolla")
print(f"My car is a {my_car.make} {my_car.model}")

class Drive:
    def __init__(self,make,model,year,mpg):
        self.make = make
        self.model = model
        self.year = year # the on on the left is the one that will be used in the program
        self.mpg = mpg

car1 = Drive("Toyota","corolla",1998, 33)
car2 = Drive("Nissan","Altima",2002,19)
car3 = Drive("lambo","aventador",2010,10)
print(type(car1))
print(car1.make)