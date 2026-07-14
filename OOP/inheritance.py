class car:
    @staticmethod
    def start():
        print("Start the car")

    @staticmethod
    def stop():
        print("Stop the car")

class ToyataCar(car):
    def __init__(self,name):
        self.name = name


car1 = ToyataCar("Toyata 1")

print(car1.name)
car1.start() # becuase it took all the properties of the parrent class that is public 
