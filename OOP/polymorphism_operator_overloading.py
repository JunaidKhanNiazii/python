# #for this we use defender function 

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real, "i + ", self.img, "j")
    
#     def add (self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img

#         return Complex(newReal, newImg)

# number1 = Complex (1,3)
# number1.showNumber()

# number2 = Complex (4,5)
# number2.showNumber()

# number3 = number1.add(number2)

# number3.showNumber()




# now use poly morphism using Becender operator 

#for this we use defender function 

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i + ", self.img, "j")
    
    def __add__ (self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img

        return Complex(newReal, newImg)

number1 = Complex (1,3)
number1.showNumber()

number2 = Complex (4,5)
number2.showNumber()

number3 = number1 + number2

number3.showNumber()
