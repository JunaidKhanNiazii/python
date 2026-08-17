# Create student class that take name and marks of 3 subjects as arguments in constructor. Then create a method to print the average 

class Student:

    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
    
    def average(self):
        average = self.sub1 + self.sub2 + self.sub3
        average = average // 3
        return average

student1 = Student("Junaid", 2 , 4, 7)
student2 = Student("Adeel", 3,8,9)

print (student1.average())
print(student2.average())


    
