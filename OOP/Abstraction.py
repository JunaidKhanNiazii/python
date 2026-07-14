class Car:
    def __init__(self):
        self.brk = False
        self.cluck = False
        self.acl = False

    def show(self):
        if self.cluck == True & self.acl == True:
            print("Start the car")
        print("Do'nt start ")

    
    def start(self):
        self.cluck = True
        self.acl = True
        self.show()
car1 = Car()

car1.start()