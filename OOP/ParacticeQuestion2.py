class Employee:

    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print(self.role)
        print(self.department)
        print(self.salary)

class Engineer(Employee):
    def __init__(self, name, age, role, department, salary):
        self.name = name 
        self.age = age
        super().__init__(role, department, salary)

    def shows(self):
        print(self.name)
        print(self.age)


eng1 = Engineer("junaid", 12, "Engineer", "Electrical", 5000)

eng1.shows()
eng1.showDetails()
