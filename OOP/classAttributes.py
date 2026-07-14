class Person:
    def __init__(self, name, name2):
        self.name = name
        self.name2 = name2



    def changeName2(self, name2):
        self.name2 = name2

    @classmethod
    def changeName(self,name):
        self.name = name

   


obj1 = Person("Ahmad", "Ali")

obj1.changeName("Junaid")

print(obj1.name)
print(Person.name)


obj1.changeName2("khan")
print(obj1.name2)
print(Person.name2)

