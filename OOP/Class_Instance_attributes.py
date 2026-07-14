class Student:
    university = "Namal"

    def __init__(self, name , roll_no):
        self.name = name
        self.roll_no = roll_no

s1 = Student("junaid", 46)
s2 = Student("Sarfraz", 26)

print(s1.name, s1.roll_no, s1.university, Student.university)
print(s2.name, s2.roll_no, s2.university, Student.university)