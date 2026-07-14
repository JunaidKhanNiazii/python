class Student:

    def __init__(self, fullName):
        self.name = fullName
    def hello(self):
        print("hello :", self.name)
    
s1 = Student("junaid")
s1.hello()
