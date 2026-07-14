# The purpose of the property method is that when the value update then it give the update result


class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    
    @property
    def percantage(self):
        return str ((self.phy + self.math + self.chem) // 3) + "%"


student1 = Student(12,14,13)
print(student1.percantage)  
student1.math = 20

print(student1.percantage)  # so it give the update result 


# print(student1.percantage()) this give error because it return the property mean variable not a function   
