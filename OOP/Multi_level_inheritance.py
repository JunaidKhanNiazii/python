class Car:

    @staticmethod
    def start ():
        print("Start the car")

    @staticmethod
    def stop():
        print("Stop the car")
    
class ToyataCar(Car):
    def __init__(self, brand):
        self.brand = brand

class frontuner (ToyataCar):
    def __init__ (self, type):
        self.type = type

car1 = frontuner("diesel")
print(car1.type)
# print(car1.brand)
print(car1.start())