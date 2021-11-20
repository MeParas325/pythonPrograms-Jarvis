class Employee:
    no_of_leaves=8

    def __init__(self, aname, asalary, arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"name is {self.name}.Salary is {self.salary} and roll is {self.role}"

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee({self.name}, {self.salary}, {self.role})"

    def __str__(self):
        return f"name is {self.name}.Salary is {self.salary} and roll is {self.role}"

emp1=Employee("Paras",344,"Hacker")
# emp2=Employee("Saras",344,"Kukur")
print(str(emp1))
print(emp1)
print(repr(emp1))
