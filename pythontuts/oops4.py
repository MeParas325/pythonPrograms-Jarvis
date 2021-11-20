class Employee:
    no_of_leaves=8
    def __init__(self, aname, asalary, arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"name is {self.name}.Salary is {self.salary} and roll is {self.role}"

    @classmethod
    def change_leaves(cls, change):
        cls.no_of_leaves = change

harry=Employee("harry",455,"Instructor")
rohan=Employee("rohan",255,"Student")

Employee.change_leaves(56)
print(harry.no_of_leaves)

harry.change_leaves(6)
print(Employee.no_of_leaves)

print(harry.no_of_leaves)
