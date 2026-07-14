class Circle:
    def __init__ (self, radius):
        self.radius = radius

    @property
    def Area(self):
        # pi r square 
        return (3.14 * self.radius * self.radius)
    
    @property
    def Parimeter(self):
        return (2 * 3.14 * self.radius)
    
    def AreaShow(self):
        print("Area : ", self.Area)

    def ParimeterShow(self):
        print("ParimeterShow : ", self.Parimeter)

    
value1 = Circle(21)
value2 = Circle(6)

value1.AreaShow()
value1.ParimeterShow()
    

